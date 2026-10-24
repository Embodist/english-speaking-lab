# Docker Swarm 部署

> 当前决策：**CPU-only**，暂不部署 Swarm/GPU。GPU 镜像与 stack 作为备选保留；理由与切换条件见 [[deploy/ADR-001-cpu-first|ADR-001]]。

把统一服务（OpenPronounce + Piper + Whisper/Vosk + 统一网页）部署成 Swarm 服务。模型权重从 RustFS/S3 拉取，避免把 2.6GB 打进镜像。

```text
RustFS (english-lab/rustfs/english-lab/models/models.tar)
        │  rclone（容器启动时）
        ▼
lab-models volume  /models
        │
        ▼
Swarm service: lab (uvicorn lab_server:app)
        │  :8000
        ├─ /        OpenPronounce 原生界面
        └─ /lab     统一页（TTS + 录音 + 发音 + Whisper/Vosk）
```

## 前提

- Docker Engine + Swarm 可用（`docker info`、`docker node ls` 正常）。
- RustFS/S3 可达，且已上传 `models.tar` 和 `models.tar.sha256`。
- 单节点 Swarm 默认把服务放在 manager；多节点见第 7 节。
- 当前 RustFS 默认凭据较弱，**先修改凭据**再用 Docker secrets。

## 1. 上传模型权重

```bash
cd ~/english/english-speaking-lab
cp deploy/rustfs.env.example deploy/rustfs.env
# 编辑 deploy/rustfs.env：endpoint / bucket / prefix

source deploy/rustfs.env
export RUSTFS_ACCESS_KEY='...'
export RUSTFS_SECRET_KEY='...'
bash scripts/upload-weights.sh
```

上传目标默认为 `english-lab/rustfs/english-lab/models/`，包含：

- `models.tar`（约 2.6GB，含 HF/Piper/Whisper/Vosk）
- `models.tar.sha256`（相对文件名，供容器校验）

> 2026-10-24 实测：`storage1` 桶首次整包上传返回 503/timeout；改用 16M 分片后成功。`rustfs` 作为桶名被 RustFS 判为非法，因此另建了 `english-lab` 桶。两处内容一致；默认建议用 `english-lab`，需要时设置 `RUSTFS_BUCKET=storage1`。上传结果与校验值见 [[deploy/upload-status|RustFS 权重上传记录]]。

模型前缀已配置公共读（只读、只限 `rustfs/english-lab/models/*`），见 [[deploy/RUSTFS-PUBLIC-READ|RustFS 模型公共读]]。

> endpoint 是 Windows 上 RustFS 的 S3 地址。WSL 里可用 `http://<Windows-IP>:9000`；Windows IP 会变化，用 `ipconfig` 确认。

## 2. 构建镜像

```bash
cd ~/english/english-speaking-lab
docker build -f deploy/Dockerfile -t english-lab:latest .
```

多节点需要推送到 registry：

```bash
docker tag english-lab:latest registry.example.com/english-lab:latest
docker push registry.example.com/english-lab:latest
export LAB_IMAGE=registry.example.com/english-lab:latest
```

## 3. 初始化 Swarm

```bash
docker swarm init --advertise-addr <本机IP>
# 已初始化会报错，可忽略
```

WSL 中需要 Docker daemon 运行；Docker Desktop 用户请在设置中启用对应 WSL 集成。

## 4. 创建 RustFS secrets

不要把密钥写进 compose 或镜像。用文件或 stdin：

```bash
# 方式 A：从文件读取（推荐，避免 shell history）
docker secret create rustfs_access_key /path/to/access_key.txt
docker secret create rustfs_secret_key /path/to/secret_key.txt

# 方式 B：stdin
printf '%s' "$RUSTFS_ACCESS_KEY" | docker secret create rustfs_access_key -
printf '%s' "$RUSTFS_SECRET_KEY" | docker secret create rustfs_secret_key -
```

## 5. 部署

```bash
cd ~/english/english-speaking-lab
source deploy/rustfs.env
docker stack deploy -c deploy/swarm-stack.yml englishlab
```

## 6. 验证

```bash
docker stack services englishlab
docker service logs -f englishlab_lab
curl http://localhost:8000/health
```

打开：

- 统一页：<http://localhost:8000/lab>
- 原生页：<http://localhost:8000/>

首次启动会从 RustFS 下载 2.6GB 并解压，`start_period` 设为 120 秒；慢网络下会先 unhealthy，等同步完成即可。

## 7. GPU 部署（备选，当前未启用）

本机有 NVIDIA Quadro P1000（4GB VRAM），WSL 的 `nvidia-smi` 正常，但当前 PyTorch 是 CPU 版。GPU 镜像使用 CUDA 基础镜像，单独构建：

```bash
docker build -f deploy/Dockerfile.gpu -t english-lab-gpu:latest .
```

> 基础镜像为 `pytorch/pytorch:2.6.0-cuda12.4-cudnn9-runtime`。若该 tag 在你所在网络/架构不可用，换成同系列 CUDA runtime tag（例如 `2.5.1-cuda12.4-cudnn9-runtime`），并确认 `python -c "import torch; print(torch.version.cuda)"` 非空。

前提：

- Windows NVIDIA 驱动 + WSL2 GPU 支持（`nvidia-smi` 正常）。
- Docker 主机安装 `nvidia-container-toolkit`，Docker 能识别 GPU：
  ```bash
  docker run --rm --gpus all nvidia/cuda:12.4.0-base-ubuntu22.04 nvidia-smi
  ```
- **Swarm 节点使用 NVIDIA 作为默认 runtime**（Swarm 不支持 `docker run --gpus` 那套参数）。在 GPU 节点的 `/etc/docker/daemon.json` 中配置并重启 Docker：
  ```json
  {
    "default-runtime": "nvidia",
    "runtimes": {
      "nvidia": { "path": "nvidia-container-runtime", "args": [] }
    }
  }
  ```
- Swarm 节点打标签（GPU stack 用标签调度）：
  ```bash
  docker node update --label-add gpu=true $(docker node ls -q | head -1)
  ```
- 可选：让 Swarm 感知 GPU 资源（硬性调度）：
  ```bash
  docker node update --generic-resource-add nvidia.com/gpu=1 <node>
  ```
  然后在 `swarm-stack.gpu.yml` 的 `deploy.resources.reservations` 下加入
  `generic_resources: [{discrete_resource_spec: {kind: "nvidia.com/gpu", value: 1}}]`。

部署 GPU stack：

```bash
docker stack deploy -c deploy/swarm-stack.gpu.yml englishlab-gpu
```

默认是 **混合模式**：OpenPronounce 在 CPU，Whisper 在 GPU（约 1–1.5 GB 显存），适合 4GB 的 P1000。其他模式：

| 模式 | 环境变量 | 显存 | 适用 |
|---|---|---|---|
| 混合（默认） | `OPENPRONOUNCE_DEVICE=cpu`、`WHISPER_DEVICE=cuda` | ~1–1.5 GB | P1000 4GB |
| 发音 GPU | `OPENPRONOUNCE_DEVICE=cuda`、`WHISPER_DEVICE=cpu` | ~2.5–3 GB | 4GB 卡上限 |
| 全 GPU | 两者都 `cuda` | ≥8 GB | 大显存卡 |

注意：

- P1000 是 Pascal，FP16 很慢，默认 `WHISPER_FP16=0`。
- 4GB 显存不要同时把两个 Wav2Vec2 和 Whisper 都放 GPU。
- 资源预算见 [[deploy/RESOURCE-PLAN|资源占用规划]]。

## 8. 多节点

当前 stack 假设单节点：

- `lab-models` 是本地卷，每个节点首次启动会各自从 RustFS 同步。
- `lab-reports`、`lab-attachments` 也是本地卷，不会跨节点共享；多节点请改用 NFS/CephFS，或把报告/录音放对象存储。
- 每个副本约占 3–6GB 内存（OpenPronounce + Whisper/Vosk），默认 1 副本。
- 多节点时删除 `node.role == manager` 约束，或改成带标签的节点：
  ```yaml
  placement:
    constraints:
      - node.labels.english-lab == true
  ```

## 9. 更新与回滚

```bash
docker build -f deploy/Dockerfile -t english-lab:v2 .
LAB_IMAGE=english-lab:v2 docker stack deploy -c deploy/swarm-stack.yml englishlab
# 回滚
docker service rollback englishlab_lab
```

## 10. 部署前检查

```bash
bash deploy/validate.sh
```

它会检查：

- 两个 stack 的 YAML 与 `docker compose config`
- `entrypoint.sh` / 上传脚本的 shell 语法
- Python 脚本语法
- Dockerfile、lab 页面、入口脚本是否存在
- Docker daemon 是否可用（不可用时只做静态检查）
- RustFS secrets 是否存在（daemon 可用时）

另外确认：

- [ ] `deploy/rustfs.env` 已配置 endpoint/bucket/prefix
- [ ] `docker secret` 已创建
- [ ] `/models` 卷已有模型，或 `RUSTFS_ENDPOINT` + secrets 可同步
- [ ] 8000 端口未被本地服务占用
- [ ] GPU 部署时节点有 `gpu=true` 标签且默认 runtime 为 nvidia

## 11. 常见问题

| 现象 | 原因 / 解决 |
|---|---|
| 服务反复重启 | 看 `docker service logs englishlab_lab`；多为 RustFS 下载失败或 checksum 不匹配 |
| `sha256sum: models.tar: No such file` | 上传的 `.sha256` 里是绝对路径；用 `scripts/upload-weights.sh` 重新生成相对路径 |
| 启动很慢 | 首次同步 2.6GB；观察日志 `Syncing models...` |
| 内存不足 | 提高限制或减少副本；Whisper/Vosk 与 OpenPronounce 同时加载占内存 |
| 8000 端口冲突 | 停止本机 `start-web.sh`，或改 stack 的 published port |
| 无法访问 RustFS | 确认 Windows 防火墙、endpoint IP、path-style 设置 |
| `docker info` 连不上 | Docker daemon 未启动；先启动 Docker Desktop/Engine |

## 12. 安全

- RustFS 的默认凭据很弱，先修改 access/secret；不要提交到 git。
- 生产环境用 TLS endpoint，别用明文 HTTP 传模型。
- Docker secrets 只在容器内以文件形式挂载，不要 `docker service inspect` 打印。
- 报告和录音可能含个人信息；共享卷/对象存储要加访问控制。

## 相关

- [[deploy/ADR-001-cpu-first|ADR-001：CPU-first 决策]]
- [[deploy/RESOURCE-PLAN|资源占用规划]]
- [[deploy/upload-status|RustFS 权重上传记录]]
- [[deploy/RUSTFS-PUBLIC-READ|RustFS 模型公共读]]
- [[TOOLING|工具搭建与搭配]]
- [[QUICKSTART|工具体验指南]]
- [[scripts/README|脚本说明]]

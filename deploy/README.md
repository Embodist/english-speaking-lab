# Docker Swarm 部署

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

> 2026-10-24 实测：`storage1` 桶返回 503/timeout（RustFS 自身扫描/heal 报错），`rustfs` 作为桶名被 RustFS 判为非法；因此新建了 `english-lab` 桶。若 `storage1` 恢复，可设置 `RUSTFS_BUCKET=storage1` 重新上传。

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

## 7. 多节点

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

## 8. 更新与回滚

```bash
docker build -f deploy/Dockerfile -t english-lab:v2 .
LAB_IMAGE=english-lab:v2 docker stack deploy -c deploy/swarm-stack.yml englishlab
# 回滚
docker service rollback englishlab_lab
```

## 9. 常见问题

| 现象 | 原因 / 解决 |
|---|---|
| 服务反复重启 | 看 `docker service logs englishlab_lab`；多为 RustFS 下载失败或 checksum 不匹配 |
| `sha256sum: models.tar: No such file` | 上传的 `.sha256` 里是绝对路径；用 `scripts/upload-weights.sh` 重新生成相对路径 |
| 启动很慢 | 首次同步 2.6GB；观察日志 `Syncing models...` |
| 内存不足 | 提高限制或减少副本；Whisper/Vosk 与 OpenPronounce 同时加载占内存 |
| 8000 端口冲突 | 停止本机 `start-web.sh`，或改 stack 的 published port |
| 无法访问 RustFS | 确认 Windows 防火墙、endpoint IP、path-style 设置 |
| `docker info` 连不上 | Docker daemon 未启动；先启动 Docker Desktop/Engine |

## 10. 安全

- RustFS 的默认凭据很弱，先修改 access/secret；不要提交到 git。
- 生产环境用 TLS endpoint，别用明文 HTTP 传模型。
- Docker secrets 只在容器内以文件形式挂载，不要 `docker service inspect` 打印。
- 报告和录音可能含个人信息；共享卷/对象存储要加访问控制。

## 相关

- [[TOOLING|工具搭建与搭配]]
- [[QUICKSTART|工具体验指南]]
- [[scripts/README|脚本说明]]

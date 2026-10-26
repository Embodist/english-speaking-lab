---
type: guide
title: 资源占用规划
tags: [deploy, guide]
created: 2026-10-24
updated: 2026-10-24
---

# 资源占用规划

> [!important] 当前决策：发音/ASR CPU-first；翻译可选 GPU
> 发音和 ASR 继续用 CPU 本地服务；可选的中译英服务 Hy-MT2-1.8B 单独占用 GPU（1.6GB VRAM，端口 8081）。GPU 镜像与 Swarm stack 仍作为备选保留。

## 一、当前实测（2026-10-24）

| 资源 | 当前情况 |
|---|---|
| CPU | 6 线程（i7-8850H，3 核 / 6 线程） |
| 内存 | 7.8 GiB；已用 2.4 GiB；可用 5.4 GiB；Swap 4 GiB（已用 1.4 GiB） |
| 磁盘 | `/` 剩余 151 GB；`F:` 剩余 2.0 TB |
| GPU | NVIDIA Quadro P1000，**4 GB VRAM**；驱动 577.00；WSL CUDA 12.9 |
| 当前服务 | `lab_server` RSS 约 3.2 GB；翻译服务 RSS 约 0.88 GB、VRAM 1.63 GB |
| RustFS（Windows） | 进程约 653 MB；F: 数据盘 |
| 模型缓存 | HF 2.5 GB；Whisper 139 MB；Vosk 68 MB |
| 运行环境 | venv 2.6 GB；OpenPronounce 17 MB；model-bundle 2.7 GB；vault 4.9 MB |

结论：**内存和 4GB 显存是主要瓶颈**；磁盘充足。

## 二、单项占用预算

| 组件 | 内存 | 显存 | CPU | 磁盘 | 说明 |
|---|---|---|---|---|---|
| lab_server 空闲 | ~3.2 GB | 0 | <1 线程 | — | 已加载 OpenPronounce 模型 |
| OpenPronounce 分析 | +1–2 GB | 0（CPU）/ ~2.4–3 GB（GPU） | 2–4 线程 | — | 两个 Wav2Vec2 检查点 |
| Whisper base.en | +0.5–1 GB | ~1 GB | 2–3 线程 | 139 MB | CPU 约 3.6s；GPU 约 1–2s |
| Vosk small | +0.2 GB | 0 | 1 线程 | 68 MB | 约 1.4s |
| Hy-MT2-1.8B Q6_K | ~0.9 GB | 1.63 GB | 2–3 线程 | 3.2 GB | llama-server CUDA，8081，约 27 tok/s |
| Piper TTS | <0.2 GB | 0 | 短时 | 61 MB | 本地合成 |
| Docker 镜像（CPU） | — | — | — | 4–6 GB | torch CPU + 依赖 |
| Docker 镜像（GPU） | — | — | — | 10–15 GB | CUDA runtime + torch |
| 模型卷 | — | — | — | ~3 GB | `/models` 解压后 |
| RustFS 权重 | — | — | — | 5.2 GB | 两处各 2.6 GB |
| 单次模型同步 | — | — | — | 2.6 GB/节点 | 新节点/新卷首次启动 |

## 三、当前机器的推荐配置

### CPU 本地（现状）

- 1 个服务实例，1 个并发分析；不要同时跑本地服务和 Swarm 服务（都占 8000）。
- 容器限制：`cpus: 4`、`memory: 5G`、reservation 3G。
- PyTorch 线程限制：`OMP_NUM_THREADS=4`、`MKL_NUM_THREADS=4`，给系统留 2 线程。
- 目标：内存可用 ≥1 GB，Swap 使用 <1 GB；Swap 持续增长时先停掉多余服务。

### GPU 翻译（当前唯一启用的 GPU 服务）

- Hy-MT2-1.8B Q6_K，llama-server CUDA，端口 8081。
- 实测：VRAM 1.63 GB；RSS 约 0.88 GB；磁盘 3.2 GB（llama.cpp 1.8G + 模型 1.4G）；约 27 tok/s；加载约 27s。
- 剩余 VRAM 约 2.37 GB；**不要同时**跑 GPU 版 OpenPronounce/Whisper。
- `bash scripts/stop-translate.sh` 随时释放显存。

### GPU 混合（备选，当前未启用；P1000 4GB 若启用则用此模式）

- OpenPronounce 留在 CPU，Whisper 用 GPU：
  `OPENPRONOUNCE_DEVICE=cpu`、`WHISPER_DEVICE=cuda`、`WHISPER_FP16=0`。
- 显存占用约 1–1.5 GB；适合 4GB 卡。
- 收益主要在 ASR（约 3.6s → 1–2s）；发音分析仍是 CPU 时间。

### GPU 发音（可选）

- `OPENPRONOUNCE_DEVICE=cuda`、`WHISPER_DEVICE=cpu`。
- OpenPronounce 两个 Wav2Vec2 约 2.4–3 GB 显存，4GB 卡**接近上限**；不要同时把 Whisper 放 GPU。
- 收益：发音分析的 embedding 部分加速；DTW/音素对齐仍在 CPU，整体不是线性加速。

### 全 GPU（不推荐在 4GB 卡）

- `OPENPRONOUNCE_DEVICE=cuda` + `WHISPER_DEVICE=cuda`。
- 需要 ≥8 GB 显存；P1000 4GB 很可能 OOM。

### CPU / GPU 对比预期

| 任务 | CPU（当前） | GPU 混合 | 备注 |
|---|---|---|---|
| Whisper base.en | ~3.6s | ~1–2s | 收益明显 |
| Vosk | ~1.4s | 不适用 | CPU 已足够快 |
| 中译英 Hy-MT2 | — | ~4s / 27 tok/s（GPU） | 只做草稿；专名/数字核对 |
| OpenPronounce | ~8–12s | ~4–8s（若全 GPU） | DTW/对齐是 CPU 瓶颈；4GB 需谨慎 |
| 并发 | 1–2 | 1–2 | 4GB VRAM + 7.8GB RAM 限制 |

> P1000 是 Pascal（sm_61），FP16 吞吐很差；`WHISPER_FP16=0` 是有意为之，不要盲目开 FP16。

## 四、容量分级

| 级别 | 硬件 | 并发 | 部署 |
|---|---|---|---|
| T0 当前本地 | 6 线程 / 7.8 GB / P1000 4GB | 1 | 本地 venv + `start-web.sh` |
| T1 单节点 CPU Swarm | 6–8 线程 / 8–16 GB | 1–2 | 1 副本，5G 限制 |
| T2 单节点 GPU 混合 | 8–12 线程 / 16 GB / 4–8 GB VRAM | 1–2 | GPU stack，Whisper GPU |
| T3 多节点 Swarm | 每节点 8–16 GB；GPU 节点 8GB+ VRAM | 2–4 | 每节点同步模型；共享 NFS 报告/附件 |
| T4 生产 | 队列 + worker + 对象存储 | 10+ | 拆分 ASR/发音 worker，独立扩缩 |

当前机器建议停在 **T1 或 T2**；不要在同一台 7.8 GB 机器上跑多个副本。

## 五、磁盘规划

- 保留至少 **20–30 GB** 空闲。
- CPU 镜像约 4–6 GB，GPU 镜像约 10–15 GB；构建前后用 `docker system df` 检查。
- `model-bundle/models.tar` 2.7 GB：上传完成且确认远程可用后可以删除，保留则作为离线备份。
- HF 缓存 2.5 GB：**不要删**，否则重新下载。
- RustFS 两处权重 5.2 GB；F: 剩余 2.0 TB，压力不大。
- 定期清理：`docker image prune`、旧镜像 tag、旧报告/录音（按需归档）。

## 六、监控与告警建议

```bash
free -h
nvidia-smi
docker stats --no-stream
df -h / /mnt/f
du -sh ~/.cache/huggingface ~/.cache/whisper ~/english/.venv ~/english/model-bundle
curl -s http://localhost:8000/health
docker service logs -f englishlab_lab
```

| 指标 | 目标 |
|---|---|
| 可用内存 | ≥ 1 GB |
| Swap 使用 | < 1 GB，且不持续增长 |
| 显存剩余 | ≥ 512 MB |
| 磁盘剩余 | ≥ 20 GB |
| ASR p95 | CPU < 5s；GPU < 2s |
| 发音分析 p95 | CPU < 15s；GPU < 8s |
| 错误率 | < 1% |

## 七、当前建议（CPU-first）

1. **保持本地 CPU 服务**用于个人练习；不启用 GPU、不部署 Swarm（见 [[deploy/ADR-001-cpu-first|ADR-001]]）。
2. GPU 镜像与 stack 保留为备选；只有满足 ADR 里的重新评估条件（≥30% 加速、并发 >2、≥8GB VRAM 等）再切换。
3. 不要在同一台机器同时运行本地服务和 Swarm 服务（8000 端口冲突 + 内存不足）。
4. RustFS 默认凭据较弱，部署前修改；两处权重保留一份即可，另一份作备份。
5. 日常监控：`free -h`、`df -h /`、`curl localhost:8000/health`；目标是可用内存 ≥1GB、Swap <1GB。

## 相关

- [[deploy/README|Docker Swarm 部署]]
- [[deploy/upload-status|RustFS 权重上传记录]]
- [[TOOLING|工具搭建与搭配]]

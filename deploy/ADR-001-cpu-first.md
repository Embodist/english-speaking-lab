---
type: adr
title: "ADR-001：当前采用 CPU 推理"
status: accepted
date: 2026-10-24
tags: [deploy, adr]
---

# ADR-001：当前采用 CPU 推理

## 状态

已采纳（2026-10-24）。GPU 镜像与 Swarm stack 作为备选保留，暂不启用。

## 背景

- 当前机器：i7-8850H，6 线程；7.8 GiB 内存；Quadro P1000，**4 GB 显存**。
- 当前 Python 环境为 CPU 版 PyTorch（`2.14.1+cpu`），CUDA 不可用。
- Docker daemon 未运行；GPU 镜像尚未构建/实测。
- 主要负载是个人练习：5–30 秒音频，单用户，偶尔 1–2 并发。
- 实测耗时：Whisper base.en ~3.6s；Vosk ~1.4s；OpenPronounce ~8–12s。

## 决策

当前使用 **CPU-only** 的本地 `lab_server`：

- 不启用 GPU 镜像、不部署 Swarm；
- 保持 `deploy/Dockerfile.gpu` 与 `swarm-stack.gpu.yml` 作为可选方案；
- 如未来满足重新评估条件，再切换到 GPU 混合模式。

## 理由

1. **4 GB 显存太小**：OpenPronounce 两个 Wav2Vec2 检查点约 2.4 GB，再叠加 Whisper 很容易 OOM；只能做混合模式。
2. **收益不线性**：OpenPronounce 的 DTW/音素对齐仍在 CPU，GPU 主要加速 embedding；Whisper 才是明显受益项。
3. **当前延迟可接受**：个人单用户场景 8–12 秒的发音分析可以接受，不值得为此增加 CUDA、驱动、镜像和运维复杂度。
4. **环境成本**：GPU 镜像约 10–15 GB；需要 Docker daemon + `nvidia-container-toolkit`，而当前 Docker 未运行。
5. **资源紧张**：7.8 GiB 内存已出现 1.4 GiB Swap 使用；再跑容器/多副本会加剧压力。

## 资源预算（CPU 模式）

| 项目 | 预算 |
|---|---|
| 服务实例 | 1 |
| 并发分析 | 1–2 |
| CPU | 4 线程（`OMP_NUM_THREADS=4`） |
| 内存限制 | 5 GB；reservation 3 GB |
| 当前 RSS | 约 3.2 GB（空闲） |
| 显存 | 0 |
| 磁盘 | 保留 ≥20 GB |
| Swap | 目标 <1 GB，且不持续增长 |

## 后果

- Whisper 3.6s、Vosk 1.4s、OpenPronounce 8–12s；对个人练习足够。
- 不引入 CUDA 版本漂移、驱动兼容和 4GB 显存 OOM 风险。
- 多用户/高并发场景不适合当前机器，需要更多节点或 GPU。

## 重新评估条件

满足任意两条即可考虑切换 GPU：

- Docker daemon 与 `nvidia-container-toolkit` 可用，`docker run --gpus all nvidia-smi` 通过。
- 同一句录音的端到端 GPU 基准比 CPU 快 **≥30%**。
- 并发需求持续 >2，或需要批量处理论文/长音频。
- 换到 **≥8 GB VRAM** 的 GPU（可全 GPU 模式）。
- 内存升级到 16 GB 以上，能同时容纳服务与容器。

切换方式：见 [[deploy/README|Docker Swarm 部署]] 的 GPU 章节；默认先启用混合模式（OpenPronounce CPU + Whisper GPU）。

## 2026-10-26 补充：翻译模型单独用 GPU

- 发音/ASR 仍保持 CPU-first；新增**可选**中译英服务 Hy-MT2-1.8B，单独用 GPU（1.6GB VRAM，端口 8081）。
- 这不改变 CPU-first 决策，也不启用 GPU Swarm；翻译服务可随时停止，停掉即释放显存。
- 不要同时运行 GPU 版 OpenPronounce/Whisper；P1000 4GB 余量约 2.3GB。
- 详见 [[13_tech-frameworks/translation-model|Hy-MT2 翻译模型]]。

## 相关

- [[deploy/RESOURCE-PLAN|资源占用规划]]
- [[deploy/README|Docker Swarm 部署]]
- [[TOOLING|工具搭建与搭配]]

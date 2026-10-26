---
type: guide
title: 新机器安装手册
tags: [guide, meta]
created: 2026-10-24
updated: 2026-10-24
---

# 新机器安装手册

> 目标：在一台新的 WSL2（Ubuntu/Debian）机器上，用一条脚本装好 CPU 版环境，并启动统一练习页。
> 当前默认 **CPU-only**；GPU 是可选备选，见 [[deploy/README|Docker Swarm 部署]]。

## 一、一键安装

```bash
# 1) 安装 git（如果新机器没有）
sudo apt-get update && sudo apt-get install -y git

# 2) 克隆到固定路径（setup.sh 默认使用 ~/english）
git clone https://github.com/Embodist/english-speaking-lab.git ~/english/english-speaking-lab

# 3) 一键安装（系统依赖 + venv + 模型 + 自检）
cd ~/english/english-speaking-lab
bash scripts/setup.sh

# 4) 启动
bash scripts/start-web.sh
```

浏览器打开 <http://localhost:8000/lab>。

> 只装环境、暂不下载约 2.7 GB 模型：
> `SKIP_MODELS=1 bash scripts/setup.sh`

## 二、脚本做了什么

`scripts/setup.sh` 会：

1. 安装 `ffmpeg`、`espeak-ng`、`git`、`curl`、`python3-venv`；
2. 创建 `~/english/.venv`，安装 CPU 版 PyTorch；
3. 安装 `openpronounce[app]`、Piper、Whisper、Vosk；
4. 克隆 `~/english/OpenPronounce`（网页界面源码）；
5. 下载模型到缓存：
   - Piper `en_US-lessac-medium`（约 61 MB）
   - Whisper `base.en`（约 139 MB）
   - Vosk 小模型（约 68 MB）
   - OpenPronounce 两个 Wav2Vec2 检查点（约 2.5 GB）
6. 运行 `pip check` 和 `scripts/check-env.sh` 做自检。

已安装的步骤会自动跳过，可重复执行。

## 三、机器要求

| 项目 | 要求 |
|---|---|
| 系统 | WSL2 Ubuntu/Debian；原生 Linux 也可 |
| Python | 3.10+（脚本使用系统 `python3`） |
| 磁盘 | 至少 10–15 GB 空闲（模型 + venv） |
| 内存 | 建议 8 GB；CPU 模式单实例 |
| 网络 | 可访问 PyPI、GitHub；Hugging Face 走 `hf-mirror.com` |
| 麦克风 | Windows 浏览器访问 `localhost`（或用文件上传） |

## 四、验证

```bash
cd ~/english/english-speaking-lab
bash scripts/check-env.sh
bash scripts/pronounce.sh 11_attachments/reference/sample_root_cause.wav \
  "I haven't identified the root cause yet."
```

应看到 `Score`、`Transcription`、`Heard phones`，以及 `cuda: False`（CPU 模式）。

## 五、Windows 端 GUI（可选）

在 **Windows PowerShell** 中：

```powershell
winget install Obsidian.Obsidian
winget install Audacity.Audacity
winget install Anki.Anki
```

推荐用 **D: 原生镜像**，Obsidian 打开：

```text
D:\Obsidian\EnglishVault
```

首次创建（Windows 侧）：

```powershell
mkdir D:\Obsidian
git clone https://github.com/Embodist/english-speaking-lab.git D:\Obsidian\EnglishVault
```

之后在 WSL 中同步：

```bash
cd ~/english/english-speaking-lab
bash scripts/sync-windows.sh push   # WSL 修改后 → D:
bash scripts/sync-windows.sh pull   # Obsidian 修改后 → WSL
```

也可以直接用 UNC 路径打开（不推荐长期使用）：

```text
\\wsl.localhost\<发行版>\home\<用户>\english\english-speaking-lab
```

不要打开包含 `.venv`/模型的父目录，否则 Obsidian 会索引大量无关文件。

## 六、常见问题

| 现象 | 解决 |
|---|---|
| 模型下载失败 | 确认 `HF_ENDPOINT=https://hf-mirror.com`；脚本已默认设置 |
| `sudo` 不可用 | 先安装系统依赖，再 `SKIP_MODELS=1` 分步执行 |
| 端口 8000 占用 | `PORT=8001 bash scripts/start-web.sh` |
| 麦克风不可用 | 用 `http://localhost:8000/lab`（不要用 IP/HTTPS 混用）；或文件上传 |
| Python 版本过高/过低 | 使用 3.10–3.13；Kokoro 在 3.13 不可用，已用 Piper 替代 |
| 想用 GPU | 见 [[deploy/README|Docker Swarm/GPU]]；当前建议 CPU-first |

## 七、新机器上的可选组件

- **Docker Swarm + RustFS**：见 [[deploy/README|部署]]
- **GPU 推理**：见 [[deploy/README#7. GPU 部署（备选，当前未启用）|GPU 部署]]（建议 ≥8GB VRAM）
- **中译英草稿**：[[13_tech-frameworks/translation-model|Hy-MT2-1.8B + llama-server]]（4GB 显存可跑，另需约 2GB 磁盘）
- **Anki 卡组**：见 [[14_llm-papers/anki-import|论文词汇 Anki 导入]]

## 相关

- [[TOOLING|工具搭建、搭配与最佳实践]]
- [[QUICKSTART|工具体验指南]]
- [[deploy/README|Docker Swarm 部署]]

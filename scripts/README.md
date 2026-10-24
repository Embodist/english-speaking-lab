---
type: guide
title: 脚本说明
tags: [guide, meta]
created: 2026-10-23
updated: 2026-10-23
---

# 脚本说明

所有脚本都可直接从 vault 根目录运行，会自动定位 `~/english/.venv` 和 `~/english/OpenPronounce`。

| 脚本 | 作用 | 示例 |
|---|---|---|
| `setup.sh` | 从零搭建环境（可重复执行） | `bash scripts/setup.sh` |
| `check-env.sh` | 检查工具、Python 包和模型 | `bash scripts/check-env.sh` |
| `lab.sh` | 统一流水线：TTS + ASR + 发音 + 报告 | `bash scripts/lab.sh analyze a.wav "sentence"` |
| `lab_server.py` | 同源 API：`/lab`、`/lab/asr`、`/lab/save` | 由 `start-web.sh` 启动 |
| `upload-weights.sh` | 打包并上传模型权重到 RustFS | `bash scripts/upload-weights.sh` |
| `lab-web.html` | 统一网页（TTS/录音/发音/Whisper/Vosk） | 启动后打开 `/lab` |
| `start-web.sh` | 启动 OpenPronounce 网页界面 | `bash scripts/start-web.sh` |
| `pronounce.sh` | 对录音做音素级打分 | `bash scripts/pronounce.sh a.wav "sentence"` |
| `tts.sh` | 用 Piper 生成参考音 | `bash scripts/tts.sh "sentence"` |
| `asr.sh` | 转写录音，检查可懂度 | `bash scripts/asr.sh a.wav --engine vosk` |
| `new-day.sh` | 从模板生成当天记录 | `bash scripts/new-day.sh` |

## 环境变量

| 变量 | 默认值 | 用途 |
|---|---|---|
| `ENVDIR` | `~/english/.venv` | Python 虚拟环境 |
| `REPO` | `~/english/OpenPronounce` | OpenPronounce 仓库 |
| `PORT` | `8000` | 网页界面端口 |
| `HF_ENDPOINT` | `https://hf-mirror.com` | 模型下载镜像 |
| `OPENPRONOUNCE_TTS` | `piper` | 参考音后端 |
| `OPENPRONOUNCE_TTS_VOICE` | `en_US-lessac-medium` | Piper 声音 |

## 注意

- 脚本依赖路径 `~/english`，移动环境后需同步修改或设置上面的环境变量。
- 录音和模型不进 git；`.gitignore` 已排除音频。
- `start-web.sh` 会启动 `lab_server.py`，统一网页地址为 `http://localhost:8000/lab`；`/static/lab.html` 作为静态备用入口。
- `/lab/asr` 支持 `engine=whisper|vosk|both`；`/lab/save` 把报告写入 `07_review-log/reports/`。

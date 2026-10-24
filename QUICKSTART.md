---
type: guide
title: 工具体验指南
tags: [guide, skill/pronunciation]
created: 2026-10-23
updated: 2026-10-23
---

# 工具体验指南（从零到第一次录音打分）

本机环境：Debian 13（WSL2）· Python 3.13 · ffmpeg · eSpeak NG · OpenPronounce 0.3.0 · Piper TTS 1.8.0 · Whisper base.en · Vosk。

> [!info] 网络说明
> 本环境无法直连 `huggingface.co`，所有脚本已自动使用镜像 `https://hf-mirror.com`。模型下载完成后可离线使用。

> 从零搭建、工具搭配选择和最佳实践，见 [[TOOLING|工具手册]]。

## 第 0 步：自检环境

```bash
cd ~/english/english-speaking-lab
bash scripts/check-env.sh
```

应看到：

```text
ffmpeg        /usr/bin/ffmpeg
espeak-ng     /usr/bin/espeak-ng
torch         2.14.1+cpu
openpronounce 0.3.0
Piper TTS     ok
Whisper ASR   ok
Vosk ASR      ok
```

## 第 1 步：用 Obsidian 打开 vault

1. 在 Windows 资源管理器地址栏输入 `\\wsl$\`，进入你的发行版（如 `Ubuntu`）。
2. 打开 `home/user/english/english-speaking-lab`。
3. Obsidian → **Open folder as vault** → 选择该文件夹。
4. 打开 `README.md`，点击右上角图钉固定为首页。

已预置：附件目录 `11_attachments`、模板目录 `10_templates`、新笔记进入 `00_inbox`。

> 如果 Windows 无法访问 `\\wsl$`，可把 vault 复制到 `F:\English_Study\english-speaking-lab`，但工具脚本仍需在 WSL 中运行。

## 第 2 步：体验网页界面（推荐第一次用）

1. 在 WSL 终端启动服务：

   ```bash
   cd ~/english/english-speaking-lab
   bash scripts/start-web.sh
   ```

   首次启动会提示加载模型；保持终端窗口开启。

2. 在 **Windows 浏览器** 打开统一练习页：

   <http://localhost:8000/lab>

   或原生界面 <http://localhost:8000>（WSL2 会自动转发 localhost）。

   统一页里可以：生成 Piper 参考音 → 录音/上传 → 发音分析 + ASR → 下载 Markdown 报告。

3. 允许浏览器使用麦克风。

4. 在文本框输入：

   ```text
   I haven't identified the root cause yet.
   ```

5. 点击录音，正常语速读一遍，停止后提交分析。

6. 阅读结果：

   | 输出 | 含义 |
   |---|---|
   | Score | 0–100 综合分，只作线索 |
   | Transcription | 系统实际听到的句子 |
   | Heard phones | 识别出的音素序列 |
   | Mispronounced | 具体哪个词、期望音素、实际音素 |

7. 再录一次，只改一个最影响理解的词。对比两次结果。

> [!tip] 第一次分析会下载两个 Wav2Vec2 检查点（合计约 2.5 GB），较慢；之后走本地缓存。不要重复删除 `~/.cache/huggingface`。

> [!note] 录音长度
> 网页录音**最长 60 秒**，静音 2 秒自动停止；建议 **5–30 秒、1–2 句话**。上传文件和 CLI 没有显式上限，但音频越长越慢、对齐越差。麦克风不可用时，可用页面的文件上传。

## 第 3 步：体验命令行分析

如果你已有录音文件（手机录音、Windows 录音机）：

```bash
cd ~/english/english-speaking-lab

# 1) 转成兼容格式（可选，OpenPronounce 也支持 mp3/m4a/webm）
ffmpeg -i input.m4a -ar 16000 -ac 1 11_attachments/day01_intro_first-take.wav

# 2) 打分
bash scripts/pronounce.sh \
  11_attachments/day01_intro_first-take.wav \
  "I haven't identified the root cause yet."
```

预期输出：

```text
Score        : 78/100
Transcription: I haven't identified the root cause yet
Heard phones : /aɪ hævənt aɪˈdɛntɪfaɪd ðə roʊt kɔz jɛt/
Mispronounced:
  - identified: expected /aɪˈdɛntɪfaɪd/, heard /aɪˈdɛntɪfaɪ/ (confidence 72%)
```

需要完整数据（音素、韵律、每个词的时间）时加 `--json`：

```bash
bash scripts/pronounce.sh recording.wav "The main trade-off is accuracy versus latency." --json > result.json
```

## 第 4 步：生成参考音频（离线 TTS）

```bash
bash scripts/tts.sh "The main trade-off is accuracy versus latency."
# → 11_attachments/reference/the-main-trade-off-is-accuracy-versus-latency.wav

bash scripts/tts.sh "Let me make sure I understand correctly." -o 11_attachments/reference/understand.wav
```

用播放器听 2–3 遍，标出重音和停顿，再跟读。

> 默认使用 Piper 的 `en_US-lessac-medium` 声音。固定这一个声音至少两周，不要每天换。

## 第 5 步：可懂度检查（ASR）

```bash
# Whisper（默认，已下载 base.en，约 139 MB）
bash scripts/asr.sh 11_attachments/day01_intro_first-take.wav

# 或 Vosk（更轻量，需要模型；见故障排查）
bash scripts/asr.sh 11_attachments/day01_intro_first-take.wav --engine vosk
```

判断标准：**关键词、数字、否定词是否被正确识别**。ASR 识别正确不等于发音标准，但识别错误通常是重要线索。

## 第 6 步：录一段真实基线

1. 打开 [[06_interview/introduction#30 秒版本|30 秒自我介绍]]。
2. 用手机或 Windows 录音机录一遍，**一次录完，不重录到完美**。
3. 复制到 `11_attachments/day01_intro_baseline.wav`（命名规范见 [[11_attachments/_index|录音说明]]）。
4. 按第 3 步打分，把结果填进 [[07_review-log/2026-10-23|今日记录]]。
5. 听回放，只标出 **3 个最影响理解的词**。

## 每天的标准流程

```bash
cd ~/english/english-speaking-lab
bash scripts/new-day.sh                  # 1. 生成今天的记录
bash scripts/tts.sh "今天的句子"          # 2. 生成参考音
# 3. 跟读 → 录音 → 存到 11_attachments/

# 4. 一条命令跑完 TTS + ASR + 发音，并写报告/日志
bash scripts/lab.sh analyze 11_attachments/xxx.wav "句子" --engine both

# 或分步跑
bash scripts/asr.sh 11_attachments/xxx.wav            # 可懂度
bash scripts/pronounce.sh 11_attachments/xxx.wav "句子"  # 音素分析
# 6. 只改 1–2 点 → 再录 → 填记录
```

## 可选：Windows 端 GUI 工具

在 **Windows PowerShell**（不是 WSL）中安装，录音和复习体验最好：

```powershell
winget install Obsidian.Obsidian      # 打开 vault：\\wsl$\Ubuntu\home\user\english\english-speaking-lab
winget install Audacity.Audacity      # 录音、剪辑、波形对比
winget install Anki.Anki              # 间隔重复（导入方法见 08_sentence-library/anki-import-guide.md）
```

WSL 内已装好所有命令行工具；上述三个只是 GUI 补充，不装也不影响训练。

## 故障排查

| 现象 | 原因 / 解决 |
|---|---|
| 模型下载卡住或报 `Network is unreachable` | Hugging Face 不可直连。脚本已设置 `HF_ENDPOINT=https://hf-mirror.com`；手动命令也需加此前缀 |
| `Address already in use` | 端口被占用：`PORT=8001 bash scripts/start-web.sh`，浏览器改开 8001 |
| 浏览器没有麦克风权限 | 地址必须是 `http://localhost:8000`，并在地址栏左侧允许麦克风 |
| 网页能开但分析一直转圈 | 默认 gTTS 需要访问 Google，会卡住。`scripts/start-web.sh` 已切换到本地 Piper；若手动启动，设置 `OPENPRONOUNCE_TTS=piper` |
| 网页能开但分析失败 | 查看启动终端报错；确认 `ffmpeg`、`espeak-ng` 已安装 |
| 首次分析很慢 | 正常，正在下载 Wav2Vec2 模型；保留 `~/.cache/huggingface` |
| 分数忽高忽低 | 固定麦克风距离、房间、音量和句子；一次只比较一个变化 |
| 安装 Kokoro 失败 | Python 3.13 下 spaCy 无法构建；本项目使用 Piper 替代，功能不受影响 |
| Vosk 模型下载慢 | 模型约 40 MB，官方站点速度不稳定；可稍后重试或用 Whisper 替代 |
| `openpronounce` 找不到 | 使用 `bash scripts/pronounce.sh`，或先 `source ~/english/.venv/bin/activate` |

## 模型与磁盘

| 组件 | 位置 | 体积（约） |
|---|---|---|
| OpenPronounce 模型 | `~/.cache/huggingface` | 约 2.5 GB（两个检查点） |
| Piper 声音 | `~/.cache/huggingface` | 63 MB |
| Whisper base.en | `~/.cache/whisper` | 139 MB |
| Vosk 小模型 | `~/english/models/vosk-model-small-en-us-0.15` | 68 MB |
| Python 环境 | `~/english/.venv` | 2–3 GB |

## 相关

- [[STUDY-PLAN|学习计划]]
- [[01_pronunciation/_index|发音训练]]
- [[11_attachments/_index|录音说明]]
- [[MANAGEMENT|管理规范]]

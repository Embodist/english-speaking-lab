---
type: guide
title: 工具搭建、搭配与使用最佳实践
tags: [guide, skill/pronunciation, meta]
created: 2026-10-24
updated: 2026-10-24
---

# 工具搭建、搭配与使用最佳实践

> 这份文档回答三件事：**怎么从零搭起来、每个工具该和谁搭配、怎么用才不浪费时间。**
> 只想马上开始：看 [[QUICKSTART|工具体验指南]]；想在另一台机器复现：看本文第 2 节或运行 `scripts/setup.sh`。

## 0. 一页速查

```bash
cd ~/english/english-speaking-lab
bash scripts/check-env.sh        # 环境自检
bash scripts/start-web.sh        # 网页录音 + 打分
bash scripts/tts.sh "sentence"   # 本地参考音
bash scripts/asr.sh audio.wav    # 可懂度检查
bash scripts/pronounce.sh audio.wav "sentence"  # 音素级分析
```

原则：**模型缓存不要删、下载走 hf-mirror、TTS 固定 Piper 一个声音、一次只改一个变量。**

## 1. 工具链地图

| 环节 | 主工具 | 作用 | 为什么选它 | 备选 |
|---|---|---|---|---|
| 录音 | Windows 录音机 / 手机 / 浏览器 | 采集 30–90 秒语音 | 简单、麦克风质量稳定 | Audacity |
| 参考音 TTS | Piper（`en_US-lessac-medium`） | 生成跟读示范音 | 本地、离线、稳定 | gTTS（需联网，不推荐） |
| 发音分析 | OpenPronounce 0.3.0 | 词/音素级差异、韵律 | 本地、可解释、英语校准 | 商业发音评分 API |
| 可懂度检查 | Whisper `base.en` | 转写整句 | 识别质量较好 | Vosk（更轻、更快） |
| 轻量 ASR | Vosk 小模型 | 快速离线转写 | 体积小、启动快 | Whisper |
| 复习 | Obsidian | 上下文、模板、链接 | 本地 Markdown、可检索 | Anki |
| 间隔重复 | Anki（可选） | 卡片复习 | 成熟算法 | Obsidian Spaced Repetition |
| 音频转换 | ffmpeg | m4a/mp3 → 16k mono wav | 通用、可靠 | Audacity |
| 模型下载 | Hugging Face 镜像 | 获取权重 | 本环境可访问 | 官方站点（不可直连） |
| 自动化 | `scripts/` | 启动、打分、TTS、ASR | 少记命令 | 手动执行 |

## 2. 从零搭建（可复现）

环境基线：Debian 13（WSL2）· Python 3.13 · CPU PyTorch · 无 GPU 依赖。

### 2.1 系统依赖

```bash
sudo apt-get update
sudo apt-get install -y ffmpeg espeak-ng git curl python3-venv pandoc aria2
```

- `espeak-ng`：OpenPronounce 的音素化后端，必需。
- `ffmpeg`：音频解码/转码，必需。
- `pandoc`、`aria2`：文档转换和加速下载，可选。

### 2.2 Python 环境与核心包

```bash
mkdir -p ~/english
cd ~/english
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip

# CPU 版 PyTorch（体积更小，本机无 GPU）
pip install torch --index-url https://download.pytorch.org/whl/cpu

# 发音分析 + 网页界面
pip install "openpronounce[app]"

# 本地 TTS
pip install "openpronounce[tts-piper]"

# ASR
pip install openai-whisper vosk
```

> Kokoro 在 Python 3.13 下因 spaCy 构建失败，**本项目不使用 Kokoro**；Piper 是等效的本地 TTS。不要为了装 Kokoro 降级整台机器的 Python。

### 2.3 网页界面源码

PyPI 包只含 CLI；网页界面在仓库根目录：

```bash
git clone --depth 1 https://github.com/Halleck45/OpenPronounce.git ~/english/OpenPronounce
```

### 2.4 模型下载

先设置镜像（脚本会自动设置）：

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

**Piper 声音（约 63 MB）**

```bash
~/english/.venv/bin/python - <<'EOF'
from openpronounce import tts
import soundfile as sf
wav, sr = tts.synthesize("Hello, this is a reference voice.", "en", "piper", tts.piper_default_voice("en"))
sf.write("/tmp/piper_check.wav", wav, sr)
print("Piper voice ready")
EOF
```

**Whisper base.en（约 139 MB）**

```bash
~/english/.venv/bin/python -c "import whisper; whisper.load_model('base.en')"
```

**Vosk 小模型（约 68 MB 解压后）**

```bash
mkdir -p ~/english/models && cd ~/english/models
curl -L -o vosk.tar.gz "https://hf-mirror.com/zzzlll/vosk-model-small-en-us-0.15/resolve/main/vosk-model-small-en-us-0.15.tar.gz"
tar xzf vosk.tar.gz && rm vosk.tar.gz
```

**OpenPronounce 两个检查点（合计约 2.5 GB）**

```bash
cd ~/english
~/.venv/bin/python - <<'EOF'
from openpronounce import tts
import soundfile as sf
wav, sr = tts.synthesize("I haven't identified the root cause yet.", "en", "piper", tts.piper_default_voice("en"))
sf.write("/tmp/openpronounce_check.wav", wav, sr)
EOF
HF_ENDPOINT=https://hf-mirror.com ~/.venv/bin/openpronounce /tmp/openpronounce_check.wav "I haven't identified the root cause yet."
```

首次运行会下载 `facebook/wav2vec2-large-960h` 和 `facebook/wav2vec2-lv-60-espeak-cv-ft`，完成后可离线运行。

### 2.5 一键脚本

`scripts/setup.sh` 把上面的步骤串起来，可重复执行；已安装的步骤会跳过：

```bash
bash scripts/setup.sh
# 只装环境、不下载模型（约 2.7 GB）：
SKIP_MODELS=1 bash scripts/setup.sh
```

### 2.6 验证

```bash
bash scripts/check-env.sh
bash scripts/pronounce.sh 11_attachments/reference/sample_root_cause.wav \
  "I haven't identified the root cause yet."
```

应看到 Score、Transcription、Heard phones；没有 mispronounced 或只提示少量词。

## 3. 配置与运行参数

| 变量 | 默认值 | 作用 | 什么时候改 |
|---|---|---|---|
| `HF_ENDPOINT` | `https://hf-mirror.com` | 模型下载镜像 | 网络环境变化 |
| `HF_HUB_OFFLINE` | 未设置 | 强制离线使用缓存 | 模型已下载、想避免联网检查 |
| `OPENPRONOUNCE_TTS` | `piper` | 参考音后端 | 不要改成 `gtts`（需 Google） |
| `OPENPRONOUNCE_TTS_VOICE` | `en_US-lessac-medium` | TTS 声音 | 固定两周后再考虑换 |
| `ENVDIR` | `~/english/.venv` | Python 环境 | 移动环境后 |
| `REPO` | `~/english/OpenPronounce` | 网页源码 | 移动环境后 |
| `PORT` | `8000` | 网页端口 | 端口冲突 |

### 路径

```text
~/english/
├── .venv/                  Python 环境（约 2.6 GB）
├── OpenPronounce/          网页源码
├── models/                 Vosk 模型
└── english-speaking-lab/   学习库（git 仓库）
```

### 离线模式

模型都下载完后：

```bash
HF_HUB_OFFLINE=1 bash scripts/pronounce.sh recording.wav "sentence"
```

离线时 Piper、OpenPronounce、Whisper、Vosk 都可正常工作；只有模型下载需要网络。

## 4. 工具搭配：什么场景用什么

| 任务 | 首选 | 不要用 | 原因 |
|---|---|---|---|
| 方便地录音 + 看结果 | 网页界面 | CLI | 浏览器录音、可视化更直接 |
| 批量/可重复分析 | CLI `pronounce.sh` | 网页 | 可脚本化、可存 JSON |
| 快速检查可懂度 | Vosk | Whisper | 启动快、体积小 |
| 最终可懂度判断 | Whisper | Vosk | 识别质量更好 |
| 跟读参考音 | Piper | gTTS | 离线、声音稳定 |
| 音素级错误定位 | OpenPronounce | 只看 ASR | ASR 只给整句转写 |
| 上下文与计划 | Obsidian | Anki | 链接、模板、复盘 |
| 间隔重复 | Anki | Obsidian（默认） | 算法成熟、移动端方便 |
| 剪辑/波形对比 | Audacity | 浏览器 | 可视化编辑 |
| 格式转换 | ffmpeg | 在线转换 | 本地、批量、无隐私风险 |

### 搭配规则

1. **网页负责“方便”，CLI 负责“可重复”。** 同一句话用同一工具对比。
2. **Whisper 负责准确，Vosk 负责速度。** 日常快速检查用 Vosk，关键句用 Whisper。
3. **Piper 负责稳定，gTTS 只做应急。** 本环境 gTTS 会卡住，不要用。
4. **OpenPronounce 负责诊断，ASR 负责可懂度。** 两者结论不一致时，以“人耳是否能听懂”为准。
5. **Obsidian 负责“查”，Anki 负责“记”。** 不要把所有内容同时维护两份。

## 5. 使用最佳实践

### 录音

- 安静房间，固定麦克风距离（约 20–30 cm），固定音量。
- 一次连续录完，不逐词暂停；保留第一次录音。
- 统一转成 16 kHz 单声道：

  ```bash
  ffmpeg -i input.m4a -ar 16000 -ac 1 output.wav
  ```

- 比较时只改一个变量（句子、麦克风、房间、音量之一）。

### 看分数

- 分数是**诊断线索**，不是考试成绩；优先看关键词、词尾、重音、节奏。
- 只在相同条件下比较；换房间/麦克风后不要直接比分数。
- ASR 转写正确不代表发音标准；转写错误通常是线索。
- 一次只修 1–2 个最影响理解的问题。

### TTS 与跟读

- 固定一个声音至少两周；不要每天换音色。
- 先听整句，再按意群听；影子跟读落后约半拍。
- 跟读后必须自己录一遍；只跟读不录音，无法暴露问题。

### ASR

- 重点看：关键词、数字、否定词、时间、行动项是否被识别。
- `base.en` 是小模型；专有名词识别错误不一定是发音问题。
- 不要把 ASR 当发音评分器。

### 复习

- 间隔：当天 → 第 2 天 → 第 4 天 → 第 8 天 → 第 15 天 → 第 30 天。
- 每次 3–5 句，不超过 10 条固定块。
- 能脱稿说出的条目划掉，不再重复抄写。

### 隐私与安全

- 录音、模型、分析全部在本机；OpenPronounce 不上传音频。
- gTTS 会访问 Google，本环境已禁用；统一用 Piper。
- 不要把录音提交到 git（`.gitignore` 已排除）。
- 不要把 GitHub token、模型 token 写入仓库或脚本。

### 维护

- 每周运行一次 `bash scripts/check-env.sh`。
- 每月看一次磁盘：`du -sh ~/.cache/huggingface ~/.cache/whisper ~/english/.venv`。
- 不要删除 `~/.cache/huggingface`；删了要重新下载约 2.5 GB。
- 升级工具时一次只升一个，升级后跑一次示例验证。
- 学习内容用 git 备份；音频单独备份（网盘/Git LFS）。

## 6. 常见问题（扩展）

| 现象 | 原因 | 解决 |
|---|---|---|
| `Network is unreachable` | 直连 Hugging Face 失败 | 使用 `HF_ENDPOINT=https://hf-mirror.com`（脚本已默认） |
| 网页分析一直转圈 | gTTS 在等 Google | 用 `start-web.sh`，或设置 `OPENPRONOUNCE_TTS=piper` |
| 端口被占用 | 已有服务在跑 | `PORT=8001 bash scripts/start-web.sh` |
| 麦克风没权限 | 非 localhost 或浏览器权限 | 打开 `http://localhost:8000` 并允许麦克风 |
| 首次分析很慢 | 正在下载模型 | 等下载完成；保留缓存 |
| 模型下载中断 | 网络/镜像不稳定 | 重新运行；不要删除 `.incomplete` 之外的缓存 |
| `openpronounce` 找不到 | 未激活 venv | `source ~/english/.venv/bin/activate` 或用包装脚本 |
| Vosk 模型缺失 | 未下载 | 见 2.4 的 Vosk 命令 |
| Kokoro 安装失败 | spaCy 在 Python 3.13 构建失败 | 使用 Piper，不要折腾 Kokoro |
| 分数波动大 | 麦克风/噪声/句子变了 | 固定条件，一次只改一个变量 |
| Windows 打不开 `\\wsl$` | WSL 未运行/共享关闭 | 启动 WSL；或把 vault 复制到 Windows 路径 |
| 磁盘不足 | 模型 + venv 约 5–6 GB | 清理旧缓存/旧环境，不要删当前模型 |

## 7. 版本与兼容性

| 组件 | 本机版本 | 说明 |
|---|---|---|
| OS | Debian 13（WSL2） | Windows 浏览器访问 localhost |
| Python | 3.13.5 | OpenPronounce 要求 ≥3.10 |
| PyTorch | 2.14.1+cpu | 无 GPU 依赖 |
| Transformers | 5.17.0 | Wav2Vec2 加载正常 |
| OpenPronounce | 0.3.0 | CLI + 网页 |
| Piper TTS | 1.8.0 | `en_US-lessac-medium` |
| Whisper | 20250625 | `base.en` |
| Vosk | 0.3.45 | `vosk-model-small-en-us-0.15` |
| ffmpeg | 7.1.5 | 音频转换 |
| eSpeak NG | 1.52.0 | 音素化 |

## 8. 已知限制

- OpenPronounce 的英语评分经过校准；其他语言仍是实验性。
- 自动分数受麦克风、噪声、专有名词影响，不能替代人耳判断。
- Whisper `base.en` 不是发音评分器，只是可懂度参考。
- 每次 CLI 分析会重新加载模型，约 6–12 秒；不适合实时对话评分。
- 本机无 GPU，批量分析较慢；需要时可换 GPU 环境。
- Kokoro 在 Python 3.13 下不可用；Piper 已覆盖需求。

## 9. 搭建检查清单

- [ ] `ffmpeg -version`、`espeak-ng --version` 正常
- [ ] `~/english/.venv` 可激活
- [ ] `pip check` 无冲突
- [ ] `~/english/OpenPronounce/server.py` 存在
- [ ] Piper 声音已下载
- [ ] Whisper `base.en` 已下载
- [ ] Vosk 模型目录存在
- [ ] `~/.cache/huggingface` 约 2.5 GB
- [ ] `bash scripts/check-env.sh` 全部 ok
- [ ] 示例音频能分析出 Score

## 相关

- [[QUICKSTART|工具体验指南]]
- [[scripts/README|脚本说明]]
- [[MANAGEMENT|管理规范]]
- [[01_pronunciation/_index|发音训练]]
- [[SCOPE|记录与扩展边界]]

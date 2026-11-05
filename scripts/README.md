---
type: guide
title: 脚本说明
tags: [guide, meta]
created: 2026-10-23
updated: 2026-11-05
---

# 脚本说明

所有脚本都可直接从 vault 根目录运行，会自动定位 `~/english/.venv` 和 `~/english/OpenPronounce`。

| 脚本 | 作用 | 示例 |
|---|---|---|
| `setup.sh` | 从零搭建环境（可重复执行） | `bash scripts/setup.sh` |
| `check-env.sh` | 检查工具、Python 包和模型 | `bash scripts/check-env.sh` |
| `lab.sh` | 统一流水线：TTS + ASR + 发音 + 报告 | `bash scripts/lab.sh analyze a.wav "sentence"` |
| `study.py` | 句子 / 短语 / 前后缀 / FSI 抽认与 Drill | `python scripts/study.py sentence --n 20` |
| `build_sentence_1200.py` | 生成 1200 句场景口语笔记 | `python scripts/build_sentence_1200.py` |
| `build_phrase_1200.py` | 生成基础短语（补充）笔记 | `python scripts/build_phrase_1200.py` |
| `build_affix_335.py` | 解析前后缀原文并生成笔记与 TSV | `python scripts/build_affix_335.py` |
| `build_fsi_drills.py` | 生成 FSI 替换/变换/应答/情景笔记 | `python scripts/build_fsi_drills.py` |
| `build_sentence_1200_apkg.py` | 导出 1200 句 Anki 牌组 | `~/english/.venv/bin/python scripts/build_sentence_1200_apkg.py` |
| `build_phrase_apkg.py` | 导出基础短语 Anki 牌组 | `~/english/.venv/bin/python scripts/build_phrase_apkg.py` |
| `build_affix_apkg.py` | 导出前缀/后缀/例词 Anki 牌组 | `~/english/.venv/bin/python scripts/build_affix_apkg.py` |
| `lab_server.py` | 同源 API：`/lab`、`/lab/asr`、`/lab/save` | 由 `start-web.sh` 启动 |
| `start-translate.sh` | 启动 Hy-MT2 翻译服务（GPU，8081） | `bash scripts/start-translate.sh --background` |
| `translate.sh` | 中文 → 英文草稿 | `bash scripts/translate.sh "中文"` |
| `stop-translate.sh` | 停止翻译服务 | `bash scripts/stop-translate.sh` |
| `upload-weights.sh` | 打包并上传模型权重到 RustFS | `bash scripts/upload-weights.sh` |
| `rustfs-public-read.sh` | 设置/查看/回滚模型前缀公共读 | `bash scripts/rustfs-public-read.sh status` |
| `sync-windows.sh` | WSL ↔ Windows Obsidian 镜像同步 | `WIN_VAULT=/mnt/e/english/english-speaking-lab bash scripts/sync-windows.sh push` |
| `build_vocab_10k.py` | 从 PDF/ECDICT 生成 10k 词库 | `python scripts/build_vocab_10k.py` |
| `build_reading_packs.py` | 生成 168 篇论文阅读包 | `python scripts/build_reading_packs.py` |
| `lab-web.html` | 统一网页（TTS/录音/发音/Whisper/Vosk） | 启动后打开 `/lab` |
| `start-web.sh` | 启动 OpenPronounce 网页界面 | `bash scripts/start-web.sh` |
| `pronounce.sh` | 对录音做音素级打分 | `bash scripts/pronounce.sh a.wav "sentence"` |
| `tts.sh` | 用 Piper 生成参考音 | `bash scripts/tts.sh "sentence"` |
| `asr.sh` | 转写录音，检查可懂度 | `bash scripts/asr.sh a.wav --engine vosk` |
| `new-day.sh` | 从模板生成当天记录 | `bash scripts/new-day.sh` |

## 学习数据源

| 数据 | 路径 | 生成物 |
|---|---|---|
| 1200 句场景口语 | `08_sentence-library/1200-sentences/data/sentences-1200.tsv` | `1200-sentences/*.md`、`1200-sentences.apkg` |
| 基础短语（补充） | `12_word-phrase-bank/11-basic-phrases/data/phrases-1200.tsv` | `11-basic-phrases/*.md`、`basic-phrases.apkg` |
| 前后缀 335 | `17_word-roots/data/{affixes,affix-examples}.tsv` | `17_word-roots/*.md`、`prefixes.apkg`、`suffixes.apkg`、`affix-examples.apkg` |
| FSI Drill | `18_fsi-drills/data/drills.tsv` | `18_fsi-drills/*.md` |

改内容只改 TSV，然后跑对应 `build_*.py`；不要手改生成出来的 Markdown。

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
- RustFS 公共读只开放模型前缀，说明见 [[deploy/RUSTFS-PUBLIC-READ|RustFS 模型公共读]]。

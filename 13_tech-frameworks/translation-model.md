---
type: topic
title: 中译英翻译模型（Hy-MT2-1.8B）
tags: [topic/translation, skill/writing, topic/llm]
created: 2026-10-26
updated: 2026-10-26
---

# 中译英翻译模型（Hy-MT2-1.8B）

> 用途：把中文思路快速变成英文草稿，再用固定块和面试句式改写。**不要把它当最终答案，也不要用它替代开口。**
>
> 部署：llama.cpp `llama-server` + 腾讯 `tencent/Hy-MT2-1.8B-GGUF`，Q6_K，GPU-only，端口 8081。

## 模型信息

| 项目 | 值 |
|---|---|
| 模型 | `tencent/Hy-MT2-1.8B-GGUF` |
| 基础模型 | `tencent/Hy-MT2-1.8B` |
| 许可证 | Apache-2.0 |
| 语言 | 33 种，含中文/英文/日文/韩文等 |
| 量化 | Q4_K_M 1.13GB · **Q6_K 1.47GB** · Q8_0 1.91GB |
| 官方支持 | transformers、llama.cpp |

官方推荐采样参数（1.8B）：`temperature 0.7`、`top_p 0.6`、`top_k 20`、`repetition_penalty 1.05`。本项目的翻译脚本默认 `temperature 0.3`，更稳定；需要更自然的口语可调到 0.7。

## 本机部署

```text
~/english/llama.cpp-cuda/
├── llama-b11889/llama-server          # CUDA 二进制
├── llama-b11889/llama-cli
└── cudart-llama-b11889-bin-ubuntu-cuda-12.8-x64/  # CUDA 运行库
~/english/models/hy-mt2-1.8b/Hy-MT2-1.8B-Q6_K.gguf
```

llama.cpp 使用官方 release `b11889` 的 CUDA 12.8 Linux 包，P1000（compute 6.1）可直接使用。

## 启动与停止

```bash
cd ~/english/english-speaking-lab

# 后台启动（GPU，端口 8081）
bash scripts/start-translate.sh --background

# 前台启动（Ctrl-C 停止）
bash scripts/start-translate.sh

# 停止
bash scripts/stop-translate.sh
```

启动后：

- API：`http://localhost:8081/v1/chat/completions`
- 自带 Web UI：`http://localhost:8081`
- 日志：`/tmp/llama-translate.log`

## 在 lab 里的使用环节

| 环节 | 怎么用 | 注意 |
|---|---|---|
| **说前（准备）** | 先写中文要点 → 生成英文草稿 → 只挑 2–3 个句型/关键词 | 不要背全文，草稿只是提示 |
| **说后（对照）** | 录完音 → 看 ASR 转写 → 和“中文意图的翻译”对照 | 找漏掉的信息、语法和连接词，不是改译文 |
| **写作（邮件/PR/论文摘要）** | 中文草稿 → 翻译 → 用固定块改写 | 术语表锁定专名；数字核对 |
| **阅读（可选）** | 英文段落 → `--target 中文` 辅助理解 | 理解后回到英文原文 |
| **面试** | 中文答题要点 → 英文草稿 → 按 STAR 重讲 | 不照读；公司名/指标必须真实 |

**不适合**：发音评分、直接背译文、替代开口练习。

## 网页与 CLI 集成

统一页 `http://localhost:8000/lab` 的第 4 节已接入：

- 输入中文 → 选择风格 → 生成英文草稿
- 显示耗时；可一键复制
- 需要先在 WSL 启动翻译服务（端口 8081）
- 失败时会提示启动命令

CLI 等价入口：

```bash
bash scripts/lab.sh translate "我在腾讯云负责基于大模型的恶意流量分析。"
```

## 翻译用法

```bash
# 默认：中文 -> 英语
bash scripts/translate.sh "我在腾讯云负责基于大模型的恶意流量分析和 WAF 规则推荐。"

# 口试/面试风格
bash scripts/translate.sh --style "技术面试口语" "我主导了告警分类项目。"

# 指定术语表（默认自动加载 15_resume/translation-glossary.txt）
bash scripts/translate.sh --glossary 15_resume/translation-glossary.txt "我们用 WAF 和 SOAR 做告警分诊。"

# 从文件读取
bash scripts/translate.sh --file note.md

# 关闭默认术语表
bash scripts/translate.sh --no-glossary "……"
```

## 实测数据（P1000 4GB）

| 项目 | 结果 |
|---|---|
| 显存占用 | 约 1.63GB（剩余约 2.38GB） |
| 模型加载 | 约 27 秒 |
| Prompt eval | 约 18.8 tok/s |
| 生成 | 约 26.9 tok/s |
| 示例句子（49+41 tokens） | 约 4 秒 |
| 上下文 | 2048（可用 `CTX=4096` 启动） |
| 并发 | 1（`--parallel 1`） |

结论：P1000 4GB 跑 1.8B 很轻松，显存还剩一半；适合逐段翻译和面试草稿。

## 质量与术语

实测优点：

- 技术句子结构自然，能处理“负责/主导/缩短到”等中文表达。
- 指令遵循好，默认只输出译文。
- 支持 glossary，能把 `WAF`、`SOAR`、`RAG` 等固定译法锁定。

实测问题：

- **专有名词会幻觉**：不带术语表时，`天融信` 被译成 `FireEye`/`Trend Micro`；加 glossary 后正确为 `Topsec`。
- 1.8B 模型对长难句会偏直译；技术细节需要自己核对。
- 上下文 2048，长文要分段。

因此 `translate.sh` 默认加载：

```text
15_resume/translation-glossary.txt
```

新增公司名、项目名、内部术语时，直接往这个文件加 `中文=English`。

## 使用边界

适合：

- 把中文笔记、面试思路、项目总结快速转成英文草稿。
- 对比“我自己说的”和“翻译模型写的”，找表达差距。
- 读英文资料时反向确认术语。

不适合：

- 直接背译文去面试（会像稿子，且可能有错）。
- 替代发音/口语训练。
- 翻译未公开的敏感材料到不可信服务（本模型本地运行，数据不出机器）。

## 资源与冲突

- 这是当前唯一的 GPU 常驻服务；OpenPronounce/Whisper 仍走 CPU。
- P1000 只有 4GB：不要同时再跑 GPU 版 OpenPronounce/Whisper；需要时先 `stop-translate.sh`。
- 如果 OOM：换 Q4_K_M，或把 `CTX` 降到 1024；不要盲目加 `--parallel`。
- 这是可选服务；不用时停掉，GPU 完全释放。

## 复现安装

```bash
mkdir -p ~/english/llama.cpp-cuda ~/english/models/hy-mt2-1.8b
cd ~/english/llama.cpp-cuda
# 1) CUDA 运行库
aria2c -x8 -o cudart.tar.gz \
  https://github.com/ggml-org/llama.cpp/releases/download/b11889/cudart-llama-b11889-bin-ubuntu-cuda-12.8-x64.tar.gz
tar xzf cudart.tar.gz
# 2) llama.cpp 二进制
aria2c -x8 -o llama-bin.tar.gz \
  https://github.com/ggml-org/llama.cpp/releases/download/b11889/llama-b11889-bin-ubuntu-cuda-12.8-x64.tar.gz
tar xzf llama-bin.tar.gz
# 3) 模型（Q6_K）
cd ~/english/models/hy-mt2-1.8b
aria2c -x8 -o Hy-MT2-1.8B-Q6_K.gguf \
  https://hf-mirror.com/tencent/Hy-MT2-1.8B-GGUF/resolve/main/Hy-MT2-1.8B-Q6_K.gguf
```

## 相关

- [[13_tech-frameworks/_index|技术与框架]]
- [[TOOLING|工具手册]]
- [[15_resume/translation-glossary.txt|翻译术语表]]
- [[15_resume/_index|简历与自我介绍]]
- [[QUICKSTART|工具体验指南]]

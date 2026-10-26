---
type: paper-pack
paper_id: "01-15"
stage: 1
title: "Mistral 7B"
pdf: "/home/user/llm-papers/01_大模型/PDF/15_Mistral7B.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-15 Mistral 7B

**中文标题**：Mistral 7B

**一句话概括**：发布 Mistral 7B，用分组查询注意力（GQA）与滑动窗口注意力（SWA）实现优于 Llama 2 13B 的性能和更快的推理，并以 Apache 2.0 协议开源。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| superior | /suːpˈiəɹɪə/ | 卓越的、更好的 | A |
| outperforms | /aʊtpəfˈɔːmz/ | 超过、胜过 | A |
| reasoning | /ɹˈiːzənɪŋ/ | 推理（逻辑思考能力） | A |
| arbitrary | /ˈɑːbɪtɹəɹi/ | 任意的 | A |
| surpasses | /səpˈasɪz/ | 超过、胜过 | A |
| engineered | /ˌɛndʒɪnˈiəd/ | 精心设计的 | B |
| leverages | /lˈiːvəɹɪdʒɪz/ | 利用 | B |
| grouped-query attention | /ɡɹˈuːptkwˈiəɹɪ ɐtˈɛnʃən/ | 分组查询注意力（GQA，多个查询头共享键值头） | B |
| coupled with | /kˈʌpəld wˈɪð/ | 与……结合 | B |
| license | /lˈaɪsəns/ | 许可证（开源协议） | B |

### 原句（保留完整句子）

- **superior** — “As a demonstration of its adaptability and superior performance, we present a chat model fine-tuned from Mistral 7B that significantly outperforms the Llama 2 13B – Chat model.”
- **outperforms** — “Mistral 7B outperforms the best open 13B model (Llama 2) across all evaluated benchmarks, and the best released 34B model (Llama 1) in reasoning, mathematics, and code generation.”
- **reasoning** — “Mistral 7B outperforms the best open 13B model (Llama 2) across all evaluated benchmarks, and the best released 34B model (Llama 1) in reasoning, mathematics, and code generation.”
- **arbitrary** — “Our model leverages grouped-query attention (GQA) for faster inference, coupled with sliding window attention (SWA) to effectively handle sequences of arbitrary length with a reduced inference cost.”
- **surpasses** — “We also provide a model fine-tuned to follow instructions, Mistral 7B – Instruct, that surpasses Llama 2 13B – chat model both on human and automated benchmarks.”
- **engineered** — “"a 7-billion-parameter language model engineered for superior performance"”
- **leverages** — “Our model leverages grouped-query attention (GQA) for faster inference, coupled with sliding window attention (SWA) to effectively handle sequences of arbitrary length with a reduced inference cost.”
- **grouped-query attention** — “Our model leverages grouped-query attention (GQA) for faster inference, coupled with sliding window attention (SWA) to effectively handle sequences of arbitrary length with a reduced inference cost.”
- **coupled with** — “Our model leverages grouped-query attention (GQA) for faster inference, coupled with sliding window attention (SWA) to effectively handle sequences of arbitrary length with a reduced inference cost.”
- **license** — “Our models are released under the Apache 2.0 license.”

## Abstract（自动提取）

> TITLE: Mistral 7B ABSTRACT: We introduce Mistral 7B v0.1, a 7-billion-parameter language model engineered for superior performance and efficiency. Mistral 7B outperforms Llama 2 13B across all evaluated benchmarks, and Llama 1 34B in reasoning, mathematics, and code generation. Our model leverages grouped-query attention (GQA) for faster inference, coupled with sliding window attention (SWA) to effectively handle sequences of arbitrary length with a reduced inference cost. We also provide a model fine-tuned to follow instructions, Mistral 7B -- Instruct, that surpasses the Llama 2 13B -- Chat model both on human and automated benchmarks. Our models are released under the Apache 2.0 license.

## 读中 30 分钟

- [ ] 问题：这篇论文解决什么？
- [ ] 方法：核心组件和数据流是什么？
- [ ] 数据/指标：在哪些数据集、用什么指标？
- [ ] 结果：主结果和消融说明了什么？
- [ ] 局限：作者承认什么？我还有什么疑问？

## 5 个理解问题

1. What problem does the paper address, and why does it matter?
2. What is the key idea, and what does it replace or improve?
3. What data, baselines, and metrics are used?
4. Which result is the most convincing, and which is weakest?
5. What is one limitation, and what would you test next?

## 60 秒复述

> The paper addresses … The authors propose … The key idea is … They evaluate on … The results show … One limitation is …

录音：`11_attachments/`

## 写 3 句

- The paper addresses …
- The key idea is …
- One limitation is …

## 词汇复习

- 把上面 10–12 个词加入 Anki；先读原句，再看中文。
- 词库入口：[[14_llm-papers/vocabulary-10k/_index|论文 10k 词库]]

## 相关

- [[14_llm-papers/reading-plan|12 周阅读计划]]
- [[14_llm-papers/stage-01-llm|阶段 1]]

PDF：`/home/user/llm-papers/01_大模型/PDF/15_Mistral7B.pdf`

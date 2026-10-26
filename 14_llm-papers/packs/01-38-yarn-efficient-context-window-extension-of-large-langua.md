---
type: paper-pack
paper_id: "01-38"
stage: 1
title: "YaRN: Efficient Context Window Extension of Large Language Models"
pdf: "/home/user/llm-papers/01_大模型/PDF/38_YaRN.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-38 YaRN: Efficient Context Window Extension of Large Language Models

**中文标题**：YaRN：大语言模型上下文窗口的高效扩展

**一句话概括**：提出 YaRN，一种算力高效的上下文窗口扩展方法，用远少于以往的数据量和训练步数，让 LLaMA 有效外推到超长上下文。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| generalize | /dʒˈɛnəɹəlˌaɪz/ | 泛化（推广到训练长度之外） | S |
| utilize | /jˈuːtɪlˌaɪz/ | 利用 | A |
| extension | /ɛkstˈɛnʃən/ | 扩展（延长上下文窗口） | A |
| capability | /kˌeɪpəbˈɪlɪti/ | 能力 | A |
| exhibits | /ɛɡzˈɪbɪts/ | 展现出 | A |
| context window | /kˈɒntɛkst wˈɪndəʊ/ | 上下文窗口（模型能处理的输入长度） | B |
| effectively | /ɪfˈɛktɪvli/ | 有效地 | B |
| compute-efficient | /kəmpjˈuːtɪfˈɪʃənt/ | 算力高效的（省计算资源） | B |
| extrapolate | /ɛkstɹˈapəlˌeɪt/ | 外推（超出训练长度继续使用） | B |
| surpassing | /səpˈasɪŋ/ | 超越 | B |

### 原句（保留完整句子）

- **generalize** — “We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data. ∗ Equal contribution.”
- **utilize** — “It is interesting that young parents would be often In contrast, with the chain-of-thought (CoT) prompting surprised by unexpected progress of the speaking ability strategy \[33\], LLMs can solve such tasks by utilizing the exhibited by their babies. prompting mechanism that involves intermediate reasoning steps for deriving the final answer.”
- **extension** — “LESS \[348\] Further, it can lead to substantial improvements by using an computes gradients for both downstream validation and appropriate number of exemplars as demonstrations \[69\], training instruction data, to evaluate the contribution of which also alleviates the model sensitivity to instruction instruction data based on extensions of influence funcengineering \[67, 69\].”
- **capability** — “Recently, pre-trained language models (PLMs) have been proposed by pretraining Transformer models over large-scale corpora, showing strong capabilities in solving various natural language processing (NLP) tasks.”
- **exhibits** — “"GPT-4 exhibits human-level performance on various professional and academic benchmarks"”
- **context window** — “"a compute-efficient method to extend the context window of such models"”
- **effectively** — “Thus, it is useful to establish a quantitatrain a capable LLM), adaptation (how to effectively adapt tive approach to characterizing the scaling effect.”
- **compute-efficient** — “In general, scaling law compute-efficient allocation of the compute resources.”
- **extrapolate** — “We chose the sinusoidal version because it may allow the model to extrapolate to sequence lengths longer than the ones encountered during training.”
- **surpassing** — “"while also surpassing previous the state-of-the-art at context window extension"”

## 摘要提示（PDF 文本不可提取）

> TITLE: YaRN: Efficient Context Window Extension of Large Language Models ABSTRACT: Rotary Position Embeddings (RoPE) have been shown to effectively encode positional information in transformer-based language models. However, these models fail to generalize past the sequence length they were trained on. We present YaRN (Yet another RoPE extensioN method), a compute-efficient method to extend the context window of such models, requiring 10x less tokens and 2.5x less training steps than previous methods. Using YaRN, we show that LLaMA models can effectively utilize and extrapolate to context lengths much longer than their original pre-training would allow, while also surpassing previous the state-of-the-art at context window extension. In addition, we demonstrate that YaRN exhibits the capability to extrapolate beyond the limited context of a fine-tuning dataset. Code is available at https://github.com/jquesnelle/yarn

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

PDF：`/home/user/llm-papers/01_大模型/PDF/38_YaRN.pdf`

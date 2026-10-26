---
type: paper-pack
paper_id: "01-23"
stage: 1
title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
pdf: "/home/user/llm-papers/01_大模型/PDF/23_Toolformer.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-23 Toolformer: Language Models Can Teach Themselves to Use Tools

**中文标题**：Toolformer：语言模型可以自学使用工具

**一句话概括**：提出 Toolformer，让语言模型以自监督方式学会在适当时机调用计算器、搜索引擎等外部工具，显著提升零样本性能。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| self-supervised | /sˈɛlfsˈuːpəvˌaɪzd/ | 自监督的（无需人工标注） | S |
| remarkable | /ɹɪmˈɑːkəbəl/ | 非凡的、惊人的 | A |
| incorporate | /ɪŋkˈɔːpəɹˌeɪt/ | 整合、纳入 | A |
| struggle | /stɹˈʌɡəl/ | 吃力、表现不佳 | A |
| excel | /ɛksˈɛl/ | 擅长、表现出色 | A |
| sacrificing | /sˈakɹɪfˌaɪsɪŋ/ | 牺牲 | A |
| paradoxically | /pˌaɹədˈɒksɪkli/ | 矛盾的是（看似不合理却如此） | B |
| factual lookup | /fˈaktʃuːəl lˈʊkʌp/ | 事实查询（查证事实信息） | B |
| external tools | /ɛkstˈɜːnəl tˈuːlz/ | 外部工具（模型之外的 API 等） | B |
| a handful of | /ˈeɪ hˈandfəl ˈɒv/ | 少量的 | B |

### 原句（保留完整句子）

- **self-supervised** — “This is done in a self-supervised right to attend and participate in meetings of local way, requiring nothing more than a handful of legislative bodies.\] that requires legislative bodies, like demonstrations for each API.”
- **remarkable** — “Recently, the research on LLMs has been largely advanced by both academia and industry, and a remarkable progress is the launch of ChatGPT (a powerful AI chatbot developed based on LLMs), which has attracted widespread attention from society.”
- **incorporate** — “Brown Act is an act of the best incorporate the results into future token California State Legislature that guarantees the public's prediction.”
- **struggle** — “They also, paradoxically, struggle with Out of 1400 participants, 400 (or \[Calculator(400 / 1400) basic functionality, such as arithmetic or factual lookup, where much simpler and smaller → 0.29\] 29%) passed the test. models excel.”
- **excel** — “They also, paradoxically, struggle with Out of 1400 participants, 400 (or \[Calculator(400 / 1400) basic functionality, such as arithmetic or factual lookup, where much simpler and smaller → 0.29\] 29%) passed the test. models excel.”
- **sacrificing** — “"to save memory without sacrificing performance"”
- **paradoxically** — “They also, paradoxically, struggle with Out of 1400 participants, 400 (or \[Calculator(400 / 1400) basic functionality, such as arithmetic or factual lookup, where much simpler and smaller → 0.29\] 29%) passed the test. models excel.”
- **factual lookup** — “They also, paradoxically, struggle with Out of 1400 participants, 400 (or \[Calculator(400 / 1400) basic functionality, such as arithmetic or factual lookup, where much simpler and smaller → 0.29\] 29%) passed the test. models excel.”
- **external tools** — “In this paper, we show that LMs can teach themselves to use external tools The name derives from “la tortuga”, the Spanish word for via simple APIs and achieve the best of both \[MT(“tortuga”) → turtle\] turtle. worlds.”
- **a handful of** — “This is done in a self-supervised right to attend and participate in meetings of local way, requiring nothing more than a handful of legislative bodies.\] that requires legislative bodies, like demonstrations for each API.”

## Abstract（自动提取）

> TITLE: Toolformer: Language Models Can Teach Themselves to Use Tools ABSTRACT: Language models (LMs) exhibit remarkable abilities to solve new tasks from just a few examples or textual instructions, especially at scale. They also, paradoxically, struggle with basic functionality, such as arithmetic or factual lookup, where much simpler and smaller models excel. In this paper, we show that LMs can teach themselves to use external tools via simple APIs and achieve the best of both worlds. We introduce Toolformer, a model trained to decide which APIs to call, when to call them, what arguments to pass, and how to best incorporate the results into future token prediction. This is done in a self-supervised way, requiring nothing more than a handful of demonstrations for each API. We incorporate a range of tools, including a calculator, a Q\&amp;A system, two different search engines, a translation system, and a calendar. Toolformer achieves substantially improved zero-shot performance across a variety of downstream tasks, often competitive with much larger models, without sacrificing its core language modeling abilities.

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

PDF：`/home/user/llm-papers/01_大模型/PDF/23_Toolformer.pdf`

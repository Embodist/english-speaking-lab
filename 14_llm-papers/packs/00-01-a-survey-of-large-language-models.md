---
type: paper-pack
paper_id: "00-01"
stage: 0
title: "A Survey of Large Language Models"
pdf: "/home/user/llm-papers/00_总览综述/PDF/01_A_SummaryOfLLMs.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 00-01 A Survey of Large Language Models

**中文标题**：《大语言模型综述》

**一句话概括**：综述大语言模型（LLM）的背景与关键技术，围绕预训练、适配调优、利用与能力评估四个方面总结最新进展，并讨论可用资源与开放问题。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| remarkable | /ɹɪmˈɑːkəbəl/ | 显著的、非凡的（remarkable progress 显著进展） | A |
| pose | /pˈəʊz/ | 构成、带来（pose a challenge 构成挑战，学术高频搭配） | A |
| comprehend | /kˌɒmpɹɪhˈɛnd/ | 理解、领会（比 understand 更正式，本文指让 AI 理解语言） | A |
| scaling | /skˈeɪlɪŋ/ | 规模化（model scaling 指把模型变大，从而带来性能提升） | A |
| revolutionize | /ɹˌɛvəlˈuːʃənˌaɪz/ | 彻底改变、变革（revolutionize the way 颠覆……的方式） | A |
| essentially | /ɪsˈɛnʃəli/ | 本质上（用于陈述事物的根本性质） | B |
| intricate | /ˈɪntɹɪkət/ | 错综复杂的（形容语言系统结构精细、层次繁多） | B |
| governed by | /ɡˈʌvənd bˈaɪ/ | 受……支配、受……制约（be governed by 遵循某种规则） | B |
| corpora | /kˈɔːpɔːɹə/ | 语料库（corpus 的复数，指大规模文本数据集） | B |
| exceed | /ɛksˈiːd/ | 超过、超出（参数规模超过某个阈值后能力突增） | B |
| discriminate | /dɪskɹˈɪmɪnˌeɪt/ | 区分、辨别（discriminate the difference 识别差异） | B |
| coined | /kˈɔɪnd/ | 创造（新词/术语）（coin the term 为……造词） | B |

### 原句（保留完整句子）

- **remarkable** — “Recently, the research on LLMs has been largely advanced by both academia and industry, and a remarkable progress is the launch of ChatGPT (a powerful AI chatbot developed based on LLMs), which has attracted widespread attention from society.”
- **pose** — “Apart length of LLMs may pose challenges in describing and from restricted environments such as household tasks, a demonstrating extensive tool APIs.”
- **comprehend** — “As a potential solution, it is promising to develop uation, recent work proposes to prompt LLMs with varied effective approaches to help LLMs comprehend and make contexts to generate diverse evaluation feedback.”
- **scaling** — “General-purpose Transferable task solver Task-agnostic NLP task solver GPT-3/4!ChatGPT!Claude Scaling language models Task Specific task feature learner ELMO!BERT!GPT-1/2 Prompt based completion solving helper Word2vec (NPLM)!NLPS Context-aware representations Solve various real-world tasks capacity n-gram models Static word representations Pre-training + fine-tuning Solve various NLP tasks LLM Statistical methods Neural context modeling Probability estimation Solve typical NLP tasks Pre-trained LM Assist in specific tasks Neural LM Statistical LM 1990s 2013 2018 2020 Fig.”
- **revolutionize** — “The technical evolution of LLMs has been making an important impact on the entire AI community, which would revolutionize the way how we develop and use AI algorithms.”
- **essentially** — “Language is essentially a complex, intricate system of human expressions governed by grammatical rules.”
- **intricate** — “Language is essentially a complex, intricate system of human expressions governed by grammatical rules.”
- **governed by** — “Language is essentially a complex, intricate system of human expressions governed by grammatical rules.”
- **corpora** — “Recently, pre-trained language models (PLMs) have been proposed by pretraining Transformer models over large-scale corpora, showing strong capabilities in solving various natural language processing (NLP) tasks.”
- **exceed** — “For example, retrieved want you to generate a concise summary.”), and the response documents are highly useful for open-domain question constraints (e.g., “the length of the summary cannot exceed 50.”). answering as supporting evidence.”
- **discriminate** — “To discriminate the language models in different parameter scales, the research community has coined the term large language models (LLM) for the PLMs of significant size (e.g., containing tens or hundreds of billions of parameters).”
- **coined** — “To discriminate the language models in different parameter scales, the research community has coined the term large language models (LLM) for the PLMs of significant size (e.g., containing tens or hundreds of billions of parameters).”

## Abstract（自动提取）

> TITLE: A Survey of Large Language Models ABSTRACT: Language is essentially a complex, intricate system of human expressions governed by grammatical rules. It poses a significant challenge to develop capable AI algorithms for comprehending and grasping a language. As a major approach, language modeling has been widely studied for language understanding and generation in the past two decades, evolving from statistical language models to neural language models. Recently, pre-trained language models (PLMs) have been proposed by pre-training Transformer models over large-scale corpora, showing strong capabilities in solving various NLP tasks. Since researchers have found that model scaling can lead to performance improvement, they further study the scaling effect by increasing the model size to an even larger size. Interestingly, when the parameter scale exceeds a certain level, these enlarged language models not only achieve a significant performance improvement but also show some special abilities that are not present in small-scale language models. To discriminate the difference in parameter scale, the research community has coined the term large language models (LLM) for the PLMs of significant size. Recently, the research on LLMs has been largely advanced by both academia and industry, and a remarkable progress is the launch of ChatGPT, which has attracted widespread attention 

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
- [[14_llm-papers/stage-00-surveys|阶段 0]]

PDF：`/home/user/llm-papers/00_总览综述/PDF/01_A_SummaryOfLLMs.pdf`

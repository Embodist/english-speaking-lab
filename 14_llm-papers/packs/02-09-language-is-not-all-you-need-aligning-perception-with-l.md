---
type: paper-pack
paper_id: "02-09"
stage: 2
title: "Language Is Not All You Need: Aligning Perception with Language Models"
pdf: "/home/user/llm-papers/02_多模态/PDF/09_KOSMOS1.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-09 Language Is Not All You Need: Aligning Perception with Language Models

**中文标题**：语言不是全部：让感知与语言模型对齐

**一句话概括**：提出 Kosmos-1 多模态大语言模型，从网络级多模态语料训练，能感知多种模态、上下文学习和遵循指令，并引入 Raven IQ 测试集。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| interleaved | /ˌɪntəlˈiːvd/ | 交错排列的（图文数据穿插混合） | S |
| cross-modal | /kɹˈɒsmˈəʊdəl/ | 跨模态的（知识在不同模态间迁移） | S |
| reasoning | /ɹˈiːzənɪŋ/ | 推理（此处指非言语推理能力） | A |
| convergence | /kənvˈɜːdʒəns/ | 汇聚、融合（语言、感知、行动等多方面能力走向统一） | A |
| perception | /pəsˈɛpʃən/ | 感知（对图像、声音等模态的接收与理解） | A |
| artificial general intelligence | /ˌɑːtɪfˈɪʃəl dʒˈɛnəɹəl ɪntˈɛlɪdʒəns/ | 通用人工智能（简称 AGI） | B |
| perceive | /pəsˈiːv/ | 感知（模型能接收并理解各种模态信息） | B |
| chain-of-thought | /tʃˈeɪnɒvθˈɔːt/ | 思维链的（让模型逐步推理的提示方法） | B |
| gradient update | /ɡɹˈeɪdiənt ˈʌpdeɪt/ | 梯度更新（训练中更新参数的步骤，本文指不做任何训练） | B |
| OCR-free | /ˌəʊsˌiːˈɑːfɹˈiː/ | 免 OCR 的（无需光学字符识别预处理） | B |
| specify | /spˈɛsɪfˌaɪ/ | 指定（通过文本指令指定分类要求） | B |
| diagnose | /dˌaɪəɡnˈəʊz/ | 诊断、测评（测试模型某方面能力） | B |

### 原句（保留完整句子）

- **interleaved** — “Specifically, we train KOSMOS -1 from scratch on web-scale multimodal corpora, including arbitrarily interleaved text and images, image-caption pairs, and text data.”
- **cross-modal** — “We also show that MLLMs can benefit from cross-modal transfer, i.e., transfer knowledge from language to multimodal, and from multimodal to language.”
- **reasoning** — “In addition, we introduce a dataset of Raven IQ test, which diagnoses the nonverbal reasoning capability of MLLMs.”
- **convergence** — “Abstract Ludwig Wittgenstein ” A big convergence of language, multimodal perception, action, and world modeling is a key step toward artificial general intelligence.”
- **perception** — “Abstract Ludwig Wittgenstein ” A big convergence of language, multimodal perception, action, and world modeling is a key step toward artificial general intelligence.”
- **artificial general intelligence** — “Abstract Ludwig Wittgenstein ” A big convergence of language, multimodal perception, action, and world modeling is a key step toward artificial general intelligence.”
- **perceive** — “In this work, we introduce KOSMOS -12 , a Multimodal Large Language Model (MLLM) that can perceive general modalities, learn in context (i.e., few-shot), and follow instructions (i.e., zero-shot).”
- **chain-of-thought** — “We evaluate various settings, including zero-shot, few-shot, and multimodal chain-of-thought prompting, on a wide range of tasks without any gradient updates or finetuning.”
- **gradient update** — “"without any gradient updates or finetuning"”
- **OCR-free** — “Experimental results show that KOSMOS -1 achieves impressive performance on (i) language understanding, generation, and even OCR-free NLP (directly fed with document images), (ii) perception-language tasks, including multimodal dialogue, image captioning, visual question answering, and (iii) vision tasks, such as image recognition with descriptions (specifying classification via text instructions).”
- **specify** — “Third, with the cleaned common abilities as examples to introduce how the concept data, one can further unify or specify the format for preof data curriculum23 applies in continual pre-training. training data, and perform the tokenization by training • Coding.”
- **diagnose** — “Right for the wrong reasons: Diagnosing syntactic heuristics in natural language inference. arXiv preprint arXiv:1902.01007, 2019. \[MWZ+ 18\] Margaret Mitchell, Simone Wu, Andrew Zaldivar, Parker Barnes, Lucy Vasserman, Ben Hutchinson, Elena Spitzer, Inioluwa Deborah Raji, and Timnit Gebru.”

## Abstract（自动提取）

> TITLE: Language Is Not All You Need: Aligning Perception with Language Models ABSTRACT: A big convergence of language, multimodal perception, action, and world modeling is a key step toward artificial general intelligence. In this work, we introduce Kosmos-1, a Multimodal Large Language Model (MLLM) that can perceive general modalities, learn in context (i.e., few-shot), and follow instructions (i.e., zero-shot). Specifically, we train Kosmos-1 from scratch on web-scale multimodal corpora, including arbitrarily interleaved text and images, image-caption pairs, and text data. We evaluate various settings, including zero-shot, few-shot, and multimodal chain-of-thought prompting, on a wide range of tasks without any gradient updates or finetuning. Experimental results show that Kosmos-1 achieves impressive performance on (i) language understanding, generation, and even OCR-free NLP (directly fed with document images), (ii) perception-language tasks, including multimodal dialogue, image captioning, visual question answering, and (iii) vision tasks, such as image recognition with descriptions (specifying classification via text instructions). We also show that MLLMs can benefit from cross-modal transfer, i.e., transfer knowledge from language to multimodal, and from multimodal to language. In addition, we introduce a dataset of Raven IQ test, which diagnoses the nonverbal reasoning 

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
- [[14_llm-papers/stage-02-multimodal|阶段 2]]

PDF：`/home/user/llm-papers/02_多模态/PDF/09_KOSMOS1.pdf`

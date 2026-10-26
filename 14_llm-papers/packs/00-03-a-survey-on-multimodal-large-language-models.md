---
type: paper-pack
paper_id: "00-03"
stage: 0
title: "A Survey on Multimodal Large Language Models"
pdf: "/home/user/llm-papers/00_总览综述/PDF/03_Survey_Multimodal_LLMs.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 00-03 A Survey on Multimodal Large Language Models

**中文标题**：《多模态大语言模型综述》

**一句话概括**：综述以 GPT-4V 为代表的多模态大语言模型（MLLM），梳理其基本形式、架构、训练与评估，并介绍多模态幻觉与 ICL、CoT 等扩展技术及未来方向。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| multimodal | /mˌʌltɪmˈəʊdəl/ | 多模态的（同时处理文本、图像、音频等多种信息形式） | S |
| emergent | /ɪmˈɜːdʒənt/ | 涌现的（emergent capabilities 指模型规模增大后"涌现"出的新能力） | A |
| reasoning | /ɹˈiːzənɪŋ/ | 推理（math reasoning 数学推理；本文指不依赖 OCR 直接解题） | A |
| formulation | /fˌɔːmjʊlˈeɪʃən/ | 形式化表述、基本定义（basic formulation 基本框架） | A |
| promising | /pɹˈɒmɪsɪŋ/ | 有前景的（promising research directions 有潜力的研究方向） | A |
| endeavor | /ɛndˈɛvə/ | 努力、竭力（学术界与工业界都努力去做） | A |
| hallucination | /hɐlˌuːsɪnˈeɪʃən/ | 幻觉（模型生成与事实不符的内容，即"一本正经地胡说八道"） | A |
| inspire | /ɪnspˈaɪə/ | 激发、启发（inspire more research 启发更多研究） | A |
| hotspot | /hˈɒtspɒt/ | 热点（research hotspot 研究热点） | B |
| trace | /tɹˈeɪs/ | 追溯、梳理（trace and summarize 梳理并总结发展脉络） | B |
| delineate | /dɪlˈɪniːˌeɪt/ | 详细说明、描绘（学术写作高频词，意为 describe in detail） | B |
| granularity | /ɡɹˌanjʊlˈaɹɪti/ | 粒度（支持更细的输入/输出粒度，如像素级细节） | B |

### 原句（保留完整句子）

- **multimodal** — “IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE 1 A Survey on Multimodal Large Language Models Shukang Yin*, Chaoyou Fu*†, Sirui Zhao*, Ke Li, Xing Sun, Tong Xu, and Enhong Chen, Fellow, IEEE Abstract—Recently, Multimodal Large Language Model (MLLM) represented by GPT-4V has been a new rising research hotspot, which uses powerful Large Language Models (LLMs) as a brain to perform multimodal tasks.”
- **emergent** — “The surprising emergent capabilities of MLLM, such as writing stories based on images and OCR-free math reasoning, are rare in traditional multimodal methods, suggesting a potential path to artificial general intelligence.”
- **reasoning** — “The surprising emergent capabilities of MLLM, such as writing stories based on images and OCR-free math reasoning, are rare in traditional multimodal methods, suggesting a potential path to artificial general intelligence.”
- **formulation** — “By optimizing the loss L(N, D) under the conLLMs work, this part introduces the basic background for straint C ≈ 6N D, they showed that the optimal allocation LLMs, including scaling laws, emergent abilities and key of compute budget to model size and data size can be techniques. derived as follows: Formulation of Scaling Laws for LLMs.”
- **promising** — “To conclude the paper, we discuss existing challenges and point out promising research directions.”
- **endeavor** — “To the best of its abilities, the model should mainly three kinds of approaches to collecting feedback and be capable of detecting covert endeavors aimed at soliciting preference data from human labelers. requests for malicious purposes.”
- **hallucination** — “We continue with multimodal hallucination and extended techniques, including Multimodal ICL (M-ICL), Multimodal CoT (M-CoT), and LLM-Aided Visual Reasoning (LAVR).”
- **inspire** — “In light of the fact that the era of MLLM has only just begun, we will keep updating this survey and hope it can inspire more research.”
- **hotspot** — “IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE 1 A Survey on Multimodal Large Language Models Shukang Yin*, Chaoyou Fu*†, Sirui Zhao*, Ke Li, Xing Sun, Tong Xu, and Enhong Chen, Fellow, IEEE Abstract—Recently, Multimodal Large Language Model (MLLM) represented by GPT-4V has been a new rising research hotspot, which uses powerful Large Language Models (LLMs) as a brain to perform multimodal tasks.”
- **trace** — “In this paper, we aim to trace and summarize the recent progress of MLLMs.”
- **delineate** — “Afterward, we delineate a general marized in Table 1.”
- **granularity** — “Then, we introduce research topics about how MLLMs can be extended to support more granularity, modalities, languages, and scenarios.”

## Abstract（自动提取）

> TITLE: A Survey on Multimodal Large Language Models ABSTRACT: Recently, Multimodal Large Language Model (MLLM) represented by GPT-4V has been a new rising research hotspot, which uses powerful Large Language Models (LLMs) as a brain to perform multimodal tasks. The surprising emergent capabilities of MLLM, such as writing stories based on images and OCR-free math reasoning, are rare in traditional multimodal methods, suggesting a potential path to artificial general intelligence. To this end, both academia and industry have endeavored to develop MLLMs that can compete with or even better than GPT-4V, pushing the limit of research at a surprising speed. In this paper, we aim to trace and summarize the recent progress of MLLMs. First of all, we present the basic formulation of MLLM and delineate its related concepts, including architecture, training strategy and data, as well as evaluation. Then, we introduce research topics about how MLLMs can be extended to support more granularity, modalities, languages, and scenarios. We continue with multimodal hallucination and extended techniques, including Multimodal ICL (M-ICL), Multimodal CoT (M-CoT), and LLM-Aided Visual Reasoning (LAVR). To conclude the paper, we discuss existing challenges and point out promising research directions. In light of the fact that the era of MLLM has only just begun, we will keep updating this survey and 

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

PDF：`/home/user/llm-papers/00_总览综述/PDF/03_Survey_Multimodal_LLMs.pdf`

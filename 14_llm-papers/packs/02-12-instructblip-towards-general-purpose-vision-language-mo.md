---
type: paper-pack
paper_id: "02-12"
stage: 2
title: "InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning"
pdf: "/home/user/llm-papers/02_多模态/PDF/12_InstructBLIP.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-12 InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning

**中文标题**：InstructBLIP：面向通用视觉-语言模型的指令微调

**一句话概括**：基于 BLIP-2 系统研究视觉-语言指令微调，提出指令感知的 Query Transformer，在全部留出数据集上取得零样本 SOTA。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| comprehensive | /kˌɒmpɹɪhˈɛnsɪv/ | 全面的（覆盖广泛的方面） | S |
| diversity | /daɪvˈɜːsɪti/ | 多样性（任务多样导致构建通用模型困难） | A |
| systematic | /sˌɪstəmˈatɪk/ | 系统性的（有条理、成体系的研究） | A |
| transform | /tɹansfˈɔːm/ | 转换（把数据集改造成指令微调格式） | A |
| informative | /ɪnfˈɔːmətˌɪv/ | 信息丰富的（提取对任务有用的特征） | A |
| substantially | /səbstˈanʃəli/ | 显著地（性能明显超过对比模型） | A |
| competence | /kˈɒmpɪtəns/ | 能力（大语言模型具备广泛能力） | B |
| instruction-aware | /ɪnstɹˈʌkʃənɐwˈeə/ | 指令感知的（能根据给定指令调整提取的特征） | B |
| tailored to | /tˈeɪləd tˈuː/ | 针对……定制的（特征与给定指令相匹配） | B |
| held-out | /hˈɛldˈaʊt/ | 留出的（训练时未见、专用于测试的数据） | B |
| qualitatively | /kwˈɒlɪtˌeɪtɪvli/ | 定性地（通过示例直观展示优势） | B |
| concurrent | /kəŋkˈʌɹənt/ | 同期出现的（同一时期发表的其他模型） | B |

### 原句（保留完整句子）

- **comprehensive** — “In this paper, we conduct a systematic and comprehensive study on vision-language instruction tuning based on the pretrained BLIP-2 models.”
- **diversity** — “However, building general-purpose vision-language models is challenging due to the rich input distributions and task diversity resulting from the additional visual input.”
- **systematic** — “In this paper, we conduct a systematic and comprehensive study on vision-language instruction tuning based on the pretrained BLIP-2 models.”
- **transform** — “We gather 26 publicly available datasets, covering a wide variety of tasks and capabilities, and transform them into instruction tuning format.”
- **informative** — “Additionally, we introduce an instruction-aware Query Transformer, which extracts informative features tailored to the given instruction.”
- **substantially** — “Trained on 13 held-in datasets, InstructBLIP attains state-of-the-art zero-shot performance across all 13 held-out datasets, substantially outperforming BLIP-2 and larger Flamingo models.”
- **competence** — “4.1.1 Data Source conversational competence of LLMs \[90\] and potentially imTo develop a capable LLM, it is key to collect a large amount prove their performance on a range of question-answering of natural language corpus from various data sources.”
- **instruction-aware** — “Additionally, we introduce an instruction-aware Query Transformer, which extracts informative features tailored to the given instruction.”
- **tailored to** — “Additionally, we introduce an instruction-aware Query Transformer, which extracts informative features tailored to the given instruction.”
- **held-out** — “Trained on 13 held-in datasets, InstructBLIP attains state-of-the-art zero-shot performance across all 13 held-out datasets, substantially outperforming BLIP-2 and larger Flamingo models.”
- **qualitatively** — “Furthermore, we qualitatively demonstrate the advantages of InstructBLIP over concurrent multimodal models.”
- **concurrent** — “Furthermore, we qualitatively demonstrate the advantages of InstructBLIP over concurrent multimodal models.”

## Abstract（自动提取）

> TITLE: InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning ABSTRACT: Large-scale pre-training and instruction tuning have been successful at creating general-purpose language models with broad competence. However, building general-purpose vision-language models is challenging due to the rich input distributions and task diversity resulting from the additional visual input. Although vision-language pretraining has been widely studied, vision-language instruction tuning remains under-explored. In this paper, we conduct a systematic and comprehensive study on vision-language instruction tuning based on the pretrained BLIP-2 models. We gather 26 publicly available datasets, covering a wide variety of tasks and capabilities, and transform them into instruction tuning format. Additionally, we introduce an instruction-aware Query Transformer, which extracts informative features tailored to the given instruction. Trained on 13 held-in datasets, InstructBLIP attains state-of-the-art zero-shot performance across all 13 held-out datasets, substantially outperforming BLIP-2 and larger Flamingo models. Our models also lead to state-of-the-art performance when finetuned on individual downstream tasks (e.g., 90.7% accuracy on ScienceQA questions with image contexts). Furthermore, we qualitatively demonstrate the advantages of InstructBLIP over concurrent multi

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

PDF：`/home/user/llm-papers/02_多模态/PDF/12_InstructBLIP.pdf`

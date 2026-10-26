---
type: paper-pack
paper_id: "01-01"
stage: 1
title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
pdf: "/home/user/llm-papers/01_大模型/PDF/01_BERT.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-01 BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

**中文标题**：BERT：面向语言理解的深度双向 Transformer 预训练

**一句话概括**：提出 BERT，一种在无标注文本上双向预训练的深度 Transformer 表示模型，只需额外加一个输出层微调，即可在 11 项 NLP 任务上刷新当时最优成绩。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| state-of-the-art | /stˈeɪtɒvðɪˈɑːt/ | 最先进的（SOTA，当前最优水平） | S |
| inference | /ˈɪnfəɹəns/ | 推断（判断句子间关系的自然语言推理任务） | S |
| representation | /ɹˌɛpɹɪzˈɛntˈeɪʃən/ | 表示、表征（模型对文本语义的编码结果） | S |
| architecture | /ˈɑːkɪtˌɛktʃə/ | 架构（模型的整体结构设计） | S |
| conditioning | /kəndˈɪʃənɪŋ/ | 条件化（建模时把上下文作为条件考虑） | A |
| bidirectional | /baɪdaɪɹˈɛkʃənəl/ | 双向的（同时利用左右两侧上下文） | A |
| fine-tuned | /fˈaɪntjˈuːnd/ | 微调（在预训练模型上用小规模任务数据继续训练） | A |
| empirically | /ɛmpˈɪɹɪkli/ | 从实验上、经验上 | A |
| pre-train | /pɹˈiːtɹˈeɪn/ | 预训练（先在大规模无标注文本上训练通用模型） | B |
| unlabeled | /ʌnlˈeɪbəld/ | 未标注的（没有人工标签的原始文本） | B |

### 原句（保留完整句子）

- **state-of-the-art** — “As a retask-specific parameters, and is trained on the sult, the pre-trained BERT model can be finetuned with just one additional output layer downstream tasks by simply fine-tuning all preto create state-of-the-art models for a wide trained parameters.”
- **inference** — “The two approaches share the range of tasks, such as question answering and same objective function during pre-training, where language inference, without substantial task- they use unidirectional language models to learn specific architecture modifications. general language representations.”
- **representation** — “Unlike left-to- These approaches have been generalized to right language model pre-training, the MLM ob- coarser granularities, such as sentence embedjective enables the representation to fuse the left dings (Kiros et al., 2015; Logeswaran and Lee, and the right context, which allows us to pre- 2018) or paragraph embeddings (Le and Mikolov, train a deep bidirectional Transformer.”
- **architecture** — “The two approaches share the range of tasks, such as question answering and same objective function during pre-training, where language inference, without substantial task- they use unidirectional language models to learn specific architecture modifications. general language representations.”
- **conditioning** — “The fine-tuning approach, such as train deep bidirectional representations from the Generative Pre-trained Transformer (OpenAI unlabeled text by jointly conditioning on both GPT) (Radford et al., 2018), introduces minimal left and right context in all layers.”
- **bidirectional** — “The fine-tuning approach, such as train deep bidirectional representations from the Generative Pre-trained Transformer (OpenAI unlabeled text by jointly conditioning on both GPT) (Radford et al., 2018), introduces minimal left and right context in all layers.”
- **fine-tuned** — “Pre-trained word embeddings fine-tuned for a supervised downstream task (Dai are an integral part of modern NLP systems, of- and Le, 2015; Howard and Ruder, 2018; Radford fering significant improvements over embeddings et al., 2018).”
- **empirically** — “BERT is conceptually simple and empirically We argue that current techniques restrict the powerful.”
- **pre-train** — “(2018a) and Radford et al. tion Answering (QA) and Natural Language Infer(2018), we do not use traditional left-to-right or ence (NLI) are based on understanding the relaright-to-left language models to pre-train BERT. tionship between two sentences, which is not diInstead, we pre-train BERT using two unsuper- rectly captured by language modeling.”
- **unlabeled** — “The fine-tuning approach, such as train deep bidirectional representations from the Generative Pre-trained Transformer (OpenAI unlabeled text by jointly conditioning on both GPT) (Radford et al., 2018), introduces minimal left and right context in all layers.”

## Abstract（自动提取）

> TITLE: BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding ABSTRACT: We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications. BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement).

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

PDF：`/home/user/llm-papers/01_大模型/PDF/01_BERT.pdf`

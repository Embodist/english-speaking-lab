---
type: paper-pack
paper_id: "05-22"
stage: 5
title: "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control"
pdf: "/home/user/llm-papers/05_世界模型/PDF/22_RT2_VLA.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 05-22 RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control

**中文标题**：RT-2：视觉-语言-动作模型把网络知识迁移到机器人控制

**一句话概括**：提出把互联网规模训练的视觉-语言模型直接融入端到端机器人控制，将动作表示为文本 token 与自然语言一同训练，得到 VLA 模型 RT-2，从而获得对新颖物体泛化、解读新指令与基础语义推理等涌现能力。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| recipe | /ɹˈɛsɪpˌiː/ | 做法、方法方案 | S |
| pretraining | /pɹɪtɹˈeɪnɪŋ/ | 预训练；先在大规模数据上训练 | A |
| interpret | /ɪntˈɜːpɹɪt/ | 理解、解读 | A |
| emergent semantic reasoning | /ɪmˈɜːdʒənt səmˈantɪk ɹˈiːzənɪŋ/ | 涌现的语义推理；大规模训练自然出现的推理能力 | B |
| co-fine-tune | /kˈəʊfˈaɪntjˈuːn/ | 联合微调；同时在两类数据上微调 | B |
| vision-language-action models (VLA) | /vˈɪʒənlˈaŋɡwɪdʒˈakʃən mˈɒdəlz vlˈɑː/ | 视觉-语言-动作模型 | B |
| visual question answering | /vˈɪʒuːəl kwˈɛstʃən ˈansəɹɪŋ/ | 视觉问答；根据图像回答问题的任务 | B |
| emergent capabilities | /ɪmˈɜːdʒənt kˌeɪpəbˈɪlɪtiz/ | 涌现能力；规模化训练带来的新能力 | B |
| instantiate | /ɪnstˈanʃɪˌeɪt/ | 实例化；具体实现 | B |
| rudimentary | /ɹˌuːdɪmˈɛntəɹi/ | 初步的、基础的 | B |
| incorporated | /ɪŋkˈɔːpəɹˌeɪtɪd/ | 纳入、集成 | B |
| novel objects | /nˈɒvəl ˈɒbdʒɛkts/ | 新物体；训练中未见过的物体 | B |

### 原句（保留完整句子）

- **recipe** — “More (e.g., RLHF) \[66, 116\] have been widely used by leveraging training recipes or principles should be investigated and human feedback for developing well-aligned LLMs.”
- **pretraining** — “Recently, pre-trained language models (PLMs) have been proposed by pretraining Transformer models over large-scale corpora, showing strong capabilities in solving various natural language processing (NLP) tasks.”
- **interpret** — “Bowman, “GLUE: A multi-task benchmark long sequences with structured state spaces,” and analysis platform for natural language underin The Tenth International Conference on Learning standing,” in Proceedings of the Workshop: AnalyzRepresentations, ICLR 2022, Virtual Event, April 25-29, ing and Interpreting Neural Networks for NLP, Black2022.”
- **emergent semantic reasoning** — “boost generalization and enable emergent semantic reasoning”
- **co-fine-tune** — “we propose to co-fine-tune state-of-the-art vision-language models”
- **vision-language-action models (VLA)** — “refer to such category of models as vision-language-action models”
- **visual question answering** — “such as visual question answering”
- **emergent capabilities** — “obtain a range of emergent capabilities from Internet-scale training”
- **instantiate** — “A straightforward method is to tuning (discussed in Section 5.1) in that both utilize nat- instantiate a pre-defined template with the corresponding ural language to format the task or instances.”
- **rudimentary** — “For example, PointCLIP The development of MLLMs is still in a rudimentary stage V2 \[197\] prompts GPT-3 to generate descriptions with 3Dand thus leaves much room for improvement, which we related semantics for better alignment with corresponding summarize below: images.”
- **incorporated** — “In what follows, we first discuss the data incorporated several common LLMs (e.g., Flan-T5 \[69\] and collection and processing in Section 4.1, then introduce the GLM \[93\]) into its ModelCenter, where developers can use commonly used model architectures in Section 4.2, and fithese models directly. nally present the training techniques to stably and efficiently • FastMoE \[207\] is a specialized training library for MoE optimize LLMs in Section 4.3.”
- **novel objects** — “improved generalization to novel objects”

## 摘要提示（PDF 文本不可提取）

> TITLE: RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control ABSTRACT: We study how vision-language models trained on Internet-scale data can be incorporated directly into end-to-end robotic control to boost generalization and enable emergent semantic reasoning. Our goal is to enable a single end-to-end trained model to both learn to map robot observations to actions and enjoy the benefits of large-scale pretraining on language and vision-language data from the web. To this end, we propose to co-fine-tune state-of-the-art vision-language models on both robotic trajectory data and Internet-scale vision-language tasks, such as visual question answering. In contrast to other approaches, we propose a simple, general recipe to achieve this goal: in order to fit both natural language responses and robotic actions into the same format, we express the actions as text tokens and incorporate them directly into the training set of the model in the same way as natural language tokens. We refer to such category of models as vision-language-action models (VLA) and instantiate an example of such a model, which we call RT-2. Our extensive evaluation (6k evaluation trials) shows that our approach leads to performant robotic policies and enables RT-2 to obtain a range of emergent capabilities from Internet-scale training. This includes significantly improved generalizatio

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
- [[14_llm-papers/stage-05-world-models|阶段 5]]

PDF：`/home/user/llm-papers/05_世界模型/PDF/22_RT2_VLA.pdf`

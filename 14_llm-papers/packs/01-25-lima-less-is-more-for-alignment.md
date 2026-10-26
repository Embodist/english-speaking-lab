---
type: paper-pack
paper_id: "01-25"
stage: 1
title: "LIMA: Less Is More for Alignment"
pdf: "/home/user/llm-papers/01_大模型/PDF/25_LIMA.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-25 LIMA: Less Is More for Alignment

**中文标题**：LIMA：对齐中少即是多

**一句话概括**：只用 1000 条精心筛选的指令数据微调出 LIMA，证明大模型的知识主要来自预训练，少量高质量指令数据即可完成对齐。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| generalize | /dʒˈɛnəɹəlˌaɪz/ | 泛化 | S |
| align | /ɐlˈaɪn/ | 对齐（与目标任务、用户偏好一致） | A |
| curated | /kjˈʊəɹeɪtɪd/ | 精心筛选的 | A |
| unsupervised | /ʌnsˈuːpəvˌaɪzd/ | 无监督的（无需人工标签） | A |
| instruction tuning | /ɪnstɹˈʌkʃən tjˈuːnɪŋ/ | 指令微调（用指令数据训练模型遵循指令） | A |
| measure | /mˈɛʒə/ | 衡量 | A |
| prompts | /pɹˈɒmpts/ | 提示（给模型的输入指令） | B |
| preference modeling | /pɹˈɛfɹəns mˈɒdəlɪŋ/ | 偏好建模（学习用户的偏好） | B |
| remarkably | /ɹɪmˈɑːkəbli/ | 惊人地 | B |
| unseen | /ʌnsˈiːn/ | 未见过的（训练数据中没有的） | B |

### 原句（保留完整句子）

- **generalize** — “Moreover, the model tends to generalize well to unseen tasks that did not appear in the training data.”
- **align** — “Aligning the positions to steps in computation time, they generate a sequence of hidden states ht , as a function of the previous hidden state ht−1 and the input for position t.”
- **curated** — “We measure the relative importance of these two stages by training LIMA, a 65B parameter LLaMa language model fine-tuned with the standard supervised loss on only 1,000 carefully curated prompts and responses, without any reinforcement learning or human preference modeling.”
- **unsupervised** — “To tackle these Transformer architecture, and adopted a hybrid approach of issues, a recently proposed technique is to employ external unsupervised pre-training and supervised fine-tuning.”
- **instruction tuning** — “Taken together, these results strongly suggest that almost all knowledge in large language models is learned during pretraining, and only limited instruction tuning data is necessary to teach models to produce high quality output.”
- **measure** — “We measure the relative importance of these two stages by training LIMA, a 65B parameter LLaMa language model fine-tuned with the standard supervised loss on only 1,000 carefully curated prompts and responses, without any reinforcement learning or human preference modeling.”
- **prompts** — “We measure the relative importance of these two stages by training LIMA, a 65B parameter LLaMa language model fine-tuned with the standard supervised loss on only 1,000 carefully curated prompts and responses, without any reinforcement learning or human preference modeling.”
- **preference modeling** — “We measure the relative importance of these two stages by training LIMA, a 65B parameter LLaMa language model fine-tuned with the standard supervised loss on only 1,000 carefully curated prompts and responses, without any reinforcement learning or human preference modeling.”
- **remarkably** — “LIMA demonstrates remarkably strong performance, learning to follow specific response formats from only a handful of examples in the training data, including complex queries that range from planning trip itineraries to speculating about alternate history.”
- **unseen** — “Moreover, the model tends to generalize well to unseen tasks that did not appear in the training data.”

## Abstract（自动提取）

> TITLE: LIMA: Less Is More for Alignment ABSTRACT: Large language models are trained in two stages: (1) unsupervised pretraining from raw text, to learn general-purpose representations, and (2) large scale instruction tuning and reinforcement learning, to better align to end tasks and user preferences. We measure the relative importance of these two stages by training LIMA, a 65B parameter LLaMa language model fine-tuned with the standard supervised loss on only 1,000 carefully curated prompts and responses, without any reinforcement learning or human preference modeling. LIMA demonstrates remarkably strong performance, learning to follow specific response formats from only a handful of examples in the training data, including complex queries that range from planning trip itineraries to speculating about alternate history. Moreover, the model tends to generalize well to unseen tasks that did not appear in the training data. In a controlled human study, responses from LIMA are either equivalent or strictly preferred to GPT-4 in 43% of cases; this statistic is as high as 58% when compared to Bard and 65% versus DaVinci003, which was trained with human feedback. Taken together, these results strongly suggest that almost all knowledge in large language models is learned during pretraining, and only limited instruction tuning data is necessary to teach models to produce high quality 

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

PDF：`/home/user/llm-papers/01_大模型/PDF/25_LIMA.pdf`

---
type: paper-pack
paper_id: "01-26"
stage: 1
title: "Direct Preference Optimization: Your Language Model is Secretly a Reward Model"
pdf: "/home/user/llm-papers/01_大模型/PDF/26_DPO_DirectPreferenceOptimization.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-26 Direct Preference Optimization: Your Language Model is Secretly a Reward Model

**中文标题**：直接偏好优化：你的语言模型其实是一个奖励模型（DPO）

**一句话概括**：提出直接偏好优化 DPO，把 RLHF 中的奖励模型参数化改写为闭式解，仅用简单的分类损失即可完成对齐，更简单、更稳定。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| performant | /pəfˈɔːmənt/ | 高性能的、效果好的 | A |
| steerability | /stˈiəɹəbˈɪlɪti/ | 可控性（能引导模型行为） | B |
| precise control | /pɹɪsˈaɪs kəntɹˈəʊl/ | 精确控制 | B |
| relative quality | /ɹˈɛlətˌɪv kwˈɒlɪti/ | 相对质量（样本之间的好坏比较） | B |
| unstable | /ʌnstˈeɪbəl/ | 不稳定的 | B |
| parameterization | /pˌaɹəmˌɛtəɹaɪzˈeɪʃən/ | 参数化（对模型的数学表示方式） | B |
| closed form | /klˈəʊzd fˈɔːm/ | 闭式解（可直接计算的解析形式） | B |
| classification loss | /klˌasɪfɪkˈeɪʃən lˈɒs/ | 分类损失（分类任务的损失函数） | B |
| eliminating | /ɪlˈɪmɪnˌeɪtɪŋ/ | 消除 | B |
| sentiment | /sˈɛntɪmənt/ | 情感（生成内容的情感倾向） | B |

### 原句（保留完整句子）

- **performant** — “The resulting algorithm, which we call Direct Preference Optimization (DPO), is stable, performant, and computationally lightweight, eliminating the need for sampling from the LM during fine-tuning or performing significant hyperparameter tuning.”
- **steerability** — “Existing methods for gaining such steerability collect human labels of the relative quality of model generations and fine-tune the unsupervised LM to align with these preferences, often with reinforcement learning from human feedback (RLHF).”
- **precise control** — “"achieving precise control of their behavior is difficult"”
- **relative quality** — “Existing methods for gaining such steerability collect human labels of the relative quality of model generations and fine-tune the unsupervised LM to align with these preferences, often with reinforcement learning from human feedback (RLHF).”
- **unstable** — “However, RLHF is a complex and often unstable procedure, first fitting a reward model that reflects the human preferences, and then fine-tuning the large unsupervised LM using reinforcement learning to maximize this estimated reward without drifting too far from the original model.”
- **parameterization** — “In this paper we introduce a new parameterization of the reward model in RLHF that enables extraction of the corresponding optimal policy in closed form, allowing us to solve the standard RLHF problem with only a simple classification loss.”
- **closed form** — “In this paper we introduce a new parameterization of the reward model in RLHF that enables extraction of the corresponding optimal policy in closed form, allowing us to solve the standard RLHF problem with only a simple classification loss.”
- **classification loss** — “In this paper we introduce a new parameterization of the reward model in RLHF that enables extraction of the corresponding optimal policy in closed form, allowing us to solve the standard RLHF problem with only a simple classification loss.”
- **eliminating** — “The resulting algorithm, which we call Direct Preference Optimization (DPO), is stable, performant, and computationally lightweight, eliminating the need for sampling from the LM during fine-tuning or performing significant hyperparameter tuning.”
- **sentiment** — “Notably, fine-tuning with DPO exceeds PPO-based RLHF in ability to control sentiment of generations, and matches or improves response quality in summarization and single-turn dialogue while being substantially simpler to implement and train.”

## Abstract（自动提取）

> TITLE: Direct Preference Optimization: Your Language Model is Secretly a Reward Model ABSTRACT: While large-scale unsupervised language models (LMs) learn broad world knowledge and some reasoning skills, achieving precise control of their behavior is difficult due to the completely unsupervised nature of their training. Existing methods for gaining such steerability collect human labels of the relative quality of model generations and fine-tune the unsupervised LM to align with these preferences, often with reinforcement learning from human feedback (RLHF). However, RLHF is a complex and often unstable procedure, first fitting a reward model that reflects the human preferences, and then fine-tuning the large unsupervised LM using reinforcement learning to maximize this estimated reward without drifting too far from the original model. In this paper we introduce a new parameterization of the reward model in RLHF that enables extraction of the corresponding optimal policy in closed form, allowing us to solve the standard RLHF problem with only a simple classification loss. The resulting algorithm, which we call Direct Preference Optimization (DPO), is stable, performant, and computationally lightweight, eliminating the need for sampling from the LM during fine-tuning or performing significant hyperparameter tuning. Our experiments show that DPO can fine-tune LMs to align with hum

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

PDF：`/home/user/llm-papers/01_大模型/PDF/26_DPO_DirectPreferenceOptimization.pdf`

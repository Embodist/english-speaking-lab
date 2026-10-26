---
type: paper-pack
paper_id: "01-06"
stage: 1
title: "Training language models to follow instructions with human feedback"
pdf: "/home/user/llm-papers/01_大模型/PDF/06_InstructGPT_RLHF.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-06 Training language models to follow instructions with human feedback

**中文标题**：用人类反馈训练语言模型遵循指令（InstructGPT）

**一句话概括**：提出用人类反馈（监督微调＋强化学习）训练 InstructGPT，使 13 亿参数的小模型输出比 1750 亿参数的 GPT-3 更受人类偏好、更真实有用。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| aligned | /ɐlˈaɪnd/ | 对齐的（与用户意图一致） | A |
| reinforcement learning | /ɹˌiːɪnfˈɔːsmənt lˈɜːnɪŋ/ | 强化学习（通过奖励信号学习策略） | A |
| promising | /pɹˈɒmɪsɪŋ/ | 有前景的、有希望的 | A |
| demonstrations | /dˌɛmənstɹˈeɪʃənz/ | 示范样本（人工标注的期望行为） | A |
| supervised learning | /sˈuːpəvˌaɪzd lˈɜːnɪŋ/ | 监督学习（用带标签数据训练） | A |
| inherently | /ɪnhˈiəɹəntli/ | 本质上、天生地 | B |
| intent | /ɪntˈɛnt/ | 意图、目的（用户的真实需求） | B |
| toxic | /tˈɒksɪk/ | 有毒有害的（生成攻击性、有害内容） | B |
| avenue | /ˈavənjˌuː/ | 途径、方法 | B |
| regressions | /ɹɪɡɹˈɛʃənz/ | 性能退化、回退 | B |

### 原句（保留完整句子）

- **aligned** — “In other words, these models are not aligned with their users.”
- **reinforcement learning** — “We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback.”
- **promising** — “Even though InstructGPT still makes simple mistakes, our results show that fine-tuning with human feedback is a promising direction for aligning language models with human intent.”
- **demonstrations** — “Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model behavior, which we use to fine-tune GPT-3 using supervised learning.”
- **supervised learning** — “Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model behavior, which we use to fine-tune GPT-3 using supervised learning.”
- **inherently** — “This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples.”
- **intent** — “In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback.”
- **toxic** — “For example, large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user.”
- **avenue** — “In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback.”
- **regressions** — “Moreover, InstructGPT models show improvements in truthfulness and reductions in toxic output generation while having minimal performance regressions on public NLP datasets.”

## Abstract（自动提取）

> TITLE: Training language models to follow instructions with human feedback ABSTRACT: Making language models bigger does not inherently make them better at following a user's intent. For example, large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user. In other words, these models are not aligned with their users. In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback. Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model behavior, which we use to fine-tune GPT-3 using supervised learning. We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback. We call the resulting models InstructGPT. In human evaluations on our prompt distribution, outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters. Moreover, InstructGPT models show improvements in truthfulness and reductions in toxic output generation while having minimal performance regressions on public NLP datasets. Even though InstructGPT still makes simple mistakes, our results show that fine-tuning with human feedbac

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

PDF：`/home/user/llm-papers/01_大模型/PDF/06_InstructGPT_RLHF.pdf`

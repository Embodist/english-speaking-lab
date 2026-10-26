---
type: paper-pack
paper_id: "01-07"
stage: 1
title: "Constitutional AI: Harmlessness from AI Feedback"
pdf: "/home/user/llm-papers/01_大模型/PDF/07_ConstitutionalAI.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-07 Constitutional AI: Harmlessness from AI Feedback

**中文标题**：宪法式 AI：来自 AI 反馈的无害性训练

**一句话概括**：提出"宪法式 AI"：只凭一套规则原则，让 AI 自我批评、自我改进生成偏好数据并训练无害助手（RLAIF），大幅减少人工标注。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| leverage | /lˈiːvəɹɪdʒ/ | 利用、借助 | S |
| finetune | /fˈaɪntjuːn/ | 微调 | A |
| harmless | /hˈɑːmləs/ | 无害的（不产生有害输出） | B |
| enlist | /ɛnlˈɪst/ | 借助、争取（让 AI 帮忙监督其他 AI） | B |
| oversight | /ˈəʊvəsˌaɪt/ | 监督、监管 | B |
| principles | /pɹˈɪnsɪpəlz/ | 原则、准则 | B |
| self-critiques | /sˈɛlfkɹɪtˈiːks/ | 自我批评（模型审视并指出自己输出的问题） | B |
| preference model | /pɹˈɛfɹəns mˈɒdəl/ | 偏好模型（学习判断两个输出哪个更好） | B |
| reward signal | /ɹɪwˈɔːd sˈɪɡnəl/ | 奖励信号（强化学习中的反馈） | B |
| transparency | /tɹanspˈaɹənsi/ | 透明性（决策过程可被人理解） | B |

### 原句（保留完整句子）

- **leverage** — “Both the SL and RL methods can leverage chain-of-thought style reasoning to improve the human-judged performance and transparency of AI decision making.”
- **finetune** — “In the supervised phase we sample from an initial model, then generate self-critiques and revisions, and then finetune the original model on revised responses.”
- **harmless** — “We experiment with methods for training a harmless AI assistant through selfimprovement, without any human labels identifying harmful outputs.”
- **enlist** — “Bowman, Zac Hatfield-Dodds, Ben Mann, Dario Amodei, Nicholas Joseph, Sam McCandlish, Tom Brown, Jared Kaplan∗ Anthropic Abstract As AI systems become more capable, we would like to enlist their help to supervise other AIs.”
- **oversight** — “The only human oversight is provided through a list of rules or principles, and so we refer to the method as ‘Constitutional AI’.”
- **principles** — “The only human oversight is provided through a list of rules or principles, and so we refer to the method as ‘Constitutional AI’.”
- **self-critiques** — “In the supervised phase we sample from an initial model, then generate self-critiques and revisions, and then finetune the original model on revised responses.”
- **preference model** — “In the RL phase, we sample from the finetuned model, use a model to evaluate which of the two samples is better, and then train a preference model from this dataset of AI preferences.”
- **reward signal** — “We then train with RL using the preference model as the reward signal, i.e. we use ‘RL from AI Feedback’ (RLAIF).”
- **transparency** — “Both the SL and RL methods can leverage chain-of-thought style reasoning to improve the human-judged performance and transparency of AI decision making.”

## Abstract（自动提取）

> TITLE: Constitutional AI: Harmlessness from AI Feedback ABSTRACT: As AI systems become more capable, we would like to enlist their help to supervise other AIs. We experiment with methods for training a harmless AI assistant through self-improvement, without any human labels identifying harmful outputs. The only human oversight is provided through a list of rules or principles, and so we refer to the method as 'Constitutional AI'. The process involves both a supervised learning and a reinforcement learning phase. In the supervised phase we sample from an initial model, then generate self-critiques and revisions, and then finetune the original model on revised responses. In the RL phase, we sample from the finetuned model, use a model to evaluate which of the two samples is better, and then train a preference model from this dataset of AI preferences. We then train with RL using the preference model as the reward signal, i.e. we use 'RL from AI Feedback' (RLAIF). As a result we are able to train a harmless but non-evasive AI assistant that engages with harmful queries by explaining its objections to them. Both the SL and RL methods can leverage chain-of-thought style reasoning to improve the human-judged performance and transparency of AI decision making. These methods make it possible to control AI behavior more precisely and with far fewer human labels.

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

PDF：`/home/user/llm-papers/01_大模型/PDF/07_ConstitutionalAI.pdf`

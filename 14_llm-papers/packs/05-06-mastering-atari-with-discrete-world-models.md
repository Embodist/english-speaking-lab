---
type: paper-pack
paper_id: "05-06"
stage: 5
title: "Mastering Atari with Discrete World Models"
pdf: "/home/user/llm-papers/05_世界模型/PDF/06_DreamerV2.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 05-06 Mastering Atari with Discrete World Models

**中文标题**：用离散世界模型称霸 Atari（DreamerV2）

**一句话概括**：提出 DreamerV2，在含离散表征的强世界模型的紧凑潜空间中纯靠预测学习行为，成为首个在 Atari 55 任务基准上达到人类水平、且行为完全在独立训练的世界模型内部学到的智能体。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| benchmark | /bˈɛntʃmɑːk/ | 基准；标准测试集 | S |
| generalize | /dʒˈɛnəɹəlˌaɪz/ | 泛化；把经验推广到新情况 | S |
| surpass | /səpˈas/ | 超越、超过 | S |
| open challenge | /ˈəʊpən tʃˈalɪndʒ/ | 未解决的难题 | A |
| feasible | /fˈiːzɪbəl/ | 可行的 | A |
| wall-clock time | /wˈɔːlklˈɒk tˈaɪm/ | 实际墙钟时间；真实流逝的时间 | A |
| discrete representations | /dɪskɹˈiːt ɹˌɛpɹɪzˈɛntˈeɪʃənz/ | 离散表征；用离散码（如整数码本）表示信息 | B |
| human-level performance | /hjˈuːmənlˈɛvəl pəfˈɔːməns/ | 人类水平的表现 | B |
| humanoid robot | /hjˈuːmɐnˌɔɪd ɹˈəʊbɒt/ | 类人机器人 | B |
| sample-efficiency | /sˈampəlɪfˈɪʃənsi/ | 样本效率；样本利用率 | B |
| imagined outcomes | /ɪmˈadʒɪnd ˈaʊtkʌmz/ | 想象中的结果；模型想象出的未来 | B |
| computational budget | /kˌɒmpjuːtˈeɪʃənəl bˈʌdʒɪt/ | 计算预算；允许使用的计算量 | B |

### 原句（保留完整句子）

- **benchmark** — “A recent study \[69\] found that a model size of 62B is better performance on downstream tasks, since language at least required for PaLM to perform well on various tasks modeling loss can be considered as a general measure of in four evaluation benchmarks (i.e., MMLU, BBH, TyDiQA the overall model capacity.”
- **generalize** — “We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data. ∗ Equal contribution.”
- **surpass** — “Even our base model surpasses all previously published models and ensembles, at a fraction of the training cost of any of the competitive models.”
- **open challenge** — “"an open challenge for multimodal machine learning"”
- **feasible** — “A feasible way is to learn largest version of Gemma-2 is trained on 6144 TPUv5p experiences from existing LLMs and reuse publicly avail- chips.”
- **wall-clock time** — “"in terms of wall-clock time compared"”
- **discrete representations** — “The world model uses discrete representations”
- **human-level performance** — “achieves human-level performance on the Atari benchmark”
- **humanoid robot** — “learns an accurate world model of a complex humanoid robot”
- **sample-efficiency** — “LoRA performs exhibits favorable sample-efficiency compared to other methods, including fine-tuning.”
- **imagined outcomes** — “learning behaviors from imagined outcomes”
- **computational budget** — “the same computational budget and wall-clock time”

## 摘要提示（PDF 文本不可提取）

> 提出 DreamerV2，在含离散表征的强世界模型的紧凑潜空间中纯靠预测学习行为，成为首个在 Atari 55 任务基准上达到人类水平、且行为完全在独立训练的世界模型内部学到的智能体。

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

PDF：`/home/user/llm-papers/05_世界模型/PDF/06_DreamerV2.pdf`

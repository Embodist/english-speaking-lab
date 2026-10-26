---
type: paper-pack
paper_id: "01-28"
stage: 1
title: "Fast Inference from Transformers via Speculative Decoding"
pdf: "/home/user/llm-papers/01_大模型/PDF/28_SpeculativeDecoding.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-28 Fast Inference from Transformers via Speculative Decoding

**中文标题**：通过推测解码实现 Transformer 的快速推理

**一句话概括**：提出推测解码：用高效小模型并行推测多个词元、再由大模型验证，不改变输出分布即可将解码加速 2–3 倍。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| concurrently | /kəŋkˈʌɹəntli/ | 并发地、同时 | A |
| off-the-shelf | /ˈɒfðəʃˈɛlf/ | 现成的（已有模型、无需改动） | A |
| distribution | /dˌɪstɹɪbjˈuːʃən/ | 分布（输出的概率分布） | A |
| speculative decoding | /spˈɛkjʊlətˌɪv dɪkˈəʊdɪŋ/ | 推测解码（先猜测后验证的解码方法） | B |
| serial | /sˈiəɹiəl/ | 串行的（一步步顺序执行） | B |
| sampling | /sˈamplɪŋ/ | 采样（按概率分布抽取词元） | B |
| at the heart of | /ˈat ðˈə hˈɑːt ˈɒv/ | 核心在于 | B |
| subtasks | /sˈʌbtasks/ | 子任务（大任务中的较易小任务） | B |
| approximated | /ɐpɹˈɒksɪmˌeɪtɪd/ | 近似（粗略模拟） | B |
| speculative execution | /spˈɛkjʊlətˌɪv ˌɛksɪkjˈuːʃən/ | 推测执行（先假设后验证的并行执行） | B |

### 原句（保留完整句子）

- **concurrently** — “For instance, Tree of Thoughts (ToT) \[444\] empowers LLMs to engage in the decision-making process by concurrently Numerical Computation exploring and self-evaluating various reasoning paths.”
- **off-the-shelf** — “Our The key observation above, that some inference steps are method can accelerate existing off-the-shelf mod- “harder” and some are “easier”, is also a key motivator for els without retraining or architecture changes.”
- **distribution** — “While many of these pling method, we can make exact decoding from solutions have proven extremely effective in practice, they the large models faster, by running them in par- usually require changing the model architecture, changing allel on the outputs of the approximation mod- the training-procedure and re-training the models, and don’t els, potentially generating several tokens concur- maintain identical outputs. rently, and without changing the distribution.”
- **speculative decoding** — “Fast Inference from Transformers via Speculative Decoding Yaniv Leviathan * 1 Matan Kalman * 1 Yossi Matias 1 Abstract developed to make inference from them faster.”
- **serial** — “Unfortunately, 2012) is an optimization technique, common in processors, a single decode step from these larger models is significantly where a task is performed in parallel to verifying if it’s slower than a step from their smaller counterparts, and mak- actually needed - the payoff being increased concurrency. ing things worse, these steps are done serially - decoding K A well-known example of speculative execution is branch tokens takes K serial runs of the model. prediction.”
- **sampling** — “With a novel sampling method, speculative sampling, Learning, Honolulu, Hawaii, USA.”
- **at the heart of** — “"At the heart of our approach lie the observations"”
- **subtasks** — “Han the observations that (1) hard language-modeling et al., 2021; Sukhbaatar et al., 2019; Schuster et al., 2021; tasks often include easier subtasks that can be ap- Scardapane et al., 2020; Bapna et al., 2020; Elbayad et al., proximated well by more efficient models, and 2019; Schwartz et al., 2020) aim to use less compute re(2) using speculative execution and a novel sam- sources for easier inference steps.”
- **approximated** — “Other troduce speculative decoding - an algorithm to approaches stem from the observation that not all infersample from autoregressive models faster without ence steps are born alike - some require a very large model, any changes to the outputs, by computing several while others can be approximated well by more efficient tokens in parallel.”
- **speculative execution** — “Han the observations that (1) hard language-modeling et al., 2021; Sukhbaatar et al., 2019; Schuster et al., 2021; tasks often include easier subtasks that can be ap- Scardapane et al., 2020; Bapna et al., 2020; Elbayad et al., proximated well by more efficient models, and 2019; Schwartz et al., 2020) aim to use less compute re(2) using speculative execution and a novel sam- sources for easier inference steps.”

## Abstract（自动提取）

> TITLE: Fast Inference from Transformers via Speculative Decoding ABSTRACT: Inference from large autoregressive models like Transformers is slow - decoding K tokens takes K serial runs of the model. In this work we introduce speculative decoding - an algorithm to sample from autoregressive models faster without any changes to the outputs, by computing several tokens in parallel. At the heart of our approach lie the observations that (1) hard language-modeling tasks often include easier subtasks that can be approximated well by more efficient models, and (2) using speculative execution and a novel sampling method, we can make exact decoding from the large models faster, by running them in parallel on the outputs of the approximation models, potentially generating several tokens concurrently, and without changing the distribution. Our method can accelerate existing off-the-shelf models without retraining or architecture changes. We demonstrate it on T5-XXL and show a 2X-3X acceleration compared to the standard T5X implementation, with identical outputs.

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

PDF：`/home/user/llm-papers/01_大模型/PDF/28_SpeculativeDecoding.pdf`

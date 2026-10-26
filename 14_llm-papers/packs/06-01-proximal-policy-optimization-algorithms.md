---
type: paper-pack
paper_id: "06-01"
stage: 6
title: "Proximal Policy Optimization Algorithms"
pdf: "/home/user/llm-papers/06_强化学习/PDF/01_PPO.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 06-01 Proximal Policy Optimization Algorithms

**中文标题**：《近端策略优化算法》

**一句话概括**：提出 PPO（近端策略优化）这一新的策略梯度方法，通过代理目标函数支持多轮小批量更新，实现简单、通用且样本效率高，在多个基准任务上优于其他在线策略梯度方法。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| benchmark | /bˈɛntʃmɑːk/ | 基准测试（benchmark tasks 用来比较算法性能的标准任务集） | S |
| minibatch | /mˈɪnɪbˌatʃ/ | 小批量（一次更新所使用的一小批样本） | A |
| favorable | /fˈeɪvəɹəbəl/ | 有利的、良好的（strikes a favorable balance 达到良好平衡） | A |
| proximal | /pɹˈɒksɪməl/ | 近端的、接近的（指更新时不让新策略偏离旧策略太远） | B |
| policy gradient | /pˈɒlɪsi ɡɹˈeɪdiənt/ | 策略梯度（直接对策略参数求梯度来优化的强化学习方法） | B |
| alternate | /ɔːltˈɜːnət/ | 交替、轮流（在采样数据与优化目标之间交替进行） | B |
| interaction | /ˌɪntəɹˈakʃən/ | 交互（interaction with the environment 与环境交互） | B |
| surrogate | /sˈʌɹəɡˌeɪt/ | 代理的、替代的（surrogate objective 代理目标函数，用于近似真实目标） | B |
| objective function | /ɒbdʒˈɛktɪv fˈʌŋkʃən/ | 目标函数（要最大化/最小化的数学目标） | B |
| epoch | /ˈɛpɒk/ | 一轮训练（把全部数据过一遍；multiple epochs 多轮） | B |
| sample complexity | /sˈampəl kəmplˈɛksɪti/ | 样本复杂度（达到一定性能所需样本量的度量） | B |
| locomotion | /lˌəʊkəmˈəʊʃən/ | 运动、移动（robotic locomotion 机器人行走/运动控制） | B |

### 原句（保留完整句子）

- **benchmark** — “A recent study \[69\] found that a model size of 62B is better performance on downstream tasks, since language at least required for PaLM to perform well on various tasks modeling loss can be considered as a general measure of in four evaluation benchmarks (i.e., MMLU, BBH, TyDiQA the overall model capacity.”
- **minibatch** — “Alignment tuning is more often used in scenarios where LaVIN \[101\] directly constructs a minibatch by randomly models need to be aligned with specific human preferences, sampling from both language-only and multimodal data. e.g. response with fewer hallucinations (see §6).”
- **favorable** — “This result suggests that INT4 quantization exhibits a favorable Distillation for LLMs.”
- **proximal** — “Shortly after the release of this ities in solving complex tasks than GPT-3.5, showing a RL paper \[79\], the paper of the Proximal Policy Optimiza- large performance improvement on many evaluation tasks. tion (PPO) \[128\] was published in July 2017, which now has A recent study \[41\] investigated the capacities of GPTbeen the foundational RL algorithm for learning from hu- 4 by conducting qualitative tests with human-generated man preferences \[66\].”
- **policy gradient** — “"a new family of policy gradient methods"”
- **alternate** — “(2020) 0.73 0.27 Table A2 | Estimated parameter and data scaling with increased training compute on two alternate datasets.”
- **interaction** — “It synthetic instructions, and finally obtain the Self-Instruct- comes from a virtual interaction environment called SAND52K dataset.”
- **surrogate** — “As a surrogate, there is a readily accessible open-source alternative called OpenWeb3.2 Commonly Used Corpora for Pre-training Text \[162\].”
- **objective function** — “"optimizing a "surrogate" objective function using"”
- **epoch** — “All the experiments are conducted with Alpaca-52K dataset by training LLaMA models three epochs.”
- **sample complexity** — “"have better sample complexity (empirically)"”
- **locomotion** — “Deep reinforcement learning has demonstrated remarkable capabilities in robotics, enabling autonomous performance in complex tasks such as stable locomotion \[135, 238\], precise object manipulation \[44, 308\], and intricate activities like tying shoelaces \[6\].”

## 摘要提示（PDF 文本不可提取）

> TITLE: Proximal Policy Optimization Algorithms ABSTRACT: We propose a new family of policy gradient methods for reinforcement learning, which alternate between sampling data through interaction with the environment, and optimizing a "surrogate" objective function using stochastic gradient ascent. Whereas standard policy gradient methods perform one gradient update per data sample, we propose a novel objective function that enables multiple epochs of minibatch updates. The new methods, which we call proximal policy optimization (PPO), have some of the benefits of trust region policy optimization (TRPO), but they are much simpler to implement, more general, and have better sample complexity (empirically). Our experiments test PPO on a collection of benchmark tasks, including simulated robotic locomotion and Atari game playing, and we show that PPO outperforms other online policy gradient methods, and overall strikes a favorable balance between sample complexity, simplicity, and wall-time.

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
- [[14_llm-papers/stage-06-rl|阶段 6]]

PDF：`/home/user/llm-papers/06_强化学习/PDF/01_PPO.pdf`

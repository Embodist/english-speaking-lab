---
type: paper-pack
paper_id: "05-05"
stage: 5
title: "Planning to Explore via Self-Supervised World Models"
pdf: "/home/user/llm-papers/05_世界模型/PDF/05_Plan2Explore.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 05-05 Planning to Explore via Self-Supervised World Models

**中文标题**：通过自监督世界模型规划探索（Plan2Explore）

**一句话概括**：提出自监督强化学习智能体 Plan2Explore：探索阶段用规划主动寻找"预期未来新颖性"，而非事后计算观测新颖性；探索后能以零样本/少样本方式快速适应多个下游任务。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| outperform | /aʊtpəfˈɔːm/ | 胜过、优于 | S |
| self-supervised | /sˈɛlfsˈuːpəvˌaɪzd/ | 自监督的；无需人工标注 | S |
| adaptation | /ˌadaptˈeɪʃən/ | 适应；针对新任务的调整 | S |
| sample efficiency | /sˈampəl ɪfˈɪʃənsi/ | 样本效率；样本利用率 | A |
| few-shot | /fjˈuːʃˈɒt/ | 少样本的；只用极少样本就能适应 | A |
| task-specific | /tˈaskspəsˈɪfɪk/ | 任务特定的；只针对单一任务 | A |
| exploration | /ɛksplɔːɹˈeɪʃən/ | 探索；主动去未知区域获取信息 | A |
| retrospectively | /ɹˌɛtɹəʊspˈɛktɪvli/ | 事后地、回顾式地；在到达之后才计算 | B |
| novelty | /nˈɒvəlti/ | 新颖性；观测有多"新奇"的度量 | B |
| downstream tasks | /dˈaʊnstɹiːm tˈasks/ | 下游任务；探索之后要解决的任务 | B |
| oracle | /ˈɒɹəkəl/ | 神谕参照；此处指能访问奖励的完美参照 | B |
| seek out | /sˈiːk ˈaʊt/ | 主动寻找、追求 | B |

### 原句（保留完整句子）

- **outperform** — “While for small values of dk the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of dk \[3\].”
- **self-supervised** — “We present Plan2Explore, a selfsupervised reinforcement learning agent that Task C tackles both these challenges through a new Environment Global without Rewards World Model Zero or Few Shot approach to self-supervised exploration and fast Task-Agnostic Adaptation Exploration adaptation to new tasks, which need not be known during exploration.”
- **adaptation** — “We present Plan2Explore, a selfsupervised reinforcement learning agent that Task C tackles both these challenges through a new Environment Global without Rewards World Model Zero or Few Shot approach to self-supervised exploration and fast Task-Agnostic Adaptation Exploration adaptation to new tasks, which need not be known during exploration.”
- **sample efficiency** — “"predictably improve performance and sample efficiency on a wide range"”
- **few-shot** — “After exploration, the agent quickly or few tasks-specific interactions. adapts to multiple downstream tasks in a zero or a few-shot manner.”
- **task-specific** — “The agent first leverages planning to explore in a selfprior methods which retrospectively compute supervised manner, without task-specific rewards, to efficiently the novelty of observations after the agent has learn a global world model.”
- **exploration** — “We present Plan2Explore, a selfsupervised reinforcement learning agent that Task C tackles both these challenges through a new Environment Global without Rewards World Model Zero or Few Shot approach to self-supervised exploration and fast Task-Agnostic Adaptation Exploration adaptation to new tasks, which need not be known during exploration.”
- **retrospectively** — “The agent first leverages planning to explore in a selfprior methods which retrospectively compute supervised manner, without task-specific rewards, to efficiently the novelty of observations after the agent has learn a global world model.”
- **novelty** — “The agent first leverages planning to explore in a selfprior methods which retrospectively compute supervised manner, without task-specific rewards, to efficiently the novelty of observations after the agent has learn a global world model.”
- **downstream tasks** — “After the exploration phase, it receives already reached them, our agent acts efficiently reward functions at test time to adapt to multiple downstream tasks, by leveraging planning to seek out expected future such as standing, walking, running, and flipping using either zero novelty.”
- **oracle** — “After the task-agnostic in fact, almost matches the performances oracle exploration phase, the agent is provided with downstream which has access to rewards.”
- **seek out** — “After the exploration phase, it receives already reached them, our agent acts efficiently reward functions at test time to adapt to multiple downstream tasks, by leveraging planning to seek out expected future such as standing, walking, running, and flipping using either zero novelty.”

## Abstract（自动提取）

> TITLE: Planning to Explore via Self-Supervised World Models ABSTRACT: Reinforcement learning allows solving complex tasks, however, the learning tends to be task-specific and the sample efficiency remains a challenge. We present Plan2Explore, a self-supervised reinforcement learning agent that tackles both these challenges through a new approach to self-supervised exploration and fast adaptation to new tasks, which need not be known during exploration. During exploration, unlike prior methods which retrospectively compute the novelty of observations after the agent has already reached them, our agent acts efficiently by leveraging planning to seek out expected future novelty. After exploration, the agent quickly adapts to multiple downstream tasks in a zero or a few-shot manner. We evaluate on challenging control tasks from high-dimensional image inputs. Without any training supervision or task-specific interaction, Plan2Explore outperforms prior self-supervised exploration methods, and in fact, almost matches the performances oracle which has access to rewards. Videos and code at https://ramanans1.github.io/plan2explore/

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

PDF：`/home/user/llm-papers/05_世界模型/PDF/05_Plan2Explore.pdf`

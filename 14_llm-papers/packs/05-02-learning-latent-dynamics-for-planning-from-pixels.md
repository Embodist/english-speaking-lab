---
type: paper-pack
paper_id: "05-02"
stage: 5
title: "Learning Latent Dynamics for Planning from Pixels"
pdf: "/home/user/llm-papers/05_世界模型/PDF/02_PlaNet.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 05-02 Learning Latent Dynamics for Planning from Pixels

**中文标题**：从像素学习潜动力学以进行规划（PlaNet）

**一句话概括**：提出纯基于模型的智能体 PlaNet，从图像学习潜空间动力学并做快速在线规划；通过"潜变量越步"这一多步变分推断目标，仅凭像素观测解决接触动力学、部分可观测、稀疏奖励等连续控制任务。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| leverage | /lˈiːvəɹɪdʒ/ | 利用、借助 | S |
| latent space | /lˈeɪtənt spˈeɪs/ | 潜空间；低维隐藏表示空间 | S |
| sparse rewards | /spˈɑːs ɹɪwˈɔːdz/ | 稀疏奖励；奖励信号稀少、难以获得 | A |
| model-based | /mˈɒdəlbˈeɪst/ | 基于模型的；先学习环境模型再用于规划 | A |
| dynamics | /daɪnˈamɪks/ | 动力学；环境状态如何随时间演化 | A |
| latent overshooting | /lˈeɪtənt ˌəʊvəʃˈuːtɪŋ/ | 潜变量"越步"；让潜状态预测未来多步的多步变分推断目标 | B |
| variational inference | /vˌeəɹɪˈeɪʃənəl ˈɪnfəɹəns/ | 变分推断；用优化来近似后验分布的推断方法 | B |
| partial observability | /pˈɑːʃəl ɒbzˌɜːvəbˈɪlɪti/ | 部分可观测性；智能体只能看到环境的一部分状态 | B |
| long-standing | /lˈɒŋstˈandɪŋ/ | 长期存在的、由来已久的 | B |
| episodes | /ˈɛpɪsˌəʊdz/ | 回合；智能体一次完整的交互过程 | B |
| model-free | /mˈɒdəlfɹˈiː/ | 无模型的；不显式学习环境模型 | B |

### 原句（保留完整句子）

- **leverage** — “In show that learning latent dynamics models for planning in comparison, we focus on simulated environments, where image domains is a promising approach. we leverage latent planning to scale to larger state and acDirections for future work include learning temporal abtion spaces, longer planning horizons, as well as sparse straction instead of using a fixed action repeat, possibly reward tasks.”
- **latent space** — “Moreover, planning carries the model-based agent that learns the environment promise of increasing performance just by increasing the dynamics from images and chooses actions computational budget for searching for actions, as shown through fast online planning in latent space.”
- **sparse rewards** — “However, these approaches Using only pixel observations, our agent solves typically assume access to the underlying state of the world continuous control tasks with contact dynamics, and the reward function, which may not be available in pracpartial observability, and sparse rewards, which tice.”
- **model-based** — “First, model-based planplanning has been a long-standing challenge, ning can be more data efficient because it leverages a richer especially in image-based domains.”
- **dynamics** — “Learning Latent Dynamics for Planning from Pixels Danijar Hafner 1 2 Timothy Lillicrap 3 Ian Fischer 4 Ruben Villegas 1 5 David Ha 1 Honglak Lee 1 James Davidson 1 Abstract enough for planning has been a long-standing challenge.”
- **latent overshooting** — “Moreover, simple low-dimensional environments (Deisenroth & Raswe propose a multi-step variational inference mussen, 2011; Gal et al., 2016; Amos et al., 2018; Chua objective that we name latent overshooting. et al., 2018; Henaff et al., 2018).”
- **variational inference** — “Moreover, simple low-dimensional environments (Deisenroth & Raswe propose a multi-step variational inference mussen, 2011; Gal et al., 2016; Amos et al., 2018; Chua objective that we name latent overshooting. et al., 2018; Henaff et al., 2018).”
- **partial observability** — “This could be because the tasks are stochastic from the agent’s perspective We evaluate PlaNet on six continuous control tasks from due to partial observability of the initial states.”
- **long-standing** — “Learning Latent Dynamics for Planning from Pixels Danijar Hafner 1 2 Timothy Lillicrap 3 Ian Fischer 4 Ruben Villegas 1 5 David Ha 1 Honglak Lee 1 James Davidson 1 Abstract enough for planning has been a long-standing challenge.”
- **episodes** — “The success of such latent models has previously uses substantially fewer episodes and reaches final been limited to simple tasks such as balancing cartpoles and performance close to and sometimes higher than controlling 2-link arms from dense rewards (Watter et al., strong model-free algorithms.”
- **model-free** — “However, learning Planning using learned models offers several benefits over dynamics models that are accurate enough for model-free reinforcement learning.”

## Abstract（自动提取）

> TITLE: Learning Latent Dynamics for Planning from Pixels ABSTRACT: Planning has been very successful for control tasks with known environment dynamics. To leverage planning in unknown environments, the agent needs to learn the dynamics from interactions with the world. However, learning dynamics models that are accurate enough for planning has been a long-standing challenge, especially in image-based domains. We propose the Deep Planning Network (PlaNet), a purely model-based agent that learns the environment dynamics from images and chooses actions through fast online planning in latent space. To achieve high performance, the dynamics model must accurately predict the rewards ahead for multiple time steps. We approach this using a latent dynamics model with both deterministic and stochastic transition components. Moreover, we propose a multi-step variational inference objective that we name latent overshooting. Using only pixel observations, our agent solves continuous control tasks with contact dynamics, partial observability, and sparse rewards, which exceed the difficulty of tasks that were previously solved by planning with learned models. PlaNet uses substantially fewer episodes and reaches final performance close to and sometimes higher than strong model-free algorithms.

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

PDF：`/home/user/llm-papers/05_世界模型/PDF/02_PlaNet.pdf`

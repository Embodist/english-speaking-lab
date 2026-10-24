---
type: paper-vocabulary
stage: 6
title: "阶段 6 · 强化学习基础 RL 论文词汇"
tags: [topic/paper, skill/reading, status/learning]
created: 2026-10-24
---

# 阶段 6 · 强化学习基础 RL 论文词汇

> 3 篇 · 36 个词条。读前扫词 2 分钟；读后遮住中文，用 abstract 片段自测，再用 5 个词复述 60 秒。
> 返回 [[14_llm-papers/_index|LLM 论文阅读]]；配套 [[14_llm-papers/reading-workflow|阅读与词汇流程]]。

## 06-00 Playing Atari with Deep Reinforcement Learning

- [ ] 已读

**中文标题**：《用深度强化学习玩 Atari 游戏》

**一句话概括**：首次提出用深度卷积神经网络直接从原始像素学习控制策略（DQN），在 7 款 Atari 2600 游戏中的 6 款超过此前所有方法，3 款超过人类专家。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| reinforcement learning | phr. | 强化学习（智能体通过与环境试错交互、按奖励信号学习决策的范式） | "sensory input using reinforcement learning" |
| high-dimensional | adj. | 高维的（输入数据维度很高，如整幅图像的像素） | "directly from high-dimensional sensory input using" |
| sensory | adj. | 感官的（sensory input 感官输入，本文指游戏画面像素） | "from high-dimensional sensory input using reinforcement" |
| control policies | phr. | 控制策略（policy 策略：状态到动作的映射规则） | "successfully learn control policies directly from" |
| convolutional neural network | phr. | 卷积神经网络（CNN，擅长处理图像的网络结构） | "The model is a convolutional neural network" |
| variant | n. | 变体（a variant of Q-learning Q 学习的一种变体） | "trained with a variant of Q-learning" |
| raw | adj. | 原始的、未经处理的（raw pixels 原始像素，直接输入图像） | "whose input is raw pixels and whose" |
| pixel | n. | 像素（图像的最小组成单元） | "input is raw pixels and whose output" |
| estimate | v. | 估计、估算（估计未来奖励的价值函数） | "a value function estimating future rewards" |
| reward | n. | 奖励（强化学习中环境给智能体的得分信号） | "a value function estimating future rewards" |
| outperform | v. | 胜过、优于（学术高频词，超过此前所有方法） | "it outperforms all previous approaches on six" |
| surpass | v. | 超过（surpasses a human expert 超过人类专家水平） | "and surpasses a human expert on three" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 06-01 Proximal Policy Optimization Algorithms

- [ ] 已读

**中文标题**：《近端策略优化算法》

**一句话概括**：提出 PPO（近端策略优化）这一新的策略梯度方法，通过代理目标函数支持多轮小批量更新，实现简单、通用且样本效率高，在多个基准任务上优于其他在线策略梯度方法。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| proximal | adj. | 近端的、接近的（指更新时不让新策略偏离旧策略太远） | "The new methods, which we call proximal policy optimization" |
| policy gradient | phr. | 策略梯度（直接对策略参数求梯度来优化的强化学习方法） | "a new family of policy gradient methods" |
| alternate | v. | 交替、轮流（在采样数据与优化目标之间交替进行） | "which alternate between sampling data through" |
| interaction | n. | 交互（interaction with the environment 与环境交互） | "sampling data through interaction with the environment" |
| surrogate | adj. | 代理的、替代的（surrogate objective 代理目标函数，用于近似真实目标） | "optimizing a "surrogate" objective function using" |
| objective function | phr. | 目标函数（要最大化/最小化的数学目标） | "optimizing a "surrogate" objective function using" |
| epoch | n. | 一轮训练（把全部数据过一遍；multiple epochs 多轮） | "enables multiple epochs of minibatch updates" |
| minibatch | n. | 小批量（一次更新所使用的一小批样本） | "multiple epochs of minibatch updates" |
| sample complexity | phr. | 样本复杂度（达到一定性能所需样本量的度量） | "have better sample complexity (empirically)" |
| benchmark | n. | 基准测试（benchmark tasks 用来比较算法性能的标准任务集） | "PPO on a collection of benchmark tasks" |
| locomotion | n. | 运动、移动（robotic locomotion 机器人行走/运动控制） | "including simulated robotic locomotion and Atari game" |
| favorable | adj. | 有利的、良好的（strikes a favorable balance 达到良好平衡） | "overall strikes a favorable balance between sample" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 06-02 Model-based Reinforcement Learning: A Survey

- [ ] 已读

**中文标题**：《基于模型的强化学习综述》

**一句话概括**：综述强化学习与规划相融合的"基于模型的强化学习"，系统梳理动力学模型学习（含随机性、不确定性、部分可观测等挑战）与规划-学习集成两大主题。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| sequential | adj. | 顺序的、序列的（sequential decision making 序列决策：按时间先后连续做决定） | "Sequential decision making, commonly formalized as" |
| formalize | v. | 形式化（formalized as MDP 用马尔可夫决策过程来形式化表述） | "commonly formalized as Markov Decision Process" |
| integration | n. | 整合、融合（本文指强化学习与规划的融合） | "presents a survey of the integration of" |
| dynamics | n. | 动力学（dynamics model 描述环境状态如何随时间演变的模型） | "we systematically cover approaches to dynamics model" |
| stochasticity | n. | 随机性（环境或模型的输出带有随机性） | "challenges like dealing with stochasticity, uncertainty, partial" |
| uncertainty | n. | 不确定性（对模型或环境的不确定） | "dealing with stochasticity, uncertainty, partial observability" |
| observability | n. | 可观测性（partial observability 只能观测到部分状态信息） | "uncertainty, partial observability, and temporal abstraction" |
| allocate | v. | 分配（allocate budgets 分配预算/资源） | "what budgets to allocate to planning and" |
| implicit | adj. | 隐含的（implicit model-based RL 隐式基于模型的强化学习，不显式建模） | "we also discuss implicit model-based RL" |
| end-to-end | adj. | 端到端的（直接从输入到输出的整体学习，不做中间步骤） | "as an end-to-end alternative for model learning" |
| hierarchical | adj. | 分层的（hierarchical RL 分层强化学习，把任务拆成层级结构） | "like hierarchical RL and transfer learning" |
| transfer learning | phr. | 迁移学习（把已学知识迁移到新任务的学习范式） | "hierarchical RL and transfer learning" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

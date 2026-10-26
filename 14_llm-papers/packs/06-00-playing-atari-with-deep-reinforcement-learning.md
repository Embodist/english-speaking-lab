---
type: paper-pack
paper_id: "06-00"
stage: 6
title: "Playing Atari with Deep Reinforcement Learning"
pdf: "/home/user/llm-papers/06_强化学习/PDF/00_DQN_PlayingAtari.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 06-00 Playing Atari with Deep Reinforcement Learning

**中文标题**：《用深度强化学习玩 Atari 游戏》

**一句话概括**：首次提出用深度卷积神经网络直接从原始像素学习控制策略（DQN），在 7 款 Atari 2600 游戏中的 6 款超过此前所有方法，3 款超过人类专家。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| outperform | /aʊtpəfˈɔːm/ | 胜过、优于（学术高频词，超过此前所有方法） | S |
| surpass | /səpˈas/ | 超过（surpasses a human expert 超过人类专家水平） | S |
| reinforcement learning | /ɹˌiːɪnfˈɔːsmənt lˈɜːnɪŋ/ | 强化学习（智能体通过与环境试错交互、按奖励信号学习决策的范式） | A |
| variant | /vˈeəɹiənt/ | 变体（a variant of Q-learning Q 学习的一种变体） | A |
| estimate | /ˈɛstɪmət/ | 估计、估算（估计未来奖励的价值函数） | A |
| high-dimensional | /hˈaɪdaɪmˈɛnʃənəl/ | 高维的（输入数据维度很高，如整幅图像的像素） | A |
| sensory | /sˈɛnsəɹi/ | 感官的（sensory input 感官输入，本文指游戏画面像素） | A |
| raw | /ɹˈɔː/ | 原始的、未经处理的（raw pixels 原始像素，直接输入图像） | A |
| control policies | /kəntɹˈəʊl pˈɒlɪsiz/ | 控制策略（policy 策略：状态到动作的映射规则） | B |
| convolutional neural network | /kɒnvəlˈuːʃənəl njˈuːɹəl nˈɛtwɜːk/ | 卷积神经网络（CNN，擅长处理图像的网络结构） | B |
| pixel | /pˈɪksəl/ | 像素（图像的最小组成单元） | B |
| reward | /ɹɪwˈɔːd/ | 奖励（强化学习中环境给智能体的得分信号） | B |

### 原句（保留完整句子）

- **outperform** — “Since this approach was able to outperform the best human backgammon players 20 years ago, it is natural to wonder whether two decades of hardware improvements, coupled with modern deep neural network architectures and scalable RL algorithms might produce significant progress.”
- **surpass** — “Even our base model surpasses all previously published models and ensembles, at a fraction of the training cost of any of the competitive models.”
- **reinforcement learning** — “1 Introduction Learning to control agents directly from high-dimensional sensory inputs like vision and speech is one of the long-standing challenges of reinforcement learning (RL).”
- **variant** — “The model is a convolutional neural network, trained with a variant of Q-learning, whose input is raw pixels and whose output is a value function estimating future rewards.”
- **estimate** — “Instead, it is common to use a function approximator to estimate the action-value function, Q(s, a; θ) ≈ Q∗ (s, a).”
- **high-dimensional** — “1 Introduction Learning to control agents directly from high-dimensional sensory inputs like vision and speech is one of the long-standing challenges of reinforcement learning (RL).”
- **sensory** — “1 Introduction Learning to control agents directly from high-dimensional sensory inputs like vision and speech is one of the long-standing challenges of reinforcement learning (RL).”
- **raw** — “The model is a convolutional neural network, trained with a variant of Q-learning, whose input is raw pixels and whose output is a value function estimating future rewards.”
- **control policies** — “This paper demonstrates that a convolutional neural network can overcome these challenges to learn successful control policies from raw video data in complex RL environments.”
- **convolutional neural network** — “The model is a convolutional neural network, trained with a variant of Q-learning, whose input is raw pixels and whose output is a value function estimating future rewards.”
- **pixel** — “The emulator’s internal state is not observed by the agent; instead it observes an image xt ∈ Rd from the emulator, which is a vector of raw pixel values representing the current screen.”
- **reward** — “RL algorithms, on the other hand, must be able to learn from a scalar reward signal that is frequently sparse, noisy and delayed.”

## Abstract（自动提取）

> TITLE: Playing Atari with Deep Reinforcement Learning ABSTRACT: We present the first deep learning model to successfully learn control policies directly from high-dimensional sensory input using reinforcement learning. The model is a convolutional neural network, trained with a variant of Q-learning, whose input is raw pixels and whose output is a value function estimating future rewards. We apply our method to seven Atari 2600 games from the Arcade Learning Environment, with no adjustment of the architecture or learning algorithm. We find that it outperforms all previous approaches on six of the games and surpasses a human expert on three of them.

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

PDF：`/home/user/llm-papers/06_强化学习/PDF/00_DQN_PlayingAtari.pdf`

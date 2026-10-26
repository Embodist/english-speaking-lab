---
type: paper-pack
paper_id: "05-03"
stage: 5
title: "Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model"
pdf: "/home/user/llm-papers/05_世界模型/PDF/03_MuZero.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 05-03 Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model

**中文标题**：用学习到的模型规划，称霸 Atari、围棋、国际象棋与将棋（MuZero）

**一句话概括**：提出 MuZero 算法，将基于树的搜索与学习到的模型结合，无需环境动力学和规则知识，在 57 个 Atari 游戏及围棋、国际象棋、将棋上取得超越人类或匹敌 AlphaZero 的性能。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| struggle | /stɹˈʌɡəl/ | 表现吃力、难以成功 | A |
| underlying | /ˌʌndəlˈaɪɪŋ/ | 底层的、内在的；未直接给出的 | A |
| simulator | /sˈɪmjʊlˌeɪtə/ | 模拟器；能完美模拟环境的程序 | A |
| pursuit | /pəsˈuːt/ | 追求、探索 | A |
| superhuman | /sˈuːpəhjˌuːmən/ | 超越人类水平的 | B |
| canonical | /kɐnˈɒnɪkəl/ | 经典的、公认标准的 | B |
| governing | /ɡˈʌvənɪŋ/ | 支配、控制（环境状态如何变化的） | B |
| iteratively | /ˈɪtəɹətˌɪvli/ | 迭代地；反复应用模型 | B |
| value function | /vˈaljuː fˈʌŋkʃən/ | 价值函数；评估状态（动作）好坏的函数 | B |
| tree-based search | /tɹˈiːbˈeɪst sˈɜːtʃ/ | 基于树的搜索；如蒙特卡洛树搜索 | B |
| state of the art | /stˈeɪt ˈɒv ðˈə ˈɑːt/ | 最先进水平 | B |
| supplied with | /səplˈaɪd wˈɪð/ | 被提供、给予 | B |

### 原句（保留完整句子）

- **struggle** — “However, these approaches still 6.2 In-Context Learning struggle in exploring the vast space of effective prompts.”
- **underlying** — “In this work we present the MuZero algorithm which, by combining a tree-based search with a learned model, achieves superhuman performance in a range of challenging and visually complex domains, without any knowledge of their underlying dynamics.”
- **simulator** — “Tree-based planning methods have enjoyed huge success in challenging domains, such as chess and Go, where a perfect simulator is available.”
- **pursuit** — “Abstract Constructing agents with planning capabilities has long been one of the main challenges in the pursuit of artificial intelligence.”
- **superhuman** — “In this work we present the MuZero algorithm which, by combining a tree-based search with a learned model, achieves superhuman performance in a range of challenging and visually complex domains, without any knowledge of their underlying dynamics.”
- **canonical** — “When evaluated on 57 different Atari games - the canonical video game environment for testing AI techniques, in which model-based planning approaches have historically struggled - our new algorithm achieved a new state of the art.”
- **governing** — “However, in real-world problems the dynamics governing the environment are often complex and unknown.”
- **iteratively** — “MuZero learns a model that, when applied iteratively, predicts the quantities most directly relevant to planning: the reward, the action-selection policy, and the value function.”
- **value function** — “MuZero learns a model that, when applied iteratively, predicts the quantities most directly relevant to planning: the reward, the action-selection policy, and the value function.”
- **tree-based search** — “In this work we present the MuZero algorithm which, by combining a tree-based search with a learned model, achieves superhuman performance in a range of challenging and visually complex domains, without any knowledge of their underlying dynamics.”
- **state of the art** — “When evaluated on 57 different Atari games - the canonical video game environment for testing AI techniques, in which model-based planning approaches have historically struggled - our new algorithm achieved a new state of the art.”
- **supplied with** — “When evaluated on Go, chess and shogi, without any knowledge of the game rules, MuZero matched the superhuman performance of the AlphaZero algorithm that was supplied with the game rules.”

## Abstract（自动提取）

> TITLE: Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model ABSTRACT: Constructing agents with planning capabilities has long been one of the main challenges in the pursuit of artificial intelligence. Tree-based planning methods have enjoyed huge success in challenging domains, such as chess and Go, where a perfect simulator is available. However, in real-world problems the dynamics governing the environment are often complex and unknown. In this work we present the MuZero algorithm which, by combining a tree-based search with a learned model, achieves superhuman performance in a range of challenging and visually complex domains, without any knowledge of their underlying dynamics. MuZero learns a model that, when applied iteratively, predicts the quantities most directly relevant to planning: the reward, the action-selection policy, and the value function. When evaluated on 57 different Atari games - the canonical video game environment for testing AI techniques, in which model-based planning approaches have historically struggled - our new algorithm achieved a new state of the art. When evaluated on Go, chess and shogi, without any knowledge of the game rules, MuZero matched the superhuman performance of the AlphaZero algorithm that was supplied with the game rules.

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

PDF：`/home/user/llm-papers/05_世界模型/PDF/03_MuZero.pdf`

---
type: paper-pack
paper_id: "05-10"
stage: 5
title: "IRIS: Implicit Reinforcement without Interaction at Scale for Learning Control from Offline Robot Manipulation Data"
pdf: "/home/user/llm-papers/05_世界模型/PDF/10_IRIS.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 05-10 IRIS: Implicit Reinforcement without Interaction at Scale for Learning Control from Offline Robot Manipulation Data

**中文标题**：IRIS：大规模无交互隐式强化学习——从离线机器人操作数据学习控制

**一句话概括**：提出 IRIS 框架，把控制问题分解为目标条件低级控制器（模仿短演示片段）与高层目标选择机制（组合次优解），从而从大规模离线演示数据集纯离线学习出高性能策略。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| manipulation | /mənˌɪpjʊlˈeɪʃən/ | 操作；机器人操控物体 | A |
| suboptimal | /sʌbˈɒptɪməl/ | 次优的；不是最优的方案 | A |
| demonstrations | /dˌɛmənstɹˈeɪʃənz/ | 演示数据；专家示范的轨迹 | A |
| imitate | /ˈɪmɪtˌeɪt/ | 模仿 | A |
| performant | /pəfˈɔːmənt/ | 性能良好的、高效的 | A |
| factorizes | /fˈaktəɹˌaɪzɪz/ | 分解；把复杂问题拆成几个子部分 | B |
| goal-conditioned | /ɡˈəʊlkəndˈɪʃənd/ | 以目标为条件的；输入中带目标信息 | B |
| crowdsourcing | /kɹˈaʊdsɔːsɪŋ/ | 众包；通过大众网络收集数据 | B |
| substantial diversity | /səbstˈanʃəl daɪvˈɜːsɪti/ | 显著多样性；数据差异很大 | B |
| offline learning | /ˈɒflaɪn lˈɜːnɪŋ/ | 离线学习；不与环境交互、只用固定数据 | B |
| short-horizon | /ʃˈɔːthəɹˈaɪzən/ | 短时程的；步骤很少的任务 | B |
| controller | /kəntɹˈəʊlə/ | 控制器；控制智能体的策略 | B |

### 原句（保留完整句子）

- **manipulation** — “In 2017, the Transformer model \[22\] was introsponses, e.g., rejecting to answer insulting questions. duced by Google, and the OpenAI team quickly adapted • Tools manipulation.”
- **suboptimal** — “This decision appears suboptimal for both modeling and practical reasons, as follows.”
- **demonstrations** — “"we collect a dataset of labeler demonstrations of the desired model behavior"”
- **imitate** — “Furthermore, as a behavior cloning method, SFT Since SFT and RLHF are two major adaptation tuning aims to imitate the behaviors (without explorations) of the methods for LLMs, it is important to understand the con- experts who construct the demonstration data.”
- **performant** — “While there is significant uncertainty extrapolating out many orders of magnitude, our analysis clearly suggests that given the training compute budget for many current LLMs, smaller models should have been trained on more tokens to achieve the most performant model.”
- **factorizes** — “IRIS factorizes the control problem into a goal-conditioned low-level controller”
- **goal-conditioned** — “To better plan and complete specific goals, they propose a goal-conditioned planning schema where Monte Carlo Tree Search (MCTS) is utilized to search for the true embodied task goal.”
- **crowdsourcing** — “However, LLMs are often sensitive to the evaldisinformation tasks, while Chatbot Arena \[729\] constructs uation settings, including the question prompts, zero-shot or a crowdsourcing platform that allows users to engage in few-shot tests, and the answer parsing methods.”
- **substantial diversity** — “The data can exhibit substantial diversity”
- **offline learning** — “performant policies can be learned from purely offline learning”
- **short-horizon** — “For the baseline, the goal is set to the last frame of the original short-horizon trajectories.”
- **controller** — “HuggingGPT \[437\] introduces the models available in 6.4.4 Plan Refinement HuggingFace and regards LLMs as the controller to select With access to feedback from the environment, the task suitable models based on their descriptions and aggregate planner can accordingly refine its current plan and iteratheir results as the final solution. tively go through the “planning – execution – refinement” loop for better results.”

## 摘要提示（PDF 文本不可提取）

> 提出 IRIS 框架，把控制问题分解为目标条件低级控制器（模仿短演示片段）与高层目标选择机制（组合次优解），从而从大规模离线演示数据集纯离线学习出高性能策略。

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

PDF：`/home/user/llm-papers/05_世界模型/PDF/10_IRIS.pdf`

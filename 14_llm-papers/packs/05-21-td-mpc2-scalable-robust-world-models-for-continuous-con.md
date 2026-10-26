---
type: paper-pack
paper_id: "05-21"
stage: 5
title: "TD-MPC2: Scalable, Robust World Models for Continuous Control"
pdf: "/home/user/llm-papers/05_世界模型/PDF/21_TDMPC2.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 05-21 TD-MPC2: Scalable, Robust World Models for Continuous Control

**中文标题**：TD-MPC2：面向连续控制的可扩展、鲁棒世界模型

**一句话概括**：提出 TD-MPC2，在 TD-MPC 之上做系列改进：用单一超参数集在覆盖 4 个任务域的 104 个在线 RL 任务上稳定超越基线，并成功训练出单个 3.17 亿参数、执行 80 个任务的智能体。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| robust | /ɹəʊbˈʌst/ | 鲁棒的；稳定可靠的 | S |
| latent space | /lˈeɪtənt spˈeɪs/ | 潜空间；低维隐藏表示空间 | S |
| implicit | /ɪmplˈɪsɪt/ | 隐式的；不显式输出的 | A |
| baselines | /bˈeɪslaɪnz/ | 基线；对比用的基准方法 | A |
| model-based | /mˈɒdəlbˈeɪst/ | 基于模型的；先学习环境模型 | A |
| decoder-free | /dɪkˈəʊdəfɹˈiː/ | 无解码器的；只学编码不重建图像 | B |
| trajectory optimization | /tɹədʒˈɛktəɹi ˌɒptɪmaɪzˈeɪʃən/ | 轨迹优化；寻找最优行动序列 | B |
| hyperparameters | /hˌaɪpəpəɹˈamɪtəz/ | 超参数；训练前设定的参数 | B |
| embodiments | /ɛmbˈɒdɪmənts/ | 具身形态；机器人的不同身体结构 | B |
| spanning | /spˈanɪŋ/ | 覆盖、横跨 | B |
| consistently | /kənsˈɪstəntli/ | 一致地、稳定地 | B |
| action spaces | /ˈakʃən spˈeɪsɪz/ | 动作空间；动作的取值范围 | B |

### 原句（保留完整句子）

- **robust** — “Nevertheless, LLMs may expose work argues that even human evaluation may not be robust bias (e.g., order bias or preference for LLM-generated texts enough \[630, 631, 641, 642\].”
- **latent space** — “"in the latent space of powerful"”
- **implicit** — “Long context modeling is an important it is important to identify more implicit relations between ability for LLMs, and many studies have explored extenddata sources and model abilities.”
- **baselines** — “"trains Transformers faster than existing baselines"”
- **model-based** — “It is built on top of many prior studies, conduct- model-based approach \[731\].”
- **decoder-free** — “a learned implicit (decoder-free) world model”
- **trajectory optimization** — “performs local trajectory optimization”
- **hyperparameters** — “For our base models using the hyperparameters described throughout the paper, each training step took about 0.4 seconds.”
- **embodiments** — “across multiple task domains, embodiments, and action spaces”
- **spanning** — “across 104 online RL tasks spanning 4 diverse task domains”
- **consistently** — “By increasing the discusses the key technique of reinforcement learning from complexity and diversity of the Self-Instruct-52K dataset human feedback (RLHF) for alignment tuning. respectively, the chat and QA performance of LLaMA can be consistently improved, e.g., from 37.52 to 39.73 in MMLU 5.2.1 Background and Criteria for Alignment for LLaMA (7B).”
- **action spaces** — “embodiments, and action spaces”

## 摘要提示（PDF 文本不可提取）

> TITLE: TD-MPC2: Scalable, Robust World Models for Continuous Control ABSTRACT: TD-MPC is a model-based reinforcement learning (RL) algorithm that performs local trajectory optimization in the latent space of a learned implicit (decoder-free) world model. In this work, we present TD-MPC2: a series of improvements upon the TD-MPC algorithm. We demonstrate that TD-MPC2 improves significantly over baselines across 104 online RL tasks spanning 4 diverse task domains, achieving consistently strong results with a single set of hyperparameters. We further show that agent capabilities increase with model and data size, and successfully train a single 317M parameter agent to perform 80 tasks across multiple task domains, embodiments, and action spaces. We conclude with an account of lessons, opportunities, and risks associated with large TD-MPC2 agents. Explore videos, models, data, code, and more at https://tdmpc2.com

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

PDF：`/home/user/llm-papers/05_世界模型/PDF/21_TDMPC2.pdf`

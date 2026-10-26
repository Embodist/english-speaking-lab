---
type: paper-pack
paper_id: "01-22"
stage: 1
title: "ReAct: Synergizing Reasoning and Acting in Language Models"
pdf: "/home/user/llm-papers/01_大模型/PDF/22_ReAct.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-22 ReAct: Synergizing Reasoning and Acting in Language Models

**中文标题**：ReAct：在大语言模型中协同推理与行动

**一句话概括**：提出 ReAct，让大模型交替生成推理轨迹与动作，并与外部环境（如 Wikipedia API）交互，缓解幻觉并提升决策任务的性能与可解释性。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| interleaved | /ˌɪntəlˈiːvd/ | 交错的（推理与行动交替进行） | S |
| trajectories | /tɹədʒˈɛktəɹiz/ | 轨迹（完成任务的过程记录） | A |
| synergy | /sˈɪnədʒi/ | 协同效应（两者结合产生更大效果） | A |
| diverse | /daɪvˈɜːs/ | 多样的 | A |
| hallucination | /hɐlˌuːsɪnˈeɪʃən/ | 幻觉（模型编造不实内容） | A |
| interactive | /ˌɪntəɹˈaktɪv/ | 交互式的（与环境互动） | B |
| traces | /tɹˈeɪsɪz/ | 轨迹（推理过程的记录） | B |
| induce | /ɪndjˈuːs/ | 归纳、引导 | B |
| interface | /ˈɪntəfˌeɪs/ | 对接、交互 | B |
| interpretability | /ɪntˌɜːpɹɪtəbˈɪlɪti/ | 可解释性（过程可被人理解） | B |

### 原句（保留完整句子）

- **interleaved** — “In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with and gather additional information from external sources such as knowledge bases or environments.”
- **trajectories** — “Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes prevalent issues of hallucination and error propagation in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generating human-like task-solving trajectories that are more interpretable than baselines without reasoning traces.”
- **synergy** — “In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with and gather additional information from external sources such as knowledge bases or environments.”
- **diverse** — “We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines in addition to improved human interpretability and trustworthiness.”
- **hallucination** — “Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes prevalent issues of hallucination and error propagation in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generating human-like task-solving trajectories that are more interpretable than baselines without reasoning traces.”
- **interactive** — “Furthermore, on two interactive decision making benchmarks (ALFWorld and WebShop), ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples.”
- **traces** — “In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with and gather additional information from external sources such as knowledge bases or environments.”
- **induce** — “In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with and gather additional information from external sources such as knowledge bases or environments.”
- **interface** — “In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with and gather additional information from external sources such as knowledge bases or environments.”
- **interpretability** — “We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines in addition to improved human interpretability and trustworthiness.”

## Abstract（自动提取）

> TITLE: ReAct: Synergizing Reasoning and Acting in Language Models ABSTRACT: While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information. We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines, as well as improved human interpretability and trustworthiness over methods without reasoning or acting components. Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning trace

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

PDF：`/home/user/llm-papers/01_大模型/PDF/22_ReAct.pdf`

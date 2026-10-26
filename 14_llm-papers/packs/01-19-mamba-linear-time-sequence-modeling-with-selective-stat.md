---
type: paper-pack
paper_id: "01-19"
stage: 1
title: "Mamba: Linear-Time Sequence Modeling with Selective State Spaces"
pdf: "/home/user/llm-papers/01_大模型/PDF/19_Mamba_SSM.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-19 Mamba: Linear-Time Sequence Modeling with Selective State Spaces

**中文标题**：Mamba：基于选择性状态空间的线性时间序列建模

**一句话概括**：提出 Mamba 选择性状态空间模型，让 SSM 参数随输入内容变化，以线性时间复杂度和快速推理超越同规模 Transformer 的语言建模性能。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| recurrent | /ɹɪkˈʌɹənt/ | 循环的（RNN 类逐时间步结构） | A |
| propagate | /pɹˈɒpɐɡˌeɪt/ | 传播（信息沿序列传递） | A |
| backbone | /bˈakbəʊn/ | 主干网络（通用的序列模型底座） | A |
| linear | /lˈɪniə/ | 线性的（计算量随序列长度线性增长） | B |
| selective | /sɪlˈɛktɪv/ | 选择性的（按内容决定保留或遗忘信息） | B |
| state space models | /stˈeɪt spˈeɪs mˈɒdəlz/ | 状态空间模型（SSM，一类序列建模方法） | B |
| universally | /jˌuːnɪvˈɜːsəli/ | 普遍地 | B |
| subquadratic-time | /sˌʌbkwədɹˈatɪktˈaɪm/ | 亚二次方时间的（比二次方更省计算） | B |
| gated convolution | /ɡˈeɪtɪd kɒnvəlˈuːʃən/ | 门控卷积（带门控机制的卷积） | B |
| modalities | /məʊdˈalɪtiz/ | 模态（数据类型，如语言、音频） | B |
| hardware-aware | /hˈɑːdweəɹɐwˈeə/ | 硬件感知的（针对硬件特性设计算法） | B |

### 原句（保留完整句子）

- **recurrent** — “Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and structured state space models (SSMs) have been developed to address Transformers’ computational inefficiency on long sequences, but they have not performed as well as attention on important modalities such as language.”
- **propagate** — “First, simply letting the SSM parameters be functions of the input addresses their weakness with discrete modalities, allowing the model to selectively propagate or forget information along the sequence length dimension depending on the current token.”
- **backbone** — “As a general sequence model backbone, Mamba achieves state-of-the-art performance across several modalities such as language, audio, and genomics.”
- **linear** — “Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and structured state space models (SSMs) have been developed to address Transformers’ computational inefficiency on long sequences, but they have not performed as well as attention on important modalities such as language.”
- **selective** — “We integrate these selective SSMs into a simplified end-to-end neural network architecture without attention or even MLP blocks (Mamba).”
- **state space models** — “Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and structured state space models (SSMs) have been developed to address Transformers’ computational inefficiency on long sequences, but they have not performed as well as attention on important modalities such as language.”
- **universally** — “Huang, “RRHF: rank responses to align language tuning v2: Prompt tuning can be comparable to finemodels with human feedback without tears,” tuning universally across scales and tasks,” CoRR, CoRR, vol. abs/2304.05302, 2023. \[Online\].”
- **subquadratic-time** — “Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and structured state space models (SSMs) have been developed to address Transformers’ computational inefficiency on long sequences, but they have not performed as well as attention on important modalities such as language.”
- **gated convolution** — “Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and structured state space models (SSMs) have been developed to address Transformers’ computational inefficiency on long sequences, but they have not performed as well as attention on important modalities such as language.”
- **modalities** — “Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and structured state space models (SSMs) have been developed to address Transformers’ computational inefficiency on long sequences, but they have not performed as well as attention on important modalities such as language.”
- **hardware-aware** — “Second, even though this change prevents the use of efficient convolutions, we design a hardware-aware parallel algorithm in recurrent mode.”

## Abstract（自动提取）

> TITLE: Mamba: Linear-Time Sequence Modeling with Selective State Spaces ABSTRACT: Foundation models, now powering most of the exciting applications in deep learning, are almost universally based on the Transformer architecture and its core attention module. Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and structured state space models (SSMs) have been developed to address Transformers' computational inefficiency on long sequences, but they have not performed as well as attention on important modalities such as language. We identify that a key weakness of such models is their inability to perform content-based reasoning, and make several improvements. First, simply letting the SSM parameters be functions of the input addresses their weakness with discrete modalities, allowing the model to selectively propagate or forget information along the sequence length dimension depending on the current token. Second, even though this change prevents the use of efficient convolutions, we design a hardware-aware parallel algorithm in recurrent mode. We integrate these selective SSMs into a simplified end-to-end neural network architecture without attention or even MLP blocks (Mamba). Mamba enjoys fast inference (5$\times$ higher throughput than Transformers) and linear scaling in sequence length, and its performance improves on real d

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

PDF：`/home/user/llm-papers/01_大模型/PDF/19_Mamba_SSM.pdf`

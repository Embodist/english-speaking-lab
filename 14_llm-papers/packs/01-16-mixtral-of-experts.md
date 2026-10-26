---
type: paper-pack
paper_id: "01-16"
stage: 1
title: "Mixtral of Experts"
pdf: "/home/user/llm-papers/01_大模型/PDF/16_Mixtral_MoE.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-16 Mixtral of Experts

**中文标题**：专家混合模型 Mixtral

**一句话概括**：发布 Mixtral 8x7B 稀疏专家混合模型：每层 8 个前馈专家、每个词元只激活 2 个，性能全面匹敌或超越 Llama 2 70B 与 GPT-3.5。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| architecture | /ˈɑːkɪtˌɛktʃə/ | 架构（模型整体结构） | S |
| sparse | /spˈɑːs/ | 稀疏的（每次只激活少量参数） | S |
| feedforward | /fiːdfˈɔːwəd/ | 前馈的（全连接网络层） | A |
| combine | /kəmbˈaɪn/ | 合并、结合 | A |
| surpasses | /səpˈasɪz/ | 超过 | A |
| mixture of experts | /mˈɪkstʃə ˈɒv ˈɛkspɜːts/ | 专家混合（MoE，多个子网络按输入分工） | B |
| router | /ɹˈuːtə/ | 路由的（负责选择专家的网络） | B |
| timestep | /tˈaɪmstɛp/ | 时间步（生成序列中的每一步） | B |
| active parameters | /ˈaktɪv pəɹˈamɪtəz/ | 激活参数（实际参与计算的参数） | B |
| vastly | /vˈastli/ | 极大地 | B |

### 原句（保留完整句子）

- **architecture** — “Mixtral has the same architecture as Mistral 7B, with the difference that each layer is composed of 8 feedforward blocks (i.e. experts).”
- **sparse** — “Code: https://github.com/mistralai/mistral-src Webpage: https://mistral.ai/news/mixtral-of-experts/ 1 Introduction In this paper, we present Mixtral 8x7B, a sparse mixture of experts model (SMoE) with open weights, licensed under Apache 2.0.”
- **feedforward** — “Mixtral has the same architecture as Mistral 7B, with the difference that each layer is composed of 8 feedforward blocks (i.e. experts).”
- **combine** — “For every token, at each layer, a router network selects two experts to process the current state and combine their outputs.”
- **surpasses** — “We also provide a model finetuned to follow instructions, Mixtral 8x7B – Instruct, that surpasses GPT-3.5 Turbo, Claude-2.1, Gemini Pro, and Llama 2 70B – chat model on human benchmarks.”
- **mixture of experts** — “Code: https://github.com/mistralai/mistral-src Webpage: https://mistral.ai/news/mixtral-of-experts/ 1 Introduction In this paper, we present Mixtral 8x7B, a sparse mixture of experts model (SMoE) with open weights, licensed under Apache 2.0.”
- **router** — “For every token, at each layer, a router network selects two experts to process the current state and combine their outputs.”
- **timestep** — “Even though each token only sees two experts, the selected experts can be different at each timestep.”
- **active parameters** — “As a result, each token has access to 47B parameters, but only uses 13B active parameters during inference.”
- **vastly** — “In particular, Mixtral vastly outperforms Llama 2 70B on mathematics, code generation, and multilingual benchmarks.”

## Abstract（自动提取）

> TITLE: Mixtral of Experts ABSTRACT: We introduce Mixtral 8x7B, a Sparse Mixture of Experts (SMoE) language model. Mixtral has the same architecture as Mistral 7B, with the difference that each layer is composed of 8 feedforward blocks (i.e. experts). For every token, at each layer, a router network selects two experts to process the current state and combine their outputs. Even though each token only sees two experts, the selected experts can be different at each timestep. As a result, each token has access to 47B parameters, but only uses 13B active parameters during inference. Mixtral was trained with a context size of 32k tokens and it outperforms or matches Llama 2 70B and GPT-3.5 across all evaluated benchmarks. In particular, Mixtral vastly outperforms Llama 2 70B on mathematics, code generation, and multilingual benchmarks. We also provide a model fine-tuned to follow instructions, Mixtral 8x7B - Instruct, that surpasses GPT-3.5 Turbo, Claude-2.1, Gemini Pro, and Llama 2 70B - chat model on human benchmarks. Both the base and instruct models are released under the Apache 2.0 license.

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

PDF：`/home/user/llm-papers/01_大模型/PDF/16_Mixtral_MoE.pdf`

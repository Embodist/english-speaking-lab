---
type: paper-pack
paper_id: "01-34"
stage: 1
title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"
pdf: "/home/user/llm-papers/01_大模型/PDF/34_DeepSeekMath_GRPO.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-34 DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

**中文标题**：DeepSeekMath：突破开放语言模型的数学推理极限

**一句话概括**：发布 DeepSeekMath 7B，用精心筛选的数学语料继续预训练并提出 GRPO 强化学习方法，在竞赛级 MATH 基准上达到 51.7%。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| concurrently | /kəŋkˈʌɹəntli/ | 同时 | A |
| meticulously | /mɛtˈɪkjʊləsli/ | 一丝不苟地、精心地 | A |
| harness | /hˈɑːnɪs/ | 利用、挖掘 | A |
| poses | /pˈəʊzɪz/ | 构成（构成挑战） | B |
| structured | /stɹˈʌktʃəd/ | 结构化的（有严密逻辑结构） | B |
| sourced from | /sˈɔːst fɹˈɒm/ | 来源于 | B |
| impressive | /ɪmpɹˈɛsɪv/ | 令人印象深刻的、亮眼的 | B |
| competition-level | /kˌɒmpətˈɪʃənlˈɛvəl/ | 竞赛级别的（数学竞赛难度） | B |
| relying on | /ɹɪlˈaɪɪŋ ˈɒn/ | 依赖 | B |
| attributed to | /ɐtɹˈɪbjuːtɪd tˈuː/ | 归因于 | B |

### 原句（保留完整句子）

- **concurrently** — “For instance, Tree of Thoughts (ToT) \[444\] empowers LLMs to engage in the decision-making process by concurrently Numerical Computation exploring and self-evaluating various reasoning paths.”
- **meticulously** — “Additionally, we scrutinize the burgeoning field of autonomous-driving world models, meticulously delineating their indispensable role in reshaping transportation and urban mobility.”
- **harness** — “This feature can be harnessed through specific language.”
- **poses** — “"Mathematical reasoning poses a significant challenge for language models"”
- **structured** — “"due to its complex and structured nature"”
- **sourced from** — “"with 120B math-related tokens sourced from Common Crawl"”
- **impressive** — “In effect \[90\]: declarative instructions and direct interrogatives light of the impressive generalization capabilities exhibited are erroneously perceived as the beginning of conversations, by LLMs, there are also studies that extend their pre-training thus leading to a decline in the efficacy of the instructions. corpus to more specialized datasets, such as multilingual data, scientific data, and code, endowing LLMs with specific • Books.”
- **competition-level** — “Vinyals, “Competition-level “Jurassic-1: Technical details and evaluation,” White code generation with alphacode,” Science, 2022.”
- **relying on** — “"without relying on external toolkits and voting techniques"”
- **attributed to** — “"is attributed to two key factors"”

## 摘要提示（PDF 文本不可提取）

> TITLE: DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models ABSTRACT: Mathematical reasoning poses a significant challenge for language models due to its complex and structured nature. In this paper, we introduce DeepSeekMath 7B, which continues pre-training DeepSeek-Coder-Base-v1.5 7B with 120B math-related tokens sourced from Common Crawl, together with natural language and code data. DeepSeekMath 7B has achieved an impressive score of 51.7% on the competition-level MATH benchmark without relying on external toolkits and voting techniques, approaching the performance level of Gemini-Ultra and GPT-4. Self-consistency over 64 samples from DeepSeekMath 7B achieves 60.9% on MATH. The mathematical reasoning capability of DeepSeekMath is attributed to two key factors: First, we harness the significant potential of publicly available web data through a meticulously engineered data selection pipeline. Second, we introduce Group Relative Policy Optimization (GRPO), a variant of Proximal Policy Optimization (PPO), that enhances mathematical reasoning abilities while concurrently optimizing the memory usage of PPO.

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

PDF：`/home/user/llm-papers/01_大模型/PDF/34_DeepSeekMath_GRPO.pdf`

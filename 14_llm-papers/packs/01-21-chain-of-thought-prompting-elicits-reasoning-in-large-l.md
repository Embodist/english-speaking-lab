---
type: paper-pack
paper_id: "01-21"
stage: 1
title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
pdf: "/home/user/llm-papers/01_大模型/PDF/21_ChainOfThought.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-21 Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

**中文标题**：思维链提示激发大语言模型的推理能力

**一句话概括**：提出思维链提示：在提示中给出少量中间推理步骤示例，即可显著提升大模型在算术、常识与符号推理任务上的表现。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| intermediate | /ˌɪntəmˈiːdiət/ | 中间的 | A |
| symbolic | /sɪmbˈɒlɪk/ | 符号的（符号逻辑类推理） | A |
| arithmetic | /ɐɹˈɪθmətˌɪk/ | 算术 | A |
| chain of thought | /tʃˈeɪn ˈɒv θˈɔːt/ | 思维链（一系列中间推理步骤） | B |
| significantly | /sɪɡnˈɪfɪkəntli/ | 显著地 | B |
| emerge | /ɪmˈɜːdʒ/ | 涌现（自然出现、无需专门训练） | B |
| exemplars | /ɛɡzˈɛmpləz/ | 示例（示范样本） | B |
| commonsense | /kˌɒmənsˈɛns/ | 常识 | B |
| striking | /stɹˈaɪkɪŋ/ | 惊人的 | B |
| verifier | /vˈɛɹɪfˌaɪə/ | 验证器（检查答案正确性的模型） | B |

### 原句（保留完整句子）

- **intermediate** — “A chain of thought is a series of intermediate natural language reasoning steps that lead to the final output, and we refer to this approach as chain-of-thought prompting.”
- **symbolic** — “Experiments on three large language models show that chain-of-thought prompting improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks.”
- **arithmetic** — “Experiments on three large language models show that chain-of-thought prompting improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks.”
- **chain of thought** — “In particular, we show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain-ofthought prompting, where a few chain of thought demonstrations are provided as exemplars in prompting.”
- **significantly** — “Although the results are relatively robust to the prompt for arithmetic reasoning, we want to be clear that prompt engineering still does matter, and can improve performance significantly in many cases.”
- **emerge** — “In particular, we show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain-ofthought prompting, where a few chain of thought demonstrations are provided as exemplars in prompting.”
- **exemplars** — “In particular, we show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain-ofthought prompting, where a few chain of thought demonstrations are provided as exemplars in prompting.”
- **commonsense** — “Experiments on three large language models show that chain-of-thought prompting improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks.”
- **striking** — “We present empirical evaluations on arithmetic, commonsense, and symbolic reasoning benchmarks, showing that chain-of-thought prompting outperforms standard prompting, sometimes to a striking degree.”
- **verifier** — “For instance, prompting a PaLM 540B with just eight chain-of-thought exemplars achieves state-of-the-art accuracy on the GSM8K benchmark of math word problems, surpassing even finetuned GPT-3 with a verifier.”

## Abstract（自动提取）

> TITLE: Chain-of-Thought Prompting Elicits Reasoning in Large Language Models ABSTRACT: We explore how generating a chain of thought -- a series of intermediate reasoning steps -- significantly improves the ability of large language models to perform complex reasoning. In particular, we show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain of thought prompting, where a few chain of thought demonstrations are provided as exemplars in prompting. Experiments on three large language models show that chain of thought prompting improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks. The empirical gains can be striking. For instance, prompting a 540B-parameter language model with just eight chain of thought exemplars achieves state of the art accuracy on the GSM8K benchmark of math word problems, surpassing even finetuned GPT-3 with a verifier.

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

PDF：`/home/user/llm-papers/01_大模型/PDF/21_ChainOfThought.pdf`

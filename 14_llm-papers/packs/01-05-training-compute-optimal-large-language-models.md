---
type: paper-pack
paper_id: "01-05"
stage: 1
title: "Training Compute-Optimal Large Language Models"
pdf: "/home/user/llm-papers/01_大模型/PDF/05_Chinchilla_TrainingComputeOptimal.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-05 Training Compute-Optimal Large Language Models

**中文标题**：训练算力最优的大语言模型（Chinchilla）

**一句话概括**：发现现有大模型普遍训练不足，提出模型大小与训练数据量应按相同比例同步扩大，并据此训练出全面超越 Gopher 等模型的 Chinchilla。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| benchmark | /bˈɛntʃmɑːk/ | 基准（标准评测集） | S |
| inference | /ˈɪnfəɹəns/ | 推理（用训练好的模型生成输出） | S |
| outperforms | /aʊtpəfˈɔːmz/ | 性能优于、胜过 | A |
| investigate | /ɪnvˈɛstɪɡˌeɪt/ | 研究、调查 | A |
| compute-optimal | /kəmpjˈuːtˈɒptɪməl/ | 算力最优的（给定算力下训练效果最优） | B |
| undertrained | /ˌʌndətɹˈeɪnd/ | 训练不足的（数据量不够、潜力未发挥） | B |
| consequence | /kˈɒnsɪkwəns/ | 结果、后果 | B |
| doubling | /dˈʌblɪŋ/ | 翻倍 | B |
| uniformly | /jˈuːnɪfˌɔːmli/ | 一致地、全面地 | B |
| facilitating | /fəsˈɪlɪtˌeɪtɪŋ/ | 促进、便于 | B |

### 原句（保留完整句子）

- **benchmark** — “As a highlight, Chinchilla reaches a state-of-the-art average accuracy of 67.5% on the MMLU benchmark, greater than a 7% improvement over Gopher.”
- **inference** — “This also means that Chinchilla uses substantially less compute for fine-tuning and inference, greatly facilitating downstream usage.”
- **outperforms** — “Chinchilla uniformly and significantly outperforms Gopher (280B), GPT-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large range of downstream evaluation tasks.”
- **investigate** — “The authors investigate the question of choosing the optimal model size to train for a given compute budget.”
- **compute-optimal** — “Based on our estimated compute-optimal frontier, we predict that for the compute budget used to train Gopher, an optimal model should be 4 times smaller, while being training on 4 times more tokens.”
- **undertrained** — “We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant.”
- **consequence** — “We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant.”
- **doubling** — “"for every doubling of model size the number"”
- **uniformly** — “Chinchilla uniformly and significantly outperforms Gopher (280B), GPT-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large range of downstream evaluation tasks.”
- **facilitating** — “This also means that Chinchilla uses substantially less compute for fine-tuning and inference, greatly facilitating downstream usage.”

## Abstract（自动提取）

> TITLE: Training Compute-Optimal Large Language Models ABSTRACT: We investigate the optimal model size and number of tokens for training a transformer language model under a given compute budget. We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant. By training over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens, we find that for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number of training tokens should also be doubled. We test this hypothesis by training a predicted compute-optimal model, Chinchilla, that uses the same compute budget as Gopher but with 70B parameters and 4$\times$ more more data. Chinchilla uniformly and significantly outperforms Gopher (280B), GPT-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large range of downstream evaluation tasks. This also means that Chinchilla uses substantially less compute for fine-tuning and inference, greatly facilitating downstream usage. As a highlight, Chinchilla reaches a state-of-the-art average accuracy of 67.5% on the MMLU benchmark, greater than a 7% improvement over Gopher.

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

PDF：`/home/user/llm-papers/01_大模型/PDF/05_Chinchilla_TrainingComputeOptimal.pdf`

---
type: paper-pack
paper_id: "01-09"
stage: 1
title: "LLaMA: Open and Efficient Foundation Language Models"
pdf: "/home/user/llm-papers/01_大模型/PDF/09_LLaMA_OpenEfficientFoundation.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-09 LLaMA: Open and Efficient Foundation Language Models

**中文标题**：LLaMA：开放且高效的基础语言模型

**一句话概括**：发布仅用公开数据训练的 LLaMA 系列基础模型（7B–65B），其中 13B 即超过 GPT-3，65B 与 Chinchilla-70B、PaLM-540B 相当。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| state-of-the-art | /stˈeɪtɒvðɪˈɑːt/ | 最先进的 | S |
| competitive | /kəmpˈɛtɪtˌɪv/ | 有竞争力的、不相上下的 | S |
| outperforms | /aʊtpəfˈɔːmz/ | 性能超过 | A |
| foundation | /faʊndˈeɪʃən/ | 基础的（作为底座的大规模预训练模型） | A |
| proprietary | /pɹəpɹˈaɪətəɹi/ | 专有的（不公开的） | A |
| release | /ɹɪlˈiːs/ | 发布、开源 | A |
| collection | /kəlˈɛkʃən/ | 系列、集合 | B |
| trillions | /tɹˈɪliənz/ | 万亿（级别） | B |
| tokens | /tˈəʊkənz/ | 词元（文本切分后的最小处理单元） | B |
| exclusively | /ɛksklˈuːsɪvli/ | 完全地、仅仅 | B |

### 原句（保留完整句子）

- **state-of-the-art** — “Although the non-finetuned version are still far from the state-of-the-art, that is 77.4 of LLaMA-65B is already able to follow basic in- for GPT code-davinci-002 on MMLU (numbers structions, we observe that a very small amount of taken from Iyer et al.”
- **competitive** — “In The focus of this work is to train a series of particular, LLaMA-13B outperforms GPT-3 language models that achieve the best possible per(175B) on most benchmarks, and LLaMA- formance at various inference budgets, by training 65B is competitive with the best models, on more tokens than what is typically used.”
- **outperforms** — “In The focus of this work is to train a series of particular, LLaMA-13B outperforms GPT-3 language models that achieve the best possible per(175B) on most benchmarks, and LLaMA- formance at various inference budgets, by training 65B is competitive with the best models, on more tokens than what is typically used.”
- **foundation** — “13B 20.1 23.4 28.1 31.9 LLaMA We compare LLaMA with other foundation mod- 33B 24.9 28.3 32.9 36.0 els, namely the non-publicly available language 65B 23.8 31.0 35.0 39.9 models GPT-3 (Brown et al., 2020), Gopher (Rae et al., 2021), Chinchilla (Hoffmann et al., 2022) Table 4: NaturalQuestions.”
- **proprietary** — “(2016) obtained state-of-the-art re- resorting to proprietary datasets.”
- **release** — “We release resulting models, called LLaMA, ranges from 7B all our models to the research community1 . to 65B parameters with competitive performance 1 Introduction compared to the best existing LLMs.”
- **collection** — “For instance, We introduce LLaMA, a collection of foundaalthough Hoffmann et al.”
- **trillions** — “"We train our models on trillions of tokens"”
- **tokens** — “In The focus of this work is to train a series of particular, LLaMA-13B outperforms GPT-3 language models that achieve the best possible per(175B) on most benchmarks, and LLaMA- formance at various inference budgets, by training 65B is competitive with the best models, on more tokens than what is typically used.”
- **exclusively** — “Word benchmark, a large scale training dataset to Unlike previous studies, we show that it is possible measure the progress of language models. to achieve state-of-the-art performance by training In the context of neural language models, Joze- exclusively on publicly available data, without fowicz et al.”

## Abstract（自动提取）

> TITLE: LLaMA: Open and Efficient Foundation Language Models ABSTRACT: We introduce LLaMA, a collection of foundation language models ranging from 7B to 65B parameters. We train our models on trillions of tokens, and show that it is possible to train state-of-the-art models using publicly available datasets exclusively, without resorting to proprietary and inaccessible datasets. In particular, LLaMA-13B outperforms GPT-3 (175B) on most benchmarks, and LLaMA-65B is competitive with the best models, Chinchilla-70B and PaLM-540B. We release all our models to the research community.

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

PDF：`/home/user/llm-papers/01_大模型/PDF/09_LLaMA_OpenEfficientFoundation.pdf`

---
type: paper-pack
paper_id: "01-17"
stage: 1
title: "GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding"
pdf: "/home/user/llm-papers/01_大模型/PDF/17_GShard_MoE.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-17 GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding

**中文标题**：GShard：用条件计算与自动分片扩展巨型模型

**一句话概括**：提出 GShard，用轻量注解 API 与 XLA 编译器扩展实现自动分片，把多语言机器翻译的 MoE Transformer 扩展到 6000 亿参数。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| lightweight | /lˈaɪtweɪt/ | 轻量的（简单、负担小） | A |
| scaling | /skˈeɪlɪŋ/ | 扩展（把模型做得更大） | A |
| critical | /kɹˈɪtɪkəl/ | 至关重要的 | A |
| multilingual | /mˌʌltɪlˈɪŋɡwəl/ | 多语言的 | A |
| sharding | /ʃˈɑːdɪŋ/ | 分片（把模型参数切分到多台设备） | B |
| vast | /vˈast/ | 海量的 | B |
| sure-fire | /ʃˈʊəfˈaɪə/ | 稳操胜券的、必定有效的 | B |
| elegant | /ˈɛlɪɡənt/ | 优雅的（简洁巧妙） | B |
| accelerators | /ɐksˈɛləɹˌeɪtəz/ | 加速器（专用计算硬件，如 TPU） | B |
| prior art | /pɹˈaɪə ˈɑːt/ | 现有技术（此前最好的方法） | B |

### 原句（保留完整句子）

- **lightweight** — “GShard is a module composed of a set of lightweight annotation APIs and an extension to the XLA compiler.”
- **scaling** — “Although this trend of scaling is affirmed to be a sure-fire approach for better model quality, there are challenges on the path such as the computation cost, ease of programming, and efficient implementation on parallel devices.”
- **critical** — “This general tendency motivated recent studies to scrutinize the factors playing a critical role in the success of scaling \[17, 18, 19, 20, 3\], including the amounts of training data, the model size, and the computation being utilized as found by past studies.”
- **multilingual** — “GShard enabled us to scale up multilingual neural machine translation Transformer model with Sparsely-Gated Mixture-of-Experts beyond 600 billion parameters using automatic sharding.”
- **sharding** — “GShard enabled us to scale up multilingual neural machine translation Transformer model with Sparsely-Gated Mixture-of-Experts beyond 600 billion parameters using automatic sharding.”
- **vast** — “ChatGPT exhibited superior capacitraining on code data is a very useful practice to improve ties in communicating with humans: possessing a vast store the model capacity of GPT models, especially the reasoning of knowledge, skill at reasoning on mathematical problems, ability.”
- **sure-fire** — “Although this trend of scaling is affirmed to be a sure-fire approach for better model quality, there are challenges on the path such as the computation cost, ease of programming, and efficient implementation on parallel devices.”
- **elegant** — “It provides an elegant way to express a wide range of parallel computation patterns with minimal changes to the existing model code.”
- **accelerators** — “We demonstrate that such a giant model can efficienctly be trained on 2048 TPU v3 accelerators in 4 days to achieve far superior quality for translation from 100 languages to English compared to the prior art.”
- **prior art** — “We demonstrate that such a giant model can efficienctly be trained on 2048 TPU v3 accelerators in 4 days to achieve far superior quality for translation from 100 languages to English compared to the prior art.”

## Abstract（自动提取）

> TITLE: GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding ABSTRACT: Neural network scaling has been critical for improving the model quality in many real-world machine learning applications with vast amounts of training data and compute. Although this trend of scaling is affirmed to be a sure-fire approach for better model quality, there are challenges on the path such as the computation cost, ease of programming, and efficient implementation on parallel devices. GShard is a module composed of a set of lightweight annotation APIs and an extension to the XLA compiler. It provides an elegant way to express a wide range of parallel computation patterns with minimal changes to the existing model code. GShard enabled us to scale up multilingual neural machine translation Transformer model with Sparsely-Gated Mixture-of-Experts beyond 600 billion parameters using automatic sharding. We demonstrate that such a giant model can efficiently be trained on 2048 TPU v3 accelerators in 4 days to achieve far superior quality for translation from 100 languages to English compared to the prior art.

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

PDF：`/home/user/llm-papers/01_大模型/PDF/17_GShard_MoE.pdf`

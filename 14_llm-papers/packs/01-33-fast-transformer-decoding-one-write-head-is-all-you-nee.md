---
type: paper-pack
paper_id: "01-33"
stage: 1
title: "Fast Transformer Decoding: One Write-Head is All You Need"
pdf: "/home/user/llm-papers/01_大模型/PDF/33_MultiQueryAttention.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-33 Fast Transformer Decoding: One Write-Head is All You Need

**中文标题**：快速 Transformer 解码：一个写入头就够了（多查询注意力 MQA）

**一句话概括**：提出多查询注意力 MQA，让所有注意力头共享同一组键值张量，大幅降低内存带宽需求，加速增量式解码。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| variant | /vˈeəɹiənt/ | 变体（某方法的修改版本） | A |
| decoding | /dɪkˈəʊdɪŋ/ | 解码（逐词生成输出） | B |
| powerful alternative | /pˈaʊəfəl ɔːltˈɜːnətˌɪv/ | 强大的替代方案 | B |
| parallelizability | /pˌaɹəlˌɛlaɪzəbˈɪlɪti/ | 可并行性（能同时计算） | B |
| incremental inference | /ˌɪŋkɹɪmˈɛntəl ˈɪnfəɹəns/ | 增量式推理（逐步生成、逐步计算） | B |
| memory-bandwidth | /mˈɛməɹibˈandwɪdθ/ | 内存带宽（单位时间读写内存的量） | B |
| tensors | /tˈɛnsəz/ | 张量（多维数组，此处指键值矩阵） | B |
| shared across | /ʃˈeəd əkɹˈɒs/ | 在所有……之间共享 | B |
| verify | /vˈɛɹɪfˌaɪ/ | 验证 | B |
| incur | /ɪŋkˈɜː/ | 招致、引起 | B |

### 原句（保留完整句子）

- **variant** — “We propose a variant called multi-query attention, where the keys and values are shared across all of the different attention "heads", greatly reducing the size of these tensors and hence the memory bandwidth requirements of incremental decoding.”
- **decoding** — “We propose a variant called multi-query attention, where the keys and values are shared across all of the different attention "heads", greatly reducing the size of these tensors and hence the memory bandwidth requirements of incremental decoding.”
- **powerful alternative** — “"are a powerful alternative to RNNs for moving information"”
- **parallelizability** — “While training these layers is generally fast and simple, due to parallelizability across the length of the sequence, incremental inference (where such paralleization is impossible) is often slow, due to the memory-bandwidth cost of repeatedly loading the large "keys" and "values" tensors.”
- **incremental inference** — “While training these layers is generally fast and simple, due to parallelizability across the length of the sequence, incremental inference (where such paralleization is impossible) is often slow, due to the memory-bandwidth cost of repeatedly loading the large "keys" and "values" tensors.”
- **memory-bandwidth** — “While training these layers is generally fast and simple, due to parallelizability across the length of the sequence, incremental inference (where such paralleization is impossible) is often slow, due to the memory-bandwidth cost of repeatedly loading the large "keys" and "values" tensors.”
- **tensors** — “While training these layers is generally fast and simple, due to parallelizability across the length of the sequence, incremental inference (where such paralleization is impossible) is often slow, due to the memory-bandwidth cost of repeatedly loading the large "keys" and "values" tensors.”
- **shared across** — “We propose a variant called multi-query attention, where the keys and values are shared across all of the different attention "heads", greatly reducing the size of these tensors and hence the memory bandwidth requirements of incremental decoding.”
- **verify** — “We verify experimentally that the resulting models can indeed be much faster to decode, and incur only minor quality degradation from the baseline.”
- **incur** — “We verify experimentally that the resulting models can indeed be much faster to decode, and incur only minor quality degradation from the baseline.”

## Abstract（自动提取）

> TITLE: Fast Transformer Decoding: One Write-Head is All You Need ABSTRACT: Multi-head attention layers, as used in the Transformer neural sequence model, are a powerful alternative to RNNs for moving information across and between sequences. While training these layers is generally fast and simple, due to parallelizability across the length of the sequence, incremental inference (where such paralleization is impossible) is often slow, due to the memory-bandwidth cost of repeatedly loading the large "keys" and "values" tensors. We propose a variant called multi-query attention, where the keys and values are shared across all of the different attention "heads", greatly reducing the size of these tensors and hence the memory bandwidth requirements of incremental decoding. We verify experimentally that the resulting models can indeed be much faster to decode, and incur only minor quality degradation from the baseline.

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

PDF：`/home/user/llm-papers/01_大模型/PDF/33_MultiQueryAttention.pdf`

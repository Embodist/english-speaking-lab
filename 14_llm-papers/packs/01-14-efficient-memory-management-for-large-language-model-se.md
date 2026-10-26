---
type: paper-pack
paper_id: "01-14"
stage: 1
title: "Efficient Memory Management for Large Language Model Serving with PagedAttention"
pdf: "/home/user/llm-papers/01_大模型/PDF/14_PagedAttention.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-14 Efficient Memory Management for Large Language Model Serving with PagedAttention

**中文标题**：基于 PagedAttention 的大语言模型服务的高效内存管理

**一句话概括**：借鉴操作系统虚拟内存分页思想提出 PagedAttention，并构建 vLLM 服务系统，几乎消除 KV 缓存内存浪费，吞吐量提升 2–4 倍。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| throughput | /θɹˈuːpʊt/ | 吞吐量（单位时间处理的请求数） | A |
| redundant | /ɹɪdˈʌndənt/ | 冗余的（重复多余的） | A |
| flexible | /flˈɛksɪbəl/ | 灵活的 | A |
| serving | /sˈɜːvɪŋ/ | 服务（部署模型对外提供推理服务） | B |
| batching | /bˈatʃɪŋ/ | 批处理（把多个请求放在一起处理） | B |
| key-value cache | /kˈiːvˈaljuː kˈaʃ/ | 键值缓存（KV 缓存，存储注意力计算所需的键值） | B |
| dynamically | /daɪnˈamɪkli/ | 动态地（随情况变化） | B |
| fragmentation | /fɹˌaɡməntˈeɪʃən/ | 碎片化（内存被拆散浪费） | B |
| paging | /pˈeɪdʒɪŋ/ | 分页（操作系统管理内存的技术） | B |
| pronounced | /pɹənˈaʊnst/ | 明显的、显著的 | B |

### 原句（保留完整句子）

- **throughput** — “Our evaluations show that vLLM improves the for the KV cache (red) is (de)allocated per serving request. throughput of popular LLMs by 2-4× with the same level A small amount of memory (yellow) is used ephemerally of latency compared to the state-of-the-art systems, such for activation.”
- **redundant** — “When managed inefficiently, this 1.2k memory can be significantly wasted by fragmentation and 0.8k Others redundant duplication, limiting the batch size.”
- **flexible** — “Left: Memory layout when serving an LLM with waste in KV cache memory and (2) flexible sharing of KV 13B parameters on NVIDIA A100.”
- **serving** — “Efficient Memory Management for Large Language Model Serving with PagedAttention Woosuk Kwon1,∗ Zhuohan Li1,∗ Siyuan Zhuang1 Ying Sheng1,2 Lianmin Zheng1 Cody Hao Yu3 Joseph E.”
- **batching** — “However, running putation power of GPUs and limiting the serving throughput. these applications is very expensive, requiring a large numImproving the throughput is possible by batching multiber of hardware accelerators such as GPUs.”
- **key-value cache** — “"the key-value cache (KV cache) memory for each request is huge"”
- **dynamically** — “Our evaluations on various models deep learning workloads, the KV cache has unique charac- and workloads show that vLLM improves the LLM serving teristics: it dynamically grows and shrinks over time as the throughput by 2-4× compared to the state-of-the-art sysmodel generates new tokens, and its lifetime and length are tems \[31, 60\], without affecting the model accuracy at all.”
- **fragmentation** — “When managed inefficiently, this 1.2k memory can be significantly wasted by fragmentation and 0.8k Others redundant duplication, limiting the batch size.”
- **paging** — “96.3 40 To address the above limitations, we propose PagedAt17.9 13.3 tention, an attention algorithm inspired by the operating 20 38.2 20.4 26.8 system’s (OS) solution to memory fragmentation and shar0 ing: virtual memory with paging.”
- **pronounced** — “The improvement is more curve of KV cache memory seen in existing systems \[31, 60\], pronounced with longer sequences, larger models, and more leading to a notable boost in serving throughput. complex decoding algorithms. vLLM’s source code is publicly available at https://github.com/vllm-project/vllm. the cost per request—of LLM serving systems is becoming more important.”

## Abstract（自动提取）

> TITLE: Efficient Memory Management for Large Language Model Serving with PagedAttention ABSTRACT: High throughput serving of large language models (LLMs) requires batching sufficiently many requests at a time. However, existing systems struggle because the key-value cache (KV cache) memory for each request is huge and grows and shrinks dynamically. When managed inefficiently, this memory can be significantly wasted by fragmentation and redundant duplication, limiting the batch size. To address this problem, we propose PagedAttention, an attention algorithm inspired by the classical virtual memory and paging techniques in operating systems. On top of it, we build vLLM, an LLM serving system that achieves (1) near-zero waste in KV cache memory and (2) flexible sharing of KV cache within and across requests to further reduce memory usage. Our evaluations show that vLLM improves the throughput of popular LLMs by 2-4$\times$ with the same level of latency compared to the state-of-the-art systems, such as FasterTransformer and Orca. The improvement is more pronounced with longer sequences, larger models, and more complex decoding algorithms. vLLM's source code is publicly available at https://github.com/vllm-project/vllm

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

PDF：`/home/user/llm-papers/01_大模型/PDF/14_PagedAttention.pdf`

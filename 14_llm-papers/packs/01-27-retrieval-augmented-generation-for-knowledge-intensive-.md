---
type: paper-pack
paper_id: "01-27"
stage: 1
title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
pdf: "/home/user/llm-papers/01_大模型/PDF/27_RAG_RetrievalAugmentedGeneration.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-27 Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

**中文标题**：面向知识密集型 NLP 任务的检索增强生成（RAG）

**一句话概括**：提出 RAG 检索增强生成，把预训练参数记忆与维基百科稠密向量索引结合，在知识密集型任务上刷新多项 SOTA。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| recipe | /ɹˈɛsɪpˌiː/ | 方法、方案 | S |
| retrieval-augmented | /ɹɪtɹˈiːvəlɔːɡmˈɛntɪd/ | 检索增强的（结合检索与生成） | A |
| store | /stˈɔː/ | 存储 | A |
| differentiable | /dˈɪfəɹˌɛnʃɪəbəl/ | 可微的（可求导、支持梯度传播） | A |
| retriever | /ɹɪtɹˈiːvə/ | 检索器（负责查找相关文档的模型） | A |
| knowledge-intensive | /nˈɒlɪdʒɪntˈɛnsɪv/ | 知识密集型的（需要大量外部知识） | B |
| precisely | /pɹɪsˈaɪsli/ | 精确地 | B |
| provenance | /pɹˈuːvnəns/ | 出处、来源（决策可追溯） | B |
| non-parametric | /nˈɒnpˌaɹəmˈɛtɹɪk/ | 非参数化的（参数之外的外部记忆） | B |
| dense vector index | /dˈɛns vˈɛktə ˈɪndɛks/ | 稠密向量索引（用于向量检索的结构） | B |

### 原句（保留完整句子）

- **recipe** — “We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG) — models which combine pre-trained parametric and non-parametric memory for language generation.”
- **retrieval-augmented** — “We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG) — models which combine pre-trained parametric and non-parametric memory for language generation.”
- **store** — “We find that doing Maximum Inner Product Search with FAISS is sufficiently fast on CPU, so we store document index vectors on CPU, requiring ∼ 100 GB of CPU memory for all of Wikipedia.”
- **differentiable** — “Pretrained models with a differentiable access mechanism to explicit non-parametric memory have so far been only investigated for extractive downstream tasks.”
- **retriever** — “We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever.”
- **knowledge-intensive** — “However, their ability to access and precisely manipulate knowledge is still limited, and hence on knowledge-intensive tasks, their performance lags behind task-specific architectures.”
- **precisely** — “However, their ability to access and precisely manipulate knowledge is still limited, and hence on knowledge-intensive tasks, their performance lags behind task-specific architectures.”
- **provenance** — “Additionally, providing provenance for their decisions and updating their world knowledge remain open research problems.”
- **non-parametric** — “Pretrained models with a differentiable access mechanism to explicit non-parametric memory have so far been only investigated for extractive downstream tasks.”
- **dense vector index** — “We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever.”

## Abstract（自动提取）

> TITLE: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks ABSTRACT: Large pre-trained language models have been shown to store factual knowledge in their parameters, and achieve state-of-the-art results when fine-tuned on downstream NLP tasks. However, their ability to access and precisely manipulate knowledge is still limited, and hence on knowledge-intensive tasks, their performance lags behind task-specific architectures. Additionally, providing provenance for their decisions and updating their world knowledge remain open research problems. Pre-trained models with a differentiable access mechanism to explicit non-parametric memory can overcome this issue, but have so far been only investigated for extractive downstream tasks. We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG) -- models which combine pre-trained parametric and non-parametric memory for language generation. We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever. We compare two RAG formulations, one which conditions on the same retrieved passages across the whole generated sequence, the other can use different passages per token. We fine-tune and evaluate our models on a wide range of knowledge-intensive NLP tasks and set

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

PDF：`/home/user/llm-papers/01_大模型/PDF/27_RAG_RetrievalAugmentedGeneration.pdf`

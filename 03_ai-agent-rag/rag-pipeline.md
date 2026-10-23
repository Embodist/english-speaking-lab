---
type: topic
title: RAG 流程
tags: [topic/rag, skill/speaking, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# RAG 流程

## 五个阶段

1. **Ingest & normalize**：`We ingest and normalize the documents.`
2. **Chunk & embed**：`We split the documents into chunks before embedding them.`
3. **Retrieve**：`We retrieve candidate passages and optionally rerank them.`
4. **Generate**：`We pass the most relevant context to the model.`
5. **Evaluate**：`We evaluate retrieval quality separately from answer quality.`

## 高频句

- `Chunk size affects both retrieval quality and context length.` — 分块大小影响检索质量和上下文长度。
- `The current retriever misses some relevant documents.` — 当前检索器漏掉相关文档。
- `We retrieve a larger candidate set and rerank the top results.` — 先多召回再重排。
- `The reranker improves relevance, but adds latency.` — 重排提升相关性但增加延迟。
- `We should compare dense retrieval with keyword search.` — 比较稠密检索与关键词搜索。
- `The answer should be grounded in the retrieved sources.` — 答案应以检索来源为依据。
- `The model answered confidently, but the document doesn’t support the claim.` — 模型很肯定，但文档不支持。
- `We need a dataset with positive and negative examples.` — 需要正负样本数据集。
- `Let’s evaluate recall at k and answer faithfulness separately.` — 分别评测 Recall@k 和忠实度。
- `The vector index is out of date.` — 向量索引过期。
- `We need to re-embed the documents after changing the embedding model.` — 换嵌入模型后需重建向量。
- `The metadata filter is too restrictive.` — 元数据过滤过严。
- `The query rewrite helps with vague questions.` — 查询改写对模糊问题有帮助。
- `We should handle missing sources explicitly.` — 明确处理无检索结果的情况。

## 60 秒讲法

> I’d describe the pipeline in stages. First, we ingest and normalize the documents. Then we chunk them and generate embeddings. At query time, we retrieve candidate passages, optionally rerank them, and pass the most relevant context to the model. We evaluate retrieval quality separately from answer quality, which helps us tell whether a failure comes from missing context, poor ranking, or generation. We also handle missing sources explicitly rather than letting the model guess.

## 常见追问

- 为什么分块大小重要？
- 如何减少幻觉？
- 如何知道是检索问题还是生成问题？
- 换嵌入模型后要做什么？

## 练习

- [ ] 用 60 秒讲完整流程，不看稿
- [ ] 用 30 秒讲一个失败案例和定位方法

## 相关

- [[03_ai-agent-rag/evaluation|评测]]
- [[08_sentence-library/rag-and-retrieval|RAG 句子库]]

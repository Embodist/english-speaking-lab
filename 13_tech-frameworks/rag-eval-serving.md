---
type: topic
title: RAG、评测与服务
tags: [topic/rag, topic/eval, topic/deployment, skill/speaking, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# RAG、评测与服务

> 讲 RAG 的关键不是“用了向量库”，而是**检索质量、答案依据性、延迟和成本**，以及你如何分别评测它们。

## 一、RAG 分层

| 层 | 做什么 | 常见取舍 | 说（英文） |
|---|---|---|---|
| Ingestion | 解析、清洗、去重 | 解析质量影响后续一切 | `We ingest and normalize the documents first.` |
| Chunking | 切块并加元数据 | 块太大/太小都伤检索 | `Chunk size affects retrieval quality and context length.` |
| Embedding | 文本转向量 | 领域适配 vs 通用性 | `We generate embeddings and index them.` |
| Retrieval | 召回候选 | 召回 vs 延迟 | `We retrieve a larger candidate set.` |
| Reranking | 对候选重新排序 | 相关性 vs 延迟 | `The reranker improves relevance but adds latency.` |
| Generation | 基于上下文回答 | 忠实度 vs 流畅度 | `The answer should be grounded in the retrieved sources.` |
| Guardrails | 权限、引用、拒答 | 安全 vs 可用性 | `We handle missing sources explicitly.` |
| Evaluation | 检索/生成分开评测 | 指标选择 | `We evaluate retrieval quality separately from answer quality.` |

## 二、检索组件

| 组件 | 常见选择 | 取舍 | 说（英文） |
|---|---|---|---|
| Embedding model | 通用/领域嵌入模型 | 领域术语、多语言、成本 | `We chose the embedding model based on domain recall.` |
| Vector index | Faiss（本地）、Milvus 等 | 运维复杂度 vs 规模 | `The vector index supports metadata filtering.` |
| Keyword search | Elasticsearch / BM25 | 稀有词强，语义弱 | `Hybrid search combines vectors and keywords.` |
| Reranker | Cross-encoder 等 | 质量提升 vs 延迟 | `We rerank the top candidates with a cross-encoder.` |
| Query rewrite | 改写/扩展 | 模糊查询收益大 | `Query rewriting helps with vague questions.` |
| Metadata filter | 权限、时间、来源 | 过严会漏召回 | `The metadata filter is too restrictive.` |

## 三、评测指标

| 指标 | 衡量什么 | 说（英文） |
|---|---|---|
| Recall@k | 前 k 个结果里有多少相关文档 | `We measure recall at k for retrieval.` |
| MRR | 第一个相关结果的排名 | `MRR captures how early the first relevant hit appears.` |
| nDCG | 排序质量（考虑位置） | `nDCG reflects ranking quality.` |
| Faithfulness / groundedness | 答案是否被来源支持 | `We evaluate answer faithfulness against the sources.` |
| Answer relevance | 答案是否回答了问题 | `Answer relevance is rated separately.` |
| Latency / cost | p95、tokens、单请求成本 | `We track p95 latency and token cost.` |
| Human evaluation | 人工评分 | `Human evaluation uses a fixed rubric.` |

> 常见错误：只报一个总分。应分别报告**检索**和**生成**，否则无法定位失败原因。

## 四、服务与部署

| 能力 | 做法 | 取舍 | 说（英文） |
|---|---|---|---|
| 推理引擎 | vLLM 等 | 吞吐 vs 部署复杂度 | `We serve the model with vLLM.` |
| 批处理 | 动态 batching | 吞吐 vs 单请求延迟 | `Dynamic batching improves GPU utilization.` |
| 缓存 | prompt/KV/结果缓存 | 命中率 vs 一致性 | `We cache repeated prompts and retrieval results.` |
| 自动扩缩 | 按队列/延迟扩缩 | 成本 vs 稳定性 | `The service scales based on queue depth.` |
| 限流 | rate limit | 保护 vs 可用性 | `We apply rate limiting at the gateway.` |
| 降级 | 小模型/关键词检索 | 质量 vs 可用性 | `If the model times out, we fall back to keyword search.` |
| 监控 | 延迟、错误率、成本 | 可观测性 | `We monitor p95 latency, error rate, and token cost.` |

## 五、60 秒讲法

> I’d describe the system in layers. We ingest and normalize documents, chunk them, and generate embeddings. At query time, we retrieve candidates, optionally rerank them, and pass the most relevant context to the model. We evaluate retrieval quality separately from answer quality, which helps us tell whether a failure comes from missing context, poor ranking, or generation. We also handle missing sources explicitly rather than letting the model guess. For serving, we track p95 latency, throughput, and token cost, and we keep a fallback path when the model times out.

## 六、严谨性检查

- [ ] 我是否分别报告了检索和生成指标？
- [ ] 我是否说明了评测集规模和来源？
- [ ] 我是否给出了真实的 p95/成本数据？
- [ ] 我是否讲清了无检索结果时的行为？

## 相关

- [[13_tech-frameworks/_index|技术与框架]]
- [[03_ai-agent-rag/_index|AI 与 RAG]]
- [[12_word-phrase-bank/04-paper-reading|论文阅读]]
- [[12_word-phrase-bank/06-ai-llm-terms|AI / LLM 术语]]

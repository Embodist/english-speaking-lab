---
type: topic
title: 跨模态检索
tags: [topic/music, topic/rag, skill/speaking, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# 跨模态检索

## 高频句

- `We use text and audio embeddings for cross-modal retrieval.` — 用文本和音频嵌入做跨模态检索。
- `The retrieved candidates are ranked by semantic similarity.` — 候选按语义相似度排序。
- `The workflow retrieves relevant musical references before generation.` — 生成前检索音乐参考。
- `The metadata filter is too restrictive.` — 元数据过滤过严。
- `We need a consistent evaluation process for subjective audio quality.` — 主观质量需一致评估。
- `I’m still validating the retrieval quality and end-to-end workflow.` — 仍在验证检索质量与端到端流程。

## 讲流程

> At query time, we embed the user’s text description and retrieve audio candidates from the index. Then we rank them by semantic similarity and filter by metadata such as genre or tempo. The retrieved references guide the generation stage. We evaluate retrieval separately from generation, because a bad result can come from missing references or from the generation model itself.

## 可能追问

| 问题 | 方向 |
|---|---|
| How do you align text and audio? | 对比学习 / 共享嵌入空间；用检索指标验证 |
| How do you evaluate retrieval? | Recall@k、人工相关性、下游生成质量 |
| How do you handle subjective quality? | 固定评测协议 + 多人评分 + 可重复案例 |

## 练习

- [ ] 用 60 秒讲检索链路
- [ ] 准备一个“检索对了但生成失败”的案例

## 相关

- [[05_music-agent/_index|音乐 Agent]]
- [[03_ai-agent-rag/rag-pipeline|RAG 流程]]

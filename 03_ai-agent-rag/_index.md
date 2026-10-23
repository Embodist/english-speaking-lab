---
type: hub
title: AI · Agent · RAG
tags: [hub, topic/agent, topic/rag]
created: 2026-10-23
updated: 2026-10-23
---

# AI · Agent · RAG

目标：能把架构、取舍、评测和失败模式讲清楚，**先结论，再分层解释**。

## 笔记

| 主题 | 笔记 | 要讲清 |
|---|---|---|
| Agent 与工具调用 | [[03_ai-agent-rag/agent-overview\|Agent 架构]] | 规划、执行、状态、重试、权限 |
| RAG | [[03_ai-agent-rag/rag-pipeline\|RAG 流程]] | 切块、嵌入、检索、重排、生成 |
| 评测 | [[03_ai-agent-rag/evaluation\|评测方法]] | baseline、指标、消融、失败案例 |
| 模型服务 | [[03_ai-agent-rag/deployment\|部署与推理]] | 吞吐、p95、TTFT、批处理、量化 |

## 通用表达框架

> The goal was … The main challenge was … I chose this approach because … The main trade-off was … I validated it by … As a result …

## 最小回答结构（每题 60 秒）

1. **一句话结论**：`The pipeline has three stages: retrieval, reranking, and generation.`
2. **展开 2–3 个阶段**：每段用 `First… Then… Finally…`
3. **讲取舍**：`The main trade-off is accuracy versus latency.`
4. **讲验证**：`We evaluated it on a held-out set and compared against the baseline.`

## 练习

- [ ] 每个主题选 3 句，录音
- [ ] 用 2 分钟脱稿讲一个项目，录下来回听
- [ ] 为每个项目准备 3 个可能追问

## 相关

- [[13_tech-frameworks/llm-model-capabilities|LLM 与模型能力]]
- [[13_tech-frameworks/agent-frameworks|Agent 与工作流框架]]
- [[13_tech-frameworks/rag-eval-serving|RAG、评测与服务]]
- [[06_interview/project-stories|项目故事]]
- [[09_sources/01_AI工程师英语面试与工作训练手册.docx|AI 工程师英语训练手册（原始）]]

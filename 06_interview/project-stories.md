---
type: story
title: 项目故事库
tags: [skill/interview, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# 项目故事库

每个项目一页，用同一结构。**只写真实数据；没有数字就讲工程经验。**

## 通用框架

| 步骤 | 句型 |
|---|---|
| Goal | `The goal was to …` |
| Challenge | `The main challenge was …` |
| Responsibility | `My responsibility was …` |
| Approach | `I chose this approach because …` |
| Trade-off | `The main trade-off was …` |
| Validation | `I validated the result by …` |
| Result | `As a result, …` |

## 项目 1：企业 RAG 助手

- **Goal**：帮助用户在企业知识库中快速找到有依据的答案。
- **Challenge**：领域术语、文档权限、检索遗漏、答案依据性。
- **Responsibility**：文档处理、检索与重排、模型服务集成。
- **Approach**：解析 → 分块 → 嵌入 → 混合检索 → 重排 → 生成。
- **Trade-off**：准确率 vs 延迟；召回 vs 上下文长度。
- **Validation**：Recall@k、答案忠实度、留出评测集。
- **Result**：（填写真实指标或工程产出）

> 60 秒版：I’d describe the pipeline in stages. First, we ingest and normalize the documents. Then we chunk them and generate embeddings. At query time, we retrieve candidates, rerank them, and pass the most relevant context to the model. We evaluate retrieval quality separately from answer quality. The main trade-off was accuracy versus latency, and we mitigated it by reranking a smaller candidate set. We validated the changes on a held-out evaluation set.

## 项目 2：LLM 安全分析与 WAF 建议

- **Goal**：降低分析师处理告警的负担，并辅助生成可审核的规则建议。
- **Challenge**：误报、上下文不足、敏感数据、人工审核。
- **Approach**：事件富化 → 模型总结证据 → 规则建议 → 分析师接受/修改/拒绝 → dry run。
- **Trade-off**：自动化程度 vs 安全可控。
- **Validation**：precision、recall、分析师审核时间。
- **Result**：（填写真实数据）

## 项目 3：音乐 Agent

- **Goal**：用自然语言完成音乐创作/翻唱的工作流编排。
- **Challenge**：跨模态检索、工具编排、主观质量、失败降级。
- **Approach**：意图理解 → 参考检索 → 规划 → 生成 → 转换 → 后期；LangGraph 管理状态。
- **Trade-off**：创作自由度 vs 可预测性；演示效果 vs 可重复测试。
- **Validation**：检索质量、端到端成功率、失败案例。
- **Result**：（填写真实数据）

## 追问准备

- `The main bottleneck was …`
- `My contribution was mainly in …`
- `One limitation is …`
- `If I redesigned it today, I would …`
- `The project most relevant to this role is …`

## 相关

- [[10_templates/project-story|项目故事模板]]
- [[03_ai-agent-rag/_index|AI 与 RAG]]
- [[04_security/_index|安全]]
- [[05_music-agent/_index|音乐 Agent]]

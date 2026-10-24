---
type: story
title: 项目故事（三个旗舰项目）
tags: [skill/interview, status/learning]
created: 2026-10-24
updated: 2026-10-24
---

# 项目故事（三个旗舰项目）

> 每个项目准备 30 秒、90 秒、追问三层。只讲你真实负责的部分；数字来自简历，`[confirm]` 的先确认口径。

## 1. Music Creation & Cover Agent

### 30 秒

> We built a music creation and cover agent for consumers. Users describe a song in natural language, and a LangGraph workflow coordinates pitch analysis, harmony analysis, voice conversion, and mixing. We use cross-modal retrieval to find references and add guardrails for tool permissions, copyright, and content safety. The main challenge is balancing creative flexibility with predictable behavior.

### 90 秒

> The goal was to let a user describe a song and get a usable cover or new version end to end. The workflow has three layers. First, intent understanding and planning. Second, tool execution: pitch and harmony analysis, retrieval of musical references, voice conversion, and audio post-processing. Third, validation and content checks.
>
> We used LangGraph because the task is multi-step and stateful. We persist state so a long job can resume, validate tool arguments before execution, and fall back when a tool fails. For retrieval, we align text and audio embeddings so humming, text, and mood queries can all find references.
>
> My contribution was mainly the workflow integration, the retrieval path, and the guardrails. The main trade-off is creative freedom versus controllability: more freedom gives more interesting output, but it is harder to test and support. We mitigate that by separating deterministic steps from model-driven decisions and using a fixed evaluation rubric for audio quality. `[confirm: user scale, latency, success rate]`

### 追问

| 问题 | 回答方向 |
|---|---|
| Why LangGraph instead of one prompt? | 多步骤、有状态、可恢复、可观测；单次 prompt 无法可靠编排工具 |
| How do you handle tool failure? | 有界重试 → 降级路径 → 明确告知用户；状态可恢复 |
| How do you evaluate subjective quality? | 固定 rubric、固定样本、多人评分、分歧记录 |
| How do you handle copyright? | 版权检查 + 人工审核 + 限制输出 |
| What is the biggest limitation? | 主观质量与可预测性难以同时保证；评测成本高 |

## 2. LLM Security Operations Agent & Traffic Validation

### 30 秒

> The problem was that legacy WAF rules over-flagged transformed or obfuscated attacks. We added an LLM stage: BERT did coarse filtering, and a fine-tuned Qwen model analyzed URL payloads in depth. We also built a Go platform to infer detection rules and a shadow-traffic engine that replayed production traffic. That cut rule validation from weeks to about four hours.

### 90 秒

> The system was a two-stage funnel. The first stage was BERT-based feature reduction: IP aggregation, C-block scoring, and high-throughput filtering. The second stage was a fine-tuned Qwen model that looked at the actual URL payload and judged malicious intent. False positives were deduplicated and fed back into training, which reduced manual triage.
>
> We also built a Go rule-inference platform that generated candidate regexes and thresholds. To validate rules safely, we mirrored production traffic and replayed it in a shadow environment. That let us test detection and performance before enforcement. The main result was cutting validation from weeks to about four hours `[confirm: baseline]`.
>
> My contribution covered the agent workflow, the rule-inference platform, and the traffic-validation engine. The main trade-off was detection coverage versus false positives, and we kept a human in the loop for high-impact actions.

### 追问

| 问题 | 回答方向 |
|---|---|
| Why combine rules and LLM? | 规则高吞吐、可解释；LLM 处理变形/混淆语义 |
| How do you reduce false positives without missing attacks? | 两阶段漏斗、反馈训练、dry run、人工审核、指标分开看 |
| How do you validate at scale? | 影子流量、实时回放、限流、隔离环境、与生产同构 |
| What could go wrong? | 模型漂移、提示注入、规则过拟合、回放流量偏差 |

## 3. Enterprise Security RAG Assistant

### 30 秒

> We built an enterprise security RAG assistant for knowledge QA. The knowledge base included security-group policies, NAT rules, and incident playbooks. We used hybrid retrieval across Milvus, Redis, and Elasticsearch, plus SBERT reranking. Long-text QA accuracy was above 85% `[confirm: metric]`. We also added prompt-injection and data-exfiltration defenses.

### 90 秒

> The goal was to help security teams answer questions from internal documents without reading everything manually. We normalized the documents, chunked them, and indexed them in a hybrid retrieval stack: vector search for semantics, keyword search for exact terms, and Redis for caching. We added SBERT-based reranking and fine-tuned it for security terminology.
>
> We evaluated retrieval quality separately from answer quality. That helped us tell whether a failure came from missing context, poor ranking, or generation. We also added document-level access control, prompt-injection defenses, and explicit behavior when no source was found. The workflow was orchestrated in LangGraph, including rule creation, validation, rollout, monitoring, and response.
>
> My contribution was mainly the retrieval/reranking path, the LangGraph workflow, and the security controls. The main limitation is that 85% accuracy is only meaningful with a defined dataset and metric; we need to be precise about that in interviews. `[confirm: dataset, sample size, human eval]`

### 追问

| 问题 | 回答方向 |
|---|---|
| How do you choose chunk size? | 按文档结构、问答粒度、上下文长度；用评测集验证 |
| How do you evaluate RAG? | Recall@k、忠实度、答案相关性、人工抽检，分开评测 |
| Why hybrid search? | 稀有术语/编号靠关键词，语义靠向量 |
| How do you prevent data exfiltration? | 文档级权限、最小上下文、日志脱敏、输出审核 |

## 三个项目的共同主线

> Across all three projects, I care about the same thing: making AI systems reliable. That means the right context, the right tool, a clear evaluation method, and a safe failure path. The model is only one part of the system.

## 相关

- [[15_resume/_index|简历与自我介绍]]
- [[15_resume/experience|工作经历表达]]
- [[15_resume/capability-gaps|能力补充清单]]
- [[03_ai-agent-rag/_index|AI 与 RAG 表达]]
- [[05_music-agent/_index|音乐 Agent]]

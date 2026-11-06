---
type: guide
title: "应答训练"
tags: [skill/speaking, status/learning]
created: 2026-11-06
updated: 2026-11-06
---

# 应答训练

> 看问题，先用**完整句**回答，再看模型答案。不要只答一个词。

| # | 问题 | 模型回答 |
|---:|---|---|
| 1 | What's the status of the migration? | It's on track. We've migrated 60% of the data and expect to finish by Friday. |
| 2 | Why did the latency spike? | The spike started after the model upgrade. We're rolling back and monitoring. |
| 3 | What's blocking the release? | The flaky integration test. We're isolating it and will decide by noon. |
| 4 | Can you walk me through the design? | Sure. The client sends a request, the gateway authenticates it, and the service retrieves context from the vector store. |
| 5 | What's the risk of this change? | The main risk is backward compatibility. We'll ship it behind a flag and roll out gradually. |
| 6 | How do you evaluate the RAG system? | We track retrieval recall, answer groundedness, and latency on a fixed evaluation set. |
| 7 | What did you learn from the incident? | We learned that retries need a cap and that alerts should fire on error rate, not just CPU. |
| 8 | How would you improve this pipeline? | I'd add caching at the retrieval layer and batch the embedding calls. |
| 9 | What's your role on the team? | I own the retrieval and evaluation components and work closely with the backend team. |
| 10 | Why did you choose this approach? | It's the simplest option that meets the latency target, and it's easy to roll back. |
| 11 | What are the next steps? | First, we'll add a test. Then we'll run a small experiment. Finally, we'll update the docs. |
| 12 | Is the system ready for production? | Not yet. We need to fix two blockers and run a load test. |
| 13 | How do you handle failures? | We retry with backoff, fall back to a cached response, and log the failure. |
| 14 | What's the cost impact? | The estimate is about 20% higher, mostly from the embedding calls. |
| 15 | Can we ship on Friday? | I think so, if the review passes today. Otherwise, Monday is safer. |
| 16 | What's the user feedback? | Users like the speed, but they want more control over the sources. |
| 17 | Why is the test flaky? | It depends on a shared database. We'll isolate it with a transaction. |
| 18 | How do you monitor the service? | We track latency, error rate, and queue depth, with alerts on each. |
| 19 | What's the biggest unknown? | The data distribution in production. We'll start with a small canary. |
| 20 | How would you explain this to a non-technical stakeholder? | It's like a search assistant that finds the right document and summarizes it. |
| 21 | What's the timeline? | Two weeks for the core flow, plus one week for hardening. |
| 22 | Did the fix work? | Partially. The error rate dropped, but the latency is still high. |
| 23 | What do you need from me? | A decision on the scope, and access to the staging logs. |
| 24 | Any concerns? | One: the model may hallucinate citations. We should add a verification step. |
| 25 | How do you prioritize? | I prioritize by user impact and reversibility. Small, safe changes go first. |

## 进阶

1. 同一问题准备两个版本：一个 1 句，一个 3 句。
2. 把问题里的项目换成你自己的，再说一遍。
3. 录音后检查：有没有漏掉主语、时态、数字。

## 相关

- [[18_fsi-drills/_index|FSI 训练总览]]

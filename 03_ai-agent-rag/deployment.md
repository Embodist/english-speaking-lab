---
type: topic
title: 模型服务与部署
tags: [topic/deployment, skill/speaking, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# 模型服务与部署

## 推理与性能

- `We reduced the context length to control inference cost.` — 缩短上下文以控制推理成本。
- `Quantization reduces memory usage, but we need to check quality degradation.` — 量化省内存，但要查质量下降。
- `The GPU is underutilized during decoding.` — 解码时 GPU 利用率不高。
- `Batching improves throughput for concurrent requests.` — 批处理提高并发吞吐。
- `We need to measure time to first token and tokens per second.` — 需要测 TTFT 和 TPS。
- `The average latency looks fine, but p95 is still too high.` — 平均延迟还行，p95 过高。
- `Let’s profile the hot path before optimizing it.` — 优化前先分析热点路径。
- `The new implementation improves throughput at the cost of memory.` — 以内存换吞吐。

## 发布与回滚

- `The build is green, but the integration tests are still running.` — 构建通过，集成测试还在跑。
- `The release candidate is ready for staging.` — 候选版本可进预发布。
- `Let’s deploy to a small percentage of traffic first.` — 先向少量流量部署。
- `We’ll monitor error rate, latency, and resource usage.` — 监控错误率、延迟、资源。
- `The canary looks healthy so far.` — 金丝雀目前正常。
- `The new version is failing the health check.` — 新版本健康检查失败。
- `Let’s stop the rollout and investigate.` — 停止发布并排查。
- `The rollback is complete.` — 回滚完成。
- `We need a migration plan for the database schema.` — 需要 schema 迁移计划。
- `This release is backward-compatible with the previous client.` — 与旧客户端向后兼容。

## 延迟排查 60 秒

> First, I’d break the end-to-end latency into stages: request handling, retrieval, model queueing, inference, and post-processing. Then I’d measure each stage instead of assuming the model is the bottleneck. I’d check p50 and p95, along with concurrency, batch size, GPU utilization, and memory. After identifying the bottleneck, I’d test one change at a time against the same workload. I’d also make sure the optimization doesn’t degrade output quality or reliability.

## 指标词汇

`TTFT` 首 token 时间 · `TPS` 每秒 token 数 · `RPS` 每秒请求数 · `p95 latency` · `throughput` · `batch size` · `GPU utilization` · `memory footprint` · `SLO`

## 练习

- [ ] 用 60 秒讲一次延迟排查
- [ ] 用 30 秒讲一次金丝雀发布失败与回滚

## 相关

- [[03_ai-agent-rag/_index|AI 与 RAG]]
- [[08_sentence-library/model-and-inference|模型与推理句子库]]
- [[02_daily-work/incident|事故沟通]]

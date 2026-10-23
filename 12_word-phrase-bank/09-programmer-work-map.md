---
type: topic
title: 程序员工作全景与关键表达
tags: [library/word-bank, skill/speaking, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# 程序员工作全景与关键表达

> [!warning] 内容边界
> 这里是**语言学习材料**，不是技术规范。技术细节、指标和架构以你的真实项目与官方文档为准；面试中不要编造未验证的数字。术语在不同团队可能有不同叫法，说的时候先给上下文。

这张图用来回答两个问题：**程序员工作还会涉及什么？** 以及 **每个环节该怎么说？**

## 1. 需求与产品

| 关键英文 | 中文 |
|---|---|
| user story / requirement | 用户故事 / 需求 |
| acceptance criteria | 验收标准 |
| scope / out of scope | 范围 / 不在范围内 |
| ambiguity | 歧义 |
| must-have / nice-to-have | 必需项 / 锦上添花 |
| MVP (minimum viable product) | 最小可行产品 |
| edge case | 边界情况 |
| success metric | 成功指标 |

**说 30 秒**：
- `The goal is to help analysts triage alerts faster.`
- `The acceptance criteria are clear: the endpoint returns a result in under two seconds.`
- `This requirement is ambiguous in two places.`

## 2. 设计与架构

| 关键英文 | 中文 |
|---|---|
| architecture / component | 架构 / 组件 |
| interface / contract | 接口 / 契约 |
| trade-off | 权衡 |
| constraint | 约束 |
| failure mode | 故障模式 |
| single point of failure | 单点故障 |
| scalability / reliability | 可扩展性 / 可靠性 |
| backward compatibility | 向后兼容 |
| proof of concept (PoC) | 概念验证 |

**说 30 秒**：
- `The main trade-off is accuracy versus latency.`
- `The bottleneck is the retrieval stage, not the model.`
- `If this component fails, we fall back to the baseline path.`

## 3. 实现与代码质量

| 关键英文 | 中文 |
|---|---|
| readability / maintainability | 可读性 / 可维护性 |
| modularity | 模块化 |
| refactor | 重构 |
| code review | 代码评审 |
| technical debt | 技术债 |
| lint / static analysis | 静态检查 / 静态分析 |
| duplication | 重复代码 |
| naming convention | 命名规范 |

**说 30 秒**：
- `I kept the change small and added tests around the edge case.`
- `This logic was duplicated, so I extracted a helper.`
- `The refactor preserves behavior and reduces complexity.`

## 4. 数据与存储

| 关键英文 | 中文 |
|---|---|
| schema / migration | 模式 / 迁移 |
| index | 索引 |
| consistency | 一致性 |
| transaction | 事务 |
| query plan / full table scan | 查询计划 / 全表扫描 |
| data retention | 数据保留 |
| data privacy / PII | 数据隐私 / 个人可识别信息 |
| backup / restore | 备份 / 恢复 |

**说 30 秒**：
- `The query is doing a full table scan, so we need an index.`
- `The migration adds a nullable column and backfills it in batches.`
- `We avoid logging PII in prompts or application logs.`

## 5. API 与集成

| 关键英文 | 中文 |
|---|---|
| endpoint / contract | 端点 / 契约 |
| request / response schema | 请求 / 响应结构 |
| versioning | 版本管理 |
| pagination | 分页 |
| error code / status code | 错误码 / 状态码 |
| idempotency | 幂等性 |
| rate limit | 限流 |
| authentication / authorization | 认证 / 授权 |

**说 30 秒**：
- `The endpoint returns a 500 when the downstream service times out.`
- `We need pagination for large result sets.`
- `The retry is safe because the write is idempotent.`

## 6. 测试与质量保障

| 关键英文 | 中文 |
|---|---|
| unit / integration / end-to-end test | 单元 / 集成 / 端到端测试 |
| regression test | 回归测试 |
| flaky test | 不稳定测试 |
| test coverage | 测试覆盖率 |
| test data / fixture | 测试数据 / 测试夹具 |
| negative case | 反例 |
| reproduce / verify | 复现 / 验证 |

**说 30 秒**：
- `I added a regression test for the empty-input case.`
- `The test is flaky; it fails about one in ten runs.`
- `We cover both the happy path and the failure path.`

## 7. 发布与部署

| 关键英文 | 中文 |
|---|---|
| CI/CD pipeline | 持续集成 / 持续交付 |
| staging / production | 预发布 / 生产 |
| release candidate | 候选版本 |
| canary release | 金丝雀发布 |
| feature flag | 功能开关 |
| rollout / rollback | 发布 / 回滚 |
| health check | 健康检查 |
| migration plan | 迁移计划 |

**说 30 秒**：
- `We deploy to a small percentage of traffic first.`
- `The new version is failing the health check, so we paused the rollout.`
- `The rollback is complete and the error rate is back to normal.`

## 8. 运维与 SRE

| 关键英文 | 中文 |
|---|---|
| monitoring / alerting | 监控 / 告警 |
| dashboard | 仪表盘 |
| SLO / SLA | 服务级目标 / 协议 |
| on-call | 值班 |
| incident / postmortem | 事故 / 复盘 |
| root cause | 根因 |
| mitigation | 缓解措施 |
| capacity planning | 容量规划 |

**说 30 秒**：
- `We’re seeing an elevated error rate in production.`
- `We have a mitigation in place, but the root cause is still under investigation.`
- `The action items are to add an alert, a timeout, and a regression test.`

## 9. 性能与成本

| 关键英文 | 中文 |
|---|---|
| profiling / hot path | 性能分析 / 热点路径 |
| bottleneck | 瓶颈 |
| latency / p95 | 延迟 / p95 |
| throughput / QPS | 吞吐量 / 每秒查询数 |
| caching | 缓存 |
| batching | 批处理 |
| token cost | token 成本 |
| cost per request | 单请求成本 |

**说 30 秒**：
- `We profiled the hot path before optimizing it.`
- `The average latency looks fine, but p95 is still too high.`
- `Batching improves throughput at the cost of memory.`

## 10. 安全与隐私

| 关键英文 | 中文 |
|---|---|
| least privilege | 最小权限 |
| secrets management | 密钥管理 |
| prompt injection | 提示词注入 |
| input validation | 输入校验 |
| audit log | 审计日志 |
| data exfiltration | 数据外泄 |
| vulnerability / patch | 漏洞 / 补丁 |
| human approval | 人工审批 |

**说 30 秒**：
- `We treat tool output as untrusted input.`
- `Sensitive actions require human approval.`
- `We avoid exposing sensitive event data in prompts or logs.`

## 11. AI / LLM 专项

| 关键英文 | 中文 |
|---|---|
| evaluation set | 评测集 |
| baseline | 基线 |
| hallucination / grounding | 幻觉 / 依据性 |
| retrieval quality | 检索质量 |
| answer faithfulness | 答案忠实度 |
| guardrail | 防护规则 |
| latency / cost budget | 延迟 / 成本预算 |
| fallback path | 降级路径 |

**说 30 秒**：
- `A successful tool call doesn’t guarantee a correct answer.`
- `We evaluate retrieval quality separately from answer quality.`
- `We need a fixed evaluation set before changing the prompt.`

## 12. 协作与沟通

| 关键英文 | 中文 |
|---|---|
| stand-up / sync | 站会 / 同步 |
| design review | 设计评审 |
| code review | 代码评审 |
| action item / owner | 行动项 / 负责人 |
| dependency / blocker | 依赖 / 阻塞 |
| handoff | 交接 |
| escalation | 升级 |
| decision log | 决策记录 |

**说 30 秒**：
- `I’m blocked by the staging credentials, and I need access from the platform team.`
- `I’ll hand off the investigation and post a summary.`
- `The decision is to keep the current design for this release.`

## 13. 文档与知识

| 关键英文 | 中文 |
|---|---|
| README / runbook | 说明文档 / 运行手册 |
| design doc / RFC | 设计文档 / 请求意见稿 |
| ADR (architecture decision record) | 架构决策记录 |
| changelog | 变更日志 |
| onboarding guide | 入职指南 |
| troubleshooting guide | 排障指南 |

**说 30 秒**：
- `I documented the assumptions in the design doc.`
- `The runbook covers the first three steps of the incident.`
- `We record the decision and the trade-offs in an ADR.`

## 14. 职业与面试

| 关键英文 | 中文 |
|---|---|
| project story / impact | 项目故事 / 影响 |
| ownership | 负责范围 |
| cross-team collaboration | 跨团队协作 |
| mentoring | 带人 |
| behavioral interview | 行为面试 |
| system design | 系统设计 |
| salary expectation | 薪资预期 |

**说 30 秒**：
- `I owned the retrieval pipeline end to end.`
- `I coordinated with two teams to unblock the release.`
- `My main contribution was the evaluation and failure analysis.`

## 15. 合规与许可

| 关键英文 | 中文 |
|---|---|
| license / open source license | 许可证 / 开源许可 |
| copyright | 版权 |
| data retention policy | 数据保留政策 |
| privacy policy | 隐私政策 |
| terms of service | 服务条款 |
| compliance | 合规 |

**说 30 秒**：
- `We check the license before using an open-weight model.`
- `The data-retention policy limits how long logs are stored.`
- `The pipeline includes a copyright check before delivery.`

## 用法

每天选 1 个环节：
1. 看 8 个关键英文，各说一句。
2. 用“说 30 秒”里的句子讲你的项目。
3. 选 3 个词写进日志或 PR。

## 相关

- [[12_word-phrase-bank/_index|词与短语库]]
- [[LEARNING-PATH|学习路径]]
- [[13_tech-frameworks/_index|技术与框架记录]]

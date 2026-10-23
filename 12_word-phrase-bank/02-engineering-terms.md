---
type: word-bank
title: 工程术语
tags: [library/word-bank, skill/speaking, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# 工程术语（45）

覆盖 Git/PR、测试、事故、性能、可观测性与发布。

| 级别 | 术语 | 中文 | 说（口语例句） | 写（书面例句） | 读 / 搭配 |
|---|---|---|---|---|---|
| S | pull request | PR | I opened a pull request for the fix. | The pull request adds regression tests. | in the pull request |
| S | code review | 代码评审 | Could you do a quick code review? | The change passed code review. | request / address code review |
| A | merge conflict | 合并冲突 | I hit a merge conflict on main. | The merge conflict was resolved by rebasing. | resolve a merge conflict |
| S | commit | 提交 | I pushed a small commit. | The commit fixes the empty-input bug. | make a commit |
| A | branch | 分支 | I created a feature branch. | The branch is based on main. | create / check out a branch |
| A | rebase | 变基 | I’ll rebase on the latest main. | The branch was rebased before merging. | rebase onto main |
| A | CI pipeline | CI 流水线 | The CI pipeline is still running. | The change passed the CI pipeline. | fail / pass CI |
| S | unit test | 单元测试 | I added unit tests for the parser. | Unit tests cover the empty-input case. | write / run unit tests |
| A | integration test | 集成测试 | The integration tests are failing in staging. | Integration tests cover service boundaries. | run integration tests |
| A | end-to-end test | 端到端测试 | We ran an end-to-end test on the full flow. | End-to-end tests validate the user journey. | an end-to-end test |
| S | regression test | 回归测试 | I added a regression test for this bug. | The regression test prevents recurrence. | add a regression test |
| S | flaky test | 不稳定测试 | The test is flaky; it fails one out of ten runs. | We quarantined the flaky test. | flaky test |
| A | test coverage | 测试覆盖率 | Coverage is high, but the edge cases are missing. | The change improves test coverage. | test coverage |
| S | edge case | 边界情况 | What happens in the empty-input edge case? | The fix handles the edge case explicitly. | cover an edge case |
| A | race condition | 竞态条件 | I think it’s a race condition. | The race condition occurs under concurrent writes. | introduce / expose a race |
| A | deadlock | 死锁 | The worker deadlocked under load. | The deadlock was caused by lock ordering. | resolve a deadlock |
| A | memory leak | 内存泄漏 | The service has a memory leak. | The leak grows slowly under long-running jobs. | fix a memory leak |
| S | stack trace | 堆栈 | The stack trace points to the parser. | The stack trace is included in the issue. | read the stack trace |
| S | root cause | 根因 | We haven’t found the root cause yet. | The root cause was an unbounded retry loop. | identify the root cause |
| A | postmortem | 事后复盘 | We’ll write a blameless postmortem. | The postmortem lists three action items. | write a postmortem |
| S | incident | 事故 | We had an incident after the deployment. | The incident affected a subset of users. | incident response |
| S | rollback | 回滚 | The rollback reduced the error rate. | A rollback plan is required for this release. | perform a rollback |
| A | canary release | 金丝雀发布 | We deployed to a small percentage first. | The canary release looks healthy. | canary release |
| A | feature flag | 功能开关 | I’ll put it behind a feature flag. | The feature flag lets us disable the change. | enable / disable a flag |
| S | staging | 预发布环境 | It works in staging but fails in production. | The release candidate is deployed to staging. | staging environment |
| S | production | 生产环境 | The error rate is up in production. | The change is not yet in production. | production traffic |
| A | dependency | 依赖 | We have a dependency on the platform API. | The dependency is pinned to a specific version. | external dependency |
| A | technical debt | 技术债 | We need to pay down some technical debt. | The shortcut added technical debt. | reduce technical debt |
| B | code smell | 代码异味 | This function is doing too much. | The reviewer flagged a code smell. | code smell |
| S | API endpoint | API 端点 | The endpoint returns a 500. | The endpoint validates the request body. | call an endpoint |
| S | payload | 请求体 | The payload is empty. | The payload is validated against the schema. | invalid payload |
| A | schema | 模式 / 结构 | The response schema changed. | The schema is shared across services. | request / response schema |
| A | backward compatibility | 向后兼容 | This is backward-compatible. | The change preserves backward compatibility. | maintain backward compatibility |
| A | breaking change | 不兼容变更 | This would be a breaking change. | We avoid breaking changes in minor releases. | introduce a breaking change |
| B | idempotency | 幂等性 | The retry is safe because the write is idempotent. | We need idempotency to avoid duplicate writes. | idempotent operation |
| A | retry policy | 重试策略 | We added a bounded retry policy. | The retry policy uses exponential backoff. | bounded retries |
| S | timeout | 超时 | The request timed out. | We set a timeout on the downstream call. | set a timeout |
| A | rate limit | 限流 | We’re hitting the rate limit. | The gateway applies rate limiting. | rate limit |
| A | throughput | 吞吐量 | Batching improved throughput. | The benchmark reports tokens per second. | improve throughput |
| S | latency | 延迟 | The latency is too high during peak hours. | The change reduces p95 latency. | reduce latency |
| A | p95 | p95 延迟 | The average is fine, but p95 is too high. | We track p50 and p95 latency. | p95 latency |
| A | observability | 可观测性 | We need better observability. | Logs, metrics, and traces improve observability. | observability |
| A | alert | 告警 | We got an alert at 3 a.m. | The alert fires when the error rate exceeds 1%. | add an alert |
| S | dashboard | 仪表盘 | I’m checking the dashboard. | The dashboard shows error rate and latency. | look at the dashboard |
| A | SLO | 服务级目标 | We’re still within the SLO. | The SLO is 99.9% availability. | meet / miss the SLO |

## 发音提醒

| 词 | 重音/要点 |
|---|---|
| payload | **PAY**-load |
| schema | **SKEE**-ma（常见） |
| idempotent | i-**DEM**-po-tent |
| throughput | **THROUGH**-put（/θ/ 开头） |
| latency | **LAY**-ten-cy |
| observability | ob-ser-va-**BIL**-i-ty |
| canary | ca-**NAR**-y |
| postmortem | post-**MOR**-tem |
| regression | re-**GRESH**-ion |

## 练习

- [ ] 选 10 个 S 级术语，模拟站会/事故更新各说 30 秒
- [ ] 用 5 个术语写一段 PR 描述
- [ ] 在真实文档中找 5 个搭配

## 相关

- [[12_word-phrase-bank/_index|词与短语库]]
- [[02_daily-work/_index|日常工作]]
- [[LEARNING-PATH|学习路径]]

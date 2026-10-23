---
type: topic
title: Bug 定位与调试
tags: [scene/bug, skill/speaking, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# Bug 定位与调试

## 口述模板

> First, I reproduced the issue. Then I checked the logs and narrowed it down to [component]. The root cause was [cause]. I fixed it by [change] and added a regression test for [edge case]. I also verified that [related behavior] still works.

## 描述问题

- `I can reproduce the issue locally.` — 我在本地可以复现。
- `The issue occurs only with an empty payload.` — 只在 payload 为空时出现。
- `It fails intermittently, roughly one out of ten requests.` — 间歇性失败，约十次一次。
- `The error started after the latest dependency upgrade.` — 升级依赖后开始报错。
- `The stack trace points to the request parser.` — 堆栈指向请求解析器。
- `I haven’t identified the root cause yet.` — 我还没确认根因。
- `The logs suggest a connection-pool issue.` — 日志显示可能是连接池问题。
- `Could this be a race condition?` — 会不会是竞态条件？
- `Let’s narrow it down by disabling one component at a time.` — 每次禁用一个组件缩小范围。
- `Can you share the exact request that triggers the error?` — 能分享触发错误的确切请求吗？
- `I suspect the input validation is too strict.` — 我怀疑输入校验太严格。
- `The bug is fixed, but I still need to verify the regression tests.` — 修好了，但还要验证回归测试。
- `I added a test case to prevent this from happening again.` — 加了测试用例防止复发。

## 高频调试动词

`reproduce` 复现 · `inspect` 检查 · `trace` 跟踪 · `isolate` 隔离 · `instrument` 加埋点 · `compare` 对比 · `validate` 验证 · `confirm` 确认 · `rule out` 排除 · `mitigate` 缓解 · `regress` 回归 · `throttle` 限流 · `retry` 重试 · `fall back` 降级

## 练习

- [ ] 选一个真实 Bug，按模板口述 45 秒
- [ ] 用 `I haven’t confirmed…` 练习区分事实与假设
- [ ] 录音后检查：现象、复现、范围、根因、修复、测试是否齐全

## 相关

- [[02_daily-work/_index|日常工作]]
- [[08_sentence-library/daily-work|日常工作句子库]]

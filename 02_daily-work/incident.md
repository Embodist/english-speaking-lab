---
type: topic
title: 线上事故沟通
tags: [scene/incident, skill/speaking, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# 线上事故沟通

原则：**先讲影响，再讲缓解，最后讲根因。** 没确认根因时，明确说还在调查。

## 发现与影响

- `We’re seeing an elevated error rate in production.` — 生产错误率升高。
- `The service is responding slowly, but it is still available.` — 响应慢但仍可用。
- `The incident started shortly after the deployment.` — 部署后不久发生。
- `We’re investigating the impact and scope.` — 正在调查影响范围。
- `The current impact appears limited to a subset of users.` — 当前影响似乎限于部分用户。

## 处理与同步

- `I’m checking the dashboards and recent changes.` — 查看仪表盘和近期变更。
- `Let’s roll back the deployment while we investigate.` — 调查期间先回滚。
- `The rollback reduced the error rate.` — 回滚后错误率下降。
- `We have a mitigation in place, but the root cause is still under investigation.` — 已有缓解，根因仍在调查。
- `Please avoid making unrelated changes during the incident.` — 事故期间避免无关变更。
- `I’ll post an update every fifteen minutes.` — 每十五分钟同步一次。
- `We need to preserve the logs for the postmortem.` — 保留日志供复盘。

## 恢复与复盘

- `The service has recovered, and we’re monitoring it closely.` — 服务已恢复，密切监控。
- `We’ll write a blameless postmortem.` — 写一份不追责的复盘。
- `The main contributing factor was an unbounded retry loop.` — 主要诱因是无上限重试。
- `The action items are to add an alert, a timeout, and a regression test.` — 行动项是告警、超时和回归测试。
- `We should distinguish the trigger from the underlying cause.` — 区分直接触发因素和根本原因。

## 30 秒状态更新模板

> We’re currently seeing [impact]. The likely cause is [hypothesis, if confirmed]. We’ve taken [mitigation], and the error rate is [trend]. The root cause is still under investigation. I’ll post the next update at [time].

## 练习

- [ ] 用一次真实/虚构事故练 30 秒更新
- [ ] 把“已找到根因”和“仍在调查”两种状态各说一遍

## 相关

- [[02_daily-work/_index|日常工作]]
- [[08_sentence-library/daily-work|日常工作句子库]]

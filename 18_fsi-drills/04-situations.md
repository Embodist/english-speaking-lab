---
type: guide
title: "情景训练"
tags: [skill/speaking, status/learning]
created: 2026-11-05
updated: 2026-11-05
---

# 情景训练

> 每个情景先不看答案，自己说 1–2 句，再对照模型句。

## 站会

| 你要说什么 | 模型句 |
|---|---|
| 汇报昨天做了什么 | Yesterday I fixed the flaky test and reviewed two PRs. |
| 汇报今天做什么 | Today I'll finish the migration script and run a load test. |
| 说明阻塞项 | I'm blocked on staging access. Could someone approve the request? |

## 事故

| 你要说什么 | 模型句 |
|---|---|
| 说明现状 | We're seeing a spike in 5xx errors on the recommendation service. |
| 给出缓解措施 | We rolled back the last deploy and the error rate is coming down. |
| 说明下一步 | I'll post an update every 15 minutes until the error rate is back to normal. |

## 代码评审

| 你要说什么 | 模型句 |
|---|---|
| 提出非阻塞建议 | Non-blocking suggestion: could we extract this into a helper? |
| 指出阻塞问题 | This is a blocker because it breaks backward compatibility. |

## 设计评审

| 你要说什么 | 模型句 |
|---|---|
| 提出担忧 | I agree with the goal, but I'm concerned about the operational cost. |
| 给出替代方案 | One option is to add a cache; another is to batch the requests. |

## 面试

| 你要说什么 | 模型句 |
|---|---|
| 介绍项目背景 | The system answers questions over internal documents for the support team. |
| 说明你的贡献 | I designed the retrieval pipeline and built the evaluation harness. |
| 讲清结果 | We cut the average response time from 4 seconds to 1.2 seconds. |
| 说明取舍 | The main trade-off was recall versus latency, and we chose recall. |

## 跨团队

| 你要说什么 | 模型句 |
|---|---|
| 提出请求 | Could your team expose the metrics through the existing API? |
| 协商时间 | We can start next sprint if that works for you. |

## 进阶

把四句话连成一段 60 秒独白，录音；第二天脱稿再说一遍。

## 相关

- [[18_fsi-drills/_index|FSI 训练总览]]
- [[06_interview/mock-interview|模拟面试]]
- [[02_daily-work/standup|站会]]

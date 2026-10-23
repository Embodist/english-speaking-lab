---
type: topic
title: 恶意流量分析
tags: [topic/security, skill/speaking, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# 恶意流量分析

## 高频句

- `The system flags suspicious traffic for further investigation.` — 标记可疑流量待调查。
- `The model summarizes the evidence behind each alert.` — 模型总结告警背后的证据。
- `We need to reduce false positives without missing real attacks.` — 减少误报且不漏真攻击。
- `The alert lacks enough context to make a confident decision.` — 告警上下文不足。
- `We enrich the event with asset and threat-intelligence data.` — 用资产和威胁情报丰富事件。
- `The analyst can accept, edit, or reject the suggested rule.` — 分析师可接受、修改或拒绝建议。
- `We should explain why a rule was recommended.` — 应解释推荐原因。
- `The rule needs a dry run before enforcement.` — 强制执行前先试运行。
- `Let’s measure precision, recall, and analyst review time.` — 测精确率、召回率、审核时间。
- `We must avoid exposing sensitive event data in prompts or logs.` — 避免在提示词/日志暴露敏感数据。
- `The workflow should keep a human in the loop for high-impact actions.` — 高影响操作保留人工。

## 口述模板

> First, the system collects and enriches the event. Then the model summarizes the evidence and produces a triage recommendation. The analyst can accept, edit, or reject it. Before enforcement, we run a dry test. We evaluate precision, recall, and analyst review time, and we keep sensitive data out of prompts and logs.

## 练习

- [ ] 用 60 秒讲检测闭环
- [ ] 用 30 秒解释一次误报权衡

## 相关

- [[04_security/_index|安全分析]]
- [[08_sentence-library/security-and-soar|安全句子库]]

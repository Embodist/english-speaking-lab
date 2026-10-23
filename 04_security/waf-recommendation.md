---
type: topic
title: WAF 规则建议
tags: [topic/security, skill/speaking, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# WAF 规则建议

## 讲故事结构

1. **问题**：告警多、上下文少、规则维护慢。
2. **方案**：LLM 总结证据并给出规则建议，分析师审核。
3. **安全控制**：dry run、最小权限、敏感数据脱敏、人工审批。
4. **评测**：precision / recall / review time。
5. **结果与局限**：只用真实数据；说明误报和对抗风险。

## 关键句

- `The rule recommendation is reviewed by an analyst before deployment.`
- `The analyst can accept, edit, or reject the suggested rule.`
- `We should explain why a rule was recommended.`
- `The rule needs a dry run before enforcement.`
- `We must avoid exposing sensitive event data in prompts or logs.`
- `The workflow should keep a human in the loop for high-impact actions.`
- `We need to reduce false positives without missing real attacks.`

## 可能追问

| 问题 | 回答方向 |
|---|---|
| How do you prevent prompt injection from event data? | 工具输出与事件内容视为不可信输入；确定性校验；最小权限 |
| How do you evaluate rule quality? | 固定评测集 + precision/recall + 分析师审核时间 |
| What if the model is wrong? | 人工审批 + dry run + 可回滚 |
| How do you handle sensitive data? | 脱敏、最小上下文、日志审计 |

## 练习

- [ ] 录一段 90 秒 WAF 项目介绍
- [ ] 回答“模型建议错误怎么办”

## 相关

- [[04_security/_index|安全分析]]
- [[06_interview/project-stories|项目故事]]

---
type: hub
title: 安全分析
tags: [hub, topic/security]
created: 2026-10-23
updated: 2026-10-23
---

# 安全分析

目标：讲清“检测 → 证据 → 建议 → 人工审核”的闭环，强调**可解释、可评测、可审计**。

## 笔记

- [[04_security/malicious-traffic|恶意流量分析]]
- [[04_security/waf-recommendation|WAF 规则建议]]

## 核心叙事

> The system flags suspicious traffic for further investigation. The model summarizes the evidence behind each alert and suggests a rule change. An analyst can accept, edit, or reject the recommendation. We measure precision, recall, and analyst review time, and we require a dry run before enforcement.

## 关键原则

1. **人在环内**：高影响操作必须人工审核。
2. **证据可追溯**：每条告警和规则建议都能解释原因。
3. **先试运行**：dry run 后才强制执行。
4. **数据保护**：提示词和日志不暴露敏感事件数据。
5. **评测双向**：既要降误报，也不能漏真攻击。

## 练习

- [ ] 用 60 秒讲一次“告警 → 建议 → 审核 → 上线”
- [ ] 准备一次误报权衡的回答

## 相关

- [[08_sentence-library/security-and-soar|安全句子库]]
- [[09_sources/01_AI工程师英语面试与工作训练手册.docx|AI 工程师训练手册]]

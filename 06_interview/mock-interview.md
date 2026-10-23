---
type: topic
title: 模拟面试
tags: [skill/interview, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# 模拟面试

## 15 分钟流程

| 时间 | 环节 |
|---|---|
| 0–2 min | Tell me about yourself |
| 2–7 min | Walk me through a project |
| 7–11 min | 技术追问（RAG / Agent / 部署 / 安全 / 音乐） |
| 11–14 min | 行为题（冲突、失败、优先级） |
| 14–15 min | 反问与总结 |

录音，回听后按下面的表打分。

## 高频题与答题框架

| 问题 | 框架 |
|---|---|
| Tell me about yourself. | 身份 → 背景 → 两个项目 → 方向 |
| Walk me through a project. | Goal → Challenge → Responsibility → Approach → Trade-off → Validation → Result |
| How did you design the RAG pipeline? | 五阶段 + 检索/生成分开评测 |
| How do you evaluate an agent? | 组件级 + 端到端 + 负例 |
| How do you reduce hallucinations in RAG? | 先测检索 → 查依据 → 改切块/检索/重排/提示 → 固定评测集 |
| How do you debug latency? | 分阶段测量 → p50/p95 → 逐一验证 |
| Describe a difficult bug. | 复现 → 日志 → 假设 → 修复 → 回归测试 |
| What is your approach to code quality? | 小改动、测试、CI、评测案例 |
| What is a weakness? | 真实可改进：口语表达 |
| Why are you interested in this role? | 经历匹配 + 具体方向 |
| How do you handle disagreement? | 目标与方案分离 → 假设 → 风险 → 用同一标准验证 |
| What if you don’t know the answer? | 已知 / 未知 / 验证路径 |

## 自评表（每项 0–2 分）

| 维度 | 分数 |
|---|---|
| 先说结论 |  |
| 结构清楚（2–3 点） |  |
| 取舍讲明白 |  |
| 有验证方式 |  |
| 语言可理解 |  |
| 没有编造数据 |  |
| **合计 / 12** |  |

## 不知道答案时

- `I haven’t worked with that exact technology, so I don’t want to overstate my experience.`
- `I understand the underlying concept, but I’d need to verify the details.`
- `I’d start by checking the official documentation and building a small proof of concept.`
- `I’m not sure about the exact API, but the design I’d consider is …`

## 反问

- `Could you tell me what success looks like in the first six months?`
- `What are the biggest reliability challenges for the team right now?`
- `How does the team evaluate AI quality today?`

## 相关

- [[06_interview/introduction|自我介绍]]
- [[06_interview/project-stories|项目故事]]
- [[STUDY-PLAN#面试专项|面试专项]]

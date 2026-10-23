---
type: topic
title: Agent 与工作流框架
tags: [topic/agent, skill/speaking, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# Agent 与工作流框架

> 讲 Agent 时，面试官更关心**状态、失败处理、权限和评测**，而不是你用了哪个框架的哪个 API。

## 一、框架与模式

| 名称 | 解决什么 | 常见取舍 | 说（英文） |
|---|---|---|---|
| LangChain | 组合模型、检索、工具 | 抽象多，调试链路长 | `We use LangChain to compose retrieval and generation steps.` |
| LangGraph | 有状态的图式工作流 | 需要显式设计状态和边 | `LangGraph manages the workflow state and transitions.` |
| ReAct | 推理 + 行动循环 | 容易循环；需要上限 | `The agent reasons, acts, and observes in a loop.` |
| Tool / function calling | 模型调用外部函数 | 参数错误、工具选择错误 | `The agent decides which tool to call from the user request.` |
| Planner–executor | 先规划再执行 | 规划器可能过度复杂 | `We separate planning from execution.` |
| Router | 按意图分发到不同链路 | 路由错误会放大 | `A router sends each request to the right workflow.` |
| Human-in-the-loop | 敏感操作人工确认 | 增加延迟和人力 | `Sensitive actions require human approval.` |

## 二、可靠性设计

| 能力 | 做法 | 说（英文） |
|---|---|---|
| 状态持久化 | 序列化状态，支持恢复 | `We persist the workflow state so a job can resume.` |
| 有界重试 | 限制次数 + 退避 | `We use bounded retries for transient errors.` |
| 降级路径 | 工具失败时切换方案 | `If the tool fails, we switch to a fallback path.` |
| 参数校验 | 执行前校验工具参数 | `We validate tool arguments before execution.` |
| 输出校验 | schema + 确定性检查 | `We validate structured output against a schema.` |
| 循环控制 | 限制工具调用次数 | `We limit the number of tool calls to avoid runaway loops.` |
| 权限控制 | 最小权限 + 人工审批 | `Tool execution uses least-privilege permissions.` |
| 可观测性 | 记录每次工具调用 | `We log each tool call for debugging and observability.` |
| 提示注入防护 | 工具/检索结果视为不可信 | `We treat tool output as untrusted input.` |

## 三、评测

| 层级 | 看什么 | 说（英文） |
|---|---|---|
| 组件级 | 工具是否选对、参数是否有效、结果是否正确处理 | `We check tool selection and argument validity.` |
| 端到端 | 任务成功率、答案质量、恢复能力 | `We evaluate the entire workflow, not just the model response.` |
| 负例 | 歧义请求、工具失败、缺失来源 | `We include ambiguous requests and tool failures.` |
| 成本/延迟 | 调用次数、tokens、p95 | `We track tool calls, token usage, and p95 latency.` |
| 安全 | 越权、注入、敏感操作 | `We test whether the agent can be tricked into unsafe actions.` |

## 四、常见追问

| 问题 | 回答方向 |
|---|---|
| How do you prevent runaway loops? | 调用次数上限 + 超时 + 状态检查 + 人工终止 |
| How do you handle tool failure? | 有界重试 → 降级 → 明确告知用户 |
| How do you evaluate the agent? | 组件级 + 端到端 + 负例 + 成本 |
| How do you debug a bad answer? | 看轨迹：意图 → 工具选择 → 参数 → 结果 → 最终生成 |
| How do you keep state consistent? | 序列化 + 幂等 + 恢复点 + 状态校验 |

## 五、项目表述模板

> The agent uses a graph-based workflow. The request goes through intent understanding and planning. The executor calls tools with validated arguments. We persist state so long-running jobs can resume, and we use bounded retries with a fallback path. We evaluate tool selection, end-to-end success, failure recovery, latency, and cost. The main risk is an invalid intermediate state, so we add deterministic checks around model output.

## 六、严谨性检查

- [ ] 我是否讲清了状态存在哪里、如何恢复？
- [ ] 我是否说明了失败时的行为？
- [ ] 我是否区分了“工具成功”和“答案正确”？
- [ ] 我是否给出了真实的评测方式？

## 相关

- [[13_tech-frameworks/_index|技术与框架]]
- [[03_ai-agent-rag/agent-overview|Agent 架构]]
- [[12_word-phrase-bank/06-ai-llm-terms|AI / LLM 术语]]

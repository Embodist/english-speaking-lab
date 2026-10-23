---
type: topic
title: Agent 架构与工具调用
tags: [topic/agent, skill/speaking, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# Agent 架构与工具调用

## 描述架构

- `The agent uses a planner-executor pattern.` — 使用规划器—执行器模式。
- `LangGraph manages the workflow state and transitions.` — LangGraph 管理状态与转移。
- `The agent decides which tool to call based on the user’s request.` — 根据请求选择工具。
- `We validate tool arguments before execution.` — 执行前校验参数。
- `The tool returns structured data, which is passed to the next step.` — 工具返回结构化数据传给下一步。
- `We added a retry for transient failures.` — 对瞬时故障增加重试。
- `The workflow has a fallback path when generation fails.` — 生成失败时有降级路径。
- `We limit the number of tool calls to avoid runaway loops.` — 限制调用次数防止失控循环。
- `The agent should ask a clarifying question when the request is ambiguous.` — 请求有歧义时先澄清。
- `We separate planning, execution, and evaluation.` — 规划、执行、评估分离。
- `The state needs to be serializable so we can resume interrupted runs.` — 状态可序列化以恢复中断。
- `We log each tool call for debugging and observability.` — 记录每次工具调用。

## 局限与风险

- `The agent sometimes chooses the wrong tool.` — 有时选错工具。
- `The planner overcomplicates simple requests.` — 规划器把简单请求复杂化。
- `We need to distinguish tool errors from model errors.` — 区分工具错误与模型错误。
- `A successful tool call doesn’t guarantee a correct final answer.` — 调用成功不代表答案正确。
- `We should evaluate the entire workflow, not just the model response.` — 评测整个工作流。
- `The main risk is an invalid intermediate state.` — 主要风险是中间状态无效。
- `We can add deterministic checks around the model’s output.` — 在输出外层加确定性校验。

## 安全与可靠性

- `We use least-privilege permissions for tool execution.` — 工具执行使用最小权限。
- `We treat tool output as untrusted input.` — 工具输出视为不可信输入。
- `We require human approval for sensitive actions.` — 敏感操作需要人工审批。
- `We persist the workflow state so a job can resume.` — 持久化状态以恢复任务。
- `We use bounded retries for transient errors.` — 有限重试。

## 60 秒讲法

> The agent uses a graph-based workflow. The request first goes through intent understanding. Then the planner decides which tool to call. We validate tool arguments and treat tool output as untrusted input. If a tool fails, we retry a bounded number of times and then switch to a fallback path. We persist state so long-running jobs can resume, and we log every tool call for observability. The main limitation is that a successful tool call doesn’t guarantee a correct answer, so we evaluate the whole workflow end to end.

## 练习

- [ ] 画一遍工作流，用 `First / Then / Finally` 口述
- [ ] 准备“工具调用成功≠答案正确”的例子
- [ ] 用 30 秒说清权限与人工审批

## 相关

- [[03_ai-agent-rag/_index|AI 与 RAG]]
- [[08_sentence-library/agent-and-tools|Agent 句子库]]
- [[06_interview/project-stories|项目故事]]

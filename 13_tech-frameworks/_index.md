---
type: hub
title: 技术与框架记录
tags: [hub, topic/agent, topic/rag, topic/music]
created: 2026-10-23
updated: 2026-10-23
---

# 技术与框架记录

记录你项目里用到的**能力、框架、指标和取舍**。目标不是背 API，而是能在面试和会议中解释：

1. 它解决什么问题；
2. 你用它做了什么；
3. 主要取舍是什么；
4. 你如何验证。

> [!warning] 严谨性说明
> 技术能力和框架行为会随版本变化。这里记录的是**讲解框架**和**常用说法**，不是安装手册或权威规范。涉及具体版本、性能数字、许可证时，以官方文档和你项目的实测为准；不确定就说“I’d verify it”。

## 分册

| 分册 | 内容 |
|---|---|
| [[13_tech-frameworks/llm-model-capabilities\|LLM 与模型能力]] | 训练、推理、上下文、量化、评测、护栏 |
| [[13_tech-frameworks/agent-frameworks\|Agent 与工作流框架]] | LangChain、LangGraph、ReAct、工具调用、状态 |
| [[13_tech-frameworks/music-ai-stack\|音乐 AI 技术栈]] | 生成、翻唱、分离、转换、音高/和声、跨模态 |
| [[13_tech-frameworks/rag-eval-serving\|RAG、评测与服务]] | 检索、重排、评测指标、vLLM/批量推理 |

## 每个能力的记录格式

- **是什么**：一句话定义。
- **关键指标 / 取舍**：延迟、质量、成本、复杂度。
- **说**：面试/会议中的英文句子。
- **你的项目关联**：只写真实做过的部分。

## 与词汇库的关系

- 需要词汇和例句：[[12_word-phrase-bank/06-ai-llm-terms|AI / LLM 术语]]。
- 需要整句表达：[[03_ai-agent-rag/_index|AI 与 RAG]]、[[05_music-agent/_index|音乐 Agent]]。
- 需要学习顺序：[[LEARNING-PATH|学习路径]]。

## 相关

- [[12_word-phrase-bank/_index|词与短语库]]
- [[06_interview/project-stories|项目故事]]

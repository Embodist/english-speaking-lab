---
type: hub
title: 音乐 Agent
tags: [hub, topic/music]
created: 2026-10-23
updated: 2026-10-23
---

# 音乐 Agent

目标：把多模态项目讲成“**能力链 + 工具编排 + 可评测性**”，而不是只描述效果。

## 笔记

- [[05_music-agent/music-generation|音乐生成与转换]]
- [[05_music-agent/cross-modal-retrieval|跨模态检索]]

## 核心叙事

> I’m building an agent for music creation and cover generation. The user describes the desired style in natural language. The workflow retrieves relevant musical references before generation, and the agent coordinates multiple tools instead of relying on a single model call. We separate content planning from audio generation. The main challenge is balancing creative flexibility with predictable behavior.

## 要讲清的四件事

1. **输入**：用户如何描述风格。
2. **编排**：LangGraph / tool calling 如何协调音高、和声、转换、后期。
3. **取舍**：创作自由度 vs 行为可预测性；主观质量 vs 可重复测试。
4. **底线**：版权检查、guardrails、工作流可靠性。

## 练习

- [ ] 90 秒项目介绍，录音
- [ ] 回答“如何评测主观音频质量”
- [ ] 回答“生成成功但转换失败怎么办”

## 相关

- [[13_tech-frameworks/music-ai-stack|音乐 AI 技术栈]]
- [[06_interview/project-stories|项目故事]]
- [[08_sentence-library/music-and-multimodal|音乐多模态句子库]]

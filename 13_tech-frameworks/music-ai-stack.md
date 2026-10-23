---
type: topic
title: 音乐 AI 技术栈
tags: [topic/music, topic/rag, skill/speaking, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# 音乐 AI 技术栈

> 记录“能力”而不是绑死某个模型。常见工具会随版本变化；**许可证、音色克隆授权和版权**必须逐项确认。

## 一、能力全景

```text
自然语言 / 音频输入
  → 意图理解与风格解析
  → 音乐参考检索（文本-音频跨模态）
  → 内容规划（结构、音高、和声）
  → 音乐生成 / 翻唱生成
  → 人声分离与转换
  → 音频后期处理
  → 版权与安全检查
  → 评测与交付
```

## 二、能力与常见工具

| 能力 | 常见工具 / 框架 | 关键指标 / 取舍 | 说（英文） |
|---|---|---|---|
| 音乐生成 | ACE-Step 等生成模型 | 多样性 vs 可控性；质量评估主观 | `The agent supports music generation from natural-language prompts.` |
| 翻唱生成 | 生成 + 人声转换组合 | 保旋律 vs 换音色 | `The workflow includes a cover-generation step.` |
| 音源分离 | Demucs 等分离模型 | 分离质量 vs 速度 | `We separate the vocal track before processing it.` |
| 人声转换 / SVC | RVC、SVC 模型 | 音色相似度 vs 自然度 | `SVC converts the singing voice while preserving the melody.` |
| 音高分析 | librosa、CREPE、basic-pitch | 帧级精度 vs 计算成本 | `Pitch analysis produces a frame-level contour.` |
| 和声分析 | 和弦识别模型 / 规则 | 准确率 vs 复杂度 | `Harmony analysis estimates chord progressions.` |
| 音频嵌入 | CLAP、MERT 等 | 语义对齐 vs 领域适配 | `We use audio embeddings for similarity search.` |
| 跨模态检索 | 文本/音频共享嵌入空间 | 召回 vs 排序质量 | `Cross-modal retrieval aligns text queries with audio.` |
| 向量检索 | Faiss、Milvus 等 | 延迟 vs 召回 | `The retriever returns the top-k audio candidates.` |
| 音频后期 | 响度归一化、限幅、混音 | 听感 vs 失真风险 | `Post-processing includes loudness normalization and limiting.` |
| 版权检查 | 指纹/规则/人工审核 | 召回 vs 误杀 | `The pipeline includes a copyright check before delivery.` |
| 质量评测 | 人工评分 + 客观指标 | 主观性 vs 可重复性 | `We use a fixed rubric for subjective audio quality.` |

## 三、讲清楚“为什么用 Agent”

> We use an agent because the task is multi-step and each step has a different tool. The agent coordinates pitch analysis, reference retrieval, generation, conversion, and post-processing. We keep deterministic steps separate from model-driven decisions, and we validate the output at each stage. The main challenge is balancing creative flexibility with predictable behavior.

## 四、评测主观质量

| 维度 | 问什么 | 英文表达 |
|---|---|---|
| 旋律保持 | 旋律是否可辨认 | `Does the output preserve the original melody?` |
| 音色相似度 | 是否接近目标音色 | `How close is the converted timbre to the target?` |
| 自然度 | 是否有明显 artifacts | `Are there audible artifacts or unnatural transitions?` |
| 结构完整 | 段落是否完整 | `Is the song structure coherent?` |
| 可控性 | 是否符合提示 | `Does the output follow the requested style?` |

评测方法：固定评测集 + 固定 rubric + 多人评分 + 记录分歧；不要只看一个 demo。

## 五、常见追问

| 问题 | 回答方向 |
|---|---|
| How do you evaluate subjective quality? | 固定 rubric + 多人评分 + 固定样本 |
| What if conversion fails? | 重试/降级到另一后端/返回部分结果并说明 |
| How do you handle copyright? | 版权检查 + 人工审核 + 限制输出 |
| How do you keep the melody? | 分离音高/内容与音色；分阶段验证 |
| Why not one model? | 任务异构；单模型难同时保证质量、可控性和延迟 |

## 六、严谨性检查

- [ ] 我是否把“调用现成模型”说成了“自己训练”？
- [ ] 我是否说明了音色克隆的授权与版权边界？
- [ ] 我是否给出了真实的评测方式和样本规模？
- [ ] 我是否区分了 demo 效果和可重复测试？

## 相关

- [[13_tech-frameworks/_index|技术与框架]]
- [[05_music-agent/_index|音乐 Agent]]
- [[12_word-phrase-bank/07-security-music-terms|安全与音乐术语]]
- [[03_ai-agent-rag/agent-overview|Agent 架构]]

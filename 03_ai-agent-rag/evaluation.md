---
type: topic
title: 评测与实验
tags: [topic/eval, skill/speaking, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# 评测与实验

## 核心句

- `We need a reliable baseline before changing the prompt.` — 改提示词前先有可靠基线。
- `I ran an ablation to understand which component matters most.` — 做消融实验确认关键组件。
- `The improvement is small and may be within the noise.` — 提升小，可能在噪声范围内。
- `We should evaluate on held-out examples.` — 在留出样本上评测。
- `The model follows the format, but the content is inaccurate.` — 格式对但内容不准。
- `We evaluate retrieval quality separately from answer quality.` — 检索和答案质量分开评测。
- `Let’s measure recall at k and answer faithfulness separately.` — 分别测 Recall@k 与忠实度。
- `A successful tool call doesn’t guarantee a correct answer.` — 工具成功不代表答案正确。
- `We should evaluate the entire workflow, not just the model response.` — 评测整个工作流。
- `Let’s keep the random seed fixed for reproducibility.` — 固定随机种子以便复现。

## 评测框架

| 层级 | 看什么 |
|---|---|
| 组件 | 工具是否选对、参数是否有效、检索是否召回 |
| 端到端 | 任务成功率、答案质量、失败恢复、延迟、成本 |
| 负例 | 歧义请求、工具失败、缺失来源、恶意输入 |
| 回归 | 固定评测集 + 固定随机种子 + 前后对比 |

## 60 秒讲法

> I evaluate the agent at both the component level and the end-to-end level. For each tool, I check whether it is selected correctly, whether the arguments are valid, and whether the result is handled properly. For the whole workflow, I look at task success, answer quality, failure recovery, latency, and cost. I also include negative cases, ambiguous requests, and tool failures. A successful tool call alone doesn’t guarantee that the final answer is correct.

## 练习

- [ ] 准备一个“指标提升但质量下降”的例子
- [ ] 用 30 秒解释 baseline、held-out set、ablation

## 相关

- [[03_ai-agent-rag/rag-pipeline|RAG]]
- [[08_sentence-library/model-and-inference|模型与推理句子库]]

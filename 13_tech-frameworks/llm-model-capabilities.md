---
type: topic
title: LLM 与模型能力
tags: [topic/agent, topic/deployment, skill/speaking, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# LLM 与模型能力

> 面试时先区分：**你训练过、微调过、部署过、还是只调用过 API**。不要把这四件事混在一起说。

## 一、模型生命周期

| 阶段 | 是什么 | 关键取舍 | 说（英文） |
|---|---|---|---|
| Pretraining | 在大规模语料上学习通用能力 | 成本极高；数据质量决定上限 | `The base model is pretrained on a large corpus.` |
| Supervised fine-tuning (SFT) | 用标注指令数据继续训练 | 需要高质量标注；可能过拟合 | `We fine-tuned the model on domain-specific instructions.` |
| RLHF / DPO | 用人类偏好优化回答 | 偏好数据难做；训练复杂 | `Preference optimization aligns the model with human preferences.` |
| PEFT / LoRA | 只训练少量适配参数 | 成本低；容量有限 | `LoRA keeps the base model frozen and trains a small adapter.` |
| Quantization | 降低权重精度（如 4-bit/8-bit） | 省显存；可能损失质量 | `Quantization reduces memory at the cost of some quality.` |
| Distillation | 用大模型教小模型 | 推理便宜；上限受教师限制 | `Distillation transfers behavior to a smaller model.` |
| Evaluation | 用固定集合比较版本 | 评测集质量比分数重要 | `We evaluate on a held-out set before changing the prompt.` |

## 二、推理与服务

| 能力 | 是什么 | 指标 | 说（英文） |
|---|---|---|---|
| Context window | 单次可处理的 token 上限 | 上下文越长，成本/延迟越高 | `The context window limits how much retrieved text we can pass.` |
| Tokenization | 文本切成 token | 影响长度、成本、语言差异 | `The tokenizer splits text into subword tokens.` |
| KV cache | 缓存注意力键值，避免重复计算 | 显存换速度 | `KV caching reduces repeated computation during decoding.` |
| Batching | 合并请求提高 GPU 利用率 | 吞吐上升，单请求延迟可能上升 | `Dynamic batching improves throughput.` |
| TTFT | 首 token 时间 | 影响交互体验 | `We track time to first token as a UX metric.` |
| TPS | 每秒生成 token 数 | 影响长回答的完成时间 | `Throughput is measured in tokens per second.` |
| Streaming | 边生成边返回 | 降低感知延迟 | `Streaming output reduces perceived latency.` |
| Speculative decoding | 小模型草拟、大模型校验 | 提速但实现复杂 | `Speculative decoding can reduce latency for long outputs.` |
| Prompt caching | 复用相同前缀的计算 | 长系统提示词场景收益大 | `Prompt caching helps when many requests share the same prefix.` |

## 三、关键能力与局限

| 能力 | 能做什么 | 主要风险 | 说（英文） |
|---|---|---|---|
| Reasoning | 多步推理、规划 | 错误会级联；不可解释 | `The model can plan, but the plan still needs verification.` |
| Tool use | 调用函数、查询系统 | 选错工具、参数错误 | `Tool calling lets the model act on external systems.` |
| Structured output | 输出 JSON / schema | 格式错误、字段缺失 | `We validate structured output against a schema.` |
| Long context | 处理长文档 | 中间信息丢失、成本高 | `Long context is not a substitute for good retrieval.` |
| Multimodal | 文本 + 图像/音频 | 跨模态对齐难 | `Cross-modal retrieval aligns text and audio embeddings.` |
| RAG | 用外部知识回答 | 检索失败、答案无依据 | `The answer should be grounded in the retrieved sources.` |
| Agent | 多步执行、工具编排 | 状态错误、循环失控 | `A successful tool call doesn’t guarantee a correct answer.` |

## 四、常见追问与回答方向

| 问题 | 回答框架 |
|---|---|
| How do you reduce hallucinations? | 先测检索 → 查依据 → 改切块/检索/重排/提示 → 固定评测集 |
| How do you choose a model? | 质量、延迟、成本、上下文、许可、可部署性 |
| How do you evaluate a model? | 固定评测集 + 指标 + 人工抽检 + 失败分析 |
| How do you reduce latency? | 分阶段测量 → 批处理/缓存/量化/流式 → 一次只改一项 |
| How do you control cost? | 缩短上下文、缓存、批量、小模型路由、限制重试 |
| How do you handle long documents? | 分块 + 检索 + 重排；不要盲目塞满上下文 |
| Did you train the model? | 明确：预训练 / 微调 / 部署 / API 调用，是哪一种 |

## 五、项目表述模板

> We used a [base model] for [task]. We [fine-tuned / served / called] it with [method]. The main challenge was [challenge]. We evaluated it on [dataset] using [metrics]. The main trade-off was [trade-off], and we mitigated it by [mitigation].

## 六、严谨性检查

- [ ] 我是否把“调用 API”说成了“训练模型”？
- [ ] 我是否给出了未实测的延迟/准确率数字？
- [ ] 我是否说明了评测集来源和规模？
- [ ] 我是否区分了离线评测和线上效果？

## 相关

- [[13_tech-frameworks/_index|技术与框架]]
- [[12_word-phrase-bank/06-ai-llm-terms|AI / LLM 术语]]
- [[03_ai-agent-rag/_index|AI 与 RAG]]
- [[12_word-phrase-bank/04-paper-reading|论文阅读]]

---
type: word-bank
title: AI / LLM 术语
tags: [library/word-bank, topic/agent, topic/rag, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# AI / LLM 术语（45）

覆盖模型训练、推理、RAG、Agent 与评测。术语解释偏“能开口讲清楚”，不是教科书定义。

| 级别 | 术语 | 中文 | 说（口语例句） | 写（书面例句） | 读 / 搭配 |
|---|---|---|---|---|---|
| S | large language model (LLM) | 大语言模型 | We use an LLM to generate the answer. | The system is built on an open-weight LLM. | LLM-powered assistant |
| S | token | token | The input is limited to 8k tokens. | Token-level accuracy is reported. | token budget |
| A | tokenizer | 分词器 | The tokenizer splits text into subwords. | We use the model’s tokenizer. | tokenizer vocabulary |
| S | embedding | 向量嵌入 | We generate embeddings for each chunk. | The embedding model maps text to vectors. | dense embedding |
| S | context window | 上下文窗口 | The context window is too small for the document. | The context window limits the amount of retrieved text. | context-window limit |
| S | prompt | 提示词 | The prompt asks for a structured answer. | The prompt template includes the retrieved context. | prompt engineering |
| S | system prompt | 系统提示词 | The system prompt defines the role. | The system prompt constrains the output format. | update the system prompt |
| A | zero-shot | 零样本 | It works zero-shot. | Zero-shot performance is lower than fine-tuned performance. | zero-shot setting |
| A | few-shot | 少样本 | We give three few-shot examples. | Few-shot prompting improves format compliance. | few-shot examples |
| A | chain-of-thought | 思维链 | Chain-of-thought helps with multi-step reasoning. | We use chain-of-thought prompting for planning. | reasoning trace |
| A | instruction tuning | 指令微调 | The model was instruction-tuned. | Instruction tuning improves following rate. | instruction-following |
| S | supervised fine-tuning (SFT) | 监督微调 | We did SFT on domain data. | SFT is performed on 10k labeled examples. | SFT dataset |
| A | RLHF | 人类反馈强化学习 | RLHF aligns the model with preferences. | RLHF uses human preference data. | preference optimization |
| A | DPO | 直接偏好优化 | DPO is simpler than RLHF. | DPO optimizes the policy directly on preferences. | direct preference optimization |
| A | LoRA | 低秩适配 | We use LoRA to reduce training cost. | LoRA adapts a small number of parameters. | low-rank adaptation |
| A | PEFT | 参数高效微调 | PEFT keeps the base model frozen. | PEFT methods include LoRA and adapters. | parameter-efficient fine-tuning |
| A | quantization | 量化 | 4-bit quantization reduces memory. | Quantization lowers memory usage but may hurt quality. | 4-bit / INT8 quantization |
| B | distillation | 蒸馏 | The small model is distilled from the large one. | Distillation transfers behavior to a smaller model. | knowledge distillation |
| S | inference | 推理 | Inference is expensive at long context. | Inference latency is measured at p95. | inference cost |
| S | model serving | 模型服务 | We serve the model behind an API. | The model-serving layer handles batching. | model-serving infrastructure |
| A | KV cache | KV 缓存 | The KV cache grows with context length. | KV caching reduces repeated computation. | KV-cache memory |
| A | batching | 批处理 | Batching improves throughput. | Dynamic batching increases GPU utilization. | batch size |
| A | throughput | 吞吐量 | We measure throughput in tokens per second. | Throughput improved after batching. | requests per second |
| A | time to first token (TTFT) | 首 token 时间 | TTFT is the main UX metric. | We report time to first token. | TTFT |
| A | tokens per second (TPS) | 每秒 token 数 | TPS is fine, but TTFT is high. | The service reaches 1,200 tokens per second. | TPS |
| S | hallucination | 幻觉 | The model hallucinated a citation. | We measure hallucination on a held-out set. | reduce hallucinations |
| S | grounding | 依据性 | The answer should be grounded in the sources. | Grounding is evaluated against retrieved evidence. | grounded answer |
| S | retrieval-augmented generation (RAG) | 检索增强生成 | We use RAG to answer from documents. | The RAG pipeline combines retrieval and generation. | RAG pipeline |
| S | chunking | 分块 | Chunk size affects retrieval quality. | We use section-level chunking. | document chunking |
| S | retriever | 检索器 | The retriever misses some documents. | The retriever returns the top-k passages. | dense / sparse retriever |
| A | reranker | 重排器 | The reranker improves relevance. | A cross-encoder reranker is applied to the top 50 candidates. | semantic reranking |
| A | hybrid search | 混合检索 | Hybrid search combines vectors and keywords. | Hybrid search improves recall on rare terms. | hybrid retrieval |
| A | vector database | 向量数据库 | We store embeddings in a vector database. | The vector database supports metadata filtering. | Milvus / Faiss |
| S | recall at k | 前 k 召回率 | Recall at 10 is our main retrieval metric. | Recall@k is reported for k = 5, 10, 20. | Recall@k |
| A | faithfulness | 忠实度 | Faithfulness measures whether the answer matches the sources. | We evaluate answer faithfulness separately. | groundedness / faithfulness |
| A | evaluation | 评测 | We evaluate on a fixed dataset. | Evaluation uses a held-out set. | offline evaluation |
| A | benchmark | 基准测试 | The benchmark covers three tasks. | We compare against a public benchmark. | run a benchmark |
| S | agent | 智能体 | The agent decides which tool to call. | The agent coordinates multiple tools. | agentic workflow |
| S | tool calling | 工具调用 | Tool calling lets the model run functions. | Tool calling is used to query internal services. | tool / function calling |
| A | function calling | 函数调用 | Function calling is the same idea with JSON schemas. | Function calling requires a schema for each tool. | function schema |
| S | planner | 规划器 | The planner decomposes the request. | The planner selects the next step. | planning stage |
| A | executor | 执行器 | The executor runs the selected tool. | The executor validates the tool arguments. | planner–executor |
| A | workflow state | 工作流状态 | We persist the workflow state. | The state is serializable and can be resumed. | state transitions |
| A | memory | 记忆 | The agent keeps short-term memory. | Memory is limited to the current session. | short-term memory |
| S | guardrail | 防护规则 | We add guardrails for unsafe actions. | Guardrails block disallowed tool calls. | safety guardrails |
| S | prompt injection | 提示词注入 | Retrieved text can contain prompt injection. | We treat tool output as untrusted input. | defend against prompt injection |
| A | human-in-the-loop | 人在环内 | High-impact actions need human review. | Human-in-the-loop review is required before enforcement. | human approval |
| A | observability | 可观测性 | We log every tool call for observability. | Observability covers logs, metrics, and traces. | structured logs |

## 讲清一个 LLM 系统的四句话

1. **输入**：`The input is a user query plus retrieved context.`
2. **处理**：`The model generates an answer with tool calls when needed.`
3. **约束**：`We validate outputs and keep a human in the loop for sensitive actions.`
4. **评测**：`We evaluate retrieval, answer quality, latency, and cost on a fixed set.`

## 练习

- [ ] 选 10 个 S 级术语，各说一句你项目里的话
- [ ] 用“四句话”讲你的 RAG/Agent 项目，录 90 秒
- [ ] 读一篇 LLM 论文摘要，圈出 5 个术语

## 相关

- [[12_word-phrase-bank/_index|词与短语库]]
- [[03_ai-agent-rag/_index|AI 与 RAG 项目表达]]
- [[13_tech-frameworks/llm-model-capabilities|LLM 与模型能力记录]]
- [[LEARNING-PATH|学习路径]]

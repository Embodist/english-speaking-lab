---
type: paper-vocabulary
stage: 1
title: "阶段 1 · 大模型 LLM 论文词汇"
tags: [topic/paper, skill/reading, status/learning]
created: 2026-10-24
---

# 阶段 1 · 大模型 LLM 论文词汇

> 38 篇 · 381 个词条。读前扫词 2 分钟；读后遮住中文，用 abstract 片段自测，再用 5 个词复述 60 秒。
> 返回 [[14_llm-papers/_index|LLM 论文阅读]]；配套 [[14_llm-papers/reading-workflow|阅读与词汇流程]]。

## 01-01 BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

- [ ] 已读

**中文标题**：BERT：面向语言理解的深度双向 Transformer 预训练

**一句话概括**：提出 BERT，一种在无标注文本上双向预训练的深度 Transformer 表示模型，只需额外加一个输出层微调，即可在 11 项 NLP 任务上刷新当时最优成绩。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| pre-train | v. | 预训练（先在大规模无标注文本上训练通用模型） | "BERT is designed to pre-train deep bidirectional representations from unlabeled text" |
| bidirectional | adj. | 双向的（同时利用左右两侧上下文） | "BERT is designed to pre-train deep bidirectional representations" |
| representation | n. | 表示、表征（模型对文本语义的编码结果） | "a new language representation model called BERT" |
| unlabeled | adj. | 未标注的（没有人工标签的原始文本） | "pre-train deep bidirectional representations from unlabeled text" |
| conditioning | v. | 条件化（建模时把上下文作为条件考虑） | "jointly conditioning on both left and right context in all layers" |
| fine-tuned | v. | 微调（在预训练模型上用小规模任务数据继续训练） | "the pre-trained BERT model can be fine-tuned with just one additional output layer" |
| state-of-the-art | adj. | 最先进的（SOTA，当前最优水平） | "to create state-of-the-art models for a wide range of tasks" |
| inference | n. | 推断（判断句子间关系的自然语言推理任务） | "such as question answering and language inference" |
| architecture | n. | 架构（模型的整体结构设计） | "without substantial task-specific architecture modifications" |
| empirically | adv. | 从实验上、经验上 | "BERT is conceptually simple and empirically powerful" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-02 Language Models are Unsupervised Multitask Learners (GPT-2)

- [ ] 已读

**中文标题**：语言模型是无监督的多任务学习者 (GPT-2)

**一句话概括**：证明语言模型在数百万网页构成的新数据集 WebText 上训练后，无需任何显式监督即可学会问答、翻译、摘要等多种任务，且模型容量越大、零样本任务迁移性能越好（呈对数线性提升）。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| summarization | n. | 摘要生成（把长文本压缩成简短摘要的任务） | "machine translation, reading comprehension, and summarization" |
| approached | v. | 处理、解决（approach 此处指"着手应对"） | "are typically approached with supervised learning on task-specific datasets" |
| supervised learning | phr. | 监督学习（用带标签数据训练） | "are typically approached with supervised learning on task-specific datasets" |
| demonstrate | v. | 证明、展示 | "We demonstrate that language models begin to learn these tasks" |
| explicit | adj. | 显式的、明确的（此处指人工标签） | "learn these tasks without any explicit supervision when trained" |
| conditioned on | phr. | 以……为条件（把……作为输入提供给模型） | "When conditioned on a document plus questions" |
| exceeding | v. | 超过 | "matching or exceeding the performance of 3 out of 4 baseline systems" |
| baseline | adj. | 基线的（用作对比的现有系统） | "the performance of 3 out of 4 baseline systems" |
| capacity | n. | 容量、能力（模型的参数量与表达能力） | "The capacity of the language model is essential to the success" |
| zero-shot task transfer | phr. | 零样本任务迁移（不经训练直接迁移到新任务） | "essential to the success of zero-shot task transfer" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-03 Language Models are Few-Shot Learners

- [ ] 已读

**中文标题**：语言模型是少样本学习者（GPT-3）

**一句话概括**：提出 1750 亿参数的 GPT-3，证明仅靠扩大模型规模即可让语言模型在少样本（few-shot）设置下接近甚至超越微调方法的性能。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| few-shot | adj. | 少样本的（只用极少示例学习新任务） | "test its performance in the few-shot setting" |
| demonstrated | v. | 证明、展示了 | "Recent work has demonstrated substantial gains on many NLP tasks" |
| corpus | n. | 语料库（大规模文本集合） | "by pre-training on a large corpus of text followed by fine-tuning" |
| fine-tuning | n. | 微调（用任务数据在预训练模型上继续训练） | "followed by fine-tuning on a specific task" |
| task-agnostic | adj. | 任务无关的（不针对特定任务设计结构） | "While typically task-agnostic in architecture, this method still requires" |
| struggle | v. | 难以做到、表现吃力 | "which current NLP systems still largely struggle to do" |
| scaling up | phr. | 扩大（模型）规模 | "we show that scaling up language models greatly improves task-agnostic" |
| autoregressive | adj. | 自回归的（逐词预测下一个词来生成） | "we train GPT-3, an autoregressive language model with 175 billion parameters" |
| on-the-fly | adj. | 临场的、即时的（需要即时推理） | "several tasks that require on-the-fly reasoning or domain adaptation" |
| evaluators | n. | 评估者、评测人员 | "news articles which human evaluators have difficulty distinguishing from" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-04 Scaling Laws for Neural Language Models

- [ ] 已读

**中文标题**：神经语言模型的规模定律

**一句话概括**：系统研究语言模型性能随模型大小、数据量与算力变化的经验规律（幂律关系），并据此指导固定算力预算的最优分配。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| scaling laws | n. | 规模定律（性能随规模变化的规律） | "We study empirical scaling laws for language model performance" |
| empirical | adj. | 经验的、实证的（由实验数据得出） | "We study empirical scaling laws for language model performance" |
| cross-entropy | n. | 交叉熵（衡量预测分布与真实分布差异的损失） | "language model performance on the cross-entropy loss" |
| power-law | n. | 幂律（呈幂函数关系的规律） | "The loss scales as a power-law with model size" |
| compute | n. | 算力、计算量 | "the amount of compute used for training" |
| orders of magnitude | phr. | 数量级（每十倍为一个数量级） | "with some trends spanning more than seven orders of magnitude" |
| overfitting | n. | 过拟合（模型死记训练数据而泛化变差） | "Simple equations govern the dependence of overfitting on model/dataset size" |
| allocation | n. | 分配（对算力预算的最优配置） | "to determine the optimal allocation of a fixed compute budget" |
| sample-efficient | adj. | 样本高效的（用较少数据达到较好效果） | "Larger models are significantly more sample-efficient" |
| convergence | n. | 收敛（训练损失趋于平稳不再下降） | "and stopping significantly before convergence" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-05 Training Compute-Optimal Large Language Models

- [ ] 已读

**中文标题**：训练算力最优的大语言模型（Chinchilla）

**一句话概括**：发现现有大模型普遍训练不足，提出模型大小与训练数据量应按相同比例同步扩大，并据此训练出全面超越 Gopher 等模型的 Chinchilla。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| compute-optimal | adj. | 算力最优的（给定算力下训练效果最优） | "we find that for compute-optimal training" |
| investigate | v. | 研究、调查 | "We investigate the optimal model size and number of tokens" |
| undertrained | adj. | 训练不足的（数据量不够、潜力未发挥） | "current large language models are significantly undertrained" |
| consequence | n. | 结果、后果 | "a consequence of the recent focus on scaling language models" |
| doubling | n. | 翻倍 | "for every doubling of model size the number" |
| uniformly | adv. | 一致地、全面地 | "Chinchilla uniformly and significantly outperforms Gopher" |
| outperforms | v. | 性能优于、胜过 | "Chinchilla uniformly and significantly outperforms Gopher (280B)" |
| inference | n. | 推理（用训练好的模型生成输出） | "Chinchilla uses substantially less compute for fine-tuning and inference" |
| facilitating | v. | 促进、便于 | "for fine-tuning and inference, greatly facilitating downstream usage" |
| benchmark | n. | 基准（标准评测集） | "a state-of-the-art average accuracy of 67.5% on the MMLU benchmark" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-06 Training language models to follow instructions with human feedback

- [ ] 已读

**中文标题**：用人类反馈训练语言模型遵循指令（InstructGPT）

**一句话概括**：提出用人类反馈（监督微调＋强化学习）训练 InstructGPT，使 13 亿参数的小模型输出比 1750 亿参数的 GPT-3 更受人类偏好、更真实有用。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| inherently | adv. | 本质上、天生地 | "Making language models bigger does not inherently make them better" |
| intent | n. | 意图、目的（用户的真实需求） | "better at following a user's intent" |
| toxic | adj. | 有毒有害的（生成攻击性、有害内容） | "outputs that are untruthful, toxic, or simply not helpful to the user" |
| aligned | adj. | 对齐的（与用户意图一致） | "these models are not aligned with their users" |
| avenue | n. | 途径、方法 | "we show an avenue for aligning language models with user intent" |
| demonstrations | n. | 示范样本（人工标注的期望行为） | "we collect a dataset of labeler demonstrations of the desired model behavior" |
| supervised learning | phr. | 监督学习（用带标签数据训练） | "which we use to fine-tune GPT-3 using supervised learning" |
| reinforcement learning | phr. | 强化学习（通过奖励信号学习策略） | "using reinforcement learning from human feedback" |
| regressions | n. | 性能退化、回退 | "while having minimal performance regressions on public NLP datasets" |
| promising | adj. | 有前景的、有希望的 | "fine-tuning with human feedback is a promising direction for aligning" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-07 Constitutional AI: Harmlessness from AI Feedback

- [ ] 已读

**中文标题**：宪法式 AI：来自 AI 反馈的无害性训练

**一句话概括**：提出"宪法式 AI"：只凭一套规则原则，让 AI 自我批评、自我改进生成偏好数据并训练无害助手（RLAIF），大幅减少人工标注。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| harmless | adj. | 无害的（不产生有害输出） | "we experiment with methods for training a harmless AI assistant" |
| enlist | v. | 借助、争取（让 AI 帮忙监督其他 AI） | "we would like to enlist their help to supervise other AIs" |
| oversight | n. | 监督、监管 | "The only human oversight is provided through a list of rules" |
| principles | n. | 原则、准则 | "through a list of rules or principles" |
| self-critiques | n. | 自我批评（模型审视并指出自己输出的问题） | "we sample from an initial model, then generate self-critiques and revisions" |
| finetune | v. | 微调 | "and then finetune the original model on revised responses" |
| preference model | phr. | 偏好模型（学习判断两个输出哪个更好） | "train a preference model from this dataset of AI preferences" |
| reward signal | phr. | 奖励信号（强化学习中的反馈） | "using the preference model as the reward signal" |
| leverage | v. | 利用、借助 | "Both the SL and RL methods can leverage chain-of-thought style reasoning" |
| transparency | n. | 透明性（决策过程可被人理解） | "performance and transparency of AI decision making" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-08 RoFormer: Enhanced Transformer with Rotary Position Embedding

- [ ] 已读

**中文标题**：RoFormer：带旋转位置编码的增强 Transformer

**一句话概括**：提出旋转位置编码 RoPE，用旋转矩阵编码绝对位置并显式建模相对位置依赖，改进 Transformer 在长文本分类上的表现。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| rotary position embedding | phr. | 旋转位置编码（RoPE，用旋转矩阵编码位置） | "we propose a novel method named Rotary Position Embedding(RoPE)" |
| encoding | n. | 编码（把位置信息编入模型） | "Position encoding recently has shown effective in the transformer architecture" |
| supervision | n. | 监督信息（给模型提供训练信号的额外信息） | "It enables valuable supervision for dependency modeling between elements" |
| leverage | v. | 利用 | "to effectively leverage the positional information" |
| rotation matrix | phr. | 旋转矩阵 | "the proposed RoPE encodes the absolute position with a rotation matrix" |
| explicit | adj. | 显式的（明确表达出来的） | "incorporates the explicit relative position dependency in self-attention formulation" |
| flexibility | n. | 灵活性 | "including the flexibility of sequence length" |
| decaying | adj. | 衰减的（随距离增大而减弱） | "decaying inter-token dependency with increasing relative distances" |
| alternatives | n. | 替代方案、竞争者 | "that it consistently overcomes its alternatives" |
| theoretical analysis | phr. | 理论分析 | "we provide a theoretical analysis to explain some experimental results" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-09 LLaMA: Open and Efficient Foundation Language Models

- [ ] 已读

**中文标题**：LLaMA：开放且高效的基础语言模型

**一句话概括**：发布仅用公开数据训练的 LLaMA 系列基础模型（7B–65B），其中 13B 即超过 GPT-3，65B 与 Chinchilla-70B、PaLM-540B 相当。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| foundation | adj. | 基础的（作为底座的大规模预训练模型） | "a collection of foundation language models ranging from 7B to 65B parameters" |
| collection | n. | 系列、集合 | "We introduce LLaMA, a collection of foundation language models" |
| trillions | n. | 万亿（级别） | "We train our models on trillions of tokens" |
| tokens | n. | 词元（文本切分后的最小处理单元） | "We train our models on trillions of tokens" |
| state-of-the-art | adj. | 最先进的 | "it is possible to train state-of-the-art models using publicly available datasets" |
| exclusively | adv. | 完全地、仅仅 | "using publicly available datasets exclusively" |
| proprietary | adj. | 专有的（不公开的） | "without resorting to proprietary and inaccessible datasets" |
| outperforms | v. | 性能超过 | "LLaMA-13B outperforms GPT-3 (175B) on most benchmarks" |
| competitive | adj. | 有竞争力的、不相上下的 | "LLaMA-65B is competitive with the best models" |
| release | v. | 发布、开源 | "We release all our models to the research community" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-10 Llama 2: Open Foundation and Fine-Tuned Chat Models

- [ ] 已读

**中文标题**：Llama 2：开放基础模型与微调对话模型

**一句话概括**：发布 Llama 2 系列预训练与对话微调模型（7B–70B），在多数基准上超过开源聊天模型，并详述微调与安全改进方法。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| fine-tuned | adj. | 微调过的（在预训练基础上用任务数据训练） | "a collection of pretrained and fine-tuned large language models (LLMs)" |
| ranging in scale | phr. | 规模从……不等 | "ranging in scale from 7 billion to 70 billion parameters" |
| optimized | v. | 优化、专为……设计 | "called Llama 2-Chat, are optimized for dialogue use cases" |
| dialogue | n. | 对话 | "are optimized for dialogue use cases" |
| outperform | v. | 超越、胜过 | "Our models outperform open-source chat models on most benchmarks" |
| human evaluations | phr. | 人工评估（由人来评判模型质量） | "based on our human evaluations for helpfulness and safety" |
| helpfulness | n. | 有用性、助益程度 | "for helpfulness and safety, may be a suitable substitute" |
| substitute | n. | 替代品 | "may be a suitable substitute for closed-source models" |
| closed-source | adj. | 闭源的（不公开模型权重） | "a suitable substitute for closed-source models" |
| responsible | adj. | 负责任的（安全负责地开发） | "contribute to the responsible development of LLMs" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-11 LoRA: Low-Rank Adaptation of Large Language Models

- [ ] 已读

**中文标题**：LoRA：大语言模型的低秩适配

**一句话概括**：提出 LoRA 低秩适配：冻结预训练权重、只训练注入各层的低秩分解矩阵，以极小的可训练参数量达到与全量微调相当的性能。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| low-rank | adj. | 低秩的（用低维矩阵近似高维矩阵） | "We propose Low-Rank Adaptation, or LoRA, which freezes" |
| paradigm | n. | 范式（领域内标准做法） | "An important paradigm of natural language processing consists of large-scale pre-training" |
| adaptation | n. | 适配（把预训练模型调整到具体任务） | "pre-training on general domain data and adaptation to particular tasks or domains" |
| feasible | adj. | 可行的 | "full fine-tuning, which retrains all model parameters, becomes less feasible" |
| deploying | v. | 部署（把模型投入实际使用） | "deploying independent instances of fine-tuned models" |
| freezes | v. | 冻结（固定参数不再更新） | "which freezes the pre-trained model weights and injects trainable rank decomposition matrices" |
| decomposition | n. | 分解（矩阵分解为低秩因子） | "weights and injects trainable rank decomposition matrices" |
| throughput | n. | 吞吐量（单位时间处理的数据量） | "a higher training throughput, and, unlike adapters, no additional inference latency" |
| latency | n. | 延迟（响应所需时间） | "unlike adapters, no additional inference latency" |
| efficacy | n. | 有效性、效果 | "which sheds light on the efficacy of LoRA" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-12 QLoRA: Efficient Finetuning of Quantized LLMs

- [ ] 已读

**中文标题**：QLoRA：量化大语言模型的高效微调

**一句话概括**：提出 QLoRA，把 4 位量化与低秩适配结合，使 65B 模型可在单张 48GB GPU 上微调，且不损失 16 位微调的任务性能。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| quantized | adj. | 量化的（用低精度数值表示权重） | "backpropagates gradients through a frozen, 4-bit quantized pretrained language model" |
| finetuning | n. | 微调 | "an efficient finetuning approach that reduces memory usage enough to finetune" |
| preserving | v. | 保持、保留 | "while preserving full 16-bit finetuning task performance" |
| backpropagates | v. | 反向传播（计算梯度并更新参数） | "backpropagates gradients through a frozen, 4-bit quantized pretrained language model" |
| gradients | n. | 梯度（损失对参数的导数） | "QLoRA backpropagates gradients through a frozen" |
| innovations | n. | 创新（方法） | "QLoRA introduces a number of innovations to save memory without sacrificing performance" |
| sacrificing | v. | 牺牲 | "to save memory without sacrificing performance" |
| footprint | n. | 占用（内存占用大小） | "double quantization to reduce the average memory footprint by quantizing the quantization constants" |
| spikes | n. | 峰值（内存用量瞬间激增） | "paged optimziers to manage memory spikes" |
| trustworthy | adj. | 可信的、可靠的 | "current chatbot benchmarks are not trustworthy to accurately evaluate" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-13 FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

- [ ] 已读

**中文标题**：FlashAttention：IO 感知的快速且内存高效的精确注意力

**一句话概括**：提出 IO 感知的精确注意力算法 FlashAttention，通过分块（tiling）减少 GPU 显存读写，显著加速训练并支持更长序列。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| memory-hungry | adj. | 耗内存的（内存占用大） | "Transformers are slow and memory-hungry on long sequences" |
| exact | adj. | 精确的（不做近似计算） | "an IO-aware exact attention algorithm that uses tiling" |
| quadratic | adj. | 二次方的（复杂度随序列长度平方增长） | "the time and memory complexity of self-attention are quadratic in sequence length" |
| trading off | phr. | 以……为代价换取 | "trading off model quality to reduce the compute complexity" |
| wall-clock | adj. | 实际耗时的（按真实时钟计算的运行时间） | "but often do not achieve wall-clock speedup" |
| accounting for | phr. | 考虑到、计入 | "accounting for reads and writes between levels of GPU memory" |
| tiling | n. | 分块（把数据切成小块逐个处理） | "an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes" |
| optimal | adj. | 最优的 | "and is optimal for a range of SRAM sizes" |
| baselines | n. | 基线（用于对比的已有方法） | "trains Transformers faster than existing baselines" |
| perplexity | n. | 困惑度（语言模型指标，越低越好） | "yielding higher quality models (0.7 better perplexity on GPT-2" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-14 Efficient Memory Management for Large Language Model Serving with PagedAttention

- [ ] 已读

**中文标题**：基于 PagedAttention 的大语言模型服务的高效内存管理

**一句话概括**：借鉴操作系统虚拟内存分页思想提出 PagedAttention，并构建 vLLM 服务系统，几乎消除 KV 缓存内存浪费，吞吐量提升 2–4 倍。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| serving | n. | 服务（部署模型对外提供推理服务） | "High throughput serving of large language models (LLMs) requires batching sufficiently many requests" |
| throughput | n. | 吞吐量（单位时间处理的请求数） | "High throughput serving of large language models (LLMs) requires batching" |
| batching | v. | 批处理（把多个请求放在一起处理） | "requires batching sufficiently many requests at a time" |
| key-value cache | phr. | 键值缓存（KV 缓存，存储注意力计算所需的键值） | "the key-value cache (KV cache) memory for each request is huge" |
| dynamically | adv. | 动态地（随情况变化） | "is huge and grows and shrinks dynamically" |
| fragmentation | n. | 碎片化（内存被拆散浪费） | "this memory can be significantly wasted by fragmentation and redundant duplication" |
| redundant | adj. | 冗余的（重复多余的） | "wasted by fragmentation and redundant duplication" |
| paging | n. | 分页（操作系统管理内存的技术） | "the classical virtual memory and paging techniques in operating systems" |
| flexible | adj. | 灵活的 | "(2) flexible sharing of KV cache within and across requests" |
| pronounced | adj. | 明显的、显著的 | "The improvement is more pronounced with longer sequences" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-15 Mistral 7B

- [ ] 已读

**中文标题**：Mistral 7B

**一句话概括**：发布 Mistral 7B，用分组查询注意力（GQA）与滑动窗口注意力（SWA）实现优于 Llama 2 13B 的性能和更快的推理，并以 Apache 2.0 协议开源。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| engineered | v. | 精心设计的 | "a 7-billion-parameter language model engineered for superior performance" |
| superior | adj. | 卓越的、更好的 | "engineered for superior performance and efficiency" |
| outperforms | v. | 超过、胜过 | "Mistral 7B outperforms Llama 2 13B across all evaluated benchmarks" |
| reasoning | n. | 推理（逻辑思考能力） | "and Llama 1 34B in reasoning, mathematics, and code generation" |
| leverages | v. | 利用 | "Our model leverages grouped-query attention (GQA) for faster inference" |
| grouped-query attention | phr. | 分组查询注意力（GQA，多个查询头共享键值头） | "leverages grouped-query attention (GQA) for faster inference" |
| coupled with | phr. | 与……结合 | "coupled with sliding window attention (SWA)" |
| arbitrary | adj. | 任意的 | "to effectively handle sequences of arbitrary length" |
| surpasses | v. | 超过、胜过 | "that surpasses the Llama 2 13B -- Chat model" |
| license | n. | 许可证（开源协议） | "Our models are released under the Apache 2.0 license" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-16 Mixtral of Experts

- [ ] 已读

**中文标题**：专家混合模型 Mixtral

**一句话概括**：发布 Mixtral 8x7B 稀疏专家混合模型：每层 8 个前馈专家、每个词元只激活 2 个，性能全面匹敌或超越 Llama 2 70B 与 GPT-3.5。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| sparse | adj. | 稀疏的（每次只激活少量参数） | "a Sparse Mixture of Experts (SMoE) language model" |
| mixture of experts | phr. | 专家混合（MoE，多个子网络按输入分工） | "We introduce Mixtral 8x7B, a Sparse Mixture of Experts (SMoE) language model" |
| architecture | n. | 架构（模型整体结构） | "the same architecture as Mistral 7B" |
| feedforward | adj. | 前馈的（全连接网络层） | "each layer is composed of 8 feedforward blocks (i.e. experts)" |
| router | adj. | 路由的（负责选择专家的网络） | "a router network selects two experts to process the current state" |
| combine | v. | 合并、结合 | "to process the current state and combine their outputs" |
| timestep | n. | 时间步（生成序列中的每一步） | "the selected experts can be different at each timestep" |
| active parameters | phr. | 激活参数（实际参与计算的参数） | "but only uses 13B active parameters during inference" |
| vastly | adv. | 极大地 | "Mixtral vastly outperforms Llama 2 70B on mathematics" |
| surpasses | v. | 超过 | "that surpasses GPT-3.5 Turbo, Claude-2.1, Gemini Pro" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-17 GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding

- [ ] 已读

**中文标题**：GShard：用条件计算与自动分片扩展巨型模型

**一句话概括**：提出 GShard，用轻量注解 API 与 XLA 编译器扩展实现自动分片，把多语言机器翻译的 MoE Transformer 扩展到 6000 亿参数。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| scaling | n. | 扩展（把模型做得更大） | "Neural network scaling has been critical for improving the model quality" |
| sharding | n. | 分片（把模型参数切分到多台设备） | "beyond 600 billion parameters using automatic sharding" |
| critical | adj. | 至关重要的 | "Neural network scaling has been critical for improving the model quality" |
| vast | adj. | 海量的 | "with vast amounts of training data and compute" |
| sure-fire | adj. | 稳操胜券的、必定有效的 | "this trend of scaling is affirmed to be a sure-fire approach" |
| lightweight | adj. | 轻量的（简单、负担小） | "a module composed of a set of lightweight annotation APIs" |
| elegant | adj. | 优雅的（简洁巧妙） | "It provides an elegant way to express a wide range of parallel computation patterns" |
| multilingual | adj. | 多语言的 | "scale up multilingual neural machine translation Transformer model" |
| accelerators | n. | 加速器（专用计算硬件，如 TPU） | "efficiently be trained on 2048 TPU v3 accelerators in 4 days" |
| prior art | phr. | 现有技术（此前最好的方法） | "compared to the prior art" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-18 Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity

- [ ] 已读

**中文标题**：Switch Transformer：用简单高效的稀疏性扩展到万亿参数模型

**一句话概括**：简化 MoE 路由算法、解决训练不稳定问题，首次实现万亿参数稀疏模型用低精度（bfloat16）训练，并显著提升预训练速度。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| sparse | adj. | 稀疏的（只激活部分参数） | "we show large sparse models may be trained" |
| defies | v. | 打破、违背（常规做法） | "Mixture of Experts (MoE) defies this and instead selects different parameters" |
| sparsely-activated | adj. | 稀疏激活的（每次只运行部分参数） | "The result is a sparsely-activated model -- with outrageous numbers of parameters" |
| outrageous | adj. | 惊人的、夸张的 | "with outrageous numbers of parameters -- but a constant computational cost" |
| hindered | v. | 阻碍 | "widespread adoption has been hindered by complexity" |
| instability | n. | 不稳定性（训练过程波动） | "communication costs and training instability -- we address these" |
| routing | adj. | 路由的（决定把输入分给哪个专家） | "We simplify the MoE routing algorithm and design intuitive improved models" |
| intuitive | adj. | 直观的、易理解的 | "design intuitive improved models with reduced communication and computational costs" |
| wrangle | v. | 驯服、解决（棘手问题） | "Our proposed training techniques help wrangle the instabilities" |
| precision | n. | 精度（数值表示精度，如 bfloat16） | "with lower precision (bfloat16) formats" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-19 Mamba: Linear-Time Sequence Modeling with Selective State Spaces

- [ ] 已读

**中文标题**：Mamba：基于选择性状态空间的线性时间序列建模

**一句话概括**：提出 Mamba 选择性状态空间模型，让 SSM 参数随输入内容变化，以线性时间复杂度和快速推理超越同规模 Transformer 的语言建模性能。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| linear | adj. | 线性的（计算量随序列长度线性增长） | "linear scaling in sequence length" |
| selective | adj. | 选择性的（按内容决定保留或遗忘信息） | "We integrate these selective SSMs into a simplified end-to-end neural network architecture" |
| state space models | phr. | 状态空间模型（SSM，一类序列建模方法） | "and structured state space models (SSMs) have been developed" |
| universally | adv. | 普遍地 | "are almost universally based on the Transformer architecture" |
| subquadratic-time | adj. | 亚二次方时间的（比二次方更省计算） | "Many subquadratic-time architectures such as linear attention, gated convolution" |
| gated convolution | phr. | 门控卷积（带门控机制的卷积） | "such as linear attention, gated convolution and recurrent models" |
| recurrent | adj. | 循环的（RNN 类逐时间步结构） | "gated convolution and recurrent models, and structured state space models" |
| modalities | n. | 模态（数据类型，如语言、音频） | "as well as attention on important modalities such as language" |
| propagate | v. | 传播（信息沿序列传递） | "to selectively propagate or forget information along the sequence length dimension" |
| hardware-aware | adj. | 硬件感知的（针对硬件特性设计算法） | "we design a hardware-aware parallel algorithm in recurrent mode" |
| backbone | n. | 主干网络（通用的序列模型底座） | "As a general sequence model backbone, Mamba achieves state-of-the-art performance" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-20 GPT-4 Technical Report

- [ ] 已读

**中文标题**：GPT-4 技术报告

**一句话概括**：报告 GPT-4 的开发：一个可接受图文输入并输出文本的多模态 Transformer 模型，在多项专业与学术基准上达到接近人类水平。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| multimodal | adj. | 多模态的（能同时处理图像和文本） | "a large-scale, multimodal model which can accept image and text inputs" |
| exhibits | v. | 展现出、表现出 | "GPT-4 exhibits human-level performance on various professional and academic benchmarks" |
| simulated | adj. | 模拟的 | "including passing a simulated bar exam with a score around the top 10%" |
| bar exam | phr. | 律师资格考试 | "passing a simulated bar exam with a score" |
| pre-trained | v. | 预训练 | "a Transformer-based model pre-trained to predict the next token in a document" |
| alignment | n. | 对齐（让模型行为符合期望） | "The post-training alignment process results in improved performance" |
| factuality | n. | 事实准确性（输出内容符合事实） | "improved performance on measures of factuality and adherence to desired behavior" |
| adherence | n. | 遵从、遵守 | "on measures of factuality and adherence to desired behavior" |
| infrastructure | n. | 基础设施（训练所需的工程体系） | "developing infrastructure and optimization methods that behave predictably" |
| predictably | adv. | 可预测地 | "optimization methods that behave predictably across a wide range of scales" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-21 Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

- [ ] 已读

**中文标题**：思维链提示激发大语言模型的推理能力

**一句话概括**：提出思维链提示：在提示中给出少量中间推理步骤示例，即可显著提升大模型在算术、常识与符号推理任务上的表现。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| chain of thought | n. | 思维链（一系列中间推理步骤） | "via a simple method called chain of thought prompting" |
| intermediate | adj. | 中间的 | "a series of intermediate reasoning steps" |
| significantly | adv. | 显著地 | "significantly improves the ability of large language models to perform complex reasoning" |
| emerge | v. | 涌现（自然出现、无需专门训练） | "such reasoning abilities emerge naturally in sufficiently large language models" |
| exemplars | n. | 示例（示范样本） | "chain of thought demonstrations are provided as exemplars in prompting" |
| arithmetic | n. | 算术 | "a range of arithmetic, commonsense, and symbolic reasoning tasks" |
| commonsense | n. | 常识 | "arithmetic, commonsense, and symbolic reasoning tasks" |
| symbolic | adj. | 符号的（符号逻辑类推理） | "improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks" |
| striking | adj. | 惊人的 | "The empirical gains can be striking" |
| verifier | n. | 验证器（检查答案正确性的模型） | "surpassing even finetuned GPT-3 with a verifier" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-22 ReAct: Synergizing Reasoning and Acting in Language Models

- [ ] 已读

**中文标题**：ReAct：在大语言模型中协同推理与行动

**一句话概括**：提出 ReAct，让大模型交替生成推理轨迹与动作，并与外部环境（如 Wikipedia API）交互，缓解幻觉并提升决策任务的性能与可解释性。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| synergy | n. | 协同效应（两者结合产生更大效果） | "allowing for greater synergy between the two" |
| interactive | adj. | 交互式的（与环境互动） | "language understanding and interactive decision making" |
| interleaved | adj. | 交错的（推理与行动交替进行） | "generate both reasoning traces and task-specific actions in an interleaved manner" |
| traces | n. | 轨迹（推理过程的记录） | "generate both reasoning traces and task-specific actions" |
| induce | v. | 归纳、引导 | "reasoning traces help the model induce, track, and update action plans" |
| interface | v. | 对接、交互 | "while actions allow it to interface with external sources" |
| diverse | adj. | 多样的 | "We apply our approach, named ReAct, to a diverse set of language" |
| interpretability | n. | 可解释性（过程可被人理解） | "as well as improved human interpretability and trustworthiness over methods" |
| hallucination | n. | 幻觉（模型编造不实内容） | "ReAct overcomes issues of hallucination and error propagation" |
| trajectories | n. | 轨迹（完成任务的过程记录） | "generates human-like task-solving trajectories that are more interpretable" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-23 Toolformer: Language Models Can Teach Themselves to Use Tools

- [ ] 已读

**中文标题**：Toolformer：语言模型可以自学使用工具

**一句话概括**：提出 Toolformer，让语言模型以自监督方式学会在适当时机调用计算器、搜索引擎等外部工具，显著提升零样本性能。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| remarkable | adj. | 非凡的、惊人的 | "LMs exhibit remarkable abilities to solve new tasks from just a few examples" |
| paradoxically | adv. | 矛盾的是（看似不合理却如此） | "They also, paradoxically, struggle with basic functionality" |
| struggle | v. | 吃力、表现不佳 | "struggle with basic functionality, such as arithmetic or factual lookup" |
| factual lookup | phr. | 事实查询（查证事实信息） | "such as arithmetic or factual lookup" |
| excel | v. | 擅长、表现出色 | "where much simpler and smaller models excel" |
| external tools | phr. | 外部工具（模型之外的 API 等） | "LMs can teach themselves to use external tools via simple APIs" |
| incorporate | v. | 整合、纳入 | "and how to best incorporate the results into future token prediction" |
| self-supervised | adj. | 自监督的（无需人工标注） | "This is done in a self-supervised way" |
| a handful of | phr. | 少量的 | "requiring nothing more than a handful of demonstrations for each API" |
| sacrificing | v. | 牺牲 | "without sacrificing its core language modeling abilities" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-24 Self-Instruct: Aligning Language Models with Self-Generated Instructions

- [ ] 已读

**中文标题**：Self-Instruct：用自生成的指令对齐语言模型

**一句话概括**：提出 Self-Instruct，让模型用自己的生成结果"自举"出指令数据并微调，减少对人工指令数据的依赖，显著提升指令跟随能力。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| aligning | v. | 对齐（让模型行为符合指令要求） | "method for aligning pre-trained language models with instructions" |
| bootstrapping off | phr. | 以……为基础自我提升 | "by bootstrapping off their own generations" |
| generalize | v. | 泛化（迁移到新任务） | "have demonstrated a remarkable ability to generalize zero-shot to new tasks" |
| zero-shot | adj. | 零样本的（不提供示例直接完成任务） | "generalize zero-shot to new tasks" |
| diversity | n. | 多样性 | "often limited in quantity, diversity, and creativity" |
| hindering | v. | 阻碍 | "therefore hindering the generality of the tuned model" |
| pipeline | n. | 流程（流水线式的处理步骤） | "Our pipeline generates instructions, input, and output samples from a language model" |
| filters | v. | 过滤（剔除不合格样本） | "then filters invalid or similar ones before using them to finetune" |
| curate | v. | 精心挑选、整理 | "we curate a set of expert-written instructions for novel tasks" |
| synthetic | adj. | 合成的（机器生成的数据） | "we release our large synthetic dataset to facilitate future studies" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-25 LIMA: Less Is More for Alignment

- [ ] 已读

**中文标题**：LIMA：对齐中少即是多

**一句话概括**：只用 1000 条精心筛选的指令数据微调出 LIMA，证明大模型的知识主要来自预训练，少量高质量指令数据即可完成对齐。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| align | v. | 对齐（与目标任务、用户偏好一致） | "to better align to end tasks and user preferences" |
| unsupervised | adj. | 无监督的（无需人工标签） | "unsupervised pretraining from raw text, to learn general-purpose representations" |
| instruction tuning | phr. | 指令微调（用指令数据训练模型遵循指令） | "large scale instruction tuning and reinforcement learning" |
| measure | v. | 衡量 | "We measure the relative importance of these two stages" |
| curated | adj. | 精心筛选的 | "only 1,000 carefully curated prompts and responses" |
| prompts | n. | 提示（给模型的输入指令） | "1,000 carefully curated prompts and responses" |
| preference modeling | phr. | 偏好建模（学习用户的偏好） | "without any reinforcement learning or human preference modeling" |
| remarkably | adv. | 惊人地 | "LIMA demonstrates remarkably strong performance" |
| generalize | v. | 泛化 | "the model tends to generalize well to unseen tasks" |
| unseen | adj. | 未见过的（训练数据中没有的） | "generalize well to unseen tasks that did not appear in the training data" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-26 Direct Preference Optimization: Your Language Model is Secretly a Reward Model

- [ ] 已读

**中文标题**：直接偏好优化：你的语言模型其实是一个奖励模型（DPO）

**一句话概括**：提出直接偏好优化 DPO，把 RLHF 中的奖励模型参数化改写为闭式解，仅用简单的分类损失即可完成对齐，更简单、更稳定。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| steerability | n. | 可控性（能引导模型行为） | "Existing methods for gaining such steerability collect human labels" |
| precise control | phr. | 精确控制 | "achieving precise control of their behavior is difficult" |
| relative quality | phr. | 相对质量（样本之间的好坏比较） | "human labels of the relative quality of model generations" |
| unstable | adj. | 不稳定的 | "RLHF is a complex and often unstable procedure" |
| parameterization | n. | 参数化（对模型的数学表示方式） | "we introduce a new parameterization of the reward model in RLHF" |
| closed form | phr. | 闭式解（可直接计算的解析形式） | "enables extraction of the corresponding optimal policy in closed form" |
| classification loss | phr. | 分类损失（分类任务的损失函数） | "with only a simple classification loss" |
| performant | adj. | 高性能的、效果好的 | "is stable, performant, and computationally lightweight" |
| eliminating | v. | 消除 | "eliminating the need for sampling from the LM during fine-tuning" |
| sentiment | n. | 情感（生成内容的情感倾向） | "in ability to control sentiment of generations" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-27 Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

- [ ] 已读

**中文标题**：面向知识密集型 NLP 任务的检索增强生成（RAG）

**一句话概括**：提出 RAG 检索增强生成，把预训练参数记忆与维基百科稠密向量索引结合，在知识密集型任务上刷新多项 SOTA。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| retrieval-augmented | adj. | 检索增强的（结合检索与生成） | "We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG)" |
| knowledge-intensive | adj. | 知识密集型的（需要大量外部知识） | "on a wide range of knowledge-intensive NLP tasks" |
| store | v. | 存储 | "have been shown to store factual knowledge in their parameters" |
| precisely | adv. | 精确地 | "their ability to access and precisely manipulate knowledge is still limited" |
| provenance | n. | 出处、来源（决策可追溯） | "providing provenance for their decisions" |
| differentiable | adj. | 可微的（可求导、支持梯度传播） | "Pre-trained models with a differentiable access mechanism to explicit non-parametric memory" |
| non-parametric | adj. | 非参数化的（参数之外的外部记忆） | "explicit non-parametric memory can overcome this issue" |
| recipe | n. | 方法、方案 | "We explore a general-purpose fine-tuning recipe for retrieval-augmented generation" |
| dense vector index | phr. | 稠密向量索引（用于向量检索的结构） | "the non-parametric memory is a dense vector index of Wikipedia" |
| retriever | n. | 检索器（负责查找相关文档的模型） | "accessed with a pre-trained neural retriever" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-28 Fast Inference from Transformers via Speculative Decoding

- [ ] 已读

**中文标题**：通过推测解码实现 Transformer 的快速推理

**一句话概括**：提出推测解码：用高效小模型并行推测多个词元、再由大模型验证，不改变输出分布即可将解码加速 2–3 倍。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| speculative decoding | phr. | 推测解码（先猜测后验证的解码方法） | "we introduce speculative decoding - an algorithm to sample" |
| serial | adj. | 串行的（一步步顺序执行） | "decoding K tokens takes K serial runs of the model" |
| sampling | n. | 采样（按概率分布抽取词元） | "an algorithm to sample from autoregressive models faster without any changes" |
| at the heart of | phr. | 核心在于 | "At the heart of our approach lie the observations" |
| subtasks | n. | 子任务（大任务中的较易小任务） | "hard language-modeling tasks often include easier subtasks" |
| approximated | v. | 近似（粗略模拟） | "that can be approximated well by more efficient models" |
| speculative execution | phr. | 推测执行（先假设后验证的并行执行） | "using speculative execution and a novel sampling method" |
| concurrently | adv. | 并发地、同时 | "potentially generating several tokens concurrently" |
| distribution | n. | 分布（输出的概率分布） | "and without changing the distribution" |
| off-the-shelf | adj. | 现成的（已有模型、无需改动） | "accelerate existing off-the-shelf models without retraining" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-29 Emergent Abilities of Large Language Models

- [ ] 已读

**中文标题**：大语言模型的涌现能力

**一句话概括**：系统讨论大模型的涌现能力——只在较大模型中出现、无法由小模型性能外推预测的能力，说明继续扩展可能带来新能力。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| emergent | adj. | 涌现的（小模型没有、大模型突然出现的） | "an unpredictable phenomenon that we refer to as emergent abilities" |
| predictably | adv. | 可预测地 | "has been shown to predictably improve performance and sample efficiency" |
| sample efficiency | phr. | 样本效率（数据利用效率） | "predictably improve performance and sample efficiency on a wide range" |
| unpredictable | adj. | 不可预测的 | "discusses an unpredictable phenomenon that we refer to as emergent abilities" |
| phenomenon | n. | 现象 | "an unpredictable phenomenon that we refer to" |
| present | adj. | 存在的 | "not present in smaller models but is present in larger models" |
| extrapolating | v. | 外推（由已知趋势推测未知） | "cannot be predicted simply by extrapolating the performance of smaller models" |
| emergence | n. | 涌现（现象本身） | "The existence of such emergence implies that additional scaling" |
| expand | v. | 扩展 | "could further expand the range of capabilities of language models" |
| capabilities | n. | 能力 | "expand the range of capabilities of language models" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-30 Let's Verify Step by Step

- [ ] 已读

**中文标题**：让我们一步步验证

**一句话概括**：对比结果监督与过程监督，证明对每一步推理逐步验证的过程监督显著更优，所训练模型在 MATH 数据集上解出 78% 的问题。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| multi-step reasoning | phr. | 多步推理（需要多步推导的问题） | "their ability to perform complex multi-step reasoning" |
| logical mistakes | phr. | 逻辑错误 | "even state-of-the-art models still regularly produce logical mistakes" |
| reliable | adj. | 可靠的 | "To train more reliable models" |
| outcome supervision | phr. | 结果监督（只对最终结果给反馈） | "to outcome supervision, which provides feedback for a final result" |
| process supervision | phr. | 过程监督（对每一步推理给反馈） | "or process supervision, which provides feedback for each intermediate reasoning step" |
| intermediate | adj. | 中间的 | "provides feedback for each intermediate reasoning step" |
| conduct | v. | 进行、开展 | "We conduct our own investigation" |
| representative subset | phr. | 代表性子集 | "from a representative subset of the MATH test set" |
| active learning | phr. | 主动学习（挑选最有价值的样本标注） | "active learning significantly improves the efficacy of process supervision" |
| efficacy | n. | 效果、有效性 | "significantly improves the efficacy of process supervision" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-31 DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

- [ ] 已读

**中文标题**：DeepSeek-R1：通过强化学习激励大语言模型的推理能力

**一句话概括**：提出 DeepSeek-R1，用纯强化学习激励推理能力，无需人工推理轨迹，即涌现出自我反思、验证、动态调整策略等高级推理模式。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| incentivized | v. | 激励（通过奖励引导能力出现） | "can be incentivized through pure reinforcement learning (RL)" |
| formidable | adj. | 艰巨的、难对付的 | "a long-standing and formidable challenge in artificial intelligence" |
| breakthroughs | n. | 突破 | "Recent breakthroughs, exemplified by large language models" |
| contingent upon | phr. | 依赖于 | "this success is heavily contingent upon extensive human-annotated demonstrations" |
| extensive | adj. | 大量的、广泛的 | "heavily contingent upon extensive human-annotated demonstrations" |
| obviating | v. | 免除、排除（不再需要） | "obviating the need for human-labeled reasoning trajectories" |
| trajectories | n. | 轨迹（推理过程记录） | "the need for human-labeled reasoning trajectories" |
| self-reflection | n. | 自我反思（检查自身推理是否正确） | "such as self-reflection, verification, and dynamic strategy adaptation" |
| verifiable | adj. | 可验证的（答案可客观检验） | "achieves superior performance on verifiable tasks such as mathematics" |
| harnessed | v. | 利用、驾驭 | "can be systematically harnessed to guide and enhance the reasoning capabilities" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-32 GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints

- [ ] 已读

**中文标题**：GQA：从多头检查点训练广义多查询 Transformer 模型

**一句话概括**：提出 GQA 分组查询注意力，并给出把已有多头检查点"升级训练"为多查询注意力模型的方法，以接近多头的质量、接近 MQA 的速度。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| generalization | n. | 推广、泛化（此处指 MQA 的一般化形式） | "introduce grouped-query attention (GQA), a generalization of multi-query attention" |
| checkpoints | n. | 检查点（训练好的模型存档） | "existing multi-head language model checkpoints into models with MQA" |
| drastically | adv. | 大幅度地 | "which only uses a single key-value head, drastically speeds up decoder inference" |
| decoder | n. | 解码器（负责生成输出的部分） | "drastically speeds up decoder inference" |
| degradation | n. | 退化（质量下降） | "MQA can lead to quality degradation" |
| desirable | adj. | 可取的、理想的 | "it may not be desirable to train a separate model" |
| recipe | n. | 方法、配方 | "we propose a recipe for uptraining existing multi-head language model checkpoints" |
| uptraining | v. | 升级训练（把已有模型转换成新结构继续训练） | "a recipe for uptraining existing multi-head language model checkpoints" |
| intermediate | adj. | 中间的（介于两者之间） | "which uses an intermediate (more than one, less than number of query heads)" |
| comparable | adj. | 相当的、可比的 | "achieves quality close to multi-head attention with comparable speed to MQA" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-33 Fast Transformer Decoding: One Write-Head is All You Need

- [ ] 已读

**中文标题**：快速 Transformer 解码：一个写入头就够了（多查询注意力 MQA）

**一句话概括**：提出多查询注意力 MQA，让所有注意力头共享同一组键值张量，大幅降低内存带宽需求，加速增量式解码。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| decoding | n. | 解码（逐词生成输出） | "the memory bandwidth requirements of incremental decoding" |
| powerful alternative | phr. | 强大的替代方案 | "are a powerful alternative to RNNs for moving information" |
| parallelizability | n. | 可并行性（能同时计算） | "due to parallelizability across the length of the sequence" |
| incremental inference | phr. | 增量式推理（逐步生成、逐步计算） | "incremental inference (where such paralleization is impossible) is often slow" |
| memory-bandwidth | n. | 内存带宽（单位时间读写内存的量） | "due to the memory-bandwidth cost of repeatedly loading the large" |
| tensors | n. | 张量（多维数组，此处指键值矩阵） | "the large "keys" and "values" tensors" |
| shared across | phr. | 在所有……之间共享 | "the keys and values are shared across all of the different attention "heads"" |
| variant | n. | 变体（某方法的修改版本） | "We propose a variant called multi-query attention" |
| verify | v. | 验证 | "We verify experimentally that the resulting models" |
| incur | v. | 招致、引起 | "and incur only minor quality degradation from the baseline" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-34 DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

- [ ] 已读

**中文标题**：DeepSeekMath：突破开放语言模型的数学推理极限

**一句话概括**：发布 DeepSeekMath 7B，用精心筛选的数学语料继续预训练并提出 GRPO 强化学习方法，在竞赛级 MATH 基准上达到 51.7%。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| poses | v. | 构成（构成挑战） | "Mathematical reasoning poses a significant challenge for language models" |
| structured | adj. | 结构化的（有严密逻辑结构） | "due to its complex and structured nature" |
| sourced from | phr. | 来源于 | "with 120B math-related tokens sourced from Common Crawl" |
| impressive | adj. | 令人印象深刻的、亮眼的 | "has achieved an impressive score of 51.7%" |
| competition-level | adj. | 竞赛级别的（数学竞赛难度） | "on the competition-level MATH benchmark" |
| relying on | phr. | 依赖 | "without relying on external toolkits and voting techniques" |
| attributed to | phr. | 归因于 | "is attributed to two key factors" |
| harness | v. | 利用、挖掘 | "we harness the significant potential of publicly available web data" |
| meticulously | adv. | 一丝不苟地、精心地 | "through a meticulously engineered data selection pipeline" |
| concurrently | adv. | 同时 | "while concurrently optimizing the memory usage of PPO" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-35 DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model

- [ ] 已读

**中文标题**：DeepSeek-V2：强大、经济且高效的专家混合语言模型

**一句话概括**：发布 DeepSeek-V2，用 MLA 把 KV 缓存压缩进潜在向量、用 DeepSeekMoE 稀疏计算，训练更省、推理更快，性能超越 DeepSeek 67B。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| economical | adj. | 经济的（省成本的） | "a strong Mixture-of-Experts (MoE) language model characterized by economical training" |
| characterized by | phr. | 以……为特征 | "characterized by economical training and efficient inference" |
| activated | adj. | 激活的（实际参与计算的参数） | "of which 21B are activated for each token" |
| innovative | adj. | 创新的 | "DeepSeek-V2 adopts innovative architectures including Multi-head Latent Attention" |
| latent | adj. | 隐式的（压缩后的潜在表示） | "including Multi-head Latent Attention (MLA) and DeepSeekMoE" |
| compressing | v. | 压缩 | "through significantly compressing the Key-Value (KV) cache into a latent vector" |
| sparse | adj. | 稀疏的（只激活少量参数） | "enables training strong models at an economical cost through sparse computation" |
| boosts | v. | 提升、大幅提高 | "and boosts the maximum generation throughput to 5.76 times" |
| corpus | n. | 语料库 | "a high-quality and multi-source corpus consisting of 8.1T tokens" |
| top-tier | adj. | 顶级的 | "still achieve top-tier performance among open-source models" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-36 DeepSeek-V3 Technical Report

- [ ] 已读

**中文标题**：DeepSeek-V3 技术报告

**一句话概括**：报告 671B 参数的 MoE 模型 DeepSeek-V3：采用无辅助损失负载均衡与多词元预测目标，性能比肩顶级闭源模型，且训练稳定、成本低。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| cost-effective | adj. | 成本高效的 | "To achieve efficient inference and cost-effective training" |
| thoroughly | adv. | 彻底地 | "which were thoroughly validated in DeepSeek-V2" |
| pioneers | v. | 开创、率先采用 | "DeepSeek-V3 pioneers an auxiliary-loss-free strategy for load balancing" |
| auxiliary-loss-free | adj. | 无辅助损失的（不额外添加损失项） | "pioneers an auxiliary-loss-free strategy for load balancing" |
| load balancing | phr. | 负载均衡（让各专家负载均匀） | "an auxiliary-loss-free strategy for load balancing" |
| multi-token prediction | phr. | 多词元预测（一次预测多个词元） | "sets a multi-token prediction training objective for stronger performance" |
| harness | v. | 发挥、充分利用 | "to fully harness its capabilities" |
| comprehensive | adj. | 全面的 | "Comprehensive evaluations reveal that DeepSeek-V3 outperforms" |
| comparable to | phr. | 与……相当 | "achieves performance comparable to leading closed-source models" |
| irrecoverable | adj. | 不可恢复的 | "we did not experience any irrecoverable loss spikes" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-37 Lost in the Middle: How Language Models Use Long Contexts

- [ ] 已读

**中文标题**：迷失在中间：语言模型如何使用长上下文

**一句话概括**：研究发现语言模型对长上下文中部信息的利用明显更差，揭示"迷失在中间"现象，并提供新的长上下文评测协议。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| relatively | adv. | 相对地 | "relatively little is known about how well they use longer context" |
| identifying | v. | 识别 | "two tasks that require identifying relevant information in their input contexts" |
| relevant | adj. | 相关的（与任务有关的） | "require identifying relevant information in their input contexts" |
| key-value retrieval | phr. | 键值检索（从键值对中查找信息） | "multi-document question answering and key-value retrieval" |
| degrade | v. | 下降、退化 | "performance can degrade significantly when changing the position of relevant information" |
| robustly | adv. | 稳健地 | "current language models do not robustly make use of information" |
| in particular | phr. | 特别是 | "In particular, we observe that performance is often highest" |
| occurs | v. | 出现、发生 | "relevant information occurs at the beginning or end" |
| protocols | n. | 方案、标准（此处指评测协议） | "provides new evaluation protocols for future long-context language models" |
| explicitly | adv. | 明确地 | "even for explicitly long-context models" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 01-38 YaRN: Efficient Context Window Extension of Large Language Models

- [ ] 已读

**中文标题**：YaRN：大语言模型上下文窗口的高效扩展

**一句话概括**：提出 YaRN，一种算力高效的上下文窗口扩展方法，用远少于以往的数据量和训练步数，让 LLaMA 有效外推到超长上下文。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| context window | phr. | 上下文窗口（模型能处理的输入长度） | "a compute-efficient method to extend the context window of such models" |
| extension | n. | 扩展（延长上下文窗口） | "surpassing previous the state-of-the-art at context window extension" |
| effectively | adv. | 有效地 | "have been shown to effectively encode positional information" |
| generalize | v. | 泛化（推广到训练长度之外） | "models fail to generalize past the sequence length" |
| compute-efficient | adj. | 算力高效的（省计算资源） | "a compute-efficient method to extend the context window of such models" |
| utilize | v. | 利用 | "LLaMA models can effectively utilize and extrapolate to context lengths" |
| extrapolate | v. | 外推（超出训练长度继续使用） | "can effectively utilize and extrapolate to context lengths much longer" |
| surpassing | v. | 超越 | "while also surpassing previous the state-of-the-art at context window extension" |
| capability | n. | 能力 | "YaRN exhibits the capability to extrapolate beyond the limited context" |
| exhibits | v. | 展现出 | "YaRN exhibits the capability to extrapolate" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

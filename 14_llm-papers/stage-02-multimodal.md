---
type: paper-vocabulary
stage: 2
title: "阶段 2 · 多模态 Multimodal 论文词汇"
tags: [topic/paper, skill/reading, status/learning]
created: 2026-10-24
---

# 阶段 2 · 多模态 Multimodal 论文词汇

> 57 篇 · 691 个词条。读前扫词 2 分钟；读后遮住中文，用 abstract 片段自测，再用 5 个词复述 60 秒。
> 返回 [[14_llm-papers/_index|LLM 论文阅读]]；配套 [[14_llm-papers/reading-workflow|阅读与词汇流程]]。

## 02-00 An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale

- [ ] 已读

**中文标题**：一张图像等于 16×16 个词：用于大规模图像识别的 Transformer

**一句话概括**：提出 Vision Transformer（ViT），把图像切成 patch 序列直接用纯 Transformer 处理而无需卷积网络，大规模预训练后迁移到中小规模识别基准，效果出色且训练计算量显著更低。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| de-facto | adj. | 事实上的、实际通用的（指 Transformer 已成为 NLP 领域默认标准） | "has become the de-facto standard for natural language" |
| in conjunction with | phr. | 与……结合（指注意力与卷积网络搭配使用） | "applied in conjunction with convolutional networks" |
| reliance | n. | 依赖（本文指对 CNN 的依赖） | "this reliance on CNNs is not necessary" |
| patch | n. | 图像块、图像碎片（ViT 把整图切成的小块） | "sequences of image patches can perform very well" |
| pre-trained | adj. | 预训练的（先在大数据上训练再迁移） | "When pre-trained on large amounts of data" |
| transfer | v. | 迁移（把模型能力应用到其他任务/数据上） | "transferred to multiple mid-sized or small image" |
| benchmark | n. | 基准（用于评测的标准数据集，如 ImageNet） | "small image recognition benchmarks (ImageNet, CIFAR-100" |
| attain | v. | 获得、达到（取得优秀结果） | "attains excellent results compared to state-of-the-art" |
| substantially | adv. | 显著地、大幅度地（指所需计算资源少得多） | "requiring substantially fewer computational resources" |
| state-of-the-art | phr. | 最先进的（当前最佳水平，常缩写为 SOTA） | "compared to state-of-the-art convolutional networks while" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-01 Neural Discrete Representation Learning

- [ ] 已读

**中文标题**：神经离散表示学习

**一句话概括**：提出 VQ-VAE，通过向量量化让编码器输出离散编码并学习先验，规避"后验坍塌"问题，从而生成高质量的图像、视频和语音。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| representation | n. | 表示、表征（模型学到的数据内部特征） | "learns such discrete representations" |
| supervision | n. | 监督（此处指无监督学习，不需要人工标签） | "without supervision remains a key challenge" |
| propose | v. | 提出（论文中引出自己方法的常用动词） | "we propose a simple yet powerful generative" |
| generative | adj. | 生成式的（能生成新样本的模型） | "a simple yet powerful generative model that" |
| discrete | adj. | 离散的（编码取值有限、不连续；与 continuous 相对） | "the encoder network outputs discrete, rather" |
| latent | adj. | 隐的、潜在的（latent representation 指隐空间中的表示） | "learn a discrete latent representation, we" |
| incorporate | v. | 引入、纳入（把向量量化的思想融入模型） | "incorporate ideas from vector quantisation (VQ)" |
| circumvent | v. | 规避、绕开（绕过后验坍塌这一难题） | "circumvent issues of "posterior collapse"" |
| posterior | n. | 后验（分布）（后验坍塌指隐变量被解码器忽略） | "paired with a powerful autoregressive decoder" |
| autoregressive | adj. | 自回归的（逐个预测序列元素的方式） | "with a powerful autoregressive decoder -- typically" |
| utility | n. | 实用性、效用（所学表示的价值） | "utility of the learnt representations" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-02 Taming Transformers for High-Resolution Image Synthesis

- [ ] 已读

**中文标题**：驯服 Transformer：高分辨率图像合成

**一句话概括**：提出 VQGAN，用 CNN 学习图像构成成分的"词汇表"，再用 Transformer 高效建模其组合，实现百万像素级、语义引导的图像合成。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| taming | v.-ing | 驯服、驾驭（标题用词，指让 Transformer 也能处理图像） | "Code and pretrained models can be found" |
| long-range | adj. | 长程的、远距离的（捕捉序列中相隔很远的依赖） | "long-range interactions on sequential data, transformers" |
| inductive bias | phr. | 归纳偏置（模型先天偏向某种结构，如 CNN 偏好局部） | "no inductive bias that prioritizes local interactions" |
| prioritize | v. | 优先考虑（CNN 的偏置优先处理局部信息） | "bias that prioritizes local interactions" |
| infeasible | adj. | 不可行的（计算上无法承受长序列） | "computationally infeasible for long sequences, such" |
| demonstrate | v. | 展示、证明（论文中陈述实验/结论的常用动词） | "We demonstrate how combining the effectiveness" |
| constituent | n. | 构成成分、组成元素（图像的基本组成部分） | "a context-rich vocabulary of image constituents" |
| composition | n. | 组合、构成（各成分如何排列组合成图像） | "efficiently model their composition within high-resolution" |
| conditional | adj. | 条件式的（生成受额外输入如类别/分割图控制） | "readily applied to conditional synthesis tasks" |
| semantically-guided | adj. | 语义引导的（按语义信息指导生成过程） | "semantically-guided synthesis of megapixel images" |
| megapixel | adj. | 百万像素级的（指超高分辨率图像） | "synthesis of megapixel images with transformers" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-03 Learning Transferable Visual Models From Natural Language Supervision

- [ ] 已读

**中文标题**：从自然语言监督中学习可迁移的视觉模型

**一句话概括**：提出 CLIP，用"预测哪张图配哪句说明"的预训练任务在 4 亿图文对上学习图像表示，使模型能零样本迁移到 30 多个下游任务。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| predetermined | adj. | 预先确定的（固定不变的类别集合） | "a fixed set of predetermined object categories" |
| restricted | adj. | 受限的（这种监督形式限制了泛化能力） | "This restricted form of supervision limits" |
| leverage | v. | 利用（借助更广泛的监督来源） | "leverages a much broader source of supervision" |
| caption | n. | 图片说明文字、配图文本 | "predicting which caption goes with which image" |
| scalable | adj. | 可扩展的（方法能随数据规模放大而受益） | "an efficient and scalable way to learn" |
| reference | v. | 引用、指称（用自然语言指向已学的视觉概念） | "reference learned visual concepts (or describe" |
| zero-shot | adj. | 零样本的（不经训练直接迁移到新任务） | "zero-shot transfer of the model to" |
| downstream | adj. | 下游的（预训练之后要解决的具体任务） | "the model to downstream tasks" |
| benchmark | v. | 做基准评测（在多个数据集上系统评估） | "benchmarking on over 30 different existing" |
| span | v. | 涵盖、跨越（任务范围覆盖 OCR、动作识别等） | "spanning tasks such as OCR, action" |
| competitive | adj. | 有竞争力的、可匹敌的（接近全监督基线水平） | "competitive with a fully supervised baseline" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-04 Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision

- [ ] 已读

**中文标题**：利用含噪声的文本监督扩大视觉与视觉-语言表示学习规模

**一句话概括**：提出一个简单的双编码器架构，用超过十亿的图文 alt-text 对和对比损失对齐视觉与语言表示，证明数据规模足以弥补噪声。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| annotation | n. | 标注（人工给出的标签，无需人工标注） | "without human annotations, visual and vision-language" |
| curated | adj. | 人工精选的（经过精心挑选整理的数据集） | "rely heavily on curated training datasets that" |
| curation | n. | 精选、整理过程（成本高昂的数据清洗环节） | "This costly curation process limits the" |
| hinder | v. | 阻碍（限制模型规模继续扩大） | "hinders the scaling of trained models" |
| leverage | v. | 利用（采用一个含噪声的大规模数据集） | "we leverage a noisy dataset of" |
| dual-encoder | adj. | 双编码器的（图像和文本各用一个编码器） | "A simple dual-encoder architecture learns to" |
| align | v. | 对齐（让视觉与语言表示在空间中对应起来） | "align visual and language representations of" |
| contrastive | adj. | 对比的（contrastive loss 对比损失：拉近匹配对、推远不匹配对） | "text pairs using a contrastive loss" |
| corpus | n. | 语料库（收集的大量图文数据） | "the scale of our corpus can make" |
| retrieval | n. | 检索（按查询找匹配的图像/文本） | "image-text retrieval benchmarks, even when compared" |
| cross-modality | n. | 跨模态（跨越图像与文本两种模态） | "cross-modality search with complex text" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-05 CoCa: Contrastive Captioners are Image-Text Foundation Models

- [ ] 已读

**中文标题**：CoCa：作为图像-文本基础模型的对比式说明生成器

**一句话概括**：提出 CoCa，用对比损失与说明生成损失联合预训练图像-文本编码器-解码器基础模型，兼收 CLIP 式对比方法与生成式方法的优点。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| foundation model | phr. | 基础模型（大规模预训练、可迁移到多任务的模型） | "large-scale pretrained foundation models is" |
| downstream | adj. | 下游的（预训练后迁移到的具体任务） | "quickly transferred to many downstream tasks" |
| minimalist | adj. | 极简的（设计简单、不做多余改动） | "a minimalist design to pretrain an image-text" |
| jointly | adv. | 联合地（两个训练目标同时进行） | "pretrain an image-text encoder-decoder foundation model jointly" |
| subsume | v. | 涵盖、合并（一个模型同时具备两类方法的能力） | "subsuming model capabilities from contrastive approaches" |
| omit | v. | 省略（解码器前半层不做跨注意力） | "CoCa omits cross-attention in the first" |
| cascade | v. | 级联（把剩余解码层依次串联起来） | "cascades the remaining decoder layers which" |
| embedding | n. | 嵌入（向量）（把输入映射成的稠密向量表示） | "unimodal image and text embeddings, in" |
| autoregressively | adv. | 自回归地（逐个预测下一个文本 token） | "decoder outputs which predicts text tokens" |
| overhead | n. | 开销（额外计算负担，本文指几乎为零） | "computed efficiently with minimal overhead" |
| seamlessly | adv. | 无缝地（把文本标签与图文数据统一处理） | "seamlessly unifying natural language supervision" |
| adaptation | n. | 适配、调整（针对具体任务做少量修改） | "minimal task-specific adaptation on a broad" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-06 BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation

- [ ] 已读

**中文标题**：BLIP：自举式语言-图像预训练，统一视觉-语言理解与生成

**一句话概括**：提出 BLIP 框架，用"说明生成器+过滤器"自举式利用含噪声的网络图文数据，能灵活迁移到视觉-语言理解与生成两类任务。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| excel | v. | 擅长（既有模型只在理解或生成单方面突出） | "only excel in either understanding-based tasks" |
| scale up | phr. | 扩大规模（靠堆数据提升性能） | "scaling up the dataset with noisy" |
| suboptimal | adj. | 次优的（含噪声网络数据并非最佳监督来源） | "which is a suboptimal source of supervision" |
| framework | n. | 框架（一整套方法体系） | "we propose BLIP, a new VLP framework" |
| bootstrap | v. | 自举（用自身生成的数据反哺改进训练） | "bootstrapping the captions, where a captioner generates" |
| captioner | n. | 说明生成器（为图像生成描述文本的模块） | "a captioner generates synthetic captions and" |
| synthetic | adj. | 合成的（机器生成而非人工写的） | "generates synthetic captions and a filter" |
| filter | n. | 过滤器（去掉低质量/噪声说明的模块） | "a filter removes the noisy ones" |
| retrieval | n. | 检索（图文匹配检索任务） | "image-text retrieval (+2.7% in average recall@1)" |
| generalization | n. | 泛化（模型在新数据/新任务上的适应能力） | "strong generalization ability when directly transferred" |
| zero-shot | adj. | 零样本的（不微调直接迁移到新任务） | "to video-language tasks in a zero-shot" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-07 BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models

- [ ] 已读

**中文标题**：BLIP-2：用冻结图像编码器与大语言模型自举语言-图像预训练

**一句话概括**：提出 BLIP-2，用轻量级 Querying Transformer 桥接冻结的预训练图像编码器与大语言模型，以远少于现有方法的可训练参数取得 SOTA。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| prohibitive | adj. | 高得令人望而却步的（训练成本日益高昂） | "has become increasingly prohibitive due to" |
| end-to-end | adj. | 端到端的（从输入到输出整体联合训练） | "end-to-end training of large-scale models" |
| generic | adj. | 通用的（不针对特定任务的设计） | "a generic and efficient pre-training strategy" |
| off-the-shelf | adj. | 现成的（直接拿来用的已有模型） | "off-the-shelf frozen pre-trained image encoders" |
| frozen | adj. | 冻结的（参数固定不参与训练） | "frozen pre-trained image encoders and frozen" |
| bridge | v. | 桥接、弥合（连接两种不同模态/模型） | "bridges the modality gap with a" |
| modality | n. | 模态（图像、文本等不同的信息形式） | "the modality gap with a lightweight" |
| lightweight | adj. | 轻量级的（参数量小、开销低） | "a lightweight Querying Transformer, which is" |
| stage | n. | 阶段（训练分两个阶段进行） | "which is pre-trained in two stages" |
| outperform | v. | 胜过、优于（性能超过对比模型） | "outperforms Flamingo80B by 8.7% on" |
| emerging | adj. | 涌现的（训练后自然出现的新能力） | "emerging capabilities of zero-shot image-to-text" |
| instruction | n. | 指令（自然语言给出的任务要求） | "that can follow natural language instructions" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-08 Flamingo: a Visual Language Model for Few-Shot Learning

- [ ] 已读

**中文标题**：Flamingo：用于少样本学习的视觉语言模型

**一句话概括**：提出 Flamingo 系列视觉语言模型，通过架构创新桥接预训练的纯视觉/纯语言模型并处理任意交错的图文序列，实现上下文少样本学习。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| handful | n. | 少量、一小把（只有极少几个标注样本） | "using only a handful of annotated examples" |
| annotated | adj. | 已标注的（带人工标签的） | "a handful of annotated examples is" |
| open challenge | phr. | 尚待解决的难题（尚未攻克的研究问题） | "an open challenge for multimodal machine learning" |
| innovation | n. | 创新（架构上的关键改进） | "key architectural innovations to: (i) bridge" |
| bridge | v. | 桥接、连接（把视觉模型与语言模型对接） | "bridge powerful pretrained vision-only and language-only" |
| interleaved | adj. | 交错排列的（文本与图像穿插混合） | "arbitrarily interleaved visual and textual data" |
| ingest | v. | 摄入、输入（把图像或视频作为输入） | "seamlessly ingest images or videos as inputs" |
| corpus | n. | 语料库（多模态网络数据集合） | "large-scale multimodal web corpora containing arbitrarily" |
| endow | v. | 赋予（让模型具备某种能力） | "endow them with in-context few-shot learning" |
| prompt | v. | 提示、引导（用问题/示例引导模型作答） | "the model is prompted with a question" |
| spectrum | n. | 谱系、范围（从开放式到封闭式任务的连续区间） | "lying anywhere on this spectrum" |
| fine-tune | v. | 微调（在任务数据上继续训练） | "outperforms models fine-tuned on thousands of" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-09 Language Is Not All You Need: Aligning Perception with Language Models

- [ ] 已读

**中文标题**：语言不是全部：让感知与语言模型对齐

**一句话概括**：提出 Kosmos-1 多模态大语言模型，从网络级多模态语料训练，能感知多种模态、上下文学习和遵循指令，并引入 Raven IQ 测试集。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| convergence | n. | 汇聚、融合（语言、感知、行动等多方面能力走向统一） | "A big convergence of language, multimodal perception" |
| perception | n. | 感知（对图像、声音等模态的接收与理解） | "of language, multimodal perception, action" |
| artificial general intelligence | phr. | 通用人工智能（简称 AGI） | "a key step toward artificial general intelligence" |
| perceive | v. | 感知（模型能接收并理解各种模态信息） | "that can perceive general modalities, learn" |
| interleaved | adj. | 交错排列的（图文数据穿插混合） | "web-scale multimodal corpora, including arbitrarily interleaved" |
| chain-of-thought | adj. | 思维链的（让模型逐步推理的提示方法） | "multimodal chain-of-thought prompting, on a" |
| gradient update | phr. | 梯度更新（训练中更新参数的步骤，本文指不做任何训练） | "without any gradient updates or finetuning" |
| OCR-free | adj. | 免 OCR 的（无需光学字符识别预处理） | "even OCR-free NLP (directly fed with" |
| specify | v. | 指定（通过文本指令指定分类要求） | "specifying classification via text instructions" |
| cross-modal | adj. | 跨模态的（知识在不同模态间迁移） | "benefit from cross-modal transfer, i.e.," |
| diagnose | v. | 诊断、测评（测试模型某方面能力） | "diagnoses the nonverbal reasoning capability of" |
| reasoning | n. | 推理（此处指非言语推理能力） | "the nonverbal reasoning capability of MLLMs" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-10 Visual Instruction Tuning

- [ ] 已读

**中文标题**：视觉指令微调

**一句话概括**：首次用语言-only 的 GPT-4 生成多模态语言-图像指令数据并进行指令微调，训练出端到端的大视觉语言模型 LLaVA。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| instruction tuning | phr. | 指令微调（用"指令-回答"数据训练模型服从指令） | "Instruction tuning large language models (LLMs)" |
| machine-generated | adj. | 机器生成的（由模型自动生成而非人工编写） | "machine-generated instruction-following data has improved" |
| multimodal | adj. | 多模态的（同时处理语言与图像等） | "the idea is less explored in the" |
| assistant | n. | 助手（模型定位为语言与视觉助手） | "Language and Vision Assistant, an end-to-end" |
| end-to-end | adj. | 端到端的（整体联合训练） | "an end-to-end trained large multimodal model" |
| connect | v. | 连接（把视觉编码器与大语言模型接起来） | "connects a vision encoder and LLM" |
| general-purpose | adj. | 通用目的的（不局限于单一任务） | "general-purpose visual and language understanding" |
| exhibit | v. | 展现、表现出（展现出类似 GPT-4 的行为） | "exhibiting the behaviors of multimodal GPT-4" |
| synthetic | adj. | 合成的（人工构造的评测数据） | "a synthetic multimodal instruction-following dataset" |
| synergy | n. | 协同作用（LLaVA 与 GPT-4 配合的效果） | "the synergy of LLaVA and GPT-4" |
| accuracy | n. | 准确率（评测指标，此处达 92.53%） | "a new state-of-the-art accuracy of 92.53%" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-11 MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models

- [ ] 已读

**中文标题**：MiniGPT-4：用先进大语言模型增强视觉-语言理解

**一句话概括**：仅用一层投影层把冻结的视觉编码器与 Vicuna 对齐，首次揭示仅靠正确对齐视觉特征即可让模型具备 GPT-4 式的多项高级多模态能力。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| extraordinary | adj. | 非凡的（GPT-4 展现出的出众多模态能力） | "has demonstrated extraordinary multi-modal abilities, such" |
| identify | v. | 识别、找出（识别出图像中的幽默元素） | "identifying humorous elements within images" |
| undisclosed | adj. | 未公开的（GPT-4 技术细节仍不公开） | "the technical details behind GPT-4 continue" |
| stem from | phr. | 源于、来自（能力来源于……） | "stem from the utilization of sophisticated" |
| sophisticated | adj. | 精密复杂的（先进的大语言模型） | "utilization of sophisticated large language models" |
| align | v. | 对齐（让视觉特征与语言模型匹配） | "aligns a frozen visual encoder with" |
| projection layer | phr. | 投影层（把视觉特征映射到语言空间的网络层） | "with a frozen advanced LLM, Vicuna, using" |
| uncover | v. | 揭示、发现（首次发现某现象） | "uncovers that properly aligning the visual" |
| emerging | adj. | 涌现的（训练后自然冒出的新能力） | "other emerging capabilities in MiniGPT-4" |
| curate | v. | 精心整理（人工筛选并构建数据集） | "we curate a detailed image description" |
| reliability | n. | 可靠性（生成内容更稳定可信） | "improves the model's generation reliability and" |
| usability | n. | 可用性（模型整体更实用） | "reliability and overall usability" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-12 InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning

- [ ] 已读

**中文标题**：InstructBLIP：面向通用视觉-语言模型的指令微调

**一句话概括**：基于 BLIP-2 系统研究视觉-语言指令微调，提出指令感知的 Query Transformer，在全部留出数据集上取得零样本 SOTA。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| competence | n. | 能力（大语言模型具备广泛能力） | "general-purpose language models with broad competence" |
| diversity | n. | 多样性（任务多样导致构建通用模型困难） | "task diversity resulting from the additional" |
| systematic | adj. | 系统性的（有条理、成体系的研究） | "a systematic and comprehensive study on" |
| comprehensive | adj. | 全面的（覆盖广泛的方面） | "systematic and comprehensive study on vision-language" |
| transform | v. | 转换（把数据集改造成指令微调格式） | "transform them into instruction tuning format" |
| instruction-aware | adj. | 指令感知的（能根据给定指令调整提取的特征） | "an instruction-aware Query Transformer, which extracts" |
| informative | adj. | 信息丰富的（提取对任务有用的特征） | "extracts informative features tailored to the" |
| tailored to | phr. | 针对……定制的（特征与给定指令相匹配） | "features tailored to the given instruction" |
| held-out | adj. | 留出的（训练时未见、专用于测试的数据） | "across all 13 held-out datasets, substantially" |
| substantially | adv. | 显著地（性能明显超过对比模型） | "substantially outperforming BLIP-2 and larger" |
| qualitatively | adv. | 定性地（通过示例直观展示优势） | "qualitatively demonstrate the advantages of InstructBLIP" |
| concurrent | adj. | 同期出现的（同一时期发表的其他模型） | "over concurrent multimodal models" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-13 Improved Baselines with Visual Instruction Tuning

- [ ] 已读

**中文标题**：基于视觉指令微调的改进基线

**一句话概括**：用全连接跨模态连接器、MLP 投影与任务导向 VQA 数据等简单改进，用仅 1.2M 数据在 11 个基准上建立更强的 LLaVA 基线。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| encouraging | adj. | 令人鼓舞的（视觉指令微调进展喜人） | "have recently shown encouraging progress with" |
| connector | n. | 连接器（桥接视觉与语言表示的模块） | "the fully-connected vision-language cross-modal connector" |
| fully-connected | adj. | 全连接的（每一层神经元全部相连的 MLP 结构） | "that the fully-connected vision-language cross-modal" |
| surprisingly | adv. | 惊人地、出乎意料地（性能出人意料地强） | "is surprisingly powerful and data-efficient" |
| data-efficient | adj. | 数据高效的（少量数据就能学好） | "powerful and data-efficient" |
| modification | n. | 修改、改进（对 LLaVA 的简单改动） | "simple modifications to LLaVA, namely, using" |
| projection | n. | 投影（把视觉特征映射到语言空间的 MLP 层） | "with an MLP projection and adding" |
| formatting | adj. | 格式化的（给回答设计统一格式的提示） | "simple response formatting prompts, we establish" |
| establish | v. | 建立（建立起更强的基线模型） | "we establish stronger baselines that achieve" |
| checkpoint | n. | 检查点（此处指训练好的模型权重文件） | "Our final 13B checkpoint uses merely" |
| merely | adv. | 仅仅（只用很少的数据） | "checkpoint uses merely 1.2M publicly available" |
| accessible | adj. | 易获得的、可及的（让 SOTA 研究门槛更低） | "make state-of-the-art LMM research more accessible" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-14 Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond

- [ ] 已读

**中文标题**：Qwen-VL：用于理解、定位、文本阅读等任务的多功能视觉-语言模型

**一句话概括**：提出 Qwen-VL 系列，通过精心设计的视觉接收器、3 阶段训练管线与图像-说明-框元组对齐，赋予模型定位与文本阅读能力。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| versatile | adj. | 多用途的、多才多艺的（能胜任多种任务） | "Qwen-VL: A Versatile Vision-Language Model" |
| localization | n. | 定位（视觉定位，找出图像中目标的位置/框） | "for Understanding, Localization, Text Reading" |
| endow | v. | 赋予（让语言模型获得视觉能力） | "we endow it with visual capacity" |
| meticulously | adv. | 精心地、细致地（设计非常考究） | "the meticulously designed (i) visual receptor" |
| receptor | n. | 感受器、接收模块（负责接收图像输入的组件） | "meticulously designed (i) visual receptor" |
| pipeline | n. | 管线、流程（分阶段串联的训练流程） | "3-stage training pipeline, and (iv) multilingual" |
| corpus | n. | 语料库（清洗后的多语言多模态数据） | "multilingual multimodal cleaned corpus" |
| conventional | adj. | 常规的、传统的（除常规任务之外） | "Beyond the conventional image description and" |
| grounding | n. | 视觉定位（把文本指称与图像区域对应起来） | "implement the grounding and text-reading ability" |
| tuple | n. | 元组（图像、说明、边框组成的数据单元） | "by aligning image-caption-box tuples" |
| generalist | adj. | 通才型的（一个模型应对多种任务） | "set new records for generalist models" |
| benchmark | n. | 基准（以视觉为中心的标准评测数据集） | "a broad range of visual-centric benchmarks" |
| superiority | n. | 优越性（性能优于现有模型） | "demonstrates superiority compared to existing vision-language" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-15 CogVLM: Visual Expert for Pretrained Language Models

- [ ] 已读

**中文标题**：CogVLM：预训练语言模型的视觉专家

**一句话概括**：提出 CogVLM，在注意力与 FFN 层中加入可训练的"视觉专家"模块实现视觉-语言特征深度融合，不牺牲任何 NLP 性能。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| shallow | adj. | 浅层的（只做简单映射、融合不深的对齐方法） | "the popular shallow alignment method which maps" |
| alignment | n. | 对齐（把图像特征与语言模型输入空间对应） | "shallow alignment method which maps image" |
| map | v. | 映射（把特征变换到另一空间） | "maps image features into the input space" |
| bridge | v. | 弥合、桥接（填补模型间的差距） | "bridges the gap between the frozen" |
| trainable | adj. | 可训练的（参数参与训练更新） | "a trainable visual expert module in" |
| module | n. | 模块（模型中的功能组件） | "visual expert module in the attention" |
| fusion | n. | 融合（视觉与语言特征的深度融合） | "deep fusion of vision language features" |
| sacrifice | v. | 牺牲（不牺牲任何 NLP 任务性能） | "without sacrificing any performance on NLP" |
| cross-modal | adj. | 跨模态的（跨越视觉与语言两种模态） | "10 classic cross-modal benchmarks, including NoCaps" |
| rank | v. | 排名（在基准上位居第 2） | "ranks the 2nd on VQAv2, OKVQA" |
| surpass | v. | 超越（性能超过或持平更大模型） | "surpassing or matching PaLI-X 55B" |
| checkpoint | n. | 检查点（训练好的模型权重） | "Codes and checkpoints are available at" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-16 InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks

- [ ] 已读

**中文标题**：InternVL：扩大视觉基础模型规模并对其对齐以适配通用视觉-语言任务

**一句话概括**：将视觉基础模型扩到 60 亿参数并逐步与大语言模型对齐，在 32 个通用视觉-语言基准上达到 SOTA，可替代 ViT-22B。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| exponential | adj. | 指数级的（LLM 规模飞速增长） | "The exponential growth of large language" |
| numerous | adj. | 大量的（带来众多新的可能性） | "opened up numerous possibilities for multimodal" |
| critical | adj. | 关键的（视觉基础模型是 AGI 的关键要素） | "critical elements of multi-modal AGI" |
| keep pace with | phr. | 跟上……的步伐（视觉领域进展落后于 LLM） | "has not kept pace with LLMs" |
| progressively | adv. | 逐步地（分阶段逐渐对齐） | "progressively aligns it with the LLM" |
| align | v. | 对齐（让视觉模型与语言模型协同） | "progressively aligns it with the LLM" |
| generic | adj. | 通用的（覆盖面广、不限于特定任务） | "32 generic visual-linguistic benchmarks including visual" |
| perception | n. | 感知（对视觉信息的理解任务） | "including visual perception tasks such as" |
| pixel-level | adj. | 像素级的（对每个像素做识别，如分割） | "such as image-level or pixel-level recognition" |
| retrieval | n. | 检索（图文/视频文本检索任务） | "zero-shot image/video-text retrieval, and link" |
| alternative | n. | 替代方案（可替代 ViT-22B 的选择） | "a good alternative to the ViT-22B" |
| contribute | v. | 贡献（希望推动多模态大模型发展） | "could contribute to the development of" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-17 Segment Anything

- [ ] 已读

**中文标题**：分割一切

**一句话概括**：提出 Segment Anything（SA）项目：新任务、可提示（promptable）模型与含 10 亿掩码、1100 万图像的最大分割数据集 SA-1B。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| segment | v. | 分割（把图像中的物体区域划分出来） | "image segmentation" |
| data collection loop | phr. | 数据采集闭环（用模型辅助收集数据再训练模型的循环） | "in a data collection loop, we built" |
| mask | n. | 掩码（标注物体区域的像素级标记） | "with over 1 billion masks on" |
| licensed | adj. | 有许可的（数据使用合规授权） | "licensed and privacy respecting images" |
| privacy respecting | phr. | 尊重隐私的（不泄露个人信息） | "11M licensed and privacy respecting images" |
| promptable | adj. | 可提示的（接受点、框等提示输入的） | "trained to be promptable, so it can" |
| distribution | n. | 分布（数据分布，指新的图像分布） | "transfer zero-shot to new image distributions" |
| evaluate | v. | 评估（系统评测模型能力） | "We evaluate its capabilities on numerous" |
| competitive | adj. | 有竞争力的（接近甚至超过全监督方法） | "competitive with or even superior to" |
| superior | adj. | 更优的（超过之前全监督结果） | "or even superior to prior fully supervised" |
| foster | v. | 促进、推动（推动基础模型研究） | "to foster research into foundation models" |
| corresponding | adj. | 相应的（与模型配套的数据集） | "corresponding dataset (SA-1B) of 1B masks" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-18 ImageBind: One Embedding Space To Bind Them All

- [ ] 已读

**中文标题**：ImageBind：用一个嵌入空间绑定所有模态

**一句话概括**：仅用图像配对数据就把六种模态（图像、文本、音频、深度、热成像、IMU）绑进一个联合嵌入空间，涌现出多种开箱即用的跨模态能力。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| joint | adj. | 联合的（多模态共享一个嵌入空间） | "learn a joint embedding across six" |
| modality | n. | 模态（图像、文本、音频等信息形式） | "six different modalities - images, text" |
| thermal | n. | 热成像（数据）（本文中与深度、IMU 并列的模态） | "depth, thermal, and IMU data" |
| sufficient | adj. | 充分的（仅图像配对数据就足够） | "only image-paired data is sufficient to" |
| bind | v. | 绑定、联结（把各模态联结到同一空间） | "is sufficient to bind the modalities" |
| leverage | v. | 利用（借助现有大规模视觉-语言模型） | "ImageBind can leverage recent large scale" |
| emergent | adj. | 涌现的（训练后自然出现、未显式设计的能力） | "It enables novel emergent applications 'out-of-the-box'" |
| out-of-the-box | phr. | 开箱即用的（无需额外训练即可使用） | "enables novel emergent applications 'out-of-the-box'" |
| arithmetic | n. | 算术运算（对模态向量做加减组合） | "composing modalities with arithmetic, cross-modal" |
| retrieval | n. | 检索（跨模态检索任务） | "including cross-modal retrieval, composing modalities" |
| strength | n. | 强度、能力（图像编码器越强涌现能力越好） | "improve with the strength of the image" |
| specialist | adj. | 专才型的（只擅长单一模态/任务的专门模型） | "recognition tasks across modalities, outperforming specialist" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-19 Robust Speech Recognition via Large-Scale Weak Supervision

- [ ] 已读

**中文标题**：通过大规模弱监督实现鲁棒语音识别

**一句话概括**：用 68 万小时多语言、多任务的弱监督数据训练语音识别系统，零样本迁移即可媲美全监督结果，接近人类准确率与鲁棒性。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| robust | adj. | 鲁棒的、稳健的（对各种条件都稳定可靠） | "Robust Speech Recognition via Large-Scale" |
| weak supervision | phr. | 弱监督（用低质量、自动获取的标签训练） | "via Large-Scale Weak Supervision" |
| transcript | n. | 转录文本（音频对应的文字记录） | "predict large amounts of transcripts of audio" |
| multilingual | adj. | 多语言的（覆盖多种语言） | "multilingual and multitask supervision, the resulting" |
| multitask | adj. | 多任务的（同时学习多种任务） | "multitask supervision, the resulting models generalize" |
| generalize | v. | 泛化（在新数据上表现良好） | "the resulting models generalize well to" |
| competitive | adj. | 有竞争力的（可与全监督结果相比） | "competitive with prior fully supervised results" |
| zero-shot | adj. | 零样本的（不微调直接用于新场景） | "in a zero-shot transfer setting without" |
| fine-tuning | n. | 微调（在任务数据上继续训练） | "without the need for any fine-tuning" |
| robustness | n. | 鲁棒性（面对干扰/噪声的稳定性） | "approach their accuracy and robustness" |
| inference | n. | 推理（用训练好的模型做预测） | "models and inference code to serve" |
| foundation | n. | 基础（为后续研究提供基础） | "serve as a foundation for further" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-20 GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models

- [ ] 已读

**中文标题**：GLIDE：文本引导扩散模型实现照片级图像生成与编辑

**一句话概括**：比较 CLIP 引导与无分类器引导两种文本条件扩散模型策略，后者更受人类评估者青睐，模型还可微调用于图像修复与编辑。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| photorealistic | adj. | 照片级逼真的（生成图像与真实照片难以区分） | "Towards Photorealistic Image Generation and" |
| guidance | n. | 引导（生成过程中控制方向的机制） | "paired with a guidance technique to trade" |
| trade off | phr. | 权衡、以……换取……（牺牲多样性换保真度） | "trade off diversity for fidelity" |
| fidelity | n. | 保真度（生成结果与目标/真实图像的吻合程度） | "diversity for fidelity" |
| text-conditional | adj. | 文本条件的（生成受文本描述控制） | "the problem of text-conditional image synthesis" |
| strategy | n. | 策略（两种不同的引导方案） | "two different guidance strategies: CLIP guidance" |
| classifier-free | adj. | 无分类器的（不借助分类器梯度、更简单的引导方法） | "CLIP guidance and classifier-free guidance" |
| evaluator | n. | 评估者（做人工评测的人） | "preferred by human evaluators for both" |
| similarity | n. | 相似度（生成图与说明文字的匹配程度） | "photorealism and caption similarity, and often" |
| reranking | n. | 重排序（对候选结果重新排序挑选） | "even when the latter uses expensive" |
| inpainting | n. | 图像修复（补全图像缺失/被遮区域） | "fine-tuned to perform image inpainting, enabling" |
| editing | n. | 编辑（修改图像内容） | "enabling powerful text-driven image editing" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-21 Hierarchical Text-Conditional Image Generation with CLIP Latents

- [ ] 已读

**中文标题**：用 CLIP 隐向量进行分层文本条件图像生成

**一句话概括**：提出两阶段模型——先验根据文本生成 CLIP 图像嵌入，解码器再据此生成图像，并以零样本方式实现语言引导的图像操控。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| hierarchical | adj. | 分层的（模型分两级：先验+解码器） | "Hierarchical Text-Conditional Image Generation with" |
| contrastive | adj. | 对比的（对比学习得到的模型，如 CLIP） | "Contrastive models like CLIP have been" |
| robust | adj. | 稳健的（学到可靠、鲁棒的表示） | "learn robust representations of images that" |
| capture | v. | 捕捉（表示同时包含语义和风格信息） | "capture both semantics and style" |
| semantics | n. | 语义（图像的内容含义） | "capture both semantics and style" |
| prior | n. | 先验（模型）（本文指根据文本生成图像嵌入的模块） | "a prior that generates a CLIP" |
| embedding | n. | 嵌入（向量）（CLIP 图像嵌入） | "generates a CLIP image embedding given" |
| conditioned on | phr. | 以……为条件的（生成过程受嵌入控制） | "conditioned on the image embedding" |
| variation | n. | 变体（保留语义风格的图像变化版本） | "produce variations of an image that" |
| preserve | v. | 保留（保持原图的语义与风格） | "preserve both its semantics and style" |
| manipulation | n. | 操作、操控（对图像内容的修改） | "language-guided image manipulations in a zero-shot" |
| autoregressive | adj. | 自回归的（逐元素生成的方式，与扩散模型并列） | "experiment with both autoregressive and diffusion" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-22 Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding

- [ ] 已读

**中文标题**：深度语言理解的逼真文生图扩散模型

**一句话概括**：提出 Imagen，关键发现是增大文本语言模型比增大图像扩散模型更能提升保真度与图文对齐，并引入 DrawBench 基准。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| unprecedented | adj. | 前所未有的（逼真度达到新高度） | "an unprecedented degree of photorealism and" |
| photorealism | n. | 照片级真实感（生成图像的真实程度） | "degree of photorealism and a deep" |
| hinge on | phr. | 取决于、关键在于（成功依托于……） | "hinges on the strength of diffusion" |
| high-fidelity | adj. | 高保真的（生成质量与真实图像高度一致） | "diffusion models in high-fidelity image generation" |
| discovery | n. | 发现（论文的核心发现） | "Our key discovery is that generic" |
| generic | adj. | 通用的（非专门为图像设计的语言模型） | "is that generic large language models" |
| corpus | n. | 语料库（纯文本训练数据） | "pretrained on text-only corpora, are surprisingly" |
| surprisingly | adv. | 惊人地（效果出乎意料地好） | "corpora, are surprisingly effective at encoding" |
| encode | v. | 编码（把文本转成可用于生成的表示） | "surprisingly effective at encoding text for" |
| boost | v. | 提升（提高样本保真度与图文对齐） | "boosts both sample fidelity and image-text" |
| alignment | n. | 对齐（生成图像与文本描述的一致程度） | "fidelity and image-text alignment much more" |
| rater | n. | 评分者（做人工评测的人） | "human raters find Imagen samples to" |
| on par with | phr. | 与……相当（与 COCO 数据本身水平相当） | "on par with the COCO data" |
| comprehensive | adj. | 全面的（覆盖广泛场景的基准） | "a comprehensive and challenging benchmark for" |
| side-by-side | adj. | 并排的（并排对比两种模型的输出） | "side-by-side comparisons, both in terms" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-23 High-Resolution Image Synthesis with Latent Diffusion Models

- [ ] 已读

**中文标题**：潜在扩散模型实现高分辨率图像合成

**一句话概括**：把扩散模型搬进预训练自编码器的隐空间训练，大幅降低算力需求，并通过跨注意力层支持文本、框等条件控制的高分辨率生成。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| decompose | v. | 分解（把图像生成过程拆解成逐步去噪） | "decomposing the image formation process into" |
| sequential | adj. | 顺序的、逐次的（逐步依次应用去噪自编码器） | "a sequential application of denoising autoencoders" |
| denoising | adj. | 去噪的（逐步去除噪声恢复图像） | "sequential application of denoising autoencoders" |
| autoencoder | n. | 自编码器（先压缩再重建的神经网络） | "a sequential application of denoising autoencoders" |
| formulation | n. | 公式化表述（模型的数学表述方式） | "their formulation allows for a guiding mechanism" |
| mechanism | n. | 机制（控制生成过程的引导机制） | "allows for a guiding mechanism to" |
| pixel space | phr. | 像素空间（直接在像素层面操作） | "operate directly in pixel space" |
| consume | v. | 消耗（训练耗掉数百个 GPU 天） | "consumes hundreds of GPU days and" |
| inference | n. | 推理（生成样本的过程） | "inference is expensive due to sequential" |
| latent space | phr. | 隐空间、潜在空间（压缩后的低维特征空间） | "in the latent space of powerful" |
| preservation | n. | 保留（在压缩与细节保留之间取最优平衡） | "between complexity reduction and detail preservation" |
| conditioning | n. | 条件（控制生成的外部输入） | "general conditioning inputs such as text" |
| inpainting | n. | 图像修复（补全图像缺失区域） | "image inpainting and highly competitive performance" |
| super-resolution | n. | 超分辨率（把低分辨率图放大并补细节） | "semantic scene synthesis, and super-resolution, while" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-24 Video Diffusion Models

- [ ] 已读

**中文标题**：视频扩散模型

**一句话概括**：提出视频扩散模型，可联合训练图像与视频数据以降低梯度方差、加快优化，并用新的条件采样技术支持长视频与高分辨率扩展。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| temporally | adv. | 时间上地（视频在时间维度的连贯性） | "Generating temporally coherent high fidelity video" |
| coherent | adj. | 连贯的（视频帧间在时间上一致连贯） | "temporally coherent high fidelity video" |
| milestone | n. | 里程碑（生成建模研究的重要节点） | "an important milestone in generative modeling" |
| promising | adj. | 有前景的（初步结果很有希望） | "shows very promising initial results" |
| extension | n. | 扩展（标准图像扩散架构的自然扩展） | "a natural extension of the standard" |
| jointly | adv. | 联合地（图像与视频数据一起训练） | "enables jointly training from image and" |
| variance | n. | 方差（小批量梯度的波动幅度） | "reduce the variance of minibatch gradients" |
| minibatch | n. | 小批量（每次训练用的一小批样本） | "the variance of minibatch gradients and" |
| gradient | n. | 梯度（训练中用于更新参数的信号） | "gradients and speed up optimization" |
| optimization | n. | 优化（训练收敛过程） | "and speed up optimization" |
| conditional sampling | phr. | 条件采样（受额外条件控制的采样方法） | "a new conditional sampling technique for" |
| unconditional | adj. | 无条件的（不依赖任何输入条件的生成） | "video prediction and unconditional video generation" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-25 GPT-4o System Card

- [ ] 已读

**中文标题**：GPT-4o 系统卡

**一句话概括**：发布 GPT-4o 系统卡，介绍这一端到端全模态（omni）模型的输入输出组合、能力、局限，以及安全评估与第三方评估。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| autoregressive | adj. | 自回归的（逐 token 预测式生成） | "an autoregressive omni model that accepts" |
| omni | adj. | 全能的、全模态的（能处理所有模态的模型） | "an autoregressive omni model that accepts" |
| combination | n. | 组合（文本、音频、图像、视频的任意组合） | "as input any combination of text" |
| end-to-end | adv. | 端到端地（整个模型联合训练） | "trained end-to-end across text, vision" |
| process | v. | 处理（所有输入由同一神经网络处理） | "processed by the same neural network" |
| millisecond | n. | 毫秒（响应时延的单位，232 毫秒） | "respond to audio inputs in as" |
| commitment | n. | 承诺（安全建设方面的承诺） | "In line with our commitment to" |
| voluntary | adj. | 自愿的（向白宫作出的自愿承诺） | "consistent with our voluntary commitments to" |
| preparedness | n. | 预备性、准备（安全预备框架，评估潜在风险） | "which includes our Preparedness Framework evaluations" |
| assessment | n. | 评估（第三方对危险能力的评估） | "third-party assessments on dangerous capabilities" |
| capability | n. | 能力（危险能力等） | "assessments on dangerous capabilities, as well" |
| societal | adj. | 社会的（对社会层面的潜在影响） | "potential societal impacts of GPT-4o's" |
| aligned | adj. | 对齐的（模型行为符合人类意图与安全要求） | "to ensure the model is safe and" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-26 Auto-Encoding Variational Bayes

- [ ] 已读

**中文标题**：自编码变分贝叶斯

**一句话概括**：提出变分自编码器（VAE），用重参数化技巧与随机梯度方法高效优化变分下界，解决连续隐变量后验不可解时的推断问题。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| inference | n. | 推断（从数据估计隐变量的过程） | "efficient inference and learning in directed" |
| directed | adj. | 有向的（有向概率模型，边有方向的图模型） | "inference and learning in directed probabilistic" |
| latent variable | phr. | 隐变量（未被观测、需推断的变量） | "continuous latent variables with intractable posterior" |
| intractable | adj. | 不可解的、难处理的（后验无法精确计算） | "latent variables with intractable posterior distributions" |
| posterior | n. | 后验（分布）（已知数据后隐变量的条件分布） | "with intractable posterior distributions, and large" |
| stochastic | adj. | 随机的（基于随机采样的方法） | "stochastic variational inference and learning algorithm" |
| variational | adj. | 变分的（用近似分布逼近真实后验的框架） | "variational inference and learning algorithm that" |
| mild | adj. | 温和的（要求宽松、易满足的条件） | "under some mild differentiability conditions, even" |
| differentiability | n. | 可微性（函数可求导的性质） | "some mild differentiability conditions, even works" |
| reparameterization | n. | 重参数化（把采样改写为可微的形式，即"重参数化技巧"） | "a reparameterization of the variational lower bound" |
| bound | n. | 界（下界，此处指变分下界 ELBO） | "reparameterization of the variational lower bound" |
| estimator | n. | 估计器（估计下界的工具） | "a lower bound estimator that can" |
| i.i.d. | adj. | 独立同分布的（数据集样本相互独立且同分布） | "continuous latent variables per datapoint, posterior" |
| recognition model | phr. | 识别模型（本文中指近似后验的编码器网络） | "fitting an approximate inference model" |
| reflect | v. | 反映（理论优势体现在实验结果中） | "advantages are reflected in experimental results" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-27 Denoising Diffusion Probabilistic Models

- [ ] 已读

**中文标题**：去噪扩散概率模型

**一句话概括**：提出 DDPM，用加权变分界训练扩散概率模型，在无条件 CIFAR10 上取得 FID 3.17 的 SOTA 图像生成质量。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| denoising | adj. | 去噪的（逐步去除噪声的） | "high quality image synthesis results using" |
| diffusion | n. | 扩散（前向逐步加噪声、反向去噪的生成范式） | "synthesis results using diffusion probabilistic models" |
| probabilistic | adj. | 概率的（基于概率分布的模型） | "diffusion probabilistic models, a class of" |
| latent variable model | phr. | 隐变量模型（含有未观测变量的生成模型） | "a class of latent variable models" |
| inspired by | phr. | 受……启发（思想来源于非平衡热力学） | "inspired by considerations from nonequilibrium thermodynamics" |
| nonequilibrium | adj. | 非平衡的（热力学中的非平衡态） | "from nonequilibrium thermodynamics" |
| thermodynamics | n. | 热力学（研究能量转化的物理分支） | "inspired by considerations from nonequilibrium thermodynamics" |
| variational bound | phr. | 变分界（用于训练的加权变分下界） | "a weighted variational bound designed according" |
| novel | adj. | 新颖的（新的联系/发现） | "a novel connection between diffusion probabilistic" |
| score matching | phr. | 分数匹配（估计数据分布梯度的一种方法） | "denoising score matching with Langevin dynamics" |
| admit | v. | 具有、允许（模型天然支持一种渐进式有损解压方案） | "naturally admit a progressive lossy decompression" |
| lossy | adj. | 有损的（压缩后信息有损失） | "a progressive lossy decompression scheme" |
| decompression | n. | 解压缩（从压缩表示还原数据） | "lossy decompression scheme that can be" |
| interpret | v. | 解释为、理解为（可看作自回归解码的推广） | "interpreted as a generalization of autoregressive" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-28 Denoising Diffusion Implicit Models

- [ ] 已读

**中文标题**：去噪扩散隐式模型

**一句话概括**：提出 DDIM，构造一类非马尔可夫扩散过程，用与 DDPM 相同的训练目标实现快 10–50 倍的采样，并支持隐空间语义插值。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| adversarial training | phr. | 对抗训练（生成对抗网络的训练方式，本文无需使用） | "without adversarial training, yet they require" |
| simulate | v. | 模拟（一步步模拟马尔可夫链） | "simulating a Markov chain for many" |
| Markov chain | phr. | 马尔可夫链（状态转移只依赖当前状态的随机过程） | "a Markov chain for many steps" |
| accelerate | v. | 加速（加快采样速度） | "To accelerate sampling, we present denoising" |
| implicit | adj. | 隐式的（不显式依赖马尔可夫性质的过程） | "we present denoising diffusion implicit models" |
| iterative | adj. | 迭代的（反复执行若干步的） | "a more efficient class of iterative" |
| reverse | n. | 逆过程（生成过程是扩散过程的逆向） | "the reverse of a Markovian diffusion" |
| Markovian | adj. | 马尔可夫（性质）的（具有马尔可夫性的） | "the reverse of a Markovian diffusion" |
| objective | n. | 目标（函数）（与 DDPM 相同的训练目标） | "lead to the same training objective" |
| empirically | adv. | 实验上、凭经验地（通过实验证明） | "We empirically demonstrate that DDIMs can" |
| wall-clock time | phr. | 墙钟时间（实际经过的真实时间） | "in terms of wall-clock time compared" |
| trade off | phr. | 权衡（用计算量换样本质量） | "trade off computation for sample quality" |
| semantically | adv. | 语义上（在语义层面有意义） | "semantically meaningful image interpolation directly in" |
| interpolation | n. | 插值（在两个点之间平滑过渡） | "meaningful image interpolation directly in the" |
| latent space | phr. | 隐空间（低维特征空间） | "image interpolation directly in the latent" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-29 Score-Based Generative Modeling through Stochastic Differential Equations

- [ ] 已读

**中文标题**：基于随机微分方程的基于分数的生成建模

**一句话概括**：提出用随机微分方程（SDE）及其反向过程统一基于分数的生成模型与扩散概率模型，并引入预测-校正框架、等价神经 ODE 与逆问题求解，创下无条件图像生成纪录。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| stochastic | adj. | 随机的；本文指引入随机噪声的微分方程 | "a stochastic differential equation (SDE) that smoothly transforms" |
| transform | v. | 变换、转化；把数据分布平滑地转为噪声分布 | "smoothly transforms a complex data distribution to a known prior" |
| prior distribution | phr. | 先验分布；噪声所在的已知简单分布 | "a known prior distribution by slowly injecting noise" |
| reverse-time | adj. | 反向时间的；从先验分布还原回数据分布的 | "a corresponding reverse-time SDE that transforms the prior" |
| leverage | v. | 利用、借助（已有成果） | "By leveraging advances in score-based generative modeling" |
| estimate | v. | 估计；用神经网络近似计算分数（梯度场） | "we can accurately estimate these scores with neural networks" |
| solver | n. | 求解器；数值求解微分方程的程序 | "use numerical SDE solvers to generate samples" |
| encapsulate | v. | 囊括、涵盖；统一了此前多种方法 | "this framework encapsulates previous approaches in score-based generative" |
| diffusion | n. | 扩散；扩散概率建模，与本文方法并列的生成范式 | "score-based generative modeling and diffusion probabilistic modeling" |
| likelihood | n. | 似然；精确计算数据概率的能力 | "enables exact likelihood computation" |
| inpainting | n. | 图像修复/补全；实验中验证的逆问题任务 | "image inpainting, and colorization" |
| fidelity | n. | 保真度；生成图像与真实图像的接近程度 | "demonstrate high fidelity generation of 1024 x 1024 images" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-30 Flow Matching for Generative Modeling

- [ ] 已读

**中文标题**：用于生成建模的流匹配

**一句话概括**：提出"流匹配"这一免模拟的训练范式，通过回归条件概率路径的向量场训练连续归一化流，比扩散路径训练更快、采样更稳、泛化更好。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| paradigm | n. | 范式；一种新的生成建模思路 | "We introduce a new paradigm for generative modeling" |
| unprecedented | adj. | 前所未有的；此前无法达到的规模 | "allowing us to train CNFs at unprecedented scale" |
| regress | v. | 回归；让网络拟合目标向量场 | "based on regressing vector fields of fixed conditional probability paths" |
| vector field | phr. | 向量场；概率路径上每个点处的速度方向场 | "regressing vector fields of fixed conditional probability paths" |
| subsume | v. | 涵盖、包含；扩散路径只是其特例 | "which subsumes existing diffusion paths as specific instances" |
| robust | adj. | 稳健的；训练更稳定、不易发散 | "results in a more robust and stable alternative" |
| instance | n. | 实例、情形；一种特别值得关注的设置 | "An instance of particular interest is using Optimal Transport" |
| displacement interpolation | phr. | 位移插值；最优传输中连接两个分布的过程 | "Optimal Transport (OT) displacement interpolation to define" |
| generalization | n. | 泛化；在新数据上的表现能力 | "result in better generalization" |
| likelihood | n. | 似然；模型对数据概率的拟合程度 | "in terms of both likelihood and sample quality" |
| off-the-shelf | adj. | 现成的；无需改动即可直接使用 | "using off-the-shelf numerical ODE solvers" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-31 NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis

- [ ] 已读

**中文标题**：NeRF：用神经辐射场表示场景以合成新视角

**一句话概括**：用全连接网络编码连续的 5D 场景函数（位置+视角），配合可微体积渲染，仅凭一组带位姿的照片即可合成照片级真实的新视角。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| synthesize | v. | 合成；从模型生成新视角图像 | "for synthesizing novel views of complex scenes" |
| novel view | phr. | 新视角；相机未拍摄过的观察角度 | "achieves state-of-the-art results for synthesizing novel views" |
| optimize | v. | 优化；训练中不断调整网络参数 | "by optimizing an underlying continuous volumetric scene function" |
| volumetric | adj. | 体（积）的；描述三维空间中连续分布的场景函数 | "by optimizing an underlying continuous volumetric scene function" |
| sparse | adj. | 稀疏的；数量很少的输入照片 | "using a sparse set of input views" |
| coordinate | n. | 坐标；网络输入的 5 维空间-方向表示 | "whose input is a single continuous 5D coordinate" |
| radiance | n. | 辐射度；某方向发出的光能量，决定像素颜色 | "the volume density and view-dependent emitted radiance" |
| query | v. | 查询；沿相机光线采样坐标点 | "We synthesize views by querying 5D coordinates along camera rays" |
| differentiable | adj. | 可微的；可反向传播梯度 | "Because volume rendering is naturally differentiable" |
| camera pose | phr. | 相机位姿；拍摄时的位置与朝向 | "a set of images with known camera poses" |
| photorealistic | adj. | 照片级逼真的 | "render photorealistic novel views of scenes" |
| geometry | n. | 几何；场景的立体形状结构 | "scenes with complicated geometry and appearance" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-32 3D Gaussian Splatting for Real-Time Radiance Field Rendering

- [ ] 已读

**中文标题**：用于实时辐射场渲染的 3D 高斯泼溅

**一句话概括**：用可优化的 3D 高斯表示场景、配合同步的密度控制与可见性感知渲染算法，首次实现 1080p 分辨率下 30fps 以上的实时新视角合成。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| revolutionize | v. | 彻底改变；革新了新视角合成领域 | "have recently revolutionized novel-view synthesis of scenes" |
| inevitably | adv. | 不可避免地；速度与质量难以两全 | "while recent faster methods inevitably trade off speed for quality" |
| trade off | phr. | 权衡、取舍；牺牲一方面换取另一方面 | "inevitably trade off speed for quality" |
| unbounded | adj. | 无界的；指不受边界限制的完整场景 | "For unbounded and complete scenes (rather than isolated objects)" |
| real-time | adj. | 实时的；满足交互式显示帧率 | "no current method can achieve real-time display rates" |
| calibration | n. | 标定；估计相机内外参数的过程 | "sparse points produced during camera calibration" |
| preserve | v. | 保持、保留；继承连续辐射场场的优点 | "preserve desirable properties of continuous volumetric radiance fields" |
| anisotropic | adj. | 各向异性的；沿不同方向尺度不同的协方差 | "notably optimizing anisotropic covariance to achieve an accurate" |
| covariance | n. | 协方差；描述高斯形状的矩阵 | "optimizing anisotropic covariance to achieve an accurate representation" |
| visibility-aware | adj. | 可见性感知的；考虑遮挡关系的渲染 | "we develop a fast visibility-aware rendering algorithm" |
| accelerate | v. | 加速；加快训练与渲染速度 | "both accelerates training and allows realtime rendering" |
| resolution | n. | 分辨率；本文目标为 1080p 高清 | "1080p resolution rendering, no current method" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-33 Adding Conditional Control to Text-to-Image Diffusion Models

- [ ] 已读

**中文标题**：为文本到图像扩散模型添加条件控制（ControlNet）

**一句话概括**：提出 ControlNet 架构，通过"零卷积"锁定预训练扩散模型，向其中注入边缘、深度、姿态等空间条件控制，且小数据集训练同样稳健。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| architecture | n. | 架构；神经网络的整体结构设计 | "a neural network architecture to add spatial conditioning controls" |
| conditioning | n. | 条件控制；给模型额外输入以约束生成 | "to add spatial conditioning controls to large, pretrained" |
| pretrained | adj. | 预训练的；已在海量数据上训练好的 | "to add spatial conditioning controls to large, pretrained" |
| lock | v. | 锁定；保持原模型参数不动 | "ControlNet locks the production-ready large diffusion models" |
| backbone | n. | 主干网络；承担特征提取的主体结构 | "as a strong backbone to learn a diverse set" |
| diverse | adj. | 多样的；类型丰富的条件控制 | "to learn a diverse set of conditional controls" |
| zero convolutions | phr. | 零卷积；参数从零初始化的卷积层 | "zero-initialized convolution layers) that progressively grow the parameters" |
| progressively | adv. | 渐进地；参数随训练逐步增长 | "that progressively grow the parameters from zero" |
| harmful | adj. | 有害的；可能破坏微调的噪声 | "ensure that no harmful noise could affect the finetuning" |
| segmentation | n. | 分割；按语义划分图像区域的输出 | "edges, depth, segmentation, human pose, etc" |
| facilitate | v. | 促进、推动；使更广泛应用成为可能 | "ControlNet may facilitate wider applications to control image" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-34 InstructPix2Pix: Learning to Follow Image Editing Instructions

- [ ] 已读

**中文标题**：InstructPix2Pix：学习遵循图像编辑指令

**一句话概括**：结合 GPT-3 与 Stable Diffusion 自动生成大规模"指令-图像"编辑数据，训练出能按自然语言指令快速编辑任意图像的条件扩散模型。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| edit | v. | 编辑；按指令修改图像内容 | "a method for editing images from human instructions" |
| instruction | n. | 指令；告诉模型做什么的文字描述 | "a written instruction that tells the model what to do" |
| combine | v. | 结合；融合两个模型的知识 | "we combine the knowledge of two large pretrained models" |
| dataset | n. | 数据集；用于训练的图像编辑样本集合 | "to generate a large dataset of image editing examples" |
| conditional | adj. | 条件的；以输入图像和指令为条件的扩散模型 | "Our conditional diffusion model, InstructPix2Pix, is trained" |
| generalize | v. | 泛化；迁移到未见过的真实图像 | "generalizes to real images and user-written instructions at inference" |
| inference | n. | 推理；模型训练后的使用阶段 | "generalizes to real images and user-written instructions at inference" |
| forward pass | phr. | 前向传播；一次网络计算即完成编辑 | "Since it performs edits in the forward pass" |
| inversion | n. | 反演；把图像逆向映射回潜空间的操作 | "does not require per example fine-tuning or inversion" |
| compelling | adj. | 令人信服的；效果很有说服力 | "We show compelling editing results for a diverse collection" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-35 DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation

- [ ] 已读

**中文标题**：DreamBooth：微调文生图扩散模型实现主体驱动生成

**一句话概括**：仅用少量主体照片微调预训练文生图模型，把唯一标识符与具体主体绑定，从而在不同场景、姿态、光照下生成该主体的照片级新图像。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| remarkable | adj. | 显著的；非常突出的进步 | "achieved a remarkable leap in the evolution of AI" |
| leap | n. | 飞跃；质的跨越式进展 | "achieved a remarkable leap in the evolution of AI" |
| prompt | n. | 提示词；描述生成内容的文本 | "high-quality and diverse synthesis of images from a given text prompt" |
| mimic | v. | 模仿；复现主体的外观 | "these models lack the ability to mimic the appearance of subjects" |
| rendition | n. | 呈现、再现；主体在不同情境下的新图像 | "synthesize novel renditions of them in different contexts" |
| personalization | n. | 个性化；让模型学会特定主体 | "a new approach for "personalization" of text-to-image" |
| fine-tune | v. | 微调；在预训练基础上继续训练 | "we fine-tune a pretrained text-to-image model such that" |
| bind | v. | 绑定；把标识符与主体对应起来 | "it learns to bind a unique identifier with that specific subject" |
| identifier | n. | 标识符；指代主体的唯一词元 | "bind a unique identifier with that specific subject" |
| embed | v. | 嵌入；把主体信息编码进模型输出域 | "Once the subject is embedded in the output domain" |
| contextualize | v. | 情境化；把主体放到不同场景中 | "photorealistic images of the subject contextualized in different scenes" |
| recontextualization | n. | 情境重设；在全新场景中重绘主体 | "including subject recontextualization, text-guided view synthesis" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-36 Sigmoid Loss for Language Image Pre-Training

- [ ] 已读

**中文标题**：用于语言-图像预训练的 Sigmoid 损失（SigLIP）

**一句话概括**：提出成对 Sigmoid 损失替代 softmax 对比损失，无需全局归一化即可解耦批大小与损失，小批训练更好、大批可扩到百万，两天内达 84.5% 零样本准确率。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| pairwise | adj. | 成对的；逐对图像-文本计算损失 | "We propose a simple pairwise Sigmoid loss" |
| pre-training | n. | 预训练；在大规模数据上先训练通用表征 | "for Language-Image Pre-training (SigLIP)" |
| contrastive learning | phr. | 对比学习；拉近匹配样本、推开不匹配样本 | "Unlike standard contrastive learning with softmax normalization" |
| normalization | n. | 归一化；把相似度缩放到可比范围 | "Unlike standard contrastive learning with softmax normalization" |
| global | adj. | 全局的；跨整批样本的统计量 | "does not require a global view of the pairwise similarities" |
| similarity | n. | 相似度；图像与文本特征的距离度量 | "a global view of the pairwise similarities" |
| batch size | phr. | 批大小；一次训练用的样本数量 | "the sigmoid loss simultaneously allows further scaling up the batch size" |
| disentanglement | n. | 解耦；使损失不再依赖批大小 | "The disentanglement of the batch size from the loss" |
| negative | adj. | 负样本；与正样本不匹配的配对 | "the impact of examples vs pairs and negative to positive ratio" |
| diminish | v. | 减弱；收益随规模增加而递减 | "the benefits of growing batch size quickly diminish" |
| sufficient | adj. | 足够的；32k 已够用 | "a more reasonable batch size of 32k being sufficient" |
| zero-shot | adj. | 零样本的；未经微调直接测试 | "achieves 84.5% ImageNet zero-shot accuracy in two days" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-37 Is Space-Time Attention All You Need for Video Understanding?

- [ ] 已读

**中文标题**：时空注意力是否足以胜任视频理解？（TimeSformer）

**一句话概括**：提出完全无卷积、仅用时空自注意力的 TimeSformer，"分离注意力"设计使其在动作识别基准上达 SOTA，且训练更快、测试效率更高。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| convolution-free | adj. | 无卷积的；不依赖卷积网络结构 | "We present a convolution-free approach to video classification" |
| self-attention | n. | 自注意力；序列内元素相互关注的机制 | "built exclusively on self-attention over space and time" |
| spatiotemporal | adj. | 时空的；同时涵盖空间与时间的特征 | "enabling spatiotemporal feature learning directly from a sequence" |
| patch | n. | 图像块；从视频帧切分出的局部块 | "from a sequence of frame-level patches" |
| scheme | n. | 方案；不同的注意力组织形式 | "compares different self-attention schemes and suggests that" |
| divided attention | phr. | 分离注意力；时间与空间注意力分开应用 | "where temporal attention and spatial attention are separately applied" |
| benchmark | n. | 基准（数据集）；公认的评测任务 | "state-of-the-art results on several action recognition benchmarks" |
| dramatically | adv. | 大幅地；测试效率显著提高 | "it can achieve dramatically higher test efficiency" |
| efficiency | n. | 效率；单位算力下的处理能力 | "achieve dramatically higher test efficiency (at a small drop in accuracy)" |
| clip | n. | 视频片段；模型处理的视频长度 | "applied to much longer video clips (over one minute long)" |
| radically | adv. | 根本地；设计思路全新的 | "Despite the radically new design, TimeSformer achieves state-of-the-art" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-38 VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training

- [ ] 已读

**中文标题**：VideoMAE：掩码自编码器是自监督视频预训练的高数据效率学习器

**一句话概括**：将掩码自编码器用于视频，提出极高比例（90%~95%）的"视频管"掩码，仅用几千段视频即可预训练出优秀模型，并揭示数据质量重于数量。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| premier | adj. | 顶尖的；最好的性能 | "to achieve premier performance on relatively small datasets" |
| data-efficient | adj. | 数据高效的；少量数据即可学好 | "video masked autoencoders (VideoMAE) are data-efficient learners" |
| self-supervised | adj. | 自监督的；无需人工标注的预训练 | "for self-supervised video pre-training (SSVP)" |
| customized | adj. | 定制的；针对视频专门设计的掩码方式 | "propose customized video tube masking with an extremely high ratio" |
| masking | n. | 掩码；遮盖部分输入迫使模型重建 | "propose customized video tube masking with an extremely high ratio" |
| ratio | n. | 比例；被遮盖视频块所占比重 | "with an extremely high ratio" |
| reconstruction | n. | 重建；从剩余部分还原被遮盖内容 | "makes video reconstruction a more challenging self-supervision task" |
| redundant | adj. | 冗余的；视频相邻帧信息高度重复 | "The temporally redundant video content enables" |
| domain shift | phr. | 域偏移；预训练与目标任务数据分布不同 | "Domain shift between pre-training and target datasets" |
| vanilla | adj. | 基础的；不加额外改动的标准结构 | "our VideoMAE with the vanilla ViT" |
| favorable | adj. | 有利的；仍然取得不错的效果 | "still yields favorable performance of VideoMAE" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-39 VideoMAE V2: Scaling Video Masked Autoencoders with Dual Masking

- [ ] 已读

**中文标题**：VideoMAE V2：以双重掩码扩展视频掩码自编码器

**一句话概括**：提出编码器、解码器各处理一部分 token 的双重掩码策略与渐进式训练范式，成功预训练十亿参数视频 ViT，在 Kinetics 等基准刷新 SOTA。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| foundation model | phr. | 基础模型；可迁移到多种下游任务的大模型 | "for building a powerful foundation model that could well generalize" |
| generalize | v. | 泛化；迁移到多种任务 | "that could well generalize to a variety of downstream tasks" |
| downstream | adj. | 下游的；基于预训练模型的后续任务 | "that could well generalize to a variety of downstream tasks" |
| billion | n. | 十亿；本文模型的参数规模 | "train video foundation models with billions of parameters" |
| dual masking | phr. | 双重掩码；编解码器分别掩码的策略 | "we present a dual masking strategy for efficient pre-training" |
| encoder | n. | 编码器；处理可见 token 的网络部分 | "with an encoder operating on a subset of video tokens" |
| decoder | n. | 解码器；重建被掩码内容的部分 | "a decoder processing another subset of video tokens" |
| subset | n. | 子集；token 的一部分 | "operating on a subset of video tokens" |
| computational cost | phr. | 计算成本；训练消耗的算力 | "can still further reduce the overall computational cost" |
| progressive | adj. | 渐进式的；分阶段推进的训练方式 | "we also use a progressive training paradigm" |
| multi-sourced | adj. | 多来源的；来自不同数据源 | "on a diverse multi-sourced unlabeled dataset" |
| extensively | adv. | 广泛地；在大量下游任务上验证 | "we extensively verify the pre-trained video ViT models" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-40 InternVideo: General Video Foundation Models via Generative and Discriminative Learning

- [ ] 已读

**中文标题**：InternVideo：通过生成式与判别式学习构建通用视频基础模型

**一句话概括**：同时采用掩码视频建模与视频-语言对比学习两种自监督目标，并以可学习方式协调互补表征，在 39 个视频数据集上达到 SOTA。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| foundation model | phr. | 基础模型；支撑多种下游任务的大模型 | "The foundation models have recently shown excellent performance" |
| downstream | adj. | 下游的；在此基础之上的具体任务 | "a variety of downstream tasks in computer vision" |
| dynamic | adj. | 动态的；涉及运动与时间变化的理解 | "limited for dynamic and complex video-level understanding tasks" |
| generative | adj. | 生成式的；以重建等目标学习表征 | "taking advantage of both generative and discriminative" |
| discriminative | adj. | 判别式的；以区分正负样本学习表征 | "both generative and discriminative self-supervised video learning" |
| contrastive learning | phr. | 对比学习；拉近匹配视频-文本对 | "masked video modeling and video-language contrastive learning" |
| complementary | adj. | 互补的；两种方法各有所长 | "these two complementary frameworks in a learnable manner" |
| coordinate | v. | 协调；把两种表征按需融合 | "selectively coordinates video representations of these two complementary" |
| boost | v. | 提升；增强各类视频应用效果 | "to boost various video applications" |
| bells and whistles | phr. | 花哨的附加功能；指复杂技巧 | "Without bells and whistles, InternVideo achieves state-of-the-art" |
| alignment | n. | 对齐；视频与语言语义的匹配 | "video action recognition/detection, video-language alignment" |
| benchmark | n. | 基准测试；权威评测数据集 | "on the challenging Kinetics-400 and Something-Something V2 benchmarks" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-41 Video-LLaVA: Learning United Visual Representation by Alignment Before Projection

- [ ] 已读

**中文标题**：Video-LLaVA：在投影前先对齐以学习统一视觉表征

**一句话概括**：指出图像与视频因缺乏统一词元化而在投影前错位，主张先把视觉表征统一到语言特征空间，再用图文视频混合数据训练出彼此增强的统一 LVLM。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| enhance | v. | 提升、增强；改善下游任务表现 | "has enhanced the performance of various downstream tasks" |
| downstream | adj. | 下游的；基于大模型的具体任务 | "has enhanced the performance of various downstream tasks" |
| tokenization | n. | 词元化；把输入切成统一单元 | "due to the lack of unified tokenization for images and videos" |
| misalignment | n. | 错位；图像与视频表征不对齐的问题 | "namely misalignment before projection" |
| projection | n. | 投影；把视觉特征映射到语言空间的层 | "misalignment before projection" |
| unify | v. | 统一；把视觉表示纳入同一特征空间 | "we unify visual representation into the language feature space" |
| baseline | n. | 基线（模型）；作为基准的简单模型 | "we establish a simple but robust LVLM baseline" |
| toolkit | n. | 工具包；评测用的框架集合 | "4 image benchmark toolkits" |
| outperform | v. | 超越；性能优于对比模型 | "our Video-LLaVA also outperforms Video-ChatGPT by 5.8%" |
| notably | adv. | 值得注意的是；引出重要结论 | "Notably, extensive experiments demonstrate that Video-LLaVA mutually benefits" |
| modest | adj. | 适度的；谦虚而有价值的见解 | "provide modest insights into the multi-modal inputs for the LLM" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-42 LLaVA-Video: Video Instruction Tuning With Synthetic Data

- [ ] 已读

**中文标题**：LLaVA-Video：用合成数据进行视频指令微调

**一句话概括**：为解决网络原始视频数据难整理的问题，构建高质量合成视频指令数据集 LLaVA-Video-178K，训练出的视频多模态模型在多个基准上表现强劲。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| hinder | v. | 阻碍；拖慢了模型发展 | "has been hindered by the difficulty of curating large amounts" |
| curate | v. | 整理、筛选；从海量数据中挑选高质量样本 | "has been hindered by the difficulty of curating large amounts" |
| synthetic | adj. | 合成的；由程序生成的训练数据 | "creating a high-quality synthetic dataset specifically for video" |
| instruction-following | adj. | 指令遵循的；按指令完成任务的 | "specifically for video instruction-following" |
| captioning | n. | 描述生成；为视频写详细文字说明 | "This dataset includes key tasks such as detailed captioning" |
| open-ended | adj. | 开放式的；答案不固定的问答 | "open-ended question-answering (QA), and multiple-choice QA" |
| tuning | n. | 调优；在预训练基础上继续训练 | "in combination with existing visual instruction tuning data" |
| benchmark | n. | 基准测试；权威评测数据集 | "achieves strong performance across various video benchmarks" |
| effectiveness | n. | 有效性；数据确实起作用 | "highlighting the effectiveness of our dataset" |
| pipeline | n. | 流程/管线；数据生成的处理链路 | "we plan to release the dataset, its generation pipeline" |
| checkpoint | n. | 检查点；训练得到的模型权重文件 | "and the model checkpoints" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-43 Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution

- [ ] 已读

**中文标题**：Qwen2-VL：增强视觉语言模型对任意分辨率世界的感知

**一句话概括**：提出朴素动态分辨率机制与多模态旋转位置编码，让模型按分辨率自适应切分视觉词元，并探究 LVLM 缩放定律，72B 版达到 GPT-4o 同级水平。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| upgrade | n. | 升级；对旧版模型的全面改进 | "an advanced upgrade of the previous Qwen-VL models" |
| redefine | v. | 重新定义；抛弃旧有处理方式 | "that redefines the conventional predetermined-resolution approach" |
| conventional | adj. | 传统的；此前普遍采用的 | "that redefines the conventional predetermined-resolution approach" |
| predetermined | adj. | 预设的；事先固定不变的 | "the conventional predetermined-resolution approach" |
| resolution | n. | 分辨率；图像的像素密度 | "process images of varying resolutions into different numbers" |
| mechanism | n. | 机制；实现某功能的具体方案 | "the Naive Dynamic Resolution mechanism" |
| token | n. | 词元；模型处理的基本单元 | "into different numbers of visual tokens" |
| perceptual | adj. | 感知的；与人类视觉感知一致 | "closely aligning with human perceptual processes" |
| fusion | n. | 融合；把位置信息整合进表示 | "facilitating the effective fusion of positional information" |
| scaling laws | phr. | 缩放定律；性能随规模增长的规律 | "investigates the scaling laws for large vision-language models" |
| comparable | adj. | 相当的；与顶尖模型水平接近 | "achieves results comparable to leading models such as GPT-4o" |
| outperform | v. | 优于；表现超过其他通用模型 | "outperforming other generalist models" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-44 Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs

- [ ] 已读

**中文标题**：Cambrian-1：对多模态大语言模型的完全开源、以视觉为中心的探索

**一句话概括**：以视觉为中心系统评估 20 多种视觉编码器，提出空间视觉聚合器（SVA）与视觉中心基准 CV-Bench，并开源全套数据、代码与训练配方。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| vision-centric | adj. | 以视觉为中心的；优先设计视觉组件 | "a family of multimodal LLMs (MLLMs) designed with a vision-centric approach" |
| disconnected | adj. | 脱节的；视觉组件研究与表征学习脱钩 | "often insufficiently explored and disconnected from visual representation learning" |
| grounding | n. | 锚定；模型对真实世界视觉信息的准确对应 | "This gap hinders accurate sensory grounding in real-world scenarios" |
| sensory | adj. | 感知的；来自视觉等感官的信息 | "accurate sensory grounding in real-world scenarios" |
| encoder | n. | 编码器；把图像转为特征向量的网络 | "based on experiments with over 20 vision encoders" |
| benchmark | n. | 基准测试；评测模型的权威任务 | "We critically examine existing MLLM benchmarks" |
| consolidate | v. | 整合；汇总多个任务的结果 | "the difficulties involved in consolidating and interpreting results" |
| interpret | v. | 解读；理解评测结果的含义 | "consolidating and interpreting results from various tasks" |
| aggregator | n. | 聚合器；把多尺度视觉特征合并的模块 | "we propose the Spatial Vision Aggregator (SVA)" |
| integrate | v. | 整合；把视觉特征接入语言模型 | "integrates high-resolution vision features with LLMs while reducing" |
| curation | n. | 整理、策划；挑选高质量训练数据 | "the curation of high-quality visual instruction-tuning data" |
| cookbook | n. | 手册/指南；可复现的完整方案集 | "serves as a comprehensive, open cookbook for instruction-tuned MLLMs" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-45 xGen-MM (BLIP-3): A Family of Open Large Multimodal Models

- [ ] 已读

**中文标题**：xGen-MM（BLIP-3）：一系列开源的大型多模态模型

**一句话概括**：发布包含精挑数据集、训练配方、模型架构与 4B/14B 模型的完整开源 LMM 框架，模型能理解交错的图文输入，性能在同类开源模型中具竞争力。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| framework | n. | 框架；支撑模型开发的整套体系 | "an open framework for developing Large Multimodal Models (LMMs)" |
| meticulously | adv. | 一丝不苟地；非常精心地整理 | "The framework comprises meticulously curated datasets" |
| curated | adj. | 精心整理的；经过筛选的高质量数据 | "meticulously curated datasets" |
| recipe | n. | 配方/方案；可复现的训练流程 | "a training recipe, model architectures, and a resulting suite" |
| suite | n. | 系列；一组配套的模型 | "a resulting suite of LMMs" |
| rigorous | adj. | 严格的；全面规范的评测 | "Our models undergo rigorous evaluation across a range of tasks" |
| evaluation | n. | 评估；检验模型性能的过程 | "undergo rigorous evaluation across a range of tasks" |
| benchmark | n. | 基准测试；标准评测数据集 | "including both single and multi-image benchmarks" |
| interleaved | adj. | 交错的；图文交替混合的输入 | "the ability to comprehend interleaved image-text inputs" |
| comprehend | v. | 理解；把握图文内容含义 | "the ability to comprehend interleaved image-text inputs" |
| open-source | v. | 开源；公开代码与模型 | "will be open-sourced to better support the research community" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-46 Aria: An Open Multimodal Native Mixture-of-Experts Model

- [ ] 已读

**中文标题**：Aria：一个开源的多模态原生专家混合模型

**一句话概括**：发布开源多模态原生 MoE 模型，每个视觉/文本词元仅激活约 3.5~3.9B 参数，经四阶段预训练，性能超越同规模闭源竞品。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| modality | n. | 模态；信息的呈现形式（文本、图像等） | "Information comes in diverse modalities" |
| multimodal | adj. | 多模态的；同时处理多种信息形式 | "Multimodal native AI models are essential to integrate" |
| proprietary | adj. | 专有的、闭源的；不公开的模型 | "While proprietary multimodal native models exist" |
| openness | n. | 开放性；开源带来的透明度 | "their lack of openness imposes obstacles for adoptions" |
| obstacle | n. | 障碍；阻碍采用的因素 | "their lack of openness imposes obstacles for adoptions" |
| adoption | n. | 采用；把模型用在实际场景 | "imposes obstacles for adoptions" |
| adaptation | n. | 适配、改造；针对特定需求微调 | "let alone adaptations" |
| mixture-of-experts | n. | 专家混合；每次只激活部分参数的架构 | "Aria is a mixture-of-expert model with 3.9B and 3.5B activated" |
| activated parameters | phr. | 激活参数；处理单个词元实际用到的参数 | "activated parameters per visual token and text token" |
| outperform | v. | 超越；性能超过对比模型 | "It outperforms Pixtral-12B and Llama3.2-11B" |
| pipeline | n. | 流程；分阶段完成的训练计划 | "We pre-train Aria from scratch following a 4-stage pipeline" |
| progressively | adv. | 逐步地；分阶段赋予能力 | "which progressively equips the model with strong capabilities" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-47 AnyGPT: Unified Multimodal LLM with Discrete Sequence Modeling

- [ ] 已读

**中文标题**：AnyGPT：基于离散序列建模的统一多模态大语言模型

**一句话概括**：用离散表示统一语音、文本、图像、音乐等模态，不改动 LLM 架构，仅靠数据级预处理即可实现任意模态组合的输入输出对话。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| any-to-any | adj. | 任意到任意的；任意模态输入到任意模态输出 | "an any-to-any multimodal language model that utilizes discrete representations" |
| discrete | adj. | 离散的；用有限符号序列表示连续信号 | "utilizes discrete representations for the unified processing of various modalities" |
| representation | n. | 表示；数据在模型中的编码形式 | "utilizes discrete representations" |
| unified | adj. | 统一的；用同一框架处理所有模态 | "for the unified processing of various modalities" |
| modality | n. | 模态；信息呈现形式 | "including speech, text, images, and music" |
| architecture | n. | 架构；模型整体结构 | "without any alterations to the current large language model (LLM) architecture" |
| paradigm | n. | 范式；训练方式 | "or training paradigms" |
| seamless | adj. | 无缝的；平滑自然的接入 | "facilitating the seamless integration of new modalities into LLMs" |
| akin to | phr. | 类似于；如同……一样 | "akin to the incorporation of new languages" |
| alignment | n. | 对齐；让多模态表示相互对应 | "a multimodal text-centric dataset for multimodal alignment pre-training" |
| synthesize | v. | 合成；用生成模型制造数据 | "we synthesize the first large-scale any-to-any multimodal instruction dataset" |
| interweave | v. | 交织；多种模态穿插在对话中 | "conversations that intricately interweave various modalities" |
| arbitrary | adj. | 任意的；不受限制的组合 | "handle arbitrary combinations of multimodal inputs and outputs" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-48 Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action

- [ ] 已读

**中文标题**：Unified-IO 2：用视觉、语言、音频与动作扩展自回归多模态模型

**一句话概括**：首个能理解并生成图像、文本、音频与动作的自回归多模态模型，把各模态统一词元化到共享语义空间，用单一模型在 35+ 基准上取得 SOTA。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| autoregressive | adj. | 自回归的；逐个预测下一词元的生成方式 | "the first autoregressive multimodal model that is capable" |
| tokenize | v. | 词元化；把各模态切成统一单元 | "we tokenize inputs and outputs" |
| shared semantic space | phr. | 共享语义空间；各模态共同的特征表示空间 | "into a shared semantic space and then process them" |
| encoder-decoder | n. | 编码器-解码器；编码输入再解码输出的结构 | "with a single encoder-decoder transformer model" |
| stabilize | v. | 稳定；防止训练发散 | "we propose various architectural improvements to stabilize model training" |
| corpus | n. | 语料库；大规模训练数据集合 | "on a large multimodal pre-training corpus from diverse sources" |
| mixture of denoisers | phr. | 去噪器混合；组合多种去噪目标的训练目标 | "with a multimodal mixture of denoisers objective" |
| expansive | adj. | 广泛的；涵盖大量技能 | "To learn an expansive set of skills" |
| ensemble | n. | 集成；多个数据集构成的组合 | "we construct and finetune on an ensemble of 120 datasets" |
| augmentation | n. | 数据增强；对样本做变换扩充 | "with prompts and augmentations" |
| benchmark | n. | 基准测试；权威评测 | "state-of-the-art performance on the GRIT benchmark" |
| robotic manipulation | phr. | 机器人操作；控制机械臂等动作任务 | "video and audio understanding, and robotic manipulation" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-49 Retrieval-Augmented Multimodal Language Modeling

- [ ] 已读

**中文标题**：检索增强的多模态语言建模（RA-CM3）

**一句话概括**：让生成模型从外部记忆检索相关图文而非把知识全存进参数，训练算力不到 DALL-E 的 30%，却在图文生成任务上全面超越。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| remarkable | adj. | 显著的；进展非常突出 | "have achieved remarkable progress in text-to-image and image-to-text generation" |
| store | v. | 存储；把知识写进模型参数 | "these models store all learned knowledge (e.g., the appearance" |
| capture | v. | 获取、捕捉；把知识学会 | "requiring increasingly larger models and training data to capture more knowledge" |
| scalable | adj. | 可扩展的；随规模增大仍高效 | "in a more scalable and modular way" |
| modular | adj. | 模块化的；各部分可独立更换 | "in a more scalable and modular way" |
| retrieval-augmented | adj. | 检索增强的；生成前先检索相关信息 | "we propose a retrieval-augmented multimodal model" |
| retriever | n. | 检索器；从外部库找出相关样本的模块 | "text and images fetched by a retriever from external memory" |
| external memory | phr. | 外部记忆；模型之外的存储（如网页文档） | "from external memory (e.g., documents on the web)" |
| outperform | v. | 超越；性能优于基线 | "RA-CM3 significantly outperforms baseline multimodal models such as DALL-E" |
| compute | n. | 算力；训练消耗的计算资源 | "while requiring much less compute for training" |
| faithful | adj. | 忠实的；忠实还原真实知识的生成 | "such as faithful image generation" |
| in-context learning | phr. | 上下文学习；从示例中直接学习新任务 | "multimodal in-context learning (e.g., image generation from demonstrations)" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-50 VideoPoet: A Large Language Model for Zero-Shot Video Generation

- [ ] 已读

**中文标题**：VideoPoet：用于零样本视频生成的大语言模型

**一句话概括**：采用仅解码器 Transformer 架构、按 LLM 两阶段流程训练，统一处理图像、视频、文本与音频，实现零样本高质量视频（含运动）生成。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| synthesize | v. | 合成；生成视频内容 | "a language model capable of synthesizing high-quality video" |
| conditioning signals | phr. | 条件信号；控制生成内容的输入（如文本、图像） | "from a large variety of conditioning signals" |
| decoder-only | adj. | 仅解码器的；没有编码器的 Transformer 结构 | "employs a decoder-only transformer architecture that processes multimodal inputs" |
| protocol | n. | 流程/协议；标准训练步骤 | "The training protocol follows that of Large Language Models (LLMs)" |
| pretraining | n. | 预训练；训练的第一阶段 | "consisting of two stages: pretraining and task-specific adaptation" |
| adaptation | n. | 适配；针对具体任务调整模型 | "pretraining and task-specific adaptation" |
| objective | n. | 目标（函数）；训练要优化的损失 | "a mixture of multimodal generative objectives within an autoregressive Transformer" |
| autoregressive | adj. | 自回归的；逐 token 预测的框架 | "within an autoregressive Transformer framework" |
| empirical | adj. | 实证的；基于实验结果的 | "We present empirical results demonstrating the model's state-of-the-art" |
| zero-shot | adj. | 零样本的；无需任务数据即可生成 | "capabilities in zero-shot video generation" |
| high-fidelity | adj. | 高保真的；运动细节高度真实 | "ability to generate high-fidelity motions" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-51 CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer

- [ ] 已读

**中文标题**：CogVideoX：带专家 Transformer 的文本到视频扩散模型

**一句话概括**：基于扩散 Transformer 的 10 秒长视频生成模型，用 3D VAE 时空压缩、专家自适应 LayerNorm 深度融合文视频模态，配多分辨率帧打包与数据处理流水线。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| aligned | adj. | 对齐的；视频内容与文本提示一致 | "can generate 10-second continuous videos aligned with text prompt" |
| frame rate | phr. | 帧率；每秒播放的画面数 | "with a frame rate of 16 fps" |
| resolution | n. | 分辨率；画面的像素尺寸 | "resolution of 768 * 1360 pixels" |
| narrative | n. | 叙事；连贯的故事情节 | "generate videos with coherent narratives based on text" |
| coherent | adj. | 连贯的；前后一致不跳变 | "generate videos with coherent narratives based on text" |
| compress | v. | 压缩；减少视频的数据量 | "to compress videos along both spatial and temporal dimensions" |
| temporal | adj. | 时间的；沿时间轴的信息维度 | "along both spatial and temporal dimensions" |
| fidelity | n. | 保真度；还原真实细节的程度 | "to improve both compression rate and video fidelity" |
| fusion | n. | 融合；两种模态信息的深度结合 | "to facilitate the deep fusion between the two modalities" |
| progressive | adj. | 渐进式的；分阶段逐步训练 | "by employing a progressive training and multi-resolution frame pack technique" |
| captioning | n. | 描述生成；给视频写文字说明 | "a video captioning method, greatly contributing to the generation quality" |
| metric | n. | 指标；量化评测的标准 | "across both multiple machine metrics and human evaluations" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-52 Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets

- [ ] 已读

**中文标题**：Stable Video Diffusion：把潜视频扩散模型扩展到大规模数据集

**一句话概括**：系统梳理文生视频训练三阶段并给出数据整理流程，训练出可与闭源模型竞争的视频 LDM，其基座还是图像到视频、多视角生成的有力基础。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| latent | adj. | 潜（空间）的；在压缩的低维空间中扩散 | "a latent video diffusion model for high-resolution, state-of-the-art" |
| insert | v. | 插入；把时间层加进图像模型 | "by inserting temporal layers and finetuning them" |
| finetune | v. | 微调；在小数据上继续训练 | "inserting temporal layers and finetuning them" |
| curate | v. | 整理；筛选高质量训练数据 | "the field has yet to agree on a unified strategy" |
| unified | adj. | 统一的；大家公认一致的方案 | "the field has yet to agree on a unified strategy" |
| identify | v. | 识别、确定；找出关键阶段 | "we identify and evaluate three different stages" |
| necessity | n. | 必要性；不可或缺的条件 | "we demonstrate the necessity of a well-curated pretraining dataset" |
| systematic | adj. | 系统性的；成体系的数据整理 | "present a systematic curation process to train a strong base model" |
| filtering | n. | 过滤；剔除低质量数据 | "including captioning and filtering strategies" |
| competitive | adj. | 有竞争力的；不输于闭源方案 | "train a text-to-video model that is competitive" |
| downstream | adj. | 下游的；后续应用任务 | "a powerful motion representation for downstream tasks" |
| feedforward | adj. | 前馈的；一次前向计算直接出结果 | "jointly generates multiple views of objects in a feedforward fashion" |
| compute budget | phr. | 计算预算；可投入的算力总量 | "at a fraction of their compute budget" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-53 AnimateDiff: Animate Your Personalized Text-to-Image Diffusion Models without Specific Tuning

- [ ] 已读

**中文标题**：AnimateDiff：无需专门微调即可让个性化文生图模型动起来

**一句话概括**：训练一次即插即用的运动模块，可无缝嵌入任何基于同一基座的个性化文生图模型，让其生成时间上平滑的动画；MotionLoRA 再以低成本适配新运动模式。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| advance | n. | 进展；技术的发展 | "With the advance of text-to-image (T2I) diffusion models" |
| personalization | n. | 个性化；让模型学会特定主体 | "personalization techniques such as DreamBooth and LoRA" |
| manifest | v. | 实现、展现；把想象变成图像 | "everyone can manifest their imagination into high-quality images" |
| affordable | adj. | 负担得起的；成本可接受 | "at an affordable cost" |
| motion dynamics | phr. | 运动动态；物体随时间运动的信息 | "adding motion dynamics to existing high-quality personalized T2Is" |
| open challenge | phr. | 未解决的难题；尚待攻克的问题 | "remains an open challenge" |
| plug-and-play | adj. | 即插即用的；无需改动即可接入 | "a plug-and-play motion module that can be trained once" |
| seamlessly | adv. | 无缝地；平滑自然地集成 | "seamlessly integrated into any personalized T2Is originating" |
| transferable | adj. | 可迁移的；能泛化到其他模型 | "the motion module effectively learns transferable motion priors from real-world videos" |
| lightweight | adj. | 轻量级的；参数量小、成本低 | "MotionLoRA, a lightweight fine-tuning technique for AnimateDiff" |
| adapt | v. | 适配；调整以适应新需求 | "to adapt to new motion patterns, such as different shot types" |
| preserve | v. | 保持；不损失原有质量 | "generate temporally smooth animation clips while preserving the visual quality" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-54 HunyuanVideo: A Systematic Framework For Large Video Generative Models

- [ ] 已读

**中文标题**：HunyuanVideo：面向大型视频生成模型的系统化框架

**一句话概括**：开源 130 亿参数视频基础模型，整合数据整理、架构设计、渐进式扩规模训练与高效基础设施，性能超越 Runway Gen-3 等领先闭源模型。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| advancement | n. | 进展；技术的进步 | "Recent advancements in video generation have significantly impacted" |
| impact | v. | 影响；对生活产生作用 | "have significantly impacted daily life for both individuals" |
| closed-source | adj. | 闭源的；不公开代码的 | "the leading video generation models remain closed-source" |
| performance gap | phr. | 性能差距；业界与公众可用模型间的差距 | "a notable performance gap between industry capabilities" |
| innovative | adj. | 创新的；有开创性的 | "we introduce HunyuanVideo, an innovative open-source video foundation model" |
| comprehensive | adj. | 全面的；覆盖完整环节 | "encompasses a comprehensive framework that integrates several key elements" |
| curation | n. | 整理；数据筛选工作 | "including data curation, advanced architectural design, progressive model scaling" |
| infrastructure | n. | 基础设施；支撑训练与推理的软硬件体系 | "an efficient infrastructure tailored for large-scale model training and inference" |
| inference | n. | 推理；用训练好的模型做预测 | "large-scale model training and inference" |
| targeted | adj. | 有针对性的；专门设计的方案 | "we implemented a series of targeted designs to ensure" |
| filming techniques | phr. | 拍摄技法；镜头语言等高级效果 | "and advanced filming techniques" |
| outperform | v. | 超越；性能超过以往最优模型 | "HunyuanVideo outperforms previous state-of-the-art models" |
| bridge the gap | phr. | 弥合差距；拉近两个群体间的距离 | "we aim to bridge the gap between closed-source and open-source communities" |
| empower | v. | 赋能；给予尝试创新的能力 | "This initiative will empower individuals within the community" |
| foster | v. | 促进；培育健康生态 | "fostering a more dynamic and vibrant video generation ecosystem" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-55 Wan: Open and Advanced Large-Scale Video Generative Models

- [ ] 已读

**中文标题**：Wan：开源且先进的大规模视频生成模型

**一句话概括**：开源 1.3B/14B 双规格视频基础模型系列，覆盖图像转视频、指令编辑等八类任务，14B 版在多基准上超越开源与商业模型，1.3B 版仅需 8.19GB 显存。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| suite | n. | 系列；一组配套模型 | "a comprehensive and open suite of video foundation models" |
| push the boundaries | phr. | 突破边界；把能力上限再提高 | "designed to push the boundaries of video generation" |
| paradigm | n. | 范式；主流技术路线 | "Built upon the mainstream diffusion transformer paradigm" |
| innovation | n. | 创新；新的技术方案 | "through a series of innovations" |
| scalable | adj. | 可扩展的；能随数据规模增长的 | "our novel VAE, scalable pre-training strategies" |
| curation | n. | 整理；大规模数据筛选 | "large-scale data curation, and automated evaluation metrics" |
| automated | adj. | 自动化的；机器自动完成的评测 | "and automated evaluation metrics" |
| versatility | n. | 通用性、多面性；适用多种任务的能力 | "enhance the model's performance and versatility" |
| scaling laws | phr. | 缩放定律；性能随数据与规模增长的规律 | "demonstrates the scaling laws of video generation with respect" |
| outperform | v. | 超越；表现优于对比对象 | "It consistently outperforms the existing open-source models" |
| commercial | adj. | 商业的；商用的解决方案 | "state-of-the-art commercial solutions across multiple internal and external benchmarks" |
| superiority | n. | 优越性；明显更优的表现 | "demonstrating a clear and significant performance superiority" |
| consumer-grade | adj. | 消费级的；普通用户显卡可运行 | "requiring only 8.19 GB VRAM, making it compatible" |
| foster | v. | 促进；推动社区发展 | "with the goal of fostering the growth of the video generation community" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 02-56 Movie Gen: A Cast of Media Foundation Models

- [ ] 已读

**中文标题**：Movie Gen：一组媒体基础模型

**一句话概括**：发布能生成 1080p 高清视频与同步音频的媒体基础模型系列，30B 参数 Transformer 支持 73K 视频词元上下文，在多任务上刷新 SOTA。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| cast | n. | 阵容；一组配合使用的模型 | "a cast of foundation models that generates high-quality" |
| aspect ratio | phr. | 宽高比；画面的长宽比例 | "with different aspect ratios and synchronized audio" |
| synchronized | adj. | 同步的；与画面时间对齐的音频 | "with different aspect ratios and synchronized audio" |
| personalized | adj. | 个性化的；针对特定用户生成 | "generation of personalized videos based on a user's image" |
| state-of-the-art | n. | 最先进水平；当前最佳成绩 | "Our models set a new state-of-the-art on multiple tasks" |
| synthesis | n. | 合成；从条件生成内容 | "text-to-video synthesis, video personalization, video editing" |
| context length | phr. | 上下文长度；模型一次能处理的序列规模 | "a 30B parameter transformer trained with a maximum context length" |
| innovation | n. | 创新；技术上的新设计 | "We show multiple technical innovations and simplifications" |
| latent space | phr. | 潜空间；压缩表示所在的空间 | "on the architecture, latent spaces, training objectives and recipes" |
| recipe | n. | 配方/方案；训练流程的具体安排 | "training objectives and recipes" |
| curation | n. | 整理；训练数据筛选 | "data curation, evaluation protocols, parallelization techniques" |
| protocol | n. | 方案；评测的标准流程 | "data curation, evaluation protocols, parallelization techniques" |
| parallelization | n. | 并行化；把训练分布到多设备 | "parallelization techniques" |
| reap the benefits | phr. | 收获收益；享受规模化带来的好处 | "that allow us to reap the benefits of scaling pre-training data" |
| accelerate | v. | 加速；加快领域进展 | "We hope this paper helps the research community to accelerate progress" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

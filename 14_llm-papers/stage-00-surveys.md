---
type: paper-vocabulary
stage: 0
title: "阶段 0 · 总览与综述 论文词汇"
tags: [topic/paper, skill/reading, status/learning]
created: 2026-10-24
---

# 阶段 0 · 总览与综述 论文词汇

> 7 篇 · 84 个词条。读前扫词 2 分钟；读后遮住中文，用 abstract 片段自测，再用 5 个词复述 60 秒。
> 返回 [[14_llm-papers/_index|LLM 论文阅读]]；配套 [[14_llm-papers/reading-workflow|阅读与词汇流程]]。

## 00-00 Attention Is All You Need

- [ ] 已读

**中文标题**：《注意力即一切》

**一句话概括**：提出完全基于注意力机制的 Transformer 架构，摒弃循环与卷积网络，在机器翻译等任务上取得当时最先进的效果，成为后续几乎所有大语言模型的基石。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| dominant | adj. | 主导的、占支配地位的（本文指当前主流的序列转导模型） | "The dominant sequence transduction models are based on" |
| transduction | n. | 转导：把输入序列整体转换为输出序列的任务（如机器翻译） | "The dominant sequence transduction models are based on" |
| recurrent | adj. | 循环的（指 RNN 这类按时间步循环处理序列的网络） | "complex recurrent or convolutional neural networks in" |
| configuration | n. | 结构、配置（encoder-decoder configuration 即编码器-解码器架构） | "neural networks in an encoder-decoder configuration" |
| mechanism | n. | 机制（attention mechanism 注意力机制：让模型聚焦输入中重要部分的机制） | "the encoder and decoder through an attention mechanism" |
| propose | v. | 提出（学术写作高频词，指提出新的方法/架构） | "We propose a new simple network architecture" |
| solely | adv. | 仅仅、完全（based solely on 即"完全基于"） | "based solely on attention mechanisms" |
| dispensing with | phr. | 摒弃、省去（dispense with 意为不再需要某事物） | "dispensing with recurrence and convolutions entirely" |
| parallelizable | adj. | 可并行计算的（本文强调 Transformer 比 RNN 更易于并行训练） | "superior in quality while being more parallelizable" |
| ensemble | n. | 集成模型（多个模型组合起来投票/平均得到的结果） | "including ensembles by over 2 BLEU" |
| state-of-the-art | adj. | 最先进的、当前最优的（常缩写为 SOTA） | "a new single-model state-of-the-art BLEU score" |
| constituency parsing | phr. | 成分句法分析（把句子按短语结构解析成语法树的任务） | "applying it successfully to English constituency parsing" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 00-01 A Survey of Large Language Models

- [ ] 已读

**中文标题**：《大语言模型综述》

**一句话概括**：综述大语言模型（LLM）的背景与关键技术，围绕预训练、适配调优、利用与能力评估四个方面总结最新进展，并讨论可用资源与开放问题。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| essentially | adv. | 本质上（用于陈述事物的根本性质） | "Language is essentially a complex, intricate system" |
| intricate | adj. | 错综复杂的（形容语言系统结构精细、层次繁多） | "Language is essentially a complex, intricate system" |
| governed by | phr. | 受……支配、受……制约（be governed by 遵循某种规则） | "human expressions governed by grammatical rules" |
| pose | v. | 构成、带来（pose a challenge 构成挑战，学术高频搭配） | "It poses a significant challenge to develop" |
| comprehend | v. | 理解、领会（比 understand 更正式，本文指让 AI 理解语言） | "for comprehending and grasping a language" |
| corpora | n. | 语料库（corpus 的复数，指大规模文本数据集） | "pre-training Transformer models over large-scale corpora" |
| scaling | n. | 规模化（model scaling 指把模型变大，从而带来性能提升） | "model scaling can lead to performance improvement" |
| exceed | v. | 超过、超出（参数规模超过某个阈值后能力突增） | "when the parameter scale exceeds a certain level" |
| discriminate | v. | 区分、辨别（discriminate the difference 识别差异） | "To discriminate the difference in parameter scale" |
| coined | v. | 创造（新词/术语）（coin the term 为……造词） | "the research community has coined the term" |
| remarkable | adj. | 显著的、非凡的（remarkable progress 显著进展） | "a remarkable progress is the launch of ChatGPT" |
| revolutionize | v. | 彻底改变、变革（revolutionize the way 颠覆……的方式） | "which would revolutionize the way how we" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 00-02 The Dawn of LMMs: Preliminary Explorations with GPT-4V(ision)

- [ ] 已读

**中文标题**：多模态大模型之黎明：GPT-4V(ision) 初步探索

**一句话概括**：对 GPT-4V(ision) 进行系统的初步探索，通过精心设计的定性样本揭示其处理任意交错多模态输入的强大能力与通用性，并提出视觉指代提示等新的人机交互方式。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| dawn | n. | 黎明、开端（the dawn of LMMs 指多模态大模型时代刚刚开启） | "The Dawn of LMMs: Preliminary Explorations with" |
| preliminary | adj. | 初步的、预备的（preliminary explorations 探索性研究） | "The Dawn of LMMs: Preliminary Explorations with" |
| extend | v. | 扩展（LMMs 在 LLM 基础上扩展出视觉等多感官能力） | "Large multimodal models (LMMs) extend large language" |
| multi-sensory | adj. | 多感官的（能处理视觉、文本等多种感官信息） | "extend large language models (LLMs) with multi-sensory skills" |
| generic | adj. | 通用的（generic intelligence 通用智能；本文强调能力具有通用性） | "to achieve stronger generic intelligence" |
| probe | v. | 探查、检验（用精心设计的测试样本检验能力质量） | "test samples to probe the quality and genericity" |
| curate | v. | 精心挑选、策划（curate a collection 系统地挑选并组织样本） | "we curate and organize a collection of" |
| span | v. | 涵盖、跨越（样本跨越多种领域与任务） | "spanning a variety of domains and tasks" |
| unprecedented | adj. | 前所未有的（GPT-4V 处理任意交错多模态输入的能力） | "GPT-4V's unprecedented ability in processing arbitrarily" |
| interleaved | adj. | 交错的、穿插的（文本与图像任意穿插组合的输入） | "processing arbitrarily interleaved multimodal inputs and" |
| generalist | n. | 通才（multimodal generalist system 能处理多种任务的多模态通才系统） | "make GPT-4V a powerful multimodal generalist system" |
| visual referring prompting | phr. | 视觉指代提示（通过在输入图像上画标记来指示模型关注的对象） | "such as visual referring prompting" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 00-03 A Survey on Multimodal Large Language Models

- [ ] 已读

**中文标题**：《多模态大语言模型综述》

**一句话概括**：综述以 GPT-4V 为代表的多模态大语言模型（MLLM），梳理其基本形式、架构、训练与评估，并介绍多模态幻觉与 ICL、CoT 等扩展技术及未来方向。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| multimodal | adj. | 多模态的（同时处理文本、图像、音频等多种信息形式） | "Multimodal Large Language Model (MLLM) represented by" |
| hotspot | n. | 热点（research hotspot 研究热点） | "has been a new rising research hotspot" |
| emergent | adj. | 涌现的（emergent capabilities 指模型规模增大后"涌现"出的新能力） | "The surprising emergent capabilities of MLLM" |
| reasoning | n. | 推理（math reasoning 数学推理；本文指不依赖 OCR 直接解题） | "OCR-free math reasoning, are rare in traditional" |
| endeavor | v. | 努力、竭力（学术界与工业界都努力去做） | "both academia and industry have endeavored to" |
| trace | v. | 追溯、梳理（trace and summarize 梳理并总结发展脉络） | "we aim to trace and summarize the recent" |
| formulation | n. | 形式化表述、基本定义（basic formulation 基本框架） | "we present the basic formulation of MLLM and" |
| delineate | v. | 详细说明、描绘（学术写作高频词，意为 describe in detail） | "and delineate its related concepts, including architecture" |
| granularity | n. | 粒度（支持更细的输入/输出粒度，如像素级细节） | "to support more granularity, modalities, languages, and" |
| hallucination | n. | 幻觉（模型生成与事实不符的内容，即"一本正经地胡说八道"） | "We continue with multimodal hallucination and extended techniques" |
| promising | adj. | 有前景的（promising research directions 有潜力的研究方向） | "and point out promising research directions" |
| inspire | v. | 激发、启发（inspire more research 启发更多研究） | "hope it can inspire more research" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 00-04 A Comprehensive Survey on Deep Music Generation: Multi-level Representations, Algorithms, Evaluations, and Future Directions

- [ ] 已读

**中文标题**：《深度音乐生成综合综述：多层次表示、算法、评估与未来方向》

**一句话概括**：按乐谱生成、演奏生成、音频生成三个层次全面综述深度音乐生成任务，总结各任务的数据集、音乐表示与评估方法并展望未来方向。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| comprehensive | adj. | 全面的、综合的（comprehensive survey 全面综述，学术高频词） | "A Comprehensive Survey on Deep Music Generation" |
| utilization | n. | 利用、运用（utilize 的名词形式，学术写作高频） | "The utilization of deep learning techniques in" |
| widespread | adj. | 广泛的（attract widespread attention 引起广泛关注） | "has attracted widespread attention of countless researchers" |
| stage | n. | 阶段（本文把音乐制作流程分成三个阶段） | "can be divided into three stages" |
| corresponding | adj. | 相应的、对应的（corresponding to 与……相对应） | "corresponding to the three levels of music" |
| convert | v. | 转换（convert A into B 把 A 转换成 B） | "converts scores with performance characteristics into audio" |
| assign | v. | 分配、赋予（assigning timbre 给音符指定音色） | "into audio by assigning timbre or generates" |
| timbre | n. | 音色（区分不同乐器/声音的特质） | "by assigning timbre or generates music in" |
| evolution | n. | 演变、发展（model evolution 模型的发展历程） | "the development history, the model evolution, as" |
| pros and cons | phr. | 优缺点、利与弊（指同一任务不同方法的长处与不足） | "as well as the pros and cons of" |
| illustrate | v. | 阐明、说明（have not been clearly illustrated 尚未被清楚阐明） | "have not been clearly illustrated" |
| representation | n. | 表示（music representations 音乐的编码/表达形式，如音符、MIDI） | "discuss the music representations, the evaluation methods" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 00-05 Understanding World or Predicting Future? A Comprehensive Survey of World Models

- [ ] 已读

**中文标题**：《理解世界还是预测未来？世界模型综合综述》

**一句话概括**：系统综述世界模型研究，将其归纳为"构建内部表征理解世界"与"预测未来状态辅助决策"两大功能，并介绍在生成游戏、自动驾驶、机器人等领域的应用。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| garner | v. | 获得、赢得（garner attention 赢得关注，书面语高频） | "has garnered significant attention due to advancements" |
| advancement | n. | 进步、进展（advancements in … 某领域的最新进展） | "due to advancements in multimodal large language" |
| pursuit | n. | 追求、探索（the pursuit of AGI 对通用人工智能的追求） | "central to the pursuit of artificial general" |
| systematic | adj. | 系统的（systematic categorization 系统分类，学术高频） | "This review presents a systematic categorization of" |
| categorization | n. | 分类（把研究对象归入不同类别） | "This review presents a systematic categorization of" |
| emphasize | v. | 强调（emphasizing two primary functions 强调两大主要功能） | "categorization of world models, emphasizing two primary" |
| representation | n. | 表征（internal representations 模型内部对世界的编码） | "constructing internal representations to understand the" |
| simulate | v. | 模拟（simulate future states 模拟未来状态） | "predicting future states to simulate and guide" |
| domain | n. | 领域（key domains 关键领域，如自动驾驶、机器人） | "the application of world models in key domains" |
| autonomous driving | phr. | 自动驾驶（autonomous 自主的 + driving 驾驶） | "including generative games, autonomous driving, robotics, and" |
| simulacra | n. | 仿真体、模拟物（social simulacra 社会仿真环境/虚拟社会） | "robotics, and social simulacra, with a focus" |
| insight | n. | 洞见、深刻见解（provide insights into 对……给出见解） | "provide insights into potential future research directions" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 00-06 Is Sora a World Simulator? A Comprehensive Survey on General World Models and Beyond

- [ ] 已读

**中文标题**：《Sora 是世界模拟器吗？通用世界模型综合综述》

**一句话概括**：围绕 Sora 引发的通用世界模型热潮，综述视频生成、自动驾驶、自主智能体等领域的最新进展，并讨论世界模型的挑战与未来方向。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| simulator | n. | 模拟器（world simulator 世界模拟器：能模拟物理世界的模型） | "Is Sora a World Simulator?" |
| crucial | adj. | 至关重要的（crucial pathway 关键路径） | "General world models represent a crucial pathway" |
| pathway | n. | 路径、途径（走向通用人工智能的路径） | "represent a crucial pathway toward achieving" |
| cornerstone | n. | 基石、基础（serving as the cornerstone 作为……的基石） | "serving as the cornerstone for various applications" |
| emergence | n. | 出现、兴起（Sora 模型的出现） | "the emergence of the Sora model has attained" |
| incipient | adj. | 初期的、萌芽的（incipient comprehension 初步的理解） | "an incipient comprehension of physical laws" |
| embark on | phr. | 着手、开始（embark on an exploration 开始一项探索） | "we embark on a comprehensive exploration of" |
| forefront | n. | 前沿、最前线（处于研究最前沿） | "navigates through the forefront of generative methodologies" |
| pivotal | adj. | 关键的、核心的（pivotal constructs 核心构件） | "world models stand as pivotal constructs facilitating" |
| scrutinize | v. | 仔细审视、细查（比 examine 更强调细致） | "we scrutinize the burgeoning field of autonomous-driving" |
| burgeoning | adj. | 蓬勃发展的、迅速增长的（burgeoning field 新兴领域） | "the burgeoning field of autonomous-driving world models" |
| delve into | phr. | 深入探究（delve into the intricacies 深入复杂的细节） | "we delve into the intricacies inherent in" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

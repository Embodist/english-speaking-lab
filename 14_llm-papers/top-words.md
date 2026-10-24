---
type: word-bank
title: "LLM 论文高频词（S/A）"
tags: [library/word-bank, skill/reading, status/learning]
created: 2026-10-24
---

# LLM 论文高频词（S/A）

> 按“出现论文数”排序：S ≥5 篇，A 2–4 篇，B 仅 1 篇（放在逐篇词表里学）。
> 先掌握 S，再扫 A；B 不要单独背，读论文时顺带记。

> [!tip] 用法
> 遮住中文，看词说出“中文 + 论文搭配”；能用它说一句 abstract 总结，才算掌握。

## S 级：跨论文高频（44）

| 级别 | 词/短语 | 词性 | 中文 | 出现论文数 | 示例语境 |
|---|---|---|---|---|---|
| S | benchmark | n. | 基准（标准评测集） | 15 | "a state-of-the-art average accuracy of 67.5% on the MMLU benchmark" |
| S | outperform | v. | 超越、胜过 | 14 | "Our models outperform open-source chat models on most benchmarks" |
| S | zero-shot | adj. | 零样本的（不提供示例直接完成任务） | 11 | "generalize zero-shot to new tasks" |
| S | downstream | adj. | 下游的（预训练之后要解决的具体任务） | 10 | "the model to downstream tasks" |
| S | autoregressive | adj. | 自回归的（逐词预测下一个词来生成） | 9 | "we train GPT-3, an autoregressive language model with 175 billion parameters" |
| S | corpus | n. | 语料库（大规模文本集合） | 9 | "by pre-training on a large corpus of text followed by fine-tuning" |
| S | competitive | adj. | 有竞争力的、不相上下的 | 8 | "LLaMA-65B is competitive with the best models" |
| S | inference | n. | 推断（判断句子间关系的自然语言推理任务） | 8 | "such as question answering and language inference" |
| S | leverage | v. | 利用、借助 | 8 | "Both the SL and RL methods can leverage chain-of-thought style reasoning" |
| S | state-of-the-art | adj. | 最先进的、当前最优的（常缩写为 SOTA） | 8 | "a new single-model state-of-the-art BLEU score" |
| S | alignment | n. | 对齐（让模型行为符合期望） | 7 | "The post-training alignment process results in improved performance" |
| S | comprehensive | adj. | 全面的、综合的（comprehensive survey 全面综述，学术高频词） | 7 | "A Comprehensive Survey on Deep Music Generation" |
| S | end-to-end | adj. | 端到端的（从输入到输出整体联合训练） | 7 | "end-to-end training of large-scale models" |
| S | generalize | v. | 泛化（迁移到新任务） | 7 | "have demonstrated a remarkable ability to generalize zero-shot to new tasks" |
| S | hierarchical | adj. | 分层的（模型分两级：先验+解码器） | 7 | "Hierarchical Text-Conditional Image Generation with" |
| S | retrieval | n. | 检索（按查询找匹配的图像/文本） | 7 | "image-text retrieval benchmarks, even when compared" |
| S | self-supervised | adj. | 自监督的（无需人工标注） | 7 | "This is done in a self-supervised way" |
| S | architecture | n. | 架构（模型的整体结构设计） | 6 | "without substantial task-specific architecture modifications" |
| S | curate | v. | 精心挑选、策划（curate a collection 系统地挑选并组织样本） | 6 | "we curate and organize a collection of" |
| S | curation | n. | 精选、整理过程（成本高昂的数据清洗环节） | 6 | "This costly curation process limits the" |
| S | latent | adj. | 隐式的（压缩后的潜在表示） | 6 | "including Multi-head Latent Attention (MLA) and DeepSeekMoE" |
| S | modality | n. | 模态（图像、文本等不同的信息形式） | 6 | "the modality gap with a lightweight" |
| S | multimodal | adj. | 多模态的（同时处理文本、图像、音频等多种信息形式） | 6 | "Multimodal Large Language Model (MLLM) represented by" |
| S | representation | n. | 表示（music representations 音乐的编码/表达形式，如音符、MIDI） | 6 | "discuss the music representations, the evaluation methods" |
| S | robust | adj. | 鲁棒的、稳健的（对各种条件都稳定可靠） | 6 | "Robust Speech Recognition via Large-Scale" |
| S | adaptation | n. | 适配（把预训练模型调整到具体任务） | 5 | "pre-training on general domain data and adaptation to particular tasks or domains" |
| S | baseline | adj. | 基线的（用作对比的现有系统） | 5 | "the performance of 3 out of 4 baseline systems" |
| S | comparable | adj. | 相当的、可比的 | 5 | "achieves quality close to multi-head attention with comparable speed to MQA" |
| S | contrastive | adj. | 对比的（contrastive loss 对比损失：拉近匹配对、推远不匹配对） | 5 | "text pairs using a contrastive loss" |
| S | cross-modal | adj. | 跨模态的（知识在不同模态间迁移） | 5 | "benefit from cross-modal transfer, i.e.," |
| S | discrete | adj. | 离散的（编码取值有限、不连续；与 continuous 相对） | 5 | "the encoder network outputs discrete, rather" |
| S | fidelity | n. | 保真度（生成结果与目标/真实图像的吻合程度） | 5 | "diversity for fidelity" |
| S | generalization | n. | 推广、泛化（此处指 MQA 的一般化形式） | 5 | "introduce grouped-query attention (GQA), a generalization of multi-query attention" |
| S | high-fidelity | adj. | 高保真的（生成质量与真实图像高度一致） | 5 | "diffusion models in high-fidelity image generation" |
| S | interleaved | adj. | 交错的、穿插的（文本与图像任意穿插组合的输入） | 5 | "processing arbitrarily interleaved multimodal inputs and" |
| S | latent space | phr. | 隐空间、潜在空间（压缩后的低维特征空间） | 5 | "in the latent space of powerful" |
| S | paradigm | n. | 范式（领域内标准做法） | 5 | "An important paradigm of natural language processing consists of large-scale pre-training" |
| S | pipeline | n. | 流程（流水线式的处理步骤） | 5 | "Our pipeline generates instructions, input, and output samples from a language model" |
| S | recipe | n. | 方法、方案 | 5 | "We explore a general-purpose fine-tuning recipe for retrieval-augmented generation" |
| S | scalable | adj. | 可扩展的（方法能随数据规模放大而受益） | 5 | "an efficient and scalable way to learn" |
| S | sparse | adj. | 稀疏的（每次只激活少量参数） | 5 | "a Sparse Mixture of Experts (SMoE) language model" |
| S | surpass | v. | 超越（性能超过或持平更大模型） | 5 | "surpassing or matching PaLI-X 55B" |
| S | synthesize | v. | 合成；从模型生成新视角图像 | 5 | "for synthesizing novel views of complex scenes" |
| S | synthetic | adj. | 合成的（机器生成的数据） | 5 | "we release our large synthetic dataset to facilitate future studies" |

## A 级：常见（约 290）

| 级别 | 词/短语 | 词性 | 中文 | 出现论文数 | 示例语境 |
|---|---|---|---|---|---|
| A | align | v. | 对齐（与目标任务、用户偏好一致） | 4 | "to better align to end tasks and user preferences" |
| A | capture | v. | 捕捉（表示同时包含语义和风格信息） | 4 | "capture both semantics and style" |
| A | concurrently | adv. | 并发地、同时 | 4 | "potentially generating several tokens concurrently" |
| A | conditioning | v. | 条件化（建模时把上下文作为条件考虑） | 4 | "jointly conditioning on both left and right context in all layers" |
| A | embedding | n. | 嵌入（向量）（把输入映射成的稠密向量表示） | 4 | "unimodal image and text embeddings, in" |
| A | fine-tuning | n. | 微调（用任务数据在预训练模型上继续训练） | 4 | "followed by fine-tuning on a specific task" |
| A | generative | adj. | 生成式的（能生成新样本的模型） | 4 | "a simple yet powerful generative model that" |
| A | generic | adj. | 通用的（generic intelligence 通用智能；本文强调能力具有通用性） | 4 | "to achieve stronger generic intelligence" |
| A | incorporate | v. | 整合、纳入 | 4 | "and how to best incorporate the results into future token prediction" |
| A | inpainting | n. | 图像修复（补全图像缺失/被遮区域） | 4 | "fine-tuned to perform image inpainting, enabling" |
| A | intermediate | adj. | 中间的 | 4 | "a series of intermediate reasoning steps" |
| A | jointly | adv. | 联合地（两个训练目标同时进行） | 4 | "pretrain an image-text encoder-decoder foundation model jointly" |
| A | long-horizon | adj. | 长时程的；需要很多步才能完成的任务 | 4 | solves long-horizon tasks from images |
| A | metric | n. | 指标；量化评测的标准 | 4 | "across both multiple machine metrics and human evaluations" |
| A | objective | n. | 目标（函数）（与 DDPM 相同的训练目标） | 4 | "lead to the same training objective" |
| A | pre-trained | v. | 预训练 | 4 | "a Transformer-based model pre-trained to predict the next token in a document" |
| A | pretraining | n. | 预训练；训练的第一阶段 | 4 | "consisting of two stages: pretraining and task-specific adaptation" |
| A | progressively | adv. | 逐步地（分阶段逐渐对齐） | 4 | "progressively aligns it with the LLM" |
| A | prompt | v. | 提示、引导（用问题/示例引导模型作答） | 4 | "the model is prompted with a question" |
| A | remarkable | adj. | 显著的、非凡的（remarkable progress 显著进展） | 4 | "a remarkable progress is the launch of ChatGPT" |
| A | symbolic | adj. | 符号的（符号逻辑类推理） | 4 | "improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks" |
| A | temporal | adj. | 时间的；沿时间轴的信息维度 | 4 | "along both spatial and temporal dimensions" |
| A | trajectories | n. | 轨迹（完成任务的过程记录） | 4 | "generates human-like task-solving trajectories that are more interpretable" |
| A | accelerate | v. | 加速（加快采样速度） | 3 | "To accelerate sampling, we present denoising" |
| A | accessible | adj. | 易获得的、可及的（让 SOTA 研究门槛更低） | 3 | "make state-of-the-art LMM research more accessible" |
| A | adherence | n. | 遵从、遵守 | 3 | "on measures of factuality and adherence to desired behavior" |
| A | aligned | adj. | 对齐的（与用户意图一致） | 3 | "these models are not aligned with their users" |
| A | augmentation | n. | 数据增强；对样本做变换扩充 | 3 | "with prompts and augmentations" |
| A | bidirectional | adj. | 双向的（同时利用左右两侧上下文） | 3 | "BERT is designed to pre-train deep bidirectional representations" |
| A | bridge | v. | 桥接、弥合（连接两种不同模态/模型） | 3 | "bridges the modality gap with a" |
| A | captioning | n. | 描述生成；为视频写详细文字说明 | 3 | "This dataset includes key tasks such as detailed captioning" |
| A | checkpoint | n. | 检查点（此处指训练好的模型权重文件） | 3 | "Our final 13B checkpoint uses merely" |
| A | coherence | n. | 连贯性（长程一致性） | 3 | "that require maintaining long-range coherence" |
| A | coherent | adj. | 连贯的（视频帧间在时间上一致连贯） | 3 | "temporally coherent high fidelity video" |
| A | compress | v. | 压缩；减少视频的数据量 | 3 | "to compress videos along both spatial and temporal dimensions" |
| A | conditional | adj. | 条件式的（生成受额外输入如类别/分割图控制） | 3 | "readily applied to conditional synthesis tasks" |
| A | conditioned on | phr. | 以……为条件（把……作为输入提供给模型） | 3 | "When conditioned on a document plus questions" |
| A | conventional | adj. | 常规的、传统的（除常规任务之外） | 3 | "Beyond the conventional image description and" |
| A | corresponding | adj. | 相应的、对应的（corresponding to 与……相对应） | 3 | "corresponding to the three levels of music" |
| A | curated | adj. | 精心筛选的 | 3 | "only 1,000 carefully curated prompts and responses" |
| A | diffusion | n. | 扩散（前向逐步加噪声、反向去噪的生成范式） | 3 | "synthesis results using diffusion probabilistic models" |
| A | diversity | n. | 多样性 | 3 | "often limited in quantity, diversity, and creativity" |
| A | emergent | adj. | 涌现的（emergent capabilities 指模型规模增大后"涌现"出的新能力） | 3 | "The surprising emergent capabilities of MLLM" |
| A | empirically | adv. | 从实验上、经验上 | 3 | "BERT is conceptually simple and empirically powerful" |
| A | estimate | v. | 估计；用神经网络近似计算分数（梯度场） | 3 | "we can accurately estimate these scores with neural networks" |
| A | feasible | adj. | 可行的 | 3 | "full fine-tuning, which retrains all model parameters, becomes less feasible" |
| A | fine-tune | v. | 微调（在任务数据上继续训练） | 3 | "outperforms models fine-tuned on thousands of" |
| A | fine-tuned | v. | 微调（在预训练模型上用小规模任务数据继续训练） | 3 | "the pre-trained BERT model can be fine-tuned with just one additional output layer" |
| A | formulation | n. | 形式化表述、基本定义（basic formulation 基本框架） | 3 | "we present the basic formulation of MLLM and" |
| A | forward pass | phr. | 前向传播；一次网络计算即完成编辑 | 3 | "Since it performs edits in the forward pass" |
| A | foster | v. | 促进、推动（推动基础模型研究） | 3 | "to foster research into foundation models" |
| A | foundation model | phr. | 基础模型（大规模预训练、可迁移到多任务的模型） | 3 | "large-scale pretrained foundation models is" |
| A | framework | n. | 框架（一整套方法体系） | 3 | "we propose BLIP, a new VLP framework" |
| A | fusion | n. | 融合（视觉与语言特征的深度融合） | 3 | "deep fusion of vision language features" |
| A | general-purpose | adj. | 通用目的的（不局限于单一任务） | 3 | "general-purpose visual and language understanding" |
| A | hinder | v. | 阻碍（限制模型规模继续扩大） | 3 | "hinders the scaling of trained models" |
| A | implicit | adj. | 隐式的（不显式依赖马尔可夫性质的过程） | 3 | "we present denoising diffusion implicit models" |
| A | innovation | n. | 创新（架构上的关键改进） | 3 | "key architectural innovations to: (i) bridge" |
| A | interpret | v. | 解释为、理解为（可看作自回归解码的推广） | 3 | "interpreted as a generalization of autoregressive" |
| A | lightweight | adj. | 轻量的（简单、负担小） | 3 | "a module composed of a set of lightweight annotation APIs" |
| A | likelihood | n. | 似然；精确计算数据概率的能力 | 3 | "enables exact likelihood computation" |
| A | manipulation | n. | 操作、操控（对图像内容的修改） | 3 | "language-guided image manipulations in a zero-shot" |
| A | mechanism | n. | 机制（attention mechanism 注意力机制：让模型聚焦输入中重要部分的机制） | 3 | "the encoder and decoder through an attention mechanism" |
| A | meticulously | adv. | 一丝不苟地、精心地 | 3 | "through a meticulously engineered data selection pipeline" |
| A | milestone | n. | 里程碑（生成建模研究的重要节点） | 3 | "an important milestone in generative modeling" |
| A | off-the-shelf | adj. | 现成的（已有模型、无需改动） | 3 | "accelerate existing off-the-shelf models without retraining" |
| A | open challenge | phr. | 尚待解决的难题（尚未攻克的研究问题） | 3 | "an open challenge for multimodal machine learning" |
| A | outperforms | v. | 性能优于、胜过 | 3 | "Chinchilla uniformly and significantly outperforms Gopher (280B)" |
| A | perceptual | adj. | 感知的；与人类视觉感知一致 | 3 | "closely aligning with human perceptual processes" |
| A | pre-training | n. | 预训练；在大规模数据上先训练通用表征 | 3 | "for Language-Image Pre-training (SigLIP)" |
| A | preserve | v. | 保留（保持原图的语义与风格） | 3 | "preserve both its semantics and style" |
| A | promising | adj. | 有前景的（promising research directions 有潜力的研究方向） | 3 | "and point out promising research directions" |
| A | propose | v. | 提出（学术写作高频词，指提出新的方法/架构） | 3 | "We propose a new simple network architecture" |
| A | reasoning | n. | 推理（math reasoning 数学推理；本文指不依赖 OCR 直接解题） | 3 | "OCR-free math reasoning, are rare in traditional" |
| A | reconstruction | n. | 重建；从剩余部分还原被遮盖内容 | 3 | "makes video reconstruction a more challenging self-supervision task" |
| A | recurrent | adj. | 循环的（指 RNN 这类按时间步循环处理序列的网络） | 3 | "complex recurrent or convolutional neural networks in" |
| A | reinforcement learning | phr. | 强化学习（通过奖励信号学习策略） | 3 | "using reinforcement learning from human feedback" |
| A | resolution | n. | 分辨率；本文目标为 1080p 高清 | 3 | "1080p resolution rendering, no current method" |
| A | sample efficiency | phr. | 样本效率（数据利用效率） | 3 | "predictably improve performance and sample efficiency on a wide range" |
| A | sample-efficient | adj. | 样本高效的（用较少数据达到较好效果） | 3 | "Larger models are significantly more sample-efficient" |
| A | scaling laws | n. | 规模定律（性能随规模变化的规律） | 3 | "We study empirical scaling laws for language model performance" |
| A | self-attention | n. | 自注意力；序列内元素相互关注的机制 | 3 | "built exclusively on self-attention over space and time" |
| A | sequential | adj. | 顺序的、逐次的（逐步依次应用去噪自编码器） | 3 | "a sequential application of denoising autoencoders" |
| A | simulate | v. | 模拟（simulate future states 模拟未来状态） | 3 | "predicting future states to simulate and guide" |
| A | solely | adv. | 仅仅、完全（based solely on 即"完全基于"） | 3 | "based solely on attention mechanisms" |
| A | span | v. | 涵盖、跨越（样本跨越多种领域与任务） | 3 | "spanning a variety of domains and tasks" |
| A | struggle | v. | 难以做到、表现吃力 | 3 | "which current NLP systems still largely struggle to do" |
| A | suite | n. | 系列；一组配套的模型 | 3 | "a resulting suite of LMMs" |
| A | superior | adj. | 卓越的、更好的 | 3 | "engineered for superior performance and efficiency" |
| A | supervision | n. | 监督信息（给模型提供训练信号的额外信息） | 3 | "It enables valuable supervision for dependency modeling between elements" |
| A | synthesis | n. | 合成；从条件生成内容 | 3 | "text-to-video synthesis, video personalization, video editing" |
| A | systematic | adj. | 系统的（systematic categorization 系统分类，学术高频） | 3 | "This review presents a systematic categorization of" |
| A | tackle | v. | 应对、处理（难题） | 3 | "We tackle the long context of raw audio" |
| A | tokenization | n. | 词元化；把输入切成统一单元 | 3 | "due to the lack of unified tokenization for images and videos" |
| A | trade off | phr. | 权衡、以……换取……（牺牲多样性换保真度） | 3 | "trade off diversity for fidelity" |
| A | transfer | v. | 迁移（把模型能力应用到其他任务/数据上） | 3 | "transferred to multiple mid-sized or small image" |
| A | unified | adj. | 统一的；用同一框架处理所有模态 | 3 | "for the unified processing of various modalities" |
| A | unprecedented | adj. | 前所未有的（GPT-4V 处理任意交错多模态输入的能力） | 3 | "GPT-4V's unprecedented ability in processing arbitrarily" |
| A | utilize | v. | 利用 | 3 | "LLaMA models can effectively utilize and extrapolate to context lengths" |
| A | variant | n. | 变体（某方法的修改版本） | 3 | "We propose a variant called multi-query attention" |
| A | versatile | adj. | 多用途的、多才多艺的（能胜任多种任务） | 3 | "Qwen-VL: A Versatile Vision-Language Model" |
| A | ablation | n. | 消融（消融实验：逐一去掉组件验证作用） | 2 | "Ablation studies also verify the effectiveness of" |
| A | accompaniment | n. | 伴奏 | 2 | "melody completion, accompaniment suggestion, genre classification" |
| A | accuracy | n. | 准确率（评测指标，此处达 92.53%） | 2 | "a new state-of-the-art accuracy of 92.53%" |
| A | adopt | v. | 采用（被广泛采用） | 2 | "have been widely adopted as the main" |
| A | advancement | n. | 进步、进展（advancements in … 某领域的最新进展） | 2 | "due to advancements in multimodal large language" |
| A | aligning | v. | 对齐（让模型行为符合指令要求） | 2 | "method for aligning pre-trained language models with instructions" |
| A | alleviate | v. | 缓解（缓解上述挑战） | 2 | "To alleviate the aforementioned challenges we propose" |
| A | arbitrary | adj. | 任意的 | 2 | "to effectively handle sequences of arbitrary length" |
| A | arithmetic | n. | 算术 | 2 | "a range of arithmetic, commonsense, and symbolic reasoning tasks" |
| A | attain | v. | 获得、达到（取得优秀结果） | 2 | "attains excellent results compared to state-of-the-art" |
| A | auto-regressive | adj. | 自回归的（逐个预测生成） | 2 | "we propose AaudioGen, an auto-regressive generative model" |
| A | autoencoder | n. | 自编码器（先压缩再重建的神经网络） | 2 | "a sequential application of denoising autoencoders" |
| A | autoregressively | adv. | 自回归地（逐个预测下一个文本 token） | 2 | "decoder outputs which predicts text tokens" |
| A | availability | n. | 可用性、可获得性 | 2 | "by the limited availability of large audio datasets" |
| A | backbone | n. | 主干网络（通用的序列模型底座） | 2 | "As a general sequence model backbone, Mamba achieves state-of-the-art performance" |
| A | baselines | n. | 基线（用于对比的已有方法） | 2 | "trains Transformers faster than existing baselines" |
| A | bind | v. | 绑定、联结（把各模态联结到同一空间） | 2 | "is sufficient to bind the modalities" |
| A | bitrate | n. | 比特率（每秒传输的数据量） | 2 | "maintaining a similar bitrate and perceptual quality" |
| A | boost | v. | 提升（提高样本保真度与图文对齐） | 2 | "boosts both sample fidelity and image-text" |
| A | bridge the gap | phr. | 弥合差距；拉近两个群体间的距离 | 2 | "we aim to bridge the gap between closed-source and open-source communities" |
| A | capability | n. | 能力 | 2 | "YaRN exhibits the capability to extrapolate beyond the limited context" |
| A | caption | n. | 图片说明文字、配图文本 | 2 | "predicting which caption goes with which image" |
| A | cascade | v. | 级联（把剩余解码层依次串联起来） | 2 | "cascades the remaining decoder layers which" |
| A | cast | n. | 阵容；一组配合使用的模型 | 2 | "a cast of foundation models that generates high-quality" |
| A | closed-source | adj. | 闭源的（不公开模型权重） | 2 | "a suitable substitute for closed-source models" |
| A | codec | n. | 编解码器（压缩/解压音频的模块） | 2 | "produced by a neural audio codec to" |
| A | combine | v. | 合并、结合 | 2 | "to process the current state and combine their outputs" |
| A | comprehend | v. | 理解、领会（比 understand 更正式，本文指让 AI 理解语言） | 2 | "for comprehending and grasping a language" |
| A | compressed | adj. | 压缩的（压缩后的离散表示） | 2 | "streams of compressed discrete music representation" |
| A | compute | n. | 算力、计算量 | 2 | "the amount of compute used for training" |
| A | condition on | phr. | 以…为条件（生成时给定前序信息） | 2 | "sample conditioned on all previous ones" |
| A | consistent | adj. | 一致的（音乐保持连贯） | 2 | "that remains consistent over several minutes" |
| A | contrastive learning | phr. | 对比学习；拉近匹配样本、推开不匹配样本 | 2 | "Unlike standard contrastive learning with softmax normalization" |
| A | controllability | n. | 可控性（可控制生成结果） | 2 | "we present its controllability and generalization for" |
| A | convergence | n. | 收敛（训练损失趋于平稳不再下降） | 2 | "and stopping significantly before convergence" |
| A | coordinate | n. | 坐标；网络输入的 5 维空间-方向表示 | 2 | "whose input is a single continuous 5D coordinate" |
| A | critical | adj. | 至关重要的 | 2 | "Neural network scaling has been critical for improving the model quality" |
| A | customized | adj. | 定制的；针对视频专门设计的掩码方式 | 2 | "propose customized video tube masking with an extremely high ratio" |
| A | data-efficient | adj. | 数据高效的（少量数据就能学好） | 2 | "powerful and data-efficient" |
| A | decoder | n. | 解码器（负责生成输出的部分） | 2 | "drastically speeds up decoder inference" |
| A | demonstrate | v. | 证明、展示 | 2 | "We demonstrate that language models begin to learn these tasks" |
| A | demonstrations | n. | 示范样本（人工标注的期望行为） | 2 | "we collect a dataset of labeler demonstrations of the desired model behavior" |
| A | denoising | adj. | 去噪的（逐步去除噪声恢复图像） | 2 | "sequential application of denoising autoencoders" |
| A | differentiable | adj. | 可微的（可求导、支持梯度传播） | 2 | "Pre-trained models with a differentiable access mechanism to explicit non-parametric memory" |
| A | discriminative | adj. | 判别式的；以区分正负样本学习表征 | 2 | "both generative and discriminative self-supervised video learning" |
| A | distribution | n. | 分布（输出的概率分布） | 2 | "and without changing the distribution" |
| A | diverse | adj. | 多样的 | 2 | "We apply our approach, named ReAct, to a diverse set of language" |
| A | dominant | adj. | 主导的、占支配地位的（本文指当前主流的序列转导模型） | 2 | "The dominant sequence transduction models are based on" |
| A | dropout | n. | 随机失活（文本丢弃，作数据增强） | 2 | "It employed text dropout as a data" |
| A | dynamic | adj. | 动态的；涉及运动与时间变化的理解 | 2 | "limited for dynamic and complex video-level understanding tasks" |
| A | dynamics | n. | 动力学；环境状态如何随时间演化 | 2 | learns the environment dynamics from images |
| A | efficacy | n. | 有效性、效果 | 2 | "which sheds light on the efficacy of LoRA" |
| A | efficiency | n. | 效率；单位算力下的处理能力 | 2 | "achieve dramatically higher test efficiency (at a small drop in accuracy)" |
| A | emergence | n. | 出现、兴起（Sora 模型的出现） | 2 | "the emergence of the Sora model has attained" |
| A | emerging | adj. | 涌现的（训练后自然出现的新能力） | 2 | "emerging capabilities of zero-shot image-to-text" |
| A | empirical | adj. | 经验的、实证的（由实验数据得出） | 2 | "We study empirical scaling laws for language model performance" |
| A | encoder | n. | 编码器；处理可见 token 的网络部分 | 2 | "with an encoder operating on a subset of video tokens" |
| A | endeavor | v. | 努力、竭力（学术界与工业界都努力去做） | 2 | "both academia and industry have endeavored to" |
| A | endow | v. | 赋予（让模型具备某种能力） | 2 | "endow them with in-context few-shot learning" |
| A | ensemble | n. | 集成模型（多个模型组合起来投票/平均得到的结果） | 2 | "including ensembles by over 2 BLEU" |
| A | evaluation | n. | 评估；检验模型性能的过程 | 2 | "undergo rigorous evaluation across a range of tasks" |
| A | excel | v. | 擅长、表现出色 | 2 | "where much simpler and smaller models excel" |
| A | exhibits | v. | 展现出、表现出 | 2 | "GPT-4 exhibits human-level performance on various professional and academic benchmarks" |
| A | explicit | adj. | 显式的、明确的（此处指人工标签） | 2 | "learn these tasks without any explicit supervision when trained" |
| A | exploration | n. | 探索；主动去未知区域获取信息 | 2 | self-supervised exploration and fast adaptation |
| A | extension | n. | 扩展（延长上下文窗口） | 2 | "surpassing previous the state-of-the-art at context window extension" |
| A | extensive | adj. | 大量的、广泛的 | 2 | "heavily contingent upon extensive human-annotated demonstrations" |
| A | extract | v. | 提取（提取音乐特征） | 2 | "methods to extract the music features which" |
| A | facilitate | v. | 促进、推动；使更广泛应用成为可能 | 2 | "ControlNet may facilitate wider applications to control image" |
| A | favorable | adj. | 有利的；仍然取得不错的效果 | 2 | "still yields favorable performance of VideoMAE" |
| A | feedforward | adj. | 前馈的（全连接网络层） | 2 | "each layer is composed of 8 feedforward blocks (i.e. experts)" |
| A | few-shot | adj. | 少样本的（只用极少示例学习新任务） | 2 | "test its performance in the few-shot setting" |
| A | finetune | v. | 微调 | 2 | "and then finetune the original model on revised responses" |
| A | flexible | adj. | 灵活的 | 2 | "(2) flexible sharing of KV cache within and across requests" |
| A | foundation | adj. | 基础的（作为底座的大规模预训练模型） | 2 | "a collection of foundation language models ranging from 7B to 65B parameters" |
| A | from scratch | phr. | 从零开始（不依赖人类输入） | 2 | "four bars right from scratch (i.e. without" |
| A | generalist | n. | 通才（multimodal generalist system 能处理多种任务的多模态通才系统） | 2 | "make GPT-4V a powerful multimodal generalist system" |
| A | grounding | n. | 视觉定位（把文本指称与图像区域对应起来） | 2 | "implement the grounding and text-reading ability" |
| A | hallucination | n. | 幻觉（模型生成与事实不符的内容，即"一本正经地胡说八道"） | 2 | "We continue with multimodal hallucination and extended techniques" |
| A | harness | v. | 利用、挖掘 | 2 | "we harness the significant potential of publicly available web data" |
| A | high-dimensional | adj. | 高维的；维度很多的输入 | 2 | learning world models from high-dimensional sensory inputs |
| A | hybrid | adj. | 混合的（此处指 CNN+RNN 的混合结构） | 2 | "effectiveness of its hybrid structure in music feature" |
| A | identify | v. | 识别、找出（识别出图像中的幽默元素） | 2 | "identifying humorous elements within images" |
| A | imitate | v. | 模仿 | 2 | that imitates short demonstration sequences |
| A | impact | v. | 影响；对生活产生作用 | 2 | "have significantly impacted daily life for both individuals" |
| A | informative | adj. | 信息丰富的（提取对任务有用的特征） | 2 | "extracts informative features tailored to the" |
| A | infrastructure | n. | 基础设施（训练所需的工程体系） | 2 | "developing infrastructure and optimization methods that behave predictably" |
| A | innovative | adj. | 创新的 | 2 | "DeepSeek-V2 adopts innovative architectures including Multi-head Latent Attention" |
| A | inspire | v. | 激发、启发（inspire more research 启发更多研究） | 2 | "hope it can inspire more research" |
| A | instability | n. | 不稳定性（训练过程波动） | 2 | "communication costs and training instability -- we address these" |
| A | instruction | n. | 指令（自然语言给出的任务要求） | 2 | "that can follow natural language instructions" |
| A | instruction tuning | phr. | 指令微调（用指令数据训练模型遵循指令） | 2 | "large scale instruction tuning and reinforcement learning" |
| A | interpolation | n. | 插值（在两个点之间平滑过渡） | 2 | "meaningful image interpolation directly in the" |
| A | investigate | v. | 研究、调查 | 2 | "We investigate the optimal model size and number of tokens" |
| A | latency | n. | 延迟（响应所需时间） | 2 | "unlike adapters, no additional inference latency" |
| A | latent imagination | phr. | 潜空间想象；在世界模型的潜空间中想象未来轨迹 | 2 | solves long-horizon tasks from images purely by latent imagination |
| A | localization | n. | 定位（视觉定位，找出图像中目标的位置/框） | 2 | "for Understanding, Localization, Text Reading" |
| A | long-range | adj. | 长程的、远距离的（捕捉序列中相隔很远的依赖） | 2 | "long-range interactions on sequential data, transformers" |
| A | mapping | n. | 映射（输入到输出的对应关系） | 2 | "learn a direct mapping from audio spectrograms" |
| A | Markov chain | phr. | 马尔可夫链（状态转移只依赖当前状态的随机过程） | 2 | "a Markov chain for many steps" |
| A | mask | n. | 掩码（标注物体区域的像素级标记） | 2 | "with over 1 billion masks on" |
| A | measure | v. | 衡量 | 2 | "We measure the relative importance of these two stages" |
| A | melody | n. | 旋律 | 2 | "including melody completion, accompaniment suggestion, genre" |
| A | minibatch | n. | 小批量（每次训练用的一小批样本） | 2 | "the variance of minibatch gradients and" |
| A | model-based | adj. | 基于模型的；先学习环境模型再用于规划 | 2 | a purely model-based agent |
| A | multilingual | adj. | 多语言的 | 2 | "scale up multilingual neural machine translation Transformer model" |
| A | necessitate | v. | 需要、使成为必要（要求时序模型） | 2 | "music is an art of time, necessitating" |
| A | normalization | n. | 归一化；把相似度缩放到可比范围 | 2 | "Unlike standard contrastive learning with softmax normalization" |
| A | novel | adj. | 新颖的（新的联系/发现） | 2 | "a novel connection between diffusion probabilistic" |
| A | order of magnitude | phr. | 数量级（相差约 10 倍） | 2 | "spanning six orders of magnitude (~0.1 ms" |
| A | out-of-the-box | phr. | 开箱即用的（无需额外训练即可使用） | 2 | "enables novel emergent applications 'out-of-the-box'" |
| A | patch | n. | 图像块、图像碎片（ViT 把整图切成的小块） | 2 | "sequences of image patches can perform very well" |
| A | perception | n. | 感知（对图像、声音等模态的接收与理解） | 2 | "of language, multimodal perception, action" |
| A | performant | adj. | 高性能的、效果好的 | 2 | "is stable, performant, and computationally lightweight" |
| A | personalization | n. | 个性化；让模型学会特定主体 | 2 | "a new approach for "personalization" of text-to-image" |
| A | photorealistic | adj. | 照片级逼真的（生成图像与真实照片难以区分） | 2 | "Towards Photorealistic Image Generation and" |
| A | pose | v. | 构成、带来（pose a challenge 构成挑战，学术高频搭配） | 2 | "It poses a significant challenge to develop" |
| A | post-training | n. | 后训练；预训练后的继续训练 | 2 | examples of post-training of pre-trained world foundation models |
| A | posterior | n. | 后验（分布）（后验坍塌指隐变量被解码器忽略） | 2 | "paired with a powerful autoregressive decoder" |
| A | predetermined | adj. | 预先确定的（固定不变的类别集合） | 2 | "a fixed set of predetermined object categories" |
| A | predictably | adv. | 可预测地 | 2 | "optimization methods that behave predictably across a wide range of scales" |
| A | probabilistic | adj. | 概率的（基于概率分布的模型） | 2 | "diffusion probabilistic models, a class of" |
| A | probe | v. | 探查、检验（用精心设计的测试样本检验能力质量） | 2 | "test samples to probe the quality and genericity" |
| A | progressive | adj. | 渐进式的；分阶段推进的训练方式 | 2 | "we also use a progressive training paradigm" |
| A | projection | n. | 投影（把视觉特征映射到语言空间的 MLP 层） | 2 | "with an MLP projection and adding" |
| A | propagate | v. | 传播（信息沿序列传递） | 2 | "to selectively propagate or forget information along the sequence length dimension" |
| A | proprietary | adj. | 专有的（不公开的） | 2 | "without resorting to proprietary and inaccessible datasets" |
| A | protocol | n. | 流程/协议；标准训练步骤 | 2 | "The training protocol follows that of Large Language Models (LLMs)" |
| A | pursuit | n. | 追求、探索（the pursuit of AGI 对通用人工智能的追求） | 2 | "central to the pursuit of artificial general" |
| A | quadratic | adj. | 二次方的（复杂度随序列长度平方增长） | 2 | "the time and memory complexity of self-attention are quadratic in sequence length" |
| A | qualitative | adj. | 定性的（定性评估共享空间质量） | 2 | "as qualitative assessment of the shared embedding" |
| A | quantized | adj. | 量化的（用低精度数值表示权重） | 2 | "backpropagates gradients through a frozen, 4-bit quantized pretrained language model" |
| A | raw | adj. | 原始的（未经处理的音频波形） | 2 | "useful representations of raw music waveforms" |
| A | real-time | adj. | 实时的；满足交互式显示帧率 | 2 | "no current method can achieve real-time display rates" |
| A | redundant | adj. | 冗余的（重复多余的） | 2 | "wasted by fragmentation and redundant duplication" |
| A | release | v. | 发布、开源 | 2 | "We release all our models to the research community" |
| A | reliance | n. | 依赖（本文指对 CNN 的依赖） | 2 | "this reliance on CNNs is not necessary" |
| A | rely on | phr. | 依赖 | 2 | "meanwhile relying on pretrained vision models to" |
| A | retrieval-augmented | adj. | 检索增强的（结合检索与生成） | 2 | "We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG)" |
| A | retriever | n. | 检索器（负责查找相关文档的模型） | 2 | "accessed with a pre-trained neural retriever" |
| A | revolutionize | v. | 彻底改变、变革（revolutionize the way 颠覆……的方式） | 2 | "which would revolutionize the way how we" |
| A | robustness | n. | 鲁棒性（面对干扰/噪声的稳定性） | 2 | "approach their accuracy and robustness" |
| A | sacrificing | v. | 牺牲 | 2 | "to save memory without sacrificing performance" |
| A | scalability | n. | 可扩展性（模型在音频任务上的扩展能力） | 2 | "limits the model's scalability in audio tasks" |
| A | scaling | n. | 规模化（model scaling 指把模型变大，从而带来性能提升） | 2 | "model scaling can lead to performance improvement" |
| A | scarcity | n. | 稀缺（标注数据不足） | 2 | "is the scarcity of labeled data" |
| A | seamlessly | adv. | 无缝地（把文本标签与图文数据统一处理） | 2 | "seamlessly unifying natural language supervision" |
| A | semantically | adv. | 语义上（在语义层面有意义） | 2 | "semantically meaningful image interpolation directly in" |
| A | semantics | n. | 语义（图像的内容含义） | 2 | "capture both semantics and style" |
| A | sensory | adj. | 感知的；来自视觉等感官的信息 | 2 | "accurate sensory grounding in real-world scenarios" |
| A | shallow | adj. | 浅层的（只做简单映射、融合不深的对齐方法） | 2 | "the popular shallow alignment method which maps" |
| A | similarity | n. | 相似度（生成图与说明文字的匹配程度） | 2 | "photorealism and caption similarity, and often" |
| A | simulator | n. | 模拟器（world simulator 世界模拟器：能模拟物理世界的模型） | 2 | "Is Sora a World Simulator?" |
| A | sparse rewards | phr. | 稀疏奖励；奖励信号稀少、难以获得 | 2 | partial observability, and sparse rewards |
| A | spatiotemporal | adj. | 时空的；同时涵盖空间与时间的特征 | 2 | "enabling spatiotemporal feature learning directly from a sequence" |
| A | stabilize | v. | 稳定；防止训练发散 | 2 | "we propose various architectural improvements to stabilize model training" |
| A | stage | n. | 阶段（本文把音乐制作流程分成三个阶段） | 2 | "can be divided into three stages" |
| A | steer | v. | 引导、控制（引导风格方向） | 2 | "to steer the musical and vocal style" |
| A | stereo | adj. | 立体声的 | 2 | "both mono and stereo, while being conditioned" |
| A | stochastic | adj. | 随机的（基于随机采样的方法） | 2 | "stochastic variational inference and learning algorithm" |
| A | store | v. | 存储 | 2 | "have been shown to store factual knowledge in their parameters" |
| A | suboptimal | adj. | 次优的（含噪声网络数据并非最佳监督来源） | 2 | "which is a suboptimal source of supervision" |
| A | substantially | adv. | 显著地、大幅度地（指所需计算资源少得多） | 2 | "requiring substantially fewer computational resources" |
| A | subsume | v. | 涵盖、合并（一个模型同时具备两类方法的能力） | 2 | "subsuming model capabilities from contrastive approaches" |
| A | sufficient | adj. | 充分的（仅图像配对数据就足够） | 2 | "only image-paired data is sufficient to" |
| A | superiority | n. | 优越性（性能优于现有模型） | 2 | "demonstrates superiority compared to existing vision-language" |
| A | supervised learning | phr. | 监督学习（用带标签数据训练） | 2 | "are typically approached with supervised learning on task-specific datasets" |
| A | surpasses | v. | 超过、胜过 | 2 | "that surpasses the Llama 2 13B -- Chat model" |
| A | surprisingly | adv. | 惊人地、出乎意料地（性能出人意料地强） | 2 | "is surprisingly powerful and data-efficient" |
| A | synergy | n. | 协同效应（两者结合产生更大效果） | 2 | "allowing for greater synergy between the two" |
| A | task-specific | adj. | 任务特定的；只针对单一任务 | 2 | the learning tends to be task-specific |
| A | tempo | n. | 速度（音乐的节拍速度） | 2 | "e.g., tempo, instrument, and pitch" |
| A | thoroughly | adv. | 彻底地 | 2 | "which were thoroughly validated in DeepSeek-V2" |
| A | throughput | n. | 吞吐量（单位时间处理的数据量） | 2 | "a higher training throughput, and, unlike adapters, no additional inference latency" |
| A | timbre | n. | 音色（区分不同乐器/声音的特质） | 2 | "by assigning timbre or generates music in" |
| A | token | n. | 词元；模型处理的基本单元 | 2 | "into different numbers of visual tokens" |
| A | transcript | n. | 转录文本（音频对应的文字记录） | 2 | "predict large amounts of transcripts of audio" |
| A | transfer learning | phr. | 迁移学习（把某任务学到的知识用于另一任务） | 2 | "we present a transfer learning approach for" |
| A | transform | v. | 转换（把数据集改造成指令微调格式） | 2 | "transform them into instruction tuning format" |
| A | uncertainty | n. | 不确定性；对未来状态的不确定程度 | 2 | learns a prior model of uncertainty in a given environment |
| A | unconditional | adj. | 无条件的（不依赖任何输入条件的生成） | 2 | "video prediction and unconditional video generation" |
| A | underlying | adj. | 底层的（三个模型不同的基本假设） | 2 | "differ in the underlying assumptions and accordingly" |
| A | unsupervised | adj. | 无监督的（无需人工标签） | 2 | "unsupervised pretraining from raw text, to learn general-purpose representations" |
| A | variation | n. | 变体（保留语义风格的图像变化版本） | 2 | "produce variations of an image that" |
| A | wall-clock time | phr. | 墙钟时间（实际经过的真实时间） | 2 | "in terms of wall-clock time compared" |
| A | waveform | n. | 波形（音频信号形态） | 2 | "of raw music waveforms in a self-supervised" |

---
type: paper-vocabulary
stage: 4
title: "阶段 4 · 音乐生成 论文词汇"
tags: [topic/paper, skill/reading, status/learning]
created: 2026-10-24
---

# 阶段 4 · 音乐生成 论文词汇

> 20 篇 · 240 个词条。读前扫词 2 分钟；读后遮住中文，用 abstract 片段自测，再用 5 个词复述 60 秒。
> 返回 [[14_llm-papers/_index|LLM 论文阅读]]；配套 [[14_llm-papers/reading-workflow|阅读与词汇流程]]。

## 04-00 Neural Audio Synthesis of Musical Notes with WaveNet Autoencoders

- [ ] 已读

**中文标题**：基于 WaveNet 自编码器的音符神经音频合成

**一句话概括**：提出以原始波形上学到的时序编码为条件、自回归解码生成音频的 WaveNet 自编码器，并发布比同类数据集大一个数量级的 NSynth 音符数据集，模型可在不同乐器的音色间插值实现"乐器变形"。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| generative | adj. | 生成的（生成模型） | "Generative models in vision have seen rapid" |
| availability | n. | 可用性、可获得性（有高质量数据集可用） | "the availability of high-quality image datasets" |
| autoencoder | n. | 自编码器（先编码再解码重建的神经网络） | "a powerful new WaveNet-style autoencoder model that" |
| autoregressive | adj. | 自回归的（逐个预测、依赖前面已生成的样本） | "that conditions an autoregressive decoder on" |
| waveform | n. | 波形（音频信号的原始形态） | "learned from the raw audio waveform" |
| order of magnitude | phr. | 数量级（相差约 10 倍） | "that is an order of magnitude larger than" |
| qualitative | adj. | 定性的（主观听感层面的） | "improved qualitative and quantitative performance of the" |
| quantitative | adj. | 定量的（数值指标层面的） | "qualitative and quantitative performance of the WaveNet" |
| manifold | n. | 流形（嵌入向量构成的连续空间） | "the model learns a manifold of embeddings" |
| interpolate | v. | 插值（在两个点之间平滑过渡） | "meaningfully interpolating in timbre to create new" |
| timbre | n. | 音色（乐器声音的质感特征） | "interpolating in timbre to create new types" |
| expressive | adj. | 有表现力的（声音富有情感） | "that are realistic and expressive" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 04-01 WaveNet: A Generative Model for Raw Audio

- [ ] 已读

**中文标题**：WaveNet：用于原始音频的生成模型

**一句话概括**：提出全概率、自回归的原始音频波形生成模型 WaveNet，在文本转语音中达到当时最优自然度，还能学习音乐片段生成，并可作为判别模型用于音素识别。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| probabilistic | adj. | 概率的（输出为概率分布） | "The model is fully probabilistic and autoregressive" |
| predictive | adj. | 预测的（预测下一个样本） | "with the predictive distribution for each audio" |
| condition on | phr. | 以…为条件（生成时给定前序信息） | "sample conditioned on all previous ones" |
| nonetheless | adv. | 尽管如此（转折） | "nonetheless we show that it can be" |
| yield | v. | 产生、带来（取得结果） | "it yields state-of-the-art performance, with human" |
| parametric | adj. | 参数化的（基于参数模型的语音合成方法） | "the best parametric and concatenative systems" |
| concatenative | adj. | 拼接的（拼接录音片段合成的语音） | "parametric and concatenative systems for both English" |
| fidelity | n. | 保真度（还原度） | "different speakers with equal fidelity" |
| novel | adj. | 新颖的（从未听过的） | "it generates novel and often highly realistic" |
| fragment | n. | 片段（音乐片段） | "often highly realistic musical fragments" |
| discriminative | adj. | 判别式的（区分类别而非生成的模型） | "it can be employed as a discriminative model" |
| phoneme | n. | 音素（语音的最小单位） | "promising results for phoneme recognition" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 04-02 A Hierarchical Latent Vector Model for Learning Long-Term Structure in Music

- [ ] 已读

**中文标题**：用于学习音乐长程结构的分层潜在向量模型

**一句话概括**：提出使用分层解码器的 MusicVAE：先输出输入各子序列的嵌入，再用这些嵌入独立生成每个子序列，从而避免"后验坍缩"，在音乐序列的采样、插值与重建上显著优于扁平基线模型。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| semantically | adv. | 语义上（表示有含义的特征） | "an effective model for producing semantically meaningful" |
| latent | adj. | 潜在的（隐空间中的向量表示） | "semantically meaningful latent representations for natural data" |
| thus far | phr. | 迄今为止 | "it has thus far seen limited application" |
| sequential | adj. | 序列的（按顺序排列的数据） | "limited application to sequential data" |
| hierarchical | adj. | 分层的（多级结构的） | "we propose the use of a hierarchical decoder" |
| subsequence | n. | 子序列（整段序列中的一段） | "embeddings for subsequences of the input and" |
| encourage | v. | 促使、鼓励（让模型更倾向使用潜在码） | "This structure encourages the model to utilize" |
| utilize | v. | 利用（充分利用潜在码） | "encourages the model to utilize its latent code" |
| thereby | adv. | 从而（由此） | "thereby avoiding the posterior collapse problem" |
| collapse | n. | 坍缩（后验坍缩：潜在码被忽略的退化问题） | "avoiding the posterior collapse problem" |
| reconstruction | n. | 重建（从潜在码还原输入） | "sampling, interpolation, and reconstruction performance than" |
| interpolation | n. | 插值（在样本间平滑过渡） | "better sampling, interpolation, and reconstruction performance" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 04-03 MuseGAN: Multi-track Sequential Generative Adversarial Networks for Symbolic Music Generation and Accompaniment

- [ ] 已读

**中文标题**：MuseGAN：用于符号音乐生成与伴奏的多轨序列生成对抗网络

**一句话概括**：在 GAN 框架下提出三个面向符号多轨音乐生成的模型（jamming、composer、hybrid），用十万多小节摇滚乐训练生成五轨钢琴卷帘（贝斯、鼓、吉他、钢琴、弦乐），可从零生成四小节连贯音乐，并支持人机协作：给定人写的一轨，生成四轨伴奏。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| notable | adj. | 显著的（音乐与图像生成有显著不同） | "a few notable differences from generating images" |
| necessitate | v. | 需要、使成为必要（要求时序模型） | "music is an art of time, necessitating" |
| temporal | adj. | 时间上的（每个声部有自己的时序动态） | "their own temporal dynamics, but collectively" |
| collectively | adv. | 共同地（多轨一起展开） | "own temporal dynamics, but collectively they unfold" |
| unfold | v. | 展开（随时间逐步呈现） | "they unfold over time interdependently" |
| arpeggio | n. | 琶音（把和弦拆开依次弹奏） | "grouped into chords, arpeggios or melodies in" |
| polyphonic | adj. | 复调的、多声部的 | "or melodies in polyphonic music, and thereby" |
| underlying | adj. | 底层的（三个模型不同的基本假设） | "differ in the underlying assumptions and accordingly" |
| metric | n. | 指标（客观评测指标） | "intra-track and inter-track objective metrics are also" |
| coherent | adj. | 连贯的（结构合理的音乐） | "can generate coherent music of four bars" |
| from scratch | phr. | 从零开始（不依赖人类输入） | "four bars right from scratch (i.e. without" |
| cooperative | adj. | 协作的（人机协作生成） | "extend our models to human-AI cooperative music" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 04-04 Music Transformer

- [ ] 已读

**中文标题**：音乐 Transformer

**一句话概括**：提出把相对注意力机制对中间相对信息的存储需求从二次方降为线性的算法，使基于自注意力的 Transformer 能生成数分钟长、结构连贯的音乐，以及根据旋律生成伴奏。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| rely on | phr. | 依赖（音乐高度依赖重复） | "Music relies heavily on repetition to build" |
| repetition | n. | 重复（音乐结构的重要手法） | "relies heavily on repetition to build structure" |
| self-reference | n. | 自指（音乐对自身的引用） | "Self-reference occurs on multiple timescales, from motifs" |
| motif | n. | 动机（音乐中最小的主题乐思） | "from motifs to phrases to reusing of" |
| coherence | n. | 连贯性（长程一致性） | "that require maintaining long-range coherence" |
| relative | adj. | 相对的（相对位置信息） | "relative timing is critically important" |
| modulate | v. | 调节（根据距离调节注意力权重） | "modulate attention based on pairwise distance" |
| impractical | adj. | 不切实际的（不可行的） | "This is impractical for long sequences such" |
| quadratic | adj. | 二次的（随序列长度平方增长） | "is quadratic in the sequence length" |
| elaborate | v. | 展开、发挥（围绕动机作展开） | "coherently elaborate on a given motif" |
| accompaniment | n. | 伴奏 | "generate accompaniments conditioned on melodies" |
| chorale | n. | 众赞歌（四声部赞美诗，JSB 巴赫的众赞歌数据集） | "on two datasets, JSB Chorales and Piano-e-Competition" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 04-05 Jukebox: A Generative Model for Music

- [ ] 已读

**中文标题**：Jukebox：音乐生成模型

**一句话概括**：提出用多尺度 VQ-VAE 把长时域原始音频压缩为离散码、再用自回归 Transformer 建模的 Jukebox 模型，可生成数分钟连贯、高保真且带人声演唱的多样化歌曲，并支持按艺术家、风格与歌词控制。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| tackle | v. | 应对、处理（难题） | "We tackle the long context of raw audio" |
| compress | v. | 压缩（把音频压成离散码） | "to compress it to discrete codes" |
| discrete | adj. | 离散的（不连续的符号码） | "compress it to discrete codes, and modeling" |
| at scale | phr. | 大规模地（模型放大后） | "the combined model at scale can generate" |
| high-fidelity | adj. | 高保真的（音质还原度高） | "can generate high-fidelity and diverse songs" |
| coherence | n. | 连贯性（音乐的连贯） | "with coherence up to multiple minutes" |
| steer | v. | 引导、控制（引导风格方向） | "to steer the musical and vocal style" |
| vocal | adj. | 人声的（演唱风格） | "the musical and vocal style, and on" |
| unaligned | adj. | 未对齐的（歌词与音频没有严格对齐） | "and on unaligned lyrics to make the" |
| lyrics | n. | 歌词 | "unaligned lyrics to make the singing more" |
| controllable | adj. | 可控的（更容易控制） | "make the singing more controllable" |
| cherry-picked | adj. | 精心挑选的（只挑好听样本展示） | "thousands of non cherry-picked samples at" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 04-06 DiffWave: A Versatile Diffusion Model for Audio Synthesis

- [ ] 已读

**中文标题**：DiffWave：多用途音频合成扩散模型

**一句话概括**：提出非自回归的扩散概率波形生成模型 DiffWave，通过马尔可夫链以固定步数把白噪声转换为结构化波形，在神经声码、条件与无条件生成等任务上达到与 WaveNet 相当的语音质量且快数个数量级。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| versatile | adj. | 多功能的、通用的（适用多种任务） | "we propose DiffWave, a versatile diffusion probabilistic" |
| diffusion | n. | 扩散（扩散模型：逐步去噪生成） | "a versatile diffusion probabilistic model for conditional" |
| conditional | adj. | 有条件的（给定条件生成） | "for conditional and unconditional waveform generation" |
| unconditional | adj. | 无条件的（不给定条件直接生成） | "conditional and unconditional waveform generation" |
| non-autoregressive | adj. | 非自回归的（一次并行生成全部样本） | "The model is non-autoregressive, and converts the" |
| Markov chain | phr. | 马尔可夫链（状态只依赖前一状态的随机过程） | "through a Markov chain with a constant" |
| likelihood | n. | 似然（数据出现的概率） | "a variant of variational bound on the data likelihood" |
| vocoding | n. | 声码合成（从声学特征合成语音） | "including neural vocoding conditioned on mel spectrogram" |
| mel spectrogram | phr. | 梅尔频谱图（按梅尔刻度划分的频谱图） | "neural vocoding conditioned on mel spectrogram" |
| in terms of | phr. | 在…方面 | "in terms of speech quality (MOS: 4.44" |
| diversity | n. | 多样性（生成样本的丰富程度） | "audio quality and sample diversity from various" |
| evaluation | n. | 评估（自动与人工评测） | "from various automatic and human evaluations" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 04-07 AudioLM: a Language Modeling Approach to Audio Generation

- [ ] 已读

**中文标题**：AudioLM：音频生成的语言建模方法

**一句话概括**：提出把输入音频映射为离散词元、把音频生成当作语言建模任务的框架，并设计混合分词方案兼顾重建质量与长程结构，可在无任何标注下生成连贯、保留说话人身份的语音与钢琴续奏。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| consistency | n. | 一致性（长期保持一致） | "audio generation with long-term consistency" |
| token | n. | 词元、令牌（离散符号单元） | "to a sequence of discrete tokens and" |
| cast | v. | 将…视为（把任务表述为另一种形式） | "casts audio generation as a language modeling" |
| trade-off | n. | 权衡（两类指标之间的取舍） | "tokenizers provide different trade-offs between reconstruction" |
| leverage | v. | 利用（借助已有成果） | "we leverage the discretized activations of a" |
| discretized | adj. | 离散化的（连续值变成离散值） | "the discretized activations of a masked language" |
| codec | n. | 编解码器（压缩/解压音频的模块） | "produced by a neural audio codec to" |
| synthesis | n. | 合成（音频合成） | "to achieve high-quality synthesis. By training" |
| corpus | n. | 语料库（大批原始音频） | "By training on large corpora of raw audio" |
| transcript | n. | 转写文本（语音的文字记录） | "without any transcript or annotation, AudioLM generates" |
| prosody | n. | 韵律（语音的节奏与语调） | "speaker identity and prosody for unseen speakers" |
| symbolic | adj. | 符号的（如乐谱等符号表示） | "without any symbolic representation of music" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 04-08 AudioGen: Textually Guided Audio Generation

- [ ] 已读

**中文标题**：AudioGen：文本引导的音频生成

**一句话概括**：提出以文本描述为条件、基于学习到的离散音频表示的自回归生成模型 AudioGen，通过音频混合增强、多流建模与无分类器引导应对源分离、数据稀缺、序列过长等挑战，在客观与主观指标上均优于基线。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| tackle | v. | 应对、解决（问题） | "We tackle the problem of generating audio" |
| condition on | phr. | 以…为条件（生成时给定文本输入） | "generating audio samples conditioned on descriptive text" |
| auto-regressive | adj. | 自回归的（逐个预测生成） | "we propose AaudioGen, an auto-regressive generative model" |
| pose | v. | 带来、构成（任务带来多重挑战） | "text-to-audio generation poses multiple challenges" |
| differentiate | v. | 区分（分离同时说话的多个人） | "differentiating ``objects'' can be a difficult" |
| scarce | adj. | 稀少的（文本标注不足） | "Scarce text annotations impose another constraint" |
| impose | v. | 施加（标注稀缺带来约束） | "text annotations impose another constraint, limiting the" |
| alleviate | v. | 缓解（缓解上述挑战） | "To alleviate the aforementioned challenges we propose" |
| curate | v. | 整理、汇集（收集并筛选数据集） | "We curated 10 datasets containing different types" |
| bitrate | n. | 比特率（每秒传输的数据量） | "maintaining a similar bitrate and perceptual quality" |
| perceptual | adj. | 感知的（人耳听感层面的质量） | "a similar bitrate and perceptual quality" |
| adherence | n. | 贴合度（生成内容对文本的遵从程度） | "guidance to improve adherence to text" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 04-09 MusicLM: Generating Music From Text

- [ ] 已读

**中文标题**：MusicLM：从文本生成音乐

**一句话概括**：提出分层序列到序列的音乐生成模型 MusicLM，可在 24kHz 采样率下生成与文本描述高度一致、持续数分钟的高保真音乐，并发布含 5.5k 条专家撰写描述的 MusicCaps 评测数据集。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| high-fidelity | adj. | 高保真的（音质还原度高） | "a model generating high-fidelity music from text" |
| violin | n. | 小提琴 | "such as "a calming violin melody backed" |
| melody | n. | 旋律 | "a calming violin melody backed by a" |
| distorted | adj. | 失真的（电吉他失真音色） | "backed by a distorted guitar riff" |
| riff | n. | 即兴乐段（riff，吉他反复演奏的短乐句） | "by a distorted guitar riff" |
| hierarchical | adj. | 分层的（多级建模） | "as a hierarchical sequence-to-sequence modeling task" |
| sequence-to-sequence | adj. | 序列到序列的（输入输出都是序列） | "hierarchical sequence-to-sequence modeling task, and it" |
| consistent | adj. | 一致的（音乐保持连贯） | "that remains consistent over several minutes" |
| adherence | n. | 遵从、贴合（与文本描述的贴合度） | "in audio quality and adherence to the" |
| whistled | adj. | 吹口哨的 | "it can transform whistled and hummed melodies" |
| hummed | adj. | 哼唱的 | "transform whistled and hummed melodies according to" |
| caption | n. | 说明文字（描述音乐的文本） | "described in a text caption" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 04-10 Make-An-Audio: Text-To-Audio Generation with Prompt-Enhanced Diffusion Models

- [ ] 已读

**中文标题**：Make-An-Audio：提示增强扩散模型的文生音频

**一句话概括**：提出提示增强的扩散模型：用"蒸馏-再编程"的伪提示增强缓解数据稀缺，用频谱自编码器预测自监督表示而非波形，实现高质量文本到音频生成，并首次解锁 X-to-Audio 多模态输入生成。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| milestone | n. | 里程碑（标志性成果） | "has created milestones in text-to-image" |
| lag behind | phr. | 落后于（音频进展滞后） | "Its application to audio still lags behind" |
| prompt | n. | 提示（词）（引导生成的文本输入） | "with a prompt-enhanced diffusion model that addresses" |
| alleviate | v. | 缓解（减轻问题） | "it alleviates data scarcity with orders of" |
| scarcity | n. | 稀缺（数据不足） | "alleviates data scarcity with orders of magnitude" |
| self-supervised | adj. | 自监督的（无需人工标签） | "predict the self-supervised audio representation instead" |
| robust | adj. | 稳健的（鲁棒性强） | "Together with robust contrastive language-audio pretraining" |
| objective | adj. | 客观的（客观指标评测） | "in both objective and subjective benchmark evaluation" |
| subjective | adj. | 主观的（人工听感评测） | "objective and subjective benchmark evaluation" |
| controllability | n. | 可控性（可控制生成结果） | "we present its controllability and generalization for" |
| generalization | n. | 泛化能力（推广到新输入的能力） | "its controllability and generalization for X-to-Audio" |
| modality | n. | 模态（输入数据的类型） | "given a user-defined modality input" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 04-11 AudioLDM: Text-to-Audio Generation with Latent Diffusion Models

- [ ] 已读

**中文标题**：AudioLDM：基于潜在扩散模型的文生音频

**一句话概括**：提出在 CLAP 潜在空间中训练潜在扩散模型 AudioLDM，无需显式建模跨模态关系即可学习音频表示，在生成质量与计算效率上均有优势，并首次支持零样本的文本引导音频操控（如风格迁移）。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| synthesize | v. | 合成（生成音频） | "its ability to synthesize general audio based" |
| latent | adj. | 潜在的（隐空间） | "a TTA system that is built on a latent space" |
| embedding | n. | 嵌入（向量表示） | "train LDMs with audio embedding while providing" |
| cross-modal | adj. | 跨模态的（音频与文本之间） | "without modeling the cross-modal relationship" |
| advantageous | adj. | 有优势的（两方面都更好） | "AudioLDM is advantageous in both generation quality" |
| metric | n. | 指标（评测标准） | "measured by both objective and subjective metrics" |
| manipulation | n. | 操控、编辑（对音频的加工） | "various text-guided audio manipulations (e.g., style transfer)" |
| style transfer | phr. | 风格迁移（把音频换成另一种风格） | "audio manipulations (e.g., style transfer) in a" |
| zero-shot | adj. | 零样本的（无需针对任务训练即可用） | "in a zero-shot fashion. Our implementation and" |
| computational | adj. | 计算的（计算效率） | "in both generation quality and computational efficiency" |
| gain attention | phr. | 受到关注 | "has recently gained attention for its ability" |
| continuous | adj. | 连续的（连续的音频表示） | "learn the continuous audio representations from contrastive" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 04-12 AudioLDM 2: Learning Holistic Audio Generation with Self-supervised Pretraining

- [ ] 已读

**中文标题**：AudioLDM 2：自监督预训练的整体音频生成

**一句话概括**：提出对语音、音乐、音效使用同一套方法的统一音频生成框架：用自监督的 AudioMAE 把任意音频翻译为"音频的语言"（LOA）表示，再用 GPT-2 把各模态输入转为 LOA，并以 LOA 为条件训练潜在扩散模型，在文生音频、文生音乐、文生语音基准上达到最优或相当性能。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| commonality | n. | 共性（不同类型音频之间的共同点） | "shares commonalities across different types of audio" |
| objective | n. | 目标（针对各类型设计的具体目标） | "careful consideration of specific objectives and biases" |
| bias | n. | 偏差（不同任务特有的倾向） | "of specific objectives and biases that can" |
| unified | adj. | 统一的（用同一方法统一处理） | "closer to a unified perspective of audio" |
| perspective | n. | 视角（统一看待音频生成的角度） | "a unified perspective of audio generation" |
| utilize | v. | 利用（采用同一种学习方法） | "a framework that utilizes the same learning method" |
| translate | v. | 转换（把音频转成 LOA 表示） | "Any audio can be translated into LOA" |
| modality | n. | 模态（文本、图像等输入类型） | "we translate any modalities into LOA by" |
| in-context | adj. | 上下文内的（上下文学习能力） | "such as in-context learning abilities and reusable" |
| reusable | adj. | 可复用的（预训练模型可重复使用） | "abilities and reusable self-supervised pretrained AudioMAE" |
| benchmark | n. | 基准（标准评测集） | "Experiments on the major benchmarks of text-to-audio" |
| competitive | adj. | 有竞争力的（与最优水平相当） | "state-of-the-art or competitive performance against previous" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 04-13 Simple and Controllable Music Generation

- [ ] 已读

**中文标题**：简单可控的音乐生成

**一句话概括**：提出 MusicGen，用单阶段 Transformer 语言模型加高效词元交错模式替代级联多个模型的做法，可基于文本描述或旋律特征生成高质量单声道与立体声音乐，并在标准基准上优于基线。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| tackle | v. | 应对、处理（任务） | "We tackle the task of conditional music" |
| stream | n. | 流（并行的码流） | "operates over several streams of compressed" |
| compressed | adj. | 压缩的（压缩后的离散表示） | "streams of compressed discrete music representation" |
| interleaving | n. | 交错（把多个码流交错排列的模式） | "efficient token interleaving patterns, which eliminates" |
| eliminate | v. | 消除（不再需要） | "which eliminates the need for cascading several" |
| cascade | v. | 级联（串联多个模型） | "the need for cascading several models, e.g" |
| mono | adj. | 单声道的 | "high-quality samples, both mono and stereo" |
| stereo | adj. | 立体声的 | "both mono and stereo, while being conditioned" |
| melodic | adj. | 旋律的（旋律特征） | "conditioned on textual description or melodic features" |
| extensive | adj. | 大量的、广泛的（大规模实验） | "We conduct extensive empirical evaluation, considering both" |
| shed light on | phr. | 阐明、使…更清楚（本文原句用 over） | "we shed light over the importance of" |
| ablation | n. | 消融（消融实验） | "Through ablation studies, we shed light over" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 04-14 Mustango: Toward Controllable Text-to-Music Generation

- [ ] 已读

**中文标题**：Mustango：迈向可控的文本到音乐生成

**一句话概括**：提出基于扩散、融入音乐领域知识的文生音乐系统 Mustango，其核心 MuNet 引导模块可在逆向扩散过程中加入和弦、节拍、速度、调性等音乐条件，并发布含 5.2 万条乐理描述样本的 MusicBench 数据集。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| controllability | n. | 可控性（对生成结果的控制能力） | "The controllability of various musical aspects, however" |
| barely | adv. | 几乎不（很少被探索） | "however, has barely been explored" |
| chord | n. | 和弦 | "instructions related to chords, beats, tempo, and key" |
| tempo | n. | 速度（音乐的快慢） | "related to chords, beats, tempo, and key" |
| key | n. | 调性（音乐的调） | "to chords, beats, tempo, and key" |
| steer | v. | 引导（引导生成方向） | "guidance module that steers the generated music" |
| reverse diffusion | phr. | 逆向扩散（扩散模型生成时的去噪过程） | "during the reverse diffusion process" |
| harmonic | adj. | 和声的（和弦方面） | "altering the harmonic, rhythmic, and dynamic aspects" |
| rhythmic | adj. | 节奏的 | "harmonic, rhythmic, and dynamic aspects of music" |
| dynamic | adj. | 力度的（音乐强弱变化） | "rhythmic, and dynamic aspects of music audio" |
| extract | v. | 提取（提取音乐特征） | "methods to extract the music features which" |
| append | v. | 附加（把特征附到描述文本后） | "will then be appended to the existing" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 04-15 VampNet: Music Generation via Masked Acoustic Token Modeling

- [ ] 已读

**中文标题**：VampNet：基于掩蔽声学词元建模的音乐生成

**一句话概括**：提出非自回归的掩蔽声学词元模型 VampNet，训练时用可变掩蔽调度、推理时用不同"提示"采样，仅 36 次采样即可生成连贯高保真波形，并可通过提示实现压缩、修补、外扩、续写与循环变奏。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| masked | adj. | 掩蔽的（遮盖部分词元让模型预测） | "we introduce VampNet, a masked acoustic token" |
| acoustic | adj. | 声学的（声音层面的） | "a masked acoustic token modeling approach to" |
| inpainting | n. | 修补、填充（补全中间缺失的部分） | "music synthesis, compression, inpainting, and variation" |
| variation | n. | 变奏（对主题的变化重复） | "compression, inpainting, and variation. We use" |
| inference | n. | 推理（模型使用时） | "of masking approaches (called prompts) during inference" |
| bidirectional | adj. | 双向的（同时看到前后文） | "leveraging a bidirectional transformer architecture that attends" |
| forward pass | phr. | 前向传播（一次完整的前向计算） | "attends to all tokens in a forward pass" |
| outpainting | n. | 外扩填充（向外续写缺失部分） | "inpainting, outpainting, continuation, and looping with" |
| looping | n. | 循环（循环播放片段） | "continuation, and looping with variation (vamping)" |
| instrumentation | n. | 配器（乐器配置） | "maintaining style, genre, instrumentation, and other" |
| flexible | adj. | 灵活的（提示方式灵活） | "This flexible prompting capability makes VampNet" |
| co-creation | n. | 共同创作（人与 AI 协作创作） | "a powerful music co-creation tool" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 04-16 Symphony: Bidirectional Language-Music Modeling

- [ ] 已读

**中文标题**：Symphony：双向语言-音乐建模

**一句话概括**：提出基于大语言模型的双向语言-音乐建模框架 Symphony：把音乐编码为离散词元，用统一的大语言模型既支持文本条件生成音乐（text-to-music），也支持音乐理解与描述生成（music-to-text），并在音乐生成与理解任务上展示效果。（无官方 abstract，基于标题与领域知识）

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| bidirectional | adj. | 双向的（文本→音乐与音乐→文本两个方向） | （无官方 abstract，基于标题与领域知识） |
| tokenization | n. | 词元化（把音乐/文本切成离散词元序列） | （无官方 abstract，基于标题与领域知识） |
| discrete | adj. | 离散的（音乐以离散词元而非连续波形表示） | （无官方 abstract，基于标题与领域知识） |
| autoregressive | adj. | 自回归的（逐个词元预测生成） | （无官方 abstract，基于标题与领域知识） |
| conditioning | n. | 条件（生成时给定文本/音乐提示作为条件） | （无官方 abstract，基于标题与领域知识） |
| alignment | n. | 对齐（文本语义与音乐片段的对应关系） | （无官方 abstract，基于标题与领域知识） |
| prompt | n. | 提示（词）（引导生成的文本输入） | （无官方 abstract，基于标题与领域知识） |
| captioning | n. | 描述生成（为音乐自动生成文字描述） | （无官方 abstract，基于标题与领域知识） |
| generation | n. | 生成（音乐生成任务） | （无官方 abstract，基于标题与领域知识） |
| coherence | n. | 连贯性（长篇幅音乐的结构连贯） | （无官方 abstract，基于标题与领域知识） |
| fine-tuning | n. | 微调（在下游任务上继续训练） | （无官方 abstract，基于标题与领域知识） |
| zero-shot | adj. | 零样本的（无需微调即可完成新任务） | （无官方 abstract，基于标题与领域知识） |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 04-17 Stable Audio Open

- [ ] 已读

**中文标题**：Stable Audio Open（开放版）

**一句话概括**：发布用 Creative Commons 数据训练的开放权重文生音频模型，性能在多项指标上与现有最优方法相当，并展示其在 44.1kHz 高保真立体声合成上的潜力。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| vitally | adv. | 极其、至关重要地 | "Open generative models are vitally important for" |
| fine-tune | n. | 微调（在模型基础上继续训练） | "allowing for fine-tunes and serving as baselines" |
| baseline | n. | 基线（作对比的模型） | "and serving as baselines when presenting new" |
| accessible | adj. | 可获取的（可公开使用） | "are private and not accessible for artists" |
| build upon | phr. | 在此基础上构建（二次开发） | "and researchers to build upon" |
| open-weights | adj. | 开放权重的（模型权重公开） | "a new open-weights text-to-audio model trained" |
| competitive | adj. | 有竞争力的（与最优相当） | "the model's performance is competitive with the" |
| metric | n. | 指标（评测标准） | "the state-of-the-art across various metrics" |
| realism | n. | 真实感（生成音频的真实程度） | "measuring the realism of the generations" |
| showcase | v. | 展示（体现潜力） | "results showcase its potential for high-quality" |
| stereo | adj. | 立体声的 | "for high-quality stereo sound synthesis at" |
| synthesis | n. | 合成（声音合成） | "stereo sound synthesis at 44.1kHz" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 04-18 SoundStream: An End-to-End Neural Audio Codec

- [ ] 已读

**中文标题**：SoundStream：端到端神经音频编解码器

**一句话概括**：提出全卷积编码器-解码器加残差矢量量化、端到端联合训练的神经音频编解码器，通过结构化 dropout 让单一模型支持 3–18kbps 可变码率，并可在智能手机 CPU 上实时流式推理。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| codec | n. | 编解码器（压缩与还原音频的系统） | "SoundStream, a novel neural audio codec that" |
| compress | v. | 压缩（降低数据量） | "can efficiently compress speech, music and general" |
| bitrate | n. | 比特率（每秒传输的比特数） | "at bitrates normally targeted by speech-tailored codecs" |
| residual | adj. | 残差的（对残差进行量化） | "and a residual vector quantizer, which are" |
| end-to-end | adv. | 端到端地（整体联合训练） | "which are trained jointly end-to-end" |
| adversarial | adj. | 对抗的（对抗训练的损失） | "which combine adversarial and reconstruction losses to" |
| dropout | n. | 随机失活（dropout 正则化技术） | "By training with structured dropout applied to" |
| negligible | adj. | 可忽略的（质量损失极小） | "with a negligible quality loss when compared" |
| amenable | adj. | 适合的、易于实现的 | "the model is amenable to a low" |
| latency | n. | 延迟（处理等待时间） | "a low latency implementation, which supports streamable" |
| streamable | adj. | 可流式处理的（边接收边解码） | "which supports streamable inference and runs in" |
| suppression | n. | 抑制（降噪） | "through background noise suppression for speech" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 04-19 High Fidelity Neural Audio Compression

- [ ] 已读

**中文标题**：高保真神经音频压缩

**一句话概括**：提出流式编码器-解码器加量化潜在空间的端到端高保真神经音频编解码器 EnCodec，引入多尺度频谱对抗与损失均衡机制稳定训练，主观评测在语音与音乐上均优于基线，并可进一步用轻量 Transformer 压缩表示。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| real-time | adj. | 实时的（能实时运行） | "a state-of-the-art real-time, high-fidelity, audio codec" |
| high-fidelity | adj. | 高保真的（音质还原度高） | "real-time, high-fidelity, audio codec leveraging neural" |
| consist in | phr. | 在于（由…构成） | "It consists in a streaming encoder-decoder architecture" |
| quantized | adj. | 量化的（离散化的潜在空间） | "architecture with quantized latent space trained in" |
| artifact | n. | 伪影（压缩产生的失真痕迹） | "that efficiently reduces artifacts and produce high-quality" |
| stabilize | v. | 稳定（训练过程） | "a novel loss balancer mechanism to stabilize training" |
| decouple | v. | 解耦（把参数选择与损失量级分开） | "thus decoupling the choice of this hyper-parameter" |
| perceptual | adj. | 感知的（基于人耳听感的损失） | "a study of various perceptual loss functions" |
| bandwidth | n. | 带宽（频率范围/码率范围） | "for a range of bandwidths and audio domains" |
| reverberant | adj. | 混响的（带回声的） | "including speech, noisy-reverberant speech, and music" |
| monophonic | adj. | 单声道的 | "considering both 24 kHz monophonic and 48 kHz" |
| stereophonic | adj. | 立体声的 | "24 kHz monophonic and 48 kHz stereophonic audio" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

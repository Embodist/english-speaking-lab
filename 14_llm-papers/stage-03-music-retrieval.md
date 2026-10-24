---
type: paper-vocabulary
stage: 3
title: "阶段 3 · 音乐检索与理解 论文词汇"
tags: [topic/paper, skill/reading, status/learning]
created: 2026-10-24
---

# 阶段 3 · 音乐检索与理解 论文词汇

> 17 篇 · 199 个词条。读前扫词 2 分钟；读后遮住中文，用 abstract 片段自测，再用 5 个词复述 60 秒。
> 返回 [[14_llm-papers/_index|LLM 论文阅读]]；配套 [[14_llm-papers/reading-workflow|阅读与词汇流程]]。

## 03-00 Automatic tagging using deep convolutional neural networks

- [ ] 已读

**中文标题**：使用深度卷积神经网络进行自动标注

**一句话概括**：提出基于内容的音乐自动标注算法，只用二维卷积与下采样层组成不同网络结构，在 MagnaTagATune 上以梅尔频谱图输入取得当时最优性能，并证明更复杂的模型受益于更多训练数据。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| tagging | n. | （音乐）标注、打标签 | "automatic music tagging algorithm using fully" |
| content-based | adj. | 基于内容的（依据音频本身特征而非元数据） | "a content-based automatic music tagging algorithm" |
| convolutional | adj. | 卷积的（神经网络中的卷积运算） | "using fully convolutional neural networks" |
| architecture | n. | 网络结构、架构 | "We evaluate different architectures consisting of" |
| subsampling | n. | 下采样（降低特征维度的操作） | "2D convolutional layers and subsampling layers only" |
| measure | v. | 衡量、测定（指标） | "we measure the AUC-ROC scores of the architectures" |
| complexity | n. | 复杂度（此处指网络规模） | "with different complexities and input types" |
| state-of-the-art | adj. | 最先进的、当时最优的 | "shows state-of-the-art performance with mel-spectrogram" |
| outperform | v. | 表现优于、胜过 | "deeper models outperformed the 4-layer architecture" |
| effective | adj. | 有效的 | "mel-spectrogram is an effective time-frequency representation" |
| benefit from | phr. | 受益于 | "more complex models benefit from more training data" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 03-01 Convolutional Recurrent Neural Networks for Music Classification

- [ ] 已读

**中文标题**：用于音乐分类的卷积循环神经网络

**一句话概括**：提出结合 CNN 局部特征提取与 RNN 时序汇总的 CRNN 音乐标注模型，在控制参数数量的前提下，其性能与训练效率均优于三种纯 CNN 结构。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| introduce | v. | 提出、引入（新方法） | "We introduce a convolutional recurrent neural network" |
| recurrent | adj. | 循环的（循环神经网络中的"循环"） | "convolutional recurrent neural network (CRNN) for music tagging" |
| take advantage of | phr. | 利用、发挥…的优势 | "CRNNs take advantage of convolutional neural networks" |
| extraction | n. | 提取（特征提取） | "for local feature extraction and recurrent neural networks" |
| temporal | adj. | 时间上的、时序的 | "recurrent neural networks for temporal summarisation" |
| summarisation | n. | 汇总、概括（把时序信息压缩成摘要） | "temporal summarisation of the extracted features" |
| with respect to | phr. | 就…而言、关于 | "with respect to their performance and training time" |
| indicate | v. | 表明、显示（结论） | "indicating the effectiveness of its hybrid structure" |
| hybrid | adj. | 混合的（此处指 CNN+RNN 的混合结构） | "effectiveness of its hybrid structure in music feature" |
| overall | adv. | 总体而言 | "Overall, we found that CRNNs show a strong" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 03-02 Toward Interpretable Music Tagging with Self-Attention

- [ ] 已读

**中文标题**：迈向可解释的基于自注意力的音乐标注

**一句话概括**：提出基于自注意力的深度序列模型用于音乐标注：浅层卷积层后接堆叠的 Transformer 编码器，相比全卷积或循环网络更可解释，同时在 MagnaTagATune 与 Million Song Dataset 上取得有竞争力的结果。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| interpretable | adj. | 可解释的（能看清模型决策依据） | "our model is more interpretable while reporting" |
| self-attention | n. | 自注意力（让序列中每个位置关注其他位置的机制） | "Self-attention is an attention mechanism that" |
| relate | v. | 关联、建立联系（把序列中不同位置联系起来） | "by relating different positions in the sequence" |
| solely | adv. | 仅仅、完全（只基于自注意力） | "a sequence model solely based on self-attention" |
| variant | n. | 变体（Transformer 的各种改进版本） | "and its variants achieved state-of-the-art results" |
| semantics | n. | 语义（音乐表达的意义） | "music composes its semantics based on the" |
| sparse | adj. | 稀疏的（音乐中相关成分分布分散） | "relations between components in sparse positions" |
| retrieval | n. | 检索（音乐信息检索 MIR） | "to solve music information retrieval (MIR) problems can be beneficial" |
| architecture | n. | 网络结构、架构 | "The proposed architecture consists of shallow" |
| stacked | adj. | 堆叠的（多层叠放的编码器） | "followed by stacked Transformer encoders" |
| conventional | adj. | 常规的、传统的（既有方法） | "Compared to conventional approaches using fully convolutional" |
| validate | v. | 验证（用数据集检验性能） | "We validate the performance of our model" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 03-03 Transfer learning for music classification and regression tasks

- [ ] 已读

**中文标题**：面向音乐分类与回归任务的迁移学习

**一句话概括**：提出把预训练卷积网络多层特征图的激活值拼接成通用音乐特征向量，迁移到其他音乐分类与回归任务后，全面优于 MFCC 基线特征及多种聚合 MFCC 的既有方法。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| transfer learning | phr. | 迁移学习（把某任务学到的知识用于另一任务） | "we present a transfer learning approach for" |
| regression | n. | 回归（预测连续数值的任务） | "music classification and regression tasks" |
| propose | v. | 提出（方法） | "We propose to use a pre-trained convnet" |
| pre-trained | adj. | 预训练的（先在别的任务上训练好的） | "use a pre-trained convnet feature, a concatenated" |
| concatenated | adj. | 拼接的、串联的（把向量连在一起） | "a concatenated feature vector using the activations" |
| activation | n. | 激活值（网络层输出的数值） | "the activations of feature maps of multiple" |
| general-purpose | adj. | 通用的（适用于多种任务） | "can serve as general-purpose music representation" |
| transfer | v. | 迁移（把模型用到新任务） | "and then transferred to other music-related classification" |
| outperform | v. | 优于、超过（基线） | "The convnet feature outperforms the baseline MFCC" |
| baseline | n. | 基线、基准（作对比的最简单方法） | "outperforms the baseline MFCC feature in all" |
| aggregate | v. | 聚合（把多个特征合并统计） | "approaches that are aggregating MFCCs as well" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 03-04 FMA: A Dataset For Music Analysis

- [ ] 已读

**中文标题**：FMA：用于音乐分析的数据集

**一句话概括**：介绍 Free Music Archive（FMA）开放数据集：包含 917 GiB、共 34.3 万天时长的创用 CC 许可音频，来自 10.6 万首曲目并按 161 个流派的层次分类组织，同时提供预计算特征、元数据与标签，可用于多种音乐信息检索任务。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| accessible | adj. | 易获取的（开放且方便使用） | "an open and easily accessible dataset suitable" |
| suitable | adj. | 适合的（适用于评测多项任务） | "a dataset suitable for evaluating several tasks" |
| concerned with | phr. | 涉及、与…相关（研究领域关注的内容） | "a field concerned with browsing, searching, and" |
| organize | v. | 整理、组织（管理大规模音乐库） | "searching, and organizing large music collections" |
| restrained | adj. | 受限制的（发展被数据缺乏所制约） | "is however restrained by the limited availability" |
| availability | n. | 可用性、可获得性 | "by the limited availability of large audio datasets" |
| hurdle | n. | 障碍、难关（需要克服的问题） | "The FMA aims to overcome this hurdle" |
| hierarchical | adj. | 层次的（按等级结构分类） | "arranged in a hierarchical taxonomy of 161 genres" |
| taxonomy | n. | 分类体系（类别的树状结构） | "a hierarchical taxonomy of 161 genres" |
| metadata | n. | 元数据（描述数据的数据） | "track- and user-level metadata, tags, and free-form" |
| split | n. | 划分（训练/验证/测试集的切分） | "propose a train/validation/test split and three" |
| baseline | n. | 基线（作对比的最简单方法） | "evaluate some baselines for genre recognition" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 03-05 Audio Set: An ontology and human-labeled dataset for audio events

- [ ] 已读

**中文标题**：Audio Set：面向音频事件的 ontology（本体分类体系）与人工标注数据集

**一句话概括**：描述 Audio Set 数据集的构建：基于文献与人工整理出含 632 个音频类别的层次化本体分类体系，再请人工标注员判断 YouTube 视频 10 秒片段中各音频类别的存在与否，以填补图像与音频研究在数据可用性上的差距。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| ontology | n. | 本体（类别的结构化分类体系） | "a carefully structured hierarchical ontology of 632" |
| recognition | n. | 识别（音频事件识别任务） | "Audio event recognition, the human-like ability to" |
| nascent | adj. | 新兴的、初期的（尚在起步阶段） | "is a nascent problem in machine perception" |
| comparable | adj. | 类似的、可比的（与之相当的问题） | "Comparable problems such as object detection" |
| reap | v. | 收获（获得巨大收益） | "have reaped enormous benefits from comprehensive datasets" |
| comprehensive | adj. | 全面的、大规模的（数据集） | "enormous benefits from comprehensive datasets - principally" |
| manually-annotated | adj. | 人工标注的（由人来打标签） | "a large-scale dataset of manually-annotated audio events" |
| endeavor | v. | 努力、致力于（试图做到某事） | "that endeavors to bridge the gap in" |
| bridge the gap | phr. | 弥合差距（填补数据不足的空缺） | "endeavors to bridge the gap in data" |
| hierarchical | adj. | 层次的（分类体系的层级结构） | "carefully structured hierarchical ontology of 632 audio" |
| curation | n. | 整理、筛选（人工把关挑选） | "guided by the literature and manual curation" |
| probe | v. | 探查、检测（判断类别是否存在） | "we collect data from human labelers to probe" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 03-06 Enabling Factorized Piano Music Modeling and Generation with the MAESTRO Dataset

- [ ] 已读

**中文标题**：利用 MAESTRO 数据集实现分解式钢琴音乐建模与生成

**一句话概括**：提出以音符作为中间表示（Wave2Midi2Wave 流程），训练能够转写、作曲并合成音频波形、跨越约六个数量级时间尺度的模型，并发布含 172 小时高精度对齐钢琴演奏的 MAESTRO 数据集。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| notoriously | adv. | 出了名地（公认地困难） | "directly with neural networks is notoriously difficult" |
| coherently | adv. | 连贯地（一致地建模多尺度结构） | "because it requires coherently modeling structure at" |
| timescale | n. | 时间尺度（不同长短的时间跨度） | "structure at many different timescales" |
| discrete | adj. | 离散的（一个个独立的音符事件） | "can be represented as discrete note events" |
| intermediate | adj. | 中间的（介于音频与语义之间的表示） | "using notes as an intermediate representation" |
| suite | n. | 一套、一组（系列模型） | "we can train a suite of models capable" |
| transcribe | v. | 转写（把音频转成音符序列） | "models capable of transcribing, composing, and synthesizing" |
| synthesize | v. | 合成（从音符生成音频波形） | "composing, and synthesizing audio waveforms with" |
| span | v. | 跨越（覆盖从毫秒到百秒的范围） | "on timescales spanning six orders of magnitude" |
| order of magnitude | phr. | 数量级（相差约 10 倍） | "spanning six orders of magnitude (~0.1 ms" |
| virtuosic | adj. | 技艺高超的（演奏家级别的） | "172 hours of virtuosic piano performances captured" |
| alignment | n. | 对齐（音符标签与波形的精确对应） | "captured with fine alignment (~3 ms) between" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 03-07 wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations

- [ ] 已读

**中文标题**：wav2vec 2.0：语音表示自监督学习框架

**一句话概括**：提出在潜在空间掩蔽语音输入、求解对比量化任务的语音表示自监督预训练框架，仅用十分钟标注数据加海量无标注数据预训练即可达到很低的词错误率，验证了少标注语音识别的可行性。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| fine-tuning | n. | 微调（在预训练基础上用标注数据再训练） | "followed by fine-tuning on transcribed speech can" |
| transcribed | adj. | 转写后的（语音对应的文字标注） | "fine-tuning on transcribed speech can outperform" |
| outperform | v. | 超越、胜过 | "can outperform the best semi-supervised methods" |
| semi-supervised | adj. | 半监督的（少量标注+大量无标注） | "the best semi-supervised methods while being conceptually" |
| conceptually | adv. | 概念上、原理上 | "methods while being conceptually simpler" |
| mask | v. | 掩蔽（遮盖部分输入让模型预测） | "wav2vec 2.0 masks the speech input in" |
| latent | adj. | 潜在的（隐空间中的特征） | "the speech input in the latent space" |
| contrastive | adj. | 对比的（对比学习任务） | "solves a contrastive task defined over" |
| quantization | n. | 量化（把连续表示映射为离散码） | "over a quantization of the latent representations" |
| jointly | adv. | 联合地（一起学习） | "latent representations which are jointly learned" |
| pre-training | n. | 预训练（先用无标注数据训练） | "pre-training on 53k hours of unlabeled data" |
| feasibility | n. | 可行性 | "demonstrates the feasibility of speech recognition" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 03-08 Look, Listen, and Learn More: Design Choices for Deep Audio Embeddings (OpenL3)

- [ ] 已读

**中文标题**：看得更多、听得更多：深度音频嵌入的设计选择（OpenL3）

**一句话概括**：系统研究 L3-Net 框架中影响音频嵌入行为的三个关键设计选择——音频嵌入架构、音视频对应关系学习目标与音频预处理，以提升该自监督嵌入在音频分类下游任务中的开箱即用表现。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| considerable | adj. | 相当大的（不小的挑战） | "A considerable challenge in applying deep learning" |
| scarcity | n. | 稀缺（标注数据不足） | "is the scarcity of labeled data" |
| increasingly | adv. | 越来越（越来越流行的做法） | "An increasingly popular solution is to learn" |
| embedding | n. | 嵌入（学习到的音频向量表示） | "learn deep audio embeddings from large audio" |
| shallow | adj. | 浅层的（结构简单的分类器） | "train shallow classifiers using small labeled datasets" |
| self-supervised | adj. | 自监督的（无需人工标签的训练方式） | "trained through self-supervised learning of audio-visual" |
| correspondence | n. | 对应关系（音频与视频内容的一致性） | "learning of audio-visual correspondence in videos as" |
| as opposed to | phr. | 与…不同、而非 | "in videos as opposed to other embeddings" |
| out-of-the-box | adj. | 开箱即用的（拿来就能用） | "produce powerful out-of-the-box embeddings for downstream" |
| downstream | adj. | 下游的（后续应用任务） | "for downstream audio classification tasks, but has" |
| impact | v. | 影响（设计选择会影响行为） | "design choices that may impact the embeddings' behavior" |
| investigate | v. | 研究、考察 | "we investigate three key design choices in" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 03-09 AST: Audio Spectrogram Transformer

- [ ] 已读

**中文标题**：AST：音频频谱图 Transformer

**一句话概括**：提出首个完全无卷积、纯注意力机制的音频分类模型 AST（音频频谱图 Transformer），回答"音频分类是否必须依赖 CNN"的问题，并在 AudioSet 等多个基准上刷新最优结果。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| adopt | v. | 采用（被广泛采用） | "have been widely adopted as the main" |
| building block | phr. | 基本构件、核心组成单元 | "as the main building block for end-to-end" |
| end-to-end | adj. | 端到端的（从输入直接学到输出） | "building block for end-to-end audio classification models" |
| mapping | n. | 映射（输入到输出的对应关系） | "learn a direct mapping from audio spectrograms" |
| capture | v. | 捕捉（获取信息） | "To better capture long-range global context" |
| long-range | adj. | 长距离的、长程的（全局上下文） | "capture long-range global context, a recent" |
| self-attention | n. | 自注意力（Transformer 的核心机制） | "add a self-attention mechanism on top of" |
| hybrid | adj. | 混合的（CNN 加注意力的组合） | "forming a CNN-attention hybrid model" |
| reliance | n. | 依赖（对 CNN 的依赖） | "whether the reliance on a CNN is" |
| purely | adv. | 纯粹地（完全基于…） | "neural networks purely based on attention" |
| benchmark | n. | 基准（标准评测数据集） | "on various audio classification benchmarks, where it" |
| accuracy | n. | 准确率 | "and 98.1% accuracy on Speech Commands" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 03-10 HTS-AT: A Hierarchical Token-Semantic Audio Transformer for Sound Classification and Detection

- [ ] 已读

**中文标题**：HTS-AT：用于声音分类与检测的分层词元-语义音频 Transformer

**一句话概括**：提出带分层结构以缩小模型规模、缩短训练时间的音频 Transformer HTS-AT，并加入词元-语义模块把输出映射为类别特征图以支持音频事件检测（时间定位），在 AudioSet、ESC-50 上取得新的最优结果且仅需原模型 35% 参数。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| hierarchical | adj. | 分层的（多层次网络结构） | "an audio transformer with a hierarchical structure" |
| token-semantic | adj. | 词元-语义的（把词元映射到语义特征） | "combined with a token-semantic module to map" |
| mapping | n. | 映射（样本到标签的对应） | "task of mapping audio samples into their" |
| corresponding | adj. | 对应的（与样本相应的标签） | "mapping audio samples into their corresponding labels" |
| adopt | v. | 采用（Transformer 被引入该领域） | "has been adopted in this field" |
| meanwhile | adv. | 与此同时（还依赖预训练视觉模型） | "and long training time, meanwhile relying on" |
| rely on | phr. | 依赖 | "meanwhile relying on pretrained vision models to" |
| scalability | n. | 可扩展性（模型在音频任务上的扩展能力） | "limits the model's scalability in audio tasks" |
| combat | v. | 应对、克服（问题） | "To combat these problems, we introduce HTS-AT" |
| localization | n. | 定位（在时间轴上确定事件位置） | "the audio event detection (i.e. localization in" |
| state-of-the-art | adj. | 最先进的（当时最优结果） | "achieves new state-of-the-art (SOTA) results on AudioSet" |
| efficiency | n. | 效率（高性能与高效率） | "the high performance and high efficiency of" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 03-11 MusicBERT: Symbolic Music Understanding with Large-Scale Pre-Training

- [ ] 已读

**中文标题**：MusicBERT：大规模预训练的符号音乐理解

**一句话概括**：构建含百万级歌曲的符号音乐语料库，提出 OctupleMIDI 编码与小节级掩蔽策略，训练大规模预训练模型 MusicBERT，在旋律补全、伴奏建议等四项音乐理解任务上取得显著优势。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| symbolic | adj. | 符号的（以 MIDI 等符号形式而非音频表示音乐） | "understanding of music from the symbolic data" |
| genre | n. | 流派、类型（音乐风格分类） | "such as genre classification, emotion classification" |
| hinder | v. | 阻碍（数据不足妨碍表示学习） | "the lack of training data hinders representation" |
| inspire | v. | 启发（受 NLP 预训练成功启发） | "Inspired by the success of pre-training models" |
| pre-training | n. | 预训练（先在大规模数据上训练通用模型） | "the success of pre-training models in natural" |
| corpus | n. | 语料库（大规模数据集） | "we construct a large-scale symbolic music corpus" |
| tempo | n. | 速度（音乐的节拍速度） | "e.g., tempo, instrument, and pitch" |
| pitch | n. | 音高（音符的高低） | "tempo, instrument, and pitch), simply adopting" |
| marginal | adj. | 微小的、边缘的（收益甚微） | "to symbolic music only brings marginal gains" |
| melody | n. | 旋律 | "including melody completion, accompaniment suggestion, genre" |
| accompaniment | n. | 伴奏 | "melody completion, accompaniment suggestion, genre classification" |
| ablation | n. | 消融（消融实验：逐一去掉组件验证作用） | "Ablation studies also verify the effectiveness of" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 03-12 MAP-Music2Vec: A Simple and Effective Baseline for Self-Supervised Music Audio Representation Learning

- [ ] 已读

**中文标题**：MAP-Music2Vec：自监督音乐音频表示学习的简单有效基线

**一句话概括**：设计 Music2Vec 框架，系统探索用于原始音乐波形的各种自监督学习组件与技巧，以不到 Jukebox 2% 的参数规模达到与其相当的音乐自监督表示学习效果。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| witness | v. | 见证（社区见证了快速增长） | "community has witnessed an exponentially growing interest" |
| exponentially | adv. | 指数级地（增长极快） | "witnessed an exponentially growing interest in self-supervised" |
| unexplored | adj. | 未探索的（尚未研究清楚） | "it still remains unexplored how to build" |
| framework | n. | 框架（完整的方案体系） | "how to build a framework for learning" |
| raw | adj. | 原始的（未经处理的音频波形） | "useful representations of raw music waveforms" |
| waveform | n. | 波形（音频信号形态） | "of raw music waveforms in a self-supervised" |
| component | n. | 组件（算法模块） | "different SSL algorithmic components and tricks for" |
| comparable | adj. | 相当的（与最优模型水平相近） | "achieves comparable results to the state-of-the-art" |
| state-of-the-art | adj. | 最先进的（音乐 SSL 最优模型） | "to the state-of-the-art (SOTA) music SSL model" |
| despite | prep. | 尽管（虽然参数少得多） | "despite being significantly smaller with less than" |
| release | v. | 发布（公开模型） | "The model will be released on Huggingface" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 03-13 Large-scale Contrastive Language-Audio Pretraining with Feature Fusion and Keyword-to-Caption Augmentation

- [ ] 已读

**中文标题**：融合特征融合与关键词到描述增强的大规模对比语言-音频预训练

**一句话概括**：发布含 63 万余对音频-文本数据的 LAION-Audio-630K 数据集，提出融入特征融合机制与关键词到描述数据增强的对比语言-音频预训练模型 CLAP，在文本到音频检索与零样本分类上取得最优性能。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| contrastive | adj. | 对比的（对比学习：拉近匹配对、推远不匹配对） | "Contrastive learning has shown remarkable success in" |
| multimodal | adj. | 多模态的（同时涉及音频与文本） | "in the field of multimodal representation learning" |
| pipeline | n. | 流程、管线（一整套处理流程） | "we propose a pipeline of contrastive language-audio" |
| pretraining | n. | 预训练 | "a pipeline of contrastive language-audio pretraining to" |
| incorporate | v. | 纳入、融合（把机制加入模型设计） | "We incorporate the feature fusion mechanism and" |
| augmentation | n. | 增强（数据增强：扩充训练数据） | "keyword-to-caption augmentation into the model design" |
| variable | adj. | 可变的（长度不一的音频输入） | "audio inputs of variable lengths and enhance" |
| comprehensive | adj. | 全面的（多角度实验） | "we perform comprehensive experiments to evaluate our" |
| retrieval | n. | 检索（根据文本查找音频） | "text-to-audio retrieval, zero-shot audio classification" |
| zero-shot | adj. | 零样本的（训练时未见过的类别也能识别） | "state-of-the-art performance in the zero-shot setting" |
| comparable | adj. | 可比的、相当的 | "performance comparable to models' results in the" |
| superior | adj. | 优越的（表现更好） | "achieves superior performance in text-to-audio retrieval" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 03-14 MERT: Acoustic Music Understanding Model with Large-Scale Self-supervised Training

- [ ] 已读

**中文标题**：MERT：大规模自监督训练的声学音乐理解模型

**一句话概括**：提出声学音乐理解模型 MERT，用教师模型在掩蔽语言建模（MLM）风格的声学预训练中提供伪标签，组合 RVQ-VAE 声学教师与 CQT 音乐教师，可扩展到 3.3 亿参数，在 14 项音乐理解任务上取得总体最优分数。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| paradigm | n. | 范式（训练通用模型的新范式） | "emerged as a promising paradigm for training" |
| generalisable | adj. | 可泛化的（能迁移到多种任务） | "for training generalisable models on large-scale data" |
| thoroughly | adv. | 彻底地（尚未被充分探索） | "has yet to be thoroughly explored" |
| distinctive | adj. | 独特的（音乐建模特有的挑战） | "partially due to the distinctive challenges associated" |
| tonal | adj. | 调性的（音乐调性特征） | "particularly tonal and pitched characteristics of music" |
| pitched | adj. | 有音高的（音高特征） | "tonal and pitched characteristics of music" |
| incorporate | v. | 纳入（把教师模型融入训练） | "which incorporates teacher models to provide pseudo" |
| pseudo | adj. | 伪的（模型生成的近似标签） | "to provide pseudo labels in the masked" |
| masked language modelling | phr. | 掩蔽语言建模（遮盖部分输入让模型预测） | "in the masked language modelling (MLM) style" |
| overcome | v. | 克服（训练不稳定的问题） | "to overcome the instability in acoustic language" |
| instability | n. | 不稳定性（预训练过程的不稳定） | "overcome the instability in acoustic language model" |
| attain | v. | 达到（取得最优总体分数） | "and attain state-of-the-art (SOTA) overall scores" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 03-15 CLaMP: Contrastive Language-Music Pre-training for Cross-Modal Symbolic Music Information Retrieval

- [ ] 已读

**中文标题**：CLaMP：面向跨模态符号音乐信息检索的对比语言-音乐预训练

**一句话概括**：提出用对比损失联合训练音乐编码器与文本编码器的 CLaMP 模型，学习自然语言与符号音乐之间的跨模态表示，实现符号音乐的语义检索与零样本分类，并发布含 1010 张 ABC 记谱主旋律谱的 WikiMusicText 数据集。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| contrastive | adj. | 对比的（对比学习损失） | "Contrastive Language-Music Pre-training, which learns cross-modal" |
| cross-modal | adj. | 跨模态的（语言与音乐两个模态之间） | "learns cross-modal representations between natural language" |
| symbolic | adj. | 符号的（以乐谱等符号形式表示的音乐） | "between natural language and symbolic music using" |
| jointly | adv. | 联合地（两个编码器一起训练） | "trained jointly with a contrastive loss" |
| dropout | n. | 随机失活（文本丢弃，作数据增强） | "It employed text dropout as a data" |
| augmentation | n. | 增强（扩充训练数据的手段） | "as a data augmentation technique and bar" |
| patching | n. | 分块（把小节拼成块以压缩序列） | "and bar patching to efficiently represent music" |
| comprehension | n. | 理解（编码器对音乐语境的把握） | "enhance the music encoder's comprehension of musical" |
| semantic | adj. | 语义的（按含义进行搜索） | "to enable semantic search and zero-shot classification" |
| zero-shot | adj. | 零样本的（无需微调即可分类新类别） | "semantic search and zero-shot classification for symbolic" |
| surpass | v. | 超越（超过以往模型的能力） | "surpassing the capabilities of previous models" |
| lead sheet | phr. | 主旋律谱（只记旋律与和弦的简谱） | "a dataset of 1010 lead sheets in ABC notation" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

## 03-16 Wav2CLIP: Learning Robust Audio Representations From CLIP

- [ ] 已读

**中文标题**：Wav2CLIP：从 CLIP 学习稳健的音频表示

**一句话概括**：提出从对比语言-图像预训练模型（CLIP）蒸馏出稳健音频表示的方法 Wav2CLIP，把音频映射到与图像、文本共享的嵌入空间，支持零样本分类与跨模态检索，且只需约 10% 数据即可达到接近全监督模型的性能。

| 词汇/短语 | 词性 | 中文释义 | abstract 原句片段 |
|---|---|---|---|
| robust | adj. | 稳健的、鲁棒的（表示质量可靠） | "Wav2CLIP, a robust audio representation learning method" |
| distill | v. | 蒸馏（把大模型知识迁移到小模型） | "learning method by distilling from Contrastive Language-Image" |
| systematically | adv. | 系统地（全面评估） | "We systematically evaluate Wav2CLIP on a variety" |
| retrieval | n. | 检索（跨模态检索任务） | "classification, retrieval, and generation, and show" |
| outperform | v. | 优于（超过公开的预训练方法） | "Wav2CLIP can outperform several publicly available" |
| project | v. | 映射（投影到共享空间） | "Wav2CLIP projects audio into a shared embedding" |
| shared | adj. | 共享的（多模态共用的嵌入空间） | "into a shared embedding space with images" |
| multimodal | adj. | 多模态的（同时涉及音频、图像、文本） | "which enables multimodal applications such as zero-shot" |
| cross-modal | adj. | 跨模态的（跨模态检索） | "zero-shot classification, and cross-modal retrieval" |
| competitive | adj. | 有竞争力的（与全监督模型接近） | "to achieve competitive performance on downstream tasks" |
| downstream | adj. | 下游的（后续任务） | "competitive performance on downstream tasks compared with" |
| qualitative | adj. | 定性的（定性评估共享空间质量） | "as qualitative assessment of the shared embedding" |

**复述任务**：用本篇 5 个词，口头总结 abstract 60 秒。

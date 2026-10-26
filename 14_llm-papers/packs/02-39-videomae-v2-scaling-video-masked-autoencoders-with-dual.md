---
type: paper-pack
paper_id: "02-39"
stage: 2
title: "VideoMAE V2: Scaling Video Masked Autoencoders with Dual Masking"
pdf: "/home/user/llm-papers/02_多模态/PDF/39_VideoMAEV2.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-39 VideoMAE V2: Scaling Video Masked Autoencoders with Dual Masking

**中文标题**：VideoMAE V2：以双重掩码扩展视频掩码自编码器

**一句话概括**：提出编码器、解码器各处理一部分 token 的双重掩码策略与渐进式训练范式，成功预训练十亿参数视频 ViT，在 Kinetics 等基准刷新 SOTA。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| downstream | /dˈaʊnstɹiːm/ | 下游的；基于预训练模型的后续任务 | S |
| generalize | /dʒˈɛnəɹəlˌaɪz/ | 泛化；迁移到多种任务 | S |
| foundation model | /faʊndˈeɪʃən mˈɒdəl/ | 基础模型；可迁移到多种下游任务的大模型 | A |
| encoder | /ɛŋkˈəʊdə/ | 编码器；处理可见 token 的网络部分 | A |
| decoder | /dɪkˈəʊdə/ | 解码器；重建被掩码内容的部分 | A |
| progressive | /pɹəɡɹˈɛsɪv/ | 渐进式的；分阶段推进的训练方式 | A |
| billion | /bˈɪliən/ | 十亿；本文模型的参数规模 | B |
| dual masking | /djˈuːəl mˈaskɪŋ/ | 双重掩码；编解码器分别掩码的策略 | B |
| subset | /sˈʌbsɛt/ | 子集；token 的一部分 | B |
| computational cost | /kˌɒmpjuːtˈeɪʃənəl kˈɒst/ | 计算成本；训练消耗的算力 | B |
| multi-sourced | /mˈʌltisˈɔːst/ | 多来源的；来自不同数据源 | B |
| extensively | /ɛkstˈɛnsɪvli/ | 广泛地；在大量下游任务上验证 | B |

### 原句（保留完整句子）

- **downstream** — “In this paradigm, it word representations by first pre-training a bidirectional often requires fine-tuning the PLM for adapting to different LSTM (biLSTM) network (instead of learning fixed word downstream tasks. representations) and then fine-tuning the biLSTM network according to specific downstream tasks.”
- **generalize** — “We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data. ∗ Equal contribution.”
- **foundation model** — “"large-scale pretrained foundation models is"”
- **encoder** — “Gomez∗ † Łukasz Kaiser∗ Google Research University of Toronto Google Brain llion@google.com aidan@cs.toronto.edu lukaszkaiser@google.com Illia Polosukhin∗ ‡ illia.polosukhin@gmail.com Abstract The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder.”
- **decoder** — “Gomez∗ † Łukasz Kaiser∗ Google Research University of Toronto Google Brain llion@google.com aidan@cs.toronto.edu lukaszkaiser@google.com Illia Polosukhin∗ ‡ illia.polosukhin@gmail.com Abstract The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder.”
- **progressive** — “Awadallah, “Orca: Progressive contamination: Accelerating large language modlearning from complex explanation traces of GPT-4,” els without impacting performance,” arXiv preprint CoRR, vol. abs/2306.02707, 2023. arXiv:2107.02027, 2021. \[341\] YuLan-Chat-Team, “Yulan-chat: An open-source \[354\] K.”
- **billion** — “To discriminate the language models in different parameter scales, the research community has coined the term large language models (LLM) for the PLMs of significant size (e.g., containing tens or hundreds of billions of parameters).”
- **dual masking** — “"we present a dual masking strategy for efficient pre-training"”
- **subset** — “The basic principle underlying GPT models is on a subset of the world text.”
- **computational cost** — “"can still further reduce the overall computational cost"”
- **multi-sourced** — “"on a diverse multi-sourced unlabeled dataset"”
- **extensively** — “In the GPT-4V’s system and to do alignment research”. card \[133\], it has extensively discussed the assessment and These enhancement techniques lead to the improved mitigation of risks related to visually augmented inputs.”

## 摘要提示（PDF 文本不可提取）

> TITLE: VideoMAE V2: Scaling Video Masked Autoencoders with Dual Masking ABSTRACT: Scale is the primary factor for building a powerful foundation model that could well generalize to a variety of downstream tasks. However, it is still challenging to train video foundation models with billions of parameters. This paper shows that video masked autoencoder (VideoMAE) is a scalable and general self-supervised pre-trainer for building video foundation models. We scale the VideoMAE in both model and data with a core design. Specifically, we present a dual masking strategy for efficient pre-training, with an encoder operating on a subset of video tokens and a decoder processing another subset of video tokens. Although VideoMAE is very efficient due to high masking ratio in encoder, masking decoder can still further reduce the overall computational cost. This enables the efficient pre-training of billion-level models in video. We also use a progressive training paradigm that involves an initial pre-training on a diverse multi-sourced unlabeled dataset, followed by a post-pre-training on a mixed labeled dataset. Finally, we successfully train a video ViT model with a billion parameters, which achieves a new state-of-the-art performance on the datasets of Kinetics (90.0% on K400 and 89.9% on K600) and Something-Something (68.7% on V1 and 77.0% on V2). In addition, we extensively verify the

## 读中 30 分钟

- [ ] 问题：这篇论文解决什么？
- [ ] 方法：核心组件和数据流是什么？
- [ ] 数据/指标：在哪些数据集、用什么指标？
- [ ] 结果：主结果和消融说明了什么？
- [ ] 局限：作者承认什么？我还有什么疑问？

## 5 个理解问题

1. What problem does the paper address, and why does it matter?
2. What is the key idea, and what does it replace or improve?
3. What data, baselines, and metrics are used?
4. Which result is the most convincing, and which is weakest?
5. What is one limitation, and what would you test next?

## 60 秒复述

> The paper addresses … The authors propose … The key idea is … They evaluate on … The results show … One limitation is …

录音：`11_attachments/`

## 写 3 句

- The paper addresses …
- The key idea is …
- One limitation is …

## 词汇复习

- 把上面 10–12 个词加入 Anki；先读原句，再看中文。
- 词库入口：[[14_llm-papers/vocabulary-10k/_index|论文 10k 词库]]

## 相关

- [[14_llm-papers/reading-plan|12 周阅读计划]]
- [[14_llm-papers/stage-02-multimodal|阶段 2]]

PDF：`/home/user/llm-papers/02_多模态/PDF/39_VideoMAEV2.pdf`

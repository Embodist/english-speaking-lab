---
type: paper-pack
paper_id: "03-07"
stage: 3
title: "wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations"
pdf: "/home/user/llm-papers/03_音乐检索理解/PDF/07_wav2vec2.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 03-07 wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations

**中文标题**：wav2vec 2.0：语音表示自监督学习框架

**一句话概括**：提出在潜在空间掩蔽语音输入、求解对比量化任务的语音表示自监督预训练框架，仅用十分钟标注数据加海量无标注数据预训练即可达到很低的词错误率，验证了少标注语音识别的可行性。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| outperform | /aʊtpəfˈɔːm/ | 超越、胜过 | S |
| latent | /lˈeɪtənt/ | 潜在的（隐空间中的特征） | S |
| contrastive | /kˈɒntɹastˌɪv/ | 对比的（对比学习任务） | S |
| fine-tuning | /fˈaɪntjˈuːnɪŋ/ | 微调（在预训练基础上用标注数据再训练） | A |
| jointly | /dʒˈɔɪntli/ | 联合地（一起学习） | A |
| pre-training | /pɹˈiːtɹˈeɪnɪŋ/ | 预训练（先用无标注数据训练） | A |
| mask | /mˈask/ | 掩蔽（遮盖部分输入让模型预测） | A |
| transcribed | /tɹanskɹˈaɪbd/ | 转写后的（语音对应的文字标注） | B |
| semi-supervised | /sˈɛmisˈuːpəvˌaɪzd/ | 半监督的（少量标注+大量无标注） | B |
| conceptually | /kənsˈɛptʃuːəli/ | 概念上、原理上 | B |
| quantization | /kwˌɒntaɪzˈeɪʃən/ | 量化（把连续表示映射为离散码） | B |
| feasibility | /fˌiːzɪbˈɪlɪti/ | 可行性 | B |

### 原句（保留完整句子）

- **outperform** — “Moreover, when we lower the amount of labeled data to just one hour, we still outperform the previous state of the art self-training method of \[42\] while using 100 times less labeled data and the same amount of unlabeled data.”
- **latent** — “Our approach encodes speech audio via a multi-layer convolutional neural network and then masks spans of the resulting latent speech representations \[26, 56\], similar to masked language modeling \[9\].”
- **contrastive** — “The latent representations are fed to a Transformer network to build contextualized representations and the model is trained via a contrastive task where the true latent is to be distinguished from distractors \[54, 49, 48, 28\] (§ 2).”
- **fine-tuning** — “We encourage the equal use of the V entries in each of the G codebooks by maximizing the entropy of the averaged softmax distribution l over the codebook entries for each 3 codebook p̄g across a batch of utterances; the softmax disribution does not contain the gumbel noise nor a temperature:2 G G V 1 X 1 XX Ld = −H(p̄g ) = p̄g,v log p̄g,v (4) GV g=1 GV g=1 v=1 3.3 Fine-tuning Pre-trained models are fine-tuned for speech recognition by adding a randomly initialized linear projection on top of the context network into C classes representing the vocabulary of the task \[4\].”
- **jointly** — “Our results show that jointly learning discrete speech units with contextualized representations achieves substantially better results than fixed units learned in a prior step \[4\].”
- **pre-training** — “Using just ten minutes of labeled data and pre-training on 53k hours of unlabeled data still achieves 4.8/8.2 WER.”
- **mask** — “3 Training To pre-train the model we mask a certain proportion of time steps in the latent feature encoder space (§ 3.1), similar to masked language modeling in BERT \[9\].”
- **transcribed** — “However, in many settings labeled data is much harder to come by than unlabeled data: current speech recognition systems require thousands of hours of transcribed speech to reach acceptable performance which is not available for the vast majority of the nearly 7,000 languages spoken worldwide \[31\].”
- **semi-supervised** — “Transducer \[60\] - Transf. - - 2.0 4.6 ContextNet \[17\] - LSTM 1.9 3.9 1.9 4.1 Conformer \[15\] - LSTM 2.1 4.3 1.9 3.9 Semi-supervised CTC Transf. + PL \[51\] LV-60k CLM+Transf.”
- **conceptually** — “Prompting with ICL and CoT is a conceptually simple yet Then, the plan executor acts according to the plan in the general approach to solving various tasks.”
- **quantization** — “The output of the feature encoder is discretized to qt with a quantization module Z 7→ Q to represent the targets (Figure 1) in the self-supervised objective (§ 3.2).”
- **feasibility** — “This demonstrates the feasibility of speech recognition with limited amounts of labeled data.1 1 Introduction Neural networks benefit from large quantities of labeled training data.”

## Abstract（自动提取）

> TITLE: wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations ABSTRACT: We show for the first time that learning powerful representations from speech audio alone followed by fine-tuning on transcribed speech can outperform the best semi-supervised methods while being conceptually simpler. wav2vec 2.0 masks the speech input in the latent space and solves a contrastive task defined over a quantization of the latent representations which are jointly learned. Experiments using all labeled data of Librispeech achieve 1.8/3.3 WER on the clean/other test sets. When lowering the amount of labeled data to one hour, wav2vec 2.0 outperforms the previous state of the art on the 100 hour subset while using 100 times less labeled data. Using just ten minutes of labeled data and pre-training on 53k hours of unlabeled data still achieves 4.8/8.2 WER. This demonstrates the feasibility of speech recognition with limited amounts of labeled data.

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
- [[14_llm-papers/stage-03-music-retrieval|阶段 3]]

PDF：`/home/user/llm-papers/03_音乐检索理解/PDF/07_wav2vec2.pdf`

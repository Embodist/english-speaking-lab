---
type: paper-pack
paper_id: "02-05"
stage: 2
title: "CoCa: Contrastive Captioners are Image-Text Foundation Models"
pdf: "/home/user/llm-papers/02_多模态/PDF/05_CoCa.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-05 CoCa: Contrastive Captioners are Image-Text Foundation Models

**中文标题**：CoCa：作为图像-文本基础模型的对比式说明生成器

**一句话概括**：提出 CoCa，用对比损失与说明生成损失联合预训练图像-文本编码器-解码器基础模型，兼收 CLIP 式对比方法与生成式方法的优点。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| downstream | /dˈaʊnstɹiːm/ | 下游的（预训练后迁移到的具体任务） | S |
| adaptation | /ˌadaptˈeɪʃən/ | 适配、调整（针对具体任务做少量修改） | S |
| jointly | /dʒˈɔɪntli/ | 联合地（两个训练目标同时进行） | A |
| embedding | /ɛmbˈɛdɪŋ/ | 嵌入（向量）（把输入映射成的稠密向量表示） | A |
| foundation model | /faʊndˈeɪʃən mˈɒdəl/ | 基础模型（大规模预训练、可迁移到多任务的模型） | A |
| subsume | /sʌbsjˈuːm/ | 涵盖、合并（一个模型同时具备两类方法的能力） | A |
| cascade | /kɐskˈeɪd/ | 级联（把剩余解码层依次串联起来） | A |
| autoregressively | /ˌɔːtəʊɹɪɡɹˈɛsɪvli/ | 自回归地（逐个预测下一个文本 token） | A |
| seamlessly | /sˈiːmləsli/ | 无缝地（把文本标签与图文数据统一处理） | A |
| minimalist | /mˈɪnɪməlˌɪst/ | 极简的（设计简单、不做多余改动） | B |
| omit | /əʊmˈɪt/ | 省略（解码器前半层不做跨注意力） | B |
| overhead | /ˌəʊvəhˈɛd/ | 开销（额外计算负担，本文指几乎为零） | B |

### 原句（保留完整句子）

- **downstream** — “Compared with specialized individual models, pretraining foundation models for massive downstream tasks can amortize training costs, providing opportunities to push the limits of model scale \[5\] for human-level intelligence.”
- **adaptation** — “CoCa shows that a single pretrained model can outperform many specialized models using zero-shot transfer or minimal task-specific adaptation.”
- **jointly** — “This paper presents Contrastive Captioner (CoCa), a minimalist design to pretrain an image-text encoder-decoder foundation model jointly with contrastive loss and captioning loss, thereby subsuming model capabilities from contrastive approaches like CLIP and generative methods like SimVLM.”
- **embedding** — “For the contrastive objective LCon , we append a learnable \[CLS\] token at the end of the input sentence and use its corresponding output of unimodal decoder as the text embedding.”
- **foundation model** — “This paper presents Contrastive Captioner (CoCa), a minimalist design to pretrain an image-text encoder-decoder foundation model jointly with contrastive loss and captioning loss, thereby subsuming model capabilities from contrastive approaches like CLIP and generative methods like SimVLM.”
- **subsume** — “Recent work has proposed image-text foundation models that can subsume both vision and vision-language pretraining.”
- **cascade** — “We omit cross-attention in unimodal decoder layers to encode text-only representations, and cascade multimodal decoder layers cross-attending to image encoder outputs to learn multimodal image-text representations.”
- **autoregressively** — “We apply a contrastive loss between unimodal image and text embeddings, in addition to a captioning loss on the multimodal decoder outputs which predicts text tokens autoregressively.”
- **seamlessly** — “CoCa is pretrained end-to-end and from scratch on both web-scale alt-text data and annotated images by treating all labels simply as text, seamlessly unifying natural language supervision for representation learning.”
- **minimalist** — “This paper presents Contrastive Captioner (CoCa), a minimalist design to pretrain an image-text encoder-decoder foundation model jointly with contrastive loss and captioning loss, thereby subsuming model capabilities from contrastive approaches like CLIP and generative methods like SimVLM.”
- **omit** — “We omit cross-attention in unimodal decoder layers to encode text-only representations, and cascade multimodal decoder layers cross-attending to image encoder outputs to learn multimodal image-text representations.”
- **overhead** — “By sharing the same computational graph, the two training objectives are computed efficiently with minimal overhead.”

## Abstract（自动提取）

> TITLE: CoCa: Contrastive Captioners are Image-Text Foundation Models ABSTRACT: Exploring large-scale pretrained foundation models is of significant interest in computer vision because these models can be quickly transferred to many downstream tasks. This paper presents Contrastive Captioner (CoCa), a minimalist design to pretrain an image-text encoder-decoder foundation model jointly with contrastive loss and captioning loss, thereby subsuming model capabilities from contrastive approaches like CLIP and generative methods like SimVLM. In contrast to standard encoder-decoder transformers where all decoder layers attend to encoder outputs, CoCa omits cross-attention in the first half of decoder layers to encode unimodal text representations, and cascades the remaining decoder layers which cross-attend to the image encoder for multimodal image-text representations. We apply a contrastive loss between unimodal image and text embeddings, in addition to a captioning loss on the multimodal decoder outputs which predicts text tokens autoregressively. By sharing the same computational graph, the two training objectives are computed efficiently with minimal overhead. CoCa is pretrained end-to-end and from scratch on both web-scale alt-text data and annotated images by treating all labels simply as text, seamlessly unifying natural language supervision for representation learning. Empiric

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

PDF：`/home/user/llm-papers/02_多模态/PDF/05_CoCa.pdf`

---
type: paper-pack
paper_id: "02-00"
stage: 2
title: "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale"
pdf: "/home/user/llm-papers/02_多模态/PDF/00_ViT_VisionTransformer.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-00 An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale

**中文标题**：一张图像等于 16×16 个词：用于大规模图像识别的 Transformer

**一句话概括**：提出 Vision Transformer（ViT），把图像切成 patch 序列直接用纯 Transformer 处理而无需卷积网络，大规模预训练后迁移到中小规模识别基准，效果出色且训练计算量显著更低。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| benchmark | /bˈɛntʃmɑːk/ | 基准（用于评测的标准数据集，如 ImageNet） | S |
| state-of-the-art | /stˈeɪtɒvðɪˈɑːt/ | 最先进的（当前最佳水平，常缩写为 SOTA） | S |
| pre-trained | /pɹˈiːtɹˈeɪnd/ | 预训练的（先在大数据上训练再迁移） | A |
| transfer | /tɹˈansfɜː/ | 迁移（把模型能力应用到其他任务/数据上） | A |
| reliance | /ɹɪlˈaɪəns/ | 依赖（本文指对 CNN 的依赖） | A |
| patch | /pˈatʃ/ | 图像块、图像碎片（ViT 把整图切成的小块） | A |
| attain | /ɐtˈeɪn/ | 获得、达到（取得优秀结果） | A |
| substantially | /səbstˈanʃəli/ | 显著地、大幅度地（指所需计算资源少得多） | A |
| de-facto | /dəfˈaktəʊ/ | 事实上的、实际通用的（指 Transformer 已成为 NLP 领域默认标准） | B |
| in conjunction with | /ˈɪn kəndʒˈʌŋkʃən wˈɪð/ | 与……结合（指注意力与卷积网络搭配使用） | B |

### 原句（保留完整句子）

- **benchmark** — “To understand the data requirements of each model, we pre-train on datasets of varying size and evaluate many benchmark tasks.”
- **state-of-the-art** — “When pre-trained on large amounts of data and transferred to multiple mid-sized or small image recognition benchmarks (ImageNet, CIFAR-100, VTAB, etc.), Vision Transformer (ViT) attains excellent results compared to state-of-the-art convolutional networks while requiring substantially fewer computational resources to train.1 1 I NTRODUCTION Self-attention-based architectures, in particular Transformers (Vaswani et al., 2017), have become the model of choice in natural language processing (NLP).”
- **pre-trained** — “When pre-trained on large amounts of data and transferred to multiple mid-sized or small image recognition benchmarks (ImageNet, CIFAR-100, VTAB, etc.), Vision Transformer (ViT) attains excellent results compared to state-of-the-art convolutional networks while requiring substantially fewer computational resources to train.1 1 I NTRODUCTION Self-attention-based architectures, in particular Transformers (Vaswani et al., 2017), have become the model of choice in natural language processing (NLP).”
- **transfer** — “(2020) perform an empirical exploration of CNN transfer learning from large scale datasets such as ImageNet-21k and JFT-300M.”
- **reliance** — “We show that this reliance on CNNs is not necessary and a pure transformer applied directly to sequences of image patches can perform very well on image classification tasks.”
- **patch** — “(2020) use a small patch size of 2 × 2 pixels, which makes the model applicable only to small-resolution images, while we handle medium-resolution images as well.”
- **attain** — “ViT uses approximately 2 − 4× less compute to attain the same performance (average over 5 datasets).”
- **substantially** — “When pre-trained on large amounts of data and transferred to multiple mid-sized or small image recognition benchmarks (ImageNet, CIFAR-100, VTAB, etc.), Vision Transformer (ViT) attains excellent results compared to state-of-the-art convolutional networks while requiring substantially fewer computational resources to train.1 1 I NTRODUCTION Self-attention-based architectures, in particular Transformers (Vaswani et al., 2017), have become the model of choice in natural language processing (NLP).”
- **de-facto** — “A Comprehensive Survey on Deep Music Generation 67 texture is simply a distorted duplicate of the source. \[86\] put forward the audio evaluation metrics in Table 3, among which IS and FID have become a de-facto standard for measuring the performance of any GAN-based model \[334\].”
- **in conjunction with** — “In vision, attention is either applied in conjunction with convolutional networks, or used to replace certain components of convolutional networks while keeping their overall structure in place.”

## Abstract（自动提取）

> TITLE: An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale ABSTRACT: While the Transformer architecture has become the de-facto standard for natural language processing tasks, its applications to computer vision remain limited. In vision, attention is either applied in conjunction with convolutional networks, or used to replace certain components of convolutional networks while keeping their overall structure in place. We show that this reliance on CNNs is not necessary and a pure transformer applied directly to sequences of image patches can perform very well on image classification tasks. When pre-trained on large amounts of data and transferred to multiple mid-sized or small image recognition benchmarks (ImageNet, CIFAR-100, VTAB, etc.), Vision Transformer (ViT) attains excellent results compared to state-of-the-art convolutional networks while requiring substantially fewer computational resources to train.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/00_ViT_VisionTransformer.pdf`

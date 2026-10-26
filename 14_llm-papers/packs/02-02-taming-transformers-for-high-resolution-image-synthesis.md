---
type: paper-pack
paper_id: "02-02"
stage: 2
title: "Taming Transformers for High-Resolution Image Synthesis"
pdf: "/home/user/llm-papers/02_多模态/PDF/02_VQGAN.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-02 Taming Transformers for High-Resolution Image Synthesis

**中文标题**：驯服 Transformer：高分辨率图像合成

**一句话概括**：提出 VQGAN，用 CNN 学习图像构成成分的"词汇表"，再用 Transformer 高效建模其组合，实现百万像素级、语义引导的图像合成。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| conditional | /kəndˈɪʃənəl/ | 条件式的（生成受额外输入如类别/分割图控制） | A |
| long-range | /lˈɒŋɹˈeɪndʒ/ | 长程的、远距离的（捕捉序列中相隔很远的依赖） | A |
| demonstrate | /dˈɛmənstɹˌeɪt/ | 展示、证明（论文中陈述实验/结论的常用动词） | A |
| taming | /tˈeɪmɪŋ/ | 驯服、驾驭（标题用词，指让 Transformer 也能处理图像） | B |
| inductive bias | /ɪndˈʌktɪv bˈaɪəs/ | 归纳偏置（模型先天偏向某种结构，如 CNN 偏好局部） | B |
| prioritize | /pɹaɪˈɒɹɪtˌaɪz/ | 优先考虑（CNN 的偏置优先处理局部信息） | B |
| infeasible | /ɪnfˈiːzɪbəl/ | 不可行的（计算上无法承受长序列） | B |
| constituent | /kənstˈɪtjuːənt/ | 构成成分、组成元素（图像的基本组成部分） | B |
| composition | /kˌɒmpəzˈɪʃən/ | 组合、构成（各成分如何排列组合成图像） | B |
| semantically-guided | /səmˈantɪkliɡˈaɪdɪd/ | 语义引导的（按语义信息指导生成过程） | B |
| megapixel | /mˈɛɡəpˌɪksəl/ | 百万像素级的（指超高分辨率图像） | B |

### 原句（保留完整句子）

- **conditional** — “(1) sentation with a Variational Autoencoder (VAE) \[38, 62\], dk and then again learning its distribution with a VAE. \[18, 78\] When performing autoregressive maximum-likelihood demonstrate similar gains when using an unconditional norlearning, non-causal entries of QK t , i.e. all entries be- malizing flow for the second stage, and \[63, 64\] when using low its diagonal, are set to −∞ and the final output of the a conditional normalizing flow.”
- **long-range** — “In contrast to the predominant viDesigned to learn long-range interactions on sequential sion architecture, convolutional neural networks (CNNs), data, transformers continue to show state-of-the-art results the transformer architecture contains no built-in inductive on a wide variety of tasks.”
- **demonstrate** — “We ships, whereas CNNs have been designed to exploit prior demonstrate how combining the effectiveness of the induc- knowledge about strong local correlations within images. tive bias of CNNs with the expressivity of transformers en- Thus, the increased expressivity of transformers comes with ables them to model and thereby synthesize high-resolution quadratically increasing computational costs, because all images.”
- **taming** — “9 Taming Transformers for High-Resolution Image Synthesis – Supplementary Material The supplementary material for our work Taming Transformers for High-Resolution Image Synthesis is structured as follows: First, Sec.”
- **inductive bias** — “In contrast to CNNs, they contain prior on the locality of interactions and is therefore free no inductive bias that prioritizes local interactions.”
- **prioritize** — “It democratize LLMs inference by prioritizing high throughhas a simple and user-friendly API, making it easy to use put, low latency, and cost-effectiveness.”
- **infeasible** — “While the ability to consider interactions model is that, taken together, convolutional and transformer between all elements is the reason transformers efficiently architectures can model the compositional nature of our vi- learn long-range interactions, it is also the reason transformsual world \[51\]: We use a convolutional approach to effi- ers quickly become infeasible, especially on images, where ciently learn a codebook of context-rich visual parts and, the sequence length itself scales quadratically with the ressubsequently, learn a model of their global compositions. olution.”
- **constituent** — “Fast and accurate shift-reduce constituent parsing.”
- **composition** — “The resultrich vocabulary of image constituents, and in turn (ii) utilize ing energy and time requirements of state-of-the-art transtransformers to efficiently model their composition within former models thus pose fundamental problems for scaling high-resolution images.”
- **semantically-guided** — “"semantically-guided synthesis of megapixel images"”
- **megapixel** — “To effectively learn such high-resolution image synthesis up to the megapixel range. a discrete spatial codebook, we propose to directly incorPrevious work \[55, 8\] which applied transformers to image porate the inductive biases of CNNs and incorporate ideas generation demonstrated promising results for images up to from neural discrete representation learning \[72\].”

## Abstract（自动提取）

> TITLE: Taming Transformers for High-Resolution Image Synthesis ABSTRACT: Designed to learn long-range interactions on sequential data, transformers continue to show state-of-the-art results on a wide variety of tasks. In contrast to CNNs, they contain no inductive bias that prioritizes local interactions. This makes them expressive, but also computationally infeasible for long sequences, such as high-resolution images. We demonstrate how combining the effectiveness of the inductive bias of CNNs with the expressivity of transformers enables them to model and thereby synthesize high-resolution images. We show how to (i) use CNNs to learn a context-rich vocabulary of image constituents, and in turn (ii) utilize transformers to efficiently model their composition within high-resolution images. Our approach is readily applied to conditional synthesis tasks, where both non-spatial information, such as object classes, and spatial information, such as segmentations, can control the generated image. In particular, we present the first results on semantically-guided synthesis of megapixel images with transformers and obtain the state of the art among autoregressive models on class-conditional ImageNet. Code and pretrained models can be found at https://github.com/CompVis/taming-transformers .

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

PDF：`/home/user/llm-papers/02_多模态/PDF/02_VQGAN.pdf`

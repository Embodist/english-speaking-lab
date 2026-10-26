---
type: paper-pack
paper_id: "05-11"
stage: 5
title: "Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture"
pdf: "/home/user/llm-papers/05_世界模型/PDF/11_IJEPA_JEPA.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 05-11 Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture

**中文标题**：用联合嵌入预测架构从图像做自监督学习（I-JEPA）

**一句话概括**：提出 I-JEPA，一种非生成式自监督方法：从单个上下文块预测同一图像中多个目标块的表征，配合大尺度目标块采样与信息丰富的上下文掩码策略，与 ViT 结合高度可扩展。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| scalable | /skˈeɪləbəl/ | 可扩展的 | S |
| empirically | /ɛmpˈɪɹɪkli/ | 经验上、通过实验 | A |
| informative | /ɪnfˈɔːmətˌɪv/ | 信息量丰富的 | A |
| hand-crafted | /hˈandkɹˈaftɪd/ | 手工设计的；人工设计的 | B |
| data-augmentations | /dˈeɪtəɹˌɔːɡmɛntˈeɪʃənz/ | 数据增强；对数据做变换增加多样性 | B |
| masking strategy | /mˈaskɪŋ stɹˈatədʒi/ | 掩码策略；决定遮挡哪些图像块 | B |
| semantic representations | /səmˈantɪk ɹˌɛpɹɪzˈɛntˈeɪʃənz/ | 语义表征；蕴含高级语义信息的表示 | B |
| context block | /kˈɒntɛkst blˈɒk/ | 上下文块；提供预测依据的图像块 | B |
| downstream performance | /dˈaʊnstɹiːm pəfˈɔːməns/ | 下游任务表现 | B |
| non-generative | /nˈɒndʒˈɛnəɹətˌɪv/ | 非生成式的；不重建像素 | B |
| linear classification | /lˈɪniə klˌasɪfɪkˈeɪʃən/ | 线性分类；用线性分类器评估表征质量 | B |
| joint-embedding | /dʒˈɔɪntɛmbˈɛdɪŋ/ | 联合嵌入；把不同块映射到同一表征空间 | B |

### 原句（保留完整句子）

- **scalable** — “Empirically, when combined with Vision Transformers, we find I-JEPA to be highly scalable.”
- **empirically** — “Empirically, when combined with Vision Transformers, we find I-JEPA to be highly scalable.”
- **informative** — “A core design choice to guide 77 ViT-S/16 (800ep) data2vec ViT-H/14 (1600ep) I-JEPA towards producing semantic representations is the ViT-L/16 (1600ep) masking strategy; specifically, it is crucial to (a) sample tar- 76 103 104 get blocks with sufficiently large scale (semantic), and to (b) use a sufficiently informative (spatially distributed) context Pretraining GPU Hours block.”
- **hand-crafted** — “This idea is at the constructed using a set of hand-crafted data augmentations, core of self-supervised generative methods, which remove such as random scaling, cropping, and color jittering \[20\], or corrupt portions of the input and learn to predict the coramongst others \[35\].”
- **data-augmentations** — “I-JEPA pretraining outperforms proves linear probing performance compared to other methods that MAE which also does not rely on hand-crafted data-augmentations do not rely on hand-crafted view data-augmentations during pre- during pretraining.”
- **masking strategy** — “A core design choice to guide 77 ViT-S/16 (800ep) data2vec ViT-H/14 (1600ep) I-JEPA towards producing semantic representations is the ViT-L/16 (1600ep) masking strategy; specifically, it is crucial to (a) sample tar- 76 103 104 get blocks with sufficiently large scale (semantic), and to (b) use a sufficiently informative (spatially distributed) context Pretraining GPU Hours block.”
- **semantic representations** — “A core design choice to guide 77 ViT-S/16 (800ep) data2vec ViT-H/14 (1600ep) I-JEPA towards producing semantic representations is the ViT-L/16 (1600ep) masking strategy; specifically, it is crucial to (a) sample tar- 76 103 104 get blocks with sufficiently large scale (semantic), and to (b) use a sufficiently informative (spatially distributed) context Pretraining GPU Hours block.”
- **context block** — “The idea behind I-JEPA is simple: from a single CAE context block, predict the representations of various target 78 ViT-L/16 (1600ep) iBOT MAE blocks in the same image.”
- **downstream performance** — “By predicting in representation under 72 hours to achieve strong downstream performance space, I-JEPA produces semantic representations while using less across a wide range of tasks, from linear classification to compute than previous methods. object counting and depth prediction. how to generalize these biases for tasks requiring differ1.”
- **non-generative** — “We introduce the Image- 80 I-JEPA ViT-H/14 (300ep) Top 1 (%) based Joint-Embedding Predictive Architecture (I-JEPA), a non-generative approach for self-supervised learning from 79 images.”
- **linear classification** — “By predicting in representation under 72 hours to achieve strong downstream performance space, I-JEPA produces semantic representations while using less across a wide range of tasks, from linear classification to compute than previous methods. object counting and depth prediction. how to generalize these biases for tasks requiring differ1.”
- **joint-embedding** — “We introduce the Image- 80 I-JEPA ViT-H/14 (300ep) Top 1 (%) based Joint-Embedding Predictive Architecture (I-JEPA), a non-generative approach for self-supervised learning from 79 images.”

## Abstract（自动提取）

> TITLE: Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture ABSTRACT: This paper demonstrates an approach for learning highly semantic image representations without relying on hand-crafted data-augmentations. We introduce the Image-based Joint-Embedding Predictive Architecture (I-JEPA), a non-generative approach for self-supervised learning from images. The idea behind I-JEPA is simple: from a single context block, predict the representations of various target blocks in the same image. A core design choice to guide I-JEPA towards producing semantic representations is the masking strategy; specifically, it is crucial to (a) sample target blocks with sufficiently large scale (semantic), and to (b) use a sufficiently informative (spatially distributed) context block. Empirically, when combined with Vision Transformers, we find I-JEPA to be highly scalable. For instance, we train a ViT-Huge/14 on ImageNet using 16 A100 GPUs in under 72 hours to achieve strong downstream performance across a wide range of tasks, from linear classification to object counting and depth prediction.

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
- [[14_llm-papers/stage-05-world-models|阶段 5]]

PDF：`/home/user/llm-papers/05_世界模型/PDF/11_IJEPA_JEPA.pdf`

---
type: paper-pack
paper_id: "02-04"
stage: 2
title: "Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision"
pdf: "/home/user/llm-papers/02_多模态/PDF/04_ALIGN.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-04 Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision

**中文标题**：利用含噪声的文本监督扩大视觉与视觉-语言表示学习规模

**一句话概括**：提出一个简单的双编码器架构，用超过十亿的图文 alt-text 对和对比损失对齐视觉与语言表示，证明数据规模足以弥补噪声。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| corpus | /kˈɔːpəs/ | 语料库（收集的大量图文数据） | S |
| leverage | /lˈiːvəɹɪdʒ/ | 利用（采用一个含噪声的大规模数据集） | S |
| retrieval | /ɹɪtɹˈiːvəl/ | 检索（按查询找匹配的图像/文本） | S |
| curation | /kjʊəɹˈeɪʃən/ | 精选、整理过程（成本高昂的数据清洗环节） | S |
| contrastive | /kˈɒntɹastˌɪv/ | 对比的（contrastive loss 对比损失：拉近匹配对、推远不匹配对） | S |
| align | /ɐlˈaɪn/ | 对齐（让视觉与语言表示在空间中对应起来） | A |
| curated | /kjˈʊəɹeɪtɪd/ | 人工精选的（经过精心挑选整理的数据集） | A |
| hinder | /hˈɪndə/ | 阻碍（限制模型规模继续扩大） | A |
| annotation | /ˌanətˈeɪʃən/ | 标注（人工给出的标签，无需人工标注） | B |
| dual-encoder | /djˈuːəlɛŋkˈəʊdə/ | 双编码器的（图像和文本各用一个编码器） | B |
| cross-modality | /kɹˈɒsməʊdˈalɪti/ | 跨模态（跨越图像与文本两种模态） | B |

### 原句（保留完整句子）

- **corpus** — “We show that the scale of our in the vision domain, and much smaller than large corpora corpus can make up for its noise and leads to of text from the internet for NLP pre-training (e.g., Devlin state-of-the-art representations even with such a et al.”
- **leverage** — “In this paper, we pre-training datasets such as Conceptual Captions (Sharma leverage a noisy dataset of over one billion image et al., 2018), Visual Genome Dense Captions (Krishna alt-text pairs, obtained without expensive filter- et al., 2016), and ImageBERT (Qi et al., 2020) require ing or post-processing steps in the Conceptual even heavier work on human annotation, semantic parsing, Captions dataset.”
- **retrieval** — “But instead of applying the MSCOCO image-text retrieval benchmarks, even complex filtering and post-processing steps as proposed when compared with more sophisticated cross- by (Sharma et al., 2018) to clean the dataset, we only apply attention models.”
- **curation** — “Curation of such pre-training datasets with explicit class labels such as Ima- datasets requires heavy work on data gathering, sampling, geNet or OpenImages.”
- **contrastive** — “This is at resentations of the image and text pairs using a least an order of magnitude smaller than their counterparts contrastive loss.”
- **align** — “As a result, the scales of these tecture learns to align visual and language rep- datasets are only in the realm of ∼10M examples.”
- **curated** — “In the vision domain, pre-training ing on raw text without human annotations, vi- on large-scale supervised data such as ImageNet (Deng sual and vision-language representations still rely et al., 2009), OpenImages (Kuznetsova et al., 2020), and JFTheavily on curated training datasets that are expen- 300M (Sun et al., 2017; Kolesnikov et al., 2020) has proven sive or require expert knowledge.”
- **hinder** — “This process involves creatassessment, it is also often hindered by high annotation ing datasets annotated with preferences and feedback from costs, significant time requirements, and annotation inconhumans or proficient LLMs.”
- **annotation** — “For vision-language, popu- and human annotation, and hence is difficult to scale. lar datasets like Conceptual Captions, MSCOCO, or CLIP all involve a non-trivial data collection Pre-training has also become the de-facto approach (and cleaning) process.”
- **dual-encoder** — “A simple dual-encoder archi- cleaning and balancing.”
- **cross-modality** — “The resulting dataset is cross-modality search with complex text and text noisy, but is two orders of magnitude larger than the Con+ image queries. ceptual Captions dataset.”

## Abstract（自动提取）

> TITLE: Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision ABSTRACT: Pre-trained representations are becoming crucial for many NLP and perception tasks. While representation learning in NLP has transitioned to training on raw text without human annotations, visual and vision-language representations still rely heavily on curated training datasets that are expensive or require expert knowledge. For vision applications, representations are mostly learned using datasets with explicit class labels such as ImageNet or OpenImages. For vision-language, popular datasets like Conceptual Captions, MSCOCO, or CLIP all involve a non-trivial data collection (and cleaning) process. This costly curation process limits the size of datasets and hence hinders the scaling of trained models. In this paper, we leverage a noisy dataset of over one billion image alt-text pairs, obtained without expensive filtering or post-processing steps in the Conceptual Captions dataset. A simple dual-encoder architecture learns to align visual and language representations of the image and text pairs using a contrastive loss. We show that the scale of our corpus can make up for its noise and leads to state-of-the-art representations even with such a simple learning scheme. Our visual representation achieves strong performance when transferred to classification tasks such as Im

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

PDF：`/home/user/llm-papers/02_多模态/PDF/04_ALIGN.pdf`

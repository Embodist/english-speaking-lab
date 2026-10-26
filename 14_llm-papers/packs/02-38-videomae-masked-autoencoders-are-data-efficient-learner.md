---
type: paper-pack
paper_id: "02-38"
stage: 2
title: "VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training"
pdf: "/home/user/llm-papers/02_多模态/PDF/38_VideoMAE.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-38 VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training

**中文标题**：VideoMAE：掩码自编码器是自监督视频预训练的高数据效率学习器

**一句话概括**：将掩码自编码器用于视频，提出极高比例（90%~95%）的"视频管"掩码，仅用几千段视频即可预训练出优秀模型，并揭示数据质量重于数量。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| self-supervised | /sˈɛlfsˈuːpəvˌaɪzd/ | 自监督的；无需人工标注的预训练 | S |
| reconstruction | /ɹˌiːkənstɹˈʌkʃən/ | 重建；从剩余部分还原被遮盖内容 | A |
| data-efficient | /dˈeɪtəɹɪfˈɪʃənt/ | 数据高效的；少量数据即可学好 | A |
| customized | /kˈʌstəmˌaɪzd/ | 定制的；针对视频专门设计的掩码方式 | A |
| redundant | /ɹɪdˈʌndənt/ | 冗余的；视频相邻帧信息高度重复 | A |
| favorable | /fˈeɪvəɹəbəl/ | 有利的；仍然取得不错的效果 | A |
| premier | /pɹˈɛmɪə/ | 顶尖的；最好的性能 | B |
| masking | /mˈaskɪŋ/ | 掩码；遮盖部分输入迫使模型重建 | B |
| ratio | /ɹˈeɪʃɪˌəʊ/ | 比例；被遮盖视频块所占比重 | B |
| domain shift | /dəmˈeɪn ʃˈɪft/ | 域偏移；预训练与目标任务数据分布不同 | B |
| vanilla | /vɐnˈɪlə/ | 基础的；不加额外改动的标准结构 | B |

### 原句（保留完整句子）

- **self-supervised** — “A key innovation of JEPA lies in its self-supervised learning paradigm, which enables the system to learn rich representations of the world without relying on extensive labeled data.”
- **reconstruction** — “To illustrate the essential idea of model quanally leads to inaccurate reconstruction results.”
- **data-efficient** — “Jaitly, “Rephrasing the web: A recipe for compute European Chapter of the Association for Computational and data-efficient language modeling,” in ICLR 2024 Linguistics: Main Volume, EACL 2021, Online, April 19 Workshop on Navigating and Addressing Data Problems - 23, 2021, 2021, pp.”
- **customized** — “"propose customized video tube masking with an extremely high ratio"”
- **redundant** — “First, low-quality sentences that contain recorpus, especially removing noisy, redundant, irrelevant, peated words and phrases should be removed, as they may and potentially toxic data \[56, 64, 227\], which may largely introduce repetitive patterns in language modeling \[235\]. affect the capacity and performance of LLMs.”
- **favorable** — “This result suggests that INT4 quantization exhibits a favorable Distillation for LLMs.”
- **premier** — “If the answer cannot be found in the articles, write “I could not find an answer.” Articles: “““Joao Moutinho is a Portuguese footballer who last played as a central midfielder for Premier League club Wolverhampton Wanderers and the Portugal national team.””” Question: Is the following sentence plausible? ’Joao Moutinho was out at third.’ Answer: Let’s think step by step.”
- **masking** — “"propose customized video tube masking with an extremely high ratio"”
- **ratio** — “6: Ratios of various data sources in the pre-training data for existing LLMs.”
- **domain shift** — “"Domain shift between pre-training and target datasets"”
- **vanilla** — “The vanilla Transformer total parameter size \[265\].”

## 摘要提示（PDF 文本不可提取）

> TITLE: VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training ABSTRACT: Pre-training video transformers on extra large-scale datasets is generally required to achieve premier performance on relatively small datasets. In this paper, we show that video masked autoencoders (VideoMAE) are data-efficient learners for self-supervised video pre-training (SSVP). We are inspired by the recent ImageMAE and propose customized video tube masking with an extremely high ratio. This simple design makes video reconstruction a more challenging self-supervision task, thus encouraging extracting more effective video representations during this pre-training process. We obtain three important findings on SSVP: (1) An extremely high proportion of masking ratio (i.e., 90% to 95%) still yields favorable performance of VideoMAE. The temporally redundant video content enables a higher masking ratio than that of images. (2) VideoMAE achieves impressive results on very small datasets (i.e., around 3k-4k videos) without using any extra data. (3) VideoMAE shows that data quality is more important than data quantity for SSVP. Domain shift between pre-training and target datasets is an important issue. Notably, our VideoMAE with the vanilla ViT can achieve 87.4% on Kinetics-400, 75.4% on Something-Something V2, 91.3% on UCF101, and 62.6% on HMDB51, without using any e

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

PDF：`/home/user/llm-papers/02_多模态/PDF/38_VideoMAE.pdf`

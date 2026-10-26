---
type: paper-pack
paper_id: "02-03"
stage: 2
title: "Learning Transferable Visual Models From Natural Language Supervision"
pdf: "/home/user/llm-papers/02_多模态/PDF/03_CLIP.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-03 Learning Transferable Visual Models From Natural Language Supervision

**中文标题**：从自然语言监督中学习可迁移的视觉模型

**一句话概括**：提出 CLIP，用"预测哪张图配哪句说明"的预训练任务在 4 亿图文对上学习图像表示，使模型能零样本迁移到 30 多个下游任务。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| benchmark | /bˈɛntʃmɑːk/ | 做基准评测（在多个数据集上系统评估） | S |
| zero-shot | /zˈiəɹəʊʃˈɒt/ | 零样本的（不经训练直接迁移到新任务） | S |
| downstream | /dˈaʊnstɹiːm/ | 下游的（预训练之后要解决的具体任务） | S |
| leverage | /lˈiːvəɹɪdʒ/ | 利用（借助更广泛的监督来源） | S |
| competitive | /kəmpˈɛtɪtˌɪv/ | 有竞争力的、可匹敌的（接近全监督基线水平） | S |
| scalable | /skˈeɪləbəl/ | 可扩展的（方法能随数据规模放大而受益） | S |
| span | /spˈan/ | 涵盖、跨越（任务范围覆盖 OCR、动作识别等） | A |
| predetermined | /pɹɪdɪtˈɜːmɪnd/ | 预先确定的（固定不变的类别集合） | A |
| caption | /kˈapʃən/ | 图片说明文字、配图文本 | A |
| restricted | /ɹɪstɹˈɪktɪd/ | 受限的（这种监督形式限制了泛化能力） | B |
| reference | /ɹˈɛfɹəns/ | 引用、指称（用自然语言指向已学的视觉概念） | B |

### 原句（保留完整句子）

- **benchmark** — “We study crowd-labeled datasets such as ImageNet (Deng et al., 2009). the performance of this approach by benchmark- Could scalable pre-training methods which learn directly ing on over 30 different existing computer vi- from web text result in a similar breakthrough in computer sion datasets, spanning tasks such as OCR, ac- vision?”
- **zero-shot** — “This restricted form of supera standardized input-output interface (McCann et al., 2018; vision limits their generality and usability since Radford et al., 2019; Raffel et al., 2019) has enabled taskadditional labeled data is needed to specify any agnostic architectures to zero-shot transfer to downstream other visual concept.”
- **downstream** — “This restricted form of supera standardized input-output interface (McCann et al., 2018; vision limits their generality and usability since Radford et al., 2019; Raffel et al., 2019) has enabled taskadditional labeled data is needed to specify any agnostic architectures to zero-shot transfer to downstream other visual concept.”
- **leverage** — “Although early work wrestled with the complexity 35 of natural language when using topic model and n-gram Zero-Shot ImageNet Accuracy representations, improvements in deep contextual represen30 tation learning suggest we now have the tools to effectively 25 leverage this abundant source of supervision (McCann et al., 20 2017).”
- **competitive** — “(Brown et al., 2020) are now competitive across many tasks We demonstrate that the simple pre-training task with bespoke models while requiring little to no dataset of predicting which caption goes with which imspecific training data. age is an efficient and scalable way to learn SOTA image representations from scratch on a dataset These results suggest that the aggregate supervision accesof 400 million (image, text) pairs collected from sible to modern pre-training methods within web-scale colthe internet.”
- **scalable** — “(Brown et al., 2020) are now competitive across many tasks We demonstrate that the simple pre-training task with bespoke models while requiring little to no dataset of predicting which caption goes with which imspecific training data. age is an efficient and scalable way to learn SOTA image representations from scratch on a dataset These results suggest that the aggregate supervision accesof 400 million (image, text) pairs collected from sible to modern pre-training methods within web-scale colthe internet.”
- **span** — “Their approach learns the cache the zero-shot classifier once it has been computed by parameters of a dictionary of 142,806 visual n-grams (span- the text encoder and reuse it for all subsequent predictions. ning 1- to 5- grams) and optimizes these n-grams using a This allows the cost of generating it to be amortized across differential version of Jelinek-Mercer smoothing to maxi- all the predictions in a dataset. mize the probability of all text n-grams for a given image.”
- **predetermined** — “"a fixed set of predetermined object categories"”
- **caption** — “(Brown et al., 2020) are now competitive across many tasks We demonstrate that the simple pre-training task with bespoke models while requiring little to no dataset of predicting which caption goes with which imspecific training data. age is an efficient and scalable way to learn SOTA image representations from scratch on a dataset These results suggest that the aggregate supervision accesof 400 million (image, text) pairs collected from sible to modern pre-training methods within web-scale colthe internet.”
- **restricted** — “This restricted form of supera standardized input-output interface (McCann et al., 2018; vision limits their generality and usability since Radford et al., 2019; Raffel et al., 2019) has enabled taskadditional labeled data is needed to specify any agnostic architectures to zero-shot transfer to downstream other visual concept.”
- **reference** — “After pre-training, natural language lections of text surpasses that of high-quality crowd-labeled is used to reference learned visual concepts (or NLP datasets.”

## Abstract（自动提取）

> TITLE: Learning Transferable Visual Models From Natural Language Supervision ABSTRACT: State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories. This restricted form of supervision limits their generality and usability since additional labeled data is needed to specify any other visual concept. Learning directly from raw text about images is a promising alternative which leverages a much broader source of supervision. We demonstrate that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image representations from scratch on a dataset of 400 million (image, text) pairs collected from the internet. After pre-training, natural language is used to reference learned visual concepts (or describe new ones) enabling zero-shot transfer of the model to downstream tasks. We study the performance of this approach by benchmarking on over 30 different existing computer vision datasets, spanning tasks such as OCR, action recognition in videos, geo-localization, and many types of fine-grained object classification. The model transfers non-trivially to most tasks and is often competitive with a fully supervised baseline without the need for any dataset specific training. For instance, we match the accuracy of the original ResNet-50 on ImageNet zero-shot without needi

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

PDF：`/home/user/llm-papers/02_多模态/PDF/03_CLIP.pdf`

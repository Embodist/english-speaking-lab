---
type: paper-pack
paper_id: "02-40"
stage: 2
title: "InternVideo: General Video Foundation Models via Generative and Discriminative Learning"
pdf: "/home/user/llm-papers/02_多模态/PDF/40_InternVideo.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-40 InternVideo: General Video Foundation Models via Generative and Discriminative Learning

**中文标题**：InternVideo：通过生成式与判别式学习构建通用视频基础模型

**一句话概括**：同时采用掩码视频建模与视频-语言对比学习两种自监督目标，并以可学习方式协调互补表征，在 39 个视频数据集上达到 SOTA。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| benchmark | /bˈɛntʃmɑːk/ | 基准测试；权威评测数据集 | S |
| downstream | /dˈaʊnstɹiːm/ | 下游的；在此基础之上的具体任务 | S |
| alignment | /ɐlˈaɪnmənt/ | 对齐；视频与语言语义的匹配 | S |
| generative | /dʒˈɛnəɹətˌɪv/ | 生成式的；以重建等目标学习表征 | A |
| foundation model | /faʊndˈeɪʃən mˈɒdəl/ | 基础模型；支撑多种下游任务的大模型 | A |
| dynamic | /daɪnˈamɪk/ | 动态的；涉及运动与时间变化的理解 | A |
| discriminative | /dɪskɹˈɪmɪnətˌɪv/ | 判别式的；以区分正负样本学习表征 | A |
| contrastive learning | /kˈɒntɹastˌɪv lˈɜːnɪŋ/ | 对比学习；拉近匹配视频-文本对 | A |
| coordinate | /kəʊˈɔːdɪnət/ | 协调；把两种表征按需融合 | A |
| boost | /bˈuːst/ | 提升；增强各类视频应用效果 | A |
| complementary | /kˌɒmplɪmˈɛntəɹi/ | 互补的；两种方法各有所长 | B |
| bells and whistles | /bˈɛlz ˈand wˈɪsəlz/ | 花哨的附加功能；指复杂技巧 | B |

### 原句（保留完整句子）

- **benchmark** — “A recent study \[69\] found that a model size of 62B is better performance on downstream tasks, since language at least required for PaLM to perform well on various tasks modeling loss can be considered as a general measure of in four evaluation benchmarks (i.e., MMLU, BBH, TyDiQA the overall model capacity.”
- **downstream** — “In this paradigm, it word representations by first pre-training a bidirectional often requires fine-tuning the PLM for adapting to different LSTM (biLSTM) network (instead of learning fixed word downstream tasks. representations) and then fine-tuning the biLSTM network according to specific downstream tasks.”
- **alignment** — “Index Terms—Large Language Models; Emergent Abilities; Adaptation Tuning; Utilization; Alignment; Capacity Evaluation ✦ 1 I NTRODUCTION “The limits of my language mean the limits of my world.” extensive attention in the literature, which can be divided —Ludwig Wittgenstein into four major development stages: • Statistical language models (SLM).”
- **generative** — “(2016) \[8\] generative 93.3 increased the maximum output length to input length + 300.”
- **foundation model** — “"large-scale pretrained foundation models is"”
- **dynamic** — “It is a powerful achieves accelerated text generation inference by leveraging library with a large and active community of users and four essential technologies: blocked KV caching, continuous developers who regularly update and improve the models batching, dynamic SplitFuse, and high-performance CUDA and algorithms.”
- **discriminative** — “(2014) \[37\] WSJ only, discriminative 88.3 Petrov et al.”
- **contrastive learning** — “"Unlike standard contrastive learning with softmax normalization"”
- **coordinate** — “To facilitate a more thorough grained information (e.g., coordinate of objects) into the evaluation of MLLMs, various benchmarks have been develinstruction \[836\], or synthesizing complex visual reasoning oped.”
- **boost** — “Since each kind of data source is closely of LLMs heavily rely on data selection and mixture, and related to the development of certain capacities for LLMs one can boost the proportions of specific data sources to (referring to the discussions in Section 4.1), it is important enhance certain model abilities \[64, 227\].”
- **complementary** — “To better synergize be utilized to enhance the task performance of LLMs by pro- the LLM and KG in a complementary manner, recent studies viding precise and necessary knowledge.”
- **bells and whistles** — “"Without bells and whistles, InternVideo achieves state-of-the-art"”

## 摘要提示（PDF 文本不可提取）

> TITLE: InternVideo: General Video Foundation Models via Generative and Discriminative Learning ABSTRACT: The foundation models have recently shown excellent performance on a variety of downstream tasks in computer vision. However, most existing vision foundation models simply focus on image-level pretraining and adpation, which are limited for dynamic and complex video-level understanding tasks. To fill the gap, we present general video foundation models, InternVideo, by taking advantage of both generative and discriminative self-supervised video learning. Specifically, InternVideo efficiently explores masked video modeling and video-language contrastive learning as the pretraining objectives, and selectively coordinates video representations of these two complementary frameworks in a learnable manner to boost various video applications. Without bells and whistles, InternVideo achieves state-of-the-art performance on 39 video datasets from extensive tasks including video action recognition/detection, video-language alignment, and open-world video applications. Especially, our methods can obtain 91.1% and 77.2% top-1 accuracy on the challenging Kinetics-400 and Something-Something V2 benchmarks, respectively. All of these results effectively show the generality of our InternVideo for video understanding. The code will be released at https://github.com/OpenGVLab/InternVideo .

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

PDF：`/home/user/llm-papers/02_多模态/PDF/40_InternVideo.pdf`

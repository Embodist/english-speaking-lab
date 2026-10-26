---
type: paper-pack
paper_id: "02-30"
stage: 2
title: "Flow Matching for Generative Modeling"
pdf: "/home/user/llm-papers/02_多模态/PDF/30_FlowMatching.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-30 Flow Matching for Generative Modeling

**中文标题**：用于生成建模的流匹配

**一句话概括**：提出"流匹配"这一免模拟的训练范式，通过回归条件概率路径的向量场训练连续归一化流，比扩散路径训练更快、采样更稳、泛化更好。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| robust | /ɹəʊbˈʌst/ | 稳健的；训练更稳定、不易发散 | S |
| paradigm | /pˈaɹədˌaɪm/ | 范式；一种新的生成建模思路 | S |
| generalization | /dʒˌɛnəɹəlaɪzˈeɪʃən/ | 泛化；在新数据上的表现能力 | S |
| unprecedented | /ʌnpɹˈɛsɪdəntɪd/ | 前所未有的；此前无法达到的规模 | A |
| likelihood | /lˈaɪklihˌʊd/ | 似然；模型对数据概率的拟合程度 | A |
| off-the-shelf | /ˈɒfðəʃˈɛlf/ | 现成的；无需改动即可直接使用 | A |
| subsume | /sʌbsjˈuːm/ | 涵盖、包含；扩散路径只是其特例 | A |
| regress | /ɹɪɡɹˈɛs/ | 回归；让网络拟合目标向量场 | B |
| vector field | /vˈɛktə fˈiːld/ | 向量场；概率路径上每个点处的速度方向场 | B |
| instance | /ˈɪnstəns/ | 实例、情形；一种特别值得关注的设置 | B |
| displacement interpolation | /dɪsplˈeɪsmənt ɪntˌɜːpəlˈeɪʃən/ | 位移插值；最优传输中连接两个分布的过程 | B |

### 原句（保留完整句子）

- **robust** — “Nevertheless, LLMs may expose work argues that even human evaluation may not be robust bias (e.g., order bias or preference for LLM-generated texts enough \[630, 631, 641, 642\].”
- **paradigm** — “This study has inspired a large number of follow-up models for representation learning (beyond word sequence work, which sets the “pre-training and fine-tuning” learning modeling), having an important impact on the field of NLP. paradigm.”
- **generalization** — “With instruction tuning, LLMs are mostly conducted in terms of language modeling loss are enabled to follow the task instructions for new tasks (e.g., per-token cross-entropy loss in nats \[30\]), while in without using explicit examples, thus having an improved practice we are more concerned about the performance of generalization ability.”
- **unprecedented** — “More importantly, world model technologies are fundamentally transforming game development and player experiences in unprecedented ways.”
- **likelihood** — “In general, LM aims to model the generative likelihood Thus, specially designed smoothing strategies such as backof word sequences, so as to predict the probabilities of off estimation \[15\] and Good–Turing estimation \[16\] have future (or missing) tokens.”
- **off-the-shelf** — “Castro \[283\] proposed a software system integrating off-the-shelf music generation models into improvisation.”
- **subsume** — “This paper presents Contrastive Captioner (CoCa), a minimalist design to pretrain an image-text encoder-decoder foundation model jointly with contrastive loss and captioning loss, thereby subsuming model capabilities from contrastive approaches like CLIP and generative methods like SimVLM.”
- **regress** — “High-resolution piano transcription with pedals by regressing onsets and offsets times. arXiv preprint arXiv:2010.01815, 2020. \[321\] Craig Stuart Sapp.”
- **vector field** — “"regressing vector fields of fixed conditional probability paths"”
- **instance** — “For in some specific tasks (e.g., retrieval or speech tasks), in instance, Microsoft 365 is being empowered by LLMs (i.e., which the predicted or estimated probabilities can enhance Copilot) to automate the office work, and OpenAI supports the performance of task-specific approaches.”
- **displacement interpolation** — “"Optimal Transport (OT) displacement interpolation to define"”

## 摘要提示（PDF 文本不可提取）

> TITLE: Flow Matching for Generative Modeling ABSTRACT: We introduce a new paradigm for generative modeling built on Continuous Normalizing Flows (CNFs), allowing us to train CNFs at unprecedented scale. Specifically, we present the notion of Flow Matching (FM), a simulation-free approach for training CNFs based on regressing vector fields of fixed conditional probability paths. Flow Matching is compatible with a general family of Gaussian probability paths for transforming between noise and data samples -- which subsumes existing diffusion paths as specific instances. Interestingly, we find that employing FM with diffusion paths results in a more robust and stable alternative for training diffusion models. Furthermore, Flow Matching opens the door to training CNFs with other, non-diffusion probability paths. An instance of particular interest is using Optimal Transport (OT) displacement interpolation to define the conditional probability paths. These paths are more efficient than diffusion paths, provide faster training and sampling, and result in better generalization. Training CNFs using Flow Matching on ImageNet leads to consistently better performance than alternative diffusion-based methods in terms of both likelihood and sample quality, and allows fast and reliable sample generation using off-the-shelf numerical ODE solvers.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/30_FlowMatching.pdf`

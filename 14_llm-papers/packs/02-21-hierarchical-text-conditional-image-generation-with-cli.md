---
type: paper-pack
paper_id: "02-21"
stage: 2
title: "Hierarchical Text-Conditional Image Generation with CLIP Latents"
pdf: "/home/user/llm-papers/02_多模态/PDF/21_DALLE2.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-21 Hierarchical Text-Conditional Image Generation with CLIP Latents

**中文标题**：用 CLIP 隐向量进行分层文本条件图像生成

**一句话概括**：提出两阶段模型——先验根据文本生成 CLIP 图像嵌入，解码器再据此生成图像，并以零样本方式实现语言引导的图像操控。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| autoregressive | /ˌɔːtəʊɹɪɡɹˈɛsɪv/ | 自回归的（逐元素生成的方式，与扩散模型并列） | S |
| hierarchical | /haɪəɹˈɑːkɪkəl/ | 分层的（模型分两级：先验+解码器） | S |
| robust | /ɹəʊbˈʌst/ | 稳健的（学到可靠、鲁棒的表示） | S |
| contrastive | /kˈɒntɹastˌɪv/ | 对比的（对比学习得到的模型，如 CLIP） | S |
| capture | /kˈaptʃə/ | 捕捉（表示同时包含语义和风格信息） | A |
| embedding | /ɛmbˈɛdɪŋ/ | 嵌入（向量）（CLIP 图像嵌入） | A |
| conditioned on | /kəndˈɪʃənd ˈɒn/ | 以……为条件的（生成过程受嵌入控制） | A |
| preserve | /pɹɪzˈɜːv/ | 保留（保持原图的语义与风格） | A |
| manipulation | /mənˌɪpjʊlˈeɪʃən/ | 操作、操控（对图像内容的修改） | A |
| semantics | /səmˈantɪks/ | 语义（图像的内容含义） | A |
| variation | /vˌeəɹɪˈeɪʃən/ | 变体（保留语义风格的图像变化版本） | A |
| prior | /pɹˈaɪə/ | 先验（模型）（本文指根据文本生成图像嵌入的模块） | B |

### 原句（保留完整句子）

- **autoregressive** — “We use diffusion models for the decoder and experiment with both autoregressive and diffusion models for the prior, finding that the latter are computationally more efficient and produce higher-quality samples.”
- **hierarchical** — “Previous works have leveraged hierarchical generative processes to create high-quality synthetic images.”
- **robust** — “CLIP embeddings have a number of desirable properties: they are robust to image distribution shift, have impressive zero-shot capabilities, and have been fine-tuned to achieve state-of-the-art results on a wide variety of vision and language tasks \[45\].”
- **contrastive** — “Bordes et al. \[3\] train diffusion models conditioned on image representations from contrastive models.”
- **capture** — “We retained the text conditioning pathway present in the original GLIDE model, hypothesizing that it could allow the diffusion model to learn aspects of natural language that CLIP fails to capture (e.g. variable binding), but find that it offers little help in this regard (Section 7).”
- **embedding** — “To leverage these representations for image generation, we propose a two-stage model: a prior that generates a CLIP image embedding given a text caption, and a decoder that generates an image conditioned on the image embedding.”
- **conditioned on** — “To leverage these representations for image generation, we propose a two-stage model: a prior that generates a CLIP image embedding given a text caption, and a decoder that generates an image conditioned on the image embedding.”
- **preserve** — “Our decoders conditioned on image representations can also produce variations of an image that preserve both its semantics and style, while varying the non-essential details absent from the image representation.”
- **manipulation** — “In 2017, the Transformer model \[22\] was introsponses, e.g., rejecting to answer insulting questions. duced by Google, and the OpenAI team quickly adapted • Tools manipulation.”
- **semantics** — “Our decoders conditioned on image representations can also produce variations of an image that preserve both its semantics and style, while varying the non-essential details absent from the image representation.”
- **variation** — “6.2 Model Variations To evaluate the importance of different components of the Transformer, we varied our base model in different ways, measuring the change in performance on English-to-German translation on the 5 We used values of 2.8, 3.7, 6.0 and 9.5 TFLOPS for K80, K40, M40 and P100, respectively.”
- **prior** — “To leverage these representations for image generation, we propose a two-stage model: a prior that generates a CLIP image embedding given a text caption, and a decoder that generates an image conditioned on the image embedding.”

## Abstract（自动提取）

> TITLE: Hierarchical Text-Conditional Image Generation with CLIP Latents ABSTRACT: Contrastive models like CLIP have been shown to learn robust representations of images that capture both semantics and style. To leverage these representations for image generation, we propose a two-stage model: a prior that generates a CLIP image embedding given a text caption, and a decoder that generates an image conditioned on the image embedding. We show that explicitly generating image representations improves image diversity with minimal loss in photorealism and caption similarity. Our decoders conditioned on image representations can also produce variations of an image that preserve both its semantics and style, while varying the non-essential details absent from the image representation. Moreover, the joint embedding space of CLIP enables language-guided image manipulations in a zero-shot fashion. We use diffusion models for the decoder and experiment with both autoregressive and diffusion models for the prior, finding that the latter are computationally more efficient and produce higher-quality samples.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/21_DALLE2.pdf`

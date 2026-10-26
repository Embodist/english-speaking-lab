---
type: paper-pack
paper_id: "02-22"
stage: 2
title: "Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding"
pdf: "/home/user/llm-papers/02_多模态/PDF/22_Imagen.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-22 Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding

**中文标题**：深度语言理解的逼真文生图扩散模型

**一句话概括**：提出 Imagen，关键发现是增大文本语言模型比增大图像扩散模型更能提升保真度与图文对齐，并引入 DrawBench 基准。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| corpus | /kˈɔːpəs/ | 语料库（纯文本训练数据） | S |
| alignment | /ɐlˈaɪnmənt/ | 对齐（生成图像与文本描述的一致程度） | S |
| comprehensive | /kˌɒmpɹɪhˈɛnsɪv/ | 全面的（覆盖广泛场景的基准） | S |
| high-fidelity | /hˈaɪfɪdˈɛlɪti/ | 高保真的（生成质量与真实图像高度一致） | S |
| generic | /dʒənˈɛɹɪk/ | 通用的（非专门为图像设计的语言模型） | A |
| unprecedented | /ʌnpɹˈɛsɪdəntɪd/ | 前所未有的（逼真度达到新高度） | A |
| surprisingly | /səpɹˈaɪzɪŋli/ | 惊人地（效果出乎意料地好） | A |
| boost | /bˈuːst/ | 提升（提高样本保真度与图文对齐） | A |
| photorealism | /fˌəʊtəʊɹˈiəlɪzəm/ | 照片级真实感（生成图像的真实程度） | B |
| hinge on | /hˈɪndʒ ˈɒn/ | 取决于、关键在于（成功依托于……） | B |
| discovery | /dɪskˈʌvəɹi/ | 发现（论文的核心发现） | B |
| encode | /ɛŋkˈəʊd/ | 编码（把文本转成可用于生成的表示） | B |

### 原句（保留完整句子）

- **corpus** — “Language models are trained on text only corpus significantly larger than paired image-text data, thus being exposed to a very rich and wide distribution of text.”
- **alignment** — “T5), pretrained on text-only corpora, are surprisingly effective at encoding text for image synthesis: increasing the size of the language model in Imagen boosts both sample fidelity and imagetext alignment much more than increasing the size of the image diffusion model.”
- **comprehensive** — “To assess text-to-image models in greater depth, we introduce DrawBench, a comprehensive and challenging benchmark for text-to-image models.”
- **high-fidelity** — “Imagen builds on the power of large transformer language models in understanding text and hinges on the strength of diffusion models in high-fidelity image generation.”
- **generic** — “Our key discovery is that generic large language models (e.g.”
- **unprecedented** — “To pursue this research direction further, we introduce Imagen, a text-to-image diffusion model that combines the power of transformer language models (LMs) \[15, 52\] with high-fidelity diffusion models \[28, 29, 16, 41\] to deliver an unprecedented degree of photorealism and a deep level of language understanding in text-to-image synthesis.”
- **surprisingly** — “T5), pretrained on text-only corpora, are surprisingly effective at encoding text for image synthesis: increasing the size of the language model in Imagen boosts both sample fidelity and imagetext alignment much more than increasing the size of the image diffusion model.”
- **boost** — “On the set with no people, there is a boost in preference rate of Imagen to 43.6%, indicating Imagen’s limited ability to generate photorealistic people.”
- **photorealism** — “To pursue this research direction further, we introduce Imagen, a text-to-image diffusion model that combines the power of transformer language models (LMs) \[15, 52\] with high-fidelity diffusion models \[28, 29, 16, 41\] to deliver an unprecedented degree of photorealism and a deep level of language understanding in text-to-image synthesis.”
- **hinge on** — “"hinges on the strength of diffusion"”
- **discovery** — “Our key discovery is that generic large language models (e.g.”
- **encode** — “The image-text training objectives suggest that these text encoders may encode visually semantic and meaningful representations especially relevant for the text-to-image generation task.”

## Abstract（自动提取）

> TITLE: Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding ABSTRACT: We present Imagen, a text-to-image diffusion model with an unprecedented degree of photorealism and a deep level of language understanding. Imagen builds on the power of large transformer language models in understanding text and hinges on the strength of diffusion models in high-fidelity image generation. Our key discovery is that generic large language models (e.g. T5), pretrained on text-only corpora, are surprisingly effective at encoding text for image synthesis: increasing the size of the language model in Imagen boosts both sample fidelity and image-text alignment much more than increasing the size of the image diffusion model. Imagen achieves a new state-of-the-art FID score of 7.27 on the COCO dataset, without ever training on COCO, and human raters find Imagen samples to be on par with the COCO data itself in image-text alignment. To assess text-to-image models in greater depth, we introduce DrawBench, a comprehensive and challenging benchmark for text-to-image models. With DrawBench, we compare Imagen with recent methods including VQ-GAN+CLIP, Latent Diffusion Models, and DALL-E 2, and find that human raters prefer Imagen over other models in side-by-side comparisons, both in terms of sample quality and image-text alignment. See https://imagen.research.google/ for an overv

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

PDF：`/home/user/llm-papers/02_多模态/PDF/22_Imagen.pdf`

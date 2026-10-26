---
type: paper-pack
paper_id: "05-07"
stage: 5
title: "VideoGPT: Video Generation using VQ-VAE and Transformers"
pdf: "/home/user/llm-papers/05_世界模型/PDF/07_VideoGPT.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 05-07 VideoGPT: Video Generation using VQ-VAE and Transformers

**中文标题**：VideoGPT：用 VQ-VAE 与 Transformer 进行视频生成

**一句话概括**：提出概念简单的 VideoGPT 架构：用 VQ-VAE（3D 卷积+轴向自注意力）把原始视频压缩为离散潜表征，再用类 GPT 架构自回归建模，生成的视频质量可与最先进的 GAN 模型竞争。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| formulation | /fˌɔːmjʊlˈeɪʃən/ | 表述形式、公式化 | A |
| autoregressively | /ˌɔːtəʊɹɪɡɹˈɛsɪvli/ | 自回归地；逐个地基于已生成内容预测下一个 | A |
| axial self-attention | /ˈaksɪəl sˈɛlfɐtˈɛnʃən/ | 轴向自注意力；沿时间/空间轴分别做注意力 | B |
| spatio-temporal | /spˈeɪʃɪˌəʊtˈɛmpəɹəl/ | 时空的；同时含空间与时间维度 | B |
| high fidelity | /hˈaɪ fɪdˈɛlɪti/ | 高保真；生成结果与真实视频高度接近 | B |
| downsampled | /dˈaʊnsampəld/ | 下采样的；分辨率（规模）降低的 | B |
| likelihood based | /lˈaɪklihˌʊd bˈeɪst/ | 基于似然的；直接最大化数据概率 | B |
| discrete latents | /dɪskɹˈiːt lˈeɪtənts/ | 离散潜变量；离散化的隐藏表示 | B |
| competitive with | /kəmpˈɛtɪtˌɪv wˈɪð/ | 与……不相上下、有竞争力 | B |
| reproducible | /ɹɪpɹədjˈuːsɪbəl/ | 可复现的 | B |
| minimalistic | /mˌɪnɪməlˈɪstɪk/ | 极简的、尽量简单的 | B |
| generative modeling | /dʒˈɛnəɹətˌɪv mˈɒdəlɪŋ/ | 生成建模；学习数据分布并生成新样本 | B |

### 原句（保留完整句子）

- **formulation** — “By optimizing the loss L(N, D) under the conLLMs work, this part introduces the basic background for straint C ≈ 6N D, they showed that the optimal allocation LLMs, including scaling laws, emergent abilities and key of compute budget to model size and data size can be techniques. derived as follows: Formulation of Scaling Laws for LLMs.”
- **autoregressively** — “A simple GPT- videos (Vondrick et al., 2016; Kalchbrenner et al., 2016; like architecture is then used to autoregressively Tulyakov et al., 2018; Clark et al., 2019), high-fidelity natmodel the discrete latents using spatio-temporal ural videos is one notable modality that has not seen the position encodings.”
- **axial self-attention** — “VAE that learns downsampled discrete latent representations of a raw video by employing 3D con- While there have certainly been impressive efforts to model volutions and axial self-attention.”
- **spatio-temporal** — “A simple GPT- videos (Vondrick et al., 2016; Kalchbrenner et al., 2016; like architecture is then used to autoregressively Tulyakov et al., 2018; Clark et al., 2019), high-fidelity natmodel the discrete latents using spatio-temporal ural videos is one notable modality that has not seen the position encodings.”
- **high fidelity** — “Generating high fidelity images with subscale pixel networks and multidimensional Karras, T., Laine, S., and Aila, T.”
- **downsampled** — “VAE that learns downsampled discrete latent representations of a raw video by employing 3D con- While there have certainly been impressive efforts to model volutions and axial self-attention.”
- **likelihood based** — “Despite this, it is fair to use the GPT terminology for our choice guided by our inclination to explore likelihood based gener- model because our architecture more closely resembles the vanilla ative models and non-empirically established beliefs with respect Transformer in a manner similar to iGPT (Chen et al., 2020). to stability of training.”
- **discrete latents** — “A simple GPT- videos (Vondrick et al., 2016; Kalchbrenner et al., 2016; like architecture is then used to autoregressively Tulyakov et al., 2018; Clark et al., 2019), high-fidelity natmodel the discrete latents using spatio-temporal ural videos is one notable modality that has not seen the position encodings.”
- **competitive with** — “This is reasonable since the able to generate samples competitive with state- complexity of natural videos requires modeling correlations of-the-art GAN models for video generation on across both space and time with much higher input dimenthe BAIR Robot dataset, and generate high fi- sions.”
- **reproducible** — “We hope our proposed problem also demands more compute resources which can architecture serves as a reproducible reference also be deemed as one important reason for the relatively for a minimalistic implementation of transformer slow progress in generative modeling of videos. based video generation models.”
- **minimalistic** — “We hope our proposed problem also demands more compute resources which can architecture serves as a reproducible reference also be deemed as one important reason for the relatively for a minimalistic implementation of transformer slow progress in generative modeling of videos. based video generation models.”
- **generative modeling** — “Despite the simplicity in for- same level of progress in generative modeling as compared mulation and ease of training, our architecture is to images, audio, and text.”

## Abstract（自动提取）

> TITLE: VideoGPT: Video Generation using VQ-VAE and Transformers ABSTRACT: We present VideoGPT: a conceptually simple architecture for scaling likelihood based generative modeling to natural videos. VideoGPT uses VQ-VAE that learns downsampled discrete latent representations of a raw video by employing 3D convolutions and axial self-attention. A simple GPT-like architecture is then used to autoregressively model the discrete latents using spatio-temporal position encodings. Despite the simplicity in formulation and ease of training, our architecture is able to generate samples competitive with state-of-the-art GAN models for video generation on the BAIR Robot dataset, and generate high fidelity natural videos from UCF-101 and Tumbler GIF Dataset (TGIF). We hope our proposed architecture serves as a reproducible reference for a minimalistic implementation of transformer based video generation models. Samples and code are available at https://wilson1yan.github.io/videogpt/index.html

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

PDF：`/home/user/llm-papers/05_世界模型/PDF/07_VideoGPT.pdf`

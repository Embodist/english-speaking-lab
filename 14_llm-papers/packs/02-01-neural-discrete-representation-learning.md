---
type: paper-pack
paper_id: "02-01"
stage: 2
title: "Neural Discrete Representation Learning"
pdf: "/home/user/llm-papers/02_多模态/PDF/01_VQVAE.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-01 Neural Discrete Representation Learning

**中文标题**：神经离散表示学习

**一句话概括**：提出 VQ-VAE，通过向量量化让编码器输出离散编码并学习先验，规避"后验坍塌"问题，从而生成高质量的图像、视频和语音。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| autoregressive | /ˌɔːtəʊɹɪɡɹˈɛsɪv/ | 自回归的（逐个预测序列元素的方式） | S |
| representation | /ɹˌɛpɹɪzˈɛntˈeɪʃən/ | 表示、表征（模型学到的数据内部特征） | S |
| latent | /lˈeɪtənt/ | 隐的、潜在的（latent representation 指隐空间中的表示） | S |
| discrete | /dɪskɹˈiːt/ | 离散的（编码取值有限、不连续；与 continuous 相对） | S |
| generative | /dʒˈɛnəɹətˌɪv/ | 生成式的（能生成新样本的模型） | A |
| incorporate | /ɪŋkˈɔːpəɹˌeɪt/ | 引入、纳入（把向量量化的思想融入模型） | A |
| supervision | /suːpəvˈɪʒən/ | 监督（此处指无监督学习，不需要人工标签） | A |
| propose | /pɹəpˈəʊz/ | 提出（论文中引出自己方法的常用动词） | A |
| posterior | /pɒstˈiəɹiə/ | 后验（分布）（后验坍塌指隐变量被解码器忽略） | A |
| circumvent | /sˈɜːkəmvˌɛnt/ | 规避、绕开（绕过后验坍塌这一难题） | B |
| utility | /juːtˈɪlɪti/ | 实用性、效用（所学表示的价值） | B |

### 原句（保留完整句子）

- **autoregressive** — “Using the VQ method allows the model to circumvent issues of “posterior collapse” -— where the latents are ignored when they are paired with a powerful autoregressive decoder -— typically observed in the VAE framework.”
- **representation** — “In order to learn a discrete latent representation, we incorporate ideas from vector quantisation (VQ).”
- **latent** — “In order to learn a discrete latent representation, we incorporate ideas from vector quantisation (VQ).”
- **discrete** — “In this paper, we propose a simple yet powerful generative model that learns such discrete representations.”
- **generative** — “In this paper, we propose a simple yet powerful generative model that learns such discrete representations.”
- **incorporate** — “In order to learn a discrete latent representation, we incorporate ideas from vector quantisation (VQ).”
- **supervision** — “For instance, when trained on speech we discover the latent structure of language without any supervision or prior knowledge about phonemes or words.”
- **propose** — “In this paper, we propose a simple yet powerful generative model that learns such discrete representations.”
- **posterior** — “Using the VQ method allows the model to circumvent issues of “posterior collapse” -— where the latents are ignored when they are paired with a powerful autoregressive decoder -— typically observed in the VAE framework.”
- **circumvent** — “Using the VQ method allows the model to circumvent issues of “posterior collapse” -— where the latents are ignored when they are paired with a powerful autoregressive decoder -— typically observed in the VAE framework.”
- **utility** — “Pairing these representations with an autoregressive prior, the model can generate high quality images, videos, and speech as well as doing high quality speaker conversion and unsupervised learning of phonemes, providing further evidence of the utility of the learnt representations.”

## Abstract（自动提取）

> TITLE: Neural Discrete Representation Learning ABSTRACT: Learning useful representations without supervision remains a key challenge in machine learning. In this paper, we propose a simple yet powerful generative model that learns such discrete representations. Our model, the Vector Quantised-Variational AutoEncoder (VQ-VAE), differs from VAEs in two key ways: the encoder network outputs discrete, rather than continuous, codes; and the prior is learnt rather than static. In order to learn a discrete latent representation, we incorporate ideas from vector quantisation (VQ). Using the VQ method allows the model to circumvent issues of "posterior collapse" -- where the latents are ignored when they are paired with a powerful autoregressive decoder -- typically observed in the VAE framework. Pairing these representations with an autoregressive prior, the model can generate high quality images, videos, and speech as well as doing high quality speaker conversion and unsupervised learning of phonemes, providing further evidence of the utility of the learnt representations.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/01_VQVAE.pdf`

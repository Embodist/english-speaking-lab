---
type: paper-pack
paper_id: "04-00"
stage: 4
title: "Neural Audio Synthesis of Musical Notes with WaveNet Autoencoders"
pdf: "/home/user/llm-papers/04_音乐生成/PDF/00_NSynth.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 04-00 Neural Audio Synthesis of Musical Notes with WaveNet Autoencoders

**中文标题**：基于 WaveNet 自编码器的音符神经音频合成

**一句话概括**：提出以原始波形上学到的时序编码为条件、自回归解码生成音频的 WaveNet 自编码器，并发布比同类数据集大一个数量级的 NSynth 音符数据集，模型可在不同乐器的音色间插值实现"乐器变形"。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| autoregressive | /ˌɔːtəʊɹɪɡɹˈɛsɪv/ | 自回归的（逐个预测、依赖前面已生成的样本） | S |
| generative | /dʒˈɛnəɹətˌɪv/ | 生成的（生成模型） | A |
| availability | /ɐvˌeɪləbˈɪlɪti/ | 可用性、可获得性（有高质量数据集可用） | A |
| autoencoder | /ˌɔːtəʊɛŋkˈəʊdə/ | 自编码器（先编码再解码重建的神经网络） | A |
| waveform | /wˈeɪvfɔːm/ | 波形（音频信号的原始形态） | A |
| order of magnitude | /ˈɔːdə ˈɒv mˈaɡnɪtjˌuːd/ | 数量级（相差约 10 倍） | A |
| qualitative | /kwˈɒlɪtˌeɪtɪv/ | 定性的（主观听感层面的） | A |
| timbre | /tˈambə/ | 音色（乐器声音的质感特征） | A |
| quantitative | /kwˈɒntɪtˌeɪtɪv/ | 定量的（数值指标层面的） | B |
| manifold | /mˈanɪfˌəʊld/ | 流形（嵌入向量构成的连续空间） | B |
| interpolate | /ɪntˈɜːpəlˌeɪt/ | 插值（在两个点之间平滑过渡） | B |
| expressive | /ɛkspɹˈɛsɪv/ | 有表现力的（声音富有情感） | B |

### 原句（保留完整句子）

- **autoregressive** — “However, that bias an autoregressive decoder, they effectively due to memory constraints, it is unable to fully capact as a ”driving function” for a nonlinear oscillator / ture global context.”
- **generative** — “Using NSynth, we demonstrate Explicitly, our two contributions to advance the state improved qualitative and quantitative perforof generative audio modeling are: mance of the WaveNet autoencoder over a well-tuned spectral autoencoder baseline.”
- **availability** — “See Section 2.1 for further details. the availability of high-quality and large-scale datasets learned space of embeddings.”
- **autoencoder** — “Using NSynth, we demonstrate Explicitly, our two contributions to advance the state improved qualitative and quantitative perforof generative audio modeling are: mance of the WaveNet autoencoder over a well-tuned spectral autoencoder baseline.”
- **waveform** — “First, we de- playback, such as in FM Synthesis or Granular Synthetail a powerful new WaveNet-style autoen- sis (Chowning, 1973; Xenakis, 1971), we show that it is coder model that conditions an autoregres- possible to generate new types of expressive and realsive decoder on temporal codes learned from istic instrument sounds with a neural network model. the raw audio waveform.”
- **order of magnitude** — “Recalling the original WaveNet architecture described Inspired by the large, high-quality image datasets, in (van den Oord et al., 2016a), at each step a stack NSynth is an order of magnitude larger than compa- of dilated convolutions predicts the next sample of aurable public datasets (Humphrey, 2016).”
- **qualitative** — “Using NSynth, we demonstrate Explicitly, our two contributions to advance the state improved qualitative and quantitative perforof generative audio modeling are: mance of the WaveNet autoencoder over a well-tuned spectral autoencoder baseline.”
- **timbre** — “Second, we intro- Further, we show that this model can learn a semanduce NSynth, a large-scale and high-quality tically meaningful hidden representation that can be dataset of musical notes that is an order used as a high-level control signal for manipulating of magnitude larger than comparable pub- tone, timbre, and dynamics during playback. lic datasets.”
- **quantitative** — “Using NSynth, we demonstrate Explicitly, our two contributions to advance the state improved qualitative and quantitative perforof generative audio modeling are: mance of the WaveNet autoencoder over a well-tuned spectral autoencoder baseline.”
- **manifold** — “Visually this shows up as colors it also learns a manifold of codes that yield more perwhich are faded and speckled with rainbow noise (K), ceptually interesting reconstructions. which contrasts with the bright colors of the original For example, in the interpolated note between the bass and WaveNet examples.”
- **interpolate** — “Next, we length or interpolated to align with the maximum training will introduce these issues and discuss how to address them length.”
- **expressive** — “First, we de- playback, such as in FM Synthesis or Granular Synthetail a powerful new WaveNet-style autoen- sis (Chowning, 1973; Xenakis, 1971), we show that it is coder model that conditions an autoregres- possible to generate new types of expressive and realsive decoder on temporal codes learned from istic instrument sounds with a neural network model. the raw audio waveform.”

## Abstract（自动提取）

> TITLE: Neural Audio Synthesis of Musical Notes with WaveNet Autoencoders ABSTRACT: Generative models in vision have seen rapid progress due to algorithmic improvements and the availability of high-quality image datasets. In this paper, we offer contributions in both these areas to enable similar progress in audio modeling. First, we detail a powerful new WaveNet-style autoencoder model that conditions an autoregressive decoder on temporal codes learned from the raw audio waveform. Second, we introduce NSynth, a large-scale and high-quality dataset of musical notes that is an order of magnitude larger than comparable public datasets. Using NSynth, we demonstrate improved qualitative and quantitative performance of the WaveNet autoencoder over a well-tuned spectral autoencoder baseline. Finally, we show that the model learns a manifold of embeddings that allows for morphing between instruments, meaningfully interpolating in timbre to create new types of sounds that are realistic and expressive.

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
- [[14_llm-papers/stage-04-music-generation|阶段 4]]

PDF：`/home/user/llm-papers/04_音乐生成/PDF/00_NSynth.pdf`

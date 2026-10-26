---
type: paper-pack
paper_id: "04-19"
stage: 4
title: "High Fidelity Neural Audio Compression"
pdf: "/home/user/llm-papers/04_音乐生成/PDF/19_EnCodec.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 04-19 High Fidelity Neural Audio Compression

**中文标题**：高保真神经音频压缩

**一句话概括**：提出流式编码器-解码器加量化潜在空间的端到端高保真神经音频编解码器 EnCodec，引入多尺度频谱对抗与损失均衡机制稳定训练，主观评测在语音与音乐上均优于基线，并可进一步用轻量 Transformer 压缩表示。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| high-fidelity | /hˈaɪfɪdˈɛlɪti/ | 高保真的（音质还原度高） | S |
| perceptual | /pəsˈɛptʃuːəl/ | 感知的（基于人耳听感的损失） | A |
| real-time | /ɹˈiəltˈaɪm/ | 实时的（能实时运行） | A |
| quantized | /kwˈɒntaɪzd/ | 量化的（离散化的潜在空间） | A |
| stabilize | /stˈeɪbɪlˌaɪz/ | 稳定（训练过程） | A |
| consist in | /kənsˈɪst ˈɪn/ | 在于（由…构成） | B |
| artifact | /ˈɑːtɪfˌakt/ | 伪影（压缩产生的失真痕迹） | B |
| decouple | /dɪkˈʌpəl/ | 解耦（把参数选择与损失量级分开） | B |
| bandwidth | /bˈandwɪdθ/ | 带宽（频率范围/码率范围） | B |
| reverberant | /ɹɪvˈɜːbəɹənt/ | 混响的（带回声的） | B |
| monophonic | /mˌɒnəʊfˈɒnɪk/ | 单声道的 | B |
| stereophonic | /stˌɛɹɪəʊfˈɒnɪk/ | 立体声的 | B |

### 原句（保留完整句子）

- **high-fidelity** — “Therefore, Engel et al. \[86\] proposed GANSynth, which uses GAN to generate high-fidelity and locally-coherent audio by modeling log-magnitudes and instantaneous frequency with sufficient frequency resolution in the spectrum domain.”
- **perceptual** — “They bridged analysis, synthesis and perceptual audio research by regularizing the learning of latent spaces, which were matched with the perceptual distance from timbre studies.”
- **real-time** — “MemoryBank \[539\] further provide real-time error messages \[443\], models like stable proposes the memory updating mechanism to allow memdiffusion \[534\] can be used in multimodal tasks to provide ory forgetting and strengthening following the Ebbinghaus visual perception \[439\], and virtual worlds like Minecraft Forgetting Curve theory. can provide immersive experiences \[530\].”
- **quantized** — “For neural network models, weights and activations are usually represented in the there are typically two kinds of data to be quantized, namely form of tensors.”
- **stabilize** — “To alleviate this issue, strategies (e.g., combining post-LN with pre-LN in GLMnormalization is a widely adopted strategy to stabilize the 130B \[93\]). training of neural networks.”
- **consist in** — “"It consists in a streaming encoder-decoder architecture"”
- **artifact** — “Due to the lossy characteristics of spectrograms and the oversmoothing artifacts caused by insufficiently expressive models, it is always a challenge to generate high-fidelity audio with the help of existing spectrogram model.”
- **decouple** — “Our approach is to compute the softmax normalization constant separately to decouple the columns.”
- **bandwidth** — “For example, the halfmatrix, need to be explicitly retained, leading to numerous precision compute and bandwidth of the A100 GPU are 312 memory read-write operations.”
- **reverberant** — “R ESULTS and far-field (reverberant) speech, with background noise in some of the examples.”
- **monophonic** — “Todd et al. \[29\] used RNNs to generate monophonic music note by note via predicting note pitches and durations.”
- **stereophonic** — “We extend our method to other conditioning signals, stereophonic audio.”

## 摘要提示（PDF 文本不可提取）

> TITLE: High Fidelity Neural Audio Compression ABSTRACT: We introduce a state-of-the-art real-time, high-fidelity, audio codec leveraging neural networks. It consists in a streaming encoder-decoder architecture with quantized latent space trained in an end-to-end fashion. We simplify and speed-up the training by using a single multiscale spectrogram adversary that efficiently reduces artifacts and produce high-quality samples. We introduce a novel loss balancer mechanism to stabilize training: the weight of a loss now defines the fraction of the overall gradient it should represent, thus decoupling the choice of this hyper-parameter from the typical scale of the loss. Finally, we study how lightweight Transformer models can be used to further compress the obtained representation by up to 40%, while staying faster than real time. We provide a detailed description of the key design choices of the proposed model including: training objective, architectural changes and a study of various perceptual loss functions. We present an extensive subjective evaluation (MUSHRA tests) together with an ablation study for a range of bandwidths and audio domains, including speech, noisy-reverberant speech, and music. Our approach is superior to the baselines methods across all evaluated settings, considering both 24 kHz monophonic and 48 kHz stereophonic audio. Code and models are available at gi

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

PDF：`/home/user/llm-papers/04_音乐生成/PDF/19_EnCodec.pdf`

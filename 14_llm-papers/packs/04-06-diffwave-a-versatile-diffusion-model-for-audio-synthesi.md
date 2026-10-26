---
type: paper-pack
paper_id: "04-06"
stage: 4
title: "DiffWave: A Versatile Diffusion Model for Audio Synthesis"
pdf: "/home/user/llm-papers/04_音乐生成/PDF/06_DiffWave.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 04-06 DiffWave: A Versatile Diffusion Model for Audio Synthesis

**中文标题**：DiffWave：多用途音频合成扩散模型

**一句话概括**：提出非自回归的扩散概率波形生成模型 DiffWave，通过马尔可夫链以固定步数把白噪声转换为结构化波形，在神经声码、条件与无条件生成等任务上达到与 WaveNet 相当的语音质量且快数个数量级。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| versatile | /vˈɜːsətˌaɪl/ | 多功能的、通用的（适用多种任务） | A |
| diffusion | /dɪfjˈuːʒən/ | 扩散（扩散模型：逐步去噪生成） | A |
| conditional | /kəndˈɪʃənəl/ | 有条件的（给定条件生成） | A |
| likelihood | /lˈaɪklihˌʊd/ | 似然（数据出现的概率） | A |
| diversity | /daɪvˈɜːsɪti/ | 多样性（生成样本的丰富程度） | A |
| unconditional | /ʌŋkəndˈɪʃənəl/ | 无条件的（不给定条件直接生成） | A |
| Markov chain | /mˈɑːkɒv tʃˈeɪn/ | 马尔可夫链（状态只依赖前一状态的随机过程） | A |
| evaluation | /ɪvˌaljuːˈeɪʃən/ | 评估（自动与人工评测） | A |
| non-autoregressive | /nˈɒnˌɔːtəʊɹɪɡɹˈɛsɪv/ | 非自回归的（一次并行生成全部样本） | B |
| vocoding | /vˈəʊkəʊdɪŋ/ | 声码合成（从声学特征合成语音） | B |
| mel spectrogram | /mˈɛl spˈɛktɹəɡɹˌam/ | 梅尔频谱图（按梅尔刻度划分的频谱图） | B |
| in terms of | /ˈɪn tˈɜːmz ˈɒv/ | 在…方面 | B |

### 原句（保留完整句子）

- **versatile** — “In this work, we propose DiffWave, a versatile diffusion probabilistic model for raw audio synthesis.”
- **diffusion** — “Diffusion probabilistic models (diffusion models for brevity) are a class of promising generative models, which use a Markov chain to gradually convert a simple distribution (e.g., isotropic Gaussian) into complicated data distribution (Sohl-Dickstein et al., 2015; Goyal et al., 2017; Ho et al., 2020).”
- **conditional** — “DiffWave produces high-fidelity audio in different waveform generation tasks, including neural vocoding conditioned on mel spectrogram, class-conditional generation, and unconditional generation.”
- **likelihood** — “It is efficiently trained by optimizing a variant of variational bound on the data likelihood.”
- **diversity** — “In particular, it significantly outperforms autoregressive and GAN-based waveform models in the challenging unconditional generation task in terms of audio quality and sample diversity from various automatic and human evaluations.”
- **unconditional** — “DiffWave produces high-fidelity audio in different waveform generation tasks, including neural vocoding conditioned on mel spectrogram, class-conditional generation, and unconditional generation.”
- **Markov chain** — “The model is non-autoregressive, and converts the white noise signal into structured waveform through a Markov chain with a constant number of steps at synthesis.”
- **evaluation** — “Results: We use the crowdMOS tookit (Ribeiro et al., 2011) for speech quality evaluation, where the test utterances from all models were presented to Mechanical Turk workers.”
- **non-autoregressive** — “The model is non-autoregressive, and converts the white noise signal into structured waveform through a Markov chain with a constant number of steps at synthesis.”
- **vocoding** — “DiffWave produces high-fidelity audio in different waveform generation tasks, including neural vocoding conditioned on mel spectrogram, class-conditional generation, and unconditional generation.”
- **mel spectrogram** — “DiffWave produces high-fidelity audio in different waveform generation tasks, including neural vocoding conditioned on mel spectrogram, class-conditional generation, and unconditional generation.”
- **in terms of** — “We demonstrate that DiffWave matches a strong WaveNet vocoder in terms of speech quality (MOS: 4.44 versus 4.43), while synthesizing orders of magnitude faster.”

## Abstract（自动提取）

> TITLE: DiffWave: A Versatile Diffusion Model for Audio Synthesis ABSTRACT: In this work, we propose DiffWave, a versatile diffusion probabilistic model for conditional and unconditional waveform generation. The model is non-autoregressive, and converts the white noise signal into structured waveform through a Markov chain with a constant number of steps at synthesis. It is efficiently trained by optimizing a variant of variational bound on the data likelihood. DiffWave produces high-fidelity audios in different waveform generation tasks, including neural vocoding conditioned on mel spectrogram, class-conditional generation, and unconditional generation. We demonstrate that DiffWave matches a strong WaveNet vocoder in terms of speech quality (MOS: 4.44 versus 4.43), while synthesizing orders of magnitude faster. In particular, it significantly outperforms autoregressive and GAN-based waveform models in the challenging unconditional generation task in terms of audio quality and sample diversity from various automatic and human evaluations.

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

PDF：`/home/user/llm-papers/04_音乐生成/PDF/06_DiffWave.pdf`

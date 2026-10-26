---
type: paper-pack
paper_id: "04-17"
stage: 4
title: "Stable Audio Open"
pdf: "/home/user/llm-papers/04_音乐生成/PDF/17_StableAudioOpen.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 04-17 Stable Audio Open

**中文标题**：Stable Audio Open（开放版）

**一句话概括**：发布用 Creative Commons 数据训练的开放权重文生音频模型，性能在多项指标上与现有最优方法相当，并展示其在 44.1kHz 高保真立体声合成上的潜力。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| competitive | /kəmpˈɛtɪtˌɪv/ | 有竞争力的（与最优相当） | S |
| baseline | /bˈeɪslaɪn/ | 基线（作对比的模型） | S |
| metric | /mˈɛtɹɪk/ | 指标（评测标准） | A |
| fine-tune | /fˈaɪntjˈuːn/ | 微调（在模型基础上继续训练） | A |
| accessible | /aksˈɛsəbəl/ | 可获取的（可公开使用） | A |
| synthesis | /sˈɪnθəsˌɪs/ | 合成（声音合成） | A |
| stereo | /stˈɛɹɪˌəʊ/ | 立体声的 | A |
| vitally | /vˈaɪtəli/ | 极其、至关重要地 | B |
| build upon | /bˈɪld əpˈɒn/ | 在此基础上构建（二次开发） | B |
| open-weights | /ˈəʊpənwˈeɪts/ | 开放权重的（模型权重公开） | B |
| realism | /ɹˈiəlɪzəm/ | 真实感（生成音频的真实程度） | B |
| showcase | /ʃˈəʊkeɪs/ | 展示（体现潜力） | B |

### 原句（保留完整句子）

- **competitive** — “Here manageable sequence length, a T5-based text embedding \[9\] for text we describe the architecture and training process of a new open- conditioning (109M parameters), and a transformer-based diffusion weights text-to-audio model trained with Creative Commons data. model (DiT of 1057M parameters) that operates in the latent space Our evaluation shows that the model’s performance is competitive of the autoencoder.”
- **baseline** — “We select the Encodec 32kHz variant Our model is accessible to everyone2 and can run on consumer-grade because the MusicGen-large-stereo baseline relies on it, and DAC GPUs, making it appealing for both academic and artistic use cases.”
- **metric** — “All metrics are on the English-to-German translation development set, newstest2013.”
- **fine-tune** — “Instead of directly using the model LLaMA models in non-English languages, it often needs to copies, APIs provide a more convenient way for common extend the original vocabulary (trained mainly on English users to use LLMs, without the need of running the model corpus) or fine-tune it with instructions or data in the locally.”
- **accessible** — “We select the Encodec 32kHz variant Our model is accessible to everyone2 and can run on consumer-grade because the MusicGen-large-stereo baseline relies on it, and DAC GPUs, making it appealing for both academic and artistic use cases.”
- **synthesis** — “The model’s case its potential for high-quality stereo sound synthesis at 44.1kHz. exact parameterization and its weights are available online.2 Index Terms— Stable Audio Open, Latent Diffusion, Audio.”
- **stereo** — “ARCHITECTURE Open generative models are vitally important for the community, al- Our latent diffusion model generates variable-length (up to 47s) lowing for fine-tunes and serving as baselines when presenting new stereo audio at 44.1kHz from text prompts.”
- **vitally** — “ARCHITECTURE Open generative models are vitally important for the community, al- Our latent diffusion model generates variable-length (up to 47s) lowing for fine-tunes and serving as baselines when presenting new stereo audio at 44.1kHz from text prompts.”
- **build upon** — “"and researchers to build upon"”
- **open-weights** — “Mixtral – Instruct reaches a score of 8.30 on MT-Bench \[33\] (see Table 2), making it the best open-weights model as of December 2023.”
- **realism** — “Its architecture is similar except that it FDopenl3 results (measuring the realism of the generations) show- uses T5 \[9\] text conditioning instead of CLAP \[10\].”
- **showcase** — “Existing LLMs have showcased sufrom human users are more suitable for fine-tuning LLMs, perior capabilities in traditional NLP tasks (e.g., generation it is difficult to collect them at a large scale.”

## Abstract（自动提取）

> TITLE: Stable Audio Open ABSTRACT: Open generative models are vitally important for the community, allowing for fine-tunes and serving as baselines when presenting new models. However, most current text-to-audio models are private and not accessible for artists and researchers to build upon. Here we describe the architecture and training process of a new open-weights text-to-audio model trained with Creative Commons data. Our evaluation shows that the model's performance is competitive with the state-of-the-art across various metrics. Notably, the reported FDopenl3 results (measuring the realism of the generations) showcase its potential for high-quality stereo sound synthesis at 44.1kHz.

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

PDF：`/home/user/llm-papers/04_音乐生成/PDF/17_StableAudioOpen.pdf`

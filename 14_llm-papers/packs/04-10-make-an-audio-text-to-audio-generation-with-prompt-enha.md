---
type: paper-pack
paper_id: "04-10"
stage: 4
title: "Make-An-Audio: Text-To-Audio Generation with Prompt-Enhanced Diffusion Models"
pdf: "/home/user/llm-papers/04_音乐生成/PDF/10_MakeAnAudio.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 04-10 Make-An-Audio: Text-To-Audio Generation with Prompt-Enhanced Diffusion Models

**中文标题**：Make-An-Audio：提示增强扩散模型的文生音频

**一句话概括**：提出提示增强的扩散模型：用"蒸馏-再编程"的伪提示增强缓解数据稀缺，用频谱自编码器预测自监督表示而非波形，实现高质量文本到音频生成，并首次解锁 X-to-Audio 多模态输入生成。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| self-supervised | /sˈɛlfsˈuːpəvˌaɪzd/ | 自监督的（无需人工标签） | S |
| robust | /ɹəʊbˈʌst/ | 稳健的（鲁棒性强） | S |
| modality | /məʊdˈalɪti/ | 模态（输入数据的类型） | S |
| generalization | /dʒˌɛnəɹəlaɪzˈeɪʃən/ | 泛化能力（推广到新输入的能力） | S |
| prompt | /pɹˈɒmpt/ | 提示（词）（引导生成的文本输入） | A |
| objective | /ɒbdʒˈɛktɪv/ | 客观的（客观指标评测） | A |
| milestone | /mˈaɪlstəʊn/ | 里程碑（标志性成果） | A |
| alleviate | /ɐlˈiːvɪˌeɪt/ | 缓解（减轻问题） | A |
| scarcity | /skˈeəsɪti/ | 稀缺（数据不足） | A |
| controllability | /kəntɹˌəʊləbˈɪlɪti/ | 可控性（可控制生成结果） | A |
| lag behind | /lˈaɡ bɪhˈaɪnd/ | 落后于（音频进展滞后） | B |
| subjective | /sʌbdʒˈɛktɪv/ | 主观的（人工听感评测） | B |

### 原句（保留完整句子）

- **self-supervised** — “In this work, we propose Make-An-Audio with a prompt-enhanced diffu- Video-to-audio sion model that addresses these gaps by 1) introducing pseudo prompt enhancement with a distill-then-reprogram approach, it alleviates data scarcity with orders of magnitude concept compositions by using language-free audios; 2) leveraging spectrogram autoencoder to predict the self-supervised audio representation instead of Figure 1.”
- **robust** — “Together with robust contrastive izes well to X-to-Audio with multiple user-defined inputs (text, language-audio pretraining (CLAP) representa- audio, image and video), it empowers humans to create rich and tions, Make-An-Audio achieves state-of-the-art diverse audio content, opening up to a various applications with results in both objective and subjective bench- personalized transfer and fine-grained control. mark evaluation.”
- **modality** — “No Modality Left Behind: Make-An-Audio generalwaveforms.”
- **generalization** — “Moreover, we present its controllability and generalization for X-to-Audio with et al., 2022) models are now able to vividly depict the visual “No Modality Left Behind”, for the first time scene described by a text prompt, and empower humans to unlocking the ability to generate high-definition, create rich and diverse visual content with unprecedented high-fidelity audios given a user-defined modality ease.”
- **prompt** — “In this work, we propose Make-An-Audio with a prompt-enhanced diffu- Video-to-audio sion model that addresses these gaps by 1) introducing pseudo prompt enhancement with a distill-then-reprogram approach, it alleviates data scarcity with orders of magnitude concept compositions by using language-free audios; 2) leveraging spectrogram autoencoder to predict the self-supervised audio representation instead of Figure 1.”
- **objective** — “Together with robust contrastive izes well to X-to-Audio with multiple user-defined inputs (text, language-audio pretraining (CLAP) representa- audio, image and video), it empowers humans to create rich and tions, Make-An-Audio achieves state-of-the-art diverse audio content, opening up to a various applications with results in both objective and subjective bench- personalized transfer and fine-grained control. mark evaluation.”
- **milestone** — “More recently, in November 2023, OpenAI released an upgraded generation The Milestones of Language Models.”
- **alleviate** — “To alleviate the issue of data scarcity, we introduce a Deep generative models (Goodfellow et al., 2020; Kingma pseudo prompt enhancement approach to construct natural & Dhariwal, 2018; Ho et al., 2020) have recently exhibited languages that align well with audio, opening up the usage high-quality samples in various data modalities.”
- **scarcity** — “In this work, we propose Make-An-Audio with a prompt-enhanced diffu- Video-to-audio sion model that addresses these gaps by 1) introducing pseudo prompt enhancement with a distill-then-reprogram approach, it alleviates data scarcity with orders of magnitude concept compositions by using language-free audios; 2) leveraging spectrogram autoencoder to predict the self-supervised audio representation instead of Figure 1.”
- **controllability** — “Moreover, we present its controllability and generalization for X-to-Audio with et al., 2022) models are now able to vividly depict the visual “No Modality Left Behind”, for the first time scene described by a text prompt, and empower humans to unlocking the ability to generate high-definition, create rich and diverse visual content with unprecedented high-fidelity audios given a user-defined modality ease.”
- **lag behind** — “"Its application to audio still lags behind"”
- **subjective** — “Together with robust contrastive izes well to X-to-Audio with multiple user-defined inputs (text, language-audio pretraining (CLAP) representa- audio, image and video), it empowers humans to create rich and tions, Make-An-Audio achieves state-of-the-art diverse audio content, opening up to a various applications with results in both objective and subjective bench- personalized transfer and fine-grained control. mark evaluation.”

## Abstract（自动提取）

> TITLE: Make-An-Audio: Text-To-Audio Generation with Prompt-Enhanced Diffusion Models ABSTRACT: Large-scale multimodal generative modeling has created milestones in text-to-image and text-to-video generation. Its application to audio still lags behind for two main reasons: the lack of large-scale datasets with high-quality text-audio pairs, and the complexity of modeling long continuous audio data. In this work, we propose Make-An-Audio with a prompt-enhanced diffusion model that addresses these gaps by 1) introducing pseudo prompt enhancement with a distill-then-reprogram approach, it alleviates data scarcity with orders of magnitude concept compositions by using language-free audios; 2) leveraging spectrogram autoencoder to predict the self-supervised audio representation instead of waveforms. Together with robust contrastive language-audio pretraining (CLAP) representations, Make-An-Audio achieves state-of-the-art results in both objective and subjective benchmark evaluation. Moreover, we present its controllability and generalization for X-to-Audio with "No Modality Left Behind", for the first time unlocking the ability to generate high-definition, high-fidelity audios given a user-defined modality input. Audio samples are available at https://Text-to-Audio.github.io

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

PDF：`/home/user/llm-papers/04_音乐生成/PDF/10_MakeAnAudio.pdf`

---
type: paper-pack
paper_id: "04-11"
stage: 4
title: "AudioLDM: Text-to-Audio Generation with Latent Diffusion Models"
pdf: "/home/user/llm-papers/04_音乐生成/PDF/11_AudioLDM.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 04-11 AudioLDM: Text-to-Audio Generation with Latent Diffusion Models

**中文标题**：AudioLDM：基于潜在扩散模型的文生音频

**一句话概括**：提出在 CLAP 潜在空间中训练潜在扩散模型 AudioLDM，无需显式建模跨模态关系即可学习音频表示，在生成质量与计算效率上均有优势，并首次支持零样本的文本引导音频操控（如风格迁移）。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| zero-shot | /zˈiəɹəʊʃˈɒt/ | 零样本的（无需针对任务训练即可用） | S |
| latent | /lˈeɪtənt/ | 潜在的（隐空间） | S |
| synthesize | /sˈɪnθəsˌaɪz/ | 合成（生成音频） | S |
| cross-modal | /kɹˈɒsmˈəʊdəl/ | 跨模态的（音频与文本之间） | S |
| embedding | /ɛmbˈɛdɪŋ/ | 嵌入（向量表示） | A |
| metric | /mˈɛtɹɪk/ | 指标（评测标准） | A |
| manipulation | /mənˌɪpjʊlˈeɪʃən/ | 操控、编辑（对音频的加工） | A |
| advantageous | /ɐdvantˈeɪdʒəs/ | 有优势的（两方面都更好） | B |
| style transfer | /stˈaɪl tɹˈansfɜː/ | 风格迁移（把音频换成另一种风格） | B |
| computational | /kˌɒmpjuːtˈeɪʃənəl/ | 计算的（计算效率） | B |
| gain attention | /ɡˈeɪn ɐtˈɛnʃən/ | 受到关注 | B |
| continuous | /kəntˈɪnjuːəs/ | 连续的（连续的音频表示） | B |

### 原句（保留完整句子）

- **zero-shot** — “Building on the success of guided audio manipulations (e.g., style transfer) StableDiffusion (Rombach et al., 2022), which uses latent in a zero-shot fashion.”
- **latent** — “AudioLDM: Text-to-Audio Generation with Latent Diffusion Models Haohe Liu * 1 Zehua Chen * 2 Yi Yuan 1 Xinhao Mei 1 Xubo Liu 1 Danilo Mandic 2 Wenwu Wang 1 Mark D.”
- **synthesize** — “To synthesize the audio waveform, we train it on the AudioSet dataset.”
- **cross-modal** — “By learning the latent representations of audio signals with- TTA systems are designed to generate a wide range of highout modelling the cross-modal relationship, Au- dimensional audio signals.”
- **embedding** — “During training, latent diffusion models (LDMs) are conditioned on an audio embedding E x and trained in a continuous space z 0 learned by VAE.”
- **metric** — “Although RoBERTa and CLAP have the main evaluation metric in this paper.”
- **manipulation** — “The overview of text-guided audio styles manipulation, such as audio style AudioLDM design for TTA generation and text-guided transfer, super-resolution, and inpainting, without fineaudio manipulation is shown in Figure 1.”
- **advantageous** — “One is a small model named AudioLDM-S, which model size, we notice that the larger model is advantageous has 181M parameters, and the other is a large model named for the overall audio qualities.”
- **style transfer** — “Building on the success of guided audio manipulations (e.g., style transfer) StableDiffusion (Rombach et al., 2022), which uses latent in a zero-shot fashion.”
- **computational** — “However, previous studies primarily worked on the label-to-sound setting ous studies in TTA have limited generation qualwith a small set of labels (Liu et al., 2021b; Pascual et al., ity with high computational costs.”
- **gain attention** — “"has recently gained attention for its ability"”
- **continuous** — “In comparison, natural lanbuilt on a latent space to learn continuous audio guage is considerably more flexible than labels as they can representations from contrastive language-audio include fine-grained descriptions of audio signals, such as pretraining (CLAP) embeddings.”

## Abstract（自动提取）

> TITLE: AudioLDM: Text-to-Audio Generation with Latent Diffusion Models ABSTRACT: Text-to-audio (TTA) system has recently gained attention for its ability to synthesize general audio based on text descriptions. However, previous studies in TTA have limited generation quality with high computational costs. In this study, we propose AudioLDM, a TTA system that is built on a latent space to learn the continuous audio representations from contrastive language-audio pretraining (CLAP) latents. The pretrained CLAP models enable us to train LDMs with audio embedding while providing text embedding as a condition during sampling. By learning the latent representations of audio signals and their compositions without modeling the cross-modal relationship, AudioLDM is advantageous in both generation quality and computational efficiency. Trained on AudioCaps with a single GPU, AudioLDM achieves state-of-the-art TTA performance measured by both objective and subjective metrics (e.g., frechet distance). Moreover, AudioLDM is the first TTA system that enables various text-guided audio manipulations (e.g., style transfer) in a zero-shot fashion. Our implementation and demos are available at https://audioldm.github.io.

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

PDF：`/home/user/llm-papers/04_音乐生成/PDF/11_AudioLDM.pdf`

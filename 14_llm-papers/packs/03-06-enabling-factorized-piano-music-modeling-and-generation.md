---
type: paper-pack
paper_id: "03-06"
stage: 3
title: "Enabling Factorized Piano Music Modeling and Generation with the MAESTRO Dataset"
pdf: "/home/user/llm-papers/03_音乐检索理解/PDF/06_MAESTRO_Dataset.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 03-06 Enabling Factorized Piano Music Modeling and Generation with the MAESTRO Dataset

**中文标题**：利用 MAESTRO 数据集实现分解式钢琴音乐建模与生成

**一句话概括**：提出以音符作为中间表示（Wave2Midi2Wave 流程），训练能够转写、作曲并合成音频波形、跨越约六个数量级时间尺度的模型，并发布含 172 小时高精度对齐钢琴演奏的 MAESTRO 数据集。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| alignment | /ɐlˈaɪnmənt/ | 对齐（音符标签与波形的精确对应） | S |
| discrete | /dɪskɹˈiːt/ | 离散的（一个个独立的音符事件） | S |
| synthesize | /sˈɪnθəsˌaɪz/ | 合成（从音符生成音频波形） | S |
| intermediate | /ˌɪntəmˈiːdiət/ | 中间的（介于音频与语义之间的表示） | A |
| suite | /swˈiːt/ | 一套、一组（系列模型） | A |
| span | /spˈan/ | 跨越（覆盖从毫秒到百秒的范围） | A |
| order of magnitude | /ˈɔːdə ˈɒv mˈaɡnɪtjˌuːd/ | 数量级（相差约 10 倍） | A |
| notoriously | /nəʊtˈɔːɹiəsli/ | 出了名地（公认地困难） | B |
| coherently | /kəʊhˈiəɹəntli/ | 连贯地（一致地建模多尺度结构） | B |
| timescale | /tˈaɪmskeɪl/ | 时间尺度（不同长短的时间跨度） | B |
| transcribe | /tɹanskɹˈaɪb/ | 转写（把音频转成音符序列） | B |
| virtuosic | /vˌɜːtjuːˈɒzɪk/ | 技艺高超的（演奏家级别的） | B |

### 原句（保留完整句子）

- **alignment** — “This large advance in the state of the art is enabled by our release of the new MAESTRO (MIDI and Audio Edited for Synchronous TRacks and Organization) dataset, composed of over 172 hours of virtuosic piano performances captured with fine alignment (≈3 ms) between note labels and audio waveforms.”
- **discrete** — “Fortunately, most music is also highly structured and can be represented as discrete note events played on musical instruments.”
- **synthesize** — “6 P IANO S YNTHESIS Most commercially available systems that are able to synthesize a MIDI sequence into a piano audio signal are concatenative: they stitch together snippets of audio from a large library of recordings of individual notes.”
- **intermediate** — “Herein, we show that by using notes as an intermediate representation, we can train a suite of models capable of transcribing, composing, and synthesizing audio waveforms with coherent musical structure on timescales spanning six orders of magnitude (∼0.1 ms to ∼100 s), a process we call Wave2Midi2Wave.”
- **suite** — “Herein, we show that by using notes as an intermediate representation, we can train a suite of models capable of transcribing, composing, and synthesizing audio waveforms with coherent musical structure on timescales spanning six orders of magnitude (∼0.1 ms to ∼100 s), a process we call Wave2Midi2Wave.”
- **span** — “Later in January 2020, GPT-2 was fine- problems, spanning a diverse range of difficult tasks, and tuned using the aforementioned RL algorithms \[79, 128\], showed that GPT-4 can achieve more superior performance which leveraged human preferences to improve the capac- than prior GPT models.”
- **order of magnitude** — “We overcome this barrier by curating and publicly releasing alongside this work a piano performance dataset containing well-aligned audio and symbolic performances an order of magnitude larger than the previous benchmarks.”
- **notoriously** — “Although GANs are very powerful, they are notoriously difficult to train and are usually not applied to sequential data.”
- **coherently** — “Google Brain, † DeepMind {fjord,astas,adarob,iansimon,annahuang,sedielem,eriche,jesseengel,deck}@google.com A BSTRACT arXiv:1810.12247v5 \[cs.SD\] 17 Jan 2019 Generating musical audio directly with neural networks is notoriously difficult because it requires coherently modeling structure at many different timescales.”
- **timescale** — “Each higher module runs with an increasingly longer timescale and a lower time resolution, which is called frame-level module.”
- **transcribe** — “To do this, we transcribe the audio in the MAESTRO training set, although in theory any large set of unlabeled piano music would work.”
- **virtuosic** — “This large advance in the state of the art is enabled by our release of the new MAESTRO (MIDI and Audio Edited for Synchronous TRacks and Organization) dataset, composed of over 172 hours of virtuosic piano performances captured with fine alignment (≈3 ms) between note labels and audio waveforms.”

## Abstract（自动提取）

>  Published as a conference paper at ICLR 2019 E NABLING FACTORIZED P IANO M USIC M ODELING AND G ENERATION WITH THE MAESTRO DATASET Curtis Hawthorne? , Andriy Stasyuk? , Adam Roberts? , Ian Simon? , Cheng-Zhi Anna Huang? , Sander Dieleman† , Erich Elsen? , Jesse Engel? & Douglas Eck? ? Google Brain, † DeepMind {fjord,astas,adarob,iansimon,annahuang,sedielem,eriche,jesseengel,deck}@google.com A BSTRACT arXiv:1810.12247v5 \[cs.SD\] 17 Jan 2019 Generating musical audio directly with neural networks is notoriously difficult because it requires coherently modeling structure at many different timescales. Fortunately, most music is also highly structured and can be represented as discrete note events played on musical instruments. Herein, we show that by using notes as an intermediate representation, we can train a suite of models capable of transcribing, composing, and synthesizing audio waveforms with coherent musical structure on timescales spanning six orders of magnitude (∼0.1 ms to ∼100 s), a process we call Wave2Midi2Wave.

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
- [[14_llm-papers/stage-03-music-retrieval|阶段 3]]

PDF：`/home/user/llm-papers/03_音乐检索理解/PDF/06_MAESTRO_Dataset.pdf`

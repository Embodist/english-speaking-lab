---
type: paper-pack
paper_id: "04-09"
stage: 4
title: "MusicLM: Generating Music From Text"
pdf: "/home/user/llm-papers/04_音乐生成/PDF/09_MusicLM.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 04-09 MusicLM: Generating Music From Text

**中文标题**：MusicLM：从文本生成音乐

**一句话概括**：提出分层序列到序列的音乐生成模型 MusicLM，可在 24kHz 采样率下生成与文本描述高度一致、持续数分钟的高保真音乐，并发布含 5.5k 条专家撰写描述的 MusicCaps 评测数据集。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| hierarchical | /haɪəɹˈɑːkɪkəl/ | 分层的（多级建模） | S |
| high-fidelity | /hˈaɪfɪdˈɛlɪti/ | 高保真的（音质还原度高） | S |
| adherence | /ɐdhˈiəɹəns/ | 遵从、贴合（与文本描述的贴合度） | A |
| melody | /mˈɛlədi/ | 旋律 | A |
| consistent | /kənsˈɪstənt/ | 一致的（音乐保持连贯） | A |
| caption | /kˈapʃən/ | 说明文字（描述音乐的文本） | A |
| violin | /vaɪəlˈɪn/ | 小提琴 | B |
| distorted | /dɪstˈɔːtɪd/ | 失真的（电吉他失真音色） | B |
| riff | /ɹˈɪf/ | 即兴乐段（riff，吉他反复演奏的短乐句） | B |
| sequence-to-sequence | /sˈiːkwənstəsˈiːkwəns/ | 序列到序列的（输入输出都是序列） | B |
| whistled | /wˈɪsəld/ | 吹口哨的 | B |
| hummed | /hˈʌmd/ | 哼唱的 | B |

### 原句（保留完整句子）

- **hierarchical** — “Casting audio synthetional music generation as a hierarchical sequence- sis as a language modeling task in a discrete representation to-sequence modeling task, and it generates music space, and leveraging a hierarchy of coarse-to-fine audio at 24 kHz that remains consistent over several mi- discrete units (or tokens), AudioLM achieves both highnutes.”
- **high-fidelity** — “Yu et al., 2022), recent work has explored generating audio In this work, we introduce MusicLM, a model for generafrom sequence-wide, high-level captions (Yang et al., 2022; ting high-fidelity music from text descriptions.”
- **adherence** — “Our experiments show that MusicLM out- fidelity and long-term coherence over dozens of seconds. performs previous systems both in audio quality Moreover, by making no assumptions about the content and adherence to the text descriptions.”
- **melody** — “Moreover, of the audio signal, AudioLM learns to generate realistic we demonstrate that MusicLM can be conditioned audio from audio-only corpora, be it speech or piano music, on both text and a melody in that it can transform without any annotation.”
- **consistent** — “Casting audio synthetional music generation as a hierarchical sequence- sis as a language modeling task in a discrete representation to-sequence modeling task, and it generates music space, and leveraging a hierarchy of coarse-to-fine audio at 24 kHz that remains consistent over several mi- discrete units (or tokens), AudioLM achieves both highnutes.”
- **caption** — “The ability to model diverse signals whistled and hummed melodies according to the suggests that such a system could generate richer outputs style described in a text caption.”
- **violin** — “MusicLM: Generating Music From Text Acoustic MuLan tokens Semantic tokens Acoustic tokens modeling SoundStream Semantic Decoder MuLan tokens Semantic tokens modeling RVQ k-means RVQ MuLan (Audio) w2v-BERT SoundStream MuLan (Text) Decoder Generated audio 128d Audio 128d Text Embedding Embedding Intermediate RVQ Layer Audio "Hip hop song with Text Network Network Encoder violin solo" Target Audio Figure 2.”
- **distorted** — “However, Intermediate RVQ Layer we opt for quantizing the MuLan embeddings in such a Audio Text Encoder Network Network way that both the audio and the conditioning signal have a homogeneous representation based on discrete tokens, “Rock song with distorted guitar” aiding further research into autoregressively modeling the conditioning signal as well.”
- **riff** — “Training a seq2seq as part of a blues riff, showing that the model has learned a model with lyric conditioning and limiting the dataset only wide range of singing and playing styles. to songs primarily in English made singing both intelligible and controllable. – Completions: We prime the model with 12 seconds of existing songs and ask it to complete them in the same The final model, which we call Jukebox, uses all these styles.”
- **sequence-to-sequence** — “For this, we propose a hierarchical sequencetraining and the MuLan text embedding at inference time. to-sequence modeling task, where each stage is modeled All three of these models are pretrained independently and autoregressively by a separate decoder-only Transformer. then frozen, such that they provide the discrete audio and The proposed approach is illustrated in Figure 2. text representations for the sequence-to-sequence modeling.”
- **whistled** — “The ability to model diverse signals whistled and hummed melodies according to the suggests that such a system could generate richer outputs style described in a text caption.”
- **hummed** — “The ability to model diverse signals whistled and hummed melodies according to the suggests that such a system could generate richer outputs style described in a text caption.”

## Abstract（自动提取）

> TITLE: MusicLM: Generating Music From Text ABSTRACT: We introduce MusicLM, a model generating high-fidelity music from text descriptions such as "a calming violin melody backed by a distorted guitar riff". MusicLM casts the process of conditional music generation as a hierarchical sequence-to-sequence modeling task, and it generates music at 24 kHz that remains consistent over several minutes. Our experiments show that MusicLM outperforms previous systems both in audio quality and adherence to the text description. Moreover, we demonstrate that MusicLM can be conditioned on both text and a melody in that it can transform whistled and hummed melodies according to the style described in a text caption. To support future research, we publicly release MusicCaps, a dataset composed of 5.5k music-text pairs, with rich text descriptions provided by human experts.

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

PDF：`/home/user/llm-papers/04_音乐生成/PDF/09_MusicLM.pdf`

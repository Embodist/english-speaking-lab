---
type: paper-pack
paper_id: "04-07"
stage: 4
title: "AudioLM: a Language Modeling Approach to Audio Generation"
pdf: "/home/user/llm-papers/04_音乐生成/PDF/07_AudioLM.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 04-07 AudioLM: a Language Modeling Approach to Audio Generation

**中文标题**：AudioLM：音频生成的语言建模方法

**一句话概括**：提出把输入音频映射为离散词元、把音频生成当作语言建模任务的框架，并设计混合分词方案兼顾重建质量与长程结构，可在无任何标注下生成连贯、保留说话人身份的语音与钢琴续奏。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| corpus | /kˈɔːpəs/ | 语料库（大批原始音频） | S |
| leverage | /lˈiːvəɹɪdʒ/ | 利用（借助已有成果） | S |
| symbolic | /sɪmbˈɒlɪk/ | 符号的（如乐谱等符号表示） | A |
| synthesis | /sˈɪnθəsˌɪs/ | 合成（音频合成） | A |
| token | /tˈəʊkən/ | 词元、令牌（离散符号单元） | A |
| cast | /kˈast/ | 将…视为（把任务表述为另一种形式） | A |
| codec | /kˈəʊdək/ | 编解码器（压缩/解压音频的模块） | A |
| transcript | /tɹˈanskɹɪpt/ | 转写文本（语音的文字记录） | A |
| consistency | /kənsˈɪstənsi/ | 一致性（长期保持一致） | B |
| trade-off | /tɹˈeɪdˈɒf/ | 权衡（两类指标之间的取舍） | B |
| discretized | /dɪskɹˈɛtaɪzd/ | 离散化的（连续值变成离散值） | B |
| prosody | /pɹˈɒsədi/ | 韵律（语音的节奏与语调） | B |

### 原句（保留完整句子）

- **corpus** — “We also trained it in a semi-supervised setting, using the larger high-confidence and BerkleyParser corpora from with approximately 17M sentences \[37\].”
- **leverage** — “Namely, we leverage the discretized activations of a masked language model pre-trained on audio to capture long-term and piano music continuation.”
- **symbolic** — “Autoregressive modeling of these tokens Furthermore, we demonstrate how our approach extends beyond captures both local dependencies (e.g., phonetics in speech, speech by generating coherent piano music continuations, despite local melody in piano music) and global long-term structure being trained without any symbolic representation of music.”
- **synthesis** — “We achieve this objective by structure and the discrete codes produced by a neural audio codec combining recent advances in adversarial neural audio comto achieve high-quality synthesis.”
- **token** — “At inference time, the model predicts the token sequence ĥ autoregressively. representations of the pre-trained w2v-BERT to model long• A detokenizer model, which maps the sequence of term temporal structure in a generative framework.”
- **cast** — “Due to the excellent capacity in communicating with hu- In this way, the process of solving a task can be cast as a mans, ChatGPT has ignited the excitement of the AI com- word prediction problem for generating the solution text. munity since its release.”
- **codec** — “We achieve this objective by structure and the discrete codes produced by a neural audio codec combining recent advances in adversarial neural audio comto achieve high-quality synthesis.”
- **transcript** — “When trained on speech, waveforms, we first construct coarse semantic tokens from a and without any transcript or annotation, AudioLM generates syntactically and semantically plausible speech continuations while model pre-trained with a self-supervised masked language modalso maintaining speaker identity and prosody for unseen speakers. eling objective \[19\].”
- **consistency** — “Yet, the acoustic diversity quality audio generation with long-term consistency.”
- **trade-off** — “We use w2v-BERT XL \[17\] (0.6B good trade-off between diversity and semantic consistency of parameters) and adopt a set of heuristics for choosing the the generated speech.”
- **discretized** — “Namely, we leverage the discretized activations of a masked language model pre-trained on audio to capture long-term and piano music continuation.”
- **prosody** — “When trained on speech, waveforms, we first construct coarse semantic tokens from a and without any transcript or annotation, AudioLM generates syntactically and semantically plausible speech continuations while model pre-trained with a self-supervised masked language modalso maintaining speaker identity and prosody for unseen speakers. eling objective \[19\].”

## Abstract（自动提取）

> TITLE: AudioLM: a Language Modeling Approach to Audio Generation ABSTRACT: We introduce AudioLM, a framework for high-quality audio generation with long-term consistency. AudioLM maps the input audio to a sequence of discrete tokens and casts audio generation as a language modeling task in this representation space. We show how existing audio tokenizers provide different trade-offs between reconstruction quality and long-term structure, and we propose a hybrid tokenization scheme to achieve both objectives. Namely, we leverage the discretized activations of a masked language model pre-trained on audio to capture long-term structure and the discrete codes produced by a neural audio codec to achieve high-quality synthesis. By training on large corpora of raw audio waveforms, AudioLM learns to generate natural and coherent continuations given short prompts. When trained on speech, and without any transcript or annotation, AudioLM generates syntactically and semantically plausible speech continuations while also maintaining speaker identity and prosody for unseen speakers. Furthermore, we demonstrate how our approach extends beyond speech by generating coherent piano music continuations, despite being trained without any symbolic representation of music.

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

PDF：`/home/user/llm-papers/04_音乐生成/PDF/07_AudioLM.pdf`

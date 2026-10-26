---
type: paper-pack
paper_id: "05-25"
stage: 5
title: "A-JEPA: Joint-Embedding Predictive Architecture Can Listen"
pdf: "/home/user/llm-papers/05_世界模型/PDF/25_AJEPA.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 05-25 A-JEPA: Joint-Embedding Predictive Architecture Can Listen

**中文标题**：A-JEPA：联合嵌入预测架构也能"听"

**一句话概括**：提出音频版联合嵌入预测架构 A-JEPA：在潜空间预测声谱图区域的表征，采用课程式、时间-频率感知的掩码策略与指数移动平均目标编码器，在多个音频与语音分类任务上刷新最先进水平。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| curriculum masking | /kʌɹˈɪkjʊləm mˈaskɪŋ/ | 课程式掩码；由易到难调整掩码策略 | B |
| exponential moving average | /ˌɛkspənˈɛnʃəl mˈuːvɪŋ ˈavɹɪdʒ/ | 指数移动平均；平滑更新参数的机制 | B |
| spectrogram | /spˈɛktɹəɡɹˌam/ | 声谱图；音频的时间-频率可视化 | B |
| time-frequency aware | /tˈaɪmfɹˈiːkwənsi ɐwˈeə/ | 时间-频率感知的；考虑局部时频相关性 | B |
| masked-modeling | /mˈasktmˈɒdəlɪŋ/ | 掩码建模；遮挡部分输入让模型预测 | B |
| foundational vision models | /faʊndˈeɪʃənəl vˈɪʒən mˈɒdəlz/ | 基础视觉模型；大型通用视觉模型 | B |
| regularized masking | /ɹˈɛɡjʊləɹˌaɪzd mˈaskɪŋ/ | 正则化掩码；带正则约束的掩码 | B |
| context encoder | /kˈɒntɛkst ɛŋkˈəʊdə/ | 上下文编码器；编码可见块的网络 | B |
| highly correlated | /hˈaɪli kˈɒɹɪlˌeɪtɪd/ | 高度相关的 | B |
| externally supervised | /ɛkstˈɜːnəli sˈuːpəvˌaɪzd/ | 外部监督的；用外部标注训练的 | B |
| target encoder | /tˈɑːɡɪt ɛŋkˈəʊdə/ | 目标编码器；生成预测目标表征的网络 | B |
| self-supervised learning | /sˈɛlfsˈuːpəvˌaɪzd lˈɜːnɪŋ/ | 自监督学习 | B |

### 原句（保留完整句子）

- **curriculum masking** — “encodes visible audio spectrogram patches with a curriculum masking strategy”
- **exponential moving average** — “extracted by the exponential moving average of context encoder”
- **spectrogram** — “Due to the lossy characteristics of spectrograms and the oversmoothing artifacts caused by insufficiently expressive models, it is always a challenge to generate high-fidelity audio with the help of existing spectrogram model.”
- **time-frequency aware** — “transfer random block masking into time-frequency aware masking”
- **masked-modeling** — “the masked-modeling principle driving the success”
- **foundational vision models** — “large foundational vision models”
- **regularized masking** — “fine-tune the encoder with a regularized masking”
- **context encoder** — “via context encoder”
- **highly correlated** — “highly correlated in local time and frequency”
- **externally supervised** — “models that use externally supervised pre-training”
- **target encoder** — “i.e., target encoder, on the whole spectrogram”
- **self-supervised learning** — “a simple extension method for self-supervised learning”

## 摘要提示（PDF 文本不可提取）

> TITLE: A-JEPA: Joint-Embedding Predictive Architecture Can Listen ABSTRACT: This paper presents that the masked-modeling principle driving the success of large foundational vision models can be effectively applied to audio by making predictions in a latent space. We introduce Audio-based Joint-Embedding Predictive Architecture (A-JEPA), a simple extension method for self-supervised learning from the audio spectrum. Following the design of I-JEPA, our A-JEPA encodes visible audio spectrogram patches with a curriculum masking strategy via context encoder, and predicts the representations of regions sampled at well-designed locations. The target representations of those regions are extracted by the exponential moving average of context encoder, \emph{i.e.}, target encoder, on the whole spectrogram. We find it beneficial to transfer random block masking into time-frequency aware masking in a curriculum manner, considering the complexity of highly correlated in local time and frequency in audio spectrograms. To enhance contextual semantic understanding and robustness, we fine-tune the encoder with a regularized masking on target datasets, instead of input dropping or zero. Empirically, when built with Vision Transformers structure, we find A-JEPA to be highly scalable and sets new state-of-the-art performance on multiple audio and speech classification tasks, outperforming other rec

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
- [[14_llm-papers/stage-05-world-models|阶段 5]]

PDF：`/home/user/llm-papers/05_世界模型/PDF/25_AJEPA.pdf`

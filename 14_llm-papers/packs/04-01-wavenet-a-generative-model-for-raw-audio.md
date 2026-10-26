---
type: paper-pack
paper_id: "04-01"
stage: 4
title: "WaveNet: A Generative Model for Raw Audio"
pdf: "/home/user/llm-papers/04_音乐生成/PDF/01_WaveNet.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 04-01 WaveNet: A Generative Model for Raw Audio

**中文标题**：WaveNet：用于原始音频的生成模型

**一句话概括**：提出全概率、自回归的原始音频波形生成模型 WaveNet，在文本转语音中达到当时最优自然度，还能学习音乐片段生成，并可作为判别模型用于音素识别。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| fidelity | /fɪdˈɛlɪti/ | 保真度（还原度） | S |
| probabilistic | /pɹˌɒbəbɪlˈɪstɪk/ | 概率的（输出为概率分布） | A |
| condition on | /kəndˈɪʃən ˈɒn/ | 以…为条件（生成时给定前序信息） | A |
| novel | /nˈɒvəl/ | 新颖的（从未听过的） | A |
| discriminative | /dɪskɹˈɪmɪnətˌɪv/ | 判别式的（区分类别而非生成的模型） | A |
| predictive | /pɹɪdˈɪktɪv/ | 预测的（预测下一个样本） | B |
| nonetheless | /nˌɒnðəlˈɛs/ | 尽管如此（转折） | B |
| yield | /jˈiːld/ | 产生、带来（取得结果） | B |
| parametric | /pˌaɹəmˈɛtɹɪk/ | 参数化的（基于参数模型的语音合成方法） | B |
| concatenative | /kəŋkˈatənətˌɪv/ | 拼接的（拼接录音片段合成的语音） | B |
| fragment | /fɹˈaɡmənt/ | 片段（音乐片段） | B |
| phoneme | /fˈəʊniːm/ | 音素（语音的最小单位） | B |

### 原句（保留完整句子）

- **fidelity** — “A single WaveNet can capture the characteristics of many different speakers with equal fidelity, and can switch between them by conditioning on the speaker identity.”
- **probabilistic** — “The model is fully probabilistic and autoregressive, with the predictive distribution for each audio sample conditioned on all previous ones; nonetheless we show that it can be efficiently trained on data with tens of thousands of samples per second of audio.”
- **condition on** — “"sample conditioned on all previous ones"”
- **novel** — “When trained to model music, we find that it generates novel and often highly realistic musical fragments.”
- **discriminative** — “We also show that it can be employed as a discriminative model, returning promising results for phoneme recognition.”
- **predictive** — “The model is fully probabilistic and autoregressive, with the predictive distribution for each audio sample conditioned on all previous ones; nonetheless we show that it can be efficiently trained on data with tens of thousands of samples per second of audio.”
- **nonetheless** — “The model is fully probabilistic and autoregressive, with the predictive distribution for each audio sample conditioned on all previous ones; nonetheless we show that it can be efficiently trained on data with tens of thousands of samples per second of audio.”
- **yield** — “On each of these projected versions of queries, keys and values we then perform the attention function in parallel, yielding dv -dimensional 4 To illustrate why the dot products get large, assume that the components of q and k are independent random variables with mean 0 and variance 1.”
- **parametric** — “When applied to text-to-speech, it yields state-ofthe-art performance, with human listeners rating it as significantly more natural sounding than the best parametric and concatenative systems for both English and Mandarin.”
- **concatenative** — “When applied to text-to-speech, it yields state-ofthe-art performance, with human listeners rating it as significantly more natural sounding than the best parametric and concatenative systems for both English and Mandarin.”
- **fragment** — “There are two commonly used retrieval ap- unit \[1031\], corresponding to semantically complete and proaches: lexical-based retrieval \[1026\] using sparse vector relatively independent text fragments, which can effectively representations and semantic retrieval methods using dense reduce the recall of irrelevant information.”
- **phoneme** — “We also show that it can be employed as a discriminative model, returning promising results for phoneme recognition.”

## Abstract（自动提取）

> TITLE: WaveNet: A Generative Model for Raw Audio ABSTRACT: This paper introduces WaveNet, a deep neural network for generating raw audio waveforms. The model is fully probabilistic and autoregressive, with the predictive distribution for each audio sample conditioned on all previous ones; nonetheless we show that it can be efficiently trained on data with tens of thousands of samples per second of audio. When applied to text-to-speech, it yields state-of-the-art performance, with human listeners rating it as significantly more natural sounding than the best parametric and concatenative systems for both English and Mandarin. A single WaveNet can capture the characteristics of many different speakers with equal fidelity, and can switch between them by conditioning on the speaker identity. When trained to model music, we find that it generates novel and often highly realistic musical fragments. We also show that it can be employed as a discriminative model, returning promising results for phoneme recognition.

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

PDF：`/home/user/llm-papers/04_音乐生成/PDF/01_WaveNet.pdf`

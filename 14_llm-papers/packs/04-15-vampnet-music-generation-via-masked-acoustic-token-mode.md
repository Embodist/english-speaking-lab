---
type: paper-pack
paper_id: "04-15"
stage: 4
title: "VampNet: Music Generation via Masked Acoustic Token Modeling"
pdf: "/home/user/llm-papers/04_音乐生成/PDF/15_VampNet.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 04-15 VampNet: Music Generation via Masked Acoustic Token Modeling

**中文标题**：VampNet：基于掩蔽声学词元建模的音乐生成

**一句话概括**：提出非自回归的掩蔽声学词元模型 VampNet，训练时用可变掩蔽调度、推理时用不同"提示"采样，仅 36 次采样即可生成连贯高保真波形，并可通过提示实现压缩、修补、外扩、续写与循环变奏。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| inference | /ˈɪnfəɹəns/ | 推理（模型使用时） | S |
| inpainting | /ˈɪnpeɪntɪŋ/ | 修补、填充（补全中间缺失的部分） | A |
| bidirectional | /baɪdaɪɹˈɛkʃənəl/ | 双向的（同时看到前后文） | A |
| forward pass | /fˈɔːwəd pˈas/ | 前向传播（一次完整的前向计算） | A |
| variation | /vˌeəɹɪˈeɪʃən/ | 变奏（对主题的变化重复） | A |
| flexible | /flˈɛksɪbəl/ | 灵活的（提示方式灵活） | A |
| masked | /mˈaskt/ | 掩蔽的（遮盖部分词元让模型预测） | B |
| acoustic | /ɐkˈuːstɪk/ | 声学的（声音层面的） | B |
| outpainting | /aʊtpˈeɪntɪŋ/ | 外扩填充（向外续写缺失部分） | B |
| looping | /lˈuːpɪŋ/ | 循环（循环播放片段） | B |
| instrumentation | /ˌɪnstɹəməntˈeɪʃən/ | 配器（乐器配置） | B |
| co-creation | /kˈəʊkɹiːˈeɪʃən/ | 共同创作（人与 AI 协作创作） | B |

### 原句（保留完整句子）

- **inference** — “As we show later, different approaches generating each acoustic token in the sequence in a step- to masking, applied at inference time, can be used to steer by-step fashion using transformer-based \[18\] decoder-only generation in useful and artistic ways. models.”
- **inpainting** — “We first convert audio into tasks like music compression, inpainting, outpainting, cona sequence of discrete tokens using an audio tokenizer.”
- **bidirectional** — “VampNet is non-autoregressive, leveraging a bidirectional transformer architecture that attends to all tokens in a forward pass.”
- **forward pass** — “VampNet is non-autoregressive, leveraging a bidirectional transformer architecture that attends to all tokens in a forward pass.”
- **variation** — “Totinuation, and looping with variation (vamping).”
- **flexible** — “This flexible prompting capability makes VampNet levels.”
- **masked** — “VAMPNET: MUSIC GENERATION VIA MASKED ACOUSTIC TOKEN MODELING Hugo Flores García1,2 Prem Seetharaman1 Rithesh Kumar1 Bryan Pardo2 1 Descript Inc.”
- **acoustic** — “VAMPNET: MUSIC GENERATION VIA MASKED ACOUSTIC TOKEN MODELING Hugo Flores García1,2 Prem Seetharaman1 Rithesh Kumar1 Bryan Pardo2 1 Descript Inc.”
- **outpainting** — “We first convert audio into tasks like music compression, inpainting, outpainting, cona sequence of discrete tokens using an audio tokenizer.”
- **looping** — “Totinuation, and looping with variation (vamping).”
- **instrumentation** — “Approprikens are masked, and then passed to a masked generative ately prompted, VampNet is capable of maintaining style, model, which predicts values for masked tokens via an effigenre, instrumentation, and other high-level aspects of the cient iterative parallel decoding sampling procedure at two music.”
- **co-creation** — “We then decode the result back to audio. a powerful music co-creation tool.”

## Abstract（自动提取）

> TITLE: VampNet: Music Generation via Masked Acoustic Token Modeling ABSTRACT: We introduce VampNet, a masked acoustic token modeling approach to music synthesis, compression, inpainting, and variation. We use a variable masking schedule during training which allows us to sample coherent music from the model by applying a variety of masking approaches (called prompts) during inference. VampNet is non-autoregressive, leveraging a bidirectional transformer architecture that attends to all tokens in a forward pass. With just 36 sampling passes, VampNet can generate coherent high-fidelity musical waveforms. We show that by prompting VampNet in various ways, we can apply it to tasks like music compression, inpainting, outpainting, continuation, and looping with variation (vamping). Appropriately prompted, VampNet is capable of maintaining style, genre, instrumentation, and other high-level aspects of the music. This flexible prompting capability makes VampNet a powerful music co-creation tool. Code and audio samples are available online.

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

PDF：`/home/user/llm-papers/04_音乐生成/PDF/15_VampNet.pdf`

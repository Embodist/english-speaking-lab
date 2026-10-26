---
type: paper-pack
paper_id: "04-14"
stage: 4
title: "Mustango: Toward Controllable Text-to-Music Generation"
pdf: "/home/user/llm-papers/04_音乐生成/PDF/14_Mustango.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 04-14 Mustango: Toward Controllable Text-to-Music Generation

**中文标题**：Mustango：迈向可控的文本到音乐生成

**一句话概括**：提出基于扩散、融入音乐领域知识的文生音乐系统 Mustango，其核心 MuNet 引导模块可在逆向扩散过程中加入和弦、节拍、速度、调性等音乐条件，并发布含 5.2 万条乐理描述样本的 MusicBench 数据集。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| controllability | /kəntɹˌəʊləbˈɪlɪti/ | 可控性（对生成结果的控制能力） | A |
| tempo | /tˈɛmpəʊ/ | 速度（音乐的快慢） | A |
| steer | /stˈiə/ | 引导（引导生成方向） | A |
| dynamic | /daɪnˈamɪk/ | 力度的（音乐强弱变化） | A |
| extract | /ˈɛkstɹakt/ | 提取（提取音乐特征） | A |
| barely | /bˈeəli/ | 几乎不（很少被探索） | B |
| chord | /kˈɔːd/ | 和弦 | B |
| key | /kˈiː/ | 调性（音乐的调） | B |
| reverse diffusion | /ɹɪvˈɜːs dɪfjˈuːʒən/ | 逆向扩散（扩散模型生成时的去噪过程） | B |
| harmonic | /hɑːmˈɒnɪk/ | 和声的（和弦方面） | B |
| rhythmic | /ɹˈɪðmɪk/ | 节奏的 | B |
| append | /ɐpˈɛnd/ | 附加（把特征附到描述文本后） | B |

### 原句（保留完整句子）

- **controllability** — “We thus argue that that includes altering the harmonic, rhythmic, including this information during generation may and dynamic aspects of music audio and using improve the current text-to-music models in terms state-of-the-art Music Information Retrieval of musicality and controllability (e.g., following methods to extract the music features which metrical structure and chord progressions).”
- **tempo** — “The controllabil- cific rules related to, for instance, tempo, key, and ity of various musical aspects, however, has chord progressions.”
- **steer** — “During 2.1 Feature Extraction and Description inference, these additional descriptive texts could Enrichment steer the music generation towards user-specified We extract four common music features: beats and music quality.”
- **dynamic** — “We thus argue that that includes altering the harmonic, rhythmic, including this information during generation may and dynamic aspects of music audio and using improve the current text-to-music models in terms state-of-the-art Music Information Retrieval of musicality and controllability (e.g., following methods to extract the music features which metrical structure and chord progressions).”
- **extract** — “We thus argue that that includes altering the harmonic, rhythmic, including this information during generation may and dynamic aspects of music audio and using improve the current text-to-music models in terms state-of-the-art Music Information Retrieval of musicality and controllability (e.g., following methods to extract the music features which metrical structure and chord progressions).”
- **barely** — “Evaluating whether or not the barely been explored.”
- **chord** — “The controllabil- cific rules related to, for instance, tempo, key, and ity of various musical aspects, however, has chord progressions.”
- **key** — “The controllabil- cific rules related to, for instance, tempo, key, and ity of various musical aspects, however, has chord progressions.”
- **reverse diffusion** — “Although the textual descriptions in from the text prompt, as well as the general the existing datasets include details like instrumentext embedding, during the reverse diffusion tation or vibe, more representational descriptions process.”
- **harmonic** — “To overcome the limited availability of open datasets of music with text captions, that capture the structural, melodic, and harmonic we propose a novel data augmentation method aspects of music are missing.”
- **rhythmic** — “We thus argue that that includes altering the harmonic, rhythmic, including this information during generation may and dynamic aspects of music audio and using improve the current text-to-music models in terms state-of-the-art Music Information Retrieval of musicality and controllability (e.g., following methods to extract the music features which metrical structure and chord progressions).”
- **append** — “Finally, the test instance is appended to the demonstration These two approaches are detailed below. as the input for LLMs to generate the output.”

## Abstract（自动提取）

> TITLE: Mustango: Toward Controllable Text-to-Music Generation ABSTRACT: The quality of the text-to-music models has reached new heights due to recent advancements in diffusion models. The controllability of various musical aspects, however, has barely been explored. In this paper, we propose Mustango: a music-domain-knowledge-inspired text-to-music system based on diffusion. Mustango aims to control the generated music, not only with general text captions, but with more rich captions that can include specific instructions related to chords, beats, tempo, and key. At the core of Mustango is MuNet, a Music-Domain-Knowledge-Informed UNet guidance module that steers the generated music to include the music-specific conditions, which we predict from the text prompt, as well as the general text embedding, during the reverse diffusion process. To overcome the limited availability of open datasets of music with text captions, we propose a novel data augmentation method that includes altering the harmonic, rhythmic, and dynamic aspects of music audio and using state-of-the-art Music Information Retrieval methods to extract the music features which will then be appended to the existing descriptions in text format. We release the resulting MusicBench dataset which contains over 52K instances and includes music-theory-based descriptions in the caption text. Through extensive experiments, w

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

PDF：`/home/user/llm-papers/04_音乐生成/PDF/14_Mustango.pdf`

---
type: paper-pack
paper_id: "00-04"
stage: 0
title: "A Comprehensive Survey on Deep Music Generation: Multi-level Representations, Algorithms, Evaluations, and Future Directions"
pdf: "/home/user/llm-papers/00_总览综述/PDF/04_Survey_Deep_Music_Generation.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 00-04 A Comprehensive Survey on Deep Music Generation: Multi-level Representations, Algorithms, Evaluations, and Future Directions

**中文标题**：《深度音乐生成综合综述：多层次表示、算法、评估与未来方向》

**一句话概括**：按乐谱生成、演奏生成、音频生成三个层次全面综述深度音乐生成任务，总结各任务的数据集、音乐表示与评估方法并展望未来方向。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| comprehensive | /kˌɒmpɹɪhˈɛnsɪv/ | 全面的、综合的（comprehensive survey 全面综述，学术高频词） | S |
| representation | /ɹˌɛpɹɪzˈɛntˈeɪʃən/ | 表示（music representations 音乐的编码/表达形式，如音符、MIDI） | S |
| corresponding | /kˌɒɹɪspˈɒndɪŋ/ | 相应的、对应的（corresponding to 与……相对应） | A |
| stage | /stˈeɪdʒ/ | 阶段（本文把音乐制作流程分成三个阶段） | A |
| timbre | /tˈambə/ | 音色（区分不同乐器/声音的特质） | A |
| utilization | /jˌuːtɪlaɪzˈeɪʃən/ | 利用、运用（utilize 的名词形式，学术写作高频） | B |
| widespread | /wˈaɪdspɹɛd/ | 广泛的（attract widespread attention 引起广泛关注） | B |
| convert | /kənvˈɜːt/ | 转换（convert A into B 把 A 转换成 B） | B |
| assign | /ɐsˈaɪn/ | 分配、赋予（assigning timbre 给音符指定音色） | B |
| evolution | /ɪvəlˈuːʃən/ | 演变、发展（model evolution 模型的发展历程） | B |
| pros and cons | /pɹˈəʊz ˈand kˈɒnz/ | 优缺点、利与弊（指同一任务不同方法的长处与不足） | B |
| illustrate | /ˈɪləstɹˌeɪt/ | 阐明、说明（have not been clearly illustrated 尚未被清楚阐明） | B |

### 原句（保留完整句子）

- **comprehensive** — “A Comprehensive Survey on Deep Music Generation: Multi-level Representations, Algorithms, Evaluations, and Future Directions.”
- **representation** — “Score considers musical features such as pitch, duration and chord progression, and its representation is discrete, while performance involves more abundant dynamics and timing information, determining various musical expressions \[2\].”
- **corresponding** — “Especially music, the topic of this paper, has attracted widespread attention of countless researchers.The whole process of producing music can be divided into three stages, corresponding to the three levels of music generation: score generation produces scores, performance generation adds performance characteristics to the scores, and audio generation converts scores with performance characteristics into audio by assigning timbre or generates music in audio format directly.”
- **stage** — “Thus the music generation process is usually divided into three stages \[1\], as shown in Figure 1: in the first stage, composers produce music scores; in the second stage, performers perform scores and generate performance; in the last stage, the performance is rendered into sound by adding different timbres (instruments) and perceived by human beings (listeners).”
- **timbre** — “Especially music, the topic of this paper, has attracted widespread attention of countless researchers.The whole process of producing music can be divided into three stages, corresponding to the three levels of music generation: score generation produces scores, performance generation adds performance characteristics to the scores, and audio generation converts scores with performance characteristics into audio by assigning timbre or generates music in audio format directly.”
- **utilization** — “MSMICA employed adversarial training to learn music style, the model can not only maintain the harmony of the generated music, but also control the music style for better utilization.”
- **widespread** — “Especially music, the topic of this paper, has attracted widespread attention of countless researchers.The whole process of producing music can be divided into three stages, corresponding to the three levels of music generation: score generation produces scores, performance generation adds performance characteristics to the scores, and audio generation converts scores with performance characteristics into audio by assigning timbre or generates music in audio format directly.”
- **convert** — “Good performance not only needs to convert the notes in the score into physical actions with precise timing and correct pitch on the instrument, but also needs to transfer emotion and information through subtle control of tempo, dynamics, articulations and other performance elements \[194\].”
- **assign** — “(right) Multi-Head Attention consists of several attention layers running in parallel. of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key.”
- **evolution** — “However, the development history, the model evolution, as well as the pros and cons of same music generation task have not been clearly illustrated.”
- **pros and cons** — “However, the development history, the model evolution, as well as the pros and cons of same music generation task have not been clearly illustrated.”
- **illustrate** — “5) Keyscapes Keyscapes are used to illustrate the tonality of musical works, with different color for each key.”

## Abstract（自动提取）

> TITLE: A Comprehensive Survey on Deep Music Generation: Multi-level Representations, Algorithms, Evaluations, and Future Directions ABSTRACT: The utilization of deep learning techniques in generating various contents (such as image, text, etc.) has become a trend. Especially music, the topic of this paper, has attracted widespread attention of countless researchers.The whole process of producing music can be divided into three stages, corresponding to the three levels of music generation: score generation produces scores, performance generation adds performance characteristics to the scores, and audio generation converts scores with performance characteristics into audio by assigning timbre or generates music in audio format directly. Previous surveys have explored the network models employed in the field of automatic music generation. However, the development history, the model evolution, as well as the pros and cons of same music generation task have not been clearly illustrated. This paper attempts to provide an overview of various composition tasks under different music generation levels, covering most of the currently popular music generation tasks using deep learning. In addition, we summarize the datasets suitable for diverse tasks, discuss the music representations, the evaluation methods as well as the challenges under different levels, and finally point out several fu

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
- [[14_llm-papers/stage-00-surveys|阶段 0]]

PDF：`/home/user/llm-papers/00_总览综述/PDF/04_Survey_Deep_Music_Generation.pdf`

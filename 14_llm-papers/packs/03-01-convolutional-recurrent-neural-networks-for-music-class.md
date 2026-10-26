---
type: paper-pack
paper_id: "03-01"
stage: 3
title: "Convolutional Recurrent Neural Networks for Music Classification"
pdf: "/home/user/llm-papers/03_音乐检索理解/PDF/01_CRNN_MusicClassification.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 03-01 Convolutional Recurrent Neural Networks for Music Classification

**中文标题**：用于音乐分类的卷积循环神经网络

**一句话概括**：提出结合 CNN 局部特征提取与 RNN 时序汇总的 CRNN 音乐标注模型，在控制参数数量的前提下，其性能与训练效率均优于三种纯 CNN 结构。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| temporal | /tˈɛmpəɹəl/ | 时间上的、时序的 | A |
| recurrent | /ɹɪkˈʌɹənt/ | 循环的（循环神经网络中的"循环"） | A |
| hybrid | /hˈaɪbɹɪd/ | 混合的（此处指 CNN+RNN 的混合结构） | A |
| introduce | /ˌɪntɹədjˈuːs/ | 提出、引入（新方法） | B |
| take advantage of | /tˈeɪk ɐdvˈantɪdʒ ˈɒv/ | 利用、发挥…的优势 | B |
| extraction | /ɛkstɹˈakʃən/ | 提取（特征提取） | B |
| summarisation | /sˌʌməɹaɪzˈeɪʃən/ | 汇总、概括（把时序信息压缩成摘要） | B |
| with respect to | /wˈɪð ɹɪspˈɛkt tˈuː/ | 就…而言、关于 | B |
| indicate | /ˈɪndɪkˌeɪt/ | 表明、显示（结论） | B |
| overall | /ˌəʊvəɹˈɔːl/ | 总体而言 | B |

### 原句（保留完整句子）

- **temporal** — “This structure was first current neural networks for temporal summarisation of the proposed in \[7\] for document classification and later applied extracted features.”
- **recurrent** — “Adopting an RNN We introduce a convolutional recurrent neural network (CRNN) for aggregating the features enables the networks to take the for music tagging.”
- **hybrid** — “This flexibility can be helpful beparameter and training time, indicating the effectiveness of cause some of the tags (e.g., mood tags) may be affected by its hybrid structure in music feature extraction and feature the global structure while other tags such as instruments can summarisation. be affected by local and short-segment information.”
- **introduce** — “Adopting an RNN We introduce a convolutional recurrent neural network (CRNN) for aggregating the features enables the networks to take the for music tagging.”
- **take advantage of** — “CRNNs take advantage of convolutional global structure into account while local features are extracted neural networks (CNNs) for local feature extraction and re- by the remaining convolutional layers.”
- **extraction** — “CRNNs take advantage of convolutional global structure into account while local features are extracted neural networks (CNNs) for local feature extraction and re- by the remaining convolutional layers.”
- **summarisation** — “This structure was first current neural networks for temporal summarisation of the proposed in \[7\] for document classification and later applied extracted features.”
- **with respect to** — “RNNs are more the number of parameters with respect to their performance flexible in selecting how to summarise the local features than and training time per sample.”
- **indicate** — “For small language models, it aware that a direct decrease in language modeling loss does is usually difficult to solve complex tasks that involve not always indicate an improvement of model performance 8.”
- **overall** — “Overall, we found that CRNNs CNNs which are rather static by using weighted average (conshow a strong performance with respect to the number of volution) and subsampling.”

## Abstract（自动提取）

> TITLE: Convolutional Recurrent Neural Networks for Music Classification ABSTRACT: We introduce a convolutional recurrent neural network (CRNN) for music tagging. CRNNs take advantage of convolutional neural networks (CNNs) for local feature extraction and recurrent neural networks for temporal summarisation of the extracted features. We compare CRNN with three CNN structures that have been used for music tagging while controlling the number of parameters with respect to their performance and training time per sample. Overall, we found that CRNNs show a strong performance with respect to the number of parameter and training time, indicating the effectiveness of its hybrid structure in music feature extraction and feature summarisation.

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

PDF：`/home/user/llm-papers/03_音乐检索理解/PDF/01_CRNN_MusicClassification.pdf`

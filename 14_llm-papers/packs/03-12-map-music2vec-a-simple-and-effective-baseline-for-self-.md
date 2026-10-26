---
type: paper-pack
paper_id: "03-12"
stage: 3
title: "MAP-Music2Vec: A Simple and Effective Baseline for Self-Supervised Music Audio Representation Learning"
pdf: "/home/user/llm-papers/03_音乐检索理解/PDF/12_Music2Vec.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 03-12 MAP-Music2Vec: A Simple and Effective Baseline for Self-Supervised Music Audio Representation Learning

**中文标题**：MAP-Music2Vec：自监督音乐音频表示学习的简单有效基线

**一句话概括**：设计 Music2Vec 框架，系统探索用于原始音乐波形的各种自监督学习组件与技巧，以不到 Jukebox 2% 的参数规模达到与其相当的音乐自监督表示学习效果。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| state-of-the-art | /stˈeɪtɒvðɪˈɑːt/ | 最先进的（音乐 SSL 最优模型） | S |
| comparable | /kˈɒmpəɹəbəl/ | 相当的（与最优模型水平相近） | S |
| framework | /fɹˈeɪmwɜːk/ | 框架（完整的方案体系） | A |
| raw | /ɹˈɔː/ | 原始的（未经处理的音频波形） | A |
| waveform | /wˈeɪvfɔːm/ | 波形（音频信号形态） | A |
| release | /ɹɪlˈiːs/ | 发布（公开模型） | A |
| witness | /wˈɪtnəs/ | 见证（社区见证了快速增长） | B |
| exponentially | /ˌɛkspənˈɛnʃəli/ | 指数级地（增长极快） | B |
| unexplored | /ˌʌnɛksplˈɔːd/ | 未探索的（尚未研究清楚） | B |
| component | /kəmpˈəʊnənt/ | 组件（算法模块） | B |
| despite | /dɪspˈaɪt/ | 尽管（虽然参数少得多） | B |

### 原句（保留完整句子）

- **state-of-the-art** — “On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature.”
- **comparable** — “Our model achieves comparable results to the stateof-the-art (SOTA) music SSL model Jukebox, despite be- Teacher Model Student Model ing significantly smaller with less than 2% of parameters of the latter.”
- **framework** — “However, it still remains unexplored how to build a framework for learning useful representations of raw music Masked Input waveforms in a self-supervised manner.”
- **raw** — “However, it still remains unexplored how to build a framework for learning useful representations of raw music Masked Input waveforms in a self-supervised manner.”
- **waveform** — “The representation of audio is continuous, and two common representations are waveform and spectrum.”
- **release** — “In contrast, the teacher We follow the standard pretraining protocols of model takes the unmasked input and provides contextual data2vec \[3\] with the fairseq framework \[4\], and fur- prediction targets in the pre-training. ther release our computationally affordable models.”
- **witness** — “The exploration of science by humans has Wikipedia pages) \[55, 56, 112\], high-quality synthesized been witnessed by the increasing growth of scientific publi- data \[135, 229–231\], or a combination of both.”
- **exponentially** — “EfficientNet \[TL19\] advocates scaling depth and width exponentially (with different coefficients) for optimal performance of image models, resulting in a power-law scaling of width as a function of depth.”
- **unexplored** — “However, it still remains unexplored how to build a framework for learning useful representations of raw music Masked Input waveforms in a self-supervised manner.”
- **component** — “On each of these projected versions of queries, keys and values we then perform the attention function in parallel, yielding dv -dimensional 4 To illustrate why the dot products get large, assume that the components of q and k are independent random variables with mean 0 and variance 1.”
- **despite** — “Our model achieves comparable results to the stateof-the-art (SOTA) music SSL model Jukebox, despite be- Teacher Model Student Model ing significantly smaller with less than 2% of parameters of the latter.”

## Abstract（自动提取）

>  MAP-MUSIC2VEC: A SIMPLE AND EFFECTIVE BASELINE FOR SELF-SUPERVISED MUSIC AUDIO REPRESENTATION LEARNING Yizhi Li1∗ Ruibin Yuan2,4∗ Ge Zhang2,5∗ Yinghao Ma3∗ Chenghua Lin 1† Xingran Chen 5 Anton Ragni1 Hanzhi Yin4 Zhijie Hu6 Haoyu He7 Emmanouil Benetos3 Norbert Gyenge1 Ruibo Liu 8 Jie Fu2† 1 Department of Computer Science, University of Sheffield, UK 2 Beijing Academy of Artificial Intelligence, China 3 Centre for Digital Music, Queen Mary University of London, UK 4 School of Music, Carnegie Mellon University, PA, USA 5 University of Michigan Ann Arbor, USA 6 HSBC Business School, Peking University, China 7 University of Tübingen & MPI-IS, Germany 8 Dartmouth College, NH, USA {yizhi.li, c.lin}@sheffield.ac.uk, yinghao.ma@qmul.ac.uk, fujie@baai.ac.cn ABSTRACT Original Input arXiv:2212.02508v1 \[cs.SD\] 5 Dec 2022 G Em C D B7 Am7 The deep learning community has witnessed an exponentially growing interest in self-supervised learning (SSL).

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

PDF：`/home/user/llm-papers/03_音乐检索理解/PDF/12_Music2Vec.pdf`

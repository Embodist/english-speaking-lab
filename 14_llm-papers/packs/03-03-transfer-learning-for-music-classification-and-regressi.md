---
type: paper-pack
paper_id: "03-03"
stage: 3
title: "Transfer learning for music classification and regression tasks"
pdf: "/home/user/llm-papers/03_音乐检索理解/PDF/03_TransferLearning_Music.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 03-03 Transfer learning for music classification and regression tasks

**中文标题**：面向音乐分类与回归任务的迁移学习

**一句话概括**：提出把预训练卷积网络多层特征图的激活值拼接成通用音乐特征向量，迁移到其他音乐分类与回归任务后，全面优于 MFCC 基线特征及多种聚合 MFCC 的既有方法。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| outperform | /aʊtpəfˈɔːm/ | 优于、超过（基线） | S |
| baseline | /bˈeɪslaɪn/ | 基线、基准（作对比的最简单方法） | S |
| pre-trained | /pɹˈiːtɹˈeɪnd/ | 预训练的（先在别的任务上训练好的） | A |
| propose | /pɹəpˈəʊz/ | 提出（方法） | A |
| general-purpose | /dʒˈɛnəɹəlpˈɜːpəs/ | 通用的（适用于多种任务） | A |
| transfer | /tɹˈansfɜː/ | 迁移（把模型用到新任务） | A |
| transfer learning | /tɹˈansfɜː lˈɜːnɪŋ/ | 迁移学习（把某任务学到的知识用于另一任务） | A |
| regression | /ɹɪɡɹˈɛʃən/ | 回归（预测连续数值的任务） | B |
| concatenated | /kəŋkˈatənˌeɪtɪd/ | 拼接的、串联的（把向量连在一起） | B |
| activation | /ˌaktɪvˈeɪʃən/ | 激活值（网络层输出的数值） | B |
| aggregate | /ˈaɡɹɪɡˌeɪt/ | 聚合（把多个特征合并统计） | B |

### 原句（保留完整句子）

- **outperform** — “The best performing random convnet features do not outperform the best-performing convnet feareports 94.9% of weighted average recall.”
- **baseline** — “The convnet feature out- recommendation, Choi et al. used the weights of a conperforms the baseline MFCC feature in all the considered volutional neural network for feature extraction in playlist tasks and several previous approaches that are aggregating generation \[10\], while Liang et al. used a multi-layer perMFCCs as well as low- and high-level music features. ceptron for feature extraction of content-aware collaborative filtering \[29\].”
- **pre-trained** — “We propose to embedding \[57\] of mel-spectrogram representations and use a pre-trained convnet feature, a concatenated feature genre/similarity/tag labels \[20\].”
- **propose** — “We propose to embedding \[57\] of mel-spectrogram representations and use a pre-trained convnet feature, a concatenated feature genre/similarity/tag labels \[20\].”
- **general-purpose** — “We show how this perceptron is combined with the spherical K-means algoconvnet feature can serve as general-purpose music repre- rithm \[16\] trained on tags and play-count data \[54\].”
- **transfer** — “In this paper, we present a transfer learning approach for proposed to directly learn music features using linear music classification and regression tasks.”
- **transfer learning** — “In this paper, we present a transfer learning approach for proposed to directly learn music features using linear music classification and regression tasks.”
- **regression** — “In this paper, we present a transfer learning approach for proposed to directly learn music features using linear music classification and regression tasks.”
- **concatenated** — “We propose to embedding \[57\] of mel-spectrogram representations and use a pre-trained convnet feature, a concatenated feature genre/similarity/tag labels \[20\].”
- **activation** — “Exponential linear unit (ELU) is used as an activation function in all convolutional layers \[15\].”
- **aggregate** — “In the long convolution module, the number of layers in each Hyena module. filters based on relative positions are used to aggregate information at different positions into the middle represenModel Decoding Complexity Training Complexity tations, and gating functions are employed to further project Transformer O(H(T + H)) O(T H(T + H)) intermediate representations into the final output.”

## Abstract（自动提取）

> TITLE: Transfer learning for music classification and regression tasks ABSTRACT: In this paper, we present a transfer learning approach for music classification and regression tasks. We propose to use a pre-trained convnet feature, a concatenated feature vector using the activations of feature maps of multiple layers in a trained convolutional network. We show how this convnet feature can serve as general-purpose music representation. In the experiments, a convnet is trained for music tagging and then transferred to other music-related classification and regression tasks. The convnet feature outperforms the baseline MFCC feature in all the considered tasks and several previous approaches that are aggregating MFCCs as well as low- and high-level music features.

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

PDF：`/home/user/llm-papers/03_音乐检索理解/PDF/03_TransferLearning_Music.pdf`

---
type: paper-pack
paper_id: "03-00"
stage: 3
title: "Automatic tagging using deep convolutional neural networks"
pdf: "/home/user/llm-papers/03_音乐检索理解/PDF/00_MusicAutoTagging_DeepCNN.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 03-00 Automatic tagging using deep convolutional neural networks

**中文标题**：使用深度卷积神经网络进行自动标注

**一句话概括**：提出基于内容的音乐自动标注算法，只用二维卷积与下采样层组成不同网络结构，在 MagnaTagATune 上以梅尔频谱图输入取得当时最优性能，并证明更复杂的模型受益于更多训练数据。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| outperform | /aʊtpəfˈɔːm/ | 表现优于、胜过 | S |
| state-of-the-art | /stˈeɪtɒvðɪˈɑːt/ | 最先进的、当时最优的 | S |
| architecture | /ˈɑːkɪtˌɛktʃə/ | 网络结构、架构 | S |
| measure | /mˈɛʒə/ | 衡量、测定（指标） | A |
| tagging | /tˈaɡɪŋ/ | （音乐）标注、打标签 | B |
| content-based | /kˈɒntɛntbˈeɪst/ | 基于内容的（依据音频本身特征而非元数据） | B |
| convolutional | /kɒnvəlˈuːʃənəl/ | 卷积的（神经网络中的卷积运算） | B |
| subsampling | /sˈʌbsamplɪŋ/ | 下采样（降低特征维度的操作） | B |
| complexity | /kəmplˈɛksɪti/ | 复杂度（此处指网络规模） | B |
| effective | /ɪfˈɛktɪv/ | 有效的 | B |
| benefit from | /bˈɛnɪfˌɪt fɹˈɒm/ | 受益于 | B |

### 原句（保留完整句子）

- **outperform** — “While for small values of dk the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of dk \[3\].”
- **state-of-the-art** — “CNNs have been introduced in audio-based problems for From the perspective of feature extraction, there have been similar reasons, showing state-of-the-art performance in two main types of systems proposed in the literature.”
- **architecture** — “Since these are frame-level features, els outperformed the 4-layer architecture.”
- **measure** — “In the ex- Aggregating hand-crafted features for music tagging was periments, we measure the AUC-ROC scores of the archi- introduced in \[25\].”
- **tagging** — “A more recent approach unifies feature exWe present a content-based automatic music tagging algo- traction with machine learning to allow relevant features to rithm using fully convolutional neural networks (FCNs). be learnt automatically.”
- **content-based** — “A more recent approach unifies feature exWe present a content-based automatic music tagging algo- traction with machine learning to allow relevant features to rithm using fully convolutional neural networks (FCNs). be learnt automatically.”
- **convolutional** — “A more recent approach unifies feature exWe present a content-based automatic music tagging algo- traction with machine learning to allow relevant features to rithm using fully convolutional neural networks (FCNs). be learnt automatically.”
- **subsampling** — “This approach is known as feature We evaluate different architectures consisting of 2D con- learning and requires deep neural networks (DNNs). volutional layers and subsampling layers only.”
- **complexity** — “While the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code.”
- **effective** — “The experiments their statistics such as mean and variance are computed show that mel-spectrogram is an effective time-frequency \[25\], or they are clustered and vector quantised \[15\] to obrepresentation for automatic tagging and that more com- tain clip-level features.”
- **benefit from** — “Finally, classifiers such as k-NN or plex models benefit from more training data.”

## Abstract（自动提取）

> TITLE: Automatic tagging using deep convolutional neural networks ABSTRACT: We present a content-based automatic music tagging algorithm using fully convolutional neural networks (FCNs). We evaluate different architectures consisting of 2D convolutional layers and subsampling layers only. In the experiments, we measure the AUC-ROC scores of the architectures with different complexities and input types using the MagnaTagATune dataset, where a 4-layer architecture shows state-of-the-art performance with mel-spectrogram input. Furthermore, we evaluated the performances of the architectures with varying the number of layers on a larger dataset (Million Song Dataset), and found that deeper models outperformed the 4-layer architecture. The experiments show that mel-spectrogram is an effective time-frequency representation for automatic tagging and that more complex models benefit from more training data.

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

PDF：`/home/user/llm-papers/03_音乐检索理解/PDF/00_MusicAutoTagging_DeepCNN.pdf`

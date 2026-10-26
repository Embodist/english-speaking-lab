---
type: paper-pack
paper_id: "03-09"
stage: 3
title: "AST: Audio Spectrogram Transformer"
pdf: "/home/user/llm-papers/03_音乐检索理解/PDF/09_AST_AudioSpectrogramTransformer.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 03-09 AST: Audio Spectrogram Transformer

**中文标题**：AST：音频频谱图 Transformer

**一句话概括**：提出首个完全无卷积、纯注意力机制的音频分类模型 AST（音频频谱图 Transformer），回答"音频分类是否必须依赖 CNN"的问题，并在 AudioSet 等多个基准上刷新最优结果。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| benchmark | /bˈɛntʃmɑːk/ | 基准（标准评测数据集） | S |
| end-to-end | /ˈɛndtʊˈɛnd/ | 端到端的（从输入直接学到输出） | S |
| capture | /kˈaptʃə/ | 捕捉（获取信息） | A |
| self-attention | /sˈɛlfɐtˈɛnʃən/ | 自注意力（Transformer 的核心机制） | A |
| adopt | /ɐdˈɒpt/ | 采用（被广泛采用） | A |
| mapping | /mˈapɪŋ/ | 映射（输入到输出的对应关系） | A |
| long-range | /lˈɒŋɹˈeɪndʒ/ | 长距离的、长程的（全局上下文） | A |
| hybrid | /hˈaɪbɹɪd/ | 混合的（CNN 加注意力的组合） | A |
| reliance | /ɹɪlˈaɪəns/ | 依赖（对 CNN 的依赖） | A |
| accuracy | /ˈakjʊɹəsi/ | 准确率 | A |
| building block | /bˈɪldɪŋ blˈɒk/ | 基本构件、核心组成单元 | B |
| purely | /pjˈʊəli/ | 纯粹地（完全基于…） | B |

### 原句（保留完整句子）

- **benchmark** — “A recent study \[69\] found that a model size of 62B is better performance on downstream tasks, since language at least required for PaLM to perform well on various tasks modeling loss can be considered as a general measure of in four evaluation benchmarks (i.e., MMLU, BBH, TyDiQA the overall model capacity.”
- **end-to-end** — “The output audio classification research has moved from models based embedding is input to a Transformer, and the output of the clason hand-crafted features \[1, 2\] to end-to-end models that disification token is used for classification with a linear layer. rectly map audio spectrograms to corresponding labels \[3, 4, 5\].”
- **capture** — “To better capture long-range global context, a recent trend is to E\[CLS\] E\[1\] E\[2\] E\[3\] E\[4\] E\[5\] E\[6\] E\[7\] E\[8\] add a self-attention mechanism on top of the CNN, forming a CNN-attention hybrid model.”
- **self-attention** — “To better capture long-range global context, a recent trend is to E\[CLS\] E\[1\] E\[2\] E\[3\] E\[4\] E\[5\] E\[6\] E\[7\] E\[8\] add a self-attention mechanism on top of the CNN, forming a CNN-attention hybrid model.”
- **adopt** — “Existing LLMs adopt similar Trans- α β where a = α+β , b = α+β and G is a scaling coefficient that former architectures and pre-training objectives (e.g., lancan be computed by A, B , α and β .”
- **mapping** — “Through adversarial loss, MSVC-GAN learns the acoustic feature distribution of different singers, and establishes the forward and reverse mapping among the acoustic features of different singers, that is, the model can learn a unique function for all many-to-many mappings.”
- **long-range** — “To better capture long-range global context, a recent trend is to E\[CLS\] E\[1\] E\[2\] E\[3\] E\[4\] E\[5\] E\[6\] E\[7\] E\[8\] add a self-attention mechanism on top of the CNN, forming a CNN-attention hybrid model.”
- **hybrid** — “To better capture long-range global context, a recent trend is to E\[CLS\] E\[1\] E\[2\] E\[3\] E\[4\] E\[5\] E\[6\] E\[7\] E\[8\] add a self-attention mechanism on top of the CNN, forming a CNN-attention hybrid model.”
- **reliance** — “According to the discussion in \[366\], honesty When human labelers annotate the output of LLMs, it is is a more objective criterion compared to helpfulness and helpful to specify detailed instructions and provide instant harmlessness, hence honesty alignment could potentially be guidance for human labelers, which can further regulate the developed with less reliance on human efforts. annotation of labelers. • Harmlessness.”
- **accuracy** — “We evaluate AST on various audio classifi- 5 6 7 8 cation benchmarks, where it achieves new state-of-the-art re- Patch Split with Overlap sults of 0.485 mAP on AudioSet, 95.6% accuracy on ESC-50, and 98.1% accuracy on Speech Commands V2.”
- **building block** — “"as the main building block for end-to-end"”
- **purely** — “In this paper, we answer the question by introducing the Audio Spectrogram Transformer (AST), 1 2 3 4 the first convolution-free, purely attention-based model for au- Input Spectrogram dio classification.”

## Abstract（自动提取）

> TITLE: AST: Audio Spectrogram Transformer ABSTRACT: In the past decade, convolutional neural networks (CNNs) have been widely adopted as the main building block for end-to-end audio classification models, which aim to learn a direct mapping from audio spectrograms to corresponding labels. To better capture long-range global context, a recent trend is to add a self-attention mechanism on top of the CNN, forming a CNN-attention hybrid model. However, it is unclear whether the reliance on a CNN is necessary, and if neural networks purely based on attention are sufficient to obtain good performance in audio classification. In this paper, we answer the question by introducing the Audio Spectrogram Transformer (AST), the first convolution-free, purely attention-based model for audio classification. We evaluate AST on various audio classification benchmarks, where it achieves new state-of-the-art results of 0.485 mAP on AudioSet, 95.6% accuracy on ESC-50, and 98.1% accuracy on Speech Commands V2.

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

PDF：`/home/user/llm-papers/03_音乐检索理解/PDF/09_AST_AudioSpectrogramTransformer.pdf`

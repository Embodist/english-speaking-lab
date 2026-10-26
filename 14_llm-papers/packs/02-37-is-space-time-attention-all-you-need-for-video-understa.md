---
type: paper-pack
paper_id: "02-37"
stage: 2
title: "Is Space-Time Attention All You Need for Video Understanding?"
pdf: "/home/user/llm-papers/02_多模态/PDF/37_TimeSformer.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-37 Is Space-Time Attention All You Need for Video Understanding?

**中文标题**：时空注意力是否足以胜任视频理解？（TimeSformer）

**一句话概括**：提出完全无卷积、仅用时空自注意力的 TimeSformer，"分离注意力"设计使其在动作识别基准上达 SOTA，且训练更快、测试效率更高。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| benchmark | /bˈɛntʃmɑːk/ | 基准（数据集）；公认的评测任务 | S |
| self-attention | /sˈɛlfɐtˈɛnʃən/ | 自注意力；序列内元素相互关注的机制 | A |
| spatiotemporal | /spˈatɪˌəʊtmpəɹəl/ | 时空的；同时涵盖空间与时间的特征 | A |
| patch | /pˈatʃ/ | 图像块；从视频帧切分出的局部块 | A |
| efficiency | /ɪfˈɪʃənsi/ | 效率；单位算力下的处理能力 | A |
| convolution-free | /kɒnvəlˈuːʃənfɹˈiː/ | 无卷积的；不依赖卷积网络结构 | B |
| scheme | /skˈiːm/ | 方案；不同的注意力组织形式 | B |
| divided attention | /dɪvˈaɪdɪd ɐtˈɛnʃən/ | 分离注意力；时间与空间注意力分开应用 | B |
| dramatically | /dɹəmˈatɪkli/ | 大幅地；测试效率显著提高 | B |
| clip | /klˈɪp/ | 视频片段；模型处理的视频长度 | B |
| radically | /ɹˈadɪkli/ | 根本地；设计思路全新的 | B |

### 原句（保留完整句子）

- **benchmark** — “A recent study \[69\] found that a model size of 62B is better performance on downstream tasks, since language at least required for PaLM to perform well on various tasks modeling loss can be considered as a general measure of in four evaluation benchmarks (i.e., MMLU, BBH, TyDiQA the overall model capacity.”
- **self-attention** — “Jakob proposed replacing RNNs with self-attention and started the effort to evaluate this idea.”
- **spatiotemporal** — “Building upon these principles, recent implementations such as V-JEPA \[14\] and V-JEPA2 \[8\] have demonstrated the practical viability of video-based self-supervised learning, showing how JEPA architectures can learn rich spatiotemporal representations from unlabeled video data for downstream vision tasks.”
- **patch** — “During generation, the image is first split 823\] (exemplified by RecAgent \[822\]), showing great pointo patches, and then transformed into patch embeddings tential to simulate user real behaviors in recommender by the image encoder and the connection module, to derive systems \[822, 824, 825\].”
- **efficiency** — “Recent work has achieved significant improvements in computational efficiency through factorization tricks \[21\] and conditional computation \[32\], while also improving model performance in case of the latter.”
- **convolution-free** — “In this paper, we answer the question by introducing the Audio Spectrogram Transformer (AST), 1 2 3 4 the first convolution-free, purely attention-based model for au- Input Spectrogram dio classification.”
- **scheme** — “LAION-2B \[87\] 2.3B Mar-2022 LAION-COCO \[88\] 600M Sep-2022 COYO-700M \[90\] 747M Aug-2022 the training scheme is closely related to the data quality.”
- **divided attention** — “"where temporal attention and spatial attention are separately applied"”
- **dramatically** — “However, decreasing group size M also dramatically increase the number of overall parameters.”
- **clip** — “However, more detailed decay and gradient clipping have been widely utilized, investigation on encoder-decoder models is still lacking, and where existing studies \[55, 78, 90, 93, 113\] commonly set more efforts are needed to investigate the performance of the threshold of gradient clipping to 1.0 and weight decay encoder-decoder models at a large scale. rate to 0.1.”
- **radically** — “"Despite the radically new design, TimeSformer achieves state-of-the-art"”

## 摘要提示（PDF 文本不可提取）

> TITLE: Is Space-Time Attention All You Need for Video Understanding? ABSTRACT: We present a convolution-free approach to video classification built exclusively on self-attention over space and time. Our method, named "TimeSformer," adapts the standard Transformer architecture to video by enabling spatiotemporal feature learning directly from a sequence of frame-level patches. Our experimental study compares different self-attention schemes and suggests that "divided attention," where temporal attention and spatial attention are separately applied within each block, leads to the best video classification accuracy among the design choices considered. Despite the radically new design, TimeSformer achieves state-of-the-art results on several action recognition benchmarks, including the best reported accuracy on Kinetics-400 and Kinetics-600. Finally, compared to 3D convolutional networks, our model is faster to train, it can achieve dramatically higher test efficiency (at a small drop in accuracy), and it can also be applied to much longer video clips (over one minute long). Code and models are available at: https://github.com/facebookresearch/TimeSformer.

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
- [[14_llm-papers/stage-02-multimodal|阶段 2]]

PDF：`/home/user/llm-papers/02_多模态/PDF/37_TimeSformer.pdf`

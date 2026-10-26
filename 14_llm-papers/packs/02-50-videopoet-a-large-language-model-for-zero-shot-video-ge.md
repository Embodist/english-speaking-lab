---
type: paper-pack
paper_id: "02-50"
stage: 2
title: "VideoPoet: A Large Language Model for Zero-Shot Video Generation"
pdf: "/home/user/llm-papers/02_多模态/PDF/50_VideoPoet.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-50 VideoPoet: A Large Language Model for Zero-Shot Video Generation

**中文标题**：VideoPoet：用于零样本视频生成的大语言模型

**一句话概括**：采用仅解码器 Transformer 架构、按 LLM 两阶段流程训练，统一处理图像、视频、文本与音频，实现零样本高质量视频（含运动）生成。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| zero-shot | /zˈiəɹəʊʃˈɒt/ | 零样本的；无需任务数据即可生成 | S |
| autoregressive | /ˌɔːtəʊɹɪɡɹˈɛsɪv/ | 自回归的；逐 token 预测的框架 | S |
| synthesize | /sˈɪnθəsˌaɪz/ | 合成；生成视频内容 | S |
| adaptation | /ˌadaptˈeɪʃən/ | 适配；针对具体任务调整模型 | S |
| high-fidelity | /hˈaɪfɪdˈɛlɪti/ | 高保真的；运动细节高度真实 | S |
| pretraining | /pɹɪtɹˈeɪnɪŋ/ | 预训练；训练的第一阶段 | A |
| objective | /ɒbdʒˈɛktɪv/ | 目标（函数）；训练要优化的损失 | A |
| protocol | /pɹˈəʊtəkˌɒl/ | 流程/协议；标准训练步骤 | A |
| empirical | /ɛmpˈɪɹɪkəl/ | 实证的；基于实验结果的 | A |
| conditioning signals | /kəndˈɪʃənɪŋ sˈɪɡnəlz/ | 条件信号；控制生成内容的输入（如文本、图像） | B |
| decoder-only | /dɪkˈəʊdəɹˈəʊnli/ | 仅解码器的；没有编码器的 Transformer 结构 | B |

### 原句（保留完整句子）

- **zero-shot** — “In the neural networks to a significant size can lead to a huge the GPT-3’s paper, it formally introduced the concept of increase in model capacity. in-context learning (ICL)17 , which utilizes LLMs in a fewshot or zero-shot way.”
- **autoregressive** — “These models are mainly trained randomness and diversity during generation: to recover the replaced spans in an autoregressive way. xi ∼ P (x|x<i ).”
- **synthesize** — “Each prompt the LLM \[55\] to synthesize additional instructions answer is annotated with a score calculated based on its based on randomly selected 8 instructions as reference. votes and a label denoting whether it is selected.”
- **adaptation** — “In particular, we focus on four major aspects of LLMs, namely pre-training, adaptation tuning, utilization, and capacity evaluation.”
- **high-fidelity** — “Therefore, Engel et al. \[86\] proposed GANSynth, which uses GAN to generate high-fidelity and locally-coherent audio by modeling log-magnitudes and instantaneous frequency with sufficient frequency resolution in the spectrum domain.”
- **pretraining** — “Recently, pre-trained language models (PLMs) have been proposed by pretraining Transformer models over large-scale corpora, showing strong capabilities in solving various natural language processing (NLP) tasks.”
- **objective** — “Existing LLMs adopt similar Trans- α β where a = α+β , b = α+β and G is a scaling coefficient that former architectures and pre-training objectives (e.g., lancan be computed by A, B , α and β .”
- **protocol** — “Subsequently, the planning component communication protocols have been proposed, including utilizes the processed information from short-term memory free-form dialogue \[966\], structured document \[967\], and to generate the next plan.”
- **empirical** — “Empirical evaluation of gated recurrent neural networks on sequence modeling.”
- **conditioning signals** — “"from a large variety of conditioning signals"”
- **decoder-only** — “In addition, their as the model name, standing for Generative Pre-Training. capacities are also limited to the pre-training data, e.g., the GPT-1 was developed based on a generative, decoder-only inability to capture up-to-date information.”

## 摘要提示（PDF 文本不可提取）

> TITLE: VideoPoet: A Large Language Model for Zero-Shot Video Generation ABSTRACT: We present VideoPoet, a language model capable of synthesizing high-quality video, with matching audio, from a large variety of conditioning signals. VideoPoet employs a decoder-only transformer architecture that processes multimodal inputs -- including images, videos, text, and audio. The training protocol follows that of Large Language Models (LLMs), consisting of two stages: pretraining and task-specific adaptation. During pretraining, VideoPoet incorporates a mixture of multimodal generative objectives within an autoregressive Transformer framework. The pretrained LLM serves as a foundation that can be adapted for a range of video generation tasks. We present empirical results demonstrating the model's state-of-the-art capabilities in zero-shot video generation, specifically highlighting VideoPoet's ability to generate high-fidelity motions. Project page: http://sites.research.google/videopoet/

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

PDF：`/home/user/llm-papers/02_多模态/PDF/50_VideoPoet.pdf`

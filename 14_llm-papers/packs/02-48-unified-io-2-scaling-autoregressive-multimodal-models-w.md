---
type: paper-pack
paper_id: "02-48"
stage: 2
title: "Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action"
pdf: "/home/user/llm-papers/02_多模态/PDF/48_UnifiedIO2.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-48 Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action

**中文标题**：Unified-IO 2：用视觉、语言、音频与动作扩展自回归多模态模型

**一句话概括**：首个能理解并生成图像、文本、音频与动作的自回归多模态模型，把各模态统一词元化到共享语义空间，用单一模型在 35+ 基准上取得 SOTA。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| benchmark | /bˈɛntʃmɑːk/ | 基准测试；权威评测 | S |
| autoregressive | /ˌɔːtəʊɹɪɡɹˈɛsɪv/ | 自回归的；逐个预测下一词元的生成方式 | S |
| corpus | /kˈɔːpəs/ | 语料库；大规模训练数据集合 | S |
| augmentation | /ˌɔːɡmɛntˈeɪʃən/ | 数据增强；对样本做变换扩充 | A |
| stabilize | /stˈeɪbɪlˌaɪz/ | 稳定；防止训练发散 | A |
| ensemble | /ɒnsˈɒmbəl/ | 集成；多个数据集构成的组合 | A |
| tokenize | /tˈəʊkənˌaɪz/ | 词元化；把各模态切成统一单元 | B |
| shared semantic space | /ʃˈeəd səmˈantɪk spˈeɪs/ | 共享语义空间；各模态共同的特征表示空间 | B |
| encoder-decoder | /ɛŋkˈəʊdədɪkˈəʊdə/ | 编码器-解码器；编码输入再解码输出的结构 | B |
| mixture of denoisers | /mˈɪkstʃə ˈɒv dɪnˈɔɪsəz/ | 去噪器混合；组合多种去噪目标的训练目标 | B |
| expansive | /ɛkspˈansɪv/ | 广泛的；涵盖大量技能 | B |
| robotic manipulation | /ɹəʊbˈɒtɪk mənˌɪpjʊlˈeɪʃən/ | 机器人操作；控制机械臂等动作任务 | B |

### 原句（保留完整句子）

- **benchmark** — “A recent study \[69\] found that a model size of 62B is better performance on downstream tasks, since language at least required for PaLM to perform well on various tasks modeling loss can be considered as a general measure of in four evaluation benchmarks (i.e., MMLU, BBH, TyDiQA the overall model capacity.”
- **autoregressive** — “These models are mainly trained randomness and diversity during generation: to recover the replaced spans in an autoregressive way. xi ∼ P (x|x<i ).”
- **corpus** — “We also trained it in a semi-supervised setting, using the larger high-confidence and BerkleyParser corpora from with approximately 17M sentences \[37\].”
- **augmentation** — “By fine-tuning with a mixture of Thus, it will be meaningful to study how scaling laws apply multi-task datasets formatted via natural language descripto a data-constrained regime \[61\], where data repetition or tions (called instruction tuning), LLMs are shown to perform augmentation might be useful to alleviate data scarcity. well on unseen tasks that are also described in the form • Task-level predictability.”
- **stabilize** — “To alleviate this issue, strategies (e.g., combining post-LN with pre-LN in GLMnormalization is a widely adopted strategy to stabilize the 130B \[93\]). training of neural networks.”
- **ensemble** — “Our model achieves 28.4 BLEU on the WMT 2014 Englishto-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU.”
- **tokenize** — “Tokenize the world into object-level knowledge to address long-tail events in autonomous driving, 2024. \[252\] Edward C Tolman.”
- **shared semantic space** — “"into a shared semantic space and then process them"”
- **encoder-decoder** — “Numerous efforts have since continued to push the boundaries of recurrent language models and encoder-decoder architectures \[38, 24, 15\].”
- **mixture of denoisers** — “"with a multimodal mixture of denoisers objective"”
- **expansive** — “It was pre-trained on an expansive dataset of 14.8 trillion highquality, diverse tokens, followed by supervised fine-tuning and reinforcement learning to enhance its abilities across various domains.”
- **robotic manipulation** — “"video and audio understanding, and robotic manipulation"”

## 摘要提示（PDF 文本不可提取）

> TITLE: Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action ABSTRACT: We present Unified-IO 2, the first autoregressive multimodal model that is capable of understanding and generating image, text, audio, and action. To unify different modalities, we tokenize inputs and outputs -- images, text, audio, action, bounding boxes, etc., into a shared semantic space and then process them with a single encoder-decoder transformer model. Since training with such diverse modalities is challenging, we propose various architectural improvements to stabilize model training. We train our model from scratch on a large multimodal pre-training corpus from diverse sources with a multimodal mixture of denoisers objective. To learn an expansive set of skills, such as following multimodal instructions, we construct and finetune on an ensemble of 120 datasets with prompts and augmentations. With a single unified model, Unified-IO 2 achieves state-of-the-art performance on the GRIT benchmark and strong results in more than 35 benchmarks, including image generation and understanding, natural language understanding, video and audio understanding, and robotic manipulation. We release all our models to the research community.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/48_UnifiedIO2.pdf`

---
type: paper-pack
paper_id: "02-33"
stage: 2
title: "Adding Conditional Control to Text-to-Image Diffusion Models"
pdf: "/home/user/llm-papers/02_多模态/PDF/33_ControlNet.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-33 Adding Conditional Control to Text-to-Image Diffusion Models

**中文标题**：为文本到图像扩散模型添加条件控制（ControlNet）

**一句话概括**：提出 ControlNet 架构，通过"零卷积"锁定预训练扩散模型，向其中注入边缘、深度、姿态等空间条件控制，且小数据集训练同样稳健。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| architecture | /ˈɑːkɪtˌɛktʃə/ | 架构；神经网络的整体结构设计 | S |
| conditioning | /kəndˈɪʃənɪŋ/ | 条件控制；给模型额外输入以约束生成 | A |
| progressively | /pɹəɡɹˈɛsɪvli/ | 渐进地；参数随训练逐步增长 | A |
| backbone | /bˈakbəʊn/ | 主干网络；承担特征提取的主体结构 | A |
| diverse | /daɪvˈɜːs/ | 多样的；类型丰富的条件控制 | A |
| facilitate | /fəsˈɪlɪtˌeɪt/ | 促进、推动；使更广泛应用成为可能 | A |
| pretrained | /pɹɪtɹˈeɪnd/ | 预训练的；已在海量数据上训练好的 | B |
| lock | /lˈɒk/ | 锁定；保持原模型参数不动 | B |
| zero convolutions | /zˈiəɹəʊ kɒnvəlˈuːʃənz/ | 零卷积；参数从零初始化的卷积层 | B |
| harmful | /hˈɑːmfəl/ | 有害的；可能破坏微调的噪声 | B |
| segmentation | /sˌɛɡməntˈeɪʃən/ | 分割；按语义划分图像区域的输出 | B |

### 原句（保留完整句子）

- **architecture** — “We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.”
- **conditioning** — “"jointly conditioning on both left and right context in all layers"”
- **progressively** — “It aims to ful LLMs, a more typical approach is to also incorporate diorganize different parts of pre-training data for LLMs in verse high-quality text like code, books, scientific papers, etc. a specific order, e.g., starting with easy/general examples If a LLM is specialized with a certain skill, the proportion of and progressively introducing more challenging/special- corresponding data source should be increased accordingly. ized ones.”
- **backbone** — “For the above three types of archiDue to the excellent parallelizability and capacity, the Trans- tectures, we can further extend them via the mixture-offormer architecture \[22\] has become the de facto backbone to experts (MoE) scaling, in which a subset of neural network develop various LLMs, making it possible to scale language weights for each input are sparsely activated, e.g., Switch models to hundreds or thousands of billions of parameters.”
- **diverse** — “Later in January 2020, GPT-2 was fine- problems, spanning a diverse range of difficult tasks, and tuned using the aforementioned RL algorithms \[79, 128\], showed that GPT-4 can achieve more superior performance which leveraged human preferences to improve the capac- than prior GPT models.”
- **facilitate** — “To facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension dmodel = 512.”
- **pretrained** — “As the RL training requires to large reward model (e.g., equal or greater than the original iterate the inference process of both the LLM and reward model size), since large reward models generally perform models, it would greatly increase the total memory and better in judging the quality of the LLM generated outputs. computation cost, especially for larger reward models and In LLaMa 2 \[99\], pretrained chat model checkpoints are LLMs.”
- **lock** — “Additionally, the model may cause economic harms to certain groups via its production of particular content or its deployment in particular contexts, as discussed in the Harmful content, Interactions with other systems, and Overreliance sections; The training data has a cutoff point, meaning its knowledge of the world is locked in a certain state.”
- **zero convolutions** — “"zero-initialized convolution layers) that progressively grow the parameters"”
- **harmful** — “Despite the capacities, LLMs plex tasks, making AI algorithms unprecedently powerful are also likely to produce toxic, fictitious, or harmful conand effective.”
- **segmentation** — “However, word- course: a pair is scored by dividing the co-occurrence count based tokenization can yield different segmentation results by the product of the occurrence counts of two tokens in the for the same input in some languages (e.g., Chinese word pair based on training corpus. segmentation), generate a huge word vocabulary containing many low-frequency words, and also suffer from the “out- • Unigram tokenization.”

## 摘要提示（PDF 文本不可提取）

> TITLE: Adding Conditional Control to Text-to-Image Diffusion Models ABSTRACT: We present ControlNet, a neural network architecture to add spatial conditioning controls to large, pretrained text-to-image diffusion models. ControlNet locks the production-ready large diffusion models, and reuses their deep and robust encoding layers pretrained with billions of images as a strong backbone to learn a diverse set of conditional controls. The neural architecture is connected with "zero convolutions" (zero-initialized convolution layers) that progressively grow the parameters from zero and ensure that no harmful noise could affect the finetuning. We test various conditioning controls, eg, edges, depth, segmentation, human pose, etc, with Stable Diffusion, using single or multiple conditions, with or without prompts. We show that the training of ControlNets is robust with small (&lt;50k) and large (&gt;1m) datasets. Extensive results show that ControlNet may facilitate wider applications to control image diffusion models.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/33_ControlNet.pdf`

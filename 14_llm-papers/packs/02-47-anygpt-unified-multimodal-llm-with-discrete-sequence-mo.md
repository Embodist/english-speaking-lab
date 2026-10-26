---
type: paper-pack
paper_id: "02-47"
stage: 2
title: "AnyGPT: Unified Multimodal LLM with Discrete Sequence Modeling"
pdf: "/home/user/llm-papers/02_多模态/PDF/47_AnyGPT.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-47 AnyGPT: Unified Multimodal LLM with Discrete Sequence Modeling

**中文标题**：AnyGPT：基于离散序列建模的统一多模态大语言模型

**一句话概括**：用离散表示统一语音、文本、图像、音乐等模态，不改动 LLM 架构，仅靠数据级预处理即可实现任意模态组合的输入输出对话。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| alignment | /ɐlˈaɪnmənt/ | 对齐；让多模态表示相互对应 | S |
| representation | /ɹˌɛpɹɪzˈɛntˈeɪʃən/ | 表示；数据在模型中的编码形式 | S |
| modality | /məʊdˈalɪti/ | 模态；信息呈现形式 | S |
| architecture | /ˈɑːkɪtˌɛktʃə/ | 架构；模型整体结构 | S |
| discrete | /dɪskɹˈiːt/ | 离散的；用有限符号序列表示连续信号 | S |
| paradigm | /pˈaɹədˌaɪm/ | 范式；训练方式 | S |
| synthesize | /sˈɪnθəsˌaɪz/ | 合成；用生成模型制造数据 | S |
| unified | /jˈuːnɪfˌaɪd/ | 统一的；用同一框架处理所有模态 | A |
| arbitrary | /ˈɑːbɪtɹəɹi/ | 任意的；不受限制的组合 | A |
| any-to-any | /ˌɛnitʊˈɛni/ | 任意到任意的；任意模态输入到任意模态输出 | B |
| seamless | /sˈiːmləs/ | 无缝的；平滑自然的接入 | B |
| akin to | /ɐkˈɪn tˈuː/ | 类似于；如同……一样 | B |

### 原句（保留完整句子）

- **alignment** — “Index Terms—Large Language Models; Emergent Abilities; Adaptation Tuning; Utilization; Alignment; Capacity Evaluation ✦ 1 I NTRODUCTION “The limits of my language mean the limits of my world.” extensive attention in the literature, which can be divided —Ludwig Wittgenstein into four major development stages: • Statistical language models (SLM).”
- **representation** — “Noam proposed scaled dot-product attention, multi-head attention and the parameter-free position representation and became the other person involved in nearly every detail.”
- **modality** — “As an- of non-textual modalities, especially the vision modality, other alternative approach, several studies \[819, 820\] adopt called multimodal large language models (MLLMs) \[800\]44 .”
- **architecture** — “We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.”
- **discrete** — “Based on the discrete tion tuning and alignment tuning to adapt LLMs according prompting methods \[412, 413\], it augments the input text to specific goals.”
- **paradigm** — “This study has inspired a large number of follow-up models for representation learning (beyond word sequence work, which sets the “pre-training and fine-tuning” learning modeling), having an important impact on the field of NLP. paradigm.”
- **synthesize** — “Each prompt the LLM \[55\] to synthesize additional instructions answer is annotated with a score calculated based on its based on randomly selected 8 instructions as reference. votes and a label denoting whether it is selected.”
- **unified** — “"for the unified processing of various modalities"”
- **arbitrary** — “In these models, the number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions, linearly for ConvS2S and logarithmically for ByteNet.”
- **any-to-any** — “Next-gpt: Any-to-any multimodal llm. arXiv \[144\] Wenhai Wang, Enze Xie, Xiang Li, Deng-Ping Fan, Kaitao preprint arXiv:2309.05519, 2023.”
- **seamless** — “HE) for RLHF training, which enables seamless switch be• JAX \[202\] is a Python library for high-performance tween training and inference modes, and leveraging various machine learning algorithms developed by Google, allow- optimizations from DeepSpeed Inference. ing users to easily perform computations on arrays with In addition to the above library resources, existing deep hardware acceleration (e.g., GPU or TPU).”
- **akin to** — “"akin to the incorporation of new languages"”

## 摘要提示（PDF 文本不可提取）

> TITLE: AnyGPT: Unified Multimodal LLM with Discrete Sequence Modeling ABSTRACT: We introduce AnyGPT, an any-to-any multimodal language model that utilizes discrete representations for the unified processing of various modalities, including speech, text, images, and music. AnyGPT can be trained stably without any alterations to the current large language model (LLM) architecture or training paradigms. Instead, it relies exclusively on data-level preprocessing, facilitating the seamless integration of new modalities into LLMs, akin to the incorporation of new languages. We build a multimodal text-centric dataset for multimodal alignment pre-training. Utilizing generative models, we synthesize the first large-scale any-to-any multimodal instruction dataset. It consists of 108k samples of multi-turn conversations that intricately interweave various modalities, thus equipping the model to handle arbitrary combinations of multimodal inputs and outputs. Experimental results demonstrate that AnyGPT is capable of facilitating any-to-any multimodal conversation while achieving performance comparable to specialized models across all modalities, proving that discrete representations can effectively and conveniently unify multiple modalities within a language model. Demos are shown in https://junzhan2000.github.io/AnyGPT.github.io/

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

PDF：`/home/user/llm-papers/02_多模态/PDF/47_AnyGPT.pdf`

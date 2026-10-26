---
type: paper-pack
paper_id: "02-49"
stage: 2
title: "Retrieval-Augmented Multimodal Language Modeling"
pdf: "/home/user/llm-papers/02_多模态/PDF/49_RACM3.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-49 Retrieval-Augmented Multimodal Language Modeling

**中文标题**：检索增强的多模态语言建模（RA-CM3）

**一句话概括**：让生成模型从外部记忆检索相关图文而非把知识全存进参数，训练算力不到 DALL-E 的 30%，却在图文生成任务上全面超越。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| outperform | /aʊtpəfˈɔːm/ | 超越；性能优于基线 | S |
| scalable | /skˈeɪləbəl/ | 可扩展的；随规模增大仍高效 | S |
| remarkable | /ɹɪmˈɑːkəbəl/ | 显著的；进展非常突出 | A |
| capture | /kˈaptʃə/ | 获取、捕捉；把知识学会 | A |
| store | /stˈɔː/ | 存储；把知识写进模型参数 | A |
| retrieval-augmented | /ɹɪtɹˈiːvəlɔːɡmˈɛntɪd/ | 检索增强的；生成前先检索相关信息 | A |
| retriever | /ɹɪtɹˈiːvə/ | 检索器；从外部库找出相关样本的模块 | A |
| compute | /kəmpjˈuːt/ | 算力；训练消耗的计算资源 | A |
| modular | /mˈɒdjʊlə/ | 模块化的；各部分可独立更换 | B |
| external memory | /ɛkstˈɜːnəl mˈɛməɹi/ | 外部记忆；模型之外的存储（如网页文档） | B |
| faithful | /fˈeɪθfəl/ | 忠实的；忠实还原真实知识的生成 | B |
| in-context learning | /ɪŋkˈɒntɛkst lˈɜːnɪŋ/ | 上下文学习；从示例中直接学习新任务 | B |

### 原句（保留完整句子）

- **outperform** — “While for small values of dk the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of dk \[3\].”
- **scalable** — “In this way, as the especially for sequence data, which can further decompose calculations of gradients are independently performed on the attention operation of the Transformer model. different GPUs, the data parallelism mechanism is highly scalable, enabling the way that increases the number of Mixed Precision Training.”
- **remarkable** — “Recently, the research on LLMs has been largely advanced by both academia and industry, and a remarkable progress is the launch of ChatGPT (a powerful AI chatbot developed based on LLMs), which has attracted widespread attention from society.”
- **capture** — “As an early at- ent architectures \[24, 25\] (e.g., GPT-2 \[26\] and BART \[24\]) or tempt, ELMo \[21\] was proposed to capture context-aware improved pre-training strategies \[27–29\].”
- **store** — “ChatGPT exhibited superior capacitraining on code data is a very useful practice to improve ties in communicating with humans: possessing a vast store the model capacity of GPT models, especially the reasoning of knowledge, skill at reasoning on mathematical problems, ability.”
- **retrieval-augmented** — “To achieve the above two goals, two improving LLMs, which are detailed in two aspects, namely typical training strategies are often employed for visual retrieval-augmented LLM and synergy-augmented LLM. instruction tuning, either only optimizing the connection module \[156\] or fine-tuning both the connector module Retrieval-Augmented LLM.”
- **retriever** — “In addition, EPR \[421\] proposes | {z } | {z } |{z} demonstrations input answer a two-stage retrieval approach that first recalls similar ex(11) amples with an unsupervised method (e.g., BM25) and then where the actual answer yk+1 is left as a blank to be ranks them using a dense retriever (trained with positive predicted by the LLM.”
- **compute** — “2 Background The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU \[16\], ByteNet \[18\] and ConvS2S \[9\], all of which use convolutional neural networks as basic building block, computing hidden representations in parallel for all input and output positions.”
- **modular** — “Glass, and modular pytorch library for high performance P.”
- **external memory** — “"from external memory (e.g., documents on the web)"”
- **faithful** — “Although text-based approaches refinement approaches in existing work. sound intuitive, they cannot guarantee faithful execution of the plan, which may lead to failure even when the plan is Reasoning.”
- **in-context learning** — “"multimodal in-context learning (e.g., image generation from demonstrations)"”

## 摘要提示（PDF 文本不可提取）

> TITLE: Retrieval-Augmented Multimodal Language Modeling ABSTRACT: Recent multimodal models such as DALL-E and CM3 have achieved remarkable progress in text-to-image and image-to-text generation. However, these models store all learned knowledge (e.g., the appearance of the Eiffel Tower) in the model parameters, requiring increasingly larger models and training data to capture more knowledge. To integrate knowledge in a more scalable and modular way, we propose a retrieval-augmented multimodal model, which enables a base multimodal model (generator) to refer to relevant text and images fetched by a retriever from external memory (e.g., documents on the web). Specifically, for the retriever, we use a pretrained CLIP, and for the generator, we train a CM3 Transformer on the LAION dataset. Our resulting model, named Retrieval-Augmented CM3 (RA-CM3), is the first multimodal model that can retrieve and generate both text and images. We show that RA-CM3 significantly outperforms baseline multimodal models such as DALL-E and CM3 on both image and caption generation tasks (12 FID and 17 CIDEr improvements on MS-COCO), while requiring much less compute for training (&lt;30% of DALL-E). Moreover, we show that RA-CM3 exhibits novel capabilities, such as faithful image generation and multimodal in-context learning (e.g., image generation from demonstrations).

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

PDF：`/home/user/llm-papers/02_多模态/PDF/49_RACM3.pdf`

---
type: paper-pack
paper_id: "02-44"
stage: 2
title: "Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs"
pdf: "/home/user/llm-papers/02_多模态/PDF/44_Cambrian1.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-44 Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs

**中文标题**：Cambrian-1：对多模态大语言模型的完全开源、以视觉为中心的探索

**一句话概括**：以视觉为中心系统评估 20 多种视觉编码器，提出空间视觉聚合器（SVA）与视觉中心基准 CV-Bench，并开源全套数据、代码与训练配方。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| benchmark | /bˈɛntʃmɑːk/ | 基准测试；评测模型的权威任务 | S |
| curation | /kjʊəɹˈeɪʃən/ | 整理、策划；挑选高质量训练数据 | S |
| interpret | /ɪntˈɜːpɹɪt/ | 解读；理解评测结果的含义 | A |
| grounding | /ɡɹˈaʊndɪŋ/ | 锚定；模型对真实世界视觉信息的准确对应 | A |
| sensory | /sˈɛnsəɹi/ | 感知的；来自视觉等感官的信息 | A |
| encoder | /ɛŋkˈəʊdə/ | 编码器；把图像转为特征向量的网络 | A |
| vision-centric | /vˈɪʒənsˈɛntɹɪk/ | 以视觉为中心的；优先设计视觉组件 | B |
| disconnected | /dɪskənˈɛktɪd/ | 脱节的；视觉组件研究与表征学习脱钩 | B |
| consolidate | /kənsˈɒlɪdˌeɪt/ | 整合；汇总多个任务的结果 | B |
| aggregator | /ˈaɡɹɪɡˌeɪtə/ | 聚合器；把多尺度视觉特征合并的模块 | B |
| integrate | /ˈɪntɪɡɹˌeɪt/ | 整合；把视觉特征接入语言模型 | B |
| cookbook | /kˈʊkbʊk/ | 手册/指南；可复现的完整方案集 | B |

### 原句（保留完整句子）

- **benchmark** — “A recent study \[69\] found that a model size of 62B is better performance on downstream tasks, since language at least required for PaLM to perform well on various tasks modeling loss can be considered as a general measure of in four evaluation benchmarks (i.e., MMLU, BBH, TyDiQA the overall model capacity.”
- **curation** — “It proves the are semantically aligned with given texts while maintaining importance of data curation for video diffusion models. consistency between different frames.”
- **interpret** — “Bowman, “GLUE: A multi-task benchmark long sequences with structured state spaces,” and analysis platform for natural language underin The Tenth International Conference on Learning standing,” in Proceedings of the Workshop: AnalyzRepresentations, ICLR 2022, Virtual Event, April 25-29, ing and Interpreting Neural Networks for NLP, Black2022.”
- **grounding** — “"implement the grounding and text-reading ability"”
- **sensory** — “4 Ding and Zhang et al. comprises a perception module that processes sensory data (i.e., an encoder), followed by a cognitive module (i.e., a predictor) that evaluates this information, effectively embodying the world model.”
- **encoder** — “Gomez∗ † Łukasz Kaiser∗ Google Research University of Toronto Google Brain llion@google.com aidan@cs.toronto.edu lukaszkaiser@google.com Illia Polosukhin∗ ‡ illia.polosukhin@gmail.com Abstract The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder.”
- **vision-centric** — “Hoi, “Instructblip: Towards general- open-ended decoder for vision-centric tasks,” arXiv:2305.11175, purpose vision-language models with instruction tuning,” 2023.”
- **disconnected** — “We heavily obscured disconnected component, ...).” These realso present an “oracle” result, in which the most relevant sults indicate that SAM has learned to segment valid masks of SAM’s 3 masks is selected by comparing them to the from a single point.”
- **consolidate** — “Based on such 92 assumptions, a series of works propose detecting hallucina- further expands the knowledge source to local databases, tions by assessing the uncertainty of model-generated con- devising an agent framework to retrieve, consolidate, and tent.”
- **aggregator** — “"we propose the Spatial Vision Aggregator (SVA)"”
- **integrate** — “In Figure 2, we describe the evolu- modal input by integrating the visual information.”
- **cookbook** — “We may also act (open a cookbook to read the recipe, open the fridge, check ingredients) to support the reasoning and to answer questions (“What dish can I make right now?”).”

## 摘要提示（PDF 文本不可提取）

> TITLE: Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs ABSTRACT: We introduce Cambrian-1, a family of multimodal LLMs (MLLMs) designed with a vision-centric approach. While stronger language models can enhance multimodal capabilities, the design choices for vision components are often insufficiently explored and disconnected from visual representation learning research. This gap hinders accurate sensory grounding in real-world scenarios. Our study uses LLMs and visual instruction tuning as an interface to evaluate various visual representations, offering new insights into different models and architectures -- self-supervised, strongly supervised, or combinations thereof -- based on experiments with over 20 vision encoders. We critically examine existing MLLM benchmarks, address the difficulties involved in consolidating and interpreting results from various tasks, and introduce a new vision-centric benchmark, CV-Bench. To further improve visual grounding, we propose the Spatial Vision Aggregator (SVA), a dynamic and spatially-aware connector that integrates high-resolution vision features with LLMs while reducing the number of tokens. Additionally, we discuss the curation of high-quality visual instruction-tuning data from publicly available sources, emphasizing the importance of data source balancing and distribution ratio. Collectively, Cambrian-1 not 

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

PDF：`/home/user/llm-papers/02_多模态/PDF/44_Cambrian1.pdf`

---
type: paper-pack
paper_id: "02-08"
stage: 2
title: "Flamingo: a Visual Language Model for Few-Shot Learning"
pdf: "/home/user/llm-papers/02_多模态/PDF/08_Flamingo.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-08 Flamingo: a Visual Language Model for Few-Shot Learning

**中文标题**：Flamingo：用于少样本学习的视觉语言模型

**一句话概括**：提出 Flamingo 系列视觉语言模型，通过架构创新桥接预训练的纯视觉/纯语言模型并处理任意交错的图文序列，实现上下文少样本学习。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| corpus | /kˈɔːpəs/ | 语料库（多模态网络数据集合） | S |
| interleaved | /ˌɪntəlˈiːvd/ | 交错排列的（文本与图像穿插混合） | S |
| prompt | /pɹˈɒmpt/ | 提示、引导（用问题/示例引导模型作答） | A |
| open challenge | /ˈəʊpən tʃˈalɪndʒ/ | 尚待解决的难题（尚未攻克的研究问题） | A |
| innovation | /ˌɪnəvˈeɪʃən/ | 创新（架构上的关键改进） | A |
| bridge | /bɹˈɪdʒ/ | 桥接、连接（把视觉模型与语言模型对接） | A |
| fine-tune | /fˈaɪntjˈuːn/ | 微调（在任务数据上继续训练） | A |
| endow | /ɛndˈaʊ/ | 赋予（让模型具备某种能力） | A |
| handful | /hˈandfəl/ | 少量、一小把（只有极少几个标注样本） | B |
| annotated | /ˈanətˌeɪtɪd/ | 已标注的（带人工标签的） | B |
| ingest | /ɪndʒˈɛst/ | 摄入、输入（把图像或视频作为输入） | B |
| spectrum | /spˈɛktɹəm/ | 谱系、范围（从开放式到封闭式任务的连续区间） | B |

### 原句（保留完整句子）

- **corpus** — “We also trained it in a semi-supervised setting, using the larger high-confidence and BerkleyParser corpora from with approximately 17M sentences \[37\].”
- **interleaved** — “We propose key architectural innovations to: (i) bridge powerful pretrained vision-only and language-only models, (ii) handle sequences of arbitrarily interleaved visual and textual data, and (iii) seamlessly ingest images or videos as inputs.”
- **prompt** — “A single large LM can achieve strong performance on many tasks using only its text interface: a few examples of a task are provided to the model as a prompt, along with a query input, and the model generates a continuation to produce a predicted output for that query.”
- **open challenge** — “"an open challenge for multimodal machine learning"”
- **innovation** — “This wave of how to efficiently find the effective prompts for LLMs on technical innovation would lead to an ecosystem of LLMspecific tasks.”
- **bridge** — “We propose key architectural innovations to: (i) bridge powerful pretrained vision-only and language-only models, (ii) handle sequences of arbitrarily interleaved visual and textual data, and (iii) seamlessly ingest images or videos as inputs.”
- **fine-tune** — “We fine-tune Flamingo on all nine tasks where Flamingo does not achieve SotA with few-shot learning.”
- **endow** — “Thanks to their flexibility, Flamingo models can be trained on large-scale multimodal web corpora containing arbitrarily interleaved text and images, which is key to endow them with in-context few-shot learning capabilities.”
- **handful** — “Furthermore, Perez et al. \[80\] have shown that such validation procedures are generally not robust with access to only a handful of samples during validation.”
- **annotated** — “However, successful finetuning often requires many thousands of annotated data points.”
- **ingest** — “We propose key architectural innovations to: (i) bridge powerful pretrained vision-only and language-only models, (ii) handle sequences of arbitrarily interleaved visual and textual data, and (iii) seamlessly ingest images or videos as inputs.”
- **spectrum** — “For tasks lying anywhere on this spectrum, a single Flamingo model can achieve a new state of the art with few-shot learning, simply by prompting the model with task-specific examples.”

## Abstract（自动提取）

> TITLE: Flamingo: a Visual Language Model for Few-Shot Learning ABSTRACT: Building models that can be rapidly adapted to novel tasks using only a handful of annotated examples is an open challenge for multimodal machine learning research. We introduce Flamingo, a family of Visual Language Models (VLM) with this ability. We propose key architectural innovations to: (i) bridge powerful pretrained vision-only and language-only models, (ii) handle sequences of arbitrarily interleaved visual and textual data, and (iii) seamlessly ingest images or videos as inputs. Thanks to their flexibility, Flamingo models can be trained on large-scale multimodal web corpora containing arbitrarily interleaved text and images, which is key to endow them with in-context few-shot learning capabilities. We perform a thorough evaluation of our models, exploring and measuring their ability to rapidly adapt to a variety of image and video tasks. These include open-ended tasks such as visual question-answering, where the model is prompted with a question which it has to answer; captioning tasks, which evaluate the ability to describe a scene or an event; and close-ended tasks such as multiple-choice visual question-answering. For tasks lying anywhere on this spectrum, a single Flamingo model can achieve a new state of the art with few-shot learning, simply by prompting the model with task-specific examples

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

PDF：`/home/user/llm-papers/02_多模态/PDF/08_Flamingo.pdf`

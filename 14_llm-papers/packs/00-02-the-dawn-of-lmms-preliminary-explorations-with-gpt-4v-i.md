---
type: paper-pack
paper_id: "00-02"
stage: 0
title: "The Dawn of LMMs: Preliminary Explorations with GPT-4V(ision)"
pdf: "/home/user/llm-papers/00_总览综述/PDF/02_The_Dawn_of_LMMs.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 00-02 The Dawn of LMMs: Preliminary Explorations with GPT-4V(ision)

**中文标题**：多模态大模型之黎明：GPT-4V(ision) 初步探索

**一句话概括**：对 GPT-4V(ision) 进行系统的初步探索，通过精心设计的定性样本揭示其处理任意交错多模态输入的强大能力与通用性，并提出视觉指代提示等新的人机交互方式。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| curate | /kjˈʊəɹeɪt/ | 精心挑选、策划（curate a collection 系统地挑选并组织样本） | S |
| interleaved | /ˌɪntəlˈiːvd/ | 交错的、穿插的（文本与图像任意穿插组合的输入） | S |
| generic | /dʒənˈɛɹɪk/ | 通用的（generic intelligence 通用智能；本文强调能力具有通用性） | A |
| span | /spˈan/ | 涵盖、跨越（样本跨越多种领域与任务） | A |
| unprecedented | /ʌnpɹˈɛsɪdəntɪd/ | 前所未有的（GPT-4V 处理任意交错多模态输入的能力） | A |
| probe | /pɹˈəʊb/ | 探查、检验（用精心设计的测试样本检验能力质量） | A |
| generalist | /dʒˈɛnəɹəlˌɪst/ | 通才（multimodal generalist system 能处理多种任务的多模态通才系统） | A |
| dawn | /dˈɔːn/ | 黎明、开端（the dawn of LMMs 指多模态大模型时代刚刚开启） | B |
| preliminary | /pɹɪlˈɪmɪnəɹi/ | 初步的、预备的（preliminary explorations 探索性研究） | B |
| extend | /ɛkstˈɛnd/ | 扩展（LMMs 在 LLM 基础上扩展出视觉等多感官能力） | B |
| multi-sensory | /mˈʌltisˈɛnsəɹi/ | 多感官的（能处理视觉、文本等多种感官信息） | B |
| visual referring prompting | /vˈɪʒuːəl ɹɪfˈɜːɹɪŋ pɹˈɒmptɪŋ/ | 视觉指代提示（通过在输入图像上画标记来指示模型关注的对象） | B |

### 原句（保留完整句子）

- **curate** — “For example, BLOOM \[78\] and PaLM \[56\] have use of these data resources, a large amount of data is curated multilingual data covering 46 and 122 languages, crawled from the web in previous work, such as Com- respectively, within their pre-training corpora.”
- **interleaved** — “"processing arbitrarily interleaved multimodal inputs and"”
- **generic** — “2016. context2vec: Learning generic context em- Fu Sun, Linyang Li, Xipeng Qiu, and Yang Liu. bedding with bidirectional LSTM.”
- **span** — “Later in January 2020, GPT-2 was fine- problems, spanning a diverse range of difficult tasks, and tuned using the aforementioned RL algorithms \[79, 128\], showed that GPT-4 can achieve more superior performance which leveraged human preferences to improve the capac- than prior GPT models.”
- **unprecedented** — “More importantly, world model technologies are fundamentally transforming game development and player experiences in unprecedented ways.”
- **probe** — “GPT-2 essentially used ICL for unsupervised task learning, Further, a contrastive approach \[127\] to training text and though it wasn’t called ICL at that time. code embedding was reported in January 2022, which was 10 shown to improve a series of related tasks (i.e., linear- InstructGPT in the data collection setup: human-generated probe classification, text search and code search).”
- **generalist** — “Su, “Mind2web: To- ICLR 2020, Addis Ababa, Ethiopia, April 26-30, 2020. wards a generalist agent for the web,” CoRR, vol.”
- **dawn** — “Keutzer, “The dawn of lmms: Preliminary explorations with gpt-4v M.”
- **preliminary** — “There are also some preliminary attempts to extend this It provides feedback about the execution result of the action to technique to solve multimodal \[525\] and multilingual the task planner, either in the form of natural language \[443\] tasks \[526\]. or from other multimodal signals \[439\].”
- **extend** — “We plan to extend the Transformer to problems involving input and output modalities other than text and to investigate local, restricted attention mechanisms to efficiently handle large inputs and outputs such as images, audio and video.”
- **multi-sensory** — “"extend large language models (LLMs) with multi-sensory skills"”
- **visual referring prompting** — “"such as visual referring prompting"”

## 摘要提示（PDF 文本不可提取）

> 对 GPT-4V(ision) 进行系统的初步探索，通过精心设计的定性样本揭示其处理任意交错多模态输入的强大能力与通用性，并提出视觉指代提示等新的人机交互方式。

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
- [[14_llm-papers/stage-00-surveys|阶段 0]]

PDF：`/home/user/llm-papers/00_总览综述/PDF/02_The_Dawn_of_LMMs.pdf`

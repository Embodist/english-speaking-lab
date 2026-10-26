---
type: paper-pack
paper_id: "00-05"
stage: 0
title: "Understanding World or Predicting Future? A Comprehensive Survey of World Models"
pdf: "/home/user/llm-papers/00_总览综述/PDF/05_Survey_World_Models.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 00-05 Understanding World or Predicting Future? A Comprehensive Survey of World Models

**中文标题**：《理解世界还是预测未来？世界模型综合综述》

**一句话概括**：系统综述世界模型研究，将其归纳为"构建内部表征理解世界"与"预测未来状态辅助决策"两大功能，并介绍在生成游戏、自动驾驶、机器人等领域的应用。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| representation | /ɹˌɛpɹɪzˈɛntˈeɪʃən/ | 表征（internal representations 模型内部对世界的编码） | S |
| systematic | /sˌɪstəmˈatɪk/ | 系统的（systematic categorization 系统分类，学术高频） | A |
| simulate | /sˈɪmjʊlˌeɪt/ | 模拟（simulate future states 模拟未来状态） | A |
| advancement | /ɐdvˈansmənt/ | 进步、进展（advancements in … 某领域的最新进展） | A |
| pursuit | /pəsˈuːt/ | 追求、探索（the pursuit of AGI 对通用人工智能的追求） | A |
| garner | /ɡˈɑːnə/ | 获得、赢得（garner attention 赢得关注，书面语高频） | B |
| categorization | /kˌatɪɡəɹaɪzˈeɪʃən/ | 分类（把研究对象归入不同类别） | B |
| emphasize | /ˈɛmfɐsˌaɪz/ | 强调（emphasizing two primary functions 强调两大主要功能） | B |
| domain | /dəmˈeɪn/ | 领域（key domains 关键领域，如自动驾驶、机器人） | B |
| autonomous driving | /ɔːtˈɒnəməs dɹˈaɪvɪŋ/ | 自动驾驶（autonomous 自主的 + driving 驾驶） | B |
| simulacra | /sˈɪmjʊlˌakɹə/ | 仿真体、模拟物（social simulacra 社会仿真环境/虚拟社会） | B |
| insight | /ˈɪnsaɪt/ | 洞见、深刻见解（provide insights into 对……给出见解） | B |

### 原句（保留完整句子）

- **representation** — “2 BACKGROUND AND CATEGORIZATION 2.1 History and Current Development In this section, we explore the evolving concepts of world models in the literature and categorize efforts to construct world models into two distinct branches: internal representation and future prediction.”
- **systematic** — “This review presents a systematic categorization of world models, emphasizing two primary functions: (1) constructing internal representations to understand the mechanisms of the world, and (2) predicting future states to simulate and guide decision-making.”
- **simulate** — “This review presents a systematic categorization of world models, emphasizing two primary functions: (1) constructing internal representations to understand the mechanisms of the world, and (2) predicting future states to simulate and guide decision-making.”
- **advancement** — “WHAM (World and Human Action Model) further exemplifies this advancement by generating consistent and diverse gameplay sequences while persisting user modifications—capabilities identified as critical for supporting creative practices in game development \[125\].”
- **pursuit** — “1 INTRODUCTION The scientific community has long aspired to develop a unified model that can replicate its fundamental dynamics of the world in pursuit of Artificial General Intelligence (AGI) \[140\].”
- **garner** — “Patch-division Recently, explorations of Mixture of Experts (MoE) archimethods cut a high-resolution image into patches and reuse tecture for LLMs have garnered rising attention \[65\], \[66\], the low-resolution encoder.”
- **categorization** — “This review presents a systematic categorization of world models, emphasizing two primary functions: (1) constructing internal representations to understand the mechanisms of the world, and (2) predicting future states to simulate and guide decision-making.”
- **emphasize** — “(2) Based on this categorization, we classify how various key application areas, including generative games, autonomous driving, robots, and social simulacra, emphasize different aspects of world models.”
- **domain** — “We then explore the application of world models in key domains, including generative games, autonomous driving, robotics, and social simulacra, with a focus on how each domain utilizes these aspects.”
- **autonomous driving** — “We then explore the application of world models in key domains, including generative games, autonomous driving, robotics, and social simulacra, with a focus on how each domain utilizes these aspects.”
- **simulacra** — “We then explore the application of world models in key domains, including generative games, autonomous driving, robotics, and social simulacra, with a focus on how each domain utilizes these aspects.”
- **insight** — “Craik’s insight was that human cognition fundamentally operates by creating internal representations that capture the essential structure and dynamics of the external world, enabling predictive reasoning and adaptive behavior.”

## Abstract（自动提取）

> TITLE: Understanding World or Predicting Future? A Comprehensive Survey of World Models ABSTRACT: The concept of world models has garnered significant attention due to advancements in multimodal large language models such as GPT-4 and video generation models such as Sora, which are central to the pursuit of artificial general intelligence. This survey offers a comprehensive review of the literature on world models. Generally, world models are regarded as tools for either understanding the present state of the world or predicting its future dynamics. This review presents a systematic categorization of world models, emphasizing two primary functions: (1) constructing internal representations to understand the mechanisms of the world, and (2) predicting future states to simulate and guide decision-making. Initially, we examine the current progress in these two categories. We then explore the application of world models in key domains, including generative games, autonomous driving, robotics, and social simulacra, with a focus on how each domain utilizes these aspects. Finally, we outline key challenges and provide insights into potential future research directions. We summarize the representative papers along with their code repositories in https://github.com/tsinghua-fib-lab/World-Model.

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

PDF：`/home/user/llm-papers/00_总览综述/PDF/05_Survey_World_Models.pdf`

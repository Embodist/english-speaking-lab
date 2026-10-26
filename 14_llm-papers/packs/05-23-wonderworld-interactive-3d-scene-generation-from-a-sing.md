---
type: paper-pack
paper_id: "05-23"
stage: 5
title: "WonderWorld: Interactive 3D Scene Generation from a Single Image"
pdf: "/home/user/llm-papers/05_世界模型/PDF/23_WonderWorld.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 05-23 WonderWorld: Interactive 3D Scene Generation from a Single Image

**中文标题**：WonderWorld：从单张图像交互式生成 3D 场景

**一句话概括**：提出交互式 3D 场景生成框架 WonderWorld，用快速分层高斯表面元（FLAGS）与引导式深度扩散，从单视图生成连贯互连的多样化 3D 场景，单块 A6000 GPU 上 10 秒内完成，支持实时交互探索。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| progressively | /pɹəɡɹˈɛsɪvli/ | 逐步地、渐进地 | A |
| surfels | /sˈɜːfəlz/ | 表面元；三维表面的一种点式表示 | B |
| geometry-based initialization | /dʒiˈɒmətɹibˈeɪst ɪnˌɪʃəlaɪzˈeɪʃən/ | 基于几何的初始化；用几何信息做初始估计 | B |
| coherent geometry | /kəʊhˈiəɹənt dʒiˈɒmətɹi/ | 连贯一致的几何结构 | B |
| depth diffusion | /dˈɛpθ dɪfjˈuːʒən/ | 深度扩散；生成深度图的扩散模型 | B |
| partial conditioning | /pˈɑːʃəl kəndˈɪʃənɪŋ/ | 部分条件约束；只对部分输入施加条件 | B |
| time-consuming | /tˈaɪmkənsjˈuːmɪŋ/ | 耗时的 | B |
| low latency | /lˈəʊ lˈeɪtənsi/ | 低延迟；响应很快 | B |
| scene representation | /sˈiːn ɹˌɛpɹɪzˈɛntˈeɪʃən/ | 场景表示；场景的数据结构 | B |
| depth maps | /dˈɛpθ mˈaps/ | 深度图；记录每个像素深度的图 | B |
| fall short of | /fˈɔːl ʃˈɔːt ˈɒv/ | 达不到、欠缺 | B |
| layout | /lˈeɪaʊt/ | 布局；物体在场景中的位置安排 | B |

### 原句（保留完整句子）

- **progressively** — “It aims to ful LLMs, a more typical approach is to also incorporate diorganize different parts of pre-training data for LLMs in verse high-quality text like code, books, scientific papers, etc. a specific order, e.g., starting with easy/general examples If a LLM is specialized with a certain skill, the proportion of and progressively introducing more challenging/special- corresponding data source should be increased accordingly. ized ones.”
- **surfels** — “the Fast Layered Gaussian Surfels (FLAGS)”
- **geometry-based initialization** — “leverages a geometry-based initialization”
- **coherent geometry** — “generating coherent geometry that allows all scenes to be connected”
- **depth diffusion** — “We introduce the guided depth diffusion”
- **partial conditioning** — “allows partial conditioning of depth estimation”
- **time-consuming** — “Another issue is the data contamination \[56, 740\], is both expensive and time-consuming, some work has i.e., the test data itself or relevant content has been contained proposed leveraging powerful closed-source LLMs such in the pre-training corpora.”
- **low latency** — “see the created scenes in low latency”
- **scene representation** — “as our scene representation”
- **depth maps** — “generating many views and depth maps”
- **fall short of** — “Existing scene generation approaches fall short of speed”
- **layout** — “These tasks often require the use of context-aware navigation algorithms that allow agents to adjust their trajectories and behaviors based on the layout and conditions of the environment.”

## 摘要提示（PDF 文本不可提取）

> TITLE: WonderWorld: Interactive 3D Scene Generation from a Single Image ABSTRACT: We present WonderWorld, a novel framework for interactive 3D scene generation that enables users to interactively specify scene contents and layout and see the created scenes in low latency. The major challenge lies in achieving fast generation of 3D scenes. Existing scene generation approaches fall short of speed as they often require (1) progressively generating many views and depth maps, and (2) time-consuming optimization of the scene geometry representations. We introduce the Fast Layered Gaussian Surfels (FLAGS) as our scene representation and an algorithm to generate it from a single view. Our approach does not need multiple views, and it leverages a geometry-based initialization that significantly reduces optimization time. Another challenge is generating coherent geometry that allows all scenes to be connected. We introduce the guided depth diffusion that allows partial conditioning of depth estimation. WonderWorld generates connected and diverse 3D scenes in less than 10 seconds on a single A6000 GPU, enabling real-time user interaction and exploration. We demonstrate the potential of WonderWorld for user-driven content creation and exploration in virtual environments. We release full code and software for reproducibility. Project website: https://kovenyu.com/WonderWorld/.

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
- [[14_llm-papers/stage-05-world-models|阶段 5]]

PDF：`/home/user/llm-papers/05_世界模型/PDF/23_WonderWorld.pdf`

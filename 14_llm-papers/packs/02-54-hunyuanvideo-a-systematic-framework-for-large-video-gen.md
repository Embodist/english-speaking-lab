---
type: paper-pack
paper_id: "02-54"
stage: 2
title: "HunyuanVideo: A Systematic Framework For Large Video Generative Models"
pdf: "/home/user/llm-papers/02_多模态/PDF/54_HunyuanVideo.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-54 HunyuanVideo: A Systematic Framework For Large Video Generative Models

**中文标题**：HunyuanVideo：面向大型视频生成模型的系统化框架

**一句话概括**：开源 130 亿参数视频基础模型，整合数据整理、架构设计、渐进式扩规模训练与高效基础设施，性能超越 Runway Gen-3 等领先闭源模型。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| outperform | /aʊtpəfˈɔːm/ | 超越；性能超过以往最优模型 | S |
| inference | /ˈɪnfəɹəns/ | 推理；用训练好的模型做预测 | S |
| comprehensive | /kˌɒmpɹɪhˈɛnsɪv/ | 全面的；覆盖完整环节 | S |
| curation | /kjʊəɹˈeɪʃən/ | 整理；数据筛选工作 | S |
| foster | /fˈɒstə/ | 促进；培育健康生态 | A |
| advancement | /ɐdvˈansmənt/ | 进展；技术的进步 | A |
| impact | /ˈɪmpakt/ | 影响；对生活产生作用 | A |
| closed-source | /klˈəʊzdsˈɔːs/ | 闭源的；不公开代码的 | A |
| innovative | /ˈɪnəvˌeɪtɪv/ | 创新的；有开创性的 | A |
| infrastructure | /ˈɪnfɹəstɹˌʌktʃə/ | 基础设施；支撑训练与推理的软硬件体系 | A |
| bridge the gap | /bɹˈɪdʒ ðˈə ɡˈap/ | 弥合差距；拉近两个群体间的距离 | A |
| performance gap | /pəfˈɔːməns ɡˈap/ | 性能差距；业界与公众可用模型间的差距 | B |

### 原句（保留完整句子）

- **outperform** — “While for small values of dk the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of dk \[3\].”
- **inference** — “Llion also experimented with novel model variants, was responsible for our initial codebase, and efficient inference and visualizations.”
- **comprehensive** — “Nc Compared with them, we focus on the techniques and L(N ) = , αN ∼ 0.076, Nc ∼ 8.8 × 1013 (1) N methods to develop and use LLMs and provide a relatively Dc αD comprehensive reference to important aspects of LLMs.”
- **curation** — “It proves the are semantically aligned with given texts while maintaining importance of data curation for video diffusion models. consistency between different frames.”
- **foster** — “The system should be resilient against adverular communication protocols to foster divergent thinking sarial inputs from various modalities such as text, image, and elicit valuable external feedback among agents.”
- **advancement** — “Compared to Qwen2, Given the huge cost of model pre-training, well-trained Qwen2.5 demonstrates a significant increase in knowledge model checkpoints are critical to the study and development retention, as well as notable advancements in coding and of LLMs for the research community.”
- **impact** — “The technical evolution of LLMs has been making an important impact on the entire AI community, which would revolutionize the way how we develop and use AI algorithms.”
- **closed-source** — “Furthermore, multimodal capaci18. https://openai.com/research/learning-from-human-preferences ties (see, hear, and speak) were also enhanced in this new 11 release, supported by GPT-4 Turbo with vision, DALL·E 3, closed-source LLMs, such as GPT-4, GPT-4o, and Claude Text-to-speech (TTS), and Listen to voice samples.”
- **innovative** — “Sun, “JEC-QA: A legal-domain question answer- books and movies: Towards story-like visual explaing dataset,” in The Thirty-Fourth AAAI Conference nations by watching movies and reading books,” in on Artificial Intelligence, AAAI 2020, The Thirty-Second 2015 IEEE International Conference on Computer Vision, Innovative Applications of Artificial Intelligence Confer- ICCV 2015, Santiago, Chile, December 7-13, 2015.”
- **infrastructure** — “More recently, fully pass the test case, but are less interested in selecting a GPT-4 \[46\] proposes to develop special infrastructure and better code with fewer errors between two failed ones.”
- **bridge the gap** — “"we aim to bridge the gap between closed-source and open-source communities"”
- **performance gap** — “"a notable performance gap between industry capabilities"”

## 摘要提示（PDF 文本不可提取）

> TITLE: HunyuanVideo: A Systematic Framework For Large Video Generative Models ABSTRACT: Recent advancements in video generation have significantly impacted daily life for both individuals and industries. However, the leading video generation models remain closed-source, resulting in a notable performance gap between industry capabilities and those available to the public. In this report, we introduce HunyuanVideo, an innovative open-source video foundation model that demonstrates performance in video generation comparable to, or even surpassing, that of leading closed-source models. HunyuanVideo encompasses a comprehensive framework that integrates several key elements, including data curation, advanced architectural design, progressive model scaling and training, and an efficient infrastructure tailored for large-scale model training and inference. As a result, we successfully trained a video generative model with over 13 billion parameters, making it the largest among all open-source models. We conducted extensive experiments and implemented a series of targeted designs to ensure high visual quality, motion dynamics, text-video alignment, and advanced filming techniques. According to evaluations by professionals, HunyuanVideo outperforms previous state-of-the-art models, including Runway Gen-3, Luma 1.6, and three top-performing Chinese video generative models. By releasing t

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

PDF：`/home/user/llm-papers/02_多模态/PDF/54_HunyuanVideo.pdf`

---
type: paper-pack
paper_id: "02-51"
stage: 2
title: "CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer"
pdf: "/home/user/llm-papers/02_多模态/PDF/51_CogVideoX.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-51 CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer

**中文标题**：CogVideoX：带专家 Transformer 的文本到视频扩散模型

**一句话概括**：基于扩散 Transformer 的 10 秒长视频生成模型，用 3D VAE 时空压缩、专家自适应 LayerNorm 深度融合文视频模态，配多分辨率帧打包与数据处理流水线。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| fidelity | /fɪdˈɛlɪti/ | 保真度；还原真实细节的程度 | S |
| temporal | /tˈɛmpəɹəl/ | 时间的；沿时间轴的信息维度 | A |
| metric | /mˈɛtɹɪk/ | 指标；量化评测的标准 | A |
| aligned | /ɐlˈaɪnd/ | 对齐的；视频内容与文本提示一致 | A |
| resolution | /ɹˌɛzəlˈuːʃən/ | 分辨率；画面的像素尺寸 | A |
| coherent | /kəʊhˈiəɹənt/ | 连贯的；前后一致不跳变 | A |
| compress | /kəmpɹˈɛs/ | 压缩；减少视频的数据量 | A |
| fusion | /fjˈuːʒən/ | 融合；两种模态信息的深度结合 | A |
| captioning | /kˈapʃənɪŋ/ | 描述生成；给视频写文字说明 | A |
| progressive | /pɹəɡɹˈɛsɪv/ | 渐进式的；分阶段逐步训练 | A |
| frame rate | /fɹˈeɪm ɹˈeɪt/ | 帧率；每秒播放的画面数 | B |
| narrative | /nˈaɹətˌɪv/ | 叙事；连贯的故事情节 | B |

### 原句（保留完整句子）

- **fidelity** — “Overall, the the world...the more accurate you are in predicting the next research of OpenAI on LLMs can be roughly divided into word, the higher the fidelity, the more resolution you get in the following stages13 . this process...”16 .”
- **temporal** — “SEED-Bench \[857\] further considers topic and style) and object (e.g., existence and color) or OCR- temporal understanding tasks and enlarges the evaluation related tasks, based on existing datasets or new datasets scale to 19K multiple-choice questions with the assistance of derived from existing images with annotations by humans LLMs.”
- **metric** — “All metrics are on the English-to-German translation development set, newstest2013.”
- **aligned** — “"these models are not aligned with their users"”
- **resolution** — “In the Transformer this is reduced to a constant number of operations, albeit at the cost of reduced effective resolution due to averaging attention-weighted positions, an effect we counteract with Multi-Head Attention as described in section 3.2.”
- **coherent** — “For a detailed introduction to the long-term dependency, and generate narrative and coherent commonly used corpus, one can refer to Section 3.2. texts.”
- **compress** — “Thus, unsupervised language to compress the world knowledge into the decoder-only modeling could be capable in solving various tasks, if it was Transformer model by language modeling, such that it can trained to have sufficient capacity in recovering the world recover (or memorize) the semantics of world knowledge text.”
- **fusion** — “Correspondingly, its cially designed methods, such as matrix partition and opera- maximum arithmetic intensity is 142.51 FLOP/byte47 . tor fusion, to keep intermediate results in the cache until the • Model efficiency metrics.”
- **captioning** — “"This dataset includes key tasks such as detailed captioning"”
- **progressive** — “Awadallah, “Orca: Progressive contamination: Accelerating large language modlearning from complex explanation traces of GPT-4,” els without impacting performance,” arXiv preprint CoRR, vol. abs/2306.02707, 2023. arXiv:2107.02027, 2021. \[341\] YuLan-Chat-Team, “Yulan-chat: An open-source \[354\] K.”
- **frame rate** — “"with a frame rate of 16 fps"”
- **narrative** — “For a detailed introduction to the long-term dependency, and generate narrative and coherent commonly used corpus, one can refer to Section 3.2. texts.”

## 摘要提示（PDF 文本不可提取）

> TITLE: CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer ABSTRACT: We present CogVideoX, a large-scale text-to-video generation model based on diffusion transformer, which can generate 10-second continuous videos aligned with text prompt, with a frame rate of 16 fps and resolution of 768 * 1360 pixels. Previous video generation models often had limited movement and short durations, and is difficult to generate videos with coherent narratives based on text. We propose several designs to address these issues. First, we propose a 3D Variational Autoencoder (VAE) to compress videos along both spatial and temporal dimensions, to improve both compression rate and video fidelity. Second, to improve the text-video alignment, we propose an expert transformer with the expert adaptive LayerNorm to facilitate the deep fusion between the two modalities. Third, by employing a progressive training and multi-resolution frame pack technique, CogVideoX is adept at producing coherent, long-duration, different shape videos characterized by significant motions. In addition, we develop an effective text-video data processing pipeline that includes various data preprocessing strategies and a video captioning method, greatly contributing to the generation quality and semantic alignment. Results show that CogVideoX demonstrates state-of-the-art performance across both multiple machin

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

PDF：`/home/user/llm-papers/02_多模态/PDF/51_CogVideoX.pdf`

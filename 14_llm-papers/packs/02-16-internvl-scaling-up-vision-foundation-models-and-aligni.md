---
type: paper-pack
paper_id: "02-16"
stage: 2
title: "InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks"
pdf: "/home/user/llm-papers/02_多模态/PDF/16_InternVL.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-16 InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks

**中文标题**：InternVL：扩大视觉基础模型规模并对其对齐以适配通用视觉-语言任务

**一句话概括**：将视觉基础模型扩到 60 亿参数并逐步与大语言模型对齐，在 32 个通用视觉-语言基准上达到 SOTA，可替代 ViT-22B。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| retrieval | /ɹɪtɹˈiːvəl/ | 检索（图文/视频文本检索任务） | S |
| progressively | /pɹəɡɹˈɛsɪvli/ | 逐步地（分阶段逐渐对齐） | A |
| align | /ɐlˈaɪn/ | 对齐（让视觉模型与语言模型协同） | A |
| generic | /dʒənˈɛɹɪk/ | 通用的（覆盖面广、不限于特定任务） | A |
| critical | /kɹˈɪtɪkəl/ | 关键的（视觉基础模型是 AGI 的关键要素） | A |
| perception | /pəsˈɛpʃən/ | 感知（对视觉信息的理解任务） | A |
| exponential | /ˌɛkspənˈɛnʃəl/ | 指数级的（LLM 规模飞速增长） | B |
| numerous | /njˈuːməɹəs/ | 大量的（带来众多新的可能性） | B |
| keep pace with | /kˈiːp pˈeɪs wˈɪð/ | 跟上……的步伐（视觉领域进展落后于 LLM） | B |
| pixel-level | /pˈɪksəllˈɛvəl/ | 像素级的（对每个像素做识别，如分割） | B |
| alternative | /ɔːltˈɜːnətˌɪv/ | 替代方案（可替代 ViT-22B 的选择） | B |
| contribute | /kəntɹˈɪbjuːt/ | 贡献（希望推动多模态大模型发展） | B |

### 原句（保留完整句子）

- **retrieval** — “Comparison results on various generic visual-linguistic tasks, including image classification, video classification, image-text retrieval, image captioning, and multi-modal dialogue.”
- **progressively** — “Comparison of hyperparameters in InternViT-6B. scale vision foundation model InternViT-6B, progressively The throughput (img/s) and GFLOPs are measured at 224×224 in- align it with an LLM-initialized language middleware QLput resolution, with a batch size of 1 or 128 on a single A100 GPU.”
- **align** — “(c) is our InternVL, which presents a workable way to align the large-scale vision foundation model (i.e., InternViT-6B) with the large language model and is versatile for both contrastive and generative tasks.”
- **generic** — “Comparison results on various generic visual-linguistic tasks, including image classification, video classification, image-text retrieval, image captioning, and multi-modal dialogue.”
- **critical** — “However, the progress in vision and their impressive capabilities in open-world language tasks, vision-language foundation models, which are also critical and their model scale and performance are still increasing elements of multi-modal AGI, has not kept pace with LLMs. at a fast pace.”
- **perception** — “It functions as a standalone vision encoder for models necessitates a vast amount of image-text data ob- perception tasks, or collaborates with the language middletained from the Internet.”
- **exponential** — “Introduction The exponential growth of large language models Large language models (LLMs) largely promote the devel(LLMs) has opened up numerous possibilities for multi- opment of artificial general intelligence (AGI) systems with modal AGI systems.”
- **numerous** — “Introduction The exponential growth of large language models Large language models (LLMs) largely promote the devel(LLMs) has opened up numerous possibilities for multi- opment of artificial general intelligence (AGI) systems with modal AGI systems.”
- **keep pace with** — “"has not kept pace with LLMs"”
- **pixel-level** — “Benefiting from the powerful representaInternViT-6B has better pixel-level perceptual capacity. tions learned in the first stage, we keep both InternViT-6B and QLLaMA frozen and only train the new parameters. ture If .”
- **alternative** — “Such aligncapabilities and can be a good alternative to the ViT-22B. ment contains several limitations: (1) Disparity in paramWe hope that our research could contribute to the develop- eter scales.”
- **contribute** — “Such aligncapabilities and can be a good alternative to the ViT-22B. ment contains several limitations: (1) Disparity in paramWe hope that our research could contribute to the develop- eter scales.”

## Abstract（自动提取）

> TITLE: InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks ABSTRACT: The exponential growth of large language models (LLMs) has opened up numerous possibilities for multimodal AGI systems. However, the progress in vision and vision-language foundation models, which are also critical elements of multi-modal AGI, has not kept pace with LLMs. In this work, we design a large-scale vision-language foundation model (InternVL), which scales up the vision foundation model to 6 billion parameters and progressively aligns it with the LLM, using web-scale image-text data from various sources. This model can be broadly applied to and achieve state-of-the-art performance on 32 generic visual-linguistic benchmarks including visual perception tasks such as image-level or pixel-level recognition, vision-language tasks such as zero-shot image/video classification, zero-shot image/video-text retrieval, and link with LLMs to create multi-modal dialogue systems. It has powerful visual capabilities and can be a good alternative to the ViT-22B. We hope that our research could contribute to the development of multi-modal large models. Code and models are available at https://github.com/OpenGVLab/InternVL.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/16_InternVL.pdf`

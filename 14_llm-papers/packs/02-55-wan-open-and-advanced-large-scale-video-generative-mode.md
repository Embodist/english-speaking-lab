---
type: paper-pack
paper_id: "02-55"
stage: 2
title: "Wan: Open and Advanced Large-Scale Video Generative Models"
pdf: "/home/user/llm-papers/02_多模态/PDF/55_Wan.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-55 Wan: Open and Advanced Large-Scale Video Generative Models

**中文标题**：Wan：开源且先进的大规模视频生成模型

**一句话概括**：开源 1.3B/14B 双规格视频基础模型系列，覆盖图像转视频、指令编辑等八类任务，14B 版在多基准上超越开源与商业模型，1.3B 版仅需 8.19GB 显存。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| outperform | /aʊtpəfˈɔːm/ | 超越；表现优于对比对象 | S |
| curation | /kjʊəɹˈeɪʃən/ | 整理；大规模数据筛选 | S |
| paradigm | /pˈaɹədˌaɪm/ | 范式；主流技术路线 | S |
| scalable | /skˈeɪləbəl/ | 可扩展的；能随数据规模增长的 | S |
| suite | /swˈiːt/ | 系列；一组配套模型 | A |
| innovation | /ˌɪnəvˈeɪʃən/ | 创新；新的技术方案 | A |
| scaling laws | /skˈeɪlɪŋ lˈɔːz/ | 缩放定律；性能随数据与规模增长的规律 | A |
| foster | /fˈɒstə/ | 促进；推动社区发展 | A |
| superiority | /suːpˌiəɹɪˈɒɹɪti/ | 优越性；明显更优的表现 | A |
| push the boundaries | /pˈʊʃ ðˈə bˈaʊndəɹiz/ | 突破边界；把能力上限再提高 | B |
| automated | /ˈɔːtəmˌeɪtɪd/ | 自动化的；机器自动完成的评测 | B |
| versatility | /vˌɜːsətˈɪlɪti/ | 通用性、多面性；适用多种任务的能力 | B |

### 原句（保留完整句子）

- **outperform** — “While for small values of dk the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of dk \[3\].”
- **curation** — “It proves the are semantically aligned with given texts while maintaining importance of data curation for video diffusion models. consistency between different frames.”
- **paradigm** — “This study has inspired a large number of follow-up models for representation learning (beyond word sequence work, which sets the “pre-training and fine-tuning” learning modeling), having an important impact on the field of NLP. paradigm.”
- **scalable** — “In this way, as the especially for sequence data, which can further decompose calculations of gradients are independently performed on the attention operation of the Transformer model. different GPUs, the data parallelism mechanism is highly scalable, enabling the way that increases the number of Mixed Precision Training.”
- **suite** — “Wang, evaluation suite for foundation models,” CoRR, vol.”
- **innovation** — “This wave of how to efficiently find the effective prompts for LLMs on technical innovation would lead to an ecosystem of LLMspecific tasks.”
- **scaling laws** — “"We study empirical scaling laws for language model performance"”
- **foster** — “The system should be resilient against adverular communication protocols to foster divergent thinking sarial inputs from various modalities such as text, image, and elicit valuable external feedback among agents.”
- **superiority** — “Related research has demonstrated its superiority in training Activation Functions.”
- **push the boundaries** — “"designed to push the boundaries of video generation"”
- **automated** — “A promising technique is red that guides the model to prefer certain outputs over others, teaming \[367\], which involves using manual or automated thus inducing outputs that are more reliable and safer. means to probe LLMs in an adversarial way to generate • Question-based approach.”
- **versatility** — “In robotic systems, innovative approaches further models that empowers generative models to produce visu- underscore the versatility and potential of world models. ally compelling signals of superior quality while adhering UniPi \[36\], for instance, reimagines the decision-making to stringent physical constraints.”

## 摘要提示（PDF 文本不可提取）

> TITLE: Wan: Open and Advanced Large-Scale Video Generative Models ABSTRACT: This report presents Wan, a comprehensive and open suite of video foundation models designed to push the boundaries of video generation. Built upon the mainstream diffusion transformer paradigm, Wan achieves significant advancements in generative capabilities through a series of innovations, including our novel VAE, scalable pre-training strategies, large-scale data curation, and automated evaluation metrics. These contributions collectively enhance the model's performance and versatility. Specifically, Wan is characterized by four key features: Leading Performance: The 14B model of Wan, trained on a vast dataset comprising billions of images and videos, demonstrates the scaling laws of video generation with respect to both data and model size. It consistently outperforms the existing open-source models as well as state-of-the-art commercial solutions across multiple internal and external benchmarks, demonstrating a clear and significant performance superiority. Comprehensiveness: Wan offers two capable models, i.e., 1.3B and 14B parameters, for efficiency and effectiveness respectively. It also covers multiple downstream applications, including image-to-video, instruction-guided video editing, and personal video generation, encompassing up to eight tasks. Consumer-Grade Efficiency: The 1.3B model demon

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

PDF：`/home/user/llm-papers/02_多模态/PDF/55_Wan.pdf`

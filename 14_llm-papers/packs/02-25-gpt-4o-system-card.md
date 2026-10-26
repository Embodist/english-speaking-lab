---
type: paper-pack
paper_id: "02-25"
stage: 2
title: "GPT-4o System Card"
pdf: "/home/user/llm-papers/02_多模态/PDF/25_GPT4o_SystemCard.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-25 GPT-4o System Card

**中文标题**：GPT-4o 系统卡

**一句话概括**：发布 GPT-4o 系统卡，介绍这一端到端全模态（omni）模型的输入输出组合、能力、局限，以及安全评估与第三方评估。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| autoregressive | /ˌɔːtəʊɹɪɡɹˈɛsɪv/ | 自回归的（逐 token 预测式生成） | S |
| end-to-end | /ˈɛndtʊˈɛnd/ | 端到端地（整个模型联合训练） | S |
| aligned | /ɐlˈaɪnd/ | 对齐的（模型行为符合人类意图与安全要求） | A |
| capability | /kˌeɪpəbˈɪlɪti/ | 能力（危险能力等） | A |
| omni | /ˈɒmnɪ/ | 全能的、全模态的（能处理所有模态的模型） | B |
| combination | /kˌɒmbɪnˈeɪʃən/ | 组合（文本、音频、图像、视频的任意组合） | B |
| process | /pɹˈəʊsɛs/ | 处理（所有输入由同一神经网络处理） | B |
| millisecond | /mˈɪlɪsˌɛkənd/ | 毫秒（响应时延的单位，232 毫秒） | B |
| commitment | /kəmˈɪtmənt/ | 承诺（安全建设方面的承诺） | B |
| voluntary | /vˈɒləntəɹi/ | 自愿的（向白宫作出的自愿承诺） | B |
| preparedness | /pɹɪpˈeədnəs/ | 预备性、准备（安全预备框架，评估潜在风险） | B |
| assessment | /ɐsˈɛsmənt/ | 评估（第三方对危险能力的评估） | B |

### 原句（保留完整句子）

- **autoregressive** — “These models are mainly trained randomness and diversity during generation: to recover the replaced spans in an autoregressive way. xi ∼ P (x|x<i ).”
- **end-to-end** — “It’s trained end-to-end across text, vision, and audio, meaning that all inputs and outputs are processed by the same neural network.”
- **aligned** — “In this System Card, we provide a detailed look at GPT-4o’s capabilities, limitations, and safety evaluations across multiple categories, with a focus on speech-to-speech (voice)1 while also evaluating text and image capabilities, and the measures we’ve implemented to ensure the model is safe and aligned.”
- **capability** — “This allowed us to reuse existing datasets and tooling around measuring model capability, safety behavior, and monitoring of model outputs, greatly expanding our set of usable evaluations.”
- **omni** — “5 Societal Impacts Omni models could have broad societal impacts.”
- **combination** — “We use a combination of methods, spanning all stages of development across pre-training, post-training, product development, and policy.”
- **process** — “Since we expect 4 that such inputs are also unlikely to be provided by the user over Advanced Voice Mode, we either avoid evaluating the speech-to-speech model on such tasks, or alternatively pre-process examples with such inputs.”
- **millisecond** — “For short damage less than tens of milliseconds, the goal of audio inpainting algorithm is to accurately recover the lost information \[302\]; for long corruptions, this goal becomes unrealistic, so audio inpainting algorithms attempt to reduce the damage by preventing audible artifacts and introducing new coherent information.”
- **commitment** — “In line with our commitment to building AI safely and consistent with our voluntary commitments to the White House\[3\], we are sharing the GPT-4o System Card, which includes our Preparedness Framework\[4\] evaluations.”
- **voluntary** — “In line with our commitment to building AI safely and consistent with our voluntary commitments to the White House\[3\], we are sharing the GPT-4o System Card, which includes our Preparedness Framework\[4\] evaluations.”
- **preparedness** — “In line with our commitment to building AI safely and consistent with our voluntary commitments to the White House\[3\], we are sharing the GPT-4o System Card, which includes our Preparedness Framework\[4\] evaluations.”
- **assessment** — “3 Risk identification, assessment and mitigation Deployment preparation was carried out via identifying potential risks of speech to speech models, exploratory discovery of additional novel risks through expert red teaming, turning the identified risks into structured measurements and building mitigations for them.”

## Abstract（自动提取）

> TITLE: GPT-4o System Card ABSTRACT: GPT-4o is an autoregressive omni model that accepts as input any combination of text, audio, image, and video, and generates any combination of text, audio, and image outputs. It's trained end-to-end across text, vision, and audio, meaning all inputs and outputs are processed by the same neural network. GPT-4o can respond to audio inputs in as little as 232 milliseconds, with an average of 320 milliseconds, which is similar to human response time in conversation. It matches GPT-4 Turbo performance on text in English and code, with significant improvement on text in non-English languages, while also being much faster and 50\% cheaper in the API. GPT-4o is especially better at vision and audio understanding compared to existing models. In line with our commitment to building AI safely and consistent with our voluntary commitments to the White House, we are sharing the GPT-4o System Card, which includes our Preparedness Framework evaluations. In this System Card, we provide a detailed look at GPT-4o's capabilities, limitations, and safety evaluations across multiple categories, focusing on speech-to-speech while also evaluating text and image capabilities, and measures we've implemented to ensure the model is safe and aligned. We also include third-party assessments on dangerous capabilities, as well as discussion of potential societal impacts o

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

PDF：`/home/user/llm-papers/02_多模态/PDF/25_GPT4o_SystemCard.pdf`

---
type: paper-pack
paper_id: "02-52"
stage: 2
title: "Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets"
pdf: "/home/user/llm-papers/02_多模态/PDF/52_StableVideoDiffusion.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-52 Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets

**中文标题**：Stable Video Diffusion：把潜视频扩散模型扩展到大规模数据集

**一句话概括**：系统梳理文生视频训练三阶段并给出数据整理流程，训练出可与闭源模型竞争的视频 LDM，其基座还是图像到视频、多视角生成的有力基础。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| downstream | /dˈaʊnstɹiːm/ | 下游的；后续应用任务 | S |
| competitive | /kəmpˈɛtɪtˌɪv/ | 有竞争力的；不输于闭源方案 | S |
| latent | /lˈeɪtənt/ | 潜（空间）的；在压缩的低维空间中扩散 | S |
| curate | /kjˈʊəɹeɪt/ | 整理；筛选高质量训练数据 | S |
| unified | /jˈuːnɪfˌaɪd/ | 统一的；大家公认一致的方案 | A |
| systematic | /sˌɪstəmˈatɪk/ | 系统性的；成体系的数据整理 | A |
| finetune | /fˈaɪntjuːn/ | 微调；在小数据上继续训练 | A |
| identify | /aɪdˈɛntɪfˌaɪ/ | 识别、确定；找出关键阶段 | A |
| feedforward | /fiːdfˈɔːwəd/ | 前馈的；一次前向计算直接出结果 | A |
| insert | /ˈɪnsɜːt/ | 插入；把时间层加进图像模型 | B |
| necessity | /nəsˈɛsɪti/ | 必要性；不可或缺的条件 | B |
| filtering | /fˈɪltəɹɪŋ/ | 过滤；剔除低质量数据 | B |

### 原句（保留完整句子）

- **downstream** — “In this paradigm, it word representations by first pre-training a bidirectional often requires fine-tuning the PLM for adapting to different LSTM (biLSTM) network (instead of learning fixed word downstream tasks. representations) and then fine-tuning the biLSTM network according to specific downstream tasks.”
- **competitive** — “3 Model Architecture Most competitive neural sequence transduction models have an encoder-decoder structure \[5, 2, 35\].”
- **latent** — “Self-training PCFG grammars with latent annotations across languages.”
- **curate** — “For example, BLOOM \[78\] and PaLM \[56\] have use of these data resources, a large amount of data is curated multilingual data covering 46 and 122 languages, crawled from the web in previous work, such as Com- respectively, within their pre-training corpora.”
- **unified** — “"for the unified processing of various modalities"”
- **systematic** — “Due to the huge deIn the existing literature, PLMs have been widely dis- mand of computation resources, it is very costly to carry cussed and surveyed \[36–39\], while LLMs are seldom re- out repetitive, ablating studies for investigating the effect viewed in a systematic way.”
- **finetune** — “Notably, ShareGPT4V \[83\] strikes a suggests spatial relationships. balance by first training a captioner with GPT-4V-generated IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE 6 (A) Pretrain–finetune (BERT, T5) like the image caption task \[100\].”
- **identify** — “The in-context learning (ICL) ability status of LLMs, e.g., identifying abnormal performance at an is formally introduced by GPT-3 \[55\]: assuming that the early time.”
- **feedforward** — “It employs time-mixing modules, i.e., can bidirectionally encode the prefix sequence and autore- RNN with gating, and channel-mixing modules that are gressively predict the output tokens one by one, where the special feedforward neural networks \[273\].”
- **insert** — “In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack.”
- **necessity** — “This kind of approaches the necessity of prompt engineering for LLMs to perform aims to optimize the prompt search process by maximizing well on complex tasks, since these tasks typically have the output likelihood via gradient update \[413, 458–461\].”
- **filtering** — “"including captioning and filtering strategies"”

## 摘要提示（PDF 文本不可提取）

> TITLE: Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets ABSTRACT: We present Stable Video Diffusion - a latent video diffusion model for high-resolution, state-of-the-art text-to-video and image-to-video generation. Recently, latent diffusion models trained for 2D image synthesis have been turned into generative video models by inserting temporal layers and finetuning them on small, high-quality video datasets. However, training methods in the literature vary widely, and the field has yet to agree on a unified strategy for curating video data. In this paper, we identify and evaluate three different stages for successful training of video LDMs: text-to-image pretraining, video pretraining, and high-quality video finetuning. Furthermore, we demonstrate the necessity of a well-curated pretraining dataset for generating high-quality videos and present a systematic curation process to train a strong base model, including captioning and filtering strategies. We then explore the impact of finetuning our base model on high-quality data and train a text-to-video model that is competitive with closed-source video generation. We also show that our base model provides a powerful motion representation for downstream tasks such as image-to-video generation and adaptability to camera motion-specific LoRA modules. Finally, we demonstrate that our model provides a

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

PDF：`/home/user/llm-papers/02_多模态/PDF/52_StableVideoDiffusion.pdf`

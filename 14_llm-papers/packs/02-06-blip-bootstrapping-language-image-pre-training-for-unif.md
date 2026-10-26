---
type: paper-pack
paper_id: "02-06"
stage: 2
title: "BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation"
pdf: "/home/user/llm-papers/02_多模态/PDF/06_BLIP.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-06 BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation

**中文标题**：BLIP：自举式语言-图像预训练，统一视觉-语言理解与生成

**一句话概括**：提出 BLIP 框架，用"说明生成器+过滤器"自举式利用含噪声的网络图文数据，能灵活迁移到视觉-语言理解与生成两类任务。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| zero-shot | /zˈiəɹəʊʃˈɒt/ | 零样本的（不微调直接迁移到新任务） | S |
| retrieval | /ɹɪtɹˈiːvəl/ | 检索（图文匹配检索任务） | S |
| synthetic | /sɪnθˈɛtɪk/ | 合成的（机器生成而非人工写的） | S |
| generalization | /dʒˌɛnəɹəlaɪzˈeɪʃən/ | 泛化（模型在新数据/新任务上的适应能力） | S |
| framework | /fɹˈeɪmwɜːk/ | 框架（一整套方法体系） | A |
| excel | /ɛksˈɛl/ | 擅长（既有模型只在理解或生成单方面突出） | A |
| suboptimal | /sʌbˈɒptɪməl/ | 次优的（含噪声网络数据并非最佳监督来源） | A |
| scale up | /skˈeɪl ˈʌp/ | 扩大规模（靠堆数据提升性能） | B |
| bootstrap | /bˈuːtstɹap/ | 自举（用自身生成的数据反哺改进训练） | B |
| captioner | /kˈapʃənə/ | 说明生成器（为图像生成描述文本的模块） | B |
| filter | /fˈɪltə/ | 过滤器（去掉低质量/噪声说明的模块） | B |

### 原句（保留完整句子）

- **zero-shot** — “An MED can operate either as ization ability when directly transferred to video- a unimodal encoder, or an image-grounded text encoder, language tasks in a zero-shot manner.”
- **retrieval** — “However, encoder-based models are less straightfor- the following key observations. ward to directly transfer to text generation tasks (e.g. image • We show that the captioner and the filter work together to captioning), whereas encoder-decoder models have not been achieve substantial performance improvement on various successfully adopted for image-text retrieval tasks. downstream tasks by bootstrapping the captions.”
- **synthetic** — “We use a Captioner (Cap) to generate synthetic captions mance improvement has been largely achieved for web images, and a Filter (Filt) to remove noisy captions. by scaling up the dataset with noisy image-text pairs collected from the web, which is a subop- collected from the web.”
- **generalization** — “The text encoder is the same as BERT (Devlin et al., loss that has been widely-used for VLP, LM enables the 2019), where a \[CLS\] token is appended to the beginning model with the generalization capability to convert visual of the text input to summarize the sentence. information into coherent captions.”
- **framework** — “In this paper, we tained by scaling up the dataset, our paper shows that the propose BLIP, a new VLP framework which trans- noisy web text is suboptimal for vision-language learning. fers flexibly to both vision-language understand- To this end, we propose BLIP: Bootstrapping Languageing and generation tasks.”
- **excel** — “However, most existing pre-trained mod- sprinkles on top” els only excel in either understanding-based tasks or generation-based tasks.”
- **suboptimal** — “In this paper, we tained by scaling up the dataset, our paper shows that the propose BLIP, a new VLP framework which trans- noisy web text is suboptimal for vision-language learning. fers flexibly to both vision-language understand- To this end, we propose BLIP: Bootstrapping Languageing and generation tasks.”
- **scale up** — “"scaling up the dataset with noisy"”
- **bootstrap** — “Xu, “Xducible scaling laws for contrastive language-image learning,” llm: Bootstrapping advanced large language models by treating in CVPR, 2023.”
- **captioner** — “We use a Captioner (Cap) to generate synthetic captions mance improvement has been largely achieved for web images, and a Filter (Filt) to remove noisy captions. by scaling up the dataset with noisy image-text pairs collected from the web, which is a subop- collected from the web.”
- **filter** — “We use a Captioner (Cap) to generate synthetic captions mance improvement has been largely achieved for web images, and a Filter (Filt) to remove noisy captions. by scaling up the dataset with noisy image-text pairs collected from the web, which is a subop- collected from the web.”

## Abstract（自动提取）

> TITLE: BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation ABSTRACT: Vision-Language Pre-training (VLP) has advanced the performance for many vision-language tasks. However, most existing pre-trained models only excel in either understanding-based tasks or generation-based tasks. Furthermore, performance improvement has been largely achieved by scaling up the dataset with noisy image-text pairs collected from the web, which is a suboptimal source of supervision. In this paper, we propose BLIP, a new VLP framework which transfers flexibly to both vision-language understanding and generation tasks. BLIP effectively utilizes the noisy web data by bootstrapping the captions, where a captioner generates synthetic captions and a filter removes the noisy ones. We achieve state-of-the-art results on a wide range of vision-language tasks, such as image-text retrieval (+2.7% in average recall@1), image captioning (+2.8% in CIDEr), and VQA (+1.6% in VQA score). BLIP also demonstrates strong generalization ability when directly transferred to video-language tasks in a zero-shot manner. Code, models, and datasets are released at https://github.com/salesforce/BLIP.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/06_BLIP.pdf`

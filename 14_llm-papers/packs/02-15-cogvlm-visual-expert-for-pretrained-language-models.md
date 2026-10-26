---
type: paper-pack
paper_id: "02-15"
stage: 2
title: "CogVLM: Visual Expert for Pretrained Language Models"
pdf: "/home/user/llm-papers/02_多模态/PDF/15_CogVLM.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-15 CogVLM: Visual Expert for Pretrained Language Models

**中文标题**：CogVLM：预训练语言模型的视觉专家

**一句话概括**：提出 CogVLM，在注意力与 FFN 层中加入可训练的"视觉专家"模块实现视觉-语言特征深度融合，不牺牲任何 NLP 性能。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| alignment | /ɐlˈaɪnmənt/ | 对齐（把图像特征与语言模型输入空间对应） | S |
| cross-modal | /kɹˈɒsmˈəʊdəl/ | 跨模态的（跨越视觉与语言两种模态） | S |
| surpass | /səpˈas/ | 超越（性能超过或持平更大模型） | S |
| bridge | /bɹˈɪdʒ/ | 弥合、桥接（填补模型间的差距） | A |
| fusion | /fjˈuːʒən/ | 融合（视觉与语言特征的深度融合） | A |
| checkpoint | /tʃˈɛkpɔɪnt/ | 检查点（训练好的模型权重） | A |
| shallow | /ʃˈaləʊ/ | 浅层的（只做简单映射、融合不深的对齐方法） | A |
| map | /mˈap/ | 映射（把特征变换到另一空间） | B |
| trainable | /tɹˈeɪnəbəl/ | 可训练的（参数参与训练更新） | B |
| module | /mˈɒdjuːl/ | 模块（模型中的功能组件） | B |
| sacrifice | /sˈakɹɪfˌaɪs/ | 牺牲（不牺牲任何 NLP 任务性能） | B |
| rank | /ɹˈaŋk/ | 排名（在基准上位居第 2） | B |

### 原句（保留完整句子）

- **alignment** — “Different 40.75 87.88 from the popular shallow alignment method 34.75 72.5 59.5 35.5 86.25 which maps image features into the input space RefCOCO MMBench 30.5 65.0 of language model, CogVLM bridges the gap 92.75 30.2541.7584.62 76.5 89.5 26.25 57.5 61.0 between the frozen pretrained language model 86.25 45.5 N/A and image encoder by a trainable visual ex- RefCOCO+ 88.5 84.0 79.5 31.5 41.0 50.5 MM-Vet 80.0 122.0 pert module in the attention and FFN layers.”
- **cross-modal** — “This trend is not isolated; similar effects have of-the-art across 17 classic cross-modal benchmarks. been observed in models like PaLM-E (Driess et al., 2023) and Flamingo (Alayrac et al., 2022).”
- **surpass** — “Even our base model surpasses all previously published models and ensembles, at a fraction of the training cost of any of the competitive models.”
- **bridge** — “Google’s neural machine translation system: Bridging the gap between human and machine translation. arXiv preprint arXiv:1609.08144, 2016. \[39\] Jie Zhou, Ying Cao, Xuguang Wang, Peng Li, and Wei Xu.”
- **fusion** — “85.0 75.0 60.753.5 51.5 67.0 125.0 90.0 128.0 As a result, CogVLM enables a deep fusion 85.0 79.0 of vision language features without sacrificing RefCOCOg 71.5 62.0 58.0 NoCaps 95.0 91.0 any performance on NLP tasks.”
- **checkpoint** — “For the base models, we used a single model obtained by averaging the last 5 checkpoints, which were written at 10-minute intervals.”
- **shallow** — “Different 40.75 87.88 from the popular shallow alignment method 34.75 72.5 59.5 35.5 86.25 which maps image features into the input space RefCOCO MMBench 30.5 65.0 of language model, CogVLM bridges the gap 92.75 30.2541.7584.62 76.5 89.5 26.25 57.5 61.0 between the frozen pretrained language model 86.25 45.5 N/A and image encoder by a trainable visual ex- RefCOCO+ 88.5 84.0 79.5 31.5 41.0 50.5 MM-Vet 80.0 122.0 pert module in the attention and FFN layers.”
- **map** — “To map the output of ViT into the same using conventional positional encoding would result in exspace as the text features from word embedding, we use an cessively lengthy encoding sequences.”
- **trainable** — “Different 40.75 87.88 from the popular shallow alignment method 34.75 72.5 59.5 35.5 86.25 which maps image features into the input space RefCOCO MMBench 30.5 65.0 of language model, CogVLM bridges the gap 92.75 30.2541.7584.62 76.5 89.5 26.25 57.5 61.0 between the frozen pretrained language model 86.25 45.5 N/A and image encoder by a trainable visual ex- RefCOCO+ 88.5 84.0 79.5 31.5 41.0 50.5 MM-Vet 80.0 122.0 pert module in the attention and FFN layers.”
- **module** — “Different 40.75 87.88 from the popular shallow alignment method 34.75 72.5 59.5 35.5 86.25 which maps image features into the input space RefCOCO MMBench 30.5 65.0 of language model, CogVLM bridges the gap 92.75 30.2541.7584.62 76.5 89.5 26.25 57.5 61.0 between the frozen pretrained language model 86.25 45.5 N/A and image encoder by a trainable visual ex- RefCOCO+ 88.5 84.0 79.5 31.5 41.0 50.5 MM-Vet 80.0 122.0 pert module in the attention and FFN layers.”
- **sacrifice** — “From awareness, it enables FP8 inference without sacrificing perthe perspective of engineering, OpenAI has adopted an formance.”
- **rank** — “However, this approach can compromise the bedding in the input while LoRA adapts the model weights models’ generalizability, particularly for tasks focused on in each layer via a low-rank matrix.”

## Abstract（自动提取）

> TITLE: CogVLM: Visual Expert for Pretrained Language Models ABSTRACT: We introduce CogVLM, a powerful open-source visual language foundation model. Different from the popular shallow alignment method which maps image features into the input space of language model, CogVLM bridges the gap between the frozen pretrained language model and image encoder by a trainable visual expert module in the attention and FFN layers. As a result, CogVLM enables deep fusion of vision language features without sacrificing any performance on NLP tasks. CogVLM-17B achieves state-of-the-art performance on 10 classic cross-modal benchmarks, including NoCaps, Flicker30k captioning, RefCOCO, RefCOCO+, RefCOCOg, Visual7W, GQA, ScienceQA, VizWiz VQA and TDIUC, and ranks the 2nd on VQAv2, OKVQA, TextVQA, COCO captioning, etc., surpassing or matching PaLI-X 55B. Codes and checkpoints are available at https://github.com/THUDM/CogVLM.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/15_CogVLM.pdf`

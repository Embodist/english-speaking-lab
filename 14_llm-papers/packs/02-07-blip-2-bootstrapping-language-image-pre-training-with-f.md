---
type: paper-pack
paper_id: "02-07"
stage: 2
title: "BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models"
pdf: "/home/user/llm-papers/02_多模态/PDF/07_BLIP2.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-07 BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models

**中文标题**：BLIP-2：用冻结图像编码器与大语言模型自举语言-图像预训练

**一句话概括**：提出 BLIP-2，用轻量级 Querying Transformer 桥接冻结的预训练图像编码器与大语言模型，以远少于现有方法的可训练参数取得 SOTA。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| outperform | /aʊtpəfˈɔːm/ | 胜过、优于（性能超过对比模型） | S |
| end-to-end | /ˈɛndtʊˈɛnd/ | 端到端的（从输入到输出整体联合训练） | S |
| modality | /məʊdˈalɪti/ | 模态（图像、文本等不同的信息形式） | S |
| generic | /dʒənˈɛɹɪk/ | 通用的（不针对特定任务的设计） | A |
| off-the-shelf | /ˈɒfðəʃˈɛlf/ | 现成的（直接拿来用的已有模型） | A |
| bridge | /bɹˈɪdʒ/ | 桥接、弥合（连接两种不同模态/模型） | A |
| lightweight | /lˈaɪtweɪt/ | 轻量级的（参数量小、开销低） | A |
| stage | /stˈeɪdʒ/ | 阶段（训练分两个阶段进行） | A |
| emerging | /ɪmˈɜːdʒɪŋ/ | 涌现的（训练后自然出现的新能力） | A |
| instruction | /ɪnstɹˈʌkʃən/ | 指令（自然语言给出的任务要求） | A |
| prohibitive | /pɹəhˈɪbɪtˌɪv/ | 高得令人望而却步的（训练成本日益高昂） | B |
| frozen | /fɹˈəʊzən/ | 冻结的（参数固定不参与训练） | B |

### 原句（保留完整句子）

- **outperform** — “(2) capabilities including visual knowledge reasoning, visual Within the same LLM family, larger models outperform commensense reasoning, visual conversation, personalized smaller ones.”
- **end-to-end** — “In Most VLP methods perform end-to-end pre-training using the first pre-training stage, we perform vision-language rep- large-scale image-text pair datasets.”
- **modality** — “BLIP-2 bridges the modality gap with a lightweight Querying Transformer, which is pre- Figure 1.”
- **generic** — “This paper Image Q-Former Language Encoder Querying Transformer Model Write a romantic message proposes BLIP-2, a generic and efficient pre- (LLM) that goes along this photo. training strategy that bootstraps vision-language Love is like a sunset, it’s … Text hard to see it coming but pre-training from off-the-shelf frozen pre-trained Queries when it does it’s so beautiful. image encoders and frozen large language mod- Bootstrapping Pre-trained Bootstrapping Pre-trained Image Models Large Language Models (LLMs) els.”
- **off-the-shelf** — “This paper Image Q-Former Language Encoder Querying Transformer Model Write a romantic message proposes BLIP-2, a generic and efficient pre- (LLM) that goes along this photo. training strategy that bootstraps vision-language Love is like a sunset, it’s … Text hard to see it coming but pre-training from off-the-shelf frozen pre-trained Queries when it does it’s so beautiful. image encoders and frozen large language mod- Bootstrapping Pre-trained Bootstrapping Pre-trained Image Models Large Language Models (LLMs) els.”
- **bridge** — “The first stage boot- lightweight Querying Transformer following a two-stage stratstraps vision-language representation learning egy to bridge the modality gap.”
- **lightweight** — “BLIP-2 bridges the modality gap with a lightweight Querying Transformer, which is pre- Figure 1.”
- **stage** — “The first stage boot- lightweight Querying Transformer following a two-stage stratstraps vision-language representation learning egy to bridge the modality gap.”
- **emerging** — “To achieve natural language instructions, which enables emerging this, Frozen (Tsimpoukelli et al., 2021) finetunes an image capabilities such as visual knowledge reasoning, visual encoder whose outputs are directly used as soft prompts conversation, etc.”
- **instruction** — “For the frozen language to extract language-informative visual representation, it ef- model, we explore the unsupervised-trained OPT model fectively functions as an information bottleneck that feeds family (Zhang et al., 2022) for decoder-based LLMs, and the most useful information to the LLM while removing the instruction-trained FlanT5 model family (Chung et al., irrelevant visual information.”
- **prohibitive** — “Second, although the cost of manually augmenting exemplars with chains of thought is minimal in the few-shot setting, such annotation costs could be prohibitive for finetuning (though this could potentially be surmounted with synthetic data generation, or zero-shot generalization).”
- **frozen** — “This paper Image Q-Former Language Encoder Querying Transformer Model Write a romantic message proposes BLIP-2, a generic and efficient pre- (LLM) that goes along this photo. training strategy that bootstraps vision-language Love is like a sunset, it’s … Text hard to see it coming but pre-training from off-the-shelf frozen pre-trained Queries when it does it’s so beautiful. image encoders and frozen large language mod- Bootstrapping Pre-trained Bootstrapping Pre-trained Image Models Large Language Models (LLMs) els.”

## Abstract（自动提取）

> TITLE: BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models ABSTRACT: The cost of vision-and-language pre-training has become increasingly prohibitive due to end-to-end training of large-scale models. This paper proposes BLIP-2, a generic and efficient pre-training strategy that bootstraps vision-language pre-training from off-the-shelf frozen pre-trained image encoders and frozen large language models. BLIP-2 bridges the modality gap with a lightweight Querying Transformer, which is pre-trained in two stages. The first stage bootstraps vision-language representation learning from a frozen image encoder. The second stage bootstraps vision-to-language generative learning from a frozen language model. BLIP-2 achieves state-of-the-art performance on various vision-language tasks, despite having significantly fewer trainable parameters than existing methods. For example, our model outperforms Flamingo80B by 8.7% on zero-shot VQAv2 with 54x fewer trainable parameters. We also demonstrate the model's emerging capabilities of zero-shot image-to-text generation that can follow natural language instructions.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/07_BLIP2.pdf`

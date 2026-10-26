---
type: paper-pack
paper_id: "02-13"
stage: 2
title: "Improved Baselines with Visual Instruction Tuning"
pdf: "/home/user/llm-papers/02_多模态/PDF/13_LLaVA1_5.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-13 Improved Baselines with Visual Instruction Tuning

**中文标题**：基于视觉指令微调的改进基线

**一句话概括**：用全连接跨模态连接器、MLP 投影与任务导向 VQA 数据等简单改进，用仅 1.2M 数据在 11 个基准上建立更强的 LLaVA 基线。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| checkpoint | /tʃˈɛkpɔɪnt/ | 检查点（此处指训练好的模型权重文件） | A |
| accessible | /aksˈɛsəbəl/ | 易获得的、可及的（让 SOTA 研究门槛更低） | A |
| surprisingly | /səpɹˈaɪzɪŋli/ | 惊人地、出乎意料地（性能出人意料地强） | A |
| data-efficient | /dˈeɪtəɹɪfˈɪʃənt/ | 数据高效的（少量数据就能学好） | A |
| projection | /pɹədʒˈɛkʃən/ | 投影（把视觉特征映射到语言空间的 MLP 层） | A |
| encouraging | /ɛŋkˈʌɹɪdʒɪŋ/ | 令人鼓舞的（视觉指令微调进展喜人） | B |
| connector | /kənˈɛktə/ | 连接器（桥接视觉与语言表示的模块） | B |
| fully-connected | /fˈʊlikənˈɛktɪd/ | 全连接的（每一层神经元全部相连的 MLP 结构） | B |
| modification | /mˌɒdɪfɪkˈeɪʃən/ | 修改、改进（对 LLaVA 的简单改动） | B |
| formatting | /fˈɔːmatɪŋ/ | 格式化的（给回答设计统一格式的提示） | B |
| establish | /ɪstˈablɪʃ/ | 建立（建立起更强的基线模型） | B |
| merely | /mˈiəli/ | 仅仅（只用很少的数据） | B |

### 原句（保留完整句子）

- **checkpoint** — “Our final 1487.5 85.9 67.7 1531.3 BLIP-2 13B checkpoint uses merely 1.2M publicly available data, InstructBLIP MMBench POPE Qwen-VL-Chat and finishes full training in ∼1 day on a single 8-A100 node.”
- **accessible** — “We hope this makes state-of-the-art LMM research more Qwen-VL 50 accessible.”
- **surprisingly** — “We show that the fully-connected 33.4 vision-language connector in LLaVA is surprisingly power- 61.6 58.2 SEED-Bench 53.4 63.1 68.2 71.6 SQA-IMG ful and data-efficient.”
- **data-efficient** — “We show that the fully-connected 33.4 vision-language connector in LLaVA is surprisingly power- 61.6 58.2 SEED-Bench 53.4 63.1 68.2 71.6 SQA-IMG ful and data-efficient.”
- **projection** — “With simple modifications to LLaVA, 1293.8 78.9 50.7 namely, using CLIP-ViT-L-336px with an MLP projection 61.3 and adding academic-task-oriented VQA data with response 56.7 61.5 63.6 formatting prompts, we establish stronger baselines that MMBench-CN 60.6 85.3 TextVQA achieve state-of-the-art across 11 benchmarks.”
- **encouraging** — “It is encouraging that LLaVA-1.5 achieves the best performance with the simplest architecture, academic compute and GQA MME MM-Vet public datasets, and yields a fully-reproducible and afford- high-res patch only 62.9 1425.8 31.9 able baseline for future research.”
- **connector** — “We show that the fully-connected 33.4 vision-language connector in LLaVA is surprisingly power- 61.6 58.2 SEED-Bench 53.4 63.1 68.2 71.6 SQA-IMG ful and data-efficient.”
- **fully-connected** — “We show that the fully-connected 33.4 vision-language connector in LLaVA is surprisingly power- 61.6 58.2 SEED-Bench 53.4 63.1 68.2 71.6 SQA-IMG ful and data-efficient.”
- **modification** — “With modifications on position embeddings specialized LLMs, a practical way is to employ a multi-stage (i.e., position interpolation) of RoPE-based LLMs \[57, 99, training approach, e.g., general and skill-specific data can 259\], CodeLLaMA further extends the context window of be scheduled at two consecutive stages.”
- **formatting** — “With simple modifications to LLaVA, 1293.8 78.9 50.7 namely, using CLIP-ViT-L-336px with an MLP projection 61.3 and adding academic-task-oriented VQA data with response 56.7 61.5 63.6 formatting prompts, we establish stronger baselines that MMBench-CN 60.6 85.3 TextVQA achieve state-of-the-art across 11 benchmarks.”
- **establish** — “With simple modifications to LLaVA, 1293.8 78.9 50.7 namely, using CLIP-ViT-L-336px with an MLP projection 61.3 and adding academic-task-oriented VQA data with response 56.7 61.5 63.6 formatting prompts, we establish stronger baselines that MMBench-CN 60.6 85.3 TextVQA achieve state-of-the-art across 11 benchmarks.”
- **merely** — “Our final 1487.5 85.9 67.7 1531.3 BLIP-2 13B checkpoint uses merely 1.2M publicly available data, InstructBLIP MMBench POPE Qwen-VL-Chat and finishes full training in ∼1 day on a single 8-A100 node.”

## Abstract（自动提取）

> TITLE: Improved Baselines with Visual Instruction Tuning ABSTRACT: Large multimodal models (LMM) have recently shown encouraging progress with visual instruction tuning. In this note, we show that the fully-connected vision-language cross-modal connector in LLaVA is surprisingly powerful and data-efficient. With simple modifications to LLaVA, namely, using CLIP-ViT-L-336px with an MLP projection and adding academic-task-oriented VQA data with simple response formatting prompts, we establish stronger baselines that achieve state-of-the-art across 11 benchmarks. Our final 13B checkpoint uses merely 1.2M publicly available data, and finishes full training in ~1 day on a single 8-A100 node. We hope this can make state-of-the-art LMM research more accessible. Code and model will be publicly available.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/13_LLaVA1_5.pdf`

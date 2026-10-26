---
type: paper-pack
paper_id: "01-11"
stage: 1
title: "LoRA: Low-Rank Adaptation of Large Language Models"
pdf: "/home/user/llm-papers/01_大模型/PDF/11_LoRA.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-11 LoRA: Low-Rank Adaptation of Large Language Models

**中文标题**：LoRA：大语言模型的低秩适配

**一句话概括**：提出 LoRA 低秩适配：冻结预训练权重、只训练注入各层的低秩分解矩阵，以极小的可训练参数量达到与全量微调相当的性能。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| paradigm | /pˈaɹədˌaɪm/ | 范式（领域内标准做法） | S |
| adaptation | /ˌadaptˈeɪʃən/ | 适配（把预训练模型调整到具体任务） | S |
| feasible | /fˈiːzɪbəl/ | 可行的 | A |
| throughput | /θɹˈuːpʊt/ | 吞吐量（单位时间处理的数据量） | A |
| latency | /lˈeɪtənsi/ | 延迟（响应所需时间） | A |
| efficacy | /ˈɛfɪkəsi/ | 有效性、效果 | A |
| low-rank | /lˈəʊɹˈaŋk/ | 低秩的（用低维矩阵近似高维矩阵） | B |
| deploying | /dɪplˈɔɪɪŋ/ | 部署（把模型投入实际使用） | B |
| freezes | /fɹˈiːzɪz/ | 冻结（固定参数不再更新） | B |
| decomposition | /dˌiːkɒmpəzˈɪʃən/ | 分解（矩阵分解为低秩因子） | B |

### 原句（保留完整句子）

- **paradigm** — “A new paradigm emerged with BERT (Devlin et al., 2019b) and GPT-2 (Radford et al., b) – both are large Transformer lan8 guage models trained on a large amount of text – where fine-tuning on task-specific data after pretraining on general domain data provides a significant performance gain compared to training on task-specific data directly.”
- **adaptation** — “We propose Low-Rank Adaptation, or LoRA, which freezes the pretrained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters for downstream tasks.”
- **feasible** — “As we pre-train larger models, full fine-tuning, which retrains all model parameters, becomes less feasible.”
- **throughput** — “LoRA performs on-par or better than finetuning in model quality on RoBERTa, DeBERTa, GPT-2, and GPT-3, despite having fewer trainable parameters, a higher training throughput, and, unlike adapters, no additional inference latency.”
- **latency** — “LoRA performs on-par or better than finetuning in model quality on RoBERTa, DeBERTa, GPT-2, and GPT-3, despite having fewer trainable parameters, a higher training throughput, and, unlike adapters, no additional inference latency.”
- **efficacy** — “We also provide an empirical investigation into rank-deficiency in language model adaptation, which sheds light on the efficacy of LoRA.”
- **low-rank** — “We propose Low-Rank Adaptation, or LoRA, which freezes the pretrained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters for downstream tasks.”
- **deploying** — “Using GPT-3 175B as an example – deploying independent instances of fine-tuned models, each with 175B parameters, is prohibitively expensive.”
- **freezes** — “We propose Low-Rank Adaptation, or LoRA, which freezes the pretrained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters for downstream tasks.”
- **decomposition** — “We propose Low-Rank Adaptation, or LoRA, which freezes the pretrained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters for downstream tasks.”

## Abstract（自动提取）

> TITLE: LoRA: Low-Rank Adaptation of Large Language Models ABSTRACT: An important paradigm of natural language processing consists of large-scale pre-training on general domain data and adaptation to particular tasks or domains. As we pre-train larger models, full fine-tuning, which retrains all model parameters, becomes less feasible. Using GPT-3 175B as an example -- deploying independent instances of fine-tuned models, each with 175B parameters, is prohibitively expensive. We propose Low-Rank Adaptation, or LoRA, which freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters for downstream tasks. Compared to GPT-3 175B fine-tuned with Adam, LoRA can reduce the number of trainable parameters by 10,000 times and the GPU memory requirement by 3 times. LoRA performs on-par or better than fine-tuning in model quality on RoBERTa, DeBERTa, GPT-2, and GPT-3, despite having fewer trainable parameters, a higher training throughput, and, unlike adapters, no additional inference latency. We also provide an empirical investigation into rank-deficiency in language model adaptation, which sheds light on the efficacy of LoRA. We release a package that facilitates the integration of LoRA with PyTorch models and provide our implementations and model checkpoints fo

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
- [[14_llm-papers/stage-01-llm|阶段 1]]

PDF：`/home/user/llm-papers/01_大模型/PDF/11_LoRA.pdf`

---
type: paper-pack
paper_id: "01-12"
stage: 1
title: "QLoRA: Efficient Finetuning of Quantized LLMs"
pdf: "/home/user/llm-papers/01_大模型/PDF/12_QLoRA.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-12 QLoRA: Efficient Finetuning of Quantized LLMs

**中文标题**：QLoRA：量化大语言模型的高效微调

**一句话概括**：提出 QLoRA，把 4 位量化与低秩适配结合，使 65B 模型可在单张 48GB GPU 上微调，且不损失 16 位微调的任务性能。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| quantized | /kwˈɒntaɪzd/ | 量化的（用低精度数值表示权重） | A |
| sacrificing | /sˈakɹɪfˌaɪsɪŋ/ | 牺牲 | A |
| finetuning | /fˈaɪntjuːnɪŋ/ | 微调 | B |
| preserving | /pɹɪzˈɜːvɪŋ/ | 保持、保留 | B |
| backpropagates | /bˈakpɹəpˌaɡeɪts/ | 反向传播（计算梯度并更新参数） | B |
| gradients | /ɡɹˈeɪdiənts/ | 梯度（损失对参数的导数） | B |
| innovations | /ˌɪnəvˈeɪʃənz/ | 创新（方法） | B |
| footprint | /fˈʊtpɹɪnt/ | 占用（内存占用大小） | B |
| spikes | /spˈaɪks/ | 峰值（内存用量瞬间激增） | B |
| trustworthy | /tɹˈʌstwɜːði/ | 可信的、可靠的 | B |

### 原句（保留完整句子）

- **quantized** — “QL O RA backpropagates gradients through a frozen, 4-bit quantized pretrained language model into Low Rank Adapters (LoRA).”
- **sacrificing** — “QL O RA introduces a number of innovations to save memory without sacrificing performance: (a) 4-bit NormalFloat (NF4), a new data type that is information theoretically optimal for normally distributed weights (b) Double Quantization to reduce the average memory footprint by quantizing the quantization constants, and (c) Paged Optimizers to manage memory spikes.”
- **finetuning** — “Our best model family, which we name Guanaco, outperforms all previous openly released models on the Vicuna benchmark, reaching 99.3% of the performance level of ChatGPT while only requiring 24 hours of finetuning on a single GPU.”
- **preserving** — “Major approaches for preserving 16-bit LLM quality focus on managing outlier features (e.g., SmoothQuant \[66\] and LLM.int8() \[14\]) while others use more sophisticated grouping methods \[44, 69\].”
- **backpropagates** — “QL O RA backpropagates gradients through a frozen, 4-bit quantized pretrained language model into Low Rank Adapters (LoRA).”
- **gradients** — “QL O RA backpropagates gradients through a frozen, 4-bit quantized pretrained language model into Low Rank Adapters (LoRA).”
- **innovations** — “QL O RA introduces a number of innovations to save memory without sacrificing performance: (a) 4-bit NormalFloat (NF4), a new data type that is information theoretically optimal for normally distributed weights (b) Double Quantization to reduce the average memory footprint by quantizing the quantization constants, and (c) Paged Optimizers to manage memory spikes.”
- **footprint** — “QL O RA introduces a number of innovations to save memory without sacrificing performance: (a) 4-bit NormalFloat (NF4), a new data type that is information theoretically optimal for normally distributed weights (b) Double Quantization to reduce the average memory footprint by quantizing the quantization constants, and (c) Paged Optimizers to manage memory spikes.”
- **spikes** — “QL O RA introduces a number of innovations to save memory without sacrificing performance: (a) 4-bit NormalFloat (NF4), a new data type that is information theoretically optimal for normally distributed weights (b) Double Quantization to reduce the average memory footprint by quantizing the quantization constants, and (c) Paged Optimizers to manage memory spikes.”
- **trustworthy** — “Furthermore, we find that current chatbot benchmarks are not trustworthy to accurately evaluate the performance levels of chatbots.”

## Abstract（自动提取）

> TITLE: QLoRA: Efficient Finetuning of Quantized LLMs ABSTRACT: We present QLoRA, an efficient finetuning approach that reduces memory usage enough to finetune a 65B parameter model on a single 48GB GPU while preserving full 16-bit finetuning task performance. QLoRA backpropagates gradients through a frozen, 4-bit quantized pretrained language model into Low Rank Adapters~(LoRA). Our best model family, which we name Guanaco, outperforms all previous openly released models on the Vicuna benchmark, reaching 99.3% of the performance level of ChatGPT while only requiring 24 hours of finetuning on a single GPU. QLoRA introduces a number of innovations to save memory without sacrificing performance: (a) 4-bit NormalFloat (NF4), a new data type that is information theoretically optimal for normally distributed weights (b) double quantization to reduce the average memory footprint by quantizing the quantization constants, and (c) paged optimziers to manage memory spikes. We use QLoRA to finetune more than 1,000 models, providing a detailed analysis of instruction following and chatbot performance across 8 instruction datasets, multiple model types (LLaMA, T5), and model scales that would be infeasible to run with regular finetuning (e.g. 33B and 65B parameter models). Our results show that QLoRA finetuning on a small high-quality dataset leads to state-of-the-art results, even when usin

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

PDF：`/home/user/llm-papers/01_大模型/PDF/12_QLoRA.pdf`

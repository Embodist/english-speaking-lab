---
type: paper-pack
paper_id: "01-13"
stage: 1
title: "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"
pdf: "/home/user/llm-papers/01_大模型/PDF/13_FlashAttention.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-13 FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

**中文标题**：FlashAttention：IO 感知的快速且内存高效的精确注意力

**一句话概括**：提出 IO 感知的精确注意力算法 FlashAttention，通过分块（tiling）减少 GPU 显存读写，显著加速训练并支持更长序列。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| quadratic | /kwɒdɹˈatɪk/ | 二次方的（复杂度随序列长度平方增长） | A |
| baselines | /bˈeɪslaɪnz/ | 基线（用于对比的已有方法） | A |
| memory-hungry | /mˈɛməɹihˈʌŋɡɹi/ | 耗内存的（内存占用大） | B |
| exact | /ɛɡzˈakt/ | 精确的（不做近似计算） | B |
| trading off | /tɹˈeɪdɪŋ ˈɒf/ | 以……为代价换取 | B |
| wall-clock | /wˈɔːlklˈɒk/ | 实际耗时的（按真实时钟计算的运行时间） | B |
| accounting for | /ɐkˈaʊntɪŋ fˈɔː/ | 考虑到、计入 | B |
| tiling | /tˈaɪlɪŋ/ | 分块（把数据切成小块逐个处理） | B |
| optimal | /ˈɒptɪməl/ | 最优的 | B |
| perplexity | /pəplˈɛksɪti/ | 困惑度（语言模型指标，越低越好） | B |

### 原句（保留完整句子）

- **quadratic** — “Transformers have grown larger \[5\] and deeper \[83\], but equipping them with longer context remains difficult \[80\], since the self-attention module at their heart has time and memory complexity quadratic in sequence length.”
- **baselines** — “FlashAttention trains Transformers faster than existing baselines: 15% end-to-end wall-clock speedup on BERT-large (seq. length 512) compared to the MLPerf 1.1 training speed record, 3× speedup on GPT-2 (seq. length 1K), and 2.4× speedup on long-range arena (seq. length 1K-4K).”
- **memory-hungry** — “"Transformers are slow and memory-hungry on long sequences"”
- **exact** — “FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness Tri Dao† , Daniel Y.”
- **trading off** — “Approximate attention methods have attempted to address this problem by trading off model quality to reduce the compute complexity, but often do not achieve wall-clock speedup.”
- **wall-clock** — “Approximate attention methods have attempted to address this problem by trading off model quality to reduce the compute complexity, but often do not achieve wall-clock speedup.”
- **accounting for** — “We argue that a missing principle is making attention algorithms IOaware—accounting for reads and writes between levels of GPU memory.”
- **tiling** — “We propose FlashAttention, an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU high bandwidth memory (HBM) and GPU on-chip SRAM.”
- **optimal** — “We analyze the IO complexity of FlashAttention, showing that it requires fewer HBM accesses than standard attention, and is optimal for a range of SRAM sizes.”
- **perplexity** — “FlashAttention and block-sparse FlashAttention enable longer context in Transformers, yielding higher quality models (0.7 better perplexity on GPT-2 and 6.4 points of lift on long-document classification) and entirely new capabilities: the first Transformers to achieve better-than-chance performance on the Path-X challenge (seq. length 16K, 61.4% accuracy) and Path-256 (seq. length 64K, 63.1% accuracy).”

## Abstract（自动提取）

> TITLE: FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness ABSTRACT: Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length. Approximate attention methods have attempted to address this problem by trading off model quality to reduce the compute complexity, but often do not achieve wall-clock speedup. We argue that a missing principle is making attention algorithms IO-aware -- accounting for reads and writes between levels of GPU memory. We propose FlashAttention, an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU high bandwidth memory (HBM) and GPU on-chip SRAM. We analyze the IO complexity of FlashAttention, showing that it requires fewer HBM accesses than standard attention, and is optimal for a range of SRAM sizes. We also extend FlashAttention to block-sparse attention, yielding an approximate attention algorithm that is faster than any existing approximate attention method. FlashAttention trains Transformers faster than existing baselines: 15% end-to-end wall-clock speedup on BERT-large (seq. length 512) compared to the MLPerf 1.1 training speed record, 3$\times$ speedup on GPT-2 (seq. length 1K), and 2.4$\times$ speedup on long-range arena (seq. length 1K-4K). FlashAttention and block-sparse FlashAt

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

PDF：`/home/user/llm-papers/01_大模型/PDF/13_FlashAttention.pdf`

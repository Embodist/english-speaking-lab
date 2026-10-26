---
type: paper-pack
paper_id: "00-00"
stage: 0
title: "Attention Is All You Need"
pdf: "/home/user/llm-papers/00_总览综述/PDF/00_Transformer_AttentionIsAllYouNeed.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 00-00 Attention Is All You Need

**中文标题**：《注意力即一切》

**一句话概括**：提出完全基于注意力机制的 Transformer 架构，摒弃循环与卷积网络，在机器翻译等任务上取得当时最先进的效果，成为后续几乎所有大语言模型的基石。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| state-of-the-art | /stˈeɪtɒvðɪˈɑːt/ | 最先进的、当前最优的（常缩写为 SOTA） | S |
| recurrent | /ɹɪkˈʌɹənt/ | 循环的（指 RNN 这类按时间步循环处理序列的网络） | A |
| mechanism | /mˈɛkənˌɪzəm/ | 机制（attention mechanism 注意力机制：让模型聚焦输入中重要部分的机制） | A |
| propose | /pɹəpˈəʊz/ | 提出（学术写作高频词，指提出新的方法/架构） | A |
| solely | /sˈəʊlli/ | 仅仅、完全（based solely on 即"完全基于"） | A |
| dominant | /dˈɒmɪnənt/ | 主导的、占支配地位的（本文指当前主流的序列转导模型） | A |
| ensemble | /ɒnsˈɒmbəl/ | 集成模型（多个模型组合起来投票/平均得到的结果） | A |
| transduction | /tɹansdˈʌkʃən/ | 转导：把输入序列整体转换为输出序列的任务（如机器翻译） | B |
| configuration | /kənfˌɪɡjəɹˈeɪʃən/ | 结构、配置（encoder-decoder configuration 即编码器-解码器架构） | B |
| dispensing with | /dɪspˈɛnsɪŋ wˈɪð/ | 摒弃、省去（dispense with 意为不再需要某事物） | B |
| parallelizable | /pˈaɹəlˌɛlaɪzəbəl/ | 可并行计算的（本文强调 Transformer 比 RNN 更易于并行训练） | B |
| constituency parsing | /kənstˈɪtjuːənsi pˈɑːsɪŋ/ | 成分句法分析（把句子按短语结构解析成语法树的任务） | B |

### 原句（保留完整句子）

- **state-of-the-art** — “On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature.”
- **recurrent** — “1 Introduction Recurrent neural networks, long short-term memory \[13\] and gated recurrent \[7\] neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems such as language modeling and machine translation \[35, 2, 5\].”
- **mechanism** — “The best performing models also connect the encoder and decoder through an attention mechanism.”
- **propose** — “We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.”
- **solely** — “Provided proper attribution is provided, Google hereby grants permission to reproduce the tables and figures in this paper solely for use in journalistic or scholarly works.”
- **dominant** — “Gomez∗ † Łukasz Kaiser∗ Google Research University of Toronto Google Brain llion@google.com aidan@cs.toronto.edu lukaszkaiser@google.com Illia Polosukhin∗ ‡ illia.polosukhin@gmail.com Abstract The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder.”
- **ensemble** — “Our model achieves 28.4 BLEU on the WMT 2014 Englishto-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU.”
- **transduction** — “1 Introduction Recurrent neural networks, long short-term memory \[13\] and gated recurrent \[7\] neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems such as language modeling and machine translation \[35, 2, 5\].”
- **configuration** — “The configuration of this model is listed in the bottom line of Table 3.”
- **dispensing with** — “We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.”
- **parallelizable** — “Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train.”
- **constituency parsing** — “6.3 English Constituency Parsing To evaluate if the Transformer can generalize to other tasks we performed experiments on English constituency parsing.”

## Abstract（自动提取）

> TITLE: Attention Is All You Need ABSTRACT: The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.

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
- [[14_llm-papers/stage-00-surveys|阶段 0]]

PDF：`/home/user/llm-papers/00_总览综述/PDF/00_Transformer_AttentionIsAllYouNeed.pdf`

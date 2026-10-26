---
type: paper-pack
paper_id: "01-32"
stage: 1
title: "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints"
pdf: "/home/user/llm-papers/01_大模型/PDF/32_GQA.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-32 GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints

**中文标题**：GQA：从多头检查点训练广义多查询 Transformer 模型

**一句话概括**：提出 GQA 分组查询注意力，并给出把已有多头检查点"升级训练"为多查询注意力模型的方法，以接近多头的质量、接近 MQA 的速度。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| generalization | /dʒˌɛnəɹəlaɪzˈeɪʃən/ | 推广、泛化（此处指 MQA 的一般化形式） | S |
| recipe | /ɹˈɛsɪpˌiː/ | 方法、配方 | S |
| comparable | /kˈɒmpəɹəbəl/ | 相当的、可比的 | S |
| intermediate | /ˌɪntəmˈiːdiət/ | 中间的（介于两者之间） | A |
| decoder | /dɪkˈəʊdə/ | 解码器（负责生成输出的部分） | A |
| checkpoints | /tʃˈɛkpɔɪnts/ | 检查点（训练好的模型存档） | B |
| drastically | /dɹˈastɪkli/ | 大幅度地 | B |
| degradation | /dɪɡɹɐdˈeɪʃən/ | 退化（质量下降） | B |
| desirable | /dɪzˈaɪəɹəbəl/ | 可取的、理想的 | B |
| uptraining | /ˈʌptɹeɪnɪŋ/ | 升级训练（把已有模型转换成新结构继续训练） | B |

### 原句（保留完整句子）

- **generalization** — “With instruction tuning, LLMs are mostly conducted in terms of language modeling loss are enabled to follow the task instructions for new tasks (e.g., per-token cross-entropy loss in nats \[30\]), while in without using explicit examples, thus having an improved practice we are more concerned about the performance of generalization ability.”
- **recipe** — “We (1) propose a recipe for Second, we propose grouped-query attention uptraining existing multi-head language model (GQA), an interpolation between multi-head and checkpoints into models with MQA using 5% multi-query attention with single key and value of original pre-training compute, and (2) introduce grouped-query attention (GQA), a gener- heads per subgroup of query heads.”
- **comparable** — “We show that uptrained GQA achieves quality close to multi-head attention with comparable 2 Method speed to MQA.”
- **intermediate** — “We show that alization of multi-query attention which uses uptrained GQA achieves quality close to multian intermediate (more than one, less than num- head attention while being almost as fast as multiber of query heads) number of key-value heads. query attention.”
- **decoder** — “2.1 Uptraining 1 Introduction Generating a multi-query model from a multi-head Autoregressive decoder inference is a severe bottle- model takes place in two steps: first, converting the neck for Transformer models due to the memory checkpoint, and second, additional pre-training to bandwidth overhead from loading decoder weights allow the model to adapt to its new structure.”
- **checkpoints** — “GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints Joshua Ainslie∗, James Lee-Thorp∗, Michiel de Jong∗ † Yury Zemlyanskiy, Federico Lebrón, Sumit Sanghai Google Research Abstract show that language model checkpoints with multiMulti-query attention (MQA), which only uses head attention (MHA) can be uptrained (Komata single key-value head, drastically speeds up suzaki et al., 2022) to use MQA with a small fracdecoder inference.”
- **drastically** — “GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints Joshua Ainslie∗, James Lee-Thorp∗, Michiel de Jong∗ † Yury Zemlyanskiy, Federico Lebrón, Sumit Sanghai Google Research Abstract show that language model checkpoints with multiMulti-query attention (MQA), which only uses head attention (MHA) can be uptrained (Komata single key-value head, drastically speeds up suzaki et al., 2022) to use MQA with a small fracdecoder inference.”
- **degradation** — “However, multi-query attention (MQA) can lead to quality degradation and training instability, and it may not be feasible to train separate models optimized for quality and inference.”
- **desirable** — “Furthermore, FIGA \[388\] designs a quality) and positive (the refined output by LLMs) re- token-level contrastive loss that aims to encourage desirable sponses are leveraged in a contrastive way, to enable LLMs tokens, penalize undesirable ones, and disregard trivial to deeply understand what fine-grained revisions actually tokens.”
- **uptraining** — “We (1) propose a recipe for Second, we propose grouped-query attention uptraining existing multi-head language model (GQA), an interpolation between multi-head and checkpoints into models with MQA using 5% multi-query attention with single key and value of original pre-training compute, and (2) introduce grouped-query attention (GQA), a gener- heads per subgroup of query heads.”

## Abstract（自动提取）

> TITLE: GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints ABSTRACT: Multi-query attention (MQA), which only uses a single key-value head, drastically speeds up decoder inference. However, MQA can lead to quality degradation, and moreover it may not be desirable to train a separate model just for faster inference. We (1) propose a recipe for uptraining existing multi-head language model checkpoints into models with MQA using 5% of original pre-training compute, and (2) introduce grouped-query attention (GQA), a generalization of multi-query attention which uses an intermediate (more than one, less than number of query heads) number of key-value heads. We show that uptrained GQA achieves quality close to multi-head attention with comparable speed to MQA.

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

PDF：`/home/user/llm-papers/01_大模型/PDF/32_GQA.pdf`

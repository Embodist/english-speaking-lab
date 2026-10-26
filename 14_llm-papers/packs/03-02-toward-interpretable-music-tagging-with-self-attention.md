---
type: paper-pack
paper_id: "03-02"
stage: 3
title: "Toward Interpretable Music Tagging with Self-Attention"
pdf: "/home/user/llm-papers/03_音乐检索理解/PDF/02_AttentionCNN_MusicTagging.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 03-02 Toward Interpretable Music Tagging with Self-Attention

**中文标题**：迈向可解释的基于自注意力的音乐标注

**一句话概括**：提出基于自注意力的深度序列模型用于音乐标注：浅层卷积层后接堆叠的 Transformer 编码器，相比全卷积或循环网络更可解释，同时在 MagnaTagATune 与 Million Song Dataset 上取得有竞争力的结果。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| retrieval | /ɹɪtɹˈiːvəl/ | 检索（音乐信息检索 MIR） | S |
| architecture | /ˈɑːkɪtˌɛktʃə/ | 网络结构、架构 | S |
| sparse | /spˈɑːs/ | 稀疏的（音乐中相关成分分布分散） | S |
| self-attention | /sˈɛlfɐtˈɛnʃən/ | 自注意力（让序列中每个位置关注其他位置的机制） | A |
| solely | /sˈəʊlli/ | 仅仅、完全（只基于自注意力） | A |
| variant | /vˈeəɹiənt/ | 变体（Transformer 的各种改进版本） | A |
| conventional | /kənvˈɛnʃənəl/ | 常规的、传统的（既有方法） | A |
| semantics | /səmˈantɪks/ | 语义（音乐表达的意义） | A |
| interpretable | /ɪntˈɜːpɹɪtəbəl/ | 可解释的（能看清模型决策依据） | B |
| relate | /ɹɪlˈeɪt/ | 关联、建立联系（把序列中不同位置联系起来） | B |
| stacked | /stˈakt/ | 堆叠的（多层叠放的编码器） | B |
| validate | /vˈalɪdˌeɪt/ | 验证（用数据集检验性能） | B |

### 原句（保留完整句子）

- **retrieval** — “It has been a longstanding research challenge in information retrieval (IR) \[10, 11\] and natural language to achieve this goal, to enable machines to read, write, and processing (NLP) \[12–14\].”
- **architecture** — “We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.”
- **sparse** — “Mixdeployment life-cycle, which aims to effectively reduce the tral is a kind of sparse Mixture-of-Experts (SMoE) model potential risks of using the models.”
- **self-attention** — “Jakob proposed replacing RNNs with self-attention and started the effort to evaluate this idea.”
- **solely** — “Provided proper attribution is provided, Google hereby grants permission to reproduce the tables and figures in this paper solely for use in journalistic or scholarly works.”
- **variant** — “Niki designed, implemented, tuned and evaluated countless model variants in our original codebase and tensor2tensor.”
- **conventional** — “The conventional Transformer arleave a detailed discussion about the architecture selection chitecture typically suffers from quadratic computational in Section 4.2.5. complexity with respect to sequence length, resulting in a Causal Decoder Architecture.”
- **semantics** — “Thus, unsupervised language to compress the world knowledge into the decoder-only modeling could be capable in solving various tasks, if it was Transformer model by language modeling, such that it can trained to have sufficient capacity in recovering the world recover (or memorize) the semantics of world knowledge text.”
- **interpretable** — “As side benefit, self-attention could yield more interpretable models.”
- **relate** — “In these models, the number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions, linearly for ConvS2S and logarithmically for ByteNet.”
- **stacked** — “"followed by stacked Transformer encoders"”
- **validate** — “To validate this strategy, tuned based on LLaMA \[57\], such as BenTsao \[356\].”

## 摘要提示（PDF 文本不可提取）

> 提出基于自注意力的深度序列模型用于音乐标注：浅层卷积层后接堆叠的 Transformer 编码器，相比全卷积或循环网络更可解释，同时在 MagnaTagATune 与 Million Song Dataset 上取得有竞争力的结果。

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
- [[14_llm-papers/stage-03-music-retrieval|阶段 3]]

PDF：`/home/user/llm-papers/03_音乐检索理解/PDF/02_AttentionCNN_MusicTagging.pdf`

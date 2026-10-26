---
type: paper-pack
paper_id: "01-08"
stage: 1
title: "RoFormer: Enhanced Transformer with Rotary Position Embedding"
pdf: "/home/user/llm-papers/01_大模型/PDF/08_RoPE.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-08 RoFormer: Enhanced Transformer with Rotary Position Embedding

**中文标题**：RoFormer：带旋转位置编码的增强 Transformer

**一句话概括**：提出旋转位置编码 RoPE，用旋转矩阵编码绝对位置并显式建模相对位置依赖，改进 Transformer 在长文本分类上的表现。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| leverage | /lˈiːvəɹɪdʒ/ | 利用 | S |
| supervision | /suːpəvˈɪʒən/ | 监督信息（给模型提供训练信号的额外信息） | A |
| explicit | /ɛksplˈɪsɪt/ | 显式的（明确表达出来的） | A |
| rotary position embedding | /ɹˈəʊtəɹi pəzˈɪʃən ɛmbˈɛdɪŋ/ | 旋转位置编码（RoPE，用旋转矩阵编码位置） | B |
| encoding | /ɛŋkˈəʊdɪŋ/ | 编码（把位置信息编入模型） | B |
| rotation matrix | /ɹəʊtˈeɪʃən mˈeɪtɹɪks/ | 旋转矩阵 | B |
| flexibility | /flˌɛksəbˈɪlɪti/ | 灵活性 | B |
| decaying | /dɪkˈeɪɪŋ/ | 衰减的（随距离增大而减弱） | B |
| alternatives | /ɔːltˈɜːnətˌɪvz/ | 替代方案、竞争者 | B |
| theoretical analysis | /θiəɹˈɛtɪkəl ɐnˈaləsˌɪs/ | 理论分析 | B |

### 原句（保留完整句子）

- **leverage** — “Then, we propose a novel method named Rotary Position Embedding(RoPE) to effectively leverage the positional information.”
- **supervision** — “It enables valuable supervision for dependency modeling between elements at different positions of the sequence.”
- **explicit** — “Specifically, the proposed RoPE encodes the absolute position with a rotation matrix and meanwhile incorporates the explicit relative position dependency in self-attention formulation.”
- **rotary position embedding** — “Then, we propose a novel method named Rotary Position Embedding(RoPE) to effectively leverage the positional information.”
- **encoding** — “Notably, RoPE enables valuable properties, including the flexibility of sequence length, decaying inter-token dependency with increasing relative distances, and the capability of equipping the linear self-attention with relative position encoding.”
- **rotation matrix** — “Specifically, the proposed RoPE encodes the absolute position with a rotation matrix and meanwhile incorporates the explicit relative position dependency in self-attention formulation.”
- **flexibility** — “Notably, RoPE enables valuable properties, including the flexibility of sequence length, decaying inter-token dependency with increasing relative distances, and the capability of equipping the linear self-attention with relative position encoding.”
- **decaying** — “Notably, RoPE enables valuable properties, including the flexibility of sequence length, decaying inter-token dependency with increasing relative distances, and the capability of equipping the linear self-attention with relative position encoding.”
- **alternatives** — “Our experiments show that it consistently overcomes its alternatives.”
- **theoretical analysis** — “Furthermore, we provide a theoretical analysis to explain some experimental results.”

## Abstract（自动提取）

> TITLE: RoFormer: Enhanced Transformer with Rotary Position Embedding ABSTRACT: Position encoding recently has shown effective in the transformer architecture. It enables valuable supervision for dependency modeling between elements at different positions of the sequence. In this paper, we first investigate various methods to integrate positional information into the learning process of transformer-based language models. Then, we propose a novel method named Rotary Position Embedding(RoPE) to effectively leverage the positional information. Specifically, the proposed RoPE encodes the absolute position with a rotation matrix and meanwhile incorporates the explicit relative position dependency in self-attention formulation. Notably, RoPE enables valuable properties, including the flexibility of sequence length, decaying inter-token dependency with increasing relative distances, and the capability of equipping the linear self-attention with relative position encoding. Finally, we evaluate the enhanced transformer with rotary position embedding, also called RoFormer, on various long text classification benchmark datasets. Our experiments show that it consistently overcomes its alternatives. Furthermore, we provide a theoretical analysis to explain some experimental results. RoFormer is already integrated into Huggingface: \url{https://huggingface.co/docs/transformers/model_doc/rofor

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

PDF：`/home/user/llm-papers/01_大模型/PDF/08_RoPE.pdf`

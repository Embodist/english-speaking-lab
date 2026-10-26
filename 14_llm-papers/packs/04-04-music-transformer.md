---
type: paper-pack
paper_id: "04-04"
stage: 4
title: "Music Transformer"
pdf: "/home/user/llm-papers/04_音乐生成/PDF/04_MusicTransformer.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 04-04 Music Transformer

**中文标题**：音乐 Transformer

**一句话概括**：提出把相对注意力机制对中间相对信息的存储需求从二次方降为线性的算法，使基于自注意力的 Transformer 能生成数分钟长、结构连贯的音乐，以及根据旋律生成伴奏。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| coherence | /kəʊhˈiəɹəns/ | 连贯性（长程一致性） | A |
| rely on | /ɹɪlˈaɪ ˈɒn/ | 依赖（音乐高度依赖重复） | A |
| quadratic | /kwɒdɹˈatɪk/ | 二次的（随序列长度平方增长） | A |
| accompaniment | /ɐkˈʌmpɐnˌɪmənt/ | 伴奏 | A |
| repetition | /ɹˌɛpətˈɪʃən/ | 重复（音乐结构的重要手法） | B |
| self-reference | /sˈɛlfɹˈɛfɹəns/ | 自指（音乐对自身的引用） | B |
| motif | /məʊtˈiːf/ | 动机（音乐中最小的主题乐思） | B |
| relative | /ɹˈɛlətˌɪv/ | 相对的（相对位置信息） | B |
| modulate | /mˈɒdjʊlˌeɪt/ | 调节（根据距离调节注意力权重） | B |
| impractical | /ɪmpɹˈaktɪkəl/ | 不切实际的（不可行的） | B |
| elaborate | /ɪlˈabəɹˌeɪt/ | 展开、发挥（围绕动机作展开） | B |
| chorale | /kˈɔːɹeɪl/ | 众赞歌（四声部赞美诗，JSB 巴赫的众赞歌数据集） | B |

### 原句（保留完整句子）

- **coherence** — “The Transformer (Vaswani et al., 2017), a sequence model based on self-attention, has achieved compelling results in many generation tasks that require maintaining long-range coherence.”
- **rely on** — “"meanwhile relying on pretrained vision models to"”
- **quadratic** — “This is impractical for long sequences such as musical compositions since their memory complexity for intermediate relative information is quadratic in the sequence length.”
- **accompaniment** — “4.2.2 H ARMONIZATION : C ONDITIONING ON MELODY To explore the sequence-to-sequence setup of Transformers, Table 4: Validation conditional we experimented with a conditioned generation task where NLL given groundtruth melody from the encoder takes in a given melody and the decoder has to Piano-e-Competition. realize the entire performance, i.e. melody plus accompaniment.”
- **repetition** — “(2018) use self-similarity in style-transfer fashion, where the self-similarity structure of a piece serves as a template objective for gradient descent to impose similar repetition structure on an input score.”
- **self-reference** — “Self-reference occurs on multiple timescales, from motifs to phrases to reusing of entire sections of music, such as in pieces with ABA structure.”
- **motif** — “(2018)) with compelling structure, generate continuations that coherently elaborate on a given motif, and in a seq2seq setup generate accompaniments conditioned on melodies1 .”
- **relative** — “In musical composition and performance, however, relative timing is critically important.”
- **modulate** — “Existing approaches for representing relative positional information in the Transformer modulate attention based on pairwise distance (Shaw et al., 2018).”
- **impractical** — “This is impractical for long sequences such as musical compositions since their memory complexity for intermediate relative information is quadratic in the sequence length.”
- **elaborate** — “(2018)) with compelling structure, generate continuations that coherently elaborate on a given motif, and in a seq2seq setup generate accompaniments conditioned on melodies1 .”
- **chorale** — “The JSB Chorale dataset consists of four-part scored choral music, which can be represented as a matrix where rows correspond to voices and columns to time discretized to sixteenth notes.”

## Abstract（自动提取）

> TITLE: Music Transformer ABSTRACT: Music relies heavily on repetition to build structure and meaning. Self-reference occurs on multiple timescales, from motifs to phrases to reusing of entire sections of music, such as in pieces with ABA structure. The Transformer (Vaswani et al., 2017), a sequence model based on self-attention, has achieved compelling results in many generation tasks that require maintaining long-range coherence. This suggests that self-attention might also be well-suited to modeling music. In musical composition and performance, however, relative timing is critically important. Existing approaches for representing relative positional information in the Transformer modulate attention based on pairwise distance (Shaw et al., 2018). This is impractical for long sequences such as musical compositions since their memory complexity for intermediate relative information is quadratic in the sequence length. We propose an algorithm that reduces their intermediate memory requirement to linear in the sequence length. This enables us to demonstrate that a Transformer with our modified relative attention mechanism can generate minute-long compositions (thousands of steps, four times the length modeled in Oore et al., 2018) with compelling structure, generate continuations that coherently elaborate on a given motif, and in a seq2seq setup generate accompaniments conditione

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
- [[14_llm-papers/stage-04-music-generation|阶段 4]]

PDF：`/home/user/llm-papers/04_音乐生成/PDF/04_MusicTransformer.pdf`

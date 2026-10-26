---
type: paper-pack
paper_id: "04-16"
stage: 4
title: "Symphony: Bidirectional Language-Music Modeling"
pdf: "/home/user/llm-papers/04_音乐生成/PDF/16_Symphony_Text2Music.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 04-16 Symphony: Bidirectional Language-Music Modeling

**中文标题**：Symphony：双向语言-音乐建模

**一句话概括**：提出基于大语言模型的双向语言-音乐建模框架 Symphony：把音乐编码为离散词元，用统一的大语言模型既支持文本条件生成音乐（text-to-music），也支持音乐理解与描述生成（music-to-text），并在音乐生成与理解任务上展示效果。（无官方 abstract，基于标题与领域知识）

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| zero-shot | /zˈiəɹəʊʃˈɒt/ | 零样本的（无需微调即可完成新任务） | S |
| autoregressive | /ˌɔːtəʊɹɪɡɹˈɛsɪv/ | 自回归的（逐个词元预测生成） | S |
| alignment | /ɐlˈaɪnmənt/ | 对齐（文本语义与音乐片段的对应关系） | S |
| discrete | /dɪskɹˈiːt/ | 离散的（音乐以离散词元而非连续波形表示） | S |
| conditioning | /kəndˈɪʃənɪŋ/ | 条件（生成时给定文本/音乐提示作为条件） | A |
| prompt | /pɹˈɒmpt/ | 提示（词）（引导生成的文本输入） | A |
| fine-tuning | /fˈaɪntjˈuːnɪŋ/ | 微调（在下游任务上继续训练） | A |
| bidirectional | /baɪdaɪɹˈɛkʃənəl/ | 双向的（文本→音乐与音乐→文本两个方向） | A |
| tokenization | /tˌəʊkənaɪzˈeɪʃən/ | 词元化（把音乐/文本切成离散词元序列） | A |
| captioning | /kˈapʃənɪŋ/ | 描述生成（为音乐自动生成文字描述） | A |
| coherence | /kəʊhˈiəɹəns/ | 连贯性（长篇幅音乐的结构连贯） | A |
| generation | /dʒˌɛnəɹˈeɪʃən/ | 生成（音乐生成任务） | B |

### 原句（保留完整句子）

- **zero-shot** — “In the neural networks to a significant size can lead to a huge the GPT-3’s paper, it formally introduced the concept of increase in model capacity. in-context learning (ICL)17 , which utilizes LLMs in a fewshot or zero-shot way.”
- **autoregressive** — “These models are mainly trained randomness and diversity during generation: to recover the replaced spans in an autoregressive way. xi ∼ P (x|x<i ).”
- **alignment** — “Index Terms—Large Language Models; Emergent Abilities; Adaptation Tuning; Utilization; Alignment; Capacity Evaluation ✦ 1 I NTRODUCTION “The limits of my language mean the limits of my world.” extensive attention in the literature, which can be divided —Ludwig Wittgenstein into four major development stages: • Statistical language models (SLM).”
- **discrete** — “Based on the discrete tion tuning and alignment tuning to adapt LLMs according prompting methods \[412, 413\], it augments the input text to specific goals.”
- **conditioning** — “"jointly conditioning on both left and right context in all layers"”
- **prompt** — “A number of studies 3 have explored the performance limit by training an ever the prompting interface (e.g., GPT-4 API).”
- **fine-tuning** — “This study has inspired a large number of follow-up models for representation learning (beyond word sequence work, which sets the “pre-training and fine-tuning” learning modeling), having an important impact on the field of NLP. paradigm.”
- **bidirectional** — “In this paradigm, it word representations by first pre-training a bidirectional often requires fine-tuning the PLM for adapting to different LSTM (biLSTM) network (instead of learning fixed word downstream tasks. representations) and then fine-tuning the biLSTM network according to specific downstream tasks.”
- **tokenization** — “One direct and effective approach is to employ 19 Ready to Raw Corpus Filtering & Selection De-duplication Privacy Reduction Tokenization pre-train!”
- **captioning** — “"This dataset includes key tasks such as detailed captioning"”
- **coherence** — “Beam search \[307\] retains the sentences to improve the generation coherence during decoding.”
- **generation** — “Making generation less sequential is another research goals of ours.”

## Abstract（自动提取）

> The characterizations when two natural upper bounds of the set of copulas with a given diagonal section are copulas have been well studied in the literature. Given a curvilinear section, however, there is only a partial result concerning the characterization when a natural upper bound of the set of copulas is a copula. In this paper, we completely solve the characterization problem for this natural upper bound to be a copula in the curvilinear case. 

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

PDF：`/home/user/llm-papers/04_音乐生成/PDF/16_Symphony_Text2Music.pdf`

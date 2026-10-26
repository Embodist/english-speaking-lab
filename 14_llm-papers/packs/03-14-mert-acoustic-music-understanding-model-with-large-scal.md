---
type: paper-pack
paper_id: "03-14"
stage: 3
title: "MERT: Acoustic Music Understanding Model with Large-Scale Self-supervised Training"
pdf: "/home/user/llm-papers/03_音乐检索理解/PDF/14_MERT.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 03-14 MERT: Acoustic Music Understanding Model with Large-Scale Self-supervised Training

**中文标题**：MERT：大规模自监督训练的声学音乐理解模型

**一句话概括**：提出声学音乐理解模型 MERT，用教师模型在掩蔽语言建模（MLM）风格的声学预训练中提供伪标签，组合 RVQ-VAE 声学教师与 CQT 音乐教师，可扩展到 3.3 亿参数，在 14 项音乐理解任务上取得总体最优分数。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| paradigm | /pˈaɹədˌaɪm/ | 范式（训练通用模型的新范式） | S |
| incorporate | /ɪŋkˈɔːpəɹˌeɪt/ | 纳入（把教师模型融入训练） | A |
| thoroughly | /θˈʌɹəli/ | 彻底地（尚未被充分探索） | A |
| instability | /ɪnstəbˈɪlɪti/ | 不稳定性（预训练过程的不稳定） | A |
| attain | /ɐtˈeɪn/ | 达到（取得最优总体分数） | A |
| generalisable | /dʒˈɛnəɹəlˌaɪzəbəl/ | 可泛化的（能迁移到多种任务） | B |
| distinctive | /dɪstˈɪŋktɪv/ | 独特的（音乐建模特有的挑战） | B |
| tonal | /tˈəʊnəl/ | 调性的（音乐调性特征） | B |
| pitched | /pˈɪtʃt/ | 有音高的（音高特征） | B |
| pseudo | /sˈuːdəʊ/ | 伪的（模型生成的近似标签） | B |
| masked language modelling | /mˈaskt lˈaŋɡwɪdʒ mˈɒdəlɪŋ/ | 掩蔽语言建模（遮盖部分输入让模型预测） | B |
| overcome | /ˌəʊvəkˈʌm/ | 克服（训练不稳定的问题） | B |

### 原句（保留完整句子）

- **paradigm** — “This study has inspired a large number of follow-up models for representation learning (beyond word sequence work, which sets the “pre-training and fine-tuning” learning modeling), having an important impact on the field of NLP. paradigm.”
- **incorporate** — “With the advent of Transformer, OpenAI It incorporates human in the training loop with elaborately developed two initial GPT models, namely GPT-1 \[122\] and designed labeling strategies.”
- **thoroughly** — “We thoroughly comb the literature and team) firstly proposed to model the power-law relationship summarize the key findings, techniques, and methods of of model performance with respective to three major factors, LLMs.”
- **instability** — “Despite the merits, training large model is built on the encoder-decoder architecture \[22\], MoE models may suffer from instability issues due to the which consists of two stacks of Transformer blocks as complex, hard-switching nature of the routing operation. the encoder and decoder, respectively.”
- **attain** — “Furthermore, RNN sequence-to-sequence models have not been able to attain state-of-the-art results in small-data regimes \[37\].”
- **generalisable** — “"for training generalisable models on large-scale data"”
- **distinctive** — “This section mainly introduces the common or distinctive music metrics under three levels of music generation, which does not cover all the studies.”
- **tonal** — “Yang et al. \[333\] divided the objective evaluation of music generation into three categories: the first is the probability measures (as likelihood) without music domain knowledge, the second is the metrics with the help of music theory, such as tonal distance, rhythmic patterns, etc., and the third is the metrics for specific tasks/models.”
- **pitched** — “"tonal and pitched characteristics of music"”
- **pseudo** — “To with a pseudo generated document \[796\].”
- **masked language modelling** — “"in the masked language modelling (MLM) style"”
- **overcome** — “"to overcome the instability in acoustic language"”

## 摘要提示（PDF 文本不可提取）

> 提出声学音乐理解模型 MERT，用教师模型在掩蔽语言建模（MLM）风格的声学预训练中提供伪标签，组合 RVQ-VAE 声学教师与 CQT 音乐教师，可扩展到 3.3 亿参数，在 14 项音乐理解任务上取得总体最优分数。

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

PDF：`/home/user/llm-papers/03_音乐检索理解/PDF/14_MERT.pdf`

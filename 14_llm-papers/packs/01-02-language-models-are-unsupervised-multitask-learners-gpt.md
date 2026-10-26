---
type: paper-pack
paper_id: "01-02"
stage: 1
title: "Language Models are Unsupervised Multitask Learners (GPT-2)"
pdf: "/home/user/llm-papers/01_大模型/PDF/02_GPT2_LanguageModelsUnsupervisedMultitask.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-02 Language Models are Unsupervised Multitask Learners (GPT-2)

**中文标题**：语言模型是无监督的多任务学习者 (GPT-2)

**一句话概括**：证明语言模型在数百万网页构成的新数据集 WebText 上训练后，无需任何显式监督即可学会问答、翻译、摘要等多种任务，且模型容量越大、零样本任务迁移性能越好（呈对数线性提升）。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| baseline | /bˈeɪslaɪn/ | 基线的（用作对比的现有系统） | S |
| conditioned on | /kəndˈɪʃənd ˈɒn/ | 以……为条件（把……作为输入提供给模型） | A |
| supervised learning | /sˈuːpəvˌaɪzd lˈɜːnɪŋ/ | 监督学习（用带标签数据训练） | A |
| demonstrate | /dˈɛmənstɹˌeɪt/ | 证明、展示 | A |
| explicit | /ɛksplˈɪsɪt/ | 显式的、明确的（此处指人工标签） | A |
| summarization | /sˌʌməɹaɪzˈeɪʃən/ | 摘要生成（把长文本压缩成简短摘要的任务） | B |
| approached | /ɐpɹˈəʊtʃt/ | 处理、解决（approach 此处指"着手应对"） | B |
| exceeding | /ɛksˈiːdɪŋ/ | 超过 | B |
| capacity | /kəpˈasɪti/ | 容量、能力（模型的参数量与表达能力） | B |
| zero-shot task transfer | /zˈiəɹəʊʃˈɒt tˈask tɹˈansfɜː/ | 零样本任务迁移（不经训练直接迁移到新任务） | B |

### 原句（保留完整句子）

- **baseline** — “4 E XPERIMENTAL R ESULTS 4.1 E XPERIMENTAL S ETUP To keep the comparison as meaningful as possible, we follow the BERT (Devlin et al., 2019) setup in using the B OOK C ORPUS (Zhu et al., 2015) and English Wikipedia (Devlin et al., 2019) for pretraining baseline models.”
- **conditioned on** — “"When conditioned on a document plus questions"”
- **supervised learning** — “"are typically approached with supervised learning on task-specific datasets"”
- **demonstrate** — “These pre-trained context-aware word representations for learning distributed word representations, which were are very effective as general-purpose semantic features, demonstrated to be very effective across a variety of NLP which have largely raised the performance bar of NLP tasks.”
- **explicit** — “Other objectives for sentence embedding learning include predicting future sentences rather than only neighbors (Gan et al., 2017) and predicting explicit discourse markers (Jernite et al., 2017; Nie et al., 2019).”
- **summarization** — “Self-attention has been used successfully in a variety of tasks including reading comprehension, abstractive summarization, textual entailment and learning task-independent sentence representations \[4, 27, 28, 22\].”
- **approached** — “"are typically approached with supervised learning on task-specific datasets"”
- **exceeding** — “"matching or exceeding the performance of 3 out of 4 baseline systems"”
- **capacity** — “As a result, we decide to remove dropout to further increase our model capacity.”
- **zero-shot task transfer** — “"essential to the success of zero-shot task transfer"”

## Abstract（自动提取）

>  Published as a conference paper at ICLR 2020 ALBERT: A L ITE BERT FOR S ELF - SUPERVISED L EARNING OF L ANGUAGE R EPRESENTATIONS Zhenzhong Lan1 Mingda Chen2∗ Sebastian Goodman1 Kevin Gimpel2 Piyush Sharma1 Radu Soricut1 1 Google Research 2 Toyota Technological Institute at Chicago {lanzhzh, seabass, piyushsharma, rsoricut}@google.com {mchen, kgimpel}@ttic.edu arXiv:1909.11942v6 \[cs.CL\] 9 Feb 2020 A BSTRACT Increasing model size when pretraining natural language representations often results in improved performance on downstream tasks. However, at some point further model increases become harder due to GPU/TPU memory limitations and longer training times. To address these problems, we present two parameterreduction techniques to lower memory consumption and increase the training speed of BERT (Devlin et al., 2019). Comprehensive empirical evidence shows that our proposed methods lead to models that scale much better compared to the original BERT.

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

PDF：`/home/user/llm-papers/01_大模型/PDF/02_GPT2_LanguageModelsUnsupervisedMultitask.pdf`

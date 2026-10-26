---
type: paper-pack
paper_id: "01-37"
stage: 1
title: "Lost in the Middle: How Language Models Use Long Contexts"
pdf: "/home/user/llm-papers/01_大模型/PDF/37_LostInTheMiddle.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-37 Lost in the Middle: How Language Models Use Long Contexts

**中文标题**：迷失在中间：语言模型如何使用长上下文

**一句话概括**：研究发现语言模型对长上下文中部信息的利用明显更差，揭示"迷失在中间"现象，并提供新的长上下文评测协议。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| relatively | /ɹˈɛlətˌɪvli/ | 相对地 | B |
| identifying | /aɪdˈɛntɪfˌaɪɪŋ/ | 识别 | B |
| relevant | /ɹˈɛlɪvənt/ | 相关的（与任务有关的） | B |
| key-value retrieval | /kˈiːvˈaljuː ɹɪtɹˈiːvəl/ | 键值检索（从键值对中查找信息） | B |
| degrade | /dɪɡɹˈeɪd/ | 下降、退化 | B |
| robustly | /ɹəʊbˈʌstli/ | 稳健地 | B |
| in particular | /ˈɪn pətˈɪkjʊlə/ | 特别是 | B |
| occurs | /əkˈɜːz/ | 出现、发生 | B |
| protocols | /pɹˈəʊtəkˌɒlz/ | 方案、标准（此处指评测协议） | B |
| explicitly | /ɛksplˈɪsɪtli/ | 明确地 | B |

### 原句（保留完整句子）

- **relatively** — “Nc Compared with them, we focus on the techniques and L(N ) = , αN ∼ 0.076, Nc ∼ 8.8 × 1013 (1) N methods to develop and use LLMs and provide a relatively Dc αD comprehensive reference to important aspects of LLMs.”
- **identifying** — “"two tasks that require identifying relevant information in their input contexts"”
- **relevant** — “It has achieved excellent performance in parameter size, data and computational resources required evaluations from multiple perspectives including semantics, for training, the relevant technologies employed by the mathematics, reasoning, code, and knowledge.”
- **key-value retrieval** — “"multi-document question answering and key-value retrieval"”
- **degrade** — “A note is that normalization techniques in BPE, such as NFKC \[246\], may degrade the 22. https://huggingface.co/learn/nlp-course/chapter6 tokenization performance \[34, 64, 78\].”
- **robustly** — “Stoyanov, models: A history from BERT to chatgpt,” CoRR, vol. “Roberta: A robustly optimized BERT pretraining abs/2302.09419, 2023. approach,” CoRR, vol. abs/1907.11692, 2019. \[38\] X.”
- **in particular** — “"In particular, we observe that performance is often highest"”
- **occurs** — “"relevant information occurs at the beginning or end"”
- **protocols** — “"provides new evaluation protocols for future long-context language models"”
- **explicitly** — “These abilities might not be mechanism of LLMs is still in need to understand the emer- explicitly exhibited when LLMs perform some specific tasks. gence of certain abilities.”

## 摘要提示（PDF 文本不可提取）

> TITLE: Lost in the Middle: How Language Models Use Long Contexts ABSTRACT: While recent language models have the ability to take long contexts as input, relatively little is known about how well they use longer context. We analyze the performance of language models on two tasks that require identifying relevant information in their input contexts: multi-document question answering and key-value retrieval. We find that performance can degrade significantly when changing the position of relevant information, indicating that current language models do not robustly make use of information in long input contexts. In particular, we observe that performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models. Our analysis provides a better understanding of how language models use their input context and provides new evaluation protocols for future long-context language models.

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

PDF：`/home/user/llm-papers/01_大模型/PDF/37_LostInTheMiddle.pdf`

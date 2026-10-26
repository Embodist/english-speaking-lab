---
type: paper-pack
paper_id: "01-30"
stage: 1
title: "Let's Verify Step by Step"
pdf: "/home/user/llm-papers/01_大模型/PDF/30_LetsVerifyStepByStep_PRM.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-30 Let's Verify Step by Step

**中文标题**：让我们一步步验证

**一句话概括**：对比结果监督与过程监督，证明对每一步推理逐步验证的过程监督显著更优，所训练模型在 MATH 数据集上解出 78% 的问题。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| intermediate | /ˌɪntəmˈiːdiət/ | 中间的 | A |
| efficacy | /ˈɛfɪkəsi/ | 效果、有效性 | A |
| multi-step reasoning | /mˈʌltistˈɛp ɹˈiːzənɪŋ/ | 多步推理（需要多步推导的问题） | B |
| logical mistakes | /lˈɒdʒɪkəl mɪstˈeɪks/ | 逻辑错误 | B |
| reliable | /ɹɪlˈaɪəbəl/ | 可靠的 | B |
| outcome supervision | /ˈaʊtkʌm suːpəvˈɪʒən/ | 结果监督（只对最终结果给反馈） | B |
| process supervision | /pɹˈəʊsɛs suːpəvˈɪʒən/ | 过程监督（对每一步推理给反馈） | B |
| conduct | /kˈɒndʌkt/ | 进行、开展 | B |
| representative subset | /ɹˌɛpɹɪzˈɛntətˌɪv sˈʌbsɛt/ | 代表性子集 | B |
| active learning | /ˈaktɪv lˈɜːnɪŋ/ | 主动学习（挑选最有价值的样本标注） | B |

### 原句（保留完整句子）

- **intermediate** — “To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step.”
- **efficacy** — “Additionally, we show that active learning significantly improves the efficacy of process supervision.”
- **multi-step reasoning** — “These hallucinations (Maynez et al., 2020) are particularly problematic in domains that require multi-step reasoning, since a single logical error is enough to derail a much larger solution.”
- **logical mistakes** — “However, even stateof-the-art models still regularly produce logical mistakes.”
- **reliable** — “To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step.”
- **outcome supervision** — “To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step.”
- **process supervision** — “To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step.”
- **conduct** — “We conduct our own investigation, finding that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset.”
- **representative subset** — “Our process-supervised model solves 78% of problems from a representative subset of the MATH test set.”
- **active learning** — “Additionally, we show that active learning significantly improves the efficacy of process supervision.”

## Abstract（自动提取）

> TITLE: Let's Verify Step by Step ABSTRACT: In recent years, large language models have greatly improved in their ability to perform complex multi-step reasoning. However, even state-of-the-art models still regularly produce logical mistakes. To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step. Given the importance of training reliable models, and given the high cost of human feedback, it is important to carefully compare the both methods. Recent work has already begun this comparison, but many questions still remain. We conduct our own investigation, finding that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset. Our process-supervised model solves 78% of problems from a representative subset of the MATH test set. Additionally, we show that active learning significantly improves the efficacy of process supervision. To support related research, we also release PRM800K, the complete dataset of 800,000 step-level human feedback labels used to train our best reward model.

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

PDF：`/home/user/llm-papers/01_大模型/PDF/30_LetsVerifyStepByStep_PRM.pdf`

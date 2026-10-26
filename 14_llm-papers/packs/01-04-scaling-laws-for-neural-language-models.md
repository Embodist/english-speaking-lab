---
type: paper-pack
paper_id: "01-04"
stage: 1
title: "Scaling Laws for Neural Language Models"
pdf: "/home/user/llm-papers/01_大模型/PDF/04_ScalingLaws_Kaplan.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-04 Scaling Laws for Neural Language Models

**中文标题**：神经语言模型的规模定律

**一句话概括**：系统研究语言模型性能随模型大小、数据量与算力变化的经验规律（幂律关系），并据此指导固定算力预算的最优分配。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| scaling laws | /skˈeɪlɪŋ lˈɔːz/ | 规模定律（性能随规模变化的规律） | A |
| sample-efficient | /sˈampəlɪfˈɪʃənt/ | 样本高效的（用较少数据达到较好效果） | A |
| empirical | /ɛmpˈɪɹɪkəl/ | 经验的、实证的（由实验数据得出） | A |
| compute | /kəmpjˈuːt/ | 算力、计算量 | A |
| convergence | /kənvˈɜːdʒəns/ | 收敛（训练损失趋于平稳不再下降） | A |
| cross-entropy | /kɹˈɒsˈɛntɹəpi/ | 交叉熵（衡量预测分布与真实分布差异的损失） | B |
| power-law | /pˈaʊəlˈɔː/ | 幂律（呈幂函数关系的规律） | B |
| orders of magnitude | /ˈɔːdəz ˈɒv mˈaɡnɪtjˌuːd/ | 数量级（每十倍为一个数量级） | B |
| overfitting | /ˌəʊvəfˈɪtɪŋ/ | 过拟合（模型死记训练数据而泛化变差） | B |
| allocation | /ˌaləkˈeɪʃən/ | 分配（对算力预算的最优配置） | B |

### 原句（保留完整句子）

- **scaling laws** — “1.2 Summary of Scaling Laws The test loss of a Transformer trained to autoregressively model language can be predicted using a power-law when performance is limited by only either the number of non-embedding parameters N , the dataset size D, or the optimally allocated compute budget Cmin (see Figure 1): 1.”
- **sample-efficient** — “(Section 3.2.2) Sample efficiency: Large models are more sample-efficient than small models, reaching the same level of performance with fewer optimization steps (Figure 2) and using fewer data points (Figure 4).”
- **empirical** — “See Figure 13 for comparison to the purely empirical data.”
- **compute** — “The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of magnitude.”
- **convergence** — “Convergence is inefficient: When working within a fixed compute budget C but without any other restrictions on the model size N or available data D, we attain optimal performance by training very large models and stopping significantly short of convergence (see Figure 3).”
- **cross-entropy** — “We optimize the autoregressive log-likelihood (i.e. cross-entropy loss) averaged over a 1024-token context, which is also our principal performance metric.”
- **power-law** — “The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of magnitude.”
- **orders of magnitude** — “The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of magnitude.”
- **overfitting** — “Simple equations govern the dependence of overfitting on model/dataset size and the dependence of training speed on model size.”
- **allocation** — “These relationships allow us to determine the optimal allocation of a fixed compute budget.”

## Abstract（自动提取）

> TITLE: Scaling Laws for Neural Language Models ABSTRACT: We study empirical scaling laws for language model performance on the cross-entropy loss. The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of magnitude. Other architectural details such as network width or depth have minimal effects within a wide range. Simple equations govern the dependence of overfitting on model/dataset size and the dependence of training speed on model size. These relationships allow us to determine the optimal allocation of a fixed compute budget. Larger models are significantly more sample-efficient, such that optimally compute-efficient training involves training very large models on a relatively modest amount of data and stopping significantly before convergence.

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

PDF：`/home/user/llm-papers/01_大模型/PDF/04_ScalingLaws_Kaplan.pdf`

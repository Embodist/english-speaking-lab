---
type: paper-pack
paper_id: "01-35"
stage: 1
title: "DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model"
pdf: "/home/user/llm-papers/01_大模型/PDF/35_DeepSeekV2.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-35 DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model

**中文标题**：DeepSeek-V2：强大、经济且高效的专家混合语言模型

**一句话概括**：发布 DeepSeek-V2，用 MLA 把 KV 缓存压缩进潜在向量、用 DeepSeekMoE 稀疏计算，训练更省、推理更快，性能超越 DeepSeek 67B。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| corpus | /kˈɔːpəs/ | 语料库 | S |
| latent | /lˈeɪtənt/ | 隐式的（压缩后的潜在表示） | S |
| sparse | /spˈɑːs/ | 稀疏的（只激活少量参数） | S |
| innovative | /ˈɪnəvˌeɪtɪv/ | 创新的 | A |
| economical | /ˌiːkənˈɒmɪkəl/ | 经济的（省成本的） | B |
| characterized by | /kˈaɹɪktəɹˌaɪzd bˈaɪ/ | 以……为特征 | B |
| activated | /ˈaktɪvˌeɪtɪd/ | 激活的（实际参与计算的参数） | B |
| compressing | /kəmpɹˈɛsɪŋ/ | 压缩 | B |
| boosts | /bˈuːsts/ | 提升、大幅提高 | B |
| top-tier | /tˈɒptˈiə/ | 顶级的 | B |

### 原句（保留完整句子）

- **corpus** — “We also trained it in a semi-supervised setting, using the larger high-confidence and BerkleyParser corpora from with approximately 17M sentences \[37\].”
- **latent** — “Self-training PCFG grammars with latent annotations across languages.”
- **sparse** — “Mixdeployment life-cycle, which aims to effectively reduce the tral is a kind of sparse Mixture-of-Experts (SMoE) model potential risks of using the models.”
- **innovative** — “Sun, “JEC-QA: A legal-domain question answer- books and movies: Towards story-like visual explaing dataset,” in The Thirty-Fourth AAAI Conference nations by watching movies and reading books,” in on Artificial Intelligence, AAAI 2020, The Thirty-Second 2015 IEEE International Conference on Computer Vision, Innovative Applications of Artificial Intelligence Confer- ICCV 2015, Santiago, Chile, December 7-13, 2015.”
- **economical** — “11: An illustration of instance formatting and three different methods for constructing the instruction-formatted instances. they mainly come from public NLP datasets, either lack- economical way to generate large-scale instruction data for ing instruction diversity or mismatching with real human LLMs.”
- **characterized by** — “"characterized by economical training and efficient inference"”
- **activated** — “"of which 21B are activated for each token"”
- **compressing** — “"through significantly compressing the Key-Value (KV) cache into a latent vector"”
- **boosts** — “"and boosts the maximum generation throughput to 5.76 times"”
- **top-tier** — “A recent study \[909\] has found quate for evaluating top-tier LLMs or complex tasks.”

## 摘要提示（PDF 文本不可提取）

> TITLE: DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model ABSTRACT: We present DeepSeek-V2, a strong Mixture-of-Experts (MoE) language model characterized by economical training and efficient inference. It comprises 236B total parameters, of which 21B are activated for each token, and supports a context length of 128K tokens. DeepSeek-V2 adopts innovative architectures including Multi-head Latent Attention (MLA) and DeepSeekMoE. MLA guarantees efficient inference through significantly compressing the Key-Value (KV) cache into a latent vector, while DeepSeekMoE enables training strong models at an economical cost through sparse computation. Compared with DeepSeek 67B, DeepSeek-V2 achieves significantly stronger performance, and meanwhile saves 42.5% of training costs, reduces the KV cache by 93.3%, and boosts the maximum generation throughput to 5.76 times. We pretrain DeepSeek-V2 on a high-quality and multi-source corpus consisting of 8.1T tokens, and further perform Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) to fully unlock its potential. Evaluation results show that, even with only 21B activated parameters, DeepSeek-V2 and its chat versions still achieve top-tier performance among open-source models.

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

PDF：`/home/user/llm-papers/01_大模型/PDF/35_DeepSeekV2.pdf`

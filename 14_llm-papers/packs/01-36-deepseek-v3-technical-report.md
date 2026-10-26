---
type: paper-pack
paper_id: "01-36"
stage: 1
title: "DeepSeek-V3 Technical Report"
pdf: "/home/user/llm-papers/01_大模型/PDF/36_DeepSeekV3.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-36 DeepSeek-V3 Technical Report

**中文标题**：DeepSeek-V3 技术报告

**一句话概括**：报告 671B 参数的 MoE 模型 DeepSeek-V3：采用无辅助损失负载均衡与多词元预测目标，性能比肩顶级闭源模型，且训练稳定、成本低。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| comprehensive | /kˌɒmpɹɪhˈɛnsɪv/ | 全面的 | S |
| thoroughly | /θˈʌɹəli/ | 彻底地 | A |
| harness | /hˈɑːnɪs/ | 发挥、充分利用 | A |
| cost-effective | /kˈɒstɪfˈɛktɪv/ | 成本高效的 | B |
| pioneers | /paɪənˈiəz/ | 开创、率先采用 | B |
| auxiliary-loss-free | /ɔːksˈɪliəɹilˈɒsfɹˈiː/ | 无辅助损失的（不额外添加损失项） | B |
| load balancing | /lˈəʊd bˈalənsɪŋ/ | 负载均衡（让各专家负载均匀） | B |
| multi-token prediction | /mˈʌltitˈəʊkən pɹɪdˈɪkʃən/ | 多词元预测（一次预测多个词元） | B |
| comparable to | /kˈɒmpəɹəbəl tˈuː/ | 与……相当 | B |
| irrecoverable | /ɪɹɪkˈʌvəɹəbəl/ | 不可恢复的 | B |

### 原句（保留完整句子）

- **comprehensive** — “Nc Compared with them, we focus on the techniques and L(N ) = , αN ∼ 0.076, Nc ∼ 8.8 × 1013 (1) N methods to develop and use LLMs and provide a relatively Dc αD comprehensive reference to important aspects of LLMs.”
- **thoroughly** — “We thoroughly comb the literature and team) firstly proposed to model the power-law relationship summarize the key findings, techniques, and methods of of model performance with respective to three major factors, LLMs.”
- **harness** — “This feature can be harnessed through specific language.”
- **cost-effective** — “It currently supports over 13,000 models across • DeepSpeed \[74\] is a deep learning optimization library three popular model architectures, such as LLaMA \[57\], (compatible with PyTorch) developed by Microsoft, which Mistral \[137\], and OPT \[90\]. has been used to train a number of LLMs, such as MT• DeepSpeed-Chat \[210\] is a fast, cost-effective, and NLG \[113\] and BLOOM \[78\].”
- **pioneers** — “"DeepSeek-V3 pioneers an auxiliary-loss-free strategy for load balancing"”
- **auxiliary-loss-free** — “"pioneers an auxiliary-loss-free strategy for load balancing"”
- **load balancing** — “"an auxiliary-loss-free strategy for load balancing"”
- **multi-token prediction** — “"sets a multi-token prediction training objective for stronger performance"”
- **comparable to** — “"achieves performance comparable to leading closed-source models"”
- **irrecoverable** — “"we did not experience any irrecoverable loss spikes"”

## 摘要提示（PDF 文本不可提取）

> TITLE: DeepSeek-V3 Technical Report ABSTRACT: We present DeepSeek-V3, a strong Mixture-of-Experts (MoE) language model with 671B total parameters with 37B activated for each token. To achieve efficient inference and cost-effective training, DeepSeek-V3 adopts Multi-head Latent Attention (MLA) and DeepSeekMoE architectures, which were thoroughly validated in DeepSeek-V2. Furthermore, DeepSeek-V3 pioneers an auxiliary-loss-free strategy for load balancing and sets a multi-token prediction training objective for stronger performance. We pre-train DeepSeek-V3 on 14.8 trillion diverse and high-quality tokens, followed by Supervised Fine-Tuning and Reinforcement Learning stages to fully harness its capabilities. Comprehensive evaluations reveal that DeepSeek-V3 outperforms other open-source models and achieves performance comparable to leading closed-source models. Despite its excellent performance, DeepSeek-V3 requires only 2.788M H800 GPU hours for its full training. In addition, its training process is remarkably stable. Throughout the entire training process, we did not experience any irrecoverable loss spikes or perform any rollbacks. The model checkpoints are available at https://github.com/deepseek-ai/DeepSeek-V3.

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

PDF：`/home/user/llm-papers/01_大模型/PDF/36_DeepSeekV3.pdf`

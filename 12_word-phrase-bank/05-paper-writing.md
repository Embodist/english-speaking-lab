---
type: word-bank
title: 论文写作
tags: [library/word-bank, skill/writing, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# 论文写作（50）

“说”列是你在组会/面试中讲这篇论文时的说法；“写”列是论文里的正式写法。**先说顺，再落笔。**

## 摘要 Abstract

| 级别 | 句式 | 中文 | 说（口头） | 写（论文） | 备注 |
|---|---|---|---|---|---|
| S | This paper presents … | 本文提出 | This paper presents a two-stage retrieval pipeline. | This paper presents a two-stage retrieval pipeline for enterprise search. | 开门见山 |
| S | We propose … | 我们提出 | We propose a reranking method for noisy queries. | We propose a lightweight reranker for noisy queries. | 最常用 |
| A | We introduce … | 我们引入 | We introduce a new evaluation protocol. | We introduce a new evaluation protocol for long documents. | 强调新东西 |
| S | We evaluate … | 我们评测 | We evaluate the method on three datasets. | We evaluate the method on three public datasets. | 说清数据 |
| S | Results show that … | 结果表明 | Results show that reranking helps. | Results show that reranking improves recall by 4 points. | 带指标 |

## 引言 Introduction

| 级别 | 句式 | 中文 | 说（口头） | 写（论文） | 备注 |
|---|---|---|---|---|---|
| A | Recent work has … | 近期工作已经 | Recent work has improved retrieval quality. | Recent work has improved retrieval quality on short queries. | 背景 |
| S | However, … | 然而 | However, latency remains a problem. | However, these methods add significant latency. | 转折 |
| S | In this paper, we … | 本文中我们 | In this paper, we focus on latency. | In this paper, we focus on the latency–accuracy trade-off. | 定位 |
| S | Our key insight is … | 核心洞察是 | Our key insight is that reranking a smaller set is enough. | Our key insight is that reranking a smaller candidate set is sufficient. | 贡献核心 |
| S | The main contributions are … | 主要贡献是 | The main contributions are a method and an evaluation. | The main contributions are: (1) a method, (2) an evaluation protocol. | 列表 |
| S | We address … | 我们解决 | We address the problem of noisy retrieval. | We address the problem of noisy retrieval in enterprise search. | 问题 |
| A | To this end, … | 为此 | To this end, we add a reranking stage. | To this end, we introduce a reranking stage. | 连接 |
| A | Motivated by …, we … | 受……启发 | Motivated by this gap, we design a small reranker. | Motivated by this gap, we design a parameter-efficient reranker. | 动机 |

## 方法 Method

| 级别 | 句式 | 中文 | 说（口头） | 写（论文） | 备注 |
|---|---|---|---|---|---|
| S | We formulate … as … | 将……形式化 | We formulate retrieval as a ranking problem. | We formulate retrieval as a ranking problem. | 定义 |
| A | We denote … as … | 将……记作 | We denote the candidate set as C. | We denote the candidate set as C. | 符号 |
| S | The pipeline consists of … | 流程包括 | The pipeline consists of retrieval, reranking, and generation. | The pipeline consists of three stages: retrieval, reranking, and generation. | 结构 |
| A | We encode … | 编码 | We encode the query with a frozen model. | We encode the query with a frozen encoder. | 模型 |
| A | We compute … | 计算 | We compute similarity scores for each candidate. | We compute similarity scores for each candidate. | 步骤 |
| A | We optimize … | 优化 | We optimize the model with a contrastive loss. | We optimize the model with a contrastive loss. | 训练 |
| A | We apply … to … | 将……应用于 | We apply a filter before reranking. | We apply a metadata filter before reranking. | 细节 |
| S | The model takes … as input. | 模型输入是 | The model takes the query and context as input. | The model takes the query and retrieved context as input. | 输入 |

## 实验 Experiments

| 级别 | 句式 | 中文 | 说（口头） | 写（论文） | 备注 |
|---|---|---|---|---|---|
| S | We conduct experiments on … | 在……上实验 | We conduct experiments on two datasets. | We conduct experiments on two public datasets. | 数据 |
| S | We compare against … | 与……比较 | We compare against a keyword baseline. | We compare against BM25 and a dense retriever. | baseline |
| A | We use the following metrics: … | 使用以下指标 | We report recall and answer accuracy. | We use the following metrics: Recall@k and answer accuracy. | 指标 |
| A | We report … | 报告 | We report p50 and p95 latency. | We report latency at p50 and p95. | 结果 |
| A | We ablate … | 做消融 | We ablate the reranker. | We ablate the reranker to measure its contribution. | 消融 |
| A | We keep the setting fixed. | 保持设置固定 | We keep the setting fixed across runs. | We keep all other settings fixed. | 可复现 |
| A | We use the same compute budget. | 使用相同算力 | We use the same compute budget for both methods. | Both methods are evaluated under the same compute budget. | 公平 |
| A | We run three seeds. | 跑三个随机种子 | We run three seeds and report the mean. | We run three random seeds and report the mean and standard deviation. | 稳定性 |

## 结果 Results

| 级别 | 句式 | 中文 | 说（口头） | 写（论文） | 备注 |
|---|---|---|---|---|---|
| S | As shown in Table 1, … | 如表 1 所示 | As shown in Table 1, reranking helps. | As shown in Table 1, reranking improves recall. | 引用 |
| S | Our method outperforms … | 我们的方法优于 | Our method outperforms the baseline. | Our method outperforms the baseline by 3.2 points. | 结论 |
| A | We achieve … | 我们达到 | We achieve 82% accuracy. | We achieve 82.1% accuracy on the test set. | 指标 |
| A | The improvement is … | 提升是 | The improvement is consistent across datasets. | The improvement is consistent across both datasets. | 稳健 |
| S | We observe … | 我们观察到 | We observe a latency–accuracy trade-off. | We observe a clear latency–accuracy trade-off. | 发现 |
| A | This suggests … | 这表明 | This suggests that retrieval is the bottleneck. | This suggests that retrieval quality is the bottleneck. | 解释 |
| A | The gain is within noise. | 提升在噪声范围内 | The gain is within noise. | The gain is small and within run-to-run noise. | 谨慎 |

## 讨论与局限 Discussion / Limitations

| 级别 | 句式 | 中文 | 说（口头） | 写（论文） | 备注 |
|---|---|---|---|---|---|
| S | One limitation is … | 一个局限是 | One limitation is the small dataset. | One limitation is the limited size of the evaluation set. | 诚实 |
| S | We do not … | 我们没有 | We do not evaluate multilingual data. | We do not evaluate multilingual or low-resource settings. | 边界 |
| A | This may not generalize to … | 可能无法泛化到 | This may not generalize to other domains. | This may not generalize to other domains without retraining. | 泛化 |
| A | The results are limited to … | 结果仅限于 | The results are limited to English. | The results are limited to English enterprise documents. | 范围 |
| A | A potential risk is … | 潜在风险是 | A potential risk is prompt injection. | A potential risk is prompt injection from retrieved documents. | 风险 |
| A | We leave … for future work. | 留给未来工作 | We leave multilingual evaluation for future work. | We leave multilingual evaluation for future work. | 未来 |

## 相关工作与结论 Related Work / Conclusion

| 级别 | 句式 | 中文 | 说（口头） | 写（论文） | 备注 |
|---|---|---|---|---|---|
| A | Prior work has explored … | 已有工作探索了 | Prior work has explored dense retrieval. | Prior work has explored dense retrieval for open-domain QA. | 背景 |
| A | Unlike prior work, … | 与已有工作不同 | Unlike prior work, we focus on latency. | Unlike prior work, we optimize for latency under a fixed budget. | 对比 |
| A | Our approach differs in … | 我们的方法不同在于 | Our approach differs in the reranking stage. | Our approach differs in how candidates are reranked. | 差异 |
| A | We build on … | 我们基于 | We build on a standard retriever. | We build on a standard dense retriever. | 继承 |
| B | Existing methods … | 现有方法 | Existing methods require large models. | Existing methods require large models and extensive tuning. | 综述 |
| S | We conclude that … | 我们得出结论 | We conclude that reranking is worth the latency. | We conclude that reranking is worth the additional latency. | 结论 |
| A | Future work includes … | 未来工作包括 | Future work includes multilingual evaluation. | Future work includes multilingual evaluation and online testing. | 展望 |
| B | We believe … | 我们认为 | We believe this generalizes to other domains. | We believe this approach generalizes to other retrieval tasks. | 谨慎断言 |

## 写作风格

1. **先结论后解释**：一句话说贡献，再展开。
2. **用 hedging**：`may`, `suggest`, `indicate`, `we observe`，避免 `proves`。
3. **不夸大**：小提升就写 small；在噪声内就明说。
4. **一段一个观点**：每段第一句是主题句。
5. **定义术语**：第一次出现的缩写写全称。
6. **主动语态优先**：`We propose …` 比 `It is proposed that …` 清楚。

## 练习

- [ ] 用摘要句式写一段 100 词摘要（你的项目/一篇论文）
- [ ] 用局限句式写 3 句诚实的 limitation
- [ ] 把摘要口头讲 60 秒并录音

## 相关

- [[12_word-phrase-bank/_index|词与短语库]]
- [[12_word-phrase-bank/04-paper-reading|论文阅读]]
- [[06_interview/project-stories|项目故事]]
- [[LEARNING-PATH|学习路径]]

---
type: word-bank
title: 论文阅读
tags: [library/word-bank, skill/speaking, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# 论文阅读（50）

目标：30 分钟读懂一篇 AI 论文的骨架，并能用英文口头总结。**先说，再写笔记，最后回到原文。**

> 你整理的 168 篇 LLM/多模态/音乐/世界模型论文词汇，见 [[14_llm-papers/_index|LLM 论文阅读与词汇]]。

## 30 分钟阅读流程

1. **标题 + 摘要（5 min）**：问题、方法、结果各一句。
2. **图表（5 min）**：主结果图、实验设置表。
3. **引言最后两段（5 min）**：贡献列表。
4. **方法（7 min）**：输入、模型、训练目标。
5. **实验（5 min）**：baseline、指标、消融。
6. **局限 + 结论（3 min）**：作者承认什么。
7. **口头总结 60 秒 + 写 3 句笔记**。

## 核心术语

| 级别 | 术语 | 中文 | 说（口头总结） | 写（阅读笔记） | 读（论文常见用法） |
|---|---|---|---|---|---|
| S | abstract | 摘要 | The abstract claims a 5-point gain. | The abstract summarizes the main result. | as shown in the abstract |
| A | introduction | 引言 | The introduction motivates the problem. | The introduction lists three contributions. | in the introduction |
| A | related work | 相关工作 | The related work compares prior methods. | Prior work is discussed in Section 2. | related work |
| S | method | 方法 | The method has two stages. | The method combines retrieval and reranking. | the proposed method |
| A | experiment | 实验 | They ran three experiments. | The experiments cover two datasets. | experimental setup |
| S | results | 结果 | The results show a clear improvement. | The results are reported in Table 2. | main results |
| B | discussion | 讨论 | The discussion focuses on failure cases. | The discussion highlights limitations. | in the discussion |
| S | conclusion | 结论 | The conclusion is that reranking helps. | The conclusion summarizes the findings. | in the conclusion |
| S | contribution | 贡献 | The main contribution is the training objective. | The paper makes three contributions. | main contribution |
| A | novelty | 新颖性 | The novelty is the cross-modal loss. | The novelty is limited. | novelty of the approach |
| S | baseline | 基线 | They compare against two baselines. | The baseline is a keyword retriever. | strong baseline |
| A | benchmark | 基准测试 | They evaluate on a public benchmark. | The benchmark has three tasks. | on a benchmark |
| S | dataset | 数据集 | The dataset has 10k examples. | The dataset is split into train and test. | on the dataset |
| A | evaluation metric | 评测指标 | They report recall and F1. | The main metric is answer accuracy. | evaluation metric |
| A | ablation study | 消融实验 | The ablation shows which part matters. | The ablation removes the reranker. | ablation study |
| A | hyperparameter | 超参数 | They tune the learning rate. | Hyperparameters are listed in the appendix. | hyperparameter setting |
| A | state of the art (SOTA) | 最先进水平 | They claim SOTA on two tasks. | The method outperforms SOTA. | achieve SOTA |
| B | empirical | 经验的 | The evidence is empirical. | Empirical results support the claim. | empirical study |
| B | theoretical | 理论的 | The paper is mostly theoretical. | The theoretical analysis is limited. | theoretical analysis |
| B | qualitative | 定性的 | They include qualitative examples. | The qualitative analysis is convincing. | qualitative results |
| A | quantitative | 定量的 | The quantitative results are stronger. | Quantitative results are in Table 3. | quantitative evaluation |
| A | robustness | 鲁棒性 | They test robustness to noise. | Robustness is evaluated under distribution shift. | robustness |
| A | generalization | 泛化 | The model generalizes to a new domain. | Generalization is limited to English. | generalization |
| A | scalability | 可扩展性 | Scalability is a concern at inference time. | The paper does not analyze scalability. | scalability |
| S | limitation | 局限 | One limitation is the small dataset. | The limitations are discussed in Section 6. | a key limitation |
| S | assumption | 假设 | The method assumes clean input. | The assumption may not hold in production. | underlying assumption |
| A | hypothesis | 假设 | The hypothesis is that reranking helps. | The hypothesis is tested in the ablation. | test a hypothesis |
| S | reproduce | 复现 | The results are hard to reproduce. | We reproduced the baseline. | reproduce the results |
| B | replicate | 重复验证 | Another paper replicated the finding. | The study was replicated on a new dataset. | replicate the experiment |
| A | error analysis | 错误分析 | The error analysis shows retrieval failures. | We include an error analysis. | error analysis |
| A | case study | 案例研究 | The case study is on enterprise search. | A case study illustrates the pipeline. | case study |
| A | zero-shot | 零样本 | The model works zero-shot. | Zero-shot performance is lower. | zero-shot setting |
| A | few-shot | 少样本 | Few-shot prompting improves accuracy. | They use a few-shot setup. | few-shot examples |
| S | fine-tuning | 微调 | They fine-tune on domain data. | Fine-tuning improves the target task. | supervised fine-tuning |
| S | inference | 推理 | Inference cost is high. | Inference latency is reported. | inference time |
| A | compute budget | 算力预算 | The compute budget is not reported. | They use a fixed compute budget. | under the same budget |
| S | token | token | The context is limited to 8k tokens. | Token-level accuracy is reported. | token budget |
| B | corpus | 语料库 | The corpus contains legal documents. | The corpus is filtered for quality. | training corpus |
| B | annotation | 标注 | The annotation was done by experts. | Annotation guidelines are in the appendix. | manual annotation |
| A | ground truth | 真实标注 | The ground truth is human-written. | We compare against ground truth. | ground-truth labels |
| B | statistical significance | 统计显著性 | The gain is statistically significant. | We report statistical significance. | significance test |
| B | confidence interval | 置信区间 | The confidence interval is wide. | The 95% confidence interval is reported. | confidence interval |
| A | precision | 精确率 | Precision improved by two points. | We report precision and recall. | precision at k |
| S | recall | 召回率 | Recall went up, but precision dropped. | Recall at k is the main metric. | recall at k |
| A | F1 score | F1 分数 | The F1 score is 0.82. | The F1 score is reported in Table 1. | macro F1 |
| A | human evaluation | 人工评测 | They ran a human evaluation. | Human evaluation was done by three annotators. | human evaluation |
| B | rubric | 评分标准 | The rubric has five dimensions. | Annotators followed a rubric. | evaluation rubric |
| B | qualitative analysis | 定性分析 | The qualitative analysis explains the failures. | We add a qualitative analysis. | qualitative analysis |
| B | appendix | 附录 | The details are in the appendix. | Hyperparameters are in the appendix. | see Appendix A |
| A | figure / table | 图 / 表 | Figure 2 shows the pipeline. | Table 3 reports the ablation. | as shown in Figure 2 |

## 口语句式（15）

| 用途 | 句式 |
|---|---|
| 问题 | `The paper addresses the problem of …` |
| 方法 | `The authors propose …` |
| 核心思想 | `The key idea is to …` |
| 贡献 | `The main contribution is …` |
| 继承 | `The method builds on …` |
| 对比 | `Unlike prior work, this approach …` |
| 实验 | `They evaluate on …` |
| 结果 | `The results show that …` |
| 消融 | `The ablation shows that …` |
| 提升 | `The method improves … by …` |
| 质疑 | `The improvement is small and may be within the noise.` |
| 局限 | `One limitation is that …` |
| 未解决 | `The paper does not address …` |
| 未来工作 | `Future work includes …` |
| 你的判断 | `I’m not fully convinced by …, because …` |

## 60 秒总结模板

> The paper addresses [problem]. The authors propose [method]. The key idea is [idea]. They evaluate on [dataset] using [metric]. The results show [result]. One limitation is [limitation]. My main question is [question].

## 练习

- [ ] 每天读 1 篇摘要，用 3 句口头总结
- [ ] 选 1 篇方法论文，写 5 句阅读笔记
- [ ] 用上面的模板录 60 秒

## 相关

- [[12_word-phrase-bank/_index|词与短语库]]
- [[12_word-phrase-bank/05-paper-writing|论文写作]]
- [[12_word-phrase-bank/06-ai-llm-terms|AI / LLM 术语]]
- [[LEARNING-PATH|学习路径]]

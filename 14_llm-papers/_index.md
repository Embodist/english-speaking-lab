---
type: hub
title: LLM 论文阅读与词汇
tags: [hub, topic/paper, skill/reading]
created: 2026-10-24
updated: 2026-10-24
---

# LLM 论文阅读与词汇

> 来源：`~/llm-papers`（168 篇 PDF + 你整理的词汇手册）。本目录把词汇重新组织成：**核心学术语言 → 领域术语 → 分阶段逐篇词表 → Anki CSV → 阅读流程**。

## 数据概览

| 项目 | 数量 |
|---|---|
| 论文 | 168 篇（阶段 0–6） |
| 逐篇词条 | 1,941 |
| 去重词条 | 1,282 |
| 核心学术词/搭配 | 118（A1–A4） |
| 领域术语 | 128（B1–B6） |
| 高频级别 | S 44 · A 287 · B 951 |
| **10k 词库** | **10,127 条（含 10,110 条论文原句）** |
| 阅读包 | 168 篇 |
| 领域短语 | 459 条 |

## 先学什么

1. **核心学术语言**：[[14_llm-papers/core-academic-language|118 个学术动词/名词/形容词/搭配]]。先把“提出、证明、评估、局限”这套骨架说顺。
2. **高频词 S/A**：[[14_llm-papers/top-words|跨论文高频词]]。S 级 44 个必须脱口而出；A 级 287 个以认识为主。
3. **领域术语**：[[14_llm-papers/domain-terms|128 个 LLM/多模态/音乐/世界模型术语]]。同一批词会在几十篇 abstract 里反复出现。
4. **逐篇词表**：按阶段读论文时再看，不要提前背 B 级长尾词。

> 顺序背后的逻辑：**先用核心学术语言看懂 abstract，再用领域术语降低阅读阻力，最后逐篇补长尾词。**

## 10k 词库与每日计划

- **10k 词库**：[[14_llm-papers/vocabulary-10k/_index|10,127 条论文词汇]]，按 1–1000、1001–2000… 分频段，每条保留论文原句。
- **12 周阅读计划**：[[14_llm-papers/reading-plan|每天 45 分钟 + 每周 3 篇]]。
- **逐篇阅读包**：[[14_llm-papers/packs/_index|168 篇阅读包]]，每篇 8–12 个目标词 + 原句 + 摘要 + 5 个理解问题。
- **领域短语**：[[14_llm-papers/vocabulary-10k/domain-phrases|459 条多词术语]]。

## 分阶段词表

| 阶段 | 主题 | 论文 | 词条 | 入口 |
|---|---|---|---|---|
| 0 | 总览与综述 | 7 | 84 | [[14_llm-papers/stage-00-surveys\|阶段 0]] |
| 1 | 大模型 LLM | 38 | 381 | [[14_llm-papers/stage-01-llm\|阶段 1]] |
| 2 | 多模态 | 57 | 691 | [[14_llm-papers/stage-02-multimodal\|阶段 2]] |
| 3 | 音乐检索与理解 | 17 | 199 | [[14_llm-papers/stage-03-music-retrieval\|阶段 3]] |
| 4 | 音乐生成 | 20 | 240 | [[14_llm-papers/stage-04-music-generation\|阶段 4]] |
| 5 | 世界模型 | 26 | 310 | [[14_llm-papers/stage-05-world-models\|阶段 5]] |
| 6 | 强化学习基础 | 3 | 36 | [[14_llm-papers/stage-06-rl\|阶段 6]] |

## 每天怎么用

1. **读前 2 分钟**：扫本篇词表，挑 5 个 S/A 词，遮住中文说词义。
2. **读 abstract**：不要逐词查；只标记 3–5 个真正挡路的词。
3. **读后 10 分钟**：遮住中文用 abstract 片段自测；用 5 个词说 60 秒总结；写 3 句 abstract 风格句子。
4. **记入 Anki**：只加 S/A，B 级留在逐篇词表里。

完整流程见 [[14_llm-papers/reading-workflow|阅读与词汇流程]]。

## Anki / CSV

| 文件 | 内容 | 建议牌组 |
|---|---|---|
| `14_llm-papers/core-vocabulary.csv` | 118 核心学术词 + 128 领域术语 | Core Academic |
| `14_llm-papers/vocabulary-dedup.csv` | 1,282 去重词（含 freq/level） | Paper Words |
| `14_llm-papers/vocabulary.csv` | 1,941 逐篇词条（保留论文语境） | Paper Context（可选） |
| `14_llm-papers/vocabulary-10k/anki-01.csv` … `anki-06.csv` | 10,127 条 10k 词库 | 10k Paper Vocabulary（分批） |

导入字段和步骤见 [[14_llm-papers/anki-import|论文词汇 Anki 导入]]；建议先导入 `core-vocabulary.csv`，再导入 `vocabulary-dedup.csv`。通用说明见 [[08_sentence-library/anki-import-guide|Anki 导入指南]]。

## 来源与边界

- 原始词汇：`~/llm-papers/words/论文阅读词汇手册.md`、`阶段5_世界模型_论文词汇.md`
- 原始论文清单：[[14_llm-papers/paper-list|论文阅读清单（副本）]]
- PDF 原文件：`~/llm-papers/<阶段>/PDF/`（未复制进仓库，体积约 1.1 GB）
- 技术描述与指标以论文原文为准；这里是**语言学习整理**，不替代论文阅读。

## 相关

- [[14_llm-papers/reading-workflow|阅读与词汇流程]]
- [[14_llm-papers/top-words|高频词 S/A]]
- [[14_llm-papers/core-academic-language|核心学术语言]]
- [[14_llm-papers/domain-terms|领域术语]]
- [[12_word-phrase-bank/04-paper-reading|论文阅读句式]]
- [[12_word-phrase-bank/05-paper-writing|论文写作句式]]
- [[10_templates/paper-note|论文笔记模板]]
- [[LEARNING-PATH|学习路径]]

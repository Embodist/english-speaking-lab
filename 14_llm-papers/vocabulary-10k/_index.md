---
type: hub
title: 论文 10k 词库
tags: [library/word-bank, skill/reading]
created: 2026-10-26
updated: 2026-10-26
---

# 论文 10k 词库

> 从 `~/llm-papers` 的 169 篇 PDF 和你的词汇总结中抽取、去重、分级。
> 目标不是一次背完，而是建立一个**可检索、带原句、可分频段**的长期词库。

## 规模

| 项目 | 数量 |
|---|---|
| 总词条 | **10,127** |
| 带论文原句 | 10,045 |
| 带中文释义 | 8,355 |
| 带英文释义 | 7,058 |
| 领域短语 | 459 |
| 来源论文 | 168 |
| 可提取文本的 PDF | 111（57 篇疑似扫描版，见阅读包提示） |

## 分频段词典

| 段 | 内容 | 建议 |
|---|---|---|
| [[14_llm-papers/vocabulary-10k/dictionary-01-1-1000\|1–1000]] | 最常用学术/技术词 | 先扫一遍，标记已会 |
| [[14_llm-papers/vocabulary-10k/dictionary-02-1001-2000\|1001–2000]] | 高频学术词 | 每天 25 个 |
| [[14_llm-papers/vocabulary-10k/dictionary-03-2001-3000\|2001–3000]] | 中高频 | 配合阅读包 |
| [[14_llm-papers/vocabulary-10k/dictionary-04-3001-4000\|3001–4000]] | 进阶 | CET6/TOEFL 重点 |
| [[14_llm-papers/vocabulary-10k/dictionary-05-4001-5000\|4001–5000]] | 进阶 | 同上 |
| [[14_llm-papers/vocabulary-10k/dictionary-06-5001-6000\|5001–6000]] | 低频/专业 | 按论文主题 |
| [[14_llm-papers/vocabulary-10k/dictionary-07-6001-7000\|6001–7000]] | 低频/专业 | 按论文主题 |
| [[14_llm-papers/vocabulary-10k/dictionary-08-7001-8000\|7001–8000]] | 长尾 | 只在原文遇到时记 |
| [[14_llm-papers/vocabulary-10k/dictionary-09-8001-9000\|8001–9000]] | 长尾 | 同上 |
| [[14_llm-papers/vocabulary-10k/dictionary-10-9001-10000\|9001–10000]] | 长尾 | 同上 |
| [[14_llm-papers/vocabulary-10k/dictionary-11-10001-10127\|10001–10127]] | 补充术语 | 按需 |

## 原始数据

- `master.csv`：10,127 行，含 rank、音标、中文、英文释义、标签、BNC/COCA、论文频次、原句、论文 ID。
- `anki-01.csv` … `anki-06.csv`：按 2,000 条分组的 Anki 导入文件。
- [[14_llm-papers/vocabulary-10k/domain-phrases|领域短语]]：459 条多词术语，保留原句。

## 怎么用

- **30 天启动**：[[14_llm-papers/vocabulary-10k/30-day-plan|每天 25 个，共 750 词]]。

1. **先测已会**：扫 1–1000，把已经掌握的词划掉，不重复背。
2. **每天 20–30 个**：优先 `cet6`、`toefl`、`ielts`、`gre` 标签；每个词读原句，不要只看中文。
3. **按论文使用**：读某篇论文时，打开对应 [[14_llm-papers/packs/_index|阅读包]]，先看 8–12 个词，再读 PDF。
4. **间隔复习**：1 / 3 / 7 / 14 / 30 天；只做“看词说义 + 读原句”。
5. **不要背 10k 列表**：10k 是词库容量，不是一周任务。

> [!warning] 数据说明
> 中文/英文释义来自 ECDICT（MIT），音标来自 eSpeak NG；技术词可能存在领域偏差或缺失。论文原句优先于词典释义。
> 57 篇 PDF 没有可提取文本（扫描版/图片版），阅读包会提示直接看 PDF；词汇仍来自你的总结与可提取部分。

## 与阅读计划

- 每日 45 分钟流程：[[14_llm-papers/reading-plan|论文阅读 12 周计划]]
- 逐篇阅读包：[[14_llm-papers/packs/_index|168 篇阅读包]]
- 现有论文词汇：[[14_llm-papers/_index|LLM 论文阅读与词汇]]

## 来源

- PDF 与你的词汇总结：`~/llm-papers`
- 英汉词典：ECDICT（MIT，https://github.com/skywind3000/ECDICT）
- 词频：`wordfreq`
- 词形还原：`lemminflect`

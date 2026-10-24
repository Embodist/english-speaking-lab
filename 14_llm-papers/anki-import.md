---
type: guide
title: 论文词汇 Anki 导入
tags: [guide, skill/reading, library/word-bank]
created: 2026-10-24
updated: 2026-10-24
---

# 论文词汇 Anki 导入

## 三个文件

| 文件 | 条数 | 用途 | 建议牌组 |
|---|---|---|---|
| `core-vocabulary.csv` | 246 | 118 核心学术词 + 128 领域术语 | Core Academic |
| `vocabulary-dedup.csv` | 1,282 | 去重论文词，含 freq/level | Paper Words |
| `vocabulary.csv` | 1,941 | 逐篇词条，保留论文语境 | Paper Context（可选） |

> 先导入 Core Academic，再导入 Paper Words。`vocabulary.csv` 只在你准备读某篇论文前预览，不建议每天复习全部。

## 导入步骤

1. Anki → **File → Import**。
2. 选择 `14_llm-papers/core-vocabulary.csv`。
3. Field separator = **Comma**；Allow HTML = 开；文件编码 UTF-8。
4. 字段映射：

   | CSV 列 | Anki 字段 |
   |---|---|
   | type | Type |
   | category | Category |
   | word | Word |
   | chinese | Meaning |
   | note | Note |
   | level | Level |

5. 牌组命名 `Core Academic`。
6. 再导入 `vocabulary-dedup.csv`，映射：

   | CSV 列 | Anki 字段 |
   |---|---|
   | word | Word |
   | pos | POS |
   | chinese | Meaning |
   | context | Context |
   | freq | Frequency |
   | level | Level |
   | papers | Papers |
   | stage | Stage |
   | paper_id | PaperID |
   | paper_title | PaperTitle |

7. 牌组命名 `Paper Words`。

## 卡片建议

**正面**

```text
{{Word}}  {{POS}}
```

**背面**

```text
{{Meaning}}

{{Context}}

出现论文数：{{Frequency}} · 级别：{{Level}}
来源：{{PaperTitle}}
```

- 不要做“英文 → 中文”的识别卡；要能看词说义、看中文说英文。
- 听力卡：用 `scripts/tts.sh "word or sentence"` 生成音频，再加到卡片。
- S 级词先做“产出卡”：看中文提示说英文搭配。

## 复习设置

- 新卡/天：10–15（Core Academic 优先）。
- 先过 `level = S`，再 `A`；`B` 不要单独背。
- 每天先复习到期卡，再加新卡。
- 连续 3 次能脱口而出 → 标记 Easy；卡住 → Again。
- 每周把反复失败的词抄进 [[01_pronunciation/error-notebook|错题本]] 或随身本。

## 相关

- [[14_llm-papers/_index|LLM 论文阅读与词汇]]
- [[14_llm-papers/reading-workflow|阅读与词汇流程]]
- [[08_sentence-library/anki-import-guide|通用 Anki 导入指南]]

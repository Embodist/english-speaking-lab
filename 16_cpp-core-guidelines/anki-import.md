---
type: guide
title: C++ Core Guidelines Anki 导入
tags: [guide, skill/reading, library/word-bank, topic/cpp]
created: 2026-11-04
updated: 2026-11-04
---

# C++ Core Guidelines Anki 导入

## 两个入口

| 文件 | 条数 | 用途 |
|---|---|---|
| `cpp-core-guidelines.apkg` | 292 | 直接导入，字段和模板已配好（推荐） |
| `anki-01.csv` | 292 | 手动导入 / 改释义后再导入 |

## 方式 A：导入 APKG（推荐）

1. Anki → **File → Import**。
2. 选择 `16_cpp-core-guidelines/cpp-core-guidelines.apkg`。
3. 牌组名：`C++ Core Guidelines`。
4. 导入后按标签筛选：`level-S`、`cpp-domain`。

## 方式 B：导入 CSV

1. Anki → **File → Import** → `anki-01.csv`。
2. Field separator = **Comma**；Allow HTML = 开；编码 UTF-8。
3. 字段映射：

   | CSV 列 | Anki 字段 |
   |---|---|
   | word | Word |
   | phonetic | Phonetic |
   | pos | POS |
   | chinese | Chinese |
   | definition | Definition |
   | sentence | Sentence |
   | section | Section |
   | tags | Tags |

4. 牌组命名 `C++ Core Guidelines`。

## 卡片长什么样

**正面**：`Word` + 音标 + 词性。

**背面**：中文 → 英文释义 → 规范原句 → 章节号（如 `P.5` / `R.11`）。

## 复习设置

- 新卡/天：10–15；先 `level-S`，再 `level-A`；`level-B` 若已会直接 suspend。
- 优先 `cpp-domain` 中的 `RAII`、`ownership`、`invariant`、`undefined behavior`、`data race`、`exception safety`。
- 连续 3 次能脱口而出 → Easy；卡住 → Again。
- 每周把反复失败的词抄进 [[01_pronunciation/error-notebook|错题本]] 或随身本。

## 相关

- [[16_cpp-core-guidelines/_index|C++ Core Guidelines 词库]]
- [[08_sentence-library/anki-import-guide|通用 Anki 导入指南]]
- [[14_llm-papers/anki-import|论文词汇 Anki 导入]]

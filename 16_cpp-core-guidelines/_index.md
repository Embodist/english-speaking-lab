---
type: hub
title: C++ Core Guidelines 词库
tags: [hub, library/word-bank, topic/cpp, skill/reading]
created: 2026-11-04
updated: 2026-11-04
---

# C++ Core Guidelines 词库

> 来源：[C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)（Bjarne Stroustrup / Herb Sutter）。
> 只抽取正文，剔除 `<pre>` / `<code>` 代码块；通用词与 [[14_llm-papers/vocabulary-10k/_index|10k 论文词库]] 去重，领域术语人工校订技术义。

## 规模

| 项目 | 数量 |
|---|---|
| 总卡片 | **292** |
| C++ 领域术语 | 253 |
| 通用技术词汇（10k 去重后新增） | 39 |
| 带原文例句 | 292 |
| 带中文释义 | 292 |
| 带英文释义 | 292 |
| 难度分布（S / A / B） | 107 / 95 / 90 |
| 来源章节 | P / I / F / C / R / ES / Per / CP / E / Con / T / SL 等 |

## 文件

| 文件 | 用途 |
|---|---|
| `cpp-core-guidelines.apkg` | 直接导入 Anki（推荐） |
| `anki-01.csv` | CSV 导入 / 二次编辑 |
| `master.csv` | 完整数据（kind / rank / 音标 / 释义 / 例句 / 章节 / level） |
| [[16_cpp-core-guidelines/dictionary-general\|通用词表]] | 39 个通用技术词，带例句 |
| [[16_cpp-core-guidelines/domain-terms\|领域术语表]] | 253 个 C++ 术语，表格速查 |
| `source/CppCoreGuidelines.md` | 本地 Markdown 全文（约 2.5 万行，含代码示例） |
| `source/CppCoreGuidelines.html` | 原始 HTML 快照（版式 / 锚点备份） |

## 怎么用

1. **先导入 APKG**：Anki → File → Import → `cpp-core-guidelines.apkg`。
2. **按等级过滤**：`level-S` 最难 / 最专业，`level-A` 进阶，`level-B` 基础。新卡/天 10–15，先 `level-S` + `cpp-domain`。
3. **读原句再记词**：卡片背面保留规范原句和章节号（如 `P.5`、`R.11`），可以回到原文看完整规则。
4. **不要背完整表**：253 个术语是词库容量，不是一周任务；按你正在读的章节选 8–12 个。
5. **口语产出**：每学 3 个词，用其中一个说一句你项目里的话；录音回听。

## 标签

- `cpp` / `cpp-domain` / `cpp-vocab`
- `level-S` / `level-A` / `level-B`

## 本地原文

- [[16_cpp-core-guidelines/source/CppCoreGuidelines|C++ Core Guidelines 全文（Markdown）]]：保留规则、Reason / Example / Enforcement、代码示例与参考文献，适合直接搜索和按章节读。
- `source/CppCoreGuidelines.html`：原始 HTML 快照，保留原版式与锚点。
- 上游：https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines

## 数据说明

> [!warning] 释义与音标
> 通用词的中文 / 英文释义来自 ECDICT（MIT），音标来自 eSpeak NG；领域术语的中文和英文释义为人工校订。技术细节以官方规范和你项目的实测为准；本库是语言材料，不是 C++ 标准。

## 重建

```bash
cd ~/english/english-speaking-lab
../.venv/bin/python scripts/build_cpp_guidelines_vocab.py
```

页面缓存：`~/english/data/cpp-core-guidelines.html`。首次运行会联网下载，之后离线重建。

## 相关

- [[14_llm-papers/vocabulary-10k/_index|论文 10k 词库]]
- [[12_word-phrase-bank/_index|词与短语库]]
- [[13_tech-frameworks/_index|技术与框架]]
- [[LEARNING-PATH|学习路径]]

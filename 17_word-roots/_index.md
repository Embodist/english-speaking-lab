---
type: hub
title: "英语词根训练"
tags: [library/word-bank, skill/speaking, status/learning]
created: 2026-11-05
updated: 2026-11-05
---

# 英语词根训练

> 词根是**记忆线索**，不是翻译公式。先认识一个词，再用词根解释它；不要反过来拿词根硬拼一个没见过的词。

> [!warning] 使用边界
> 词根含义来自历史语源，现代词义可能已经偏移（例如 `premise` 不能简单拆成“预先+送”）。拆解只用于辅助记忆，遇到不确定的词先查词典。

## 规模

| 模块 | 数量 | 入口 |
|---|---:|---|
| 核心词根 | 60 | [[17_word-roots/01-core-roots|词根表]] |
| 前缀 | 44 | [[17_word-roots/02-prefixes|前缀表]] |
| 后缀 | 21 | [[17_word-roots/03-suffixes|后缀表]] |
| 技术词拆解 | 50 | [[17_word-roots/04-tech-words|技术词]] |

## 每天 15 分钟

| 时间 | 动作 |
|---|---|
| 3 min | 复习昨天 5 个词根：遮住含义，各说 1 个例词 |
| 5 min | 新学 5 个词根：每个读 3 个例词，只记一个核心含义 |
| 4 min | 3 个技术词：先猜拆解，再看答案 |
| 3 min | 挑 1 个词根，用它的例词说 2 句工作场景的话 |

## 三条规则

1. **一个词根只记一个含义**：`tain` 先记“握住”，不要背五种变体。
2. **例词优先**：能说出 3 个例词，比背出词根定义有用。
3. **技术服务表达**：技术词拆解要用在你的 PR、文档或面试句子里。

## 命令

```bash
cd ~/english/english-speaking-lab
python scripts/study.py root --n 10              # 词根→含义
python scripts/study.py root --n 10 --reverse    # 含义→词根
python scripts/study.py root --tech --n 10       # 技术词拆解
~/english/.venv/bin/python scripts/build_phrase_roots_apkg.py        # 导出 Anki
```

## 相关

- [[17_word-roots/learning-plan|6 周词根计划]]
- [[17_word-roots/05-drills|词根练习卷]]
- [[12_word-phrase-bank/_index|词与短语库]]
- [[13_tech-frameworks/_index|技术与框架]]
- [[18_fsi-drills/_index|FSI 口语训练]]

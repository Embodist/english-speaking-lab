---
type: hub
title: "1200 短语训练库"
tags: [library/word-bank, skill/speaking, status/learning]
created: 2026-11-05
updated: 2026-11-05
---

# 1200 短语训练库

> 原始清单 1,200 条，去重合并多义后 **1125 条**。按 Group 1–31 分组，适合每天 20–40 条滚动训练。

> [!info] 来源
> 知乎原文需要登录，无法直接抓取；本库使用公开同款清单，处理方式见 [[09_sources/03_1200-phrases|来源与处理说明]]。

> [!warning] 释义边界
> 这是基础短语清单，个别中文释义较粗（例如 `pull down` 标成“拆毁”）。训练时以例句、词典和真实语境为准，不要只背中文。

## 每天 20 分钟

| 时间 | 动作 |
|---|---|
| 5 min | 中→英抽认 20 条：3 秒内说出短语，卡住就标记 |
| 5 min | 英→中反向过 20 条，只求认得 |
| 5 min | 选 3 条，各造一句你工作里真会说的话 |
| 5 min | 录音复述这 3 句，回听并只改 1 个问题 |

## 三条规则

1. **先整块，后拆解**：短语当预制块说，不逐词翻译。
2. **一次只换一个槽位**：`look into the ___` 只替换名词。
3. **说过才算学过**：没录音、没造句的条目留在原组重练。

## 分册

| 分册 | 组 | 条数 | 入口 |
|---|---:|---:|---|
| 1200 短语 · Group 01–03 | 01–03 | 103 | [[12_word-phrase-bank/11-phrase-1200/01-group-01-03|打开]] |
| 1200 短语 · Group 04–06 | 04–06 | 116 | [[12_word-phrase-bank/11-phrase-1200/02-group-04-06|打开]] |
| 1200 短语 · Group 07–09 | 07–09 | 110 | [[12_word-phrase-bank/11-phrase-1200/03-group-07-09|打开]] |
| 1200 短语 · Group 10–12 | 10–12 | 107 | [[12_word-phrase-bank/11-phrase-1200/04-group-10-12|打开]] |
| 1200 短语 · Group 13–15 | 13–15 | 114 | [[12_word-phrase-bank/11-phrase-1200/05-group-13-15|打开]] |
| 1200 短语 · Group 16–18 | 16–18 | 115 | [[12_word-phrase-bank/11-phrase-1200/06-group-16-18|打开]] |
| 1200 短语 · Group 19–21 | 19–21 | 94 | [[12_word-phrase-bank/11-phrase-1200/07-group-19-21|打开]] |
| 1200 短语 · Group 22–24 | 22–24 | 95 | [[12_word-phrase-bank/11-phrase-1200/08-group-22-24|打开]] |
| 1200 短语 · Group 25–27 | 25–27 | 116 | [[12_word-phrase-bank/11-phrase-1200/09-group-25-27|打开]] |
| 1200 短语 · Group 28–30 | 28–30 | 116 | [[12_word-phrase-bank/11-phrase-1200/10-group-28-30|打开]] |
| 1200 短语 · Group 31–31 | 31–31 | 39 | [[12_word-phrase-bank/11-phrase-1200/11-group-31-31|打开]] |

## 专项入口

- [[12_word-phrase-bank/11-phrase-1200/featured-work-90|工作高频 90 条]]：时间有限先练这份。
- [[12_word-phrase-bank/11-phrase-1200/learning-plan|30 天刷完计划]]：每天 38 条 + 复习。
- [[12_word-phrase-bank/10-fixed-chunks|固定搭配与高频句型]]：工作场景的整句框架。

## 命令

```bash
cd ~/english/english-speaking-lab
python scripts/study.py phrase --n 20                 # 中→英
python scripts/study.py phrase --n 20 --reverse       # 英→中
python scripts/study.py phrase --group 3 --n 20       # 按组
python scripts/study.py phrase --featured --n 20      # 工作高频
python scripts/study.py phrase --n 10 --tts           # 生成参考音
~/english/.venv/bin/python scripts/build_phrase_roots_apkg.py             # 导出 Anki
```

## 相关

- [[12_word-phrase-bank/_index|词与短语库]]
- [[18_fsi-drills/_index|FSI 口语训练]]：把短语练成条件反射。
- [[LEARNING-PATH|学习路径]]

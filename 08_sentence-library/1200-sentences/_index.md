---
type: hub
title: "1200 句场景口语"
tags: [library/sentence, skill/speaking, status/learning]
created: 2026-11-06
updated: 2026-11-06
---

# 1200 句场景口语

> 10 大场景 × 120 句 = **1,200 句**。每句都带中文，适合每天 20 句：听 → 跟读 → 中→英 → 录音。

> [!info] 来源
> 来自你提供的知乎文章正文（2026-11-05），逐条整理；来源与解析说明见 [[09_sources/04_1200-sentences|1200 句来源说明]]。

## 每天 20 分钟

| 时间 | 动作 |
|---|---|
| 4 min | 听 5 句参考音，标重音和停顿（`--tts`） |
| 4 min | 影子跟读 5 句，每句 3 遍 |
| 7 min | 中→英抽认 20 句：3 秒内开口，卡住就标记 |
| 5 min | 选 3 句改成你的真实场景，录音并回听 |

## 三条规则

1. **中文提示 → 英文反应**：不要先想语法，先说整句。
2. **一次只改一个词**：把人名、地点、时间换成你的。
3. **录音才算练过**：每天至少留 1 段 60 秒录音。

## 分类

| # | 场景 | 句数 | 入口 |
|---:|---|---:|---|
| 01 | 职场沟通与工作协作 | 120 | [[08_sentence-library/1200-sentences/01-workplace|打开]] |
| 02 | 会议表达与团队讨论 | 120 | [[08_sentence-library/1200-sentences/02-meetings|打开]] |
| 03 | 日常生活与社交交流 | 120 | [[08_sentence-library/1200-sentences/03-daily-social|打开]] |
| 04 | 表达观点与个人看法 | 120 | [[08_sentence-library/1200-sentences/04-opinions|打开]] |
| 05 | 问题解决与突发情况 | 120 | [[08_sentence-library/1200-sentences/05-problems|打开]] |
| 06 | 购物、餐厅与消费场景 | 120 | [[08_sentence-library/1200-sentences/06-shopping-dining|打开]] |
| 07 | 旅行出行与住宿交流 | 120 | [[08_sentence-library/1200-sentences/07-travel-hotel|打开]] |
| 08 | 家庭生活、健康与个人安排 | 120 | [[08_sentence-library/1200-sentences/08-family-health|打开]] |
| 09 | 学习成长与表达交流 | 120 | [[08_sentence-library/1200-sentences/09-learning|打开]] |
| 10 | 电话沟通、网络交流与综合表达 | 120 | [[08_sentence-library/1200-sentences/10-calls-online|打开]] |

## 专项入口

- [[08_sentence-library/1200-sentences/learning-plan|60 天刷完计划]]：每天 20 句。
- [[18_fsi-drills/_index|FSI 口语训练]]：把句子练成条件反射。
- [[12_word-phrase-bank/11-basic-phrases/_index|基础短语 1125（补充）]]：短语级搭配，作为补充。

## 命令

```bash
cd ~/english/english-speaking-lab
python scripts/study.py sentence --n 20                # 中→英
python scripts/study.py sentence --n 20 --reverse      # 英→中
python scripts/study.py sentence --category 1 --n 20   # 按场景
python scripts/study.py sentence --n 5 --tts           # 生成参考音
~/english/.venv/bin/python scripts/build_sentence_1200_apkg.py  # 导出 Anki
```

## 相关

- [[08_sentence-library/_index|句子库]]
- [[LEARNING-PATH|学习路径]]
- [[17_word-roots/_index|前后缀 335]]
- [[18_fsi-drills/_index|FSI 口语训练]]
- [[19_qwerty-learner/_index|qwerty 打字练习]]

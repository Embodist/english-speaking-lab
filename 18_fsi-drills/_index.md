---
type: hub
title: "FSI 式口语训练"
tags: [skill/speaking, status/learning]
created: 2026-11-05
updated: 2026-11-05
---

# FSI 式口语训练

> FSI（美国外交学院）语言课程的核心不是讲语法，而是**大量结构化重复**：听懂 → 模仿 → 替换 → 变换 → 应答 → 对话。每天 20 分钟，练到不假思索。

> [!info] 说明
> 这是按 FSI 音频语言法（audio-lingual method）设计的训练材料，不是 FSI 原版教材的复制。

## 四类训练

| 类型 | 练什么 | 数量 | 入口 |
|---|---|---:|---|
| 替换 Drill | 固定句型，只换一个槽位 | 60 | [[18_fsi-drills/01-substitution|替换训练]] |
| 变换 Drill | 陈述↔疑问、主动↔被动、直接↔礼貌 | 25 | [[18_fsi-drills/02-transformation|变换训练]] |
| 应答 Drill | 听到问题，立刻给完整回答 | 25 | [[18_fsi-drills/03-response|应答训练]] |
| 情景 Drill | 站会、事故、评审、面试 | 16 | [[18_fsi-drills/04-situations|情景训练]] |

## 每天 20 分钟

| 时间 | 动作 |
|---|---|
| 3 min | 听/读 1 个模型句，跟读 3 遍，模仿重音和停顿 |
| 7 min | 替换训练：同一句型换 6 个槽位，每个说 2 遍 |
| 5 min | 变换或应答训练：看提示，先答，再看模型答案 |
| 5 min | 录一段 60 秒自由应答，回听并只改 1 个问题 |

## 五条规则

1. **先出声，再看答案**：卡住 3 秒就看答案，然后立刻重说一遍。
2. **一次只练一个结构**：替换时不要改句型，变换时不要加内容。
3. **速度优先于完美**：先做到 2 秒内开口，再修发音。
4. **录音才算练过**：每天至少留 1 段 60 秒录音。
5. **练完立刻用**：当天至少把 1 句写进 Slack、PR 或日志。

## 命令

```bash
cd ~/english/english-speaking-lab
python scripts/study.py fsi --set sub --n 10
python scripts/study.py fsi --set trans --n 10
python scripts/study.py fsi --set resp --n 10
python scripts/study.py fsi --set situation --n 8
python scripts/study.py fsi --set resp --n 5 --tts   # 生成模型答案音频
```

## 相关

- [[18_fsi-drills/learning-plan|4 周训练计划]]
- [[12_word-phrase-bank/11-phrase-1200/_index|1200 短语训练库]]
- [[12_word-phrase-bank/10-fixed-chunks|固定搭配与高频句型]]
- [[02_daily-work/_index|日常工作表达]]
- [[06_interview/_index|面试训练]]

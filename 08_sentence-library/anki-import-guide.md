---
type: guide
title: Anki 导入指南
tags: [guide, skill/speaking]
created: 2026-10-23
updated: 2026-10-23
---

# Anki 导入指南

> 论文词汇（1,282 去重词 + 246 核心词）请用专门的 [[14_llm-papers/anki-import|论文词汇 Anki 导入]]。

## 准备

- 文件：`08_sentence-library/phrase-library.csv`（UTF-8，逗号分隔）
- 字段：`类别, English, 中文, Example, 练习提示`
- Anki 桌面版下载：<https://apps.ankiweb.net/>

> WSL 中的文件路径：`\\wsl$\<发行版名>\home\user\english\english-speaking-lab\08_sentence-library\phrase-library.csv`。也可以在 Windows 资源管理器地址栏输入 `\\wsl$` 找到。

## 导入步骤

1. 打开 Anki → **File → Import**（文件 → 导入）。
2. 选择 `phrase-library.csv`。
3. 确认 **Field separator = Comma**，**Allow HTML in fields = 开**。
4. 选择目标牌组，或新建 `English Speaking`。
5. 字段映射：
   - Field 1 ← `类别`
   - Field 2 ← `English`
   - Field 3 ← `中文`
   - Field 4 ← `Example`
   - Field 5 ← `练习提示`
6. 导入后检查一条卡片是否乱码；若乱码，确认文件编码为 UTF-8。

## 卡片类型建议

| 正面 | 背面 |
|---|---|
| 中文 + 场景提示 | English + Example + 发音要点 |

不要做“英文 → 中文”的识别卡：你的目标是**产出**英文，不是看懂英文。

## 音频

1. 用 OpenPronounce 的 TTS 或网页界面生成参考音频。
2. 在卡片背面加 `[sound:filename.mp3]`，文件放入 Anki 媒体库。
3. 或者只保留句子，用 OpenPronounce 现场跟读。

## 复习设置

- 新卡/天：5–10 张（不要贪多）
- 重点：能脱稿说出 → 选 `Good`；卡住 → `Again`
- 每周把 Anki 里反复失败的句子同步到 [[01_pronunciation/error-notebook|发音错题本]]

## 相关

- [[08_sentence-library/_index|句子库]]
- [[STUDY-PLAN#间隔复习|间隔复习]]

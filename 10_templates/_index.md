---
type: hub
title: 模板
tags: [hub, meta]
created: 2026-10-23
updated: 2026-10-23
---

# 模板

在 Obsidian 中启用核心插件 **Templates**，模板目录已指向本文件夹。

| 模板 | 用途 |
|---|---|
| [[10_templates/daily-practice\|每日练习]] | 每天 25 分钟闭环记录 |
| [[10_templates/sentence-card\|句子卡]] | 一句话一张卡，便于复习和迁移 |
| [[10_templates/project-story\|项目故事]] | 面试项目讲述（Goal → Result） |
| [[10_templates/weekly-review\|周复盘]] | 每周 15 分钟维护 |
| [[10_templates/topic-note\|主题笔记]] | 新增技术主题时复制 |

## 使用方式

1. 新建笔记，放入目标目录（默认会进 `00_inbox/`）。
2. `Ctrl/Cmd + P` → `Templates: Insert template`。
3. 填写 frontmatter 中的 `scene` 和 `tags`。
4. 保存为规范文件名（见 [[MANAGEMENT#命名规范|命名规范]]）。

> 模板里的 `{{date}}`、`{{title}}` 由 Obsidian 模板插件自动替换。

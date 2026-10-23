---
type: guide
title: 目录与管理规范
tags: [guide, meta]
created: 2026-10-23
updated: 2026-10-23
---

# 目录与管理规范

这份笔记定义整个 vault 的命名、标签和维护方式。目标是：**半年后回来仍然找得到、加得进、删得掉。**

## 设计原则

1. **编号定秩序**：顶层目录用 `01_`–`11_` 编号，新增主题放末尾，不打乱现有结构。
2. **单一入口**：每个目录有一个 `_index.md` 作为主题首页，文件之间只通过链接和组织关系连接。
3. **原子笔记**：一条句子卡只放一句话；一个项目故事只讲一个项目。方便复用和重组。
4. **来源只读**：`09_sources/` 只存放原始资料，不改动；提炼后的内容写入对应主题目录。
5. **模板先行**：任何重复出现的笔记类型，都在 `10_templates/` 有模板。
6. **纯 Markdown**：除 `09_sources/` 的 docx 外，全部内容是可检索、可版本管理的 Markdown。

## 目录地图

| 目录 | 放什么 | 不放什么 |
|---|---|---|
| `00_inbox/` | 临时句子、想法、待分类内容 | 长期维护的正式笔记 |
| `01_pronunciation/` | 发音练习、录音索引、错题本 | 项目介绍、面试答案 |
| `02_daily-work/` | 站会、Bug、PR、会议、邮件表达 | 面试专用内容 |
| `03_ai-agent-rag/` | Agent、RAG、评测、部署的表达 | 与 AI 无关的通用英语 |
| `04_security/` | 安全分析、WAF、SOAR 表达 | 通用后端内容 |
| `05_music-agent/` | 音乐生成、跨模态检索表达 | 其他项目 |
| `06_interview/` | 自我介绍、项目故事、模拟面试 | 日常沟通句子 |
| `07_review-log/` | 每日记录、每周复盘 | 句子卡正文 |
| `08_sentence-library/` | 分类句子库、Anki 导入文件 | 个人录音（放 `11_attachments/`） |
| `09_sources/` | 原始手册和资料 | 自己提炼的笔记 |
| `10_templates/` | 所有模板 | 正式内容 |
| `11_attachments/` | 录音、截图等二进制附件 | Markdown 笔记 |
| `12_word-phrase-bank/` | 词典级词条（说 / 写 / 读） | 整句对话（放句子库） |
| `13_tech-frameworks/` | LLM、Agent、音乐、RAG 能力记录 | 具体项目故事（放面试目录） |

## 命名规范

| 类型 | 规则 | 示例 |
|---|---|---|
| 主题首页 | `_index.md` | `02_daily-work/_index.md` |
| 每日记录 | `YYYY-MM-DD.md` | `2026-10-23.md` |
| 周复盘 | `YYYY-Www.md` | `2026-W43.md` |
| 句子卡 | `sentence-<slug>.md` | `sentence-root-cause.md` |
| 项目故事 | `story-<project>.md` | `story-rag-assistant.md` |
| 录音 | `day<NN>_<scene>_<take>.wav` | `day01_intro_first-take.wav` |
| 其他笔记 | 小写 kebab-case，英文 | `agent-overview.md` |

> 文件名用英文：跨工具兼容（Anki、git、脚本）；标题用中文：阅读友好。

## Frontmatter 标准

```yaml
---
type: sentence        # dashboard | hub | guide | log | sentence | story | topic | template
scene: interview      # 可选：standup | bug | pr | meeting | interview | smalltalk | incident
tags: [skill/speaking, status/learning]
created: 2026-10-23
updated: 2026-10-23
review: 2026-10-30    # 可选：下次复习日期
---
```

## 标签体系

标签只用于**跨目录筛选**，不要替代目录和链接。

| 前缀 | 可用值 | 含义 |
|---|---|---|
| `status/` | `inbox` `learning` `mastered` | 学习状态 |
| `skill/` | `pronunciation` `listening` `speaking` `interview` `writing` | 能力维度 |
| `scene/` | `standup` `bug` `pr` `meeting` `interview` `incident` `smalltalk` | 使用场景 |
| `topic/` | `agent` `rag` `eval` `deployment` `security` `music` | 技术主题 |
| `type/` | `sentence` `story` `log` `guide` | 笔记类型 |

同一条句子最多加 3 个标签；状态变化时**替换**而不是叠加。

## 工作流

```text
捕获 → 练习 → 提炼 → 复习 → 归档
```

1. **捕获**：随时把新句子丢进 `00_inbox/`，标 `status/inbox`。
2. **练习**：每天按 [[STUDY-PLAN#每日 25 分钟闭环|25 分钟闭环]] 练 3–5 句，记录到 `07_review-log/YYYY-MM-DD.md`。
3. **提炼**：把反复用错的句子升级为 `08_sentence-library/` 里的句子卡，或写入对应主题目录。
4. **复习**：按 1 / 3 / 7 / 14 / 30 天间隔回看；能脱稿说出后改为 `status/mastered`。
5. **归档**：掌握超过 3 个月且不再出错的卡片可以移入 `07_review-log/archive/`，不要删除。

## 如何扩展一个新主题

例如要加“数据工程”：

1. 新建 `14_data-engineering/`。
2. 复制 [[10_templates/topic-note|主题笔记模板]]，存为 `14_data-engineering/_index.md`。
3. 在 [[README|主页]] 导航表和本文件的目录地图各加一行。
4. 新句子卡加 `topic/data-engineering` 标签。

编号只增不改，链接只增不删，历史记录永远可追溯。

## 每周维护（15 分钟）

- [ ] 清空 `00_inbox/`：分类、合并或删除。
- [ ] 回看本周 5 份每日记录，提取最常犯的 1–3 个问题。
- [ ] 更新 [[07_review-log/weekly-review|周复盘]]：本周最有用表达、下周重点。
- [ ] 检查 `11_attachments/`，按命名规范补全或重命名录音。
- [ ] 给已掌握的句子卡改 `status/mastered`。
- [ ] 备份：复制整个文件夹，或使用 git（见下）。

## Obsidian 设置建议

用 Obsidian 打开 `english-speaking-lab` 文件夹作为 vault。仓库已带 `.obsidian` 配置：

- 附件默认保存到 `11_attachments/`；
- 新笔记默认保存到 `00_inbox/`；
- 模板目录为 `10_templates/`；
- 已启用模板、录音机、文件恢复、大纲、字数统计。

建议再安装两个可选插件（非必需）：

- **Templater**：更灵活的模板变量。
- **Spaced Repetition**：在 Obsidian 内直接做间隔复习。

## 工具与脚本

工具安装在 vault 外部，避免把大文件混进学习内容：

```text
~/english/
├── .venv/                 # Python 环境
├── OpenPronounce/         # 网页界面源码
├── models/                # Vosk 模型
└── english-speaking-lab/  # 本 vault
```

vault 内 `scripts/` 只放薄封装，详细说明见 [[scripts/README|脚本说明]]；从零搭建、工具搭配和最佳实践见 [[TOOLING|工具手册]]。

## 备份与版本管理

```bash
cd ~/english/english-speaking-lab
git init
git add .
git commit -m "init: english speaking lab"
```

`.gitignore` 已排除录音大文件和 Obsidian 工作区缓存。若希望录音也进版本库，改用 Git LFS 或定期复制到网盘。

> [!warning] 不要删除 `09_sources/`
> 原始手册是内容源头，回顾方法或补充句子时先查原文。

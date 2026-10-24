---
type: dashboard
title: 英语口语训练室
tags: [dashboard, english]
created: 2026-10-23
updated: 2026-10-23
---

# 英语口语训练室 · English Speaking Lab

> [!tip] 今天只做一件事
> 打开 [[07_review-log/2026-10-23|今日练习记录]]，按 25 分钟闭环练 3–5 句，并录一段 30 秒英文自我介绍作为基线。

## 快速导航

| 区域 | 用途 | 入口 |
|---|---|---|
| 学习路径 | 说 → 写 → 读，四周清晰步骤 | [[LEARNING-PATH\|学习路径]] |
| 记录边界 | 必须记录 vs 可扩展 | [[SCOPE\|记录与扩展]] |
| 训练总纲 | 训练方法、评分、30 天计划 | [[STUDY-PLAN\|学习计划]] |
| 工具上手 | 从启动到第一次打分 | [[QUICKSTART\|工具体验指南]] |
| 工具手册 | 搭建、搭配、最佳实践 | [[TOOLING\|工具手册]] |
| 新机器 | 一键安装手册与脚本 | [[NEW-MACHINE\|新机器安装]] |
| 部署 | Docker Swarm + RustFS | [[deploy/README\|部署]] |
| 资源规划 | CPU / GPU / 内存 / 磁盘预算 | [[deploy/RESOURCE-PLAN\|资源规划]] |
| 目录规范 | 命名、标签、维护流程 | [[MANAGEMENT\|管理规范]] |
| 发音训练 | 发音纠正、错题本、录音基线 | [[01_pronunciation/_index\|发音训练]] |
| 日常工作 | 站会、Bug、PR、会议、邮件 | [[02_daily-work/_index\|日常工作]] |
| AI / Agent / RAG | 项目表达与技术讨论 | [[03_ai-agent-rag/_index\|AI 与 RAG]] |
| 安全方向 | 恶意流量、WAF、SOAR | [[04_security/_index\|安全分析]] |
| 音乐 Agent | 跨模态检索、音频生成 | [[05_music-agent/_index\|音乐 Agent]] |
| 面试 | 自我介绍、项目故事、模拟面试 | [[06_interview/_index\|面试训练]] |
| 复习日志 | 每日记录、周复盘 | [[07_review-log/_index\|复习日志]] |
| 句子库 | 111 条按场景分类的高频句 | [[08_sentence-library/_index\|句子库]] |
| 词与短语库 | 词典级词条：说 / 写 / 读 | [[12_word-phrase-bank/_index\|词与短语库]] |
| 技术与框架 | LLM、Agent、音乐 AI、RAG 服务 | [[13_tech-frameworks/_index\|技术与框架]] |
| LLM 论文 | 168 篇论文词表与阅读流程 | [[14_llm-papers/_index\|LLM 论文]] |
| 简历表达 | 10 年安全 + AI 的英文叙事 | [[15_resume/_index\|简历与自我介绍]] |
| 原始资料 | 手册、速记卡、CSV（只读） | [[09_sources/_index\|原始资料]] |
| 模板 | 新建笔记从这里取 | [[10_templates/_index\|模板]] |
| 录音附件 | 所有录音文件 | `11_attachments/` |
| 收集箱 | 临时想法、新句子 | [[00_inbox/_index\|收集箱]] |

## 按需学习

| 你现在要做什么 | 从这里开始 |
|---|---|
| 只有 10 分钟 | 从 [[12_word-phrase-bank/10-fixed-chunks\|固定块库]] 选 10 条 S 级，跟读并各说一句 |
| 想按顺序学 | [[LEARNING-PATH\|学习路径]]：说 → 写 → 读 |
| 要找某个词 | [[12_word-phrase-bank/_index\|词与短语库]] |
| 通勤/随身复习 | [[12_word-phrase-bank/pocket-notebook\|随身笔记]] |
| 明天要站会 | [[02_daily-work/standup\|站会模板]] + 录 30 秒 |
| 明天有面试 | [[06_interview/introduction\|自我介绍]] → [[06_interview/project-stories\|项目故事]] → [[06_interview/mock-interview\|模拟面试]] |
| 某个音总读错 | [[01_pronunciation/error-notebook\|发音错题本]] |
| 要写邮件/Slack | [[02_daily-work/email-slack\|书面沟通]] |
| 要讲 RAG / Agent | [[03_ai-agent-rag/_index\|AI 与 RAG]] |
| 要讲安全项目 | [[04_security/_index\|安全分析]] |
| 要讲音乐 Agent | [[05_music-agent/_index\|音乐 Agent]] |
| 要读 LLM 论文 | [[14_llm-papers/_index\|LLM 论文阅读与词汇]] |
| 准备自我介绍/简历 | [[15_resume/_index\|简历与自我介绍]] |
| 不知道今天练什么 | [[STUDY-PLAN#每周节奏\|每周节奏]] |

> 更完整的“说 → 写 → 读”30 分钟版本和四周路径见 [[LEARNING-PATH|学习路径]]。

## 每天 25 分钟

1. **复习昨天**（3 min）：不看英文，先说昨天的 3 句。
2. **听标准音**（5 min）：整句 → 意群，标重音和停顿。
3. **跟读**（6 min）：分块跟读，再整句影子跟读。
4. **录音并检查**（5 min）：回听 + ASR/音素检查。
5. **只修 1–2 个问题**（4 min）。
6. **脱稿复述**（2 min）：用自己的话表达同一意思。

细则见 [[STUDY-PLAN#每日 25 分钟闭环|每日闭环]]。

## 工具速查

> 当前运行模式：**CPU-only**。GPU 镜像与 Swarm stack 已准备，但暂不启用；原因与切换条件见 [[deploy/ADR-001-cpu-first|ADR-001]]。

```bash
cd ~/english/english-speaking-lab

bash scripts/check-env.sh                              # 环境自检
bash scripts/start-web.sh                              # 网页界面 → http://localhost:8000
bash scripts/lab.sh analyze recording.wav "I haven't identified the root cause yet."  # TTS+ASR+发音+报告
bash scripts/pronounce.sh recording.wav "I haven't identified the root cause yet."
bash scripts/tts.sh "The main trade-off is accuracy versus latency." -o 11_attachments/reference/tradeoff.wav
bash scripts/asr.sh recording.wav                      # 检查是否被识别成目标句
bash scripts/new-day.sh                                # 生成今天的练习记录
```

统一练习页：`http://localhost:8000/lab`（参考音 + 录音 + 发音 + Whisper/Vosk）。完整工具体验步骤见 [[QUICKSTART|工具体验指南]]，搭建与搭配见 [[TOOLING|工具手册]]。

> [!note] 工具只是反馈手段
> AI 分数会受麦克风、噪声和专有名词影响。真正有效的是：**固定句子 → 录音 → 只改一个点 → 再录 → 一周后对比**。

## 进度

- [ ] Day 1：录制 30 秒自我介绍基线（`11_attachments/day01_intro_baseline.wav`）
- [ ] 第 1 周：发音基线与句子节奏
- [ ] 第 2 周：日常工作沟通自动化
- [ ] 第 3 周：把 AI / RAG / 安全 / 音乐项目讲清楚
- [ ] 第 4 周：流利度、面试与脱稿迁移
- [ ] 30 天后：整理个人错题本，选出下个月最常犯的 3 个问题

> [!warning] 内容边界
> 本仓库是英语学习材料，不是技术规范。技术细节、指标和架构以你的真实项目与官方文档为准；面试中不要背未验证的数字。词条和例句是语言模式，具体用法请结合上下文。

## 使用原则

1. **可理解性优先**：先让对方听懂关键词、数字、否定和时间，不追求消除口音。
2. **句子来自真实场景**：至少一半练习句必须是你工作或面试中真的会说的话。
3. **一次只改一个点**：元音、词尾、重音、节奏分开练。
4. **录音才算练过**：没有回听的练习无法暴露问题。
5. **最终目标是脱稿**：能用自己的话在新场景里说出正确句型，而不是背完整段。

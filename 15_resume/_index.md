---
type: hub
title: 简历与自我介绍
tags: [hub, skill/interview, skill/speaking]
created: 2026-10-24
updated: 2026-10-24
---

# 简历与自我介绍

> 来源：`~/resume-latex/resume_ai_security_en.tex`（外部简历，未复制联系方式进仓库）。
> 这里不是简历复刻，而是**面试可说的版本**：先结论、再项目、再取舍。
>
> 需要中文→英文草稿时，用 [[13_tech-frameworks/translation-model|Hy-MT2-1.8B]]（`scripts/translate.sh`）；只做草稿，最终用你自己的话。

## 你的定位（一句话）

**10 年网络安全研发/运营 + 应用型 AI 工程**，能把 Agent/RAG/模型服务落到生产，也能从安全视角设计 AI 护栏。

## 四条核心能力

| 能力 | 证据（简历事实，面试前请确认口径） |
|---|---|
| Agent / LLM 工程 | LangGraph / ReAct / Function Calling / MCP；音乐 Agent、LLM 安全 Agent；RAG、vLLM、LoRA/SFT |
| AI for Security | WAF/IPS、ATT&CK、SOAR；LLM 恶意流量意图分析、规则推断；规则验证从数周降到约 4 小时 |
| Security for AI | OWASP LLM Top 10、提示词注入、Agent guardrails、工具越权、数据投毒；Deepfake/声音克隆检测 |
| 工程与规模 | Go/Python/C++、eBPF、Docker/K8s；10B 级流量验证、千万级事件/秒探针；7 项 SOAR/安全运营专利 |

## 职业时间线

| 时间 | 公司 / 角色 | 主线 |
|---|---|---|
| 2016.07–2017.04 | 黑百丁 · 数据运营/安全分析 | 日志分析、恶意爬虫、业务风控 |
| 2017.05–2019.11 | 楚云安 · 高级安全开发 | WAF 引擎、态势感知、高可用网关 |
| 2019.11–2020.05 | 任子行 · 安全研究员 | NIDS/HIDS、资产发现、ATT&CK |
| 2020.05–2023.02 | 天融信 · 安全研究经理（AI 安全） | BERT 告警分类、漏洞/规则/情报、eBPF、专利 |
| 2023.02–2026.06 | 腾讯云 · WAF 安全运营 & AI 应用 | 规则引擎重构、LLM 安全 Agent、RAG、流量验证 |
| 2026.06–现在 | 望海科技 · 音乐 Agent / AI 安全 | 多工具音乐 Agent、跨模态检索、内容安全 |

## 三个旗舰项目

1. **Music Creation & Cover Agent**：LangGraph 编排音高/和声/SVC/混音，跨模态检索 + 版权/护栏。
2. **LLM Security Operations Agent & Traffic Validation**：BERT 粗筛 + Qwen 深度分析，Go 规则推断，10B 级影子流量验证。
3. **Enterprise Security RAG Assistant**：Milvus/Redis/Elasticsearch 混合检索、SBERT 重排、pgvector，85% 长文本 QA。

## 怎么用

1. 先读 [[15_resume/self-introduction|自我介绍]]，录 30 秒和 60 秒各一版。
2. 用 [[15_resume/experience|工作经历表达]] 练“Walk me through your resume”。
3. 用 [[15_resume/projects|项目故事]] 准备 30 秒 / 90 秒 / 追问。
4. 对照 [[15_resume/capability-gaps|能力补充清单]]，把缺的数字和边界补齐。
5. 发音和术语见 [[15_resume/keywords|关键词发音]]。

## 隐私

- 电话、邮箱、生日、住址、政治面貌等**没有**写入本仓库。
- 公司名和项目方向来自你的简历；内部系统代号（如 Tiga/Menshen）已省略，面试时按公司保密要求决定是否使用。
- 所有数字都来自简历；面试前确认单位和统计口径，不要临场编造。

## 相关

- [[15_resume/self-introduction|自我介绍]]
- [[15_resume/experience|工作经历表达]]
- [[15_resume/projects|项目故事]]
- [[15_resume/capability-gaps|能力补充清单]]
- [[15_resume/keywords|关键词发音]]
- [[06_interview/_index|面试训练]]
- [[14_llm-papers/_index|LLM 论文阅读]]

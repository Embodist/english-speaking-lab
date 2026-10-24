---
type: story
title: 工作经历表达
tags: [skill/interview, status/learning]
created: 2026-10-24
updated: 2026-10-24
---

# 工作经历表达

> 面试不是逐行念简历。每段只讲：**做什么 → 我负责什么 → 结果/取舍 → 学到什么**。
> 标 `[confirm]` 的数字来自简历，面试前确认单位和统计口径。

## 时间线（30 秒讲完）

> I’ve spent about ten years in security and applied AI. I started with data and log analysis, then moved into WAF and security operations. At Topsec, I led BERT-based alert classification and built a cloud-native probe with eBPF. At Tencent Cloud, I worked on WAF rule migration, an LLM security agent, a traffic-validation engine, and an enterprise RAG assistant. Now I build music agents with LangGraph, retrieval, and audio models.

## 逐段表达

### 2016.07–2017.04 · 数据运营/安全分析

> I started in data operations and security analysis. I collected e-commerce logs with Python, built access baselines, and used clustering to find malicious crawlers, coupon abuse, and order fraud. The main lesson was to turn findings into detection rules, not just reports.

- 你负责：日志采集、基线、聚类、规则化
- 可讲结果：从监控到规则闭环
- `[confirm]`：业务规模、拦截效果

### 2017.05–2019.11 · 高级安全开发（WAF/态势感知）

> I worked on an enterprise WAF based on ModSecurity and Tengine. I tuned hundreds of rules against OWASP Top 10 and CC attacks, and built a situational-awareness console with Redis and Kafka. We also handled transparent proxying, active-standby failover, and canary updates.

- 你负责：规则调优、引擎改造、控制台、高可用
- 关键词：WAF engine, rule tuning, HA, canary
- `[confirm]`：QPS、规则数量、可用性

### 2019.11–2020.05 · 安全研究员（NIDS/HIDS）

> I worked on network and host intrusion detection. I built asset discovery, weak-password detection, and C2 compromised-host detection, and mapped alerts to ATT&CK. We kept real-network false positives and false negatives under about fifteen percent `[confirm: dataset]`, and I also applied early ML to traffic features.

- 你负责：探针、检测逻辑、ATT&CK 映射
- `[confirm]`：15% 的统计口径

### 2020.05–2023.02 · 安全研究经理（AI 安全）

> At Topsec, I led a BERT-based semantic classification project that unified alert taxonomies across product lines. I also did vulnerability and rule research, modeled threat intelligence as a graph, and built a cloud-native probe with eBPF that kept CPU and memory low under tens of millions of events per second `[confirm: hardware]`. We filed seven patents in SOAR and security operations `[confirm: granted/filed]`.

- 你负责：团队、BERT 应用、漏洞/规则/情报、eBPF 探针
- 关键词：alert taxonomy, semantic classification, in-kernel filtering, lock-free aggregation
- 追问准备：团队多大？你具体写代码还是带人？专利角色？

### 2023.02–2026.06 · 腾讯云（WAF 安全运营 & AI 应用）

> At Tencent Cloud, I worked on three things. First, I helped migrate more than a thousand high-risk WAF rules to a higher-performance engine. Second, I built an LLM-driven security agent: a BERT stage did coarse filtering, and a fine-tuned Qwen model analyzed obfuscated requests; we also built a Go platform to infer detection rules. Third, I built a shadow-traffic validation system that cut rule validation from weeks to about four hours. I also worked on an enterprise RAG assistant with hybrid retrieval, reranking, and prompt-injection defenses.

- 你负责：规则迁移、LLM 安全 Agent、Go 规则推断、流量验证、RAG
- 可讲结果：规则验证数周 → 约 4 小时；RAG 长文本 QA 85% `[confirm: metric/dataset]`；RMB 2M+ 主动服务价值 `[confirm: 定义]`
- 关键词：rule engine, shadow traffic, intent analysis, hybrid retrieval, reranking

### 2026.06–现在 · 音乐 Agent / AI 安全

> In my current role, I build a music creation and cover agent. LangGraph coordinates pitch analysis, harmony analysis, voice conversion, and mixing. We use cross-modal retrieval for text, humming, and mood queries, and we add guardrails for tool permissions, prompt injection, copyright, and content safety. The main challenge is balancing creative flexibility with predictable, testable behavior.

- 你负责：工作流编排、跨模态检索、模型复现/部署、内容安全
- 关键词：LangGraph, tool calling, cross-modal retrieval, SVC, RVC, guardrails
- `[confirm]`：用户规模、生成成功率、延迟、成本、质量评测

## “Walk me through your resume” 90 秒模板

> Sure. I’ll go chronologically.
>
> I started in security: log analysis, WAF, and security operations. That gave me a strong foundation in traffic, detection rules, and production systems.
>
> Around 2020, I moved into applied AI. At Topsec, I led BERT-based alert classification and built an eBPF probe; we also filed several patents.
>
> At Tencent Cloud, I focused on LLM applications for security: a two-stage agent for malicious-traffic analysis, a Go rule-inference platform, and a shadow-traffic engine that cut validation from weeks to hours. I also built an enterprise RAG assistant.
>
> Now I build music agents. I care about reliability: retrieval quality, evaluation, guardrails, and failure handling. That’s the thread across all these roles.

## 高频动词（换成更具体的）

| 泛泛说法 | 更具体 |
|---|---|
| did / worked on | led, built, migrated, designed, shipped, rebuilt |
| improved | cut … from … to …, reduced … by …, improved … to … |
| handled | owned, coordinated, validated, mitigated, rolled back |
| helped | contributed to, drove the … part, was responsible for |
| used | chose … because …, evaluated … against …, deployed … |

## 面试前必须确认的数字

- [ ] 10B 级流量的单位：请求/天？事件/天？包/秒？
- [ ] 85% 长文本 QA：数据集、样本量、指标定义、人工/自动
- [ ] 规则验证“4 小时”：从什么基线到什么基线？单条规则还是批量？
- [ ] 7 项专利：已授权还是申请中？你的角色？
- [ ] 千万级事件/秒：硬件、核数、包大小、检测深度
- [ ] CPU/内存 <1%：单核、整机、还是容器？
- [ ] 15% 漏报/误报：数据集和统计方式
- [ ] RMB 2M+：计算口径、时间范围

## 相关

- [[15_resume/_index|简历与自我介绍]]
- [[15_resume/projects|项目故事]]
- [[15_resume/capability-gaps|能力补充清单]]

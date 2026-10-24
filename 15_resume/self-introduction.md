---
type: story
title: 自我介绍（基于真实简历）
tags: [skill/interview, scene/interview, status/learning]
created: 2026-10-24
updated: 2026-10-24
---

# 自我介绍（基于真实简历）

> 先记结构，不要逐字背。每段练到能换词、能缩短、能扩展。

## 30 秒版本

> I’m an AI engineer with ten years of experience across cybersecurity and applied AI. I started in WAF and security operations, then moved into machine learning for alert classification and threat detection. At Tencent Cloud, I worked on LLM-based security analysis, an enterprise RAG assistant, and a traffic-validation engine. Now I build multi-tool music agents with LangGraph, retrieval, and audio models. My main interest is making AI systems reliable in production: good retrieval, clear evaluation, strong guardrails, and acceptable latency.

**中文思路**：身份 → 安全起步 → 腾讯的 LLM/RAG/流量引擎 → 现在的音乐 Agent → 关注可靠性。

**停顿点**：cybersecurity / applied AI｜alert classification｜Tencent Cloud｜music agents｜reliable in production。

## 60 秒版本

> I’m an AI engineer with a dual background in cybersecurity and applied AI. Over the past ten years, I’ve worked across security engineering, security operations, and AI applications.
>
> At Topsec, I led BERT-based alert classification and built a cloud-native probe with eBPF; we filed several patents. At Tencent Cloud, I worked on LLM-driven security analysis, an enterprise RAG assistant, and a high-throughput traffic-validation engine that cut rule validation from weeks to about four hours.
>
> In my current role, I build a music creation and cover agent. LangGraph coordinates pitch and harmony analysis, voice conversion, and mixing; retrieval and guardrails keep the workflow reliable. I enjoy turning research ideas into production systems, especially around evaluation, failure handling, and latency. I’m looking for a role where I can combine agent engineering, RAG, and system design.

**中文思路**：双线背景 → 天融信（BERT/eBPF/专利）→ 腾讯（LLM 安全/RAG/流量引擎）→ 音乐 Agent → 工程关注点 → 求职方向。

## 2 分钟版本

> I’m an AI engineer with ten years of experience across cybersecurity and AI. My career started on the security side: I worked on WAF engines, situational awareness, and network security probes, and I spent a lot of time on high-performance traffic processing and detection rules.
>
> Around 2020, I moved deeper into applied AI. At Topsec, I led a BERT-based alert-classification project that unified alert taxonomies across product lines. I also built a cloud-native probe with eBPF that kept CPU and memory low under very high event rates, and we filed several patents in SOAR and security operations.
>
> At Tencent Cloud, I worked on three things. First, I helped migrate more than a thousand high-risk WAF rules to a higher-performance engine. Second, I built an LLM-driven security agent: a BERT stage did coarse filtering, and a fine-tuned Qwen model analyzed obfuscated requests; we also built a Go platform to infer detection rules. Third, I built a high-throughput shadow-traffic system that cut rule validation from weeks to about four hours. I also worked on an enterprise RAG assistant with hybrid retrieval, reranking, and prompt-injection defenses.
>
> In my current role, I build a music creation and cover agent. The workflow uses LangGraph and tool calling to coordinate pitch analysis, harmony analysis, voice conversion, and audio post-processing. We combine cross-modal retrieval with guardrails and content checks. The main challenge is balancing creative flexibility with predictable, testable behavior.
>
> Across these projects, I care most about reliability: whether the retrieval is good, whether the output is grounded, how we evaluate it, and what happens when a tool or model fails. I’m looking for a role where I can own AI systems end to end and keep improving them in production.

**中文思路**：安全起步 → 2020 转 AI → 天融信 → 腾讯三件事 → 音乐 Agent → 可靠性主线 → 求职方向。

## 不同岗位的裁剪

| 岗位 | 重点段落 | 可以少讲 |
|---|---|---|
| Agent / RAG 工程师 | LangGraph、工具调用、RAG、评测、护栏 | 早期 WAF 细节 |
| AI 安全工程师 | LLM 安全 Agent、OWASP、提示词注入、合规 | 音乐生成细节 |
| 安全研发 / SecOps | WAF 规则引擎、ATT&CK、SOAR、eBPF、流量验证 | 论文/多模态 |
| 音乐 / 多模态 | 跨模态检索、SVC/RVC、音频评测、版权 | 早期日志分析 |
| 0→1 / 创业团队 | 端到端交付、原型到生产、取舍、成本 | 大团队管理细节 |

## 发音与节奏

| 词 | 提示 |
|---|---|
| cybersecurity | 重音在 **se**curity |
| LangGraph | **Lang**-graph，两个音节清楚 |
| retrieval-augmented generation | 先说全称，再说 RAG |
| evaluation | e-**val**-u-a-tion |
| guardrails | **GUARD**-rails |
| orchestration | /ˌɔːrkɪˈstreɪʃən/，重音在 **stra** |
| latency | **LAY**-ten-cy |
| eBPF | 逐字母：E-B-P-F |
| ATT&CK | 读作 “attack” |
| SOAR | 逐字母或说全称 Security Orchestration, Automation and Response |

## 练习

- [ ] 30 秒版录音，检查是否包含身份、10 年、两个项目、方向
- [ ] 60 秒版录音，检查是否有具体项目和结果
- [ ] 2 分钟版录音，检查时间线和取舍
- [ ] 每个版本各准备一个“缩短到 15 秒”的版本

## 相关

- [[15_resume/_index|简历与自我介绍]]
- [[15_resume/experience|工作经历表达]]
- [[15_resume/projects|项目故事]]
- [[06_interview/introduction|通用自我介绍]]

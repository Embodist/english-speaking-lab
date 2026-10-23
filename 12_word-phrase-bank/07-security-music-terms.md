---
type: word-bank
title: 安全与音乐术语
tags: [library/word-bank, topic/security, topic/music, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# 安全与音乐术语（40）

## 安全分析（20）

| 级别 | 术语 | 中文 | 说（口语例句） | 写（书面例句） | 读 / 搭配 |
|---|---|---|---|---|---|
| S | malicious traffic | 恶意流量 | The system flags malicious traffic for review. | We detect malicious traffic at the gateway. | detect malicious traffic |
| A | anomaly detection | 异常检测 | We use anomaly detection on request patterns. | The anomaly-detection pipeline runs every minute. | anomaly-detection model |
| A | threat intelligence | 威胁情报 | We enrich the alert with threat intelligence. | Threat-intelligence feeds are joined with asset data. | enrich with threat intelligence |
| B | intrusion detection | 入侵检测 | The IDS caught the scan. | Intrusion detection covers north–south traffic. | intrusion-detection system |
| A | WAF | Web 应用防火墙 | The WAF rule was too broad. | The WAF blocks known attack patterns. | Web application firewall |
| S | false positive | 误报 | We need to reduce false positives. | The rule has a high false-positive rate. | reduce false positives |
| A | false negative | 漏报 | False negatives are worse than false positives here. | We measure false negatives on the test set. | avoid false negatives |
| A | alert triage | 告警分诊 | The model helps with alert triage. | Alert triage prioritizes high-risk events. | automate alert triage |
| B | SOAR | 安全编排、自动化与响应 | SOAR automates the response steps. | The SOAR playbook runs the enrichment steps. | Security Orchestration, Automation and Response |
| S | incident response | 事件响应 | We followed the incident-response process. | The incident-response plan defines the on-call owner. | incident-response workflow |
| B | attack surface | 攻击面 | The new endpoint increases the attack surface. | We reduce the attack surface by removing unused services. | reduce the attack surface |
| A | vulnerability | 漏洞 | The scanner found a vulnerability. | The vulnerability was patched in the latest release. | assess a vulnerability |
| A | authentication | 身份认证 | The request failed authentication. | Authentication uses short-lived tokens. | authentication flow |
| A | authorization | 授权 | Authorization is checked per document. | Authorization is enforced at the API layer. | authorization checks |
| A | audit log | 审计日志 | The audit log shows who changed the rule. | Audit logs are retained for one year. | review audit logs |
| S | prompt injection | 提示词注入 | Retrieved text can carry prompt injection. | We treat retrieved content as untrusted input. | defend against prompt injection |
| B | data exfiltration | 数据外泄 | The workflow could leak data, but we block exfiltration. | Guardrails prevent data exfiltration. | prevent data exfiltration |
| A | dry run | 试运行 | Let’s do a dry run before enforcement. | The rule is evaluated in dry-run mode first. | dry-run mode |
| S | human-in-the-loop | 人在环内 | High-impact actions need a human in the loop. | Human-in-the-loop review is required. | human review |
| A | rule recommendation | 规则建议 | The model proposes a WAF rule. | The rule recommendation is reviewed by an analyst. | accept / edit / reject a recommendation |

## 音乐与多模态（20）

| 级别 | 术语 | 中文 | 说（口语例句） | 写（书面例句） | 读 / 搭配 |
|---|---|---|---|---|---|
| S | music generation | 音乐生成 | The agent supports music generation. | Music generation is conditioned on style tags. | music-generation model |
| S | cover generation | 翻唱生成 | We support cover generation from a reference song. | The cover-generation step preserves the melody. | cover generation |
| A | source separation | 音源分离 | We separate the vocal track first. | Source separation isolates vocals and instruments. | vocal / instrumental stem |
| A | vocal conversion | 人声转换 | The system converts the vocal timbre. | Vocal conversion keeps the melody and changes the timbre. | timbre conversion |
| A | SVC | 歌声转换 | SVC changes the singer’s voice. | SVC is used to convert the singing voice. | singing voice conversion |
| A | RVC | 检索式声音转换 | RVC is one of the conversion backends. | RVC uses retrieval-based voice conversion. | Retrieval-based Voice Conversion |
| A | pitch analysis | 音高分析 | We extract pitch before generation. | Pitch analysis produces a frame-level contour. | pitch contour |
| A | harmony analysis | 和声分析 | Harmony analysis guides the arrangement. | Harmony analysis estimates chord progressions. | chord progression |
| A | audio embedding | 音频嵌入 | We encode the audio into an embedding. | Audio embeddings support similarity search. | audio embedding |
| S | cross-modal retrieval | 跨模态检索 | We retrieve audio that matches a text description. | Cross-modal retrieval aligns text and audio embeddings. | cross-modal alignment |
| B | CLAP | 音频—文本对齐模型 | CLAP maps text and audio into one space. | CLAP is used for text-to-audio retrieval. | audio–text contrastive model |
| B | MERT | 音乐理解模型 | MERT provides music-aware representations. | MERT features are used for music understanding. | music representation model |
| A | similarity score | 相似度分数 | We rank candidates by similarity score. | Candidates are ranked by cosine similarity. | cosine similarity |
| A | sampling | 采样 | The sampling settings change the output. | Sampling temperature controls diversity. | sampling parameters |
| B | seed | 随机种子 | We fix the seed for reproducibility. | A fixed random seed is used in all runs. | fixed seed |
| A | batch inference | 批量推理 | We run batch inference overnight. | Batch inference improves GPU utilization. | batch inference |
| A | streaming output | 流式输出 | The result streams back to the client. | Streaming output reduces perceived latency. | stream the output |
| A | audio post-processing | 音频后期处理 | We apply loudness normalization in post-processing. | Post-processing includes normalization and limiting. | post-processing chain |
| A | copyright check | 版权检查 | We run a copyright check before delivery. | The pipeline includes a copyright check. | copyright guardrail |
| S | guardrail | 防护规则 | Guardrails block unsafe or infringing output. | Guardrails are applied before the final response. | safety guardrail |

## 讲项目的三句话

1. **输入**：`The user describes the style in natural language.`
2. **处理**：`The agent retrieves references and coordinates generation and conversion tools.`
3. **约束**：`We validate outputs, check copyright, and keep the workflow observable.`

## 练习

- [ ] 选 8 个安全词，模拟一次告警分诊
- [ ] 选 8 个音乐词，讲 60 秒项目链路
- [ ] 用“三句话”录 90 秒

## 相关

- [[12_word-phrase-bank/_index|词与短语库]]
- [[04_security/_index|安全分析]]
- [[05_music-agent/_index|音乐 Agent]]
- [[13_tech-frameworks/music-ai-stack|音乐 AI 技术栈]]

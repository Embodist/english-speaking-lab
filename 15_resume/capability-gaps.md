---
type: guide
title: 能力补充清单
tags: [skill/interview, guide]
created: 2026-10-24
updated: 2026-10-24
---

# 能力补充清单

> 目标：把“做过很多”变成“讲得清楚、可验证、有边界”。下面按优先级列出还可以补充的内容。

## 一、你的强项（先守住）

| 强项 | 面试价值 |
|---|---|
| 10 年安全 + AI 双线 | 少见的复合背景，能做 AI 安全、也能做安全 AI |
| Agent/RAG 落地 | LangGraph、工具调用、混合检索、重排、护栏 |
| 大规模系统 | 10B 级流量验证、千万级事件/秒探针、规则引擎重构 |
| 可量化结果 | 数周 → 4 小时、85% QA、7 项专利、RMB 2M+ |
| 工程语言 | Python / Go / C++、eBPF、Docker/K8s |
| 安全纵深 | WAF/IPS、ATT&CK、SOAR、OWASP LLM Top 10 |

## 二、P0：面试前必须补齐

### 1. 数字口径

简历里的数字很强，但必须能解释“怎么算的”：

- [ ] `10B 级流量`：请求/天？事件/天？包/秒？单集群还是全量？
- [ ] `85% 长文本 QA`：数据集、样本量、指标（准确率/人工评分）、评测集是否留出？
- [ ] `规则验证数周 → 4 小时`：单条规则、批量规则、还是整条流水线？
- [ ] `7 项专利`：已授权/申请中？你是第一发明人还是参与？
- [ ] `千万级事件/秒`：硬件核数、包大小、检测深度、是否采样？
- [ ] `CPU/内存 <1%`：单核、整机、容器？什么负载下？
- [ ] `15% 漏报/误报`：数据集、统计方式、是否线上真实流量？
- [ ] `RMB 2M+`：计算口径、时间范围、是否可归因到你？

> 不确定就说 “I’d need to check the exact measurement.” 不要临场编。

### 2. 个人贡献边界

每个项目准备一句：

- `My contribution was mainly …`
- `I owned … end to end.`
- `That part was led by another team; I contributed …`

重点区分：**你写的代码 / 你带的团队 / 你协调的资源**。

### 3. 评测方法

面试官会追问“你怎么知道它变好了”：

- RAG：Recall@k、忠实度、答案相关性、人工抽检、留出集
- Agent：工具选择正确率、端到端成功率、失败恢复、延迟、成本
- 安全：precision/recall、误报/漏报、分析师审核时间、dry run
- 音乐：固定 rubric、多人评分、旋律保持、音色相似度、自然度

### 4. 音乐 Agent 的产品结果

简历更多是技术描述，补充：

- 用户规模 / 日活 / 生成量
- 生成成功率、平均耗时、单次成本
- 用户留存或满意度（如果有）
- 版权/内容安全的拦截率与人工审核量

没有数据就准备“工程结果”：延迟下降、失败率下降、可恢复性提升。

### 5. 团队与领导力

- 团队规模、汇报关系、你带了几个人
- 一次 mentoring / code review / 跨团队协调的具体例子
- 一次技术分歧如何解决
- 一次失败或延期如何复盘

## 三、P1：技术深度补充

### 6. 模型服务

- vLLM 的关键点：PagedAttention、continuous batching、TTFT/TPS、显存管理
- 你的部署：GPU 型号、并发、p95、成本、限流/降级
- 量化/批处理/缓存的实际取舍

### 7. 微调与数据

- SFT/LoRA 的数据来源、清洗、去重、标注
- 训练/验证/测试切分，防止泄漏
- 失败案例：过拟合、格式不稳定、灾难性遗忘
- 评估：自动指标 + 人工抽检 + 线上反馈

### 8. Agent 可靠性

- 状态持久化、恢复、幂等
- 有界重试、超时、降级
- 工具参数校验、最小权限、人工审批
- 可观测性：每次工具调用、token、延迟、错误分类
- 防止循环失控与成本爆炸

### 9. 安全与合规

- OWASP LLM Top 10 逐项映射到你的项目
- 提示词注入测试集、红队演练
- 工具越权、数据外泄、敏感信息脱敏
- 版权检查、Deepfake/声音克隆授权
- 人工审核与审计日志

### 10. 成本与延迟

- 每次请求的 token 成本、模型路由、缓存命中
- 上下文长度与成本的关系
- 什么时候用小模型、什么时候用大模型

## 四、P2：表达与材料

### 11. 简历呈现

- 国际岗位建议去掉生日、照片、政治面貌、详细住址；保留城市、GitHub、邮箱
- 统一时态：当前岗位用现在时，过去岗位用过去时
- 首次出现缩写写全称：RAG、SVC、SOAR、ATT&CK、eBPF
- 数字带单位；区分团队成果与个人成果
- 少用 “expert”，多用 “hands-on experience with …”
- 内部系统代号（Tiga/Menshen 等）按保密要求处理

### 12. 作品与影响力

- GitHub 项目、demo、技术文章、专利状态
- 一个 5 分钟的项目讲解视频或录音
- 开源贡献 / 社区分享（如果有）

### 13. 英语表达

- 30/60/120 秒自我介绍各录 3 版
- 每个项目 30/90 秒各一版
- 每周一次 15 分钟模拟面试
- 技术词发音见 [[15_resume/keywords|关键词发音]]

## 五、必准备的 10 个问题

1. Why did you move from cybersecurity to AI engineering?
2. Walk me through your resume.
3. What is the project you’re most proud of? Why?
4. How do you evaluate a RAG system?
5. How do you evaluate an agent?
6. How do you prevent prompt injection and tool abuse?
7. How would you debug a bad answer or a failed workflow?
8. Describe a difficult technical problem and how you solved it.
9. Tell me about a disagreement with a teammate.
10. Why this role, and what do you want to do in the next two years?

## 六、7 天补齐计划

| 天 | 任务 |
|---|---|
| Day 1 | 把 8 个数字口径写清楚；不确定的标注“需要确认” |
| Day 2 | 30 秒 / 60 秒自我介绍录音 |
| Day 3 | 音乐 Agent 30/90 秒 + 5 个追问 |
| Day 4 | 安全 Agent + 流量引擎 30/90 秒 |
| Day 5 | RAG 项目 30/90 秒 + 评测追问 |
| Day 6 | 行为面试 3 个 STAR 故事 |
| Day 7 | 15 分钟模拟面试，回听并只改 3 个问题 |

## 相关

- [[15_resume/_index|简历与自我介绍]]
- [[15_resume/self-introduction|自我介绍]]
- [[15_resume/experience|工作经历表达]]
- [[15_resume/projects|项目故事]]
- [[15_resume/keywords|关键词发音]]

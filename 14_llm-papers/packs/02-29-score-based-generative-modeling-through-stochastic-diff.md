---
type: paper-pack
paper_id: "02-29"
stage: 2
title: "Score-Based Generative Modeling through Stochastic Differential Equations"
pdf: "/home/user/llm-papers/02_多模态/PDF/29_ScoreBased_SDE.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-29 Score-Based Generative Modeling through Stochastic Differential Equations

**中文标题**：基于随机微分方程的基于分数的生成建模

**一句话概括**：提出用随机微分方程（SDE）及其反向过程统一基于分数的生成模型与扩散概率模型，并引入预测-校正框架、等价神经 ODE 与逆问题求解，创下无条件图像生成纪录。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| leverage | /lˈiːvəɹɪdʒ/ | 利用、借助（已有成果） | S |
| fidelity | /fɪdˈɛlɪti/ | 保真度；生成图像与真实图像的接近程度 | S |
| inpainting | /ˈɪnpeɪntɪŋ/ | 图像修复/补全；实验中验证的逆问题任务 | A |
| estimate | /ˈɛstɪmət/ | 估计；用神经网络近似计算分数（梯度场） | A |
| diffusion | /dɪfjˈuːʒən/ | 扩散；扩散概率建模，与本文方法并列的生成范式 | A |
| likelihood | /lˈaɪklihˌʊd/ | 似然；精确计算数据概率的能力 | A |
| stochastic | /stətʃˈastɪk/ | 随机的；本文指引入随机噪声的微分方程 | A |
| transform | /tɹansfˈɔːm/ | 变换、转化；把数据分布平滑地转为噪声分布 | A |
| prior distribution | /pɹˈaɪə dˌɪstɹɪbjˈuːʃən/ | 先验分布；噪声所在的已知简单分布 | B |
| reverse-time | /ɹɪvˈɜːstˈaɪm/ | 反向时间的；从先验分布还原回数据分布的 | B |
| solver | /sˈɒlvə/ | 求解器；数值求解微分方程的程序 | B |
| encapsulate | /ɛŋkˈapsjʊlˌeɪt/ | 囊括、涵盖；统一了此前多种方法 | B |

### 原句（保留完整句子）

- **leverage** — “Later in January 2020, GPT-2 was fine- problems, spanning a diverse range of difficult tasks, and tuned using the aforementioned RL algorithms \[79, 128\], showed that GPT-4 can achieve more superior performance which leveraged human preferences to improve the capac- than prior GPT models.”
- **fidelity** — “Overall, the the world...the more accurate you are in predicting the next research of OpenAI on LLMs can be roughly divided into word, the higher the fidelity, the more resolution you get in the following stages13 . this process...”16 .”
- **inpainting** — “From the initial melody generation to now, score generation covers polyphonic music generation, accompaniment generation, style transfer, interactive generation, music inpainting and so on.”
- **estimate** — “We estimate the number of floating point operations used to train a model by multiplying the training time, the number of GPUs used, and an estimate of the sustained single-precision floating-point capacity of each GPU 5 .”
- **diffusion** — “As for LLMs, unstructured supporting other model compression methods. pruning can generally lead to higher compression rates. • Torch-Pruning 53 is a toolkit developed for generalFor instance, SparseGPT \[1020\] achieves 60% unstructured purpose structural pruning, including the pruning for vision sparsity for OPT-175B using unstructured pruning (i.e., models, diffusion models and large language models.”
- **likelihood** — “In general, LM aims to model the generative likelihood Thus, specially designed smoothing strategies such as backof word sequences, so as to predict the probabilities of off estimation \[15\] and Good–Turing estimation \[16\] have future (or missing) tokens.”
- **stochastic** — “Adam: A method for stochastic optimization.”
- **transform** — “Since onthe distribution of the sources of pre-training data for a line conversational data often involves discussions among number of representative LLMs. multiple participants, an effective processing way is to transform a conversation into a tree structure, where the The source of pre-training corpus can be broadly cateutterance is linked to the one it responds to.”
- **prior distribution** — “"a known prior distribution by slowly injecting noise"”
- **reverse-time** — “"a corresponding reverse-time SDE that transforms the prior"”
- **solver** — “In the field of NLP, LLMs can serve as a nical concept specially for LLMs, but has evolved with the general-purpose language task solver (to some extent), and advance of artificial intelligence over the decades.”
- **encapsulate** — “In this way, the tools should be encapsulated into callable APIs with detailed description about their functions, to Other Designs better guide the LLM to utilize the tools.”

## 摘要提示（PDF 文本不可提取）

> TITLE: Score-Based Generative Modeling through Stochastic Differential Equations ABSTRACT: Creating noise from data is easy; creating data from noise is generative modeling. We present a stochastic differential equation (SDE) that smoothly transforms a complex data distribution to a known prior distribution by slowly injecting noise, and a corresponding reverse-time SDE that transforms the prior distribution back into the data distribution by slowly removing the noise. Crucially, the reverse-time SDE depends only on the time-dependent gradient field (\aka, score) of the perturbed data distribution. By leveraging advances in score-based generative modeling, we can accurately estimate these scores with neural networks, and use numerical SDE solvers to generate samples. We show that this framework encapsulates previous approaches in score-based generative modeling and diffusion probabilistic modeling, allowing for new sampling procedures and new modeling capabilities. In particular, we introduce a predictor-corrector framework to correct errors in the evolution of the discretized reverse-time SDE. We also derive an equivalent neural ODE that samples from the same distribution as the SDE, but additionally enables exact likelihood computation, and improved sampling efficiency. In addition, we provide a new way to solve inverse problems with score-based models, as demonstrated with e

## 读中 30 分钟

- [ ] 问题：这篇论文解决什么？
- [ ] 方法：核心组件和数据流是什么？
- [ ] 数据/指标：在哪些数据集、用什么指标？
- [ ] 结果：主结果和消融说明了什么？
- [ ] 局限：作者承认什么？我还有什么疑问？

## 5 个理解问题

1. What problem does the paper address, and why does it matter?
2. What is the key idea, and what does it replace or improve?
3. What data, baselines, and metrics are used?
4. Which result is the most convincing, and which is weakest?
5. What is one limitation, and what would you test next?

## 60 秒复述

> The paper addresses … The authors propose … The key idea is … They evaluate on … The results show … One limitation is …

录音：`11_attachments/`

## 写 3 句

- The paper addresses …
- The key idea is …
- One limitation is …

## 词汇复习

- 把上面 10–12 个词加入 Anki；先读原句，再看中文。
- 词库入口：[[14_llm-papers/vocabulary-10k/_index|论文 10k 词库]]

## 相关

- [[14_llm-papers/reading-plan|12 周阅读计划]]
- [[14_llm-papers/stage-02-multimodal|阶段 2]]

PDF：`/home/user/llm-papers/02_多模态/PDF/29_ScoreBased_SDE.pdf`

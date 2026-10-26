---
type: paper-pack
paper_id: "02-28"
stage: 2
title: "Denoising Diffusion Implicit Models"
pdf: "/home/user/llm-papers/02_多模态/PDF/28_DDIM.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-28 Denoising Diffusion Implicit Models

**中文标题**：去噪扩散隐式模型

**一句话概括**：提出 DDIM，构造一类非马尔可夫扩散过程，用与 DDPM 相同的训练目标实现快 10–50 倍的采样，并支持隐空间语义插值。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| latent space | /lˈeɪtənt spˈeɪs/ | 隐空间（低维特征空间） | S |
| objective | /ɒbdʒˈɛktɪv/ | 目标（函数）（与 DDPM 相同的训练目标） | A |
| simulate | /sˈɪmjʊlˌeɪt/ | 模拟（一步步模拟马尔可夫链） | A |
| accelerate | /ɐksˈɛləɹˌeɪt/ | 加速（加快采样速度） | A |
| implicit | /ɪmplˈɪsɪt/ | 隐式的（不显式依赖马尔可夫性质的过程） | A |
| empirically | /ɛmpˈɪɹɪkli/ | 实验上、凭经验地（通过实验证明） | A |
| trade off | /tɹˈeɪd ˈɒf/ | 权衡（用计算量换样本质量） | A |
| Markov chain | /mˈɑːkɒv tʃˈeɪn/ | 马尔可夫链（状态转移只依赖当前状态的随机过程） | A |
| wall-clock time | /wˈɔːlklˈɒk tˈaɪm/ | 墙钟时间（实际经过的真实时间） | A |
| semantically | /səmˈantɪkli/ | 语义上（在语义层面有意义） | A |
| interpolation | /ɪntˌɜːpəlˈeɪʃən/ | 插值（在两个点之间平滑过渡） | A |
| adversarial training | /ˌadvəsˈeəɹɪəl tɹˈeɪnɪŋ/ | 对抗训练（生成对抗网络的训练方式，本文无需使用） | B |

### 原句（保留完整句子）

- **latent space** — “"in the latent space of powerful"”
- **objective** — “Existing LLMs adopt similar Trans- α β where a = α+β , b = α+β and G is a scaling coefficient that former architectures and pre-training objectives (e.g., lancan be computed by A, B , α and β .”
- **simulate** — “BOX, where the model simulates social interactions with • Alpaca \[146\] is also a synthetic dataset based on the self- other models and revise responses according to the feedback instruct \[147\] method.”
- **accelerate** — “Lukasz and Aidan spent countless long days designing various parts of and implementing tensor2tensor, replacing our earlier codebase, greatly improving results and massively accelerating our research. † Work performed while at Google Brain. ‡ Work performed while at Google Research.”
- **implicit** — “Long context modeling is an important it is important to identify more implicit relations between ability for LLMs, and many studies have explored extenddata sources and model abilities.”
- **empirically** — “We a compute budget c, they empirically presented three basic are also aware of several related review articles on PLMs formulas for the scaling law6 : or LLMs \[32, 36, 38, 39, 43, 48–54\].”
- **trade off** — “"trade off diversity for fidelity"”
- **Markov chain** — “"a Markov chain for many steps"”
- **wall-clock time** — “"in terms of wall-clock time compared"”
- **semantically** — “LLMs are shown to sometimes suffer retriever to select examples that are semantically relevant to from the recency bias, i.e., they are prone to repeat answers the query \[420, 482\].”
- **interpolation** — “With modifications on position embeddings specialized LLMs, a practical way is to employ a multi-stage (i.e., position interpolation) of RoPE-based LLMs \[57, 99, training approach, e.g., general and skill-specific data can 259\], CodeLLaMA further extends the context window of be scheduled at two consecutive stages.”
- **adversarial training** — “"without adversarial training, yet they require"”

## 摘要提示（PDF 文本不可提取）

> TITLE: Denoising Diffusion Implicit Models ABSTRACT: Denoising diffusion probabilistic models (DDPMs) have achieved high quality image generation without adversarial training, yet they require simulating a Markov chain for many steps to produce a sample. To accelerate sampling, we present denoising diffusion implicit models (DDIMs), a more efficient class of iterative implicit probabilistic models with the same training procedure as DDPMs. In DDPMs, the generative process is defined as the reverse of a Markovian diffusion process. We construct a class of non-Markovian diffusion processes that lead to the same training objective, but whose reverse process can be much faster to sample from. We empirically demonstrate that DDIMs can produce high quality samples $10 \times$ to $50 \times$ faster in terms of wall-clock time compared to DDPMs, allow us to trade off computation for sample quality, and can perform semantically meaningful image interpolation directly in the latent space.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/28_DDIM.pdf`

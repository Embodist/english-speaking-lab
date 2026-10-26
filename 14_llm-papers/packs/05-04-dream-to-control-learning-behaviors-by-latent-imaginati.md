---
type: paper-pack
paper_id: "05-04"
stage: 5
title: "Dream to Control: Learning Behaviors by Latent Imagination"
pdf: "/home/user/llm-papers/05_世界模型/PDF/04_Dreamer.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 05-04 Dream to Control: Learning Behaviors by Latent Imagination

**中文标题**：梦控：通过潜空间想象学习行为（Dreamer）

**一句话概括**：提出 Dreamer 强化学习智能体，仅凭图像输入，把学到的状态价值的解析梯度沿世界模型潜空间中"想象"出的轨迹回传，从而高效学习长时程任务的行为。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| long-horizon | /lˈɒŋhəɹˈaɪzən/ | 长时程的；需要很多步才能完成的任务 | A |
| trajectories | /tɹədʒˈɛktəɹiz/ | 轨迹；一系列状态-动作序列 | A |
| feasible | /fˈiːzɪbəl/ | 可行的 | A |
| latent imagination | /lˈeɪtənt ɪmˌadʒɪnˈeɪʃən/ | 潜空间想象；在世界模型的潜空间中想象未来轨迹 | A |
| high-dimensional | /hˈaɪdaɪmˈɛnʃənəl/ | 高维的；维度很多的输入 | A |
| propagate | /pɹˈɒpɐɡˌeɪt/ | 传播、回传（梯度） | A |
| facilitate | /fəsˈɪlɪtˌeɪt/ | 促进、有助于 | A |
| analytic gradients | /ˌanɐlˈɪtɪk ɡɹˈeɪdiənts/ | 解析梯度；直接求导得到的精确梯度 | B |
| sensory inputs | /sˈɛnsəɹi ˈɪnpʊts/ | 感官输入；如图像等观测数据 | B |
| summarize | /sˈʌməɹˌaɪz/ | 概括、总结 | B |
| derive | /dɪɹˈaɪv/ | 推导、得出 | B |
| data-efficiency | /dˈeɪtəɹɪfˈɪʃənsi/ | 数据效率；用少量数据学到好性能 | B |

### 原句（保留完整句子）

- **long-horizon** — “We present Dreamer, a reinforcement learning agent that solves long-horizon tasks from images purely by latent imagination.”
- **trajectories** — “We efficiently learn behaviors by propagating analytic gradients of learned state values back through trajectories imagined in the compact state space of a learned world model.”
- **feasible** — “Learning effective latent dynamics models is becoming feasible through advances in deep learning and latent variable models (Krishnan et al., 2015; Karl et al., 2016; Doerr et al., 2018; Buesing et al., 2018).”
- **latent imagination** — “We present Dreamer, a reinforcement learning agent that solves long-horizon tasks from images purely by latent imagination.”
- **high-dimensional** — “When the sensory inputs are high-dimensional images, latent dynamics models can abstract observations to predict forward in compact state spaces Learned Latent Dynamics (Watter et al., 2015; Oh et al., 2017; Gregor et al., 2019).”
- **propagate** — “For this, we propagate stochastic gradients of multi-step returns through neural network predictions of actions, states, rewards, and values using reparameterization.”
- **facilitate** — “To facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension dmodel = 512.”
- **analytic gradients** — “We efficiently learn behaviors by propagating analytic gradients of learned state values back through trajectories imagined in the compact state space of a learned world model.”
- **sensory inputs** — “When the sensory inputs are high-dimensional images, latent dynamics models can abstract observations to predict forward in compact state spaces Learned Latent Dynamics (Watter et al., 2015; Oh et al., 2017; Gregor et al., 2019).”
- **summarize** — “Table 2 summarizes our results and compares our translation quality and training costs to other model architectures from the literature.”
- **derive** — “Finally, we conclude the survey in were derived by fitting the model performance with varied Section 10 by summarizing the major findings and discuss data sizes (22M to 23B tokens), model sizes (768 to 1.5B nonthe remaining issues for future work. embedding parameters) and training compute, under some assumptions (e.g., the analysis of one factor should be not bottlenecked by the other two factors).”
- **data-efficiency** — “On 20 challenging visual control tasks, Dreamer exceeds existing approaches in data-efficiency, computation time, and final performance.”

## Abstract（自动提取）

> TITLE: Dream to Control: Learning Behaviors by Latent Imagination ABSTRACT: Learned world models summarize an agent's experience to facilitate learning complex behaviors. While learning world models from high-dimensional sensory inputs is becoming feasible through deep learning, there are many potential ways for deriving behaviors from them. We present Dreamer, a reinforcement learning agent that solves long-horizon tasks from images purely by latent imagination. We efficiently learn behaviors by propagating analytic gradients of learned state values back through trajectories imagined in the compact state space of a learned world model. On 20 challenging visual control tasks, Dreamer exceeds existing approaches in data-efficiency, computation time, and final performance.

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
- [[14_llm-papers/stage-05-world-models|阶段 5]]

PDF：`/home/user/llm-papers/05_世界模型/PDF/04_Dreamer.pdf`

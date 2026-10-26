---
type: paper-pack
paper_id: "05-19"
stage: 5
title: "Diffusion Models Are Real-Time Game Engines"
pdf: "/home/user/llm-papers/05_世界模型/PDF/19_GameNGen.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 05-19 Diffusion Models Are Real-Time Game Engines

**中文标题**：扩散模型即实时游戏引擎（GameNGen）

**一句话概括**：提出 GameNGen，首个完全由神经模型驱动的游戏引擎：在 DOOM 上以 20 FPS 实时交互模拟新轨迹且长时间稳定；两阶段训练——先用 RL 智能体录制游戏过程，再训练扩散模型按过去帧与动作预测下一帧。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| fidelity | /fɪdˈɛlɪti/ | 保真度；与真实情况的吻合程度 | S |
| trajectories | /tɹədʒˈɛktəɹiz/ | 轨迹；连续的状态序列 | A |
| conditioned on | /kəndˈɪʃənd ˈɒn/ | 以……为条件；给定…… | A |
| auto-regressive | /ˈɔːtəʊɹɪɡɹˈɛsɪv/ | 自回归的；基于过去逐步生成未来 | A |
| extract | /ˈɛkstɹakt/ | 提取 | A |
| conditioning augmentations | /kəndˈɪʃənɪŋ ˌɔːɡmɛntˈeɪʃənz/ | 条件增强；对条件输入做数据增强 | B |
| lossy JPEG compression | /lˈɒsi dʒˈeɪpˈɛɡ kəmpɹˈɛʃən/ | 有损 JPEG 压缩；会丢失信息的压缩 | B |
| real-time interaction | /ɹˈiəltˈaɪm ˌɪntəɹˈakʃən/ | 实时交互 | B |
| PSNR | /pˌiːˌɛsˌɛnˈɑː/ | 峰值信噪比；衡量图像质量的指标 | B |
| human raters | /hjˈuːmən ɹˈeɪtəz/ | 人类评分员 | B |
| powered entirely by | /pˈaʊəd ɛntˈaɪəli bˈaɪ/ | 完全由……驱动 | B |
| playable environment | /plˈeɪəbəl ɛnvˈaɪɹənmənt/ | 可玩的环境 | B |

### 原句（保留完整句子）

- **fidelity** — “Overall, the the world...the more accurate you are in predicting the next research of OpenAI on LLMs can be roughly divided into word, the higher the fidelity, the more resolution you get in the following stages13 . this process...”16 .”
- **trajectories** — “"generates human-like task-solving trajectories that are more interpretable"”
- **conditioned on** — “"When conditioned on a document plus questions"”
- **auto-regressive** — “At each step the model is auto-regressive \[10\], consuming the previously generated symbols as additional input when generating the next.”
- **extract** — “As the whole dataset is much larger than BookCorpus but have not been publicly very large, existing studies mainly extract subsets of web released so far. pages from it within a specific period or specific needs • Academic Data.”
- **conditioning augmentations** — “Conditioning augmentations help ensure stable auto-regressive generation”
- **lossy JPEG compression** — “comparable to lossy JPEG compression”
- **real-time interaction** — “enables real-time interaction with a complex environment”
- **PSNR** — “Reconstruction FIDs \[29\] and PSNR are tecture, we turn diffusion models into powerful and flexi- calculated on ImageNet-val. \[12\]; see also Tab.”
- **human raters** — “Human raters are only slightly better than random chance”
- **powered entirely by** — “the first game engine powered entirely by a neural model”
- **playable environment** — “generate a playable environment”

## 摘要提示（PDF 文本不可提取）

> TITLE: Diffusion Models Are Real-Time Game Engines ABSTRACT: We present GameNGen, the first game engine powered entirely by a neural model that also enables real-time interaction with a complex environment over long trajectories at high quality. When trained on the classic game DOOM, GameNGen extracts gameplay and uses it to generate a playable environment that can interactively simulate new trajectories. GameNGen runs at 20 frames per second on a single TPU and remains stable over extended multi-minute play sessions. Next frame prediction achieves a PSNR of 29.4, comparable to lossy JPEG compression. Human raters are only slightly better than random chance at distinguishing short clips of the game from clips of the simulation, even after 5 minutes of auto-regressive generation. GameNGen is trained in two phases: (1) an RL-agent learns to play the game and the training sessions are recorded, and (2) a diffusion model is trained to produce the next frame, conditioned on the sequence of past frames and actions. Conditioning augmentations help ensure stable auto-regressive generation over long trajectories, and decoder fine-tuning improves the fidelity of visual details and text.

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

PDF：`/home/user/llm-papers/05_世界模型/PDF/19_GameNGen.pdf`

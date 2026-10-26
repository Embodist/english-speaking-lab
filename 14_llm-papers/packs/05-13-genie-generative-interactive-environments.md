---
type: paper-pack
paper_id: "05-13"
stage: 5
title: "Genie: Generative Interactive Environments"
pdf: "/home/user/llm-papers/05_世界模型/PDF/13_Genie_GenerativeInteractiveEnvironments.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 05-13 Genie: Generative Interactive Environments

**中文标题**：Genie：生成式交互环境

**一句话概括**：提出 Genie，首个完全由无标注互联网视频无监督训练的生成式交互环境（11B 参数），由时空视频分词器、自回归动力学模型与潜动作模型组成，无需真实动作标签即可生成可控虚拟世界并支持逐帧交互。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| spatiotemporal | /spˈatɪˌəʊtmpəɹəl/ | 时空的；同时含空间与时间维度 | A |
| imitate | /ˈɪmɪtˌeɪt/ | 模仿 | A |
| ground-truth | /ɡɹˈaʊndtɹˈuːθ/ | 真实标注的；与真实情况一致的标签 | B |
| tokenizer | /tˈəʊkənˌaɪzə/ | 分词器/令牌化器；把视频变成离散 token | B |
| foundation world model | /faʊndˈeɪʃən wˈɜːld mˈɒdəl/ | 基础世界模型；类似基础大模型的通用世界模型 | B |
| action-controllable | /ˈakʃəŋkəntɹˈəʊləbəl/ | 可动作控制的；用户能通过动作操控 | B |
| unlabelled | /ʌnlˈeɪbəld/ | 无标注的 | B |
| latent action space | /lˈeɪtənt ˈakʃən spˈeɪs/ | 潜动作空间；学到的隐式动作表示 | B |
| generalist agents | /dʒˈɛnəɹəlˌɪst ˈeɪdʒənts/ | 通才智能体；能完成多种任务的智能体 | B |
| synthetic images | /sɪnθˈɛtɪk ˈɪmɪdʒɪz/ | 合成图像；程序生成的图像 | B |
| frame-by-frame | /fɹˈeɪmbaɪfɹˈeɪm/ | 逐帧地；一帧一帧地 | B |
| comprised of | /kəmpɹˈaɪzd ˈɒv/ | 由……组成 | B |

### 原句（保留完整句子）

- **spatiotemporal** — “It is comprised of a spatiotemporal video tokenizer, an autoregressive dynamics model, and a simple and scalable latent action model.”
- **imitate** — “Further the resulting learned latent action space facilitates training agents to imitate behaviors from unseen videos, opening the path for training generalist agents of the future.”
- **ground-truth** — “Genie enables users to act in the generated environments on a frame-by-frame basis despite training without any ground-truth action labels or other domain-specific requirements typically found in the world model literature.”
- **tokenizer** — “It is comprised of a spatiotemporal video tokenizer, an autoregressive dynamics model, and a simple and scalable latent action model.”
- **foundation world model** — “At 11B parameters, Genie can be considered a foundation world model.”
- **action-controllable** — “Inference: Action-Controllable Video Gen- 16s video clips at 10FPS, with 160x90 resolution. eration The final dataset contains 6.8M 16s video clips (30k hours), within an order of magnitude of We now describe how to use Genie for actionother popular Internet video datasets (Bain et al., controllable video generation at inference time 2021; Wang et al., 2023).”
- **unlabelled** — “We introduce Genie, the first generative interactive environment trained in an unsupervised manner from unlabelled Internet videos.”
- **latent action space** — “Further the resulting learned latent action space facilitates training agents to imitate behaviors from unseen videos, opening the path for training generalist agents of the future.”
- **generalist agents** — “Further the resulting learned latent action space facilitates training agents to imitate behaviors from unseen videos, opening the path for training generalist agents of the future.”
- **synthetic images** — “The model can be prompted to generate an endless variety of actioncontrollable virtual worlds described through text, synthetic images, photographs, and even sketches.”
- **frame-by-frame** — “Genie enables users to act in the generated environments on a frame-by-frame basis despite training without any ground-truth action labels or other domain-specific requirements typically found in the world model literature.”
- **comprised of** — “It is comprised of a spatiotemporal video tokenizer, an autoregressive dynamics model, and a simple and scalable latent action model.”

## Abstract（自动提取）

> TITLE: Genie: Generative Interactive Environments ABSTRACT: We introduce Genie, the first generative interactive environment trained in an unsupervised manner from unlabelled Internet videos. The model can be prompted to generate an endless variety of action-controllable virtual worlds described through text, synthetic images, photographs, and even sketches. At 11B parameters, Genie can be considered a foundation world model. It is comprised of a spatiotemporal video tokenizer, an autoregressive dynamics model, and a simple and scalable latent action model. Genie enables users to act in the generated environments on a frame-by-frame basis despite training without any ground-truth action labels or other domain-specific requirements typically found in the world model literature. Further the resulting learned latent action space facilitates training agents to imitate behaviors from unseen videos, opening the path for training generalist agents of the future.

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

PDF：`/home/user/llm-papers/05_世界模型/PDF/13_Genie_GenerativeInteractiveEnvironments.pdf`

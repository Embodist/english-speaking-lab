---
type: paper-pack
paper_id: "05-24"
stage: 5
title: "V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning"
pdf: "/home/user/llm-papers/05_世界模型/PDF/24_VJEPA2.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 05-24 V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

**中文标题**：V-JEPA 2：自监督视频模型实现理解、预测与规划

**一句话概括**：提出自监督方法 V-JEPA 2：用超 100 万小时互联网视频预训练无动作的联合嵌入预测架构，再与大语言模型对齐，并在不到 62 小时机器人视频上后训练出动作条件世界模型 V-JEPA 2-AC，零样本部署到 Franka 机械臂实现抓放规划。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| zero-shot | /zˈiəɹəʊʃˈɒt/ | 零样本的；无需额外数据直接部署 | S |
| aligning | /ɐlˈaɪnɪŋ/ | 对齐；把两个模型的特征空间对齐 | A |
| post-training | /pˈəʊsttɹˈeɪnɪŋ/ | 后训练；预训练后的继续训练 | A |
| task-specific | /tˈaskspəsˈɪfɪk/ | 任务特定的 | A |
| action anticipation | /ˈakʃən antˈɪsɪpˈeɪʃən/ | 动作预测；提前预测将要发生的动作 | B |
| action-conditioned | /ˈakʃəŋkəndˈɪʃənd/ | 以动作为条件的 | B |
| action-free | /ˈakʃənfɹˈiː/ | 不含动作输入的 | B |
| recall-at-5 | /ɹˈiːkɔːlat  fˈaɪv/ | Top-5 召回率；检索类评估指标 | B |
| internet-scale | /ˈɪntənˌɛtskˈeɪl/ | 互联网规模的；数据量巨大 | B |
| comprising | /kəmpɹˈaɪzɪŋ/ | 包含、由……组成 | B |
| largely by observation | /lˈɑːdʒli bˈaɪ ɒbzəvˈeɪʃən/ | 主要依靠观察 | B |
| question-answering | /kwˈɛstʃənˈansəɹɪŋ/ | 问答（任务） | B |

### 原句（保留完整句子）

- **zero-shot** — “In the neural networks to a significant size can lead to a huge the GPT-3’s paper, it formally introduced the concept of increase in model capacity. in-context learning (ICL)17 , which utilizes LLMs in a fewshot or zero-shot way.”
- **aligning** — “"method for aligning pre-trained language models with instructions"”
- **post-training** — “Existing decoding methods proaches, namely quantization-aware training (QAT) (requirpredominantly adopt the autoregressive mechanism, gen- ing additional full model retraining) and post-training quantierating tokens one by one, which is a primary reason zation (PTQ) (requires no model retraining).”
- **task-specific** — “Our results in Table 4 show that despite the lack of task-specific tuning our model performs surprisingly well, yielding better results than all previously reported models with the exception of the Recurrent Neural Network Grammar \[8\].”
- **action anticipation** — “state-of-the-art performance on human action anticipation”
- **action-conditioned** — “Transformer Aether \[247\] Utilizes camera trajectories as geometry-aware Diffusion actions, enabling accurate action-conditioned prediction and visual planning.”
- **action-free** — “Reinforcement learning with action-free pre-training from videos.”
- **recall-at-5** — “39.7 recall-at-5 on Epic-Kitchens-100”
- **internet-scale** — “Bengio, “Neural maagents with internet-scale knowledge,” in NeurIPS, chine translation by jointly learning to align and 2022. translate,” in ICLR, 2015. \[616\] P.”
- **comprising** — “a video and image dataset comprising over 1 million hours”
- **largely by observation** — “learn to act largely by observation”
- **question-answering** — “Two major Dolly \[185\] Apr-2023 15K OpenAssistant \[186\] Apr-2023 161K sources are public code repositories under open-source licenses (e.g., GitHub) and code-related question-answering Self-Instruct \[147\] Dec-2022 82K Alpaca \[187\] Mar-2023 52K platforms (e.g., StackOverflow).”

## 摘要提示（PDF 文本不可提取）

> TITLE: V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning ABSTRACT: A major challenge for modern AI is to learn to understand the world and learn to act largely by observation. This paper explores a self-supervised approach that combines internet-scale video data with a small amount of interaction data (robot trajectories), to develop models capable of understanding, predicting, and planning in the physical world. We first pre-train an action-free joint-embedding-predictive architecture, V-JEPA 2, on a video and image dataset comprising over 1 million hours of internet video. V-JEPA 2 achieves strong performance on motion understanding (77.3 top-1 accuracy on Something-Something v2) and state-of-the-art performance on human action anticipation (39.7 recall-at-5 on Epic-Kitchens-100) surpassing previous task-specific models. Additionally, after aligning V-JEPA 2 with a large language model, we demonstrate state-of-the-art performance on multiple video question-answering tasks at the 8 billion parameter scale (e.g., 84.0 on PerceptionTest, 76.9 on TempCompass). Finally, we show how self-supervised learning can be applied to robotic planning tasks by post-training a latent action-conditioned world model, V-JEPA 2-AC, using less than 62 hours of unlabeled robot videos from the Droid dataset. We deploy V-JEPA 2-AC zero-shot on Franka arms in two dif

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

PDF：`/home/user/llm-papers/05_世界模型/PDF/24_VJEPA2.pdf`

---
type: paper-pack
paper_id: "02-46"
stage: 2
title: "Aria: An Open Multimodal Native Mixture-of-Experts Model"
pdf: "/home/user/llm-papers/02_多模态/PDF/46_Aria.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-46 Aria: An Open Multimodal Native Mixture-of-Experts Model

**中文标题**：Aria：一个开源的多模态原生专家混合模型

**一句话概括**：发布开源多模态原生 MoE 模型，每个视觉/文本词元仅激活约 3.5~3.9B 参数，经四阶段预训练，性能超越同规模闭源竞品。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| outperform | /aʊtpəfˈɔːm/ | 超越；性能超过对比模型 | S |
| modality | /məʊdˈalɪti/ | 模态；信息的呈现形式（文本、图像等） | S |
| multimodal | /mˌʌltɪmˈəʊdəl/ | 多模态的；同时处理多种信息形式 | S |
| adaptation | /ˌadaptˈeɪʃən/ | 适配、改造；针对特定需求微调 | S |
| pipeline | /pˈaɪplaɪn/ | 流程；分阶段完成的训练计划 | S |
| progressively | /pɹəɡɹˈɛsɪvli/ | 逐步地；分阶段赋予能力 | A |
| proprietary | /pɹəpɹˈaɪətəɹi/ | 专有的、闭源的；不公开的模型 | A |
| openness | /ˈəʊpənnəs/ | 开放性；开源带来的透明度 | B |
| obstacle | /ˈɒbstəkəl/ | 障碍；阻碍采用的因素 | B |
| adoption | /ɐdˈɒpʃən/ | 采用；把模型用在实际场景 | B |
| mixture-of-experts | /mˈɪkstʃəɹɒvˈɛkspɜːts/ | 专家混合；每次只激活部分参数的架构 | B |
| activated parameters | /ˈaktɪvˌeɪtɪd pəɹˈamɪtəz/ | 激活参数；处理单个词元实际用到的参数 | B |

### 原句（保留完整句子）

- **outperform** — “While for small values of dk the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of dk \[3\].”
- **modality** — “As an- of non-textual modalities, especially the vision modality, other alternative approach, several studies \[819, 820\] adopt called multimodal large language models (MLLMs) \[800\]44 .”
- **multimodal** — “From the perspective of task solving, the four vision-language models that can better serve multimodal generations of language models have exhibited different lev- dialogues \[42–45\], and GPT-4 \[46\] has supported multiels of model capacities.”
- **adaptation** — “In particular, we focus on four major aspects of LLMs, namely pre-training, adaptation tuning, utilization, and capacity evaluation.”
- **pipeline** — “A it is also crucial to prevent the overlap between the training typical pipeline of preprocessing the pre-training data for and evaluation sets \[56\], by removing the possible duplicate LLMs has been illustrated in Figure 7. texts from the training set.”
- **progressively** — “It aims to ful LLMs, a more typical approach is to also incorporate diorganize different parts of pre-training data for LLMs in verse high-quality text like code, books, scientific papers, etc. a specific order, e.g., starting with easy/general examples If a LLM is specialized with a certain skill, the proportion of and progressively introducing more challenging/special- corresponding data source should be increased accordingly. ized ones.”
- **proprietary** — “Its performance is rigorously assessed through methods based on world models on the validation set of the nuScenes dataset. extensive experimentation on datasets such as nuScenes \[185\] and sizable proprietary datasets.”
- **openness** — “We hope that this openness will enable the community to reproduce fine-tuned LLMs and continue to improve the safety of those models, paving the way for more responsible development of LLMs.”
- **obstacle** — “The Associ- the cracked foundation: A survey of obstacles in ation for Computer Linguistics, 2016. evaluation practices for generated text,” CoRR, vol. \[621\] H.”
- **adoption** — “Any technique with a high tax might not see adoption.”
- **mixture-of-experts** — “Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. arXiv preprint arXiv:1701.06538, 2017. \[33\] Nitish Srivastava, Geoffrey E Hinton, Alex Krizhevsky, Ilya Sutskever, and Ruslan Salakhutdinov.”
- **activated parameters** — “"activated parameters per visual token and text token"”

## 摘要提示（PDF 文本不可提取）

> TITLE: Aria: An Open Multimodal Native Mixture-of-Experts Model ABSTRACT: Information comes in diverse modalities. Multimodal native AI models are essential to integrate real-world information and deliver comprehensive understanding. While proprietary multimodal native models exist, their lack of openness imposes obstacles for adoptions, let alone adaptations. To fill this gap, we introduce Aria, an open multimodal native model with best-in-class performance across a wide range of multimodal, language, and coding tasks. Aria is a mixture-of-expert model with 3.9B and 3.5B activated parameters per visual token and text token, respectively. It outperforms Pixtral-12B and Llama3.2-11B, and is competitive against the best proprietary models on various multimodal tasks. We pre-train Aria from scratch following a 4-stage pipeline, which progressively equips the model with strong capabilities in language understanding, multimodal understanding, long context window, and instruction following. We open-source the model weights along with a codebase that facilitates easy adoptions and adaptations of Aria in real-world applications.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/46_Aria.pdf`

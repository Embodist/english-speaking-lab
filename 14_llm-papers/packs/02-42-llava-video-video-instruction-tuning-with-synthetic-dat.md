---
type: paper-pack
paper_id: "02-42"
stage: 2
title: "LLaVA-Video: Video Instruction Tuning With Synthetic Data"
pdf: "/home/user/llm-papers/02_多模态/PDF/42_LLaVAVideo.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-42 LLaVA-Video: Video Instruction Tuning With Synthetic Data

**中文标题**：LLaVA-Video：用合成数据进行视频指令微调

**一句话概括**：为解决网络原始视频数据难整理的问题，构建高质量合成视频指令数据集 LLaVA-Video-178K，训练出的视频多模态模型在多个基准上表现强劲。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| benchmark | /bˈɛntʃmɑːk/ | 基准测试；权威评测数据集 | S |
| curate | /kjˈʊəɹeɪt/ | 整理、筛选；从海量数据中挑选高质量样本 | S |
| synthetic | /sɪnθˈɛtɪk/ | 合成的；由程序生成的训练数据 | S |
| pipeline | /pˈaɪplaɪn/ | 流程/管线；数据生成的处理链路 | S |
| hinder | /hˈɪndə/ | 阻碍；拖慢了模型发展 | A |
| captioning | /kˈapʃənɪŋ/ | 描述生成；为视频写详细文字说明 | A |
| checkpoint | /tʃˈɛkpɔɪnt/ | 检查点；训练得到的模型权重文件 | A |
| instruction-following | /ɪnstɹˈʌkʃənfˈɒləʊɪŋ/ | 指令遵循的；按指令完成任务的 | B |
| open-ended | /ˈəʊpənˈɛndɪd/ | 开放式的；答案不固定的问答 | B |
| tuning | /tjˈuːnɪŋ/ | 调优；在预训练基础上继续训练 | B |
| effectiveness | /ɪfˈɛktɪvnəs/ | 有效性；数据确实起作用 | B |

### 原句（保留完整句子）

- **benchmark** — “A recent study \[69\] found that a model size of 62B is better performance on downstream tasks, since language at least required for PaLM to perform well on various tasks modeling loss can be considered as a general measure of in four evaluation benchmarks (i.e., MMLU, BBH, TyDiQA the overall model capacity.”
- **curate** — “For example, BLOOM \[78\] and PaLM \[56\] have use of these data resources, a large amount of data is curated multilingual data covering 46 and 122 languages, crawled from the web in previous work, such as Com- respectively, within their pre-training corpora.”
- **synthetic** — “Dolma consisting of 3T tokens of apbased on the construction method of formatted instruction proximately 200TB of raw text and has been used to train instances, namely NLP task datasets, daily chat datasets and OLMo \[178\]. synthetic datasets.”
- **pipeline** — “A it is also crucial to prevent the overlap between the training typical pipeline of preprocessing the pre-training data for and evaluation sets \[56\], by removing the possible duplicate LLMs has been illustrated in Figure 7. texts from the training set.”
- **hinder** — “This process involves creatassessment, it is also often hindered by high annotation ing datasets annotated with preferences and feedback from costs, significant time requirements, and annotation inconhumans or proficient LLMs.”
- **captioning** — “"This dataset includes key tasks such as detailed captioning"”
- **checkpoint** — “For the base models, we used a single model obtained by averaging the last 5 checkpoints, which were written at 10-minute intervals.”
- **instruction-following** — “It is trained by 52K OpenAI has provided seven major interfaces to the models instruction-following demonstrations generated via self- in GPT-3 series: ada, babbage, curie, davinci (the instruct \[147\] using text-davinci-003.”
- **open-ended** — “We show versation types include open-ended generation, question their details in Table 4. answering, brainstorming, and chatting.”
- **tuning** — “"in combination with existing visual instruction tuning data"”
- **effectiveness** — “Baichuan is a series of open-source bilingual ness and effectiveness.”

## 摘要提示（PDF 文本不可提取）

> TITLE: LLaVA-Video: Video Instruction Tuning With Synthetic Data ABSTRACT: The development of video large multimodal models (LMMs) has been hindered by the difficulty of curating large amounts of high-quality raw data from the web. To address this, we propose an alternative approach by creating a high-quality synthetic dataset specifically for video instruction-following, namely LLaVA-Video-178K. This dataset includes key tasks such as detailed captioning, open-ended question-answering (QA), and multiple-choice QA. By training on this dataset, in combination with existing visual instruction tuning data, we introduce LLaVA-Video, a new video LMM. Our experiments demonstrate that LLaVA-Video achieves strong performance across various video benchmarks, highlighting the effectiveness of our dataset. We plan to release the dataset, its generation pipeline, and the model checkpoints.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/42_LLaVAVideo.pdf`

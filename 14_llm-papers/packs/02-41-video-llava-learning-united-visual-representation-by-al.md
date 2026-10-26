---
type: paper-pack
paper_id: "02-41"
stage: 2
title: "Video-LLaVA: Learning United Visual Representation by Alignment Before Projection"
pdf: "/home/user/llm-papers/02_多模态/PDF/41_VideoLLaVA.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-41 Video-LLaVA: Learning United Visual Representation by Alignment Before Projection

**中文标题**：Video-LLaVA：在投影前先对齐以学习统一视觉表征

**一句话概括**：指出图像与视频因缺乏统一词元化而在投影前错位，主张先把视觉表征统一到语言特征空间，再用图文视频混合数据训练出彼此增强的统一 LVLM。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| outperform | /aʊtpəfˈɔːm/ | 超越；性能优于对比模型 | S |
| downstream | /dˈaʊnstɹiːm/ | 下游的；基于大模型的具体任务 | S |
| baseline | /bˈeɪslaɪn/ | 基线（模型）；作为基准的简单模型 | S |
| tokenization | /tˌəʊkənaɪzˈeɪʃən/ | 词元化；把输入切成统一单元 | A |
| projection | /pɹədʒˈɛkʃən/ | 投影；把视觉特征映射到语言空间的层 | A |
| enhance | /ɛnhˈans/ | 提升、增强；改善下游任务表现 | B |
| misalignment | /mɪsɐlˈaɪnmənt/ | 错位；图像与视频表征不对齐的问题 | B |
| unify | /jˈuːnɪfˌaɪ/ | 统一；把视觉表示纳入同一特征空间 | B |
| toolkit | /tˈuːlkɪt/ | 工具包；评测用的框架集合 | B |
| notably | /nˈəʊtəbli/ | 值得注意的是；引出重要结论 | B |
| modest | /mˈɒdɪst/ | 适度的；谦虚而有价值的见解 | B |

### 原句（保留完整句子）

- **outperform** — “While for small values of dk the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of dk \[3\].”
- **downstream** — “In this paradigm, it word representations by first pre-training a bidirectional often requires fine-tuning the PLM for adapting to different LSTM (biLSTM) network (instead of learning fixed word downstream tasks. representations) and then fine-tuning the biLSTM network according to specific downstream tasks.”
- **baseline** — “Further, it is common to set a maximum achieve better performance on mathematical reasoning tasks cap to control the maximum number of examples that a than baseline methods, with only 20% data synthesis cost. dataset can contain during instruction tuning \[82\], which • Instruction selection.”
- **tokenization** — “One direct and effective approach is to employ 19 Ready to Raw Corpus Filtering & Selection De-duplication Privacy Reduction Tokenization pre-train!”
- **projection** — “To counteract this effect, we scale the dot products by √1d . k 3.2.2 Multi-Head Attention Instead of performing a single attention function with dmodel -dimensional keys, values and queries, we found it beneficial to linearly project the queries, keys and values h times with different, learned linear projections to dk , dk and dv dimensions, respectively.”
- **enhance** — “SLMs unless equipped with powerful artificial intelligence (AI) have been widely applied to enhance task performance algorithms.”
- **misalignment** — “They provide all MIDI files as well as preprocessed pianoroll representations of alignment and misalignment for free on the following website https://qsdfo.github.io/LOP/index.html.”
- **unify** — “To model this conditional probability, language text can be naturally employed as a 2.2 Technical Evolution of GPT-series Models unified way to format input, output and task information.”
- **toolkit** — “One commonly used toolkit for cleaning the fields of physics, mathematics, and computer science.”
- **notably** — “Notably, the thought process To guide LLMs in producing long-form reasoning followed naturally includes trigger keywords like “double check” and by solutions, it is crucial to curate high-quality long CoT “wait”, which invoke the corresponding verification or redata for warming up or training the models.”
- **modest** — “We therefore use modest data augmentation in 4.2 SQuAD v1.1 our system by first fine-tuning on TriviaQA (Joshi et al., 2017) befor fine-tuning on SQuAD.”

## 摘要提示（PDF 文本不可提取）

> TITLE: Video-LLaVA: Learning United Visual Representation by Alignment Before Projection ABSTRACT: The Large Vision-Language Model (LVLM) has enhanced the performance of various downstream tasks in visual-language understanding. Most existing approaches encode images and videos into separate feature spaces, which are then fed as inputs to large language models. However, due to the lack of unified tokenization for images and videos, namely misalignment before projection, it becomes challenging for a Large Language Model (LLM) to learn multi-modal interactions from several poor projection layers. In this work, we unify visual representation into the language feature space to advance the foundational LLM towards a unified LVLM. As a result, we establish a simple but robust LVLM baseline, Video-LLaVA, which learns from a mixed dataset of images and videos, mutually enhancing each other. Video-LLaVA achieves superior performances on a broad range of 9 image benchmarks across 5 image question-answering datasets and 4 image benchmark toolkits. Additionally, our Video-LLaVA also outperforms Video-ChatGPT by 5.8%, 9.9%, 18.6%, and 10.1% on MSRVTT, MSVD, TGIF, and ActivityNet, respectively. Notably, extensive experiments demonstrate that Video-LLaVA mutually benefits images and videos within a unified visual representation, outperforming models designed specifically for images or videos.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/41_VideoLLaVA.pdf`

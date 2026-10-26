---
type: paper-pack
paper_id: "03-05"
stage: 3
title: "Audio Set: An ontology and human-labeled dataset for audio events"
pdf: "/home/user/llm-papers/03_音乐检索理解/PDF/05_AudioSet_Dataset.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 03-05 Audio Set: An ontology and human-labeled dataset for audio events

**中文标题**：Audio Set：面向音频事件的 ontology（本体分类体系）与人工标注数据集

**一句话概括**：描述 Audio Set 数据集的构建：基于文献与人工整理出含 632 个音频类别的层次化本体分类体系，再请人工标注员判断 YouTube 视频 10 秒片段中各音频类别的存在与否，以填补图像与音频研究在数据可用性上的差距。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| comprehensive | /kˌɒmpɹɪhˈɛnsɪv/ | 全面的、大规模的（数据集） | S |
| hierarchical | /haɪəɹˈɑːkɪkəl/ | 层次的（分类体系的层级结构） | S |
| curation | /kjʊəɹˈeɪʃən/ | 整理、筛选（人工把关挑选） | S |
| comparable | /kˈɒmpəɹəbəl/ | 类似的、可比的（与之相当的问题） | S |
| endeavor | /ɛndˈɛvə/ | 努力、致力于（试图做到某事） | A |
| bridge the gap | /bɹˈɪdʒ ðˈə ɡˈap/ | 弥合差距（填补数据不足的空缺） | A |
| probe | /pɹˈəʊb/ | 探查、检测（判断类别是否存在） | A |
| ontology | /ɒntˈɒlədʒi/ | 本体（类别的结构化分类体系） | B |
| recognition | /ɹˌɛkəɡnˈɪʃən/ | 识别（音频事件识别任务） | B |
| nascent | /nˈeɪsənt/ | 新兴的、初期的（尚在起步阶段） | B |
| reap | /ɹˈiːp/ | 收获（获得巨大收益） | B |
| manually-annotated | /mˈanjuːəliˈanətˌeɪtɪd/ | 人工标注的（由人来打标签） | B |

### 原句（保留完整句子）

- **comprehensive** — “Nc Compared with them, we focus on the techniques and L(N ) = , αN ∼ 0.076, Nc ∼ 8.8 × 1013 (1) N methods to develop and use LLMs and provide a relatively Dc αD comprehensive reference to important aspects of LLMs.”
- **hierarchical** — “This approach (exemplified by with intermediate reasoning steps, it is mainly effective Tree of Thoughts (ToT) \[444, 517\]) formulates the reasoning for the tasks that require step-by-step reasoning \[33\], e.g., process in a hierarchical tree structure, where intermediate arithmetic reasoning, commonsense reasoning, and symthoughts are nodes.”
- **curation** — “It proves the are semantically aligned with given texts while maintaining importance of data curation for video diffusion models. consistency between different frames.”
- **comparable** — “Conversation data can enhance the comparable or superior performance to the state-of-the18 art models that are fine-tuned on the corpus in the target quality data.”
- **endeavor** — “To the best of its abilities, the model should mainly three kinds of approaches to collecting feedback and be capable of detecting covert endeavors aimed at soliciting preference data from human labelers. requests for malicious purposes.”
- **bridge the gap** — “"we aim to bridge the gap between closed-source and open-source communities"”
- **probe** — “GPT-2 essentially used ICL for unsupervised task learning, Further, a contrastive approach \[127\] to training text and though it wasn’t called ICL at that time. code embedding was reported in January 2022, which was 10 shown to improve a series of related tasks (i.e., linear- InstructGPT in the data collection setup: human-generated probe classification, text search and code search).”
- **ontology** — “Audio set: An ontology and humanRelja Arandjelovic, Jason Ramapuram, Jeffrey De Fauw, Lu- labeled dataset for audio events.”
- **recognition** — “Deep residual learning for image recognition.”
- **nascent** — “Regarding low-altitude aerial vehicles, the vast majority of current work focuses on applications in understanding, particularly in scene comprehension and navigation \[315, 322, 326\], while applications in prediction \[323\] are still in their nascent stages.”
- **reap** — “Overall, experimental results suggest CoCa reaps the benefit of a encoder-decoder model to obtain strong multimodal understanding and generation capabilities, in addition to the vision and retrieval capabilities as a dual-encoder method.”
- **manually-annotated** — “"a large-scale dataset of manually-annotated audio events"”

## Abstract（自动提取）

> The sheer sizes of modern datasets are forcing data-structure designers to consider seriously both parallel construction and compactness. To achieve those goals we need to design a parallel algorithm with good scalability and with low memory consumption. An algorithm with good scalability improves its performance when the number of available cores increases, and an algorithm with low memory consumption uses memory proportional to the space used by the dataset in uncompact form. In this work, we discuss the engineering of a parallel algorithm with linear work and logarithmic span for the construction of the compact representation of planar embeddings. We also provide an experimental study of our implementation and prove experimentally that it has good scalability and low memory consumption. Additionally, we describe and test experimentally queries supported by the compact representation. 1998 ACM Subject Classification E.4 Coding and Information Theory 

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
- [[14_llm-papers/stage-03-music-retrieval|阶段 3]]

PDF：`/home/user/llm-papers/03_音乐检索理解/PDF/05_AudioSet_Dataset.pdf`

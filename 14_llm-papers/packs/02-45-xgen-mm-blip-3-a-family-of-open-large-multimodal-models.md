---
type: paper-pack
paper_id: "02-45"
stage: 2
title: "xGen-MM (BLIP-3): A Family of Open Large Multimodal Models"
pdf: "/home/user/llm-papers/02_多模态/PDF/45_xGenMM_BLIP3.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-45 xGen-MM (BLIP-3): A Family of Open Large Multimodal Models

**中文标题**：xGen-MM（BLIP-3）：一系列开源的大型多模态模型

**一句话概括**：发布包含精挑数据集、训练配方、模型架构与 4B/14B 模型的完整开源 LMM 框架，模型能理解交错的图文输入，性能在同类开源模型中具竞争力。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| benchmark | /bˈɛntʃmɑːk/ | 基准测试；标准评测数据集 | S |
| recipe | /ɹˈɛsɪpˌiː/ | 配方/方案；可复现的训练流程 | S |
| interleaved | /ˌɪntəlˈiːvd/ | 交错的；图文交替混合的输入 | S |
| framework | /fɹˈeɪmwɜːk/ | 框架；支撑模型开发的整套体系 | A |
| meticulously | /mɛtˈɪkjʊləsli/ | 一丝不苟地；非常精心地整理 | A |
| curated | /kjˈʊəɹeɪtɪd/ | 精心整理的；经过筛选的高质量数据 | A |
| suite | /swˈiːt/ | 系列；一组配套的模型 | A |
| evaluation | /ɪvˌaljuːˈeɪʃən/ | 评估；检验模型性能的过程 | A |
| comprehend | /kˌɒmpɹɪhˈɛnd/ | 理解；把握图文内容含义 | A |
| rigorous | /ɹˈɪɡəɹəs/ | 严格的；全面规范的评测 | B |
| open-source | /ˈəʊpənsˈɔːs/ | 开源；公开代码与模型 | B |

### 原句（保留完整句子）

- **benchmark** — “A recent study \[69\] found that a model size of 62B is better performance on downstream tasks, since language at least required for PaLM to perform well on various tasks modeling loss can be considered as a general measure of in four evaluation benchmarks (i.e., MMLU, BBH, TyDiQA the overall model capacity.”
- **recipe** — “More (e.g., RLHF) \[66, 116\] have been widely used by leveraging training recipes or principles should be investigated and human feedback for developing well-aligned LLMs.”
- **interleaved** — “"processing arbitrarily interleaved multimodal inputs and"”
- **framework** — “To support distributed training, several (e.g., the discontinuous evaluation metrics) \[70, 71\]: when optimization frameworks have been released to facilitate evaluation metrics are altered accordingly, the sharpness of the implementation and deployment of parallel algorithms, the emergent ability curve would disappear.”
- **meticulously** — “Additionally, we scrutinize the burgeoning field of autonomous-driving world models, meticulously delineating their indispensable role in reshaping transportation and urban mobility.”
- **curated** — “"only 1,000 carefully curated prompts and responses"”
- **suite** — “Wang, evaluation suite for foundation models,” CoRR, vol.”
- **evaluation** — “Empirical evaluation of gated recurrent neural networks on sequence modeling.”
- **comprehend** — “It poses a significant challenge to develop capable artificial intelligence (AI) algorithms for comprehending and grasping a language.”
- **rigorous** — “RefinedWeb \[171\] is a web dataset obtained through rigorous selection and deduplication based on data Corpora Size Source Latest Update Time from Common Crawl, encompassing all Common Crawl BookCorpus \[158\] 5GB Books Dec-2015 web records from 2008 to June 2023, totaling around 5T Gutenberg \[159\] - Books Dec-2021 C4 \[82\] 800GB CommonCrawl Apr-2019 tokens.”
- **open-source** — “Qwen \[141, 142\] is an open-source large available resources for developing LLMs, including model model series consisting of Qwen (raging from 7B to 72B), checkpoints (or APIs), corpora and libraries.”

## 摘要提示（PDF 文本不可提取）

> TITLE: xGen-MM (BLIP-3): A Family of Open Large Multimodal Models ABSTRACT: This paper introduces BLIP-3, an open framework for developing Large Multimodal Models (LMMs). The framework comprises meticulously curated datasets, a training recipe, model architectures, and a resulting suite of LMMs. We release 4B and 14B models, including both the pre-trained base model and the instruction fine-tuned ones. Our models undergo rigorous evaluation across a range of tasks, including both single and multi-image benchmarks. Our models demonstrate competitive performance among open-source LMMs with similar model sizes. Our resulting LMMs demonstrate competitive performance among open-source LMMs with similar model sizes, with the ability to comprehend interleaved image-text inputs. Our training code, models, and all datasets used in this work, including the three largescale datasets we create and the preprocessed ones, will be open-sourced to better support the research community.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/45_xGenMM_BLIP3.pdf`

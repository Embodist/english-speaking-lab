---
type: paper-pack
paper_id: "04-12"
stage: 4
title: "AudioLDM 2: Learning Holistic Audio Generation with Self-supervised Pretraining"
pdf: "/home/user/llm-papers/04_音乐生成/PDF/12_AudioLDM2.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 04-12 AudioLDM 2: Learning Holistic Audio Generation with Self-supervised Pretraining

**中文标题**：AudioLDM 2：自监督预训练的整体音频生成

**一句话概括**：提出对语音、音乐、音效使用同一套方法的统一音频生成框架：用自监督的 AudioMAE 把任意音频翻译为"音频的语言"（LOA）表示，再用 GPT-2 把各模态输入转为 LOA，并以 LOA 为条件训练潜在扩散模型，在文生音频、文生音乐、文生语音基准上达到最优或相当性能。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| benchmark | /bˈɛntʃmɑːk/ | 基准（标准评测集） | S |
| competitive | /kəmpˈɛtɪtˌɪv/ | 有竞争力的（与最优水平相当） | S |
| modality | /məʊdˈalɪti/ | 模态（文本、图像等输入类型） | S |
| objective | /ɒbdʒˈɛktɪv/ | 目标（针对各类型设计的具体目标） | A |
| unified | /jˈuːnɪfˌaɪd/ | 统一的（用同一方法统一处理） | A |
| utilize | /jˈuːtɪlˌaɪz/ | 利用（采用同一种学习方法） | A |
| commonality | /kˌɒmənˈalɪti/ | 共性（不同类型音频之间的共同点） | B |
| bias | /bˈaɪəs/ | 偏差（不同任务特有的倾向） | B |
| perspective | /pəspˈɛktɪv/ | 视角（统一看待音频生成的角度） | B |
| translate | /tɹanslˈeɪt/ | 转换（把音频转成 LOA 表示） | B |
| in-context | /ɪŋkˈɒntɛkst/ | 上下文内的（上下文学习能力） | B |
| reusable | /ɹiːjˈuːzəbəl/ | 可复用的（预训练模型可重复使用） | B |

### 原句（保留完整句子）

- **benchmark** — “A recent study \[69\] found that a model size of 62B is better performance on downstream tasks, since language at least required for PaLM to perform well on various tasks modeling loss can be considered as a general measure of in four evaluation benchmarks (i.e., MMLU, BBH, TyDiQA the overall model capacity.”
- **competitive** — “3 Model Architecture Most competitive neural sequence transduction models have an encoder-decoder structure \[5, 2, 35\].”
- **modality** — “As an- of non-textual modalities, especially the vision modality, other alternative approach, several studies \[819, 820\] adopt called multimodal large language models (MLLMs) \[800\]44 .”
- **objective** — “Existing LLMs adopt similar Trans- α β where a = α+β , b = α+β and G is a scaling coefficient that former architectures and pre-training objectives (e.g., lancan be computed by A, B , α and β .”
- **unified** — “"for the unified processing of various modalities"”
- **utilize** — “It is interesting that young parents would be often In contrast, with the chain-of-thought (CoT) prompting surprised by unexpected progress of the speaking ability strategy \[33\], LLMs can solve such tasks by utilizing the exhibited by their babies. prompting mechanism that involves intermediate reasoning steps for deriving the final answer.”
- **commonality** — “10 https://www.surgehq.ai/ 14 Note that Sparrow’s \[Glaese et al., 2022\] decomposition of harmlessness into different areas has some commonality with our use of principles forming a ‘constitution’.”
- **bias** — “Grokking refers that “a pattern in the data, improving generaliza- both high-quality and low-quality data), they are likely to tion performance from random chance level to perfect generalization”, quoted from the original paper \[73\]. generate toxic, biased, or even harmful content for humans.”
- **perspective** — “2: An evolution process of the four generations of language models (LM) from the perspective of task solving capacity.”
- **translate** — “Neural machine translation by jointly learning to align and translate.”
- **in-context** — “For have to solve complicated engineering issues, working with example, GPT-3 can solve few-shot tasks through in-context engineers or being engineers. learning, whereas GPT-2 cannot do well.”
- **reusable** — “Instruction: What are some ways we can Instruction: ✓ make our school more eco-friendly? – Use reusable water bottles instead of disposable plastic ones.”

## 摘要提示（PDF 文本不可提取）

> 提出对语音、音乐、音效使用同一套方法的统一音频生成框架：用自监督的 AudioMAE 把任意音频翻译为"音频的语言"（LOA）表示，再用 GPT-2 把各模态输入转为 LOA，并以 LOA 为条件训练潜在扩散模型，在文生音频、文生音乐、文生语音基准上达到最优或相当性能。

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
- [[14_llm-papers/stage-04-music-generation|阶段 4]]

PDF：`/home/user/llm-papers/04_音乐生成/PDF/12_AudioLDM2.pdf`

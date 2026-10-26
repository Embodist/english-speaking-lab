---
type: paper-pack
paper_id: "03-16"
stage: 3
title: "Wav2CLIP: Learning Robust Audio Representations From CLIP"
pdf: "/home/user/llm-papers/03_音乐检索理解/PDF/16_Wav2CLIP.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 03-16 Wav2CLIP: Learning Robust Audio Representations From CLIP

**中文标题**：Wav2CLIP：从 CLIP 学习稳健的音频表示

**一句话概括**：提出从对比语言-图像预训练模型（CLIP）蒸馏出稳健音频表示的方法 Wav2CLIP，把音频映射到与图像、文本共享的嵌入空间，支持零样本分类与跨模态检索，且只需约 10% 数据即可达到接近全监督模型的性能。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| outperform | /aʊtpəfˈɔːm/ | 优于（超过公开的预训练方法） | S |
| downstream | /dˈaʊnstɹiːm/ | 下游的（后续任务） | S |
| competitive | /kəmpˈɛtɪtˌɪv/ | 有竞争力的（与全监督模型接近） | S |
| retrieval | /ɹɪtɹˈiːvəl/ | 检索（跨模态检索任务） | S |
| robust | /ɹəʊbˈʌst/ | 稳健的、鲁棒的（表示质量可靠） | S |
| multimodal | /mˌʌltɪmˈəʊdəl/ | 多模态的（同时涉及音频、图像、文本） | S |
| cross-modal | /kɹˈɒsmˈəʊdəl/ | 跨模态的（跨模态检索） | S |
| qualitative | /kwˈɒlɪtˌeɪtɪv/ | 定性的（定性评估共享空间质量） | A |
| distill | /dɪstˈɪl/ | 蒸馏（把大模型知识迁移到小模型） | B |
| systematically | /sˌɪstəmˈatɪkli/ | 系统地（全面评估） | B |
| project | /pɹˈɒdʒɛkt/ | 映射（投影到共享空间） | B |
| shared | /ʃˈeəd/ | 共享的（多模态共用的嵌入空间） | B |

### 原句（保留完整句子）

- **outperform** — “While for small values of dk the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of dk \[3\].”
- **downstream** — “In this paradigm, it word representations by first pre-training a bidirectional often requires fine-tuning the PLM for adapting to different LSTM (biLSTM) network (instead of learning fixed word downstream tasks. representations) and then fine-tuning the biLSTM network according to specific downstream tasks.”
- **competitive** — “3 Model Architecture Most competitive neural sequence transduction models have an encoder-decoder structure \[5, 2, 35\].”
- **retrieval** — “It has been a longstanding research challenge in information retrieval (IR) \[10, 11\] and natural language to achieve this goal, to enable machines to read, write, and processing (NLP) \[12–14\].”
- **robust** — “Nevertheless, LLMs may expose work argues that even human evaluation may not be robust bias (e.g., order bias or preference for LLM-generated texts enough \[630, 631, 641, 642\].”
- **multimodal** — “From the perspective of task solving, the four vision-language models that can better serve multimodal generations of language models have exhibited different lev- dialogues \[42–45\], and GPT-4 \[46\] has supported multiels of model capacities.”
- **cross-modal** — “Based on the observation, a contrastive learn- that we list two in-context examples for illustration, but ing scheme is devised to pull paired cross-modal repre- the number and the ordering of examples can be flexibly sentation closer while pushing away non-hallucinated and adjusted.”
- **qualitative** — “Specially, the language we can perform instruction tuning on LLMs with task ability would relatively stable within a time interval, but descriptions expressed in natural language, for improving qualitative change only occurs when evolving into another the generalizability of LLMs on unseen tasks.”
- **distill** — “JiuZhang3.0 \[344\] fine-tunes a 7B language model to syn- Furthermore, increasing the sampling ratio of high-quality thesize questions by distilling the knowledge from GPT- collections (e.g., FLAN \[67\] and P3 \[180\]) can generally 4, and then utilizes it to synthesize massive high-quality lead to performance improvement according to recent findinstructions based on pre-training corpus.”
- **systematically** — “The concept of building an internal model of the world has a long history in AI, dating back to foundational work such as Marvin Minsky’s frame representation in the 1960s \[175\], designed to systematically capture structured knowledge about the world.”
- **project** — “To counteract this effect, we scale the dot products by √1d . k 3.2.2 Multi-Head Attention Instead of performing a single attention function with dmodel -dimensional keys, values and queries, we found it beneficial to linearly project the queries, keys and values h times with different, learned linear projections to dk , dk and dv dimensions, respectively.”
- **shared** — “"into a shared embedding space with images"”

## 摘要提示（PDF 文本不可提取）

> 提出从对比语言-图像预训练模型（CLIP）蒸馏出稳健音频表示的方法 Wav2CLIP，把音频映射到与图像、文本共享的嵌入空间，支持零样本分类与跨模态检索，且只需约 10% 数据即可达到接近全监督模型的性能。

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

PDF：`/home/user/llm-papers/03_音乐检索理解/PDF/16_Wav2CLIP.pdf`

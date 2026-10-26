---
type: paper-pack
paper_id: "02-10"
stage: 2
title: "Visual Instruction Tuning"
pdf: "/home/user/llm-papers/02_多模态/PDF/10_LLaVA.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-10 Visual Instruction Tuning

**中文标题**：视觉指令微调

**一句话概括**：首次用语言-only 的 GPT-4 生成多模态语言-图像指令数据并进行指令微调，训练出端到端的大视觉语言模型 LLaVA。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| end-to-end | /ˈɛndtʊˈɛnd/ | 端到端的（整体联合训练） | S |
| multimodal | /mˌʌltɪmˈəʊdəl/ | 多模态的（同时处理语言与图像等） | S |
| synthetic | /sɪnθˈɛtɪk/ | 合成的（人工构造的评测数据） | S |
| general-purpose | /dʒˈɛnəɹəlpˈɜːpəs/ | 通用目的的（不局限于单一任务） | A |
| instruction tuning | /ɪnstɹˈʌkʃən tjˈuːnɪŋ/ | 指令微调（用"指令-回答"数据训练模型服从指令） | A |
| synergy | /sˈɪnədʒi/ | 协同作用（LLaVA 与 GPT-4 配合的效果） | A |
| accuracy | /ˈakjʊɹəsi/ | 准确率（评测指标，此处达 92.53%） | A |
| machine-generated | /məʃˈiːndʒˈɛnəɹˌeɪtɪd/ | 机器生成的（由模型自动生成而非人工编写） | B |
| assistant | /ɐsˈɪstənt/ | 助手（模型定位为语言与视觉助手） | B |
| connect | /kənˈɛkt/ | 连接（把视觉编码器与大语言模型接起来） | B |
| exhibit | /ɛɡzˈɪbɪt/ | 展现、表现出（展现出类似 GPT-4 的行为） | B |

### 原句（保留完整句子）

- **end-to-end** — “By instruction tuning on such generated data, we introduce LLaVA: Large Language and Vision Assistant, an end-to-end trained large multimodal model that connects a vision encoder and an LLM for generalpurpose visual and language understanding.”
- **multimodal** — “We present the first attempt to use language-only GPT-4 to generate multimodal language-image instruction-following data.”
- **synthetic** — “Our experiments show that LLaVA demonstrates impressive multimodal chat abilities, sometimes exhibiting the behaviors of multimodal GPT-4 on unseen images/instructions, and yields a 85.1% relative score compared with GPT-4 on a synthetic multimodal instruction-following dataset.”
- **general-purpose** — “One of the core aspirations in artificial intelligence is to develop a general-purpose assistant that can effectively follow multi-modal vision-and-language instructions, aligned with human intent to complete various real-world tasks in the wild \[4, 27, 26\].”
- **instruction tuning** — “By instruction tuning on such generated data, we introduce LLaVA: Large Language and Vision Assistant, an end-to-end trained large multimodal model that connects a vision encoder and an LLM for generalpurpose visual and language understanding.”
- **synergy** — “When fine-tuned on Science QA, the synergy of LLaVA and GPT-4 achieves a new state-of-the-art accuracy of 92.53%.”
- **accuracy** — “When fine-tuned on Science QA, the synergy of LLaVA and GPT-4 achieves a new state-of-the-art accuracy of 92.53%.”
- **machine-generated** — “Here are five common listening tests in various studies: • Turing test, which requires the subjects to judge whether the music is machine-generated or human-created \[111, 253\]. • Carry out two/multiple comparison and selection of music.”
- **assistant** — “By instruction tuning on such generated data, we introduce LLaVA: Large Language and Vision Assistant, an end-to-end trained large multimodal model that connects a vision encoder and an LLM for generalpurpose visual and language understanding.”
- **connect** — “We consider a simple linear layer to connect image features into the word embedding space.”
- **exhibit** — “5.1 Multimodal Chatbot We developed a chatbot demo to show the image understanding and conversation abilities of LLaVA, and to study how well LLaVA is able to digest visual inputs and exhibit instruction-following capabilities.”

## Abstract（自动提取）

> TITLE: Visual Instruction Tuning ABSTRACT: Instruction tuning large language models (LLMs) using machine-generated instruction-following data has improved zero-shot capabilities on new tasks, but the idea is less explored in the multimodal field. In this paper, we present the first attempt to use language-only GPT-4 to generate multimodal language-image instruction-following data. By instruction tuning on such generated data, we introduce LLaVA: Large Language and Vision Assistant, an end-to-end trained large multimodal model that connects a vision encoder and LLM for general-purpose visual and language understanding.Our early experiments show that LLaVA demonstrates impressive multimodel chat abilities, sometimes exhibiting the behaviors of multimodal GPT-4 on unseen images/instructions, and yields a 85.1% relative score compared with GPT-4 on a synthetic multimodal instruction-following dataset. When fine-tuned on Science QA, the synergy of LLaVA and GPT-4 achieves a new state-of-the-art accuracy of 92.53%. We make GPT-4 generated visual instruction tuning data, our model and code base publicly available.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/10_LLaVA.pdf`

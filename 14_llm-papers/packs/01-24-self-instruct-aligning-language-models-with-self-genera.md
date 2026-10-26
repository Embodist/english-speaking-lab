---
type: paper-pack
paper_id: "01-24"
stage: 1
title: "Self-Instruct: Aligning Language Models with Self-Generated Instructions"
pdf: "/home/user/llm-papers/01_大模型/PDF/24_SelfInstruct.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-24 Self-Instruct: Aligning Language Models with Self-Generated Instructions

**中文标题**：Self-Instruct：用自生成的指令对齐语言模型

**一句话概括**：提出 Self-Instruct，让模型用自己的生成结果"自举"出指令数据并微调，减少对人工指令数据的依赖，显著提升指令跟随能力。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| zero-shot | /zˈiəɹəʊʃˈɒt/ | 零样本的（不提供示例直接完成任务） | S |
| generalize | /dʒˈɛnəɹəlˌaɪz/ | 泛化（迁移到新任务） | S |
| curate | /kjˈʊəɹeɪt/ | 精心挑选、整理 | S |
| pipeline | /pˈaɪplaɪn/ | 流程（流水线式的处理步骤） | S |
| synthetic | /sɪnθˈɛtɪk/ | 合成的（机器生成的数据） | S |
| diversity | /daɪvˈɜːsɪti/ | 多样性 | A |
| aligning | /ɐlˈaɪnɪŋ/ | 对齐（让模型行为符合指令要求） | A |
| bootstrapping off | /bˈuːtstɹapɪŋ ˈɒf/ | 以……为基础自我提升 | B |
| hindering | /hˈɪndəɹɪŋ/ | 阻碍 | B |
| filters | /fˈɪltəz/ | 过滤（剔除不合格样本） | B |

### 原句（保留完整句子）

- **zero-shot** — “We evaluate T5-LM 11B 25.7 GPT3 175B 6.8 InstructGPT (Ouyang et al., 2022), which is developed by OpenAI based on GPT3 to follow human ⃝ 1 Instruction-tuned w/o S UPER NI T0 11B 33.1 instructions better and has been found by the com- GPT3 + T0 Training 175B 37.9 munity to have impressive zero-shot abilities.”
- **generalize** — “We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data. ∗ Equal contribution.”
- **curate** — “For further evaluation, we curate a The food is great, the bed is comfy, and there are plenty of toys to play with.”
- **pipeline** — “Our pipeline generates degrees fahrenheit to celsius. instructions, input, and output samples from Input: Null Output: a language model, then filters invalid or sim- def convert_fahrenheit_to_celsius(fahr): ilar ones before using them to finetune the celsius = (fahr - 32) * 5 / 9 return celsius original model.”
- **synthetic** — “See Table 10 for more examples. trained language models with instructions, and we release our large synthetic dataset to facilitate future studies on instruction tuning.2 can follow natural language instructions (Mishra 1 Introduction et al., 2022; Wei et al., 2022; Sanh et al., 2022; Wang et al., 2022; Ouyang et al., 2022; Chung et al., The recent NLP literature has witnessed a tremen- 2022, i.a.).”
- **diversity** — “2 Code and data are available at https://github.com/ diversity given that most human generations tend yizhongw/self-instruct to be popular NLP tasks, falling short of covering a Step 2: Classification 175 seed tasks with Task Pool Step 1: Instruction Generation Task Identification 1 instruction and 1 instance per task 🤖 LM Task 🤖 LM Instruction : Give me a quote from a famous person on this topic.”
- **aligning** — “ACL 2023 SELF-INSTRUCT: Aligning Language Models with Self-Generated Instructions Yizhong Wang♣ Yeganeh Kordi♢ Swaroop Mishra♡ Alisa Liu♣ Noah A.”
- **bootstrapping off** — “SELF-INSTRUCT, a framework for improving Output: Name: John Doe Age: 25 Sex: Male the instruction-following capabilities of pre- Phone Number: ... trained language models by bootstrapping off Instruction: How to write a code for converting their own generations.”
- **hindering** — “Can you please help me complete it? they depend heavily on human-written instruc- Input: tion data that is often limited in quantity, di- Application Form: Name:_________ Age:__________ Sex:________ versity, and creativity, therefore hindering the Phone Number:______ Email Address:________ generality of the tuned model.”
- **filters** — “Our pipeline generates degrees fahrenheit to celsius. instructions, input, and output samples from Input: Null Output: a language model, then filters invalid or sim- def convert_fahrenheit_to_celsius(fahr): ilar ones before using them to finetune the celsius = (fahr - 32) * 5 / 9 return celsius original model.”

## Abstract（自动提取）

> TITLE: Self-Instruct: Aligning Language Models with Self-Generated Instructions ABSTRACT: Large "instruction-tuned" language models (i.e., finetuned to respond to instructions) have demonstrated a remarkable ability to generalize zero-shot to new tasks. Nevertheless, they depend heavily on human-written instruction data that is often limited in quantity, diversity, and creativity, therefore hindering the generality of the tuned model. We introduce Self-Instruct, a framework for improving the instruction-following capabilities of pretrained language models by bootstrapping off their own generations. Our pipeline generates instructions, input, and output samples from a language model, then filters invalid or similar ones before using them to finetune the original model. Applying our method to the vanilla GPT3, we demonstrate a 33% absolute improvement over the original model on Super-NaturalInstructions, on par with the performance of InstructGPT-001, which was trained with private user data and human annotations. For further evaluation, we curate a set of expert-written instructions for novel tasks, and show through human evaluation that tuning GPT3 with Self-Instruct outperforms using existing public instruction datasets by a large margin, leaving only a 5% absolute gap behind InstructGPT-001. Self-Instruct provides an almost annotation-free method for aligning pre-trained lang

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
- [[14_llm-papers/stage-01-llm|阶段 1]]

PDF：`/home/user/llm-papers/01_大模型/PDF/24_SelfInstruct.pdf`

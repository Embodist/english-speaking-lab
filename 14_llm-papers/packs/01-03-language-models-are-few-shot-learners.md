---
type: paper-pack
paper_id: "01-03"
stage: 1
title: "Language Models are Few-Shot Learners"
pdf: "/home/user/llm-papers/01_大模型/PDF/03_GPT3_FewShot.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-03 Language Models are Few-Shot Learners

**中文标题**：语言模型是少样本学习者（GPT-3）

**一句话概括**：提出 1750 亿参数的 GPT-3，证明仅靠扩大模型规模即可让语言模型在少样本（few-shot）设置下接近甚至超越微调方法的性能。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| corpus | /kˈɔːpəs/ | 语料库（大规模文本集合） | S |
| autoregressive | /ˌɔːtəʊɹɪɡɹˈɛsɪv/ | 自回归的（逐词预测下一个词来生成） | S |
| fine-tuning | /fˈaɪntjˈuːnɪŋ/ | 微调（用任务数据在预训练模型上继续训练） | A |
| struggle | /stɹˈʌɡəl/ | 难以做到、表现吃力 | A |
| few-shot | /fjˈuːʃˈɒt/ | 少样本的（只用极少示例学习新任务） | A |
| demonstrated | /dˈɛmənstɹˌeɪtɪd/ | 证明、展示了 | B |
| task-agnostic | /tˈaskaɡnˈɒstɪk/ | 任务无关的（不针对特定任务设计结构） | B |
| scaling up | /skˈeɪlɪŋ ˈʌp/ | 扩大（模型）规模 | B |
| on-the-fly | /ɒnðəflˈaɪ/ | 临场的、即时的（需要即时推理） | B |
| evaluators | /ɪvˈaljuːˌeɪtəz/ | 评估者、评测人员 | B |

### 原句（保留完整句子）

- **corpus** — “Ziegler Jeffrey Wu Clemens Winter Christopher Hesse Mark Chen Eric Sigler Mateusz Litwin Scott Gray Benjamin Chess Jack Clark Christopher Berner Sam McCandlish Alec Radford Ilya Sutskever Dario Amodei OpenAI Abstract Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task.”
- **autoregressive** — “Specifically, we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in the few-shot setting.”
- **fine-tuning** — “Ziegler Jeffrey Wu Clemens Winter Christopher Hesse Mark Chen Eric Sigler Mateusz Litwin Scott Gray Benjamin Chess Jack Clark Christopher Berner Sam McCandlish Alec Radford Ilya Sutskever Dario Amodei OpenAI Abstract Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task.”
- **struggle** — “By contrast, humans can generally perform a new language task from only a few examples or from simple instructions – something which current NLP systems still largely struggle to do.”
- **few-shot** — “Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art finetuning approaches.”
- **demonstrated** — “Ziegler Jeffrey Wu Clemens Winter Christopher Hesse Mark Chen Eric Sigler Mateusz Litwin Scott Gray Benjamin Chess Jack Clark Christopher Berner Sam McCandlish Alec Radford Ilya Sutskever Dario Amodei OpenAI Abstract Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task.”
- **task-agnostic** — “While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples.”
- **scaling up** — “Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art finetuning approaches.”
- **on-the-fly** — “GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic.”
- **evaluators** — “Finally, we find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans.”

## Abstract（自动提取）

> TITLE: Language Models are Few-Shot Learners ABSTRACT: Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions - something which current NLP systems still largely struggle to do. Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches. Specifically, we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in the few-shot setting. For all tasks, GPT-3 is applied without any gradient updates or fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction with the model. GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit ar

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

PDF：`/home/user/llm-papers/01_大模型/PDF/03_GPT3_FewShot.pdf`

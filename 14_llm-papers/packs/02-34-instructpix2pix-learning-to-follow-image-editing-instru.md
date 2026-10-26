---
type: paper-pack
paper_id: "02-34"
stage: 2
title: "InstructPix2Pix: Learning to Follow Image Editing Instructions"
pdf: "/home/user/llm-papers/02_多模态/PDF/34_InstructPix2Pix.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-34 InstructPix2Pix: Learning to Follow Image Editing Instructions

**中文标题**：InstructPix2Pix：学习遵循图像编辑指令

**一句话概括**：结合 GPT-3 与 Stable Diffusion 自动生成大规模"指令-图像"编辑数据，训练出能按自然语言指令快速编辑任意图像的条件扩散模型。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| inference | /ˈɪnfəɹəns/ | 推理；模型训练后的使用阶段 | S |
| generalize | /dʒˈɛnəɹəlˌaɪz/ | 泛化；迁移到未见过的真实图像 | S |
| conditional | /kəndˈɪʃənəl/ | 条件的；以输入图像和指令为条件的扩散模型 | A |
| forward pass | /fˈɔːwəd pˈas/ | 前向传播；一次网络计算即完成编辑 | A |
| instruction | /ɪnstɹˈʌkʃən/ | 指令；告诉模型做什么的文字描述 | A |
| combine | /kəmbˈaɪn/ | 结合；融合两个模型的知识 | A |
| edit | /ˈɛdɪt/ | 编辑；按指令修改图像内容 | B |
| dataset | /dˈeɪtəsˌɛt/ | 数据集；用于训练的图像编辑样本集合 | B |
| inversion | /ɪnvˈɜːʃən/ | 反演；把图像逆向映射回潜空间的操作 | B |
| compelling | /kəmpˈɛlɪŋ/ | 令人信服的；效果很有说服力 | B |

### 原句（保留完整句子）

- **inference** — “Llion also experimented with novel model variants, was responsible for our initial codebase, and efficient inference and visualizations.”
- **generalize** — “We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data. ∗ Equal contribution.”
- **conditional** — “Recent work has achieved significant improvements in computational efficiency through factorization tricks \[21\] and conditional computation \[32\], while also improving model performance in case of the latter.”
- **forward pass** — “"Since it performs edits in the forward pass"”
- **instruction** — “Despite that scaling law characterizes a smooth language model has been provided with a natural language trend of performance increase (or loss decrease), it also instruction and/or several task demonstrations, it can genindicates that diminishing returns7 might occur as model erate the expected output for the test instances by comscaling.”
- **combine** — “This masking, combined with fact that the output embeddings are offset by one position, ensures that the predictions for position i can depend only on the known outputs at positions less than i.”
- **edit** — “Considering the cost and efficiency of the can be automatically constructed by an aligned LLMs achuman annotation process, several methods aim to auto- cording to human-written safety principles \[336\] or refining matically annotate the correctness of intermediate reason- existing examples using edits operations \[385\].”
- **dataset** — “"to generate a large dataset of image editing examples"”
- **inversion** — “Zhu et al., “In-domain gan inversion for real image editing,” in tion via hierarchical transformers,” NeurIPS, 2022.”
- **compelling** — “Attention mechanisms have become an integral part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in the input or output sequences \[2, 19\].”

## 摘要提示（PDF 文本不可提取）

> TITLE: InstructPix2Pix: Learning to Follow Image Editing Instructions ABSTRACT: We propose a method for editing images from human instructions: given an input image and a written instruction that tells the model what to do, our model follows these instructions to edit the image. To obtain training data for this problem, we combine the knowledge of two large pretrained models -- a language model (GPT-3) and a text-to-image model (Stable Diffusion) -- to generate a large dataset of image editing examples. Our conditional diffusion model, InstructPix2Pix, is trained on our generated data, and generalizes to real images and user-written instructions at inference time. Since it performs edits in the forward pass and does not require per example fine-tuning or inversion, our model edits images quickly, in a matter of seconds. We show compelling editing results for a diverse collection of input images and written instructions.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/34_InstructPix2Pix.pdf`

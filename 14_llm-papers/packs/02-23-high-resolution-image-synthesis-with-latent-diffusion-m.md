---
type: paper-pack
paper_id: "02-23"
stage: 2
title: "High-Resolution Image Synthesis with Latent Diffusion Models"
pdf: "/home/user/llm-papers/02_多模态/PDF/23_LDM_StableDiffusion.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-23 High-Resolution Image Synthesis with Latent Diffusion Models

**中文标题**：潜在扩散模型实现高分辨率图像合成

**一句话概括**：把扩散模型搬进预训练自编码器的隐空间训练，大幅降低算力需求，并通过跨注意力层支持文本、框等条件控制的高分辨率生成。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| inference | /ˈɪnfəɹəns/ | 推理（生成样本的过程） | S |
| latent space | /lˈeɪtənt spˈeɪs/ | 隐空间、潜在空间（压缩后的低维特征空间） | S |
| conditioning | /kəndˈɪʃənɪŋ/ | 条件（控制生成的外部输入） | A |
| inpainting | /ˈɪnpeɪntɪŋ/ | 图像修复（补全图像缺失区域） | A |
| sequential | /siːkwˈɛnʃəl/ | 顺序的、逐次的（逐步依次应用去噪自编码器） | A |
| formulation | /fˌɔːmjʊlˈeɪʃən/ | 公式化表述（模型的数学表述方式） | A |
| mechanism | /mˈɛkənˌɪzəm/ | 机制（控制生成过程的引导机制） | A |
| denoising | /dɪnˈɔɪsɪŋ/ | 去噪的（逐步去除噪声恢复图像） | A |
| autoencoder | /ˌɔːtəʊɛŋkˈəʊdə/ | 自编码器（先压缩再重建的神经网络） | A |
| decompose | /dˌiːkəmpˈəʊz/ | 分解（把图像生成过程拆解成逐步去噪） | B |
| pixel space | /pˈɪksəl spˈeɪs/ | 像素空间（直接在像素层面操作） | B |
| consume | /kənsjˈuːm/ | 消耗（训练耗掉数百个 GPU 天） | B |

### 原句（保留完整句子）

- **inference** — “However, since these models typically operate directly in pixel space, optimization of powerful DMs often consumes hundreds of GPU days and inference is expensive due to sequential evaluations.”
- **latent space** — “Since diffusion models offer excelapply them in the latent space of powerful pretrained aulent inductive biases for spatial data, we do not need the heavy spatoencoders.”
- **conditioning** — “8. ble generators for general conditioning inputs such as text or bounding boxes and high-resolution synthesis becomes results in image synthesis \[30,85\] and beyond \[7,45,48,57\], possible in a convolutional manner.”
- **inpainting** — “Moreover, even age inpainting and class-conditional image synthesis and unconditional DMs can readily be applied to tasks such highly competitive performance on various tasks, includ- as inpainting and colorization \[85\] or stroke-based syning text-to-image synthesis, unconditional image generation thesis \[53\], in contrast to other types of generative modand super-resolution, while significantly reducing computa- els \[19, 46, 69\].”
- **sequential** — “However, since these models typically operate directly in pixel space, optimization of powerful DMs often consumes hundreds of GPU days and inference is expensive due to sequential evaluations.”
- **formulation** — “Additionally, their formulation allows for a guiding mechanism to control the image generation process without retraining.”
- **mechanism** — “Additionally, their formulation allows for a guiding mechanism to control the image generation process without retraining.”
- **denoising** — “In contrast, the promis- though the reweighted variational objective \[30\] aims to ading results of GANs \[3, 27, 40\] have been revealed to be dress this by undersampling the initial denoising steps, DMs mostly confined to data with comparably limited variability are still computationally demanding, since training and as their adversarial learning procedure does not easily scale evaluating such a model requires repeated function evaluto modeling complex, multi-modal distributions.”
- **autoencoder** — “Compared to pixel-based diffusion aparate training into two distinct phases: First, we train proaches, we also significantly decrease inference costs. an autoencoder which provides a lower-dimensional (and (iii) We show that, in contrast to previous work \[93\] thereby efficient) representational space which is perceptu- which learns both an encoder/decoder architecture and a ally equivalent to the data space.”
- **decompose** — “Tensor parallelism is also a comtraining. monly used technique that aims to decompose the LLM for multi-GPU loading.”
- **pixel space** — “However, since these models typically operate directly in pixel space, optimization of powerful DMs often consumes hundreds of GPU days and inference is expensive due to sequential evaluations.”
- **consume** — “At each step the model is auto-regressive \[10\], consuming the previously generated symbols as additional input when generating the next.”

## Abstract（自动提取）

> TITLE: High-Resolution Image Synthesis with Latent Diffusion Models ABSTRACT: By decomposing the image formation process into a sequential application of denoising autoencoders, diffusion models (DMs) achieve state-of-the-art synthesis results on image data and beyond. Additionally, their formulation allows for a guiding mechanism to control the image generation process without retraining. However, since these models typically operate directly in pixel space, optimization of powerful DMs often consumes hundreds of GPU days and inference is expensive due to sequential evaluations. To enable DM training on limited computational resources while retaining their quality and flexibility, we apply them in the latent space of powerful pretrained autoencoders. In contrast to previous work, training diffusion models on such a representation allows for the first time to reach a near-optimal point between complexity reduction and detail preservation, greatly boosting visual fidelity. By introducing cross-attention layers into the model architecture, we turn diffusion models into powerful and flexible generators for general conditioning inputs such as text or bounding boxes and high-resolution synthesis becomes possible in a convolutional manner. Our latent diffusion models (LDMs) achieve a new state of the art for image inpainting and highly competitive performance on various tasks, includ

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

PDF：`/home/user/llm-papers/02_多模态/PDF/23_LDM_StableDiffusion.pdf`

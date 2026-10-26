---
type: paper-pack
paper_id: "02-20"
stage: 2
title: "GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models"
pdf: "/home/user/llm-papers/02_多模态/PDF/20_GLIDE.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-20 GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models

**中文标题**：GLIDE：文本引导扩散模型实现照片级图像生成与编辑

**一句话概括**：比较 CLIP 引导与无分类器引导两种文本条件扩散模型策略，后者更受人类评估者青睐，模型还可微调用于图像修复与编辑。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| fidelity | /fɪdˈɛlɪti/ | 保真度（生成结果与目标/真实图像的吻合程度） | S |
| inpainting | /ˈɪnpeɪntɪŋ/ | 图像修复（补全图像缺失/被遮区域） | A |
| trade off | /tɹˈeɪd ˈɒf/ | 权衡、以……换取……（牺牲多样性换保真度） | A |
| photorealistic | /fˌəʊtəʊɹiəlˈɪstɪk/ | 照片级逼真的（生成图像与真实照片难以区分） | A |
| similarity | /sˌɪmɪlˈaɹɪti/ | 相似度（生成图与说明文字的匹配程度） | A |
| guidance | /ɡˈaɪdəns/ | 引导（生成过程中控制方向的机制） | B |
| text-conditional | /tˈɛkstkəndˈɪʃənəl/ | 文本条件的（生成受文本描述控制） | B |
| strategy | /stɹˈatədʒi/ | 策略（两种不同的引导方案） | B |
| classifier-free | /klˈasɪfˌaɪəfɹˈiː/ | 无分类器的（不借助分类器梯度、更简单的引导方法） | B |
| evaluator | /ɪvˈaljuːˌeɪtə/ | 评估者（做人工评测的人） | B |
| reranking | /ɹɪɹˈaŋkɪŋ/ | 重排序（对候选结果重新排序挑选） | B |
| editing | /ˈɛdɪtɪŋ/ | 编辑（修改图像内容） | B |

### 原句（保留完整句子）

- **fidelity** — “We explore diffusion fidelity that humans can’t distinguish them from real images models for the problem of text-conditional im- (Zhou et al., 2019).”
- **inpainting** — “Additionally, we find is first trained on noised images, and during the diffusion that our models can be fine-tuned to perform imsampling process, gradients from the classifier are used age inpainting, enabling powerful text-driven imto guide the sample towards the label.”
- **trade off** — “"trade off diversity for fidelity"”
- **photorealistic** — “We find that the latter is preferred by achieving state-of-the-art sample quality on a number of human evaluators for both photorealism and cap- image generation benchmarks (Ho et al., 2020; Dhariwal & tion similarity, and often produces photorealistic Nichol, 2021; Ho et al., 2021). samples.”
- **similarity** — “We find that the latter is preferred by achieving state-of-the-art sample quality on a number of human evaluators for both photorealism and cap- image generation benchmarks (Ho et al., 2020; Dhariwal & tion similarity, and often produces photorealistic Nichol, 2021; Ho et al., 2021). samples.”
- **guidance** — “Within this line of research, diffusion age synthesis and compare two different guid- models (Sohl-Dickstein et al., 2015; Song & Ermon, 2020b) ance strategies: CLIP guidance and classifier-free have emerged as a promising family of generative models, guidance.”
- **text-conditional** — “We explore diffusion fidelity that humans can’t distinguish them from real images models for the problem of text-conditional im- (Zhou et al., 2019).”
- **strategy** — “In a follow-up work, Nichol & Dhariwal (2021) “a fire in the background” present a strategy for learning Σθ , which enables the model to produce high quality samples with fewer diffusion steps.”
- **classifier-free** — “Within this line of research, diffusion age synthesis and compare two different guid- models (Sohl-Dickstein et al., 2015; Song & Ermon, 2020b) ance strategies: CLIP guidance and classifier-free have emerged as a promising family of generative models, guidance.”
- **evaluator** — “The human evaluator may also indicate objects into paintings.”
- **reranking** — “For DALL-E, we generate samples at temperature 0.85 and select the best of 256 using CLIP reranking.”
- **editing** — “Therefore, we provide our model fine-tune our model to perform image inpainting, finding with editing capabilities in addition to zero-shot generation, that it is capable of making realistic edits to existing imGLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models “zebras roaming in the field” “a girl hugging a corgi on a pedestal” “a man with red hair” “a vase of flowers” “an old car in a snowy forest” “a man wearing a white hat” Figure 2.”

## Abstract（自动提取）

> TITLE: GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models ABSTRACT: Diffusion models have recently been shown to generate high-quality synthetic images, especially when paired with a guidance technique to trade off diversity for fidelity. We explore diffusion models for the problem of text-conditional image synthesis and compare two different guidance strategies: CLIP guidance and classifier-free guidance. We find that the latter is preferred by human evaluators for both photorealism and caption similarity, and often produces photorealistic samples. Samples from a 3.5 billion parameter text-conditional diffusion model using classifier-free guidance are favored by human evaluators to those from DALL-E, even when the latter uses expensive CLIP reranking. Additionally, we find that our models can be fine-tuned to perform image inpainting, enabling powerful text-driven image editing. We train a smaller model on a filtered dataset and release the code and weights at https://github.com/openai/glide-text2im.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/20_GLIDE.pdf`

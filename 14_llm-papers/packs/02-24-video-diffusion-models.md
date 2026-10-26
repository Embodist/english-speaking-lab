---
type: paper-pack
paper_id: "02-24"
stage: 2
title: "Video Diffusion Models"
pdf: "/home/user/llm-papers/02_多模态/PDF/24_VideoDiffusionModels.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-24 Video Diffusion Models

**中文标题**：视频扩散模型

**一句话概括**：提出视频扩散模型，可联合训练图像与视频数据以降低梯度方差、加快优化，并用新的条件采样技术支持长视频与高分辨率扩展。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| jointly | /dʒˈɔɪntli/ | 联合地（图像与视频数据一起训练） | A |
| coherent | /kəʊhˈiəɹənt/ | 连贯的（视频帧间在时间上一致连贯） | A |
| milestone | /mˈaɪlstəʊn/ | 里程碑（生成建模研究的重要节点） | A |
| promising | /pɹˈɒmɪsɪŋ/ | 有前景的（初步结果很有希望） | A |
| extension | /ɛkstˈɛnʃən/ | 扩展（标准图像扩散架构的自然扩展） | A |
| minibatch | /mˈɪnɪbˌatʃ/ | 小批量（每次训练用的一小批样本） | A |
| unconditional | /ʌŋkəndˈɪʃənəl/ | 无条件的（不依赖任何输入条件的生成） | A |
| temporally | /tˈɛmpəɹəli/ | 时间上地（视频在时间维度的连贯性） | B |
| variance | /vˈeəɹiəns/ | 方差（小批量梯度的波动幅度） | B |
| gradient | /ɡɹˈeɪdiənt/ | 梯度（训练中用于更新参数的信号） | B |
| optimization | /ˌɒptɪmaɪzˈeɪʃən/ | 优化（训练收敛过程） | B |
| conditional sampling | /kəndˈɪʃənəl sˈamplɪŋ/ | 条件采样（受额外条件控制的采样方法） | B |

### 原句（保留完整句子）

- **jointly** — “Our model is a natural extension of the standard image diffusion architecture, and it enables jointly training from image and video data, which we find to reduce the variance of minibatch gradients and speed up optimization.”
- **coherent** — “When we tried the replacement method to conditional sampling, we found it to not work well for our video models: Although samples xb looked good in isolation, they were often not coherent with xa .”
- **milestone** — “We make progress towards this milestone by proposing a diffusion model for video generation that shows very promising initial results.”
- **promising** — “We make progress towards this milestone by proposing a diffusion model for video generation that shows very promising initial results.”
- **extension** — “Our model is a natural extension of the standard image diffusion architecture, and it enables jointly training from image and video data, which we find to reduce the variance of minibatch gradients and speed up optimization.”
- **minibatch** — “Our model is a natural extension of the standard image diffusion architecture, and it enables jointly training from image and video data, which we find to reduce the variance of minibatch gradients and speed up optimization.”
- **unconditional** — “We present the first results on a large text-conditioned video generation task, as well as state-of-the-art results on established benchmarks for video prediction and unconditional video generation.”
- **temporally** — “This allows one to then to upsample a video temporally, similar to how \[34\] generate high resolution images through spatial upsampling.”
- **variance** — “Our model is a natural extension of the standard image diffusion architecture, and it enables jointly training from image and video data, which we find to reduce the variance of minibatch gradients and speed up optimization.”
- **gradient** — “(7) 2 The additional gradient term in this expression can be interpreted as a form of guidance \[16, 20\] based on the model’s reconstruction of the conditioning data, and we therefore refer to this method as reconstruction-guided sampling, or simply reconstruction guidance.”
- **optimization** — “Our model is a natural extension of the standard image diffusion architecture, and it enables jointly training from image and video data, which we find to reduce the variance of minibatch gradients and speed up optimization.”
- **conditional sampling** — “To generate long and higher resolution videos we introduce a new conditional sampling technique for spatial and temporal video extension that performs better than previously proposed methods.”

## Abstract（自动提取）

> TITLE: Video Diffusion Models ABSTRACT: Generating temporally coherent high fidelity video is an important milestone in generative modeling research. We make progress towards this milestone by proposing a diffusion model for video generation that shows very promising initial results. Our model is a natural extension of the standard image diffusion architecture, and it enables jointly training from image and video data, which we find to reduce the variance of minibatch gradients and speed up optimization. To generate long and higher resolution videos we introduce a new conditional sampling technique for spatial and temporal video extension that performs better than previously proposed methods. We present the first results on a large text-conditioned video generation task, as well as state-of-the-art results on established benchmarks for video prediction and unconditional video generation. Supplementary material is available at https://video-diffusion.github.io/

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

PDF：`/home/user/llm-papers/02_多模态/PDF/24_VideoDiffusionModels.pdf`

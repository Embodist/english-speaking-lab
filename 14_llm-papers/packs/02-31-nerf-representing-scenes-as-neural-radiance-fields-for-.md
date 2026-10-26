---
type: paper-pack
paper_id: "02-31"
stage: 2
title: "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis"
pdf: "/home/user/llm-papers/02_多模态/PDF/31_NeRF.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-31 NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis

**中文标题**：NeRF：用神经辐射场表示场景以合成新视角

**一句话概括**：用全连接网络编码连续的 5D 场景函数（位置+视角），配合可微体积渲染，仅凭一组带位姿的照片即可合成照片级真实的新视角。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| synthesize | /sˈɪnθəsˌaɪz/ | 合成；从模型生成新视角图像 | S |
| sparse | /spˈɑːs/ | 稀疏的；数量很少的输入照片 | S |
| coordinate | /kəʊˈɔːdɪnət/ | 坐标；网络输入的 5 维空间-方向表示 | A |
| differentiable | /dˈɪfəɹˌɛnʃɪəbəl/ | 可微的；可反向传播梯度 | A |
| photorealistic | /fˌəʊtəʊɹiəlˈɪstɪk/ | 照片级逼真的 | A |
| novel view | /nˈɒvəl vjˈuː/ | 新视角；相机未拍摄过的观察角度 | B |
| optimize | /ˈɒptɪmˌaɪz/ | 优化；训练中不断调整网络参数 | B |
| volumetric | /vˌɒljuːmˈɛtɹɪk/ | 体（积）的；描述三维空间中连续分布的场景函数 | B |
| radiance | /ɹˈeɪdiəns/ | 辐射度；某方向发出的光能量，决定像素颜色 | B |
| query | /kwˈiəɹɪ/ | 查询；沿相机光线采样坐标点 | B |
| camera pose | /kˈamɹə pˈəʊz/ | 相机位姿；拍摄时的位置与朝向 | B |
| geometry | /dʒiˈɒmətɹi/ | 几何；场景的立体形状结构 | B |

### 原句（保留完整句子）

- **synthesize** — “Each prompt the LLM \[55\] to synthesize additional instructions answer is annotated with a score calculated based on its based on randomly selected 8 instructions as reference. votes and a label denoting whether it is selected.”
- **sparse** — “Mixdeployment life-cycle, which aims to effectively reduce the tral is a kind of sparse Mixture-of-Experts (SMoE) model potential risks of using the models.”
- **coordinate** — “To facilitate a more thorough grained information (e.g., coordinate of objects) into the evaluation of MLLMs, various benchmarks have been develinstruction \[836\], or synthesizing complex visual reasoning oped.”
- **differentiable** — “Gruza, “Transformer memory as a differentiable search inA.”
- **photorealistic** — “These works build indoor environments by providing photorealistic settings where agents can practice visual navigation and engage in interactive tasks that mimic real-life home activities.”
- **novel view** — “"achieves state-of-the-art results for synthesizing novel views"”
- **optimize** — “While the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code.”
- **volumetric** — “This involves not only capturing the visual appearance of objects and scenes but also encoding their spatial relationships, depth information, and volumetric properties.”
- **radiance** — “Mildenhall et al., “Nerf: Representing scenes as neural radiance Videos,” in RSS, 2023. fields for view synthesis,” Communications of the ACM, 2021. \[238\] R.”
- **query** — “3.2 Attention An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors.”
- **camera pose** — “"a set of images with known camera poses"”
- **geometry** — “A complementary psychometric framing anchors five Basic Spatial Abilities—perception, relations, orientation, mental rotation, visualization—revealing geometry/rotation weaknesses across 13 VLMs and supplying calibrated tasks for progress tracking \[285\].”

## 摘要提示（PDF 文本不可提取）

> TITLE: NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis ABSTRACT: We present a method that achieves state-of-the-art results for synthesizing novel views of complex scenes by optimizing an underlying continuous volumetric scene function using a sparse set of input views. Our algorithm represents a scene using a fully-connected (non-convolutional) deep network, whose input is a single continuous 5D coordinate (spatial location $(x,y,z)$ and viewing direction $(θ, φ)$) and whose output is the volume density and view-dependent emitted radiance at that spatial location. We synthesize views by querying 5D coordinates along camera rays and use classic volume rendering techniques to project the output colors and densities into an image. Because volume rendering is naturally differentiable, the only input required to optimize our representation is a set of images with known camera poses. We describe how to effectively optimize neural radiance fields to render photorealistic novel views of scenes with complicated geometry and appearance, and demonstrate results that outperform prior work on neural rendering and view synthesis. View synthesis results are best viewed as videos, so we urge readers to view our supplementary video for convincing comparisons.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/31_NeRF.pdf`

---
type: paper-pack
paper_id: "02-32"
stage: 2
title: "3D Gaussian Splatting for Real-Time Radiance Field Rendering"
pdf: "/home/user/llm-papers/02_多模态/PDF/32_3DGaussianSplatting.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-32 3D Gaussian Splatting for Real-Time Radiance Field Rendering

**中文标题**：用于实时辐射场渲染的 3D 高斯泼溅

**一句话概括**：用可优化的 3D 高斯表示场景、配合同步的密度控制与可见性感知渲染算法，首次实现 1080p 分辨率下 30fps 以上的实时新视角合成。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| trade off | /tɹˈeɪd ˈɒf/ | 权衡、取舍；牺牲一方面换取另一方面 | A |
| preserve | /pɹɪzˈɜːv/ | 保持、保留；继承连续辐射场场的优点 | A |
| accelerate | /ɐksˈɛləɹˌeɪt/ | 加速；加快训练与渲染速度 | A |
| resolution | /ɹˌɛzəlˈuːʃən/ | 分辨率；本文目标为 1080p 高清 | A |
| revolutionize | /ɹˌɛvəlˈuːʃənˌaɪz/ | 彻底改变；革新了新视角合成领域 | A |
| real-time | /ɹˈiəltˈaɪm/ | 实时的；满足交互式显示帧率 | A |
| inevitably | /ɪnˈɛvɪtəbli/ | 不可避免地；速度与质量难以两全 | B |
| unbounded | /ʌnbˈaʊndɪd/ | 无界的；指不受边界限制的完整场景 | B |
| calibration | /kˌalɪbɹˈeɪʃən/ | 标定；估计相机内外参数的过程 | B |
| anisotropic | /ˌanɪsətɹˈɒpɪk/ | 各向异性的；沿不同方向尺度不同的协方差 | B |
| covariance | /kˈɒveəɹˌiəns/ | 协方差；描述高斯形状的矩阵 | B |
| visibility-aware | /vˌɪzɪbˈɪlɪtiɐwˈeə/ | 可见性感知的；考虑遮挡关系的渲染 | B |

### 原句（保留完整句子）

- **trade off** — “"trade off diversity for fidelity"”
- **preserve** — “We need to prevent leftward information flow in the decoder to preserve the auto-regressive property.”
- **accelerate** — “Lukasz and Aidan spent countless long days designing various parts of and implementing tensor2tensor, replacing our earlier codebase, greatly improving results and massively accelerating our research. † Work performed while at Google Brain. ‡ Work performed while at Google Research.”
- **resolution** — “In the Transformer this is reduced to a constant number of operations, albeit at the cost of reduced effective resolution due to averaging attention-weighted positions, an effect we counteract with Multi-Head Attention as described in section 3.2.”
- **revolutionize** — “The technical evolution of LLMs has been making an important impact on the entire AI community, which would revolutionize the way how we develop and use AI algorithms.”
- **real-time** — “MemoryBank \[539\] further provide real-time error messages \[443\], models like stable proposes the memory updating mechanism to allow memdiffusion \[534\] can be used in multimodal tasks to provide ory forgetting and strengthening following the Ebbinghaus visual perception \[439\], and virtual worlds like Minecraft Forgetting Curve theory. can provide immersive experiences \[530\].”
- **inevitably** — “However, changing the rhythm characteristics of melody will inevitably affect the pitch contour, which would lead to the complicated behaviors of the latent space difficult to be explained intuitively.”
- **unbounded** — “Mahlernet: Unbounded orchestral music with neural networks.”
- **calibration** — “In addition to the log probability for the response with a higher ranking. conventional optimization objective, several studies further Moreover, SLiC-HF \[398\] proposes to assess the similarity explore auxiliary losses that enhance the learning from the between model outputs and human preference via the disalignment data. tance in the latent space, and introduces specific calibration • Primary training objective.”
- **anisotropic** — “"notably optimizing anisotropic covariance to achieve an accurate"”
- **covariance** — “Then, the music similarity between music distributions is quantified by calculating Mahalanobis distance \[336\] given the average feature vector 𝜇 and covariance matrix Σ of music 𝑥 and corpus D.”
- **visibility-aware** — “"we develop a fast visibility-aware rendering algorithm"”

## 摘要提示（PDF 文本不可提取）

> TITLE: 3D Gaussian Splatting for Real-Time Radiance Field Rendering ABSTRACT: Radiance Field methods have recently revolutionized novel-view synthesis of scenes captured with multiple photos or videos. However, achieving high visual quality still requires neural networks that are costly to train and render, while recent faster methods inevitably trade off speed for quality. For unbounded and complete scenes (rather than isolated objects) and 1080p resolution rendering, no current method can achieve real-time display rates. We introduce three key elements that allow us to achieve state-of-the-art visual quality while maintaining competitive training times and importantly allow high-quality real-time (&gt;= 30 fps) novel-view synthesis at 1080p resolution. First, starting from sparse points produced during camera calibration, we represent the scene with 3D Gaussians that preserve desirable properties of continuous volumetric radiance fields for scene optimization while avoiding unnecessary computation in empty space; Second, we perform interleaved optimization/density control of the 3D Gaussians, notably optimizing anisotropic covariance to achieve an accurate representation of the scene; Third, we develop a fast visibility-aware rendering algorithm that supports anisotropic splatting and both accelerates training and allows realtime rendering. We demonstrate state-of-the-art vis

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

PDF：`/home/user/llm-papers/02_多模态/PDF/32_3DGaussianSplatting.pdf`

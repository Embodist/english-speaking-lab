---
type: paper-pack
paper_id: "02-27"
stage: 2
title: "Denoising Diffusion Probabilistic Models"
pdf: "/home/user/llm-papers/02_多模态/PDF/27_DDPM.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-27 Denoising Diffusion Probabilistic Models

**中文标题**：去噪扩散概率模型

**一句话概括**：提出 DDPM，用加权变分界训练扩散概率模型，在无条件 CIFAR10 上取得 FID 3.17 的 SOTA 图像生成质量。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| diffusion | /dɪfjˈuːʒən/ | 扩散（前向逐步加噪声、反向去噪的生成范式） | A |
| interpret | /ɪntˈɜːpɹɪt/ | 解释为、理解为（可看作自回归解码的推广） | A |
| denoising | /dɪnˈɔɪsɪŋ/ | 去噪的（逐步去除噪声的） | A |
| probabilistic | /pɹˌɒbəbɪlˈɪstɪk/ | 概率的（基于概率分布的模型） | A |
| novel | /nˈɒvəl/ | 新颖的（新的联系/发现） | A |
| latent variable model | /lˈeɪtənt vˈeəɹɪəbəl mˈɒdəl/ | 隐变量模型（含有未观测变量的生成模型） | B |
| inspired by | /ɪnspˈaɪəd bˈaɪ/ | 受……启发（思想来源于非平衡热力学） | B |
| nonequilibrium | /nˌɒnˌiːkwɪlˈɪbɹiəm/ | 非平衡的（热力学中的非平衡态） | B |
| thermodynamics | /θˌɜːməʊdaɪnˈamɪks/ | 热力学（研究能量转化的物理分支） | B |
| variational bound | /vˌeəɹɪˈeɪʃənəl bˈaʊnd/ | 变分界（用于训练的加权变分下界） | B |
| score matching | /skˈɔː mˈatʃɪŋ/ | 分数匹配（估计数据分布梯度的一种方法） | B |
| admit | /ɐdmˈɪt/ | 具有、允许（模型天然支持一种渐进式有损解压方案） | B |

### 原句（保留完整句子）

- **diffusion** — “As for LLMs, unstructured supporting other model compression methods. pruning can generally lead to higher compression rates. • Torch-Pruning 53 is a toolkit developed for generalFor instance, SparseGPT \[1020\] achieves 60% unstructured purpose structural pruning, including the pruning for vision sparsity for OPT-175B using unstructured pruning (i.e., models, diffusion models and large language models.”
- **interpret** — “Bowman, “GLUE: A multi-task benchmark long sequences with structured state spaces,” and analysis platform for natural language underin The Tenth International Conference on Learning standing,” in Proceedings of the Workshop: AnalyzRepresentations, ICLR 2022, Virtual Event, April 25-29, ing and Interpreting Neural Networks for NLP, Black2022.”
- **denoising** — “For training LLMs, there are two commonly used pretraining tasks, namely language modeling and denoising LM and DAE objectives as different types of denoising tasks, autoencoding. namely S-denoiser (LM), R-denoiser (DAE, short span and low corruption), and X-denoiser (DAE, long span or high Language Modeling.”
- **probabilistic** — “For neural language models, we abbreviate the paper titles of two representative studies to name the two approaches: NPLM \[1\] (“A neural probabilistic language model”) and NLPS \[2\] (“Natural language processing (almost) from scratch”).”
- **novel** — “Llion also experimented with novel model variants, was responsible for our initial codebase, and efficient inference and visualizations.”
- **latent variable model** — “"a class of latent variable models"”
- **inspired by** — “"inspired by considerations from nonequilibrium thermodynamics"”
- **nonequilibrium** — “Deep unsupervised learning using nonequilibrium thermodynamics. arXiv:1503.03585, 2015.”
- **thermodynamics** — “Law-centric suites sharpen the picture: Physics-IQ evaluates five domains (solid/fluid mechanics, optics, thermodynamics, magnetism), finding physical understanding largely decoupled from perceived realism \[178\]; T2VPhysBench provides a first-principles checklist of 12 core laws for text-to-video systems \[86\].”
- **variational bound** — “"a weighted variational bound designed according"”
- **score matching** — “"denoising score matching with Langevin dynamics"”
- **admit** — “It’s crucial to recognize that the model isn’t always accurate in admitting its limitations, as evidenced by its tendency to hallucinate.”

## 摘要提示（PDF 文本不可提取）

> TITLE: Denoising Diffusion Probabilistic Models ABSTRACT: We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics. Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score matching with Langevin dynamics, and our models naturally admit a progressive lossy decompression scheme that can be interpreted as a generalization of autoregressive decoding. On the unconditional CIFAR10 dataset, we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17. On 256x256 LSUN, we obtain sample quality similar to ProgressiveGAN. Our implementation is available at https://github.com/hojonathanho/diffusion

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

PDF：`/home/user/llm-papers/02_多模态/PDF/27_DDPM.pdf`

---
type: paper-pack
paper_id: "02-56"
stage: 2
title: "Movie Gen: A Cast of Media Foundation Models"
pdf: "/home/user/llm-papers/02_多模态/PDF/56_MovieGen.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-56 Movie Gen: A Cast of Media Foundation Models

**中文标题**：Movie Gen：一组媒体基础模型

**一句话概括**：发布能生成 1080p 高清视频与同步音频的媒体基础模型系列，30B 参数 Transformer 支持 73K 视频词元上下文，在多任务上刷新 SOTA。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| state-of-the-art | /stˈeɪtɒvðɪˈɑːt/ | 最先进水平；当前最佳成绩 | S |
| curation | /kjʊəɹˈeɪʃən/ | 整理；训练数据筛选 | S |
| latent space | /lˈeɪtənt spˈeɪs/ | 潜空间；压缩表示所在的空间 | S |
| recipe | /ɹˈɛsɪpˌiː/ | 配方/方案；训练流程的具体安排 | S |
| synthesis | /sˈɪnθəsˌɪs/ | 合成；从条件生成内容 | A |
| innovation | /ˌɪnəvˈeɪʃən/ | 创新；技术上的新设计 | A |
| accelerate | /ɐksˈɛləɹˌeɪt/ | 加速；加快领域进展 | A |
| cast | /kˈast/ | 阵容；一组配合使用的模型 | A |
| protocol | /pɹˈəʊtəkˌɒl/ | 方案；评测的标准流程 | A |
| aspect ratio | /ˈaspɛkt ɹˈeɪʃɪˌəʊ/ | 宽高比；画面的长宽比例 | B |
| synchronized | /sˈɪŋkɹənˌaɪzd/ | 同步的；与画面时间对齐的音频 | B |
| personalized | /pˈɜːsənəlˌaɪzd/ | 个性化的；针对特定用户生成 | B |

### 原句（保留完整句子）

- **state-of-the-art** — “On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature.”
- **curation** — “It proves the are semantically aligned with given texts while maintaining importance of data curation for video diffusion models. consistency between different frames.”
- **latent space** — “"in the latent space of powerful"”
- **recipe** — “More (e.g., RLHF) \[66, 116\] have been widely used by leveraging training recipes or principles should be investigated and human feedback for developing well-aligned LLMs.”
- **synthesis** — “Muffin contains 62 tasks from the orig- AI assistant in turns, generating information in a conversainal FLAN and additional 26 tasks, including conversation tional format. and code synthesis tasks.”
- **innovation** — “This wave of how to efficiently find the effective prompts for LLMs on technical innovation would lead to an ecosystem of LLMspecific tasks.”
- **accelerate** — “Lukasz and Aidan spent countless long days designing various parts of and implementing tensor2tensor, replacing our earlier codebase, greatly improving results and massively accelerating our research. † Work performed while at Google Brain. ‡ Work performed while at Google Research.”
- **cast** — “Due to the excellent capacity in communicating with hu- In this way, the process of solving a task can be cast as a mans, ChatGPT has ignited the excitement of the AI com- word prediction problem for generating the solution text. munity since its release.”
- **protocol** — “Subsequently, the planning component communication protocols have been proposed, including utilizes the processed information from short-term memory free-form dialogue \[966\], structured document \[967\], and to generate the next plan.”
- **aspect ratio** — “"with different aspect ratios and synchronized audio"”
- **synchronized** — “"with different aspect ratios and synchronized audio"”
- **personalized** — “"generation of personalized videos based on a user's image"”

## 摘要提示（PDF 文本不可提取）

> TITLE: Movie Gen: A Cast of Media Foundation Models ABSTRACT: We present Movie Gen, a cast of foundation models that generates high-quality, 1080p HD videos with different aspect ratios and synchronized audio. We also show additional capabilities such as precise instruction-based video editing and generation of personalized videos based on a user's image. Our models set a new state-of-the-art on multiple tasks: text-to-video synthesis, video personalization, video editing, video-to-audio generation, and text-to-audio generation. Our largest video generation model is a 30B parameter transformer trained with a maximum context length of 73K video tokens, corresponding to a generated video of 16 seconds at 16 frames-per-second. We show multiple technical innovations and simplifications on the architecture, latent spaces, training objectives and recipes, data curation, evaluation protocols, parallelization techniques, and inference optimizations that allow us to reap the benefits of scaling pre-training data, model size, and training compute for training large scale media generation models. We hope this paper helps the research community to accelerate progress and innovation in media generation models. All videos from this paper are available at https://go.fb.me/MovieGenResearchVideos.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/56_MovieGen.pdf`

---
type: paper-pack
paper_id: "04-08"
stage: 4
title: "AudioGen: Textually Guided Audio Generation"
pdf: "/home/user/llm-papers/04_音乐生成/PDF/08_AudioGen.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 04-08 AudioGen: Textually Guided Audio Generation

**中文标题**：AudioGen：文本引导的音频生成

**一句话概括**：提出以文本描述为条件、基于学习到的离散音频表示的自回归生成模型 AudioGen，通过音频混合增强、多流建模与无分类器引导应对源分离、数据稀缺、序列过长等挑战，在客观与主观指标上均优于基线。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| curate | /kjˈʊəɹeɪt/ | 整理、汇集（收集并筛选数据集） | S |
| tackle | /tˈakəl/ | 应对、解决（问题） | A |
| perceptual | /pəsˈɛptʃuːəl/ | 感知的（人耳听感层面的质量） | A |
| adherence | /ɐdhˈiəɹəns/ | 贴合度（生成内容对文本的遵从程度） | A |
| condition on | /kəndˈɪʃən ˈɒn/ | 以…为条件（生成时给定文本输入） | A |
| auto-regressive | /ˈɔːtəʊɹɪɡɹˈɛsɪv/ | 自回归的（逐个预测生成） | A |
| pose | /pˈəʊz/ | 带来、构成（任务带来多重挑战） | A |
| alleviate | /ɐlˈiːvɪˌeɪt/ | 缓解（缓解上述挑战） | A |
| bitrate | /bˈɪtɹeɪt/ | 比特率（每秒传输的数据量） | A |
| differentiate | /dˌɪfəɹˈɛnʃɪˌeɪt/ | 区分（分离同时说话的多个人） | B |
| scarce | /skˈeəs/ | 稀少的（文本标注不足） | B |
| impose | /ɪmpˈəʊz/ | 施加（标注稀缺带来约束） | B |

### 原句（保留完整句子）

- **curate** — “For example, BLOOM \[78\] and PaLM \[56\] have use of these data resources, a large amount of data is curated multilingual data covering 46 and 122 languages, crawled from the web in previous work, such as Com- respectively, within their pre-training corpora.”
- **tackle** — “1 Published as a conference paper at ICLR 2023 In this work, we tackle the problem of generating audio samples conditioned on descriptive text captions.”
- **perceptual** — “For faster inference, we explore the use of multi-stream modeling, allowing the use of shorter sequences while maintaining a similar bitrate and perceptual quality.”
- **adherence** — “We apply classifier-free guidance to improve adherence to text.”
- **condition on** — “"sample conditioned on all previous ones"”
- **auto-regressive** — “In this work, we propose AUDIO G EN, an auto-regressive generative model that generates audio samples conditioned on text inputs.”
- **pose** — “It poses a significant challenge to develop capable artificial intelligence (AI) algorithms for comprehending and grasping a language.”
- **alleviate** — “To alleviate the aforementioned challenges we propose an augmentation technique that mixes different audio samples, driving the model to internally learn to separate multiple sources.”
- **bitrate** — “For faster inference, we explore the use of multi-stream modeling, allowing the use of shorter sequences while maintaining a similar bitrate and perceptual quality.”
- **differentiate** — “Audio is intrinsically a one dimensional signal and thus has less degrees of freedom to differentiate overlapping “objects” (Capon, 1969; Frost, 1972).”
- **scarce** — “Scarce text annotations impose another constraint, limiting the ability to scale models.”
- **impose** — “Scarce text annotations impose another constraint, limiting the ability to scale models.”

## Abstract（自动提取）

>  Published as a conference paper at ICLR 2023 AUDIO G EN : T EXTUALLY G UIDED AUDIO G ENERA TION Felix Kreuk1 , Gabriel Synnaeve1 , Adam Polyak1 , Uriel Singer1 , Alexandre Défossez1 , Jade Copet1 , Devi Parikh1 , Yaniv Taigman1 , Yossi Adi1,2 1 FAIR Team, Meta AI 2 The Hebrew University of Jerusalem felixkreuk@meta.com arXiv:2209.15352v2 \[cs.SD\] 5 Mar 2023 A BSTRACT We tackle the problem of generating audio samples conditioned on descriptive text captions. In this work, we propose AUDIO G EN, an auto-regressive generative model that generates audio samples conditioned on text inputs. AUDIO G EN operates on a learnt discrete audio representation. The task of text-to-audio generation poses multiple challenges. Due to the way audio travels through a medium, differentiating “objects” can be a difficult task (e.g., separating multiple people simultaneously speaking). This is further complicated by real-world recording conditions (e.g., background noise, reverberation, etc.). Scarce text annotations impose another constraint, limiting the ability to scale models.

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
- [[14_llm-papers/stage-04-music-generation|阶段 4]]

PDF：`/home/user/llm-papers/04_音乐生成/PDF/08_AudioGen.pdf`

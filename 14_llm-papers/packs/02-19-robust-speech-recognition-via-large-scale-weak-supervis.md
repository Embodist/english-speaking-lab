---
type: paper-pack
paper_id: "02-19"
stage: 2
title: "Robust Speech Recognition via Large-Scale Weak Supervision"
pdf: "/home/user/llm-papers/02_多模态/PDF/19_Whisper.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-19 Robust Speech Recognition via Large-Scale Weak Supervision

**中文标题**：通过大规模弱监督实现鲁棒语音识别

**一句话概括**：用 68 万小时多语言、多任务的弱监督数据训练语音识别系统，零样本迁移即可媲美全监督结果，接近人类准确率与鲁棒性。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| zero-shot | /zˈiəɹəʊʃˈɒt/ | 零样本的（不微调直接用于新场景） | S |
| competitive | /kəmpˈɛtɪtˌɪv/ | 有竞争力的（可与全监督结果相比） | S |
| inference | /ˈɪnfəɹəns/ | 推理（用训练好的模型做预测） | S |
| generalize | /dʒˈɛnəɹəlˌaɪz/ | 泛化（在新数据上表现良好） | S |
| robust | /ɹəʊbˈʌst/ | 鲁棒的、稳健的（对各种条件都稳定可靠） | S |
| fine-tuning | /fˈaɪntjˈuːnɪŋ/ | 微调（在任务数据上继续训练） | A |
| transcript | /tɹˈanskɹɪpt/ | 转录文本（音频对应的文字记录） | A |
| multilingual | /mˌʌltɪlˈɪŋɡwəl/ | 多语言的（覆盖多种语言） | A |
| robustness | /ɹəʊbˈʌstnəs/ | 鲁棒性（面对干扰/噪声的稳定性） | A |
| foundation | /faʊndˈeɪʃən/ | 基础（为后续研究提供基础） | A |
| weak supervision | /wˈiːk suːpəvˈɪʒən/ | 弱监督（用低质量、自动获取的标签训练） | B |
| multitask | /mˈʌltitˌask/ | 多任务的（同时学习多种任务） | B |

### 原句（保留完整句子）

- **zero-shot** — “Zero-shot Evaluation tem to further improve on clean read speech without further domain adaptation.” Yet seven years later the SOTA WER The goal of Whisper is to develop a single robust speech on LibriSpeech test-clean has dropped another 73% from processing system that works reliably without the need for their 5.3% to 1.4% (Zhang et al., 2021), far below their redataset specific fine-tuning to achieve high-quality results ported human-level error rate of 5.8%.”
- **competitive** — “(2021) documented a 9.2% increase in object supervision, the resulting models generalize well classification accuracy when fine-tuning a computer vision to standard benchmarks and are often competitive model on the ImageNet dataset (Russakovsky et al., 2015) with prior fully supervised results but in a zerowithout observing any improvement in average accuracy shot transfer setting without the need for any finewhen classifying the same objects on seven other natural tuning.”
- **inference** — “We are formance when trained on a dataset can still make many releasing models and inference code to serve as basic errors when evaluated on another, possibly precisely a foundation for further work on robust speech because it is exploiting those dataset-specific quirks that processing. humans are oblivious to (Geirhos et al., 2020).”
- **generalize** — “(2021) documented a 9.2% increase in object supervision, the resulting models generalize well classification accuracy when fine-tuning a computer vision to standard benchmarks and are often competitive model on the ImageNet dataset (Russakovsky et al., 2015) with prior fully supervised results but in a zerowithout observing any improvement in average accuracy shot transfer setting without the need for any finewhen classifying the same objects on seven other natural tuning.”
- **robust** — “Robust Speech Recognition via Large-Scale Weak Supervision Alec Radford * 1 Jong Wook Kim * 1 Tao Xu 1 Greg Brockman 1 Christine McLeavey 1 Ilya Sutskever 1 Abstract methods are exceedingly adept at finding patterns within a training dataset which boost performance on held-out data We study the capabilities of speech processing from the same dataset.”
- **fine-tuning** — “(2021) documented a 9.2% increase in object supervision, the resulting models generalize well classification accuracy when fine-tuning a computer vision to standard benchmarks and are often competitive model on the ImageNet dataset (Russakovsky et al., 2015) with prior fully supervised results but in a zerowithout observing any improvement in average accuracy shot transfer setting without the need for any finewhen classifying the same objects on seven other natural tuning.”
- **transcript** — “This results in a very diverse dataset ing beyond gold-standard crowdsourced datasets such as covering a broad distribution of audio from many different ImageNet (Russakovsky et al., 2015) to much larger but environments, recording setups, speakers, and languages. weakly supervised datasets significantly improves the roWhile diversity in audio quality can help train a model to be bustness and generalization of models (Mahajan et al., 2018; robust, diversity in transcript quality is not similarly beneKolesnikov et al., 2020). ficial.”
- **multilingual** — “In a particularly disturbing example, Radto 680,000 hours of multilingual and multitask ford et al.”
- **robustness** — “A model that achieves “superhuman” perapproach their accuracy and robustness.”
- **foundation** — “We are formance when trained on a dataset can still make many releasing models and inference code to serve as basic errors when evaluated on another, possibly precisely a foundation for further work on robust speech because it is exploiting those dataset-specific quirks that processing. humans are oblivious to (Geirhos et al., 2020).”
- **weak supervision** — “Robust Speech Recognition via Large-Scale Weak Supervision Alec Radford * 1 Jong Wook Kim * 1 Tao Xu 1 Greg Brockman 1 Christine McLeavey 1 Ilya Sutskever 1 Abstract methods are exceedingly adept at finding patterns within a training dataset which boost performance on held-out data We study the capabilities of speech processing from the same dataset.”
- **multitask** — “In a particularly disturbing example, Radto 680,000 hours of multilingual and multitask ford et al.”

## Abstract（自动提取）

> TITLE: Robust Speech Recognition via Large-Scale Weak Supervision ABSTRACT: We study the capabilities of speech processing systems trained simply to predict large amounts of transcripts of audio on the internet. When scaled to 680,000 hours of multilingual and multitask supervision, the resulting models generalize well to standard benchmarks and are often competitive with prior fully supervised results but in a zero-shot transfer setting without the need for any fine-tuning. When compared to humans, the models approach their accuracy and robustness. We are releasing models and inference code to serve as a foundation for further work on robust speech processing.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/19_Whisper.pdf`

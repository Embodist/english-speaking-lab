---
type: paper-pack
paper_id: "03-15"
stage: 3
title: "CLaMP: Contrastive Language-Music Pre-training for Cross-Modal Symbolic Music Information Retrieval"
pdf: "/home/user/llm-papers/03_音乐检索理解/PDF/15_CLaMP.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 03-15 CLaMP: Contrastive Language-Music Pre-training for Cross-Modal Symbolic Music Information Retrieval

**中文标题**：CLaMP：面向跨模态符号音乐信息检索的对比语言-音乐预训练

**一句话概括**：提出用对比损失联合训练音乐编码器与文本编码器的 CLaMP 模型，学习自然语言与符号音乐之间的跨模态表示，实现符号音乐的语义检索与零样本分类，并发布含 1010 张 ABC 记谱主旋律谱的 WikiMusicText 数据集。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| zero-shot | /zˈiəɹəʊʃˈɒt/ | 零样本的（无需微调即可分类新类别） | S |
| contrastive | /kˈɒntɹastˌɪv/ | 对比的（对比学习损失） | S |
| cross-modal | /kɹˈɒsmˈəʊdəl/ | 跨模态的（语言与音乐两个模态之间） | S |
| surpass | /səpˈas/ | 超越（超过以往模型的能力） | S |
| symbolic | /sɪmbˈɒlɪk/ | 符号的（以乐谱等符号形式表示的音乐） | A |
| jointly | /dʒˈɔɪntli/ | 联合地（两个编码器一起训练） | A |
| augmentation | /ˌɔːɡmɛntˈeɪʃən/ | 增强（扩充训练数据的手段） | A |
| dropout | /dɹˈɒpaʊt/ | 随机失活（文本丢弃，作数据增强） | A |
| patching | /pˈatʃɪŋ/ | 分块（把小节拼成块以压缩序列） | B |
| comprehension | /kˌɒmpɹɪhˈɛnʃən/ | 理解（编码器对音乐语境的把握） | B |
| semantic | /səmˈantɪk/ | 语义的（按含义进行搜索） | B |
| lead sheet | /lˈiːd ʃˈiːt/ | 主旋律谱（只记旋律与和弦的简谱） | B |

### 原句（保留完整句子）

- **zero-shot** — “CLaMP integrates textual information coders - one for music and one for text - trained jointly with to enable semantic search and zero-shot classification for a contrastive loss to learn cross-modal representations. symbolic music, surpassing the capabilities of previous models.”
- **contrastive** — “CLaMP integrates textual information coders - one for music and one for text - trained jointly with to enable semantic search and zero-shot classification for a contrastive loss to learn cross-modal representations. symbolic music, surpassing the capabilities of previous models.”
- **cross-modal** — “CLaMP integrates textual information coders - one for music and one for text - trained jointly with to enable semantic search and zero-shot classification for a contrastive loss to learn cross-modal representations. symbolic music, surpassing the capabilities of previous models.”
- **surpass** — “Even our base model surpasses all previously published models and ensembles, at a fraction of the training cost of any of the competitive models.”
- **symbolic** — “To pre-train CLaMP, we collected a large Symbolic Music Music dataset of 1.4 million music-text pairs.”
- **jointly** — “CLaMP integrates textual information coders - one for music and one for text - trained jointly with to enable semantic search and zero-shot classification for a contrastive loss to learn cross-modal representations. symbolic music, surpassing the capabilities of previous models.”
- **augmentation** — “It employed text M3 𝑀3 𝑀3 𝑇1 𝑀3 𝑇2 𝑀3 𝑇3 … 𝑀3 𝑇𝑁 Features dropout as a data augmentation technique and bar patch- Music … … … … … Encoder ing to efficiently represent music data which reduces se𝑀𝑁 𝑀𝑁 𝑇1 𝑀𝑁 𝑇2 𝑀𝑁 𝑇3 … 𝑀𝑁 𝑇𝑁 quence length to less than 10%.”
- **dropout** — “It employed text M3 𝑀3 𝑀3 𝑇1 𝑀3 𝑇2 𝑀3 𝑇3 … 𝑀3 𝑇𝑁 Features dropout as a data augmentation technique and bar patch- Music … … … … … Encoder ing to efficiently represent music data which reduces se𝑀𝑁 𝑀𝑁 𝑇1 𝑀𝑁 𝑇2 𝑀𝑁 𝑇3 … 𝑀𝑁 𝑇𝑁 quence length to less than 10%.”
- **patching** — “Our proposed exp(fm (mi ) · ft (ti )/τ ) log PN ), techniques include applying text dropout as a data j=1 ⊮i̸=j exp(fm (mj ) · ft (ti )/τ ) augmentation method, utilizing bar patching for efficient music representation, and implementing the where τ is a temperature hyper-parameter that controls the masked music model pre-training objective. sharpness of the softmax distribution, and ⊮i̸=j is an indicator function that equals 1 if i ̸= j, and 0 otherwise. • The cross-modal pre-training empowers CLaMP to The two terms in Eq.”
- **comprehension** — “In addition, we developed a masked music model pre-training objective to enhance the music encoder’s comprehension of musical con- Figure 1.”
- **semantic** — “CLaMP integrates textual information coders - one for music and one for text - trained jointly with to enable semantic search and zero-shot classification for a contrastive loss to learn cross-modal representations. symbolic music, surpassing the capabilities of previous models.”
- **lead sheet** — “The average number of tokens per lead sheet in Output Chars L : 1 / 8 END | : SP F SP | END the WikiMT dataset with different encoding methods.”

## Abstract（自动提取）

> .html \[17\] Q. Huang, A. Jansen, J. Lee, R. Ganti, J. Y. Li, \[23\] A. van den Oord, Y. Li, and O. Vinyals, “Repreand D. P. W. Ellis, “Mulan: A joint embedding sentation learning with contrastive predictive coding,” of music audio and natural language,” CoRR, vol. CoRR, vol. abs/1807.03748, 2018. \[Online\]. Available: abs/2208.12415, 2022. \[Online\]. Available: https: http://arxiv.org/abs/1807.03748 //doi.org/10.48550/arXiv.2208.12415 \[24\] Y. Liu, M. Ott, N. Goyal, J. Du, M. Joshi, \[18\] J. Devlin, M. Chang, K. Lee, and K. Toutanova, D. Chen, O. Levy, M. Lewis, L. Zettlemoyer, and “BERT: pre-training of deep bidirectional transformers V. Stoyanov, “Roberta: A robustly optimized BERT for language understanding,” in Proceedings of the pretraining approach,” CoRR, vol. abs/1907.11692, 2019 Conference of the North American Chapter 2019. \[Online\]. Available: http://arxiv.org/abs/1907. of the Association for Computational Linguistics: 11692 Human Language Technologies, NAACL-HLT 2019, \[25\] Y. Wu, K. Chen, T. Zhang, Y. Hui, T.

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
- [[14_llm-papers/stage-03-music-retrieval|阶段 3]]

PDF：`/home/user/llm-papers/03_音乐检索理解/PDF/15_CLaMP.pdf`

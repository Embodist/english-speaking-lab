---
type: paper-pack
paper_id: "03-11"
stage: 3
title: "MusicBERT: Symbolic Music Understanding with Large-Scale Pre-Training"
pdf: "/home/user/llm-papers/03_音乐检索理解/PDF/11_MusicBERT.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 03-11 MusicBERT: Symbolic Music Understanding with Large-Scale Pre-Training

**中文标题**：MusicBERT：大规模预训练的符号音乐理解

**一句话概括**：构建含百万级歌曲的符号音乐语料库，提出 OctupleMIDI 编码与小节级掩蔽策略，训练大规模预训练模型 MusicBERT，在旋律补全、伴奏建议等四项音乐理解任务上取得显著优势。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| corpus | /kˈɔːpəs/ | 语料库（大规模数据集） | S |
| symbolic | /sɪmbˈɒlɪk/ | 符号的（以 MIDI 等符号形式而非音频表示音乐） | A |
| hinder | /hˈɪndə/ | 阻碍（数据不足妨碍表示学习） | A |
| pre-training | /pɹˈiːtɹˈeɪnɪŋ/ | 预训练（先在大规模数据上训练通用模型） | A |
| inspire | /ɪnspˈaɪə/ | 启发（受 NLP 预训练成功启发） | A |
| tempo | /tˈɛmpəʊ/ | 速度（音乐的节拍速度） | A |
| melody | /mˈɛlədi/ | 旋律 | A |
| accompaniment | /ɐkˈʌmpɐnˌɪmənt/ | 伴奏 | A |
| ablation | /ɐblˈeɪʃən/ | 消融（消融实验：逐一去掉组件验证作用） | A |
| genre | /ʒˈɒnɹə/ | 流派、类型（音乐风格分类） | B |
| pitch | /pˈɪtʃ/ | 音高（音符的高低） | B |
| marginal | /mˈɑːdʒɪnəl/ | 微小的、边缘的（收益甚微） | B |

### 原句（保留完整句子）

- **corpus** — “To this end, we construct a to their shallow structures and limited unlabeled large-scale symbolic music corpus that con- data, such embedding-based approaches have limtains more than 1 million music songs.”
- **symbolic** — “To this end, we construct a to their shallow structures and limited unlabeled large-scale symbolic music corpus that con- data, such embedding-based approaches have limtains more than 1 million music songs.”
- **hinder** — “This process involves creatassessment, it is also often hindered by high annotation ing datasets annotated with preferences and feedback from costs, significant time requirements, and annotation inconhumans or proficient LLMs.”
- **pre-training** — “Inspired by the success of et al., 2020) leverage unlabeled music data to learn pre-training models in natural language pro- music token embeddings, similar to word embedcessing, in this paper, we develop MusicBERT, dings in natural language tasks.”
- **inspire** — “This study has inspired a large number of follow-up models for representation learning (beyond word sequence work, which sets the “pre-training and fine-tuning” learning modeling), having an important impact on the field of NLP. paradigm.”
- **tempo** — “Since ited capability to learn powerful music representasymbolic music contains more structural (e.g., tions. bar, position) and diverse information (e.g., In recent years, pre-trained language models tempo, instrument, and pitch), simply adopt- (e.g., BERT) have been verified to be powerful for ing the pre-training techniques from NLP to representation learning from large-scale unlabeled symbolic music only brings marginal gains.”
- **melody** — “Experiments demon- challenging to directly apply the pre-training techstrate the advantages of MusicBERT on four niques from NLP to symbolic music because of the music understanding tasks, including melody difference between natural text data and symbolic completion, accompaniment suggestion, genre music data.”
- **accompaniment** — “Experiments demon- challenging to directly apply the pre-training techstrate the advantages of MusicBERT on four niques from NLP to symbolic music because of the music understanding tasks, including melody difference between natural text data and symbolic completion, accompaniment suggestion, genre music data.”
- **ablation** — “Ablation studies also verify the effectiveness of tural (e.g., bar, position) and diverse (e.g., tempo, our designs of OctupleMIDI encoding and bar- instrument, and pitch), encoding symbolic music level masking strategy in MusicBERT. is more complicated than natural language.”
- **genre** — “Experiments demon- challenging to directly apply the pre-training techstrate the advantages of MusicBERT on four niques from NLP to symbolic music because of the music understanding tasks, including melody difference between natural text data and symbolic completion, accompaniment suggestion, genre music data.”
- **pitch** — “Since ited capability to learn powerful music representasymbolic music contains more structural (e.g., tions. bar, position) and diverse information (e.g., In recent years, pre-trained language models tempo, instrument, and pitch), simply adopt- (e.g., BERT) have been verified to be powerful for ing the pre-training techniques from NLP to representation learning from large-scale unlabeled symbolic music only brings marginal gains.”
- **marginal** — “Since ited capability to learn powerful music representasymbolic music contains more structural (e.g., tions. bar, position) and diverse information (e.g., In recent years, pre-trained language models tempo, instrument, and pitch), simply adopt- (e.g., BERT) have been verified to be powerful for ing the pre-training techniques from NLP to representation learning from large-scale unlabeled symbolic music only brings marginal gains.”

## Abstract（自动提取）

> TITLE: MusicBERT: Symbolic Music Understanding with Large-Scale Pre-Training ABSTRACT: Symbolic music understanding, which refers to the understanding of music from the symbolic data (e.g., MIDI format, but not audio), covers many music applications such as genre classification, emotion classification, and music pieces matching. While good music representations are beneficial for these applications, the lack of training data hinders representation learning. Inspired by the success of pre-training models in natural language processing, in this paper, we develop MusicBERT, a large-scale pre-trained model for music understanding. To this end, we construct a large-scale symbolic music corpus that contains more than 1 million music songs. Since symbolic music contains more structural (e.g., bar, position) and diverse information (e.g., tempo, instrument, and pitch), simply adopting the pre-training techniques from NLP to symbolic music only brings marginal gains. Therefore, we design several mechanisms, including OctupleMIDI encoding and bar-level masking strategy, to enhance pre-training with symbolic music data. Experiments demonstrate the advantages of MusicBERT on four music understanding tasks, including melody completion, accompaniment suggestion, genre classification, and style classification. Ablation studies also verify the effectiveness of our designs of OctupleMIDI encodi

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

PDF：`/home/user/llm-papers/03_音乐检索理解/PDF/11_MusicBERT.pdf`

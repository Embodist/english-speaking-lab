---
type: paper-pack
paper_id: "03-04"
stage: 3
title: "FMA: A Dataset For Music Analysis"
pdf: "/home/user/llm-papers/03_音乐检索理解/PDF/04_FMA_Dataset.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 03-04 FMA: A Dataset For Music Analysis

**中文标题**：FMA：用于音乐分析的数据集

**一句话概括**：介绍 Free Music Archive（FMA）开放数据集：包含 917 GiB、共 34.3 万天时长的创用 CC 许可音频，来自 10.6 万首曲目并按 161 个流派的层次分类组织，同时提供预计算特征、元数据与标签，可用于多种音乐信息检索任务。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| hierarchical | /haɪəɹˈɑːkɪkəl/ | 层次的（按等级结构分类） | S |
| baseline | /bˈeɪslaɪn/ | 基线（作对比的最简单方法） | S |
| accessible | /aksˈɛsəbəl/ | 易获取的（开放且方便使用） | A |
| availability | /ɐvˌeɪləbˈɪlɪti/ | 可用性、可获得性 | A |
| suitable | /sˈuːtəbəl/ | 适合的（适用于评测多项任务） | B |
| concerned with | /kənsˈɜːnd wˈɪð/ | 涉及、与…相关（研究领域关注的内容） | B |
| organize | /ˈɔːɡənˌaɪz/ | 整理、组织（管理大规模音乐库） | B |
| restrained | /ɹɪstɹˈeɪnd/ | 受限制的（发展被数据缺乏所制约） | B |
| hurdle | /hˈɜːdəl/ | 障碍、难关（需要克服的问题） | B |
| taxonomy | /taksˈɒnəmi/ | 分类体系（类别的树状结构） | B |
| metadata | /mˌɛtədˈeɪtə/ | 元数据（描述数据的数据） | B |
| split | /splˈɪt/ | 划分（训练/验证/测试集的切分） | B |

### 原句（保留完整句子）

- **hierarchical** — “Evaluation of algorithms using games: The case of muImagenet: A large-scale hierarchical image database. sic tagging.”
- **baseline** — “Further, it is common to set a maximum achieve better performance on mathematical reasoning tasks cap to control the maximum number of examples that a than baseline methods, with only 20% data synthesis cost. dataset can contain during instruction tuning \[82\], which • Instruction selection.”
- **accessible** — “97% date_created 64% date_released 18% tags Easily accessible.”
- **availability** — “With availability of audio, DL architectures ous case for the majority of tasks, in particular perceptual such as convolutional neural networks and recurrent neu- tasks.”
- **suitable** — “The subtle relation between scaling As the technical approach, it is useful to design suitable task law and emergent abilities can be explained by analogy with instructions or specific in-context learning strategies to elicit the ability acquisition of human11 .”
- **concerned with** — “"a field concerned with browsing, searching, and"”
- **organize** — “The above constraints are satisfied for all subsets, and a 3.2 Genre Recognition track is assigned to the same split across all of them.5 The 2,231 tracks without genre label are assigned to the train- Music genres are categories that have arisen through a ing set (full and large sets) as they might be useful as addi- complex interplay of cultures, artists, and market forces to tional training samples for semi-supervised algorithms. characterize similarities between compositions and organize music collections.”
- **restrained** — “The commu- MusiClef \[36\] 1,355 218 2012 yes Artist20 \[7\] 1,413 20 2007 yes nity’s growing interest in feature and end-to-end learning ISMIR2004 1,458 - 2004 yes is however restrained by the limited availability of large Homburg \[15\] 1,886 1,463 2005 yes arXiv:1612.01840v3 \[cs.SD\] 5 Sep 2017 audio datasets.”
- **hurdle** — “The FMA aims to overcome this hurdle by 103-Artists \[30\] 2,445 103 2005 yes providing 917 GiB and 343 days of Creative Commons- Unique \[41\] 3,115 3,115 2010 yes 1517-Artists \[40\] 3,180 1,517 2008 yes licensed audio from 106,574 tracks from 16,341 artists LMD \[42\] 3,227 - 2007 no and 14,854 albums, arranged in a hierarchical taxonomy of EBallroom \[23\] 4,180 - 2016 no2 161 genres.”
- **taxonomy** — “While there is no agreement on a taxonomy of gen- 2.”
- **metadata** — “It provides full-length and high-quality audio, USPOP \[1\] 8,752 400 2003 no pre-computed features, together with track- and user-level CAL10k \[44\] 10,271 4,597 2010 no metadata, tags, and free-form text such as biographies.”
- **split** — “1 Chroma \[11\] 84 44 44 48 49 2 Tonnetz \[14\] 42 40 37 42 41 2.7 Splits 3 MFCC \[33\] 140 58 55 61 53 4 Spec. centroid 7 42 45 46 48 We propose an 80/10/10% split into training, validation 5 Spec. bandwidth 7 41 45 44 45 6 Spec. contrast \[17\] 49 51 50 54 53 and test sets to make research on the FMA reproducible.”

## Abstract（自动提取）

>  FMA: A DATASET FOR MUSIC ANALYSIS Michaël Defferrard† Kirell Benzi† Pierre Vandergheynst† Xavier Bresson‡ † LTS2, EPFL, Switzerland ‡ SCSE, NTU, Singapore Work conducted when XB was at EPFL. {michael.defferrard,kirell.benzi,pierre.vandergheynst}@epfl.ch, xbresson@ntu.edu.sg ABSTRACT dataset1 #clips #artists year audio RWC \[12\] 465 - 2001 yes We introduce the Free Music Archive (FMA), an open CAL500 \[45\] 500 500 2007 yes and easily accessible dataset suitable for evaluating sev- Ballroom \[13\] 698 - 2004 yes eral tasks in MIR, a field concerned with browsing, search- GTZAN \[46\] 1,000 ∼ 300 2002 yes ing, and organizing large music collections. The commu- MusiClef \[36\] 1,355 218 2012 yes Artist20 \[7\] 1,413 20 2007 yes nity’s growing interest in feature and end-to-end learning ISMIR2004 1,458 - 2004 yes is however restrained by the limited availability of large Homburg \[15\] 1,886 1,463 2005 yes arXiv:1612.01840v3 \[cs.SD\] 5 Sep 2017 audio datasets.

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

PDF：`/home/user/llm-papers/03_音乐检索理解/PDF/04_FMA_Dataset.pdf`

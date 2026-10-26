---
type: paper-pack
paper_id: "02-17"
stage: 2
title: "Segment Anything"
pdf: "/home/user/llm-papers/02_多模态/PDF/17_SAM_SegmentAnything.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-17 Segment Anything

**中文标题**：分割一切

**一句话概括**：提出 Segment Anything（SA）项目：新任务、可提示（promptable）模型与含 10 亿掩码、1100 万图像的最大分割数据集 SA-1B。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| competitive | /kəmpˈɛtɪtˌɪv/ | 有竞争力的（接近甚至超过全监督方法） | S |
| superior | /suːpˈiəɹɪə/ | 更优的（超过之前全监督结果） | A |
| foster | /fˈɒstə/ | 促进、推动（推动基础模型研究） | A |
| corresponding | /kˌɒɹɪspˈɒndɪŋ/ | 相应的（与模型配套的数据集） | A |
| mask | /mˈask/ | 掩码（标注物体区域的像素级标记） | A |
| distribution | /dˌɪstɹɪbjˈuːʃən/ | 分布（数据分布，指新的图像分布） | A |
| segment | /sˈɛɡmənt/ | 分割（把图像中的物体区域划分出来） | B |
| data collection loop | /dˈeɪtə kəlˈɛkʃən lˈuːp/ | 数据采集闭环（用模型辅助收集数据再训练模型的循环） | B |
| licensed | /lˈaɪsənst/ | 有许可的（数据使用合规授权） | B |
| privacy respecting | /pɹˈɪvəsi ɹɪspˈɛktɪŋ/ | 尊重隐私的（不泄露个人信息） | B |
| promptable | /pɹˈɒmptəbəl/ | 可提示的（接受点、框等提示输入的） | B |
| evaluate | /ɪvˈaljuːˌeɪt/ | 评估（系统评测模型能力） | B |

### 原句（保留完整句子）

- **competitive** — “Once trained, engineered text prompts enable its zero-shot performance is impressive – often competitive zero-shot generalization to novel visual concepts and data with or even superior to prior fully supervised results.”
- **superior** — “Once trained, engineered text prompts enable its zero-shot performance is impressive – often competitive zero-shot generalization to novel visual concepts and data with or even superior to prior fully supervised results.”
- **foster** — “While much progress has https://segment-anything.com to foster research into foun- been made on vision and language encoders, computer vidation models for computer vision. sion includes a wide range of problems beyond this scope, and for many of these, abundant training data does not exist.”
- **corresponding** — “What is the corresponding model architecture? few-shot performance compares surprisingly well to (even 3.”
- **mask** — “In NLP and more recently computer vision, objects, helping increase mask diversity.”
- **distribution** — “Number of images per country 800k Asia & Oceania Per country 600k Africa Europe image count North America ≥ 100k 400k Latin America & Caribbean < 100k 200k < 10k < 1k 0 RUS THA USA ITA GBR DEU ESP IDN UKR FRA JPN MYS TUR IND CHN POL NLD VNM BRA CAN GRC AUS PRT CZE BLR ROU KOR ARE AUT SWE TWN HKG CHE ISR SGP HUN BEL HRV BGR PHL KAZ MEX NOR MMR ZAF SRB DNK MAR FIN LVA 50 most common countries (ISO codes) Figure 7: Estimated geographic distribution of SA-1B images.”
- **segment** — “Segment Anything Alexander Kirillov1,2,4 Eric Mintun2 Nikhila Ravi1,2 Hanzi Mao2 Chloe Rolland3 Laura Gustafson3 Tete Xiao3 Spencer Whitehead Alexander C.”
- **data collection loop** — “Using our dataset size, and total training compute \[56, 10, 21, 51\]. efficient model in a data collection loop, we built the largest Foundation models have also been explored in computer segmentation dataset to date (by far), with over 1 billion vision, albeit to a lesser extent.”
- **licensed** — “Perhaps the most promimasks on 11M licensed and privacy respecting images.”
- **privacy respecting** — “Perhaps the most promimasks on 11M licensed and privacy respecting images.”
- **promptable** — “The nent illustration aligns paired text and images from the web. model is designed and trained to be promptable, so it can For example, CLIP \[82\] and ALIGN \[55\] use contrastive transfer zero-shot to new image distributions and tasks.”
- **evaluate** — “We learning to train text and image encoders that align the two evaluate its capabilities on numerous tasks and find that modalities.”

## Abstract（自动提取）

> TITLE: Segment Anything ABSTRACT: We introduce the Segment Anything (SA) project: a new task, model, and dataset for image segmentation. Using our efficient model in a data collection loop, we built the largest segmentation dataset to date (by far), with over 1 billion masks on 11M licensed and privacy respecting images. The model is designed and trained to be promptable, so it can transfer zero-shot to new image distributions and tasks. We evaluate its capabilities on numerous tasks and find that its zero-shot performance is impressive -- often competitive with or even superior to prior fully supervised results. We are releasing the Segment Anything Model (SAM) and corresponding dataset (SA-1B) of 1B masks and 11M images at https://segment-anything.com to foster research into foundation models for computer vision.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/17_SAM_SegmentAnything.pdf`

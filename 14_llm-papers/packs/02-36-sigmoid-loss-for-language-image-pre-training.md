---
type: paper-pack
paper_id: "02-36"
stage: 2
title: "Sigmoid Loss for Language Image Pre-Training"
pdf: "/home/user/llm-papers/02_多模态/PDF/36_SigLIP.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 02-36 Sigmoid Loss for Language Image Pre-Training

**中文标题**：用于语言-图像预训练的 Sigmoid 损失（SigLIP）

**一句话概括**：提出成对 Sigmoid 损失替代 softmax 对比损失，无需全局归一化即可解耦批大小与损失，小批训练更好、大批可扩到百万，两天内达 84.5% 零样本准确率。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| zero-shot | /zˈiəɹəʊʃˈɒt/ | 零样本的；未经微调直接测试 | S |
| pre-training | /pɹˈiːtɹˈeɪnɪŋ/ | 预训练；在大规模数据上先训练通用表征 | A |
| contrastive learning | /kˈɒntɹastˌɪv lˈɜːnɪŋ/ | 对比学习；拉近匹配样本、推开不匹配样本 | A |
| normalization | /nˌɔːməlaɪzˈeɪʃən/ | 归一化；把相似度缩放到可比范围 | A |
| similarity | /sˌɪmɪlˈaɹɪti/ | 相似度；图像与文本特征的距离度量 | A |
| sufficient | /səfˈɪʃənt/ | 足够的；32k 已够用 | A |
| pairwise | /pˈeəwaɪz/ | 成对的；逐对图像-文本计算损失 | B |
| global | /ɡlˈəʊbəl/ | 全局的；跨整批样本的统计量 | B |
| batch size | /bˈatʃ sˈaɪz/ | 批大小；一次训练用的样本数量 | B |
| disentanglement | /dˌɪsɛntˈaŋɡəlmənt/ | 解耦；使损失不再依赖批大小 | B |
| negative | /nˈɛɡətˌɪv/ | 负样本；与正样本不匹配的配对 | B |
| diminish | /dɪmˈɪnɪʃ/ | 减弱；收益随规模增加而递减 | B |

### 原句（保留完整句子）

- **zero-shot** — “The last two Tuning, with only four TPUv4 chips, we train a SigLiT rows show results with randomly initialized models. model that achieves 84.5% ImageNet zero-shot accuracy in two days.”
- **pre-training** — “Sigmoid Loss for Language Image Pre-Training Xiaohua Zhai?”
- **contrastive learning** — “Given a mini-batch B = {(I1 , T1 ), (I2 , T2 ), . . . } of Contrastive language-image pre-training has become image-text pairs, the contrastive learning objective encourpopular since CLIP \[36\] and ALIGN \[23\] applied softmax ages embeddings of matching pairs (Ii , Ti ) to align with contrastive learning \[60, 46, 10, 24\] to large-scale imageeach other, while pushing embeddings of unmatched pairs text datasets.”
- **normalization** — “Unlike standard trained on the LiT image-text dataset \[59\] using four TPUcontrastive learning with softmax normalization, the sig- v4 chips for one day, achieves 79.7% 0-shot accuracy on moid loss operates solely on image-text pairs and does not ImageNet.”
- **similarity** — “This is achieved via a Contrastive pre-training using weak supervision from batch-level softmax-based contrastive loss, applied twice to image-text pairs found on the web is becoming the go-to normalize the pairwise similarity scores across all images, method for obtaining generic computer vision backbones, then all texts.”
- **sufficient** — “32 k, is sufficient for image-text pre- instead, while CoCa \[56\] adds such a decoder to the distraining.”
- **pairwise** — “We propose a simple pairwise Sigmoid loss for SigLiT model with a frozen public B/8 checkpoint \[42\], Language-Image Pre-training (SigLIP).”
- **global** — “The same setup with a g/14 checkpoint \[58\] require a global view of the pairwise similarities for nor- leads to 84.5% accuracy, trained for two days.”
- **batch size** — “The sigmoid loss simultaneously allows fur- lic unlocked B/16 image checkpoint \[42\], trained on the ther scaling up the batch size, while also performing bet- WebLI dataset \[13\], SigLIP achieves 71.0% 0-shot accuter at smaller batch sizes.”
- **disentanglement** — “The disentanglement of the batch size from Image Text BS #TPUv4 Days INet-0 the loss further allows us to study the impact of examples vs pairs and negative to positive ratio.”
- **negative** — “The disentanglement of the batch size from Image Text BS #TPUv4 Days INet-0 the loss further allows us to study the impact of examples vs pairs and negative to positive ratio.”
- **diminish** — “Our best SigLiT with a B-sized text mode the softmax losses diminish.”

## Abstract（自动提取）

> TITLE: Sigmoid Loss for Language Image Pre-Training ABSTRACT: We propose a simple pairwise Sigmoid loss for Language-Image Pre-training (SigLIP). Unlike standard contrastive learning with softmax normalization, the sigmoid loss operates solely on image-text pairs and does not require a global view of the pairwise similarities for normalization. The sigmoid loss simultaneously allows further scaling up the batch size, while also performing better at smaller batch sizes. Combined with Locked-image Tuning, with only four TPUv4 chips, we train a SigLiT model that achieves 84.5% ImageNet zero-shot accuracy in two days. The disentanglement of the batch size from the loss further allows us to study the impact of examples vs pairs and negative to positive ratio. Finally, we push the batch size to the extreme, up to one million, and find that the benefits of growing batch size quickly diminish, with a more reasonable batch size of 32k being sufficient. We release our models at https://github.com/google-research/big_vision and hope our research motivates further explorations in improving the quality and efficiency of language-image pre-training.

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

PDF：`/home/user/llm-papers/02_多模态/PDF/36_SigLIP.pdf`

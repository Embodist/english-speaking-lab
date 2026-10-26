---
type: paper-pack
paper_id: "05-15"
stage: 5
title: "Revisiting Feature Prediction for Learning Visual Representations from Video"
pdf: "/home/user/llm-papers/05_世界模型/PDF/15_VJEPA.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 05-15 Revisiting Feature Prediction for Learning Visual Representations from Video

**中文标题**：重新审视特征预测：从视频学习视觉表征（V-JEPA）

**一句话概括**：探索把特征预测作为从视频做无监督学习的独立目标，提出 V-JEPA 视觉模型族：纯用特征预测目标训练（无预训练图像编码器、文本、负样本、重建等监督），学得通用表征，冻结主干即可用于多种任务。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| downstream | /dˈaʊnstɹiːm/ | 下游的；后续的任务 | S |
| reconstruction | /ɹˌiːkənstɹˈʌkʃən/ | 重建；把输入重新生成出来 | A |
| versatile | /vˈɜːsətˌaɪl/ | 多用途的、通用的 | A |
| solely | /sˈəʊlli/ | 仅仅、只 | A |
| supervision | /suːpəvˈɪʒən/ | 监督；训练所用的标注信号 | A |
| stand-alone objective | /stˈandɐlˈəʊn ɒbdʒˈɛktɪv/ | 独立目标；单独使用的训练目标 | B |
| negative examples | /nˈɛɡətˌɪv ɛɡzˈampəlz/ | 负样本；需要区分开的反例 | B |
| frozen backbone | /fɹˈəʊzən bˈakbəʊn/ | 冻结的主干网络；参数不更新的特征提取网络 | B |
| appearance-based | /ɐpˈiəɹənsbˈeɪst/ | 基于外观的；依赖物体长相的任务 | B |
| feature prediction | /fˈiːtʃə pɹɪdˈɪkʃən/ | 特征预测；预测其他区域的特征 | B |
| unsupervised learning | /ʌnsˈuːpəvˌaɪzd lˈɜːnɪŋ/ | 无监督学习 | B |
| adaption | /ɐdˈapʃən/ | 调整、适配 | B |

### 原句（保留完整句子）

- **downstream** — “The models are trained on 2 million videos collected from public datasets and are evaluated on downstream image and video tasks.”
- **reconstruction** — “De- of vision transformers (Dosovitskiy et al., 2020; Li et al., creasing the available number of labeled examples re- 2022) has become standard practice in self-supervised sults in an increase in the performance gap between learning with joint-embedding architectures (Chen et al., V-JEPA and pixel-reconstruction models (Table 7).”
- **versatile** — “Our results show that learning by predicting video features leads to versatile visual representations that perform well on both motion and appearance-based tasks, without adaption of the model’s parameters; e.g., using a frozen backbone.”
- **solely** — “Finally, we emIn this work, we explored the effectiveness of feature pirically observed that V-JEPA models are label-efficient prediction as a stand-alone objective for unsupervised learners, and exhibit good performance on downstream learning from video and introduced V-JEPA, a collection tasks, even when only few labeled examples are available. of vision models trained solely using a self-supervised feature prediction objective.”
- **supervision** — “The Open- Something-v2), the V-JEPA models provide a major imCLIP model is trained with a contrastive image-text provement (over +21 points) compared to large-scale alignment objective, DINOv2 and I-JEPA are trained image baselines, such as DINOv2, OpenCLIP, and Iwith self-supervision.”
- **stand-alone objective** — “Srivastava an effective stand-alone objective for unsupervised learn- et al.”
- **negative examples** — “text, negative examples, reconstruction, or other sources of supervision”
- **frozen backbone** — “Our results show that learning by predicting video features leads to versatile visual representations that perform well on both motion and appearance-based tasks, without adaption of the model’s parameters; e.g., using a frozen backbone.”
- **appearance-based** — “Our results show that learning by predicting video features leads to versatile visual representations that perform well on both motion and appearance-based tasks, without adaption of the model’s parameters; e.g., using a frozen backbone.”
- **feature prediction** — “70 72 74 76 78 80 82 84 86 88 90 92 In this work, we revisit feature prediction as a standKinetics 400 alone objective for unsupervised learning of visual representations from video.”
- **unsupervised learning** — “A long-standing goal of the machine learning ViT-g/14 community is to identify the principles or objectives that DINOv2 I-JEPA may guide such unsupervised learning in humans (Field, 50 ViT-H/16 ViT-g/14 1994; Berkes and Wiskott, 2005; Hinton, 1989).”
- **adaption** — “Our results show that learning by predicting video features leads to versatile visual representations that perform well on both motion and appearance-based tasks, without adaption of the model’s parameters; e.g., using a frozen backbone.”

## Abstract（自动提取）

> TITLE: Revisiting Feature Prediction for Learning Visual Representations from Video ABSTRACT: This paper explores feature prediction as a stand-alone objective for unsupervised learning from video and introduces V-JEPA, a collection of vision models trained solely using a feature prediction objective, without the use of pretrained image encoders, text, negative examples, reconstruction, or other sources of supervision. The models are trained on 2 million videos collected from public datasets and are evaluated on downstream image and video tasks. Our results show that learning by predicting video features leads to versatile visual representations that perform well on both motion and appearance-based tasks, without adaption of the model's parameters; e.g., using a frozen backbone. Our largest model, a ViT-H/16 trained only on videos, obtains 81.9% on Kinetics-400, 72.2% on Something-Something-v2, and 77.9% on ImageNet1K.

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
- [[14_llm-papers/stage-05-world-models|阶段 5]]

PDF：`/home/user/llm-papers/05_世界模型/PDF/15_VJEPA.pdf`

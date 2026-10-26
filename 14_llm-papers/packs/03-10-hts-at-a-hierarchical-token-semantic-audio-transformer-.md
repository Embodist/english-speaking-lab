---
type: paper-pack
paper_id: "03-10"
stage: 3
title: "HTS-AT: A Hierarchical Token-Semantic Audio Transformer for Sound Classification and Detection"
pdf: "/home/user/llm-papers/03_音乐检索理解/PDF/10_HTSAT.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 03-10 HTS-AT: A Hierarchical Token-Semantic Audio Transformer for Sound Classification and Detection

**中文标题**：HTS-AT：用于声音分类与检测的分层词元-语义音频 Transformer

**一句话概括**：提出带分层结构以缩小模型规模、缩短训练时间的音频 Transformer HTS-AT，并加入词元-语义模块把输出映射为类别特征图以支持音频事件检测（时间定位），在 AudioSet、ESC-50 上取得新的最优结果且仅需原模型 35% 参数。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| state-of-the-art | /stˈeɪtɒvðɪˈɑːt/ | 最先进的（当时最优结果） | S |
| hierarchical | /haɪəɹˈɑːkɪkəl/ | 分层的（多层次网络结构） | S |
| corresponding | /kˌɒɹɪspˈɒndɪŋ/ | 对应的（与样本相应的标签） | A |
| mapping | /mˈapɪŋ/ | 映射（样本到标签的对应） | A |
| adopt | /ɐdˈɒpt/ | 采用（Transformer 被引入该领域） | A |
| rely on | /ɹɪlˈaɪ ˈɒn/ | 依赖 | A |
| scalability | /skˌeɪləbˈɪlɪti/ | 可扩展性（模型在音频任务上的扩展能力） | A |
| localization | /lˌəʊkəlaɪzˈeɪʃən/ | 定位（在时间轴上确定事件位置） | A |
| efficiency | /ɪfˈɪʃənsi/ | 效率（高性能与高效率） | A |
| token-semantic | /tˈəʊkənsəmˈantɪk/ | 词元-语义的（把词元映射到语义特征） | B |
| meanwhile | /mˈiːnwaɪl/ | 与此同时（还依赖预训练视觉模型） | B |
| combat | /kˈɒmbat/ | 应对、克服（问题） | B |

### 原句（保留完整句子）

- **state-of-the-art** — “On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature.”
- **hierarchical** — “This approach (exemplified by with intermediate reasoning steps, it is mainly effective Tree of Thoughts (ToT) \[444, 517\]) formulates the reasoning for the tasks that require step-by-step reasoning \[33\], e.g., process in a hierarchical tree structure, where intermediate arithmetic reasoning, commonsense reasoning, and symthoughts are nodes.”
- **corresponding** — “"corresponding to the three levels of music"”
- **mapping** — “Through adversarial loss, MSVC-GAN learns the acoustic feature distribution of different singers, and establishes the forward and reverse mapping among the acoustic features of different singers, that is, the model can learn a unique function for all many-to-many mappings.”
- **adopt** — “Existing LLMs adopt similar Trans- α β where a = α+β , b = α+β and G is a scaling coefficient that former architectures and pre-training objectives (e.g., lancan be computed by A, B , α and β .”
- **rely on** — “"meanwhile relying on pretrained vision models to"”
- **scalability** — “DeMultiMedQA has been combined with MMLU \[362\] to spite their scalability and explanability, model-based apassess the performance of specialized LLMs for healthcare, proaches have been found to suffer from several issues, insuch as Med-PaLM \[354\].”
- **localization** — “Some works adopt further finetuning to imopment of advanced models with more multimodal prove the planning abilities with respect to tool ustokens, e.g. long-video understanding, and long docage \[107\] or to improve localization capabilities \[142\], \[205\] uments interleaved with images and text. of the system.”
- **efficiency** — “Recent work has achieved significant improvements in computational efficiency through factorization tricks \[21\] and conditional computation \[32\], while also improving model performance in case of the latter.”
- **token-semantic** — “Hts-at: A hierarchical Li, Zhenqiang Li, Karttikeya Mangalam, Raghava Modhugu, token-semantic audio transformer for sound classification Jonathan Munro, Tullie Murrell, Takumi Nishiyasu, Will and detection.”
- **meanwhile** — “Meanwhile, we drew a schematic diagram de- basic understanding of this claim is that each (NLP) task picting the technological evolution of the GPT-series models can be considered as the word prediction problem based in Figure 4.”
- **combat** — “LRV-Instruction \[90\] The LRV-Instruction dataset is designed to combat hallucination in large multi-modal models.”

## 摘要提示（PDF 文本不可提取）

> 提出带分层结构以缩小模型规模、缩短训练时间的音频 Transformer HTS-AT，并加入词元-语义模块把输出映射为类别特征图以支持音频事件检测（时间定位），在 AudioSet、ESC-50 上取得新的最优结果且仅需原模型 35% 参数。

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

PDF：`/home/user/llm-papers/03_音乐检索理解/PDF/10_HTSAT.pdf`

---
type: paper-pack
paper_id: "05-18"
stage: 5
title: "Cosmos World Foundation Model Platform for Physical AI"
pdf: "/home/user/llm-papers/05_世界模型/PDF/18_Cosmos_WorldFoundationModel.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 05-18 Cosmos World Foundation Model Platform for Physical AI

**中文标题**：Cosmos 世界基础模型平台：面向物理 AI

**一句话概括**：提出 Cosmos 世界基础模型平台，面向物理 AI 提供可微调为定制世界模型的通用世界基础模型，涵盖视频筛选流水线、预训练世界基础模型、后训练示例与视频分词器，并开源开放权重。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| pre-trained | /pɹˈiːtɹˈeɪnd/ | 预训练的 | A |
| fine-tuned | /fˈaɪntjˈuːnd/ | 微调的；在预训练基础上针对性训练 | A |
| general-purpose | /dʒˈɛnəɹəlpˈɜːpəs/ | 通用目的的 | A |
| post-training | /pˈəʊsttɹˈeɪnɪŋ/ | 后训练；预训练后的继续训练 | A |
| customized | /kˈʌstəmˌaɪzd/ | 定制化的 | A |
| digital twin | /dˈɪdʒɪtəl twˈɪn/ | 数字孪生；现实对象的数字复制品 | B |
| physical AI | /fˈɪzɪkəl ˌeɪˈaɪ/ | 物理 AI；运行于真实物理世界的 AI | B |
| curation pipeline | /kjʊəɹˈeɪʃən pˈaɪplaɪn/ | 数据筛选流水线；清洗选择数据的流程 | B |
| tokenizers | /tˈəʊkənˌaɪzəz/ | 分词器/令牌化器；把视频转为离散 token | B |
| downstream applications | /dˈaʊnstɹiːm ˌaplɪkˈeɪʃənz/ | 下游应用 | B |
| open-weight | /ˈəʊpənwˈeɪt/ | 开放权重的；公开模型参数 | B |
| permissive licenses | /pəmˈɪsɪv lˈaɪsənsɪz/ | 宽松许可协议；使用限制很少的授权 | B |

### 原句（保留完整句子）

- **pre-trained** — “Recently, pre-trained language models (PLMs) have been proposed by pretraining Transformer models over large-scale corpora, showing strong capabilities in solving various natural language processing (NLP) tasks.”
- **fine-tuned** — “Because it has a relatively small model 12. https://openai.com/blog/chatgpt-plugins size, it has been widely fine-tuned in downstream tasks, 13.”
- **general-purpose** — “These pre-trained context-aware word representations for learning distributed word representations, which were are very effective as general-purpose semantic features, demonstrated to be very effective across a variety of NLP which have largely raised the performance bar of NLP tasks.”
- **post-training** — “Existing decoding methods proaches, namely quantization-aware training (QAT) (requirpredominantly adopt the autoregressive mechanism, gen- ing additional full model retraining) and post-training quantierating tokens one by one, which is a primary reason zation (PTQ) (requires no model retraining).”
- **customized** — “"propose customized video tube masking with an extremely high ratio"”
- **digital twin** — “a digital twin of itself, the policy model”
- **physical AI** — “Physical AI needs to be trained digitally first”
- **curation pipeline** — “our platform covers a video curation pipeline”
- **tokenizers** — “Thus, several neural network models igram tokenization \[244\] starts with a sufficiently large employ character as the minimum unit to derive the word set of possible substrings or subtokens for a corpus, and representation (e.g., a CNN word encoder in ELMo \[21\]). iteratively removes the tokens in the current vocabulary Recently, subword tokenizers have been widely used in Trans- until the expected vocabulary size is reached.”
- **downstream applications** — “for downstream applications”
- **open-weight** — “our models open-weight with permissive licenses”
- **permissive licenses** — “open-weight with permissive licenses”

## 摘要提示（PDF 文本不可提取）

> 提出 Cosmos 世界基础模型平台，面向物理 AI 提供可微调为定制世界模型的通用世界基础模型，涵盖视频筛选流水线、预训练世界基础模型、后训练示例与视频分词器，并开源开放权重。

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

PDF：`/home/user/llm-papers/05_世界模型/PDF/18_Cosmos_WorldFoundationModel.pdf`

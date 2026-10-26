---
type: paper-pack
paper_id: "01-18"
stage: 1
title: "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity"
pdf: "/home/user/llm-papers/01_大模型/PDF/18_SwitchTransformer.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 01-18 Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity

**中文标题**：Switch Transformer：用简单高效的稀疏性扩展到万亿参数模型

**一句话概括**：简化 MoE 路由算法、解决训练不稳定问题，首次实现万亿参数稀疏模型用低精度（bfloat16）训练，并显著提升预训练速度。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| sparse | /spˈɑːs/ | 稀疏的（只激活部分参数） | S |
| instability | /ɪnstəbˈɪlɪti/ | 不稳定性（训练过程波动） | A |
| defies | /dɪfˈaɪz/ | 打破、违背（常规做法） | B |
| sparsely-activated | /spˈɑːsliˈaktɪvˌeɪtɪd/ | 稀疏激活的（每次只运行部分参数） | B |
| outrageous | /aʊtɹˈeɪdʒəs/ | 惊人的、夸张的 | B |
| hindered | /hˈɪndəd/ | 阻碍 | B |
| routing | /ɹˈaʊtɪŋ/ | 路由的（决定把输入分给哪个专家） | B |
| intuitive | /ɪntjˈuːɪtˌɪv/ | 直观的、易理解的 | B |
| wrangle | /ɹˈaŋɡəl/ | 驯服、解决（棘手问题） | B |
| precision | /pɹɪsˈɪʒən/ | 精度（数值表示精度，如 bfloat16） | B |

### 原句（保留完整句子）

- **sparse** — “Our proposed training techniques mitigate the instabilities, and we show large sparse models may be trained, for the first time, with lower precision (bfloat16) formats.”
- **instability** — “However, despite several notable successes of MoE, widespread adoption has been hindered by complexity, communication costs, and training instability.”
- **defies** — “"Mixture of Experts (MoE) defies this and instead selects different parameters"”
- **sparsely-activated** — “The result is a sparsely-activated model—with an outrageous number of parameters—but a constant computational cost.”
- **outrageous** — “The result is a sparsely-activated model—with an outrageous number of parameters—but a constant computational cost.”
- **hindered** — “However, despite several notable successes of MoE, widespread adoption has been hindered by complexity, communication costs, and training instability.”
- **routing** — “We simplify the MoE routing algorithm and design intuitive improved models with reduced communication and computational costs.”
- **intuitive** — “We simplify the MoE routing algorithm and design intuitive improved models with reduced communication and computational costs.”
- **wrangle** — “"Our proposed training techniques help wrangle the instabilities"”
- **precision** — “Our proposed training techniques mitigate the instabilities, and we show large sparse models may be trained, for the first time, with lower precision (bfloat16) formats.”

## Abstract（自动提取）

> TITLE: Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity ABSTRACT: In deep learning, models typically reuse the same parameters for all inputs. Mixture of Experts (MoE) defies this and instead selects different parameters for each incoming example. The result is a sparsely-activated model -- with outrageous numbers of parameters -- but a constant computational cost. However, despite several notable successes of MoE, widespread adoption has been hindered by complexity, communication costs and training instability -- we address these with the Switch Transformer. We simplify the MoE routing algorithm and design intuitive improved models with reduced communication and computational costs. Our proposed training techniques help wrangle the instabilities and we show large sparse models may be trained, for the first time, with lower precision (bfloat16) formats. We design models based off T5-Base and T5-Large to obtain up to 7x increases in pre-training speed with the same computational resources. These improvements extend into multilingual settings where we measure gains over the mT5-Base version across all 101 languages. Finally, we advance the current scale of language models by pre-training up to trillion parameter models on the "Colossal Clean Crawled Corpus" and achieve a 4x speedup over the T5-XXL model.

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
- [[14_llm-papers/stage-01-llm|阶段 1]]

PDF：`/home/user/llm-papers/01_大模型/PDF/18_SwitchTransformer.pdf`

---
type: source
title: "论文阅读清单（原始副本）"
tags: [topic/paper, skill/reading]
created: 2026-10-24
---

> [!info] 来源说明
> 这是 `~/llm-papers/阅读清单.md` 的副本。PDF 原文件在 `~/llm-papers/<阶段>/PDF/`；文中的相对链接以原目录为基准。逐篇词汇见 [[14_llm-papers/_index|LLM 论文阅读与词汇]]。

# AI 方向学习论文清单（大模型 / 多模态 / 音乐 / 世界模型）

> 从 0 开始系统学习大模型、多模态、音乐检索/理解/生成、世界模型。
> 所有论文均已从 arXiv 下载为本地 PDF（见各主题 `PDF/` 目录），按学习顺序编号。
> 勾选框用于跟踪阅读进度：已读 → `[x]`。

---

## 目录

1. [学习路径总览](#学习路径总览)
2. [阶段 0 · 总览与综述](#阶段-0-总览与综述)
3. [阶段 1 · 大模型 (LLM)](#阶段-1-大模型-llm)
4. [阶段 2 · 多模态 (Multimodal)](#阶段-2-多模态-multimodal)
5. [阶段 3 · 音乐检索与理解](#阶段-3-音乐检索与理解)
6. [阶段 4 · 音乐生成](#阶段-4-音乐生成)
7. [阶段 5 · 世界模型 (World Models)](#阶段-5-世界模型-world-models)
8. [阶段 6 · 强化学习基础 (RL)](#阶段-6-强化学习基础-rl)
9. [进阶/补充阅读](#进阶补充阅读)

---

## 学习路径总览

建议的完整学习顺序（按依赖关系，而非时间线）：

```
总览综述 ──► 大模型 → 多模态 → 音乐(检索/理解) → 音乐生成
    │
    └────► 世界模型（与大模型、多模态、生成互相交融）
```

**建议节奏（3~4 个月主线）：**

| 周期 | 主题 | 目标 |
|------|------|------|
| 第 1~2 周 | 总览 + Transformer 起点 | 建立全局地图，理解自注意力/Transformer |
| 第 3~6 周 | 大模型 (LLM) | 掌握预训练、缩放定律、对齐(RLHF/DPO)、推理效率 |
| 第 6~9 周 | 多模态 (Multimodal) | 掌握对齐(CLIP)、指令微调(LLaVA)、图像生成 |
| 第 9~11 周 | 音乐检索与理解 | 掌握音频表示、自监督、对比学习（对音乐） |
| 第 11~13 周 | 音乐生成 | 掌握自回归/扩散/音频编解码的音乐生成 |
| 第 13~15 周 | 世界模型 | 掌握 latent dynamics、Dreamer/MuZero 家族、视频世界模型 |

> 关键依赖：音乐理解需先懂 `CLIP` 与 `wav2vec` 等；世界模型需先懂 `Transformer` 与 `RL` 基础（见阶段 6）。每篇后面用 ▶ 标注了「前置」。

---

## 阶段 0 · 总览与综述

> **目的**：先建立全局地图，再看具体论文。建议第 0 步通读 2~3 篇综述，其余按需查阅。

| ✓ | # | 论文 | 中文 | 用途 | 链接 |
|---|----|------|------|------|---|
| [ ] | 00 | Transformer: Attention Is All You Need | 一切的起点（也放在大模型里精读） | 全局地基 | [PDF](00_总览综述/PDF/00_Transformer_AttentionIsAllYouNeed.pdf) · [1706.03762](https://arxiv.org/abs/1706.03762) |
| [ ] | 01 | A Survey of Large Language Models | 大语言模型综述 | LLM 总览 | [PDF](00_总览综述/PDF/01_A_SummaryOfLLMs.pdf) · [2303.18223](https://arxiv.org/abs/2303.18223) |
| [ ] | 02 | The Dawn of LMMs | 视觉指令微调、多模态综述 | 多模态总览 | [PDF](00_总览综述/PDF/02_The_Dawn_of_LMMs.pdf) · [2309.17421](https://arxiv.org/abs/2309.17421) |
| [ ] | 03 | A Survey on Multimodal Large Language Models | 多模态 LLM 综述 | 多模态总览 | [PDF](00_总览综述/PDF/03_Survey_Multimodal_LLMs.pdf) · [2306.13549](https://arxiv.org/abs/2306.13549) |
| [ ] | 04 | A Comprehensive Survey on Deep Music Generation | 深度音乐生成综述 | 音乐生成总览 | [PDF](00_总览综述/PDF/04_Survey_Deep_Music_Generation.pdf) · [2011.06801](https://arxiv.org/abs/2011.06801) |
| [ ] | 05 | Understanding World or Predicting Future? A Survey of World Models | 世界模型综述 | 世界模型总览 | [PDF](00_总览综述/PDF/05_Survey_World_Models.pdf) · [2411.14499](https://arxiv.org/abs/2411.14499) |
| [ ] | 06 | Is Sora a World Simulator? | Sora / 通用世界模型综述 | 世界模型总览 | [PDF](00_总览综述/PDF/06_Is_Sora_a_World_Simulator.pdf) · [2405.03520](https://arxiv.org/abs/2405.03520) |

**✦ 必读**：00（Transformer）、01。其余综述按需翻阅。

---

## 阶段 1 · 大模型 (LLM)

> **学习主线**：Transformer → 自监督预训练 (BERT/GPT) → 缩放定律 → 规模化(LLM) → 对齐(RLHF/DPO) → 推理效率与结构演进。
> ▶️ 前置：请先精读 `00_总览` 中的 Transformer。

### 第一组 · 奠基 (必读)
| [ ]完成 | # | 文件 | 一句话要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 00 | Transformer: Attention Is All You Need | 自注意力 + 位置编码，一切大模型的地基 | [1706.03762](https://arxiv.org/abs/1706.03762) | [PDF](01_大模型/PDF/00_Transformer_AttentionIsAllYouNeed.pdf) |
| [ ] | 01 | BERT | 双向编码器 + Masked LM 预训练，开创 Pre-train+Fine-tune | [1810.04805](https://arxiv.org/abs/1810.04805) | [PDF](01_大模型/PDF/01_BERT.pdf) |
| [ ] | 02 | GPT-2 | 单向自回归生成式预训练 + 零样本迁移 | 无 arXiv（OpenAI 官网发布）· [PDF](01_大模型/PDF/02_GPT2_LanguageModelsUnsupervisedMultitask.pdf) |
| [ ] | 03 | GPT-3: Few-Shot Learners | in-context learning，规模化涌现 few-shot 能力 | [2005.14165](https://arxiv.org/abs/2005.14165) | [PDF](01_大模型/PDF/03_GPT3_FewShot.pdf) |
| [ ] | 04 | Scaling Laws for Neural LMs (Kaplan) | 模型/数据/算力的幂律缩放关系 | [2001.08361](https://arxiv.org/abs/2001.08361) | [PDF](01_大模型/PDF/04_ScalingLaws_Kaplan.pdf) |
| [ ] | 05 | Chinchilla: Training Compute-Optimal LLMs | 数据应随模型等比例缩放（70B→1.4T） | [2203.15556](https://arxiv.org/abs/2203.15556) | [PDF](01_大模型/PDF/05_Chinchilla_TrainingComputeOptimal.pdf) |
| [ ] | 06 | InstructGPT: RLHF | 基于人类反馈强化学习，让模型对齐意图 | [2203.02155](https://arxiv.org/abs/2203.02155) | [PDF](01_大模型/PDF/06_InstructGPT_RLHF.pdf) |
| [ ] | 07 | Constitutional AI | 用 AI 反馈替代人类反馈 (RLAIF) | [2212.08073](https://arxiv.org/abs/2212.08073) | [PDF](01_大模型/PDF/07_ConstitutionalAI.pdf) |
| [ ] | 08 | RoPE (Rotary Position Embedding) | 旋转位置编码，LLaMA/GPT 系标配 | [2104.09864](https://arxiv.org/abs/2104.09864) | [PDF](01_大模型/PDF/08_RoPE.pdf) |

### 第二组 · 高效训练与推理 (必读)
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 11 | LoRA: Low-Rank Adaptation | 参数高效微调 (PEFT) | [2106.09685](https://arxiv.org/abs/2106.09685) | [PDF](01_大模型/PDF/11_LoRA.pdf) |
| [ ] | 12 | QLoRA | 4-bit 量化 + LoRA，单卡微调 65B | [2305.14314](https://arxiv.org/abs/2305.14314) | [PDF](01_大模型/PDF/12_QLoRA.pdf) |
| [ ] | 13 | FlashAttention | IO 感知的精确注意力，加速+省显存 | [2205.14135](https://arxiv.org/abs/2205.14135) | [PDF](01_大模型/PDF/13_FlashAttention.pdf) |
| [ ] | 14 | PagedAttention / vLLM | KV-Cache 分页管理，推理吞吐提升 | [2309.06180](https://arxiv.org/abs/2309.06180) | [PDF](01_大模型/PDF/14_PagedAttention.pdf) |
| [ ] | 28 | Speculative Decoding | 猜测-验证加速自回归解码 | [2211.17192](https://arxiv.org/abs/2211.17192) | [PDF](01_大模型/PDF/28_SpeculativeDecoding.pdf) |

### 第三组 · 开源模型里程碑 (必读)
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 09 | LLaMA | 开源复现 GPT-3 级能力的基座模型 | [2302.13971](https://arxiv.org/abs/2302.13971) | [PDF](01_大模型/PDF/09_LLaMA_OpenEfficientFoundation.pdf) |
| [ ] | 10 | LLaMA 2 | 商用许可 + 对齐 (RLHF) | [2307.09288](https://arxiv.org/abs/2307.09288) | [PDF](01_大模型/PDF/10_LLaMA2.pdf) |
| [ ] | 15 | Mistral 7B | 质量/推理效率权衡，Sliding Window | [2310.06825](https://arxiv.org/abs/2310.06825) | [PDF](01_大模型/PDF/15_Mistral7B.pdf) |
| [ ] | 16 | Mixtral of Experts | 稀疏 MoE 提升容量/效率 | [2401.04088](https://arxiv.org/abs/2401.04088) | [PDF](01_大模型/PDF/16_Mixtral_MoE.pdf) |
| [ ] | 17 | GShard | 首个大规模稀疏 MoE (Transformer) | [2006.16668](https://arxiv.org/abs/2006.16668) | [PDF](01_大模型/PDF/17_GShard_MoE.pdf) |
| [ ] | 18 | Switch Transformer | MoE 简化 Routing，稳定高效 | [2101.03961](https://arxiv.org/abs/2101.03961) | [PDF](01_大模型/PDF/18_SwitchTransformer.pdf) |
| [ ] | 19 | Mamba (SSM) | 状态空间模型，线性复杂度序列建模 | [2312.00752](https://arxiv.org/abs/2312.00752) | [PDF](01_大模型/PDF/19_Mamba_SSM.pdf) |
| [ ] | 20 | GPT-4 Technical Report | 工程化大规模多模态 LLM | [2303.08774](https://arxiv.org/abs/2303.08774) | [PDF](01_大模型/PDF/20_GPT4_TechnicalReport.pdf) |

### 第四组 · 对齐与能力增强 (必读)
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 21 | Chain-of-Thought | 思维链提示，涌现推理能力 | [2201.11903](https://arxiv.org/abs/2201.11903) | [PDF](01_大模型/PDF/21_ChainOfThought.pdf) |
| [ ] | 22 | ReAct | 推理 + 行动结合，Agent 基础 | [2210.03629](https://arxiv.org/abs/2210.03629) | [PDF](01_大模型/PDF/22_ReAct.pdf) |
| [ ] | 23 | Toolformer | 学会调用外部工具/API | [2302.04761](https://arxiv.org/abs/2302.04761) | [PDF](01_大模型/PDF/23_Toolformer.pdf) |
| [ ] | 24 | Self-Instruct | 自生成指令数据微调 | [2212.10560](https://arxiv.org/abs/2212.10560) | [PDF](01_大模型/PDF/24_SelfInstruct.pdf) |
| [ ] | 25 | LIMA | 极少高质量数据也能对齐 | [2305.11206](https://arxiv.org/abs/2305.11206) | [PDF](01_大模型/PDF/25_LIMA.pdf) |
| [ ] | 26 | DPO | 无需 reward model 的直接偏好优化 | [2305.18290](https://arxiv.org/abs/2305.18290) | [PDF](01_大模型/PDF/26_DPO_DirectPreferenceOptimization.pdf) |
| [ ] | 27 | Retrieval-Augmented Generation (RAG) | 外挂知识检索 | [2005.11401](https://arxiv.org/abs/2005.11401) | [PDF](01_大模型/PDF/27_RAG_RetrievalAugmentedGeneration.pdf) |
| [ ] | 29 | Emergent Abilities of Large Models | 规模化沙现能力 | [2206.07682](https://arxiv.org/abs/2206.07682) | [PDF](01_大模型/PDF/29_EmergentAbilities.pdf) |
| [ ] | 30 | Let's Verify Step by Step (PRM) | 过程奖励提升数学推理 | [2305.20050](https://arxiv.org/abs/2305.20050) | [PDF](01_大模型/PDF/30_LetsVerifyStepByStep_PRM.pdf) |
| [ ] | 31 | DeepSeek-R1 | 强化学习(RL)驱动的推理 LLM | [2501.12948](https://arxiv.org/abs/2501.12948) | [PDF](01_大模型/PDF/31_DeepSeekR1.pdf) |

### 第五组 · 现代结构补缺（2024 补充）
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 32 | GQA: Grouped-Query Attention | 分组查询注意力，LLaMA2/3 与多数现代模型标配 | [2305.13245](https://arxiv.org/abs/2305.13245) | [PDF](01_大模型/PDF/32_GQA.pdf) |
| [ ] | 33 | MQA: Fast Transformer Decoding | 多头共享 KV，GQA 前身 | [1911.02150](https://arxiv.org/abs/1911.02150) | [PDF](01_大模型/PDF/33_MultiQueryAttention.pdf) |
| [ ] | 34 | DeepSeekMath (GRPO) | R1 的算法前置：组相对策略优化 | [2402.03300](https://arxiv.org/abs/2402.03300) | [PDF](01_大模型/PDF/34_DeepSeekMath_GRPO.pdf) |
| [ ] | 35 | DeepSeek-V2 | MLA 注意力，R1 架构底座 | [2405.04434](https://arxiv.org/abs/2405.04434) | [PDF](01_大模型/PDF/35_DeepSeekV2.pdf) |
| [ ] | 36 | DeepSeek-V3 | FP8/MoE 工程，R1 训练底座 | [2412.19437](https://arxiv.org/abs/2412.19437) | [PDF](01_大模型/PDF/36_DeepSeekV3.pdf) |
| [ ] | 37 | Lost in the Middle | 长上下文位置偏置，RAG 必读 | [2307.03172](https://arxiv.org/abs/2307.03172) | [PDF](01_大模型/PDF/37_LostInTheMiddle.pdf) |
| [ ] | 38 | YaRN | RoPE 长上下文外推 | [2309.00071](https://arxiv.org/abs/2309.00071) | [PDF](01_大模型/PDF/38_YaRN.pdf) |

---

## 阶段 2 · 多模态 (Multimodal)

> **主线**：图像表示(VAE/Transformer) → 图文对齐(CLIP) → 视觉理解基座(ViT) → 注入 LLM(LLaVA) → 图像/视频生成(DALLE·Video Diffusion·LDM)。
> ▶️ 前置建议：先完成大模型阶段 1（尤其 Transformer、LoRA、指令微调）。

### 第一组 · 表示与对齐 (必读)
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 00 | ViT: Vision Transformer | 把 Transformer 用到图像 | [2010.11929](https://arxiv.org/abs/2010.11929) | [PDF](02_多模态/PDF/00_ViT_VisionTransformer.pdf) |
| [ ] | 01 | VQVAE | 离散潜在编码图像/音频 | [1711.00937](https://arxiv.org/abs/1711.00937) | [PDF](02_多模态/PDF/01_VQVAE.pdf) |
| [ ] | 02 | VQGAN | VQVAE + GAN 感知重建，现代生成的地基 | [2012.09841](https://arxiv.org/abs/2012.09841) | [PDF](02_多模态/PDF/02_VQGAN.pdf) |
| [ ] | 03 | CLIP | 图文对比学习对齐，多模态基石 | [2103.00020](https://arxiv.org/abs/2103.00020) | [PDF](02_多模态/PDF/03_CLIP.pdf) |
| [ ] | 04 | ALIGN / CoCa | 弱监督/双编码对比对齐 | [2102.05918](https://arxiv.org/abs/2102.05918) · [2205.01917](https://arxiv.org/abs/2205.01917) | [PDF](02_多模态/PDF/04_ALIGN.pdf) · [PDF](02_多模态/PDF/05_CoCa.pdf) |
| [ ] | 18 | ImageBind | 六模态统一绑定(图像/音频/文本/3D) | [2305.05665](https://arxiv.org/abs/2305.05665) | [PDF](02_多模态/PDF/18_ImageBind.pdf) |

### 第二组 · LLM 视觉理解 (必读)
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 06 | BLIP | 图文理解与生成双任务 + 过滤噪声 Caption | [2201.12086](https://arxiv.org/abs/2201.12086) | [PDF](02_多模态/PDF/06_BLIP.pdf) |
| [ ] | 07 | BLIP-2 | Q-Former 连接冻结视觉编码器 + LLM | [2301.12597](https://arxiv.org/abs/2301.12597) | [PDF](02_多模态/PDF/07_BLIP2.pdf) |
| [ ] | 08 | Flamingo | 冻结 LLM + 视觉 token，注入视觉 | [2204.14198](https://arxiv.org/abs/2204.14198) | [PDF](02_多模态/PDF/08_Flamingo.pdf) |
| [ ] | 09 | KOSMOS-1 | 多模态作为基础模型的架构 | [2302.14045](https://arxiv.org/abs/2302.14045) | [PDF](02_多模态/PDF/09_KOSMOS1.pdf) |
| [ ] | 10 | LLaVA | 视觉指令微调，轻量入门口 | [2304.08485](https://arxiv.org/abs/2304.08485) | [PDF](02_多模态/PDF/10_LLaVA.pdf) |
| [ ] | 11 | MiniGPT-4 | 对齐视觉与 LLM 能力的快速验证 | [2304.10592](https://arxiv.org/abs/2304.10592) | [PDF](02_多模态/PDF/11_MiniGPT4.pdf) |
| [ ] | 12 | InstructBLIP | 指令式图文理解 | [2305.06500](https://arxiv.org/abs/2305.06500) | [PDF](02_多模态/PDF/12_InstructBLIP.pdf) |
| [ ] | 13 | LLaVA-1.5 | 视觉指令微调的上限参考 | [2310.03744](https://arxiv.org/abs/2310.03744) | [PDF](02_多模态/PDF/13_LLaVA1_5.pdf) |
| [ ] | 14 | Qwen-VL | 开源强视觉语言基座，中文友好 | [2308.12966](https://arxiv.org/abs/2308.12966) | [PDF](02_多模态/PDF/14_QwenVL.pdf) |
| [ ] | 15 | CogVLM | 视觉语言基础模型 | [2311.03079](https://arxiv.org/abs/2311.03079) | [PDF](02_多模态/PDF/15_CogVLM.pdf) |
| [ ] | 16 | InternVL | 对标 GPT-4V 的开源多模态模型 | [2312.14238](https://arxiv.org/abs/2312.14238) | [PDF](02_多模态/PDF/16_InternVL.pdf) |
| [ ] | 25 | GPT-4o System Card | 原生统一多模态模型（报告） | [2410.21276](https://arxiv.org/abs/2410.21276) | [PDF](02_多模态/PDF/25_GPT4o_SystemCard.pdf) |

### 第三组 · 感知基础与生成 (选读强相关)
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 17 | SAM: Segment Anything | 通用分割基础模型 | [2304.02643](https://arxiv.org/abs/2304.02643) | [PDF](02_多模态/PDF/17_SAM_SegmentAnything.pdf) |
| [ ] | 19 | Whisper | 大规模语音识别 | [2212.04356](https://arxiv.org/abs/2212.04356) | [PDF](02_多模态/PDF/19_Whisper.pdf) |
| [ ] | 20 | GLIDE | 文本引导扩散图像生成 | [2112.10741](https://arxiv.org/abs/2112.10741) | [PDF](02_多模态/PDF/20_GLIDE.pdf) |
| [ ] | 21 | DALL·E 2 | CLIP 引导扩散 | [2204.06125](https://arxiv.org/abs/2204.06125) | [PDF](02_多模态/PDF/21_DALLE2.pdf) |
| [ ] | 22 | Imagen | 纯文本到图像扩散 | [2205.11487](https://arxiv.org/abs/2205.11487) | [PDF](02_多模态/PDF/22_Imagen.pdf) |
| [ ] | 23 | Latent Diffusion (Stable Diffusion) | 潜在空间扩散，开源 | [2112.10752](https://arxiv.org/abs/2112.10752) | [PDF](02_多模态/PDF/23_LDM_StableDiffusion.pdf) |
| [ ] | 24 | Video Diffusion Models | 视频生成扩散 | [2204.03458](https://arxiv.org/abs/2204.03458) | [PDF](02_多模态/PDF/24_VideoDiffusionModels.pdf) |

> ✦ 若主攻**音乐**，第 19 (Whisper) 与 23 (LDM) 高度相关，建议读。

### 第四组 · 生成模型理论地基（补充）
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 26 | VAE (Auto-Encoding Variational Bayes) | VAE 原论文：ELBO/重参数化，所有潜在空间方法源头 | [1312.6114](https://arxiv.org/abs/1312.6114) | [PDF](02_多模态/PDF/26_VAE.pdf) |
| [ ] | 27 | DDPM | 扩散模型开山：加噪/去噪/损失推导 | [2006.11239](https://arxiv.org/abs/2006.11239) | [PDF](02_多模态/PDF/27_DDPM.pdf) |
| [ ] | 28 | DDIM | 确定性采样加速 | [2010.02502](https://arxiv.org/abs/2010.02502) | [PDF](02_多模态/PDF/28_DDIM.pdf) |
| [ ] | 29 | Score-Based SDE | score 视角统一扩散 | [2011.13456](https://arxiv.org/abs/2011.13456) | [PDF](02_多模态/PDF/29_ScoreBased_SDE.pdf) |
| [ ] | 30 | Flow Matching | 现役主流生成范式 (SD3/Flux) | [2210.02747](https://arxiv.org/abs/2210.02747) | [PDF](02_多模态/PDF/30_FlowMatching.pdf) |

### 第五组 · 3D 与可控生成（补充）
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 31 | NeRF | 神经辐射场：3D 表示与视图合成开山 | [2003.08934](https://arxiv.org/abs/2003.08934) | [PDF](02_多模态/PDF/31_NeRF.pdf) |
| [ ] | 32 | 3D Gaussian Splatting | 现役 3D 表示标准 | [2308.04079](https://arxiv.org/abs/2308.04079) | [PDF](02_多模态/PDF/32_3DGaussianSplatting.pdf) |
| [ ] | 33 | ControlNet | 结构/姿态/深度条件控制 | [2302.05543](https://arxiv.org/abs/2302.05543) | [PDF](02_多模态/PDF/33_ControlNet.pdf) |
| [ ] | 34 | InstructPix2Pix | 指令式图像编辑 | [2211.09800](https://arxiv.org/abs/2211.09800) | [PDF](02_多模态/PDF/34_InstructPix2Pix.pdf) |
| [ ] | 35 | DreamBooth | 主体定制生成 | [2208.12242](https://arxiv.org/abs/2208.12242) | [PDF](02_多模态/PDF/35_DreamBooth.pdf) |
| [ ] | 36 | SigLIP | CLIP 现代替代 (sigmoid 损失) | [2303.15343](https://arxiv.org/abs/2303.15343) | [PDF](02_多模态/PDF/36_SigLIP.pdf) |

### 第六组 · 视频理解（补充, 世界模型输入侧）
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 37 | TimeSformer | 视频时空注意力开山 | [2102.05095](https://arxiv.org/abs/2102.05095) | [PDF](02_多模态/PDF/37_TimeSformer.pdf) |
| [ ] | 38 | VideoMAE | 视频 MAE 自监督预训练 | [2203.12602](https://arxiv.org/abs/2203.12602) | [PDF](02_多模态/PDF/38_VideoMAE.pdf) |
| [ ] | 39 | VideoMAE V2 | 双掩码缩放，视频预训练标杆 | [2303.16727](https://arxiv.org/abs/2303.16727) | [PDF](02_多模态/PDF/39_VideoMAEV2.pdf) |
| [ ] | 40 | InternVideo | 生成+判别统一视频基础模型 | [2212.03191](https://arxiv.org/abs/2212.03191) | [PDF](02_多模态/PDF/40_InternVideo.pdf) |
| [ ] | 41 | Video-LLaVA | 图/视频统一表征的视频 VLM | [2311.10122](https://arxiv.org/abs/2311.10122) | [PDF](02_多模态/PDF/41_VideoLLaVA.pdf) |
| [ ] | 42 | LLaVA-Video | 视频指令微调参考线 | [2410.02713](https://arxiv.org/abs/2410.02713) | [PDF](02_多模态/PDF/42_LLaVAVideo.pdf) |

### 第七组 · 新一代开源 VLM（补充, 2024H2）
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 43 | Qwen2-VL | 任意分辨率感知开源 VLM | [2409.12191](https://arxiv.org/abs/2409.12191) | [PDF](02_多模态/PDF/43_Qwen2VL.pdf) |
| [ ] | 44 | Cambrian-1 | 视觉为中心多模态系统研究 | [2406.16860](https://arxiv.org/abs/2406.16860) | [PDF](02_多模态/PDF/44_Cambrian1.pdf) |
| [ ] | 45 | xGen-MM (BLIP-3) | BLIP 家族第三代 | [2408.08872](https://arxiv.org/abs/2408.08872) | [PDF](02_多模态/PDF/45_xGenMM_BLIP3.pdf) |
| [ ] | 46 | Aria | 原生多模态 MoE | [2410.05993](https://arxiv.org/abs/2410.05993) | [PDF](02_多模态/PDF/46_Aria.pdf) |
| [ ] | 47 | AnyGPT | 离散序列统一任意模态 | [2402.12226](https://arxiv.org/abs/2402.12226) | [PDF](02_多模态/PDF/47_AnyGPT.pdf) |
| [ ] | 48 | Unified-IO 2 | 视觉/语言/音频/动作统一 | [2312.17172](https://arxiv.org/abs/2312.17172) | [PDF](02_多模态/PDF/48_UnifiedIO2.pdf) |
| [ ] | 49 | RA-CM3 | 检索增强多模态生成 | [2211.12561](https://arxiv.org/abs/2211.12561) | [PDF](02_多模态/PDF/49_RACM3.pdf) |

### 第八组 · 视频生成前沿（补充, 世界模型融合区）
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 50 | VideoPoet | LLM 式 (token 自回归) 视频生成 | [2312.14125](https://arxiv.org/abs/2312.14125) | [PDF](02_多模态/PDF/50_VideoPoet.pdf) |
| [ ] | 51 | CogVideoX | 开源文生视频 DiT 代表 | [2408.06072](https://arxiv.org/abs/2408.06072) | [PDF](02_多模态/PDF/51_CogVideoX.pdf) |
| [ ] | 52 | Stable Video Diffusion | 潜在视频扩散规模化 | [2311.15127](https://arxiv.org/abs/2311.15127) | [PDF](02_多模态/PDF/52_StableVideoDiffusion.pdf) |
| [ ] | 53 | AnimateDiff | 文生图模型免训练动画化 | [2307.04725](https://arxiv.org/abs/2307.04725) | [PDF](02_多模态/PDF/53_AnimateDiff.pdf) |
| [ ] | 54 | HunyuanVideo | 腾讯开源视频生成大模型 | [2412.03603](https://arxiv.org/abs/2412.03603) | [PDF](02_多模态/PDF/54_HunyuanVideo.pdf) |
| [ ] | 55 | Wan | 阿里开源视频生成大模型 | [2503.20314](https://arxiv.org/abs/2503.20314) | [PDF](02_多模态/PDF/55_Wan.pdf) |
| [ ] | 56 | Movie Gen | Meta 媒体基础模型 (视频+音频+编辑) | [2410.13720](https://arxiv.org/abs/2410.13720) | [PDF](02_多模态/PDF/56_MovieGen.pdf) |

---

## 阶段 3 · 音乐检索与理解

> **核心问题**：如何从音频中提取可检索、可理解的表征？→ 机器学习(CRNN) → 自监督(wav2vec) → 对比学习(CLAP) → 音乐专用f 大模型(MusicBERT/MERT)。
> ▶️ 前置：阶段 1 (Transformer) + 阶段 2 的 CLIP/ViT 逻辑。

### 第一组 · 经典机器学习基础 (必读打底)
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 00 | Music Auto-Tagging with Deep CNNs (Cho等) | 音乐打标签(Spectrogram→CNN)基线 | [1606.00298](https://arxiv.org/abs/1606.00298) | [PDF](03_音乐检索理解/PDF/00_MusicAutoTagging_DeepCNN.pdf) |
| [ ] | 01 | Convolutional RNN for Music Classification | RNN 时序建模 | [1609.04243](https://arxiv.org/abs/1609.04243) | [PDF](03_音乐检索理解/PDF/01_CRNN_MusicClassification.pdf) |
| [ ] | 02 | Attention CNN for Music Tagging | 注意力应用 | [1906.04972](https://arxiv.org/abs/1906.04972) | [PDF](03_音乐检索理解/PDF/02_AttentionCNN_MusicTagging.pdf) |
| [ ] | 03 | Transfer Learning for Music | 用大数据集预训练迁移到小数据集 | [1703.09179](https://arxiv.org/abs/1703.09179) | [PDF](03_音乐检索理解/PDF/03_TransferLearning_Music.pdf) |

### 第二组 · 数据与自监督表征 (必读)
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 04 | FMA (Free Music Archive) | 大规模免费音乐数据集（检索/理解用） | [1612.01840](https://arxiv.org/abs/1612.01840) | [PDF](03_音乐检索理解/PDF/04_FMA_Dataset.pdf) |
| [ ] | 05 | AudioSet | 大规模音频事件数据集 | 无 arXiv（ICASSP 2017）· [PDF](03_音乐检索理解/PDF/05_AudioSet_Dataset.pdf) |
| [ ] | 06 | MAESTRO | 对齐 MIDI 与音频的钢琴数据集 | [1810.12247](https://arxiv.org/abs/1810.12247) | [PDF](03_音乐检索理解/PDF/06_MAESTRO_Dataset.pdf) |
| [ ] | 07 | wav2vec 2.0 | 音频自监督对比学习，通用音频表征 | [2006.11477](https://arxiv.org/abs/2006.11477) | [PDF](03_音乐检索理解/PDF/07_wav2vec2.pdf) |
| [ ] | 08 | OpenL3 | 声音嵌入 (用于检索) | 无 arXiv（ICASSP 2019）· [PDF](03_音乐检索理解/PDF/08_OpenL3.pdf) |

### 第三组 · 音乐理解 Transformer (必读)
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 09 | AST (Audio Spectrogram Transformer) | 音频谱Transformer，无需预训练 | [2104.01778](https://arxiv.org/abs/2104.01778) | [PDF](03_音乐检索理解/PDF/09_AST_AudioSpectrogramTransformer.pdf) |
| [ ] | 10 | HTSAT | 分层音频Transformer，SOTA的通用词表示 | [2202.00874](https://arxiv.org/abs/2202.00874) | [PDF](03_音乐检索理解/PDF/10_HTSAT.pdf) |
| [ ] | 11 | MusicBERT | 符号音乐理解 (MIR-旋律) | [2106.05630](https://arxiv.org/abs/2106.05630) | [PDF](03_音乐检索理解/PDF/11_MusicBERT.pdf) |
| [ ] | 12 | Music2Vec | 音乐表征向量，理解/检索 | [2212.02508](https://arxiv.org/abs/2212.02508) | [PDF](03_音乐检索理解/PDF/12_Music2Vec.pdf) |
| [ ] | 13 | CLAP | 音频-文本对比学习，音乐检索核心 | [2211.06687](https://arxiv.org/abs/2211.06687) | [PDF](03_音乐检索理解/PDF/13_CLAP.pdf) |
| [ ] | 14 | MERT | 大规模通用音乐理解模型(多任务) | [2306.00107](https://arxiv.org/abs/2306.00107) | [PDF](03_音乐检索理解/PDF/14_MERT.pdf) |
| [ ] | 15 | CLaMP | 文本与乐谱对比预训练 | [2304.11029](https://arxiv.org/abs/2304.11029) | [PDF](03_音乐检索理解/PDF/15_CLaMP.pdf) |
| [ ] | 16 | Wav2CLIP | 音频跨模态检索/零样本 | [2110.11499](https://arxiv.org/abs/2110.11499) | [PDF](03_音乐检索理解/PDF/16_Wav2CLIP.pdf) |

> ✦ 检索方向：重点精读 **CLAP、MERT、CLaMP、Wav2CLIP** 以及对比学习。理解方向：**MERT、MusicBERT、AST**。

---

## 阶段 4 · 音乐生成

> **主线**：自回归(WaveNet/Jukebox) → 符号(Token/MusicTransformer) → 潜在扩散(AudioLM/MusicLM) → 文本条件(MusicGen/Mustango)。
> ▶️ 前置：阶段 3 (音频表征)、阶段 2 的 VAE/Diffusion, 阶段 1 的 Transformer。

### 第一组 · 基础生成模型 (必读)
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 00 | NSynth | 神经合成器，音色生成 | [1704.01279](https://arxiv.org/abs/1704.01279) | [PDF](04_音乐生成/PDF/00_NSynth.pdf) |
| [ ] | 01 | WaveNet | 自回归原始波形生成 (音频生成的基石) | [1609.03499](https://arxiv.org/abs/1609.03499) | [PDF](04_音乐生成/PDF/01_WaveNet.pdf) |
| [ ] | 02 | MusicVAE | 分层潜在空间解偶音乐生成 | [1803.05428](https://arxiv.org/abs/1803.05428) | [PDF](04_音乐生成/PDF/02_MusicVAE.pdf) |
| [ ] | 03 | MuseGAN | GAN 生成多轨音乐 | [1709.06298](https://arxiv.org/abs/1709.06298) | [PDF](04_音乐生成/PDF/03_MuseGAN.pdf) |
| [ ] | 04 | Music Transformer | 自注意力生成数千 token 音乐 | [1809.04281](https://arxiv.org/abs/1809.04281) | [PDF](04_音乐生成/PDF/04_MusicTransformer.pdf) |
| [ ] | 05 | Jukebox | 大模型自回归生成带歌词歌曲 | [2005.00341](https://arxiv.org/abs/2005.00341) | [PDF](04_音乐生成/PDF/05_Jukebox.pdf) |
| [ ] | 06 | DiffWave | 扩散模型做音频生成(替代WaveNet) | [2009.09761](https://arxiv.org/abs/2009.09761) | [PDF](04_音乐生成/PDF/06_DiffWave.pdf) |

### 第二组 · 文本→音乐/音频 (必读)
| # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|
| [ ] | 07 | AudioLM | 离散音频 token 条件生成 | [2209.03143](https://arxiv.org/abs/2209.03143) | [PDF](04_音乐生成/PDF/07_AudioLM.pdf) |
| [ ] | 08 | AudioGen | 通用音频生成(条件编程) | [2209.15352](https://arxiv.org/abs/2209.15352) | [PDF](04_音乐生成/PDF/08_AudioGen.pdf) |
| [ ] | 09 | MusicLM | 文本→音乐，开创性作品 | [2301.11325](https://arxiv.org/abs/2301.11325) | [PDF](04_音乐生成/PDF/09_MusicLM.pdf) |
| [ ] | 10 | Make-An-Audio | 潜在扩散 + CLAP 跨模态音乐生成 | [2301.12661](https://arxiv.org/abs/2301.12661) | [PDF](04_音乐生成/PDF/10_MakeAnAudio.pdf) |
| [ ] | 11 | AudioLDM | 潜在空间扩散音频生成 | [2301.12503](https://arxiv.org/abs/2301.12503) | [PDF](04_音乐生成/PDF/11_AudioLDM.pdf) |
| [ ] | 12 | AudioLDM 2 | 更稳，支持混合条件 | [2308.05734](https://arxiv.org/abs/2308.05734) | [PDF](04_音乐生成/PDF/12_AudioLDM2.pdf) |
| [ ] | 13 | MusicGen | 单模型文本→音乐，开源实用 | [2306.05284](https://arxiv.org/abs/2306.05284) | [PDF](04_音乐生成/PDF/13_MusicGen.pdf) |
| [ ] | 14 | Mustango | 音乐任务适配的文本到音乐 | [2311.08355](https://arxiv.org/abs/2311.08355) | [PDF](04_音乐生成/PDF/14_Mustango.pdf) |
| [ ] | 15 | VampNet | 掩码谱码法生成音乐 | [2307.04686](https://arxiv.org/abs/2307.04686) | [PDF](04_音乐生成/PDF/15_VampNet.pdf) |
| [ ] | 16 | Symphony | 大语言模型文本到音乐 | ⚠️ 未找到 arXiv 版本（待确认） | [PDF](04_音乐生成/PDF/16_Symphony_Text2Music.pdf) |
| [ ] | 17 | Stable Audio Open | 开源生成音频模型 | [2407.14358](https://arxiv.org/abs/2407.14358) | [PDF](04_音乐生成/PDF/17_StableAudioOpen.pdf) |

> ✦ 优先精读：**WaveNet、MusicGen、MusicLM、AudioLM、AudioLDM**。选读：Jukebox(经典)、Symphony(最新)。

### 第三组 · 音频编解码器（补充, 生成前置）
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 18 | SoundStream | 端到端神经音频编解码器，AudioLM 声学 tokenizer | [2107.03312](https://arxiv.org/abs/2107.03312) | [PDF](04_音乐生成/PDF/18_SoundStream.pdf) |
| [ ] | 19 | EnCodec | 业界标准音频 tokenizer，AudioGen/MusicGen 用它 | [2210.13438](https://arxiv.org/abs/2210.13438) | [PDF](04_音乐生成/PDF/19_EnCodec.pdf) |

---

## 阶段 5 · 世界模型 (World Models)

> **核心思想**：让模型在其内部「想象」环境并预测动作的效果，从而在想象中规划/学习。
> 两大分支：**基于学习 (Dreamer/MuZero)** 与 **生成式世界模拟器 (Genie/Sora/视频生成)**。
> ▶️ 前置：阶段 1 (Transformer/Mamba) + 阶段 2 (VAE/Video Diffusion) 基础。

### 第一组 · 经典世界模型 (必读)
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 00 | World Models (Ha & Schmidhuber) | VAE+RNN 压缩时空，在想象中规划 | [1803.10122](https://arxiv.org/abs/1803.10122) | [PDF](05_世界模型/PDF/00_WorldModels_HaSchmidhuber.pdf) |
| [ ] | 02 | PlaNet | 潜在变量状态下学习世界 + planning | [1811.04551](https://arxiv.org/abs/1811.04551) | [PDF](05_世界模型/PDF/02_PlaNet.pdf) |
| [ ] | 03 | MuZero | 不依赖规划器的树搜索世界模型 | [1911.08265](https://arxiv.org/abs/1911.08265) | [PDF](05_世界模型/PDF/03_MuZero.pdf) |
| [ ] | 04 | Dreamer | 潜在(state)+ latent 想象中学习 | [1912.01603](https://arxiv.org/abs/1912.01603) | [PDF](05_世界模型/PDF/04_Dreamer.pdf) |
| [ ] | 06 | DreamerV2 | 离散式认知+想象中强化 | [2010.02193](https://arxiv.org/abs/2010.02193) | [PDF](05_世界模型/PDF/06_DreamerV2.pdf) |
| [ ] | 08 | DreamerV3 | 通用稳健世界模型(60+环境) | [2301.04104](https://arxiv.org/abs/2301.04104) | [PDF](05_世界模型/PDF/08_DreamerV3.pdf) |
| [ ] | 05 | Plan2Explore | 不确定性驱动探索世界模型 | [2005.05960](https://arxiv.org/abs/2005.05960) | [PDF](05_世界模型/PDF/05_Plan2Explore.pdf) |
| [ ] | 10 | IRIS | Transformer 图像 token 想象 | [1911.05321](https://arxiv.org/abs/1911.05321) | [PDF](05_世界模型/PDF/10_IRIS.pdf) |
| [ ] | 09 | L2WM | Transformer 世界模型可扩展 | ⚠️ 未找到 arXiv 版本（待确认） | [PDF](05_世界模型/PDF/09_L2WM_LearningLatentWorldModels.pdf) |

### 第二组 · 理解/预测 表征 (必读)
| # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|
| [ ] | 11 | I-JEPA | Yann LeCun 联合嵌入预测架构 | [2301.08243](https://arxiv.org/abs/2301.08243) | [PDF](05_世界模型/PDF/11_IJEPA_JEPA.pdf) |
| [ ] | 15 | V-JEPA | 视频级 JEPA 表征 | [2404.08471](https://arxiv.org/abs/2404.08471) | [PDF](05_世界模型/PDF/15_VJEPA.pdf) |
| [ ] | 01 | SVG | 随机视频生成 (预测未来帧) | [1802.07687](https://arxiv.org/abs/1802.07687) | [PDF](05_世界模型/PDF/01_SVG_StochasticVideoGeneration.pdf) |
| [ ] | 07 | VideoGPT | 自回归视频世界模型(混合) | [2104.10157](https://arxiv.org/abs/2104.10157) | [PDF](05_世界模型/PDF/07_VideoGPT.pdf) |
| [ ] | 14 | DiffWorldModel | 扩散世界模型 | [2402.03570](https://arxiv.org/abs/2402.03570) | [PDF](05_世界模型/PDF/14_DiffusionWorldModel.pdf) |

### 第三组 · 生成式/交互世界模拟 (新前沿，必读)
| # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|
| [ ] | 12 | UniSim | 可交互真实世界仿真器(动作条件) | [2310.06114](https://arxiv.org/abs/2310.06114) | [PDF](05_世界模型/PDF/12_UniSim_InteractiveRealWorldSimulators.pdf) |
| [ ] | 13 | Genie | 从单张图/提示生成可玩交互游戏世界 | [2402.15391](https://arxiv.org/abs/2402.15391) | [PDF](05_世界模型/PDF/13_Genie_GenerativeInteractiveEnvironments.pdf) |
| [ ] | 16 | Generative World Explorer | LLM规划式的世界探索 | [2411.11844](https://arxiv.org/abs/2411.11844) | [PDF](05_世界模型/PDF/16_GenerativeWorldExplorer.pdf) |
| [ ] | 17 | DreamTrainer | 无需奖励的世界模型训练 | ⚠️ 未找到 arXiv 版本（待确认） | [PDF](05_世界模型/PDF/17_DreamTrainer.pdf) |
| [ ] | 18 | Cosmos World Foundation Model | NVIDIA 物理世界生成平台 | [2501.03575](https://arxiv.org/abs/2501.03575) | [PDF](05_世界模型/PDF/18_Cosmos_WorldFoundationModel.pdf) |

> ✦ 优先学习顺序：**World Models → Dreamer → DreamerV3** 建立思想；再 **Genie → V-JEPA → UniSim** 接入新前沿。综述 `00_总览/05` 作为地图。

### 第四组 · 2024–2025 前沿（补充）
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 19 | GameNGen | 扩散模型=实时游戏引擎 (DOOM 30fps) | [2408.14837](https://arxiv.org/abs/2408.14837) | [PDF](05_世界模型/PDF/19_GameNGen.pdf) |
| [ ] | 20 | DIAMOND | 扩散世界模型 Atari SOTA (NeurIPS 2024) | [2405.12399](https://arxiv.org/abs/2405.12399) | [PDF](05_世界模型/PDF/20_DIAMOND_DiffusionWorldModel.pdf) |
| [ ] | 21 | TD-MPC2 | model-based RL 新 SOTA，MPC 规划 | [2310.16828](https://arxiv.org/abs/2310.16828) | [PDF](05_世界模型/PDF/21_TDMPC2.pdf) |
| [ ] | 22 | RT-2 (VLA) | 视觉语言知识→机器人控制 | [2307.15818](https://arxiv.org/abs/2307.15818) | [PDF](05_世界模型/PDF/22_RT2_VLA.pdf) |
| [ ] | 23 | WonderWorld | 单图→可交互 3D 世界 | [2406.09394](https://arxiv.org/abs/2406.09394) | [PDF](05_世界模型/PDF/23_WonderWorld.pdf) |
| [ ] | 24 | V-JEPA 2 | 自监督视频：理解/预测/规划统一 | [2506.09985](https://arxiv.org/abs/2506.09985) | [PDF](05_世界模型/PDF/24_VJEPA2.pdf) |
| [ ] | 25 | A-JEPA | 音频 JEPA，JEPA 家族补音频腿 | [2311.15830](https://arxiv.org/abs/2311.15830) | [PDF](05_世界模型/PDF/25_AJEPA.pdf) |

---

## 阶段 6 · 强化学习基础 (RL)

> **目的**：世界模型的直接前置。Dreamer/MuZero/DIAMOND/TD-MPC2 的 policy/value/actor-critic 术语都源自这里。
> ▶️ 建议在世界模型经典组之前读；理解 RLHF/R1 对齐也需要 PPO/GRPO。

### 第一组 · 入门到综述 (必读)
| [ ] | # | 文件 | 要点 | arXiv | 本地 PDF |
|---|---|---|---|---|---|
| [ ] | 00 | DQN: Playing Atari with Deep RL | 价值学习入门，Atari 基准与世界模型同源 | [1312.5602](https://arxiv.org/abs/1312.5602) | [PDF](06_强化学习/PDF/00_DQN_PlayingAtari.pdf) |
| [ ] | 01 | PPO | 策略梯度标准算法（RLHF/R1 对齐思想源头） | [1707.06347](https://arxiv.org/abs/1707.06347) | [PDF](06_强化学习/PDF/01_PPO.pdf) |
| [ ] | 02 | Model-Based RL: A Survey | 世界模型方法完整坐标系 | [2006.16712](https://arxiv.org/abs/2006.16712) | [PDF](06_强化学习/PDF/02_Survey_ModelBasedRL.pdf) |

> ✦ 读完后回到阶段 5：Dreamer → DreamerV3 → TD-MPC2 → DIAMOND。

---

## 建议补充阅读

- **音乐检索专用数据集标注**：FMA (文件 3-04)、证集。
- **世界模型前沿**：Genie 2 / Sora（非 arXiv, PDF）→ 用 `webfetch` 抓官方页转换 markdown。
- **2024–2025 补充批次**：已并入 50 篇（01-32~38、02-26~56、04-18~19、05-19~25、06-00~02），缺口分析与理由见 [补充阅读建议_世界模型与多模态.md](补充阅读建议_世界模型与多模态.md)。

---

## 使用说明

1. **下载脚本**：`dl_parallel.sh manifest.txt <并行数>`（并行下载，可断点续传）；`manifest.txt` 为论文清单（`arxiv_id|本地路径`），可自行增删。
2. **清单**：本文件即 master 阅读清单，勾选 `[ ]` → `[x]` 记录进度。
3. **目录结构**：`XX_主题/PDF/编号_论文名.pdf`，编号即为推荐阅读顺序。
4. **阅读建议**：先精读每个阶段「✦ 必读」标项，再看其余；音频/视觉/序列生成模型结构高度相通，可跨阶段对比理解。
5. **重下/补下**：`bash dl_parallel.sh manifest.txt 8` 即可补齐缺失论文。
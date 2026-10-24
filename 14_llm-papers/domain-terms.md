---
type: word-bank
title: "论文领域术语（Part 2）"
tags: [library/word-bank, skill/reading, status/learning]
created: 2026-10-24
---

# 论文领域术语（Part 2）

> 同一批术语会在几十篇 abstract 中反复出现。先背术语，再逐篇阅读。

## B1 生成模型与扩散（Diffusion / VAE / Flow）

| 术语 | 中文 | 一句话解释 |
|---|---|---|
| diffusion model | 扩散模型 | 先逐步加噪、再学习逐步去噪来生成数据的模型 |
| denoising | 去噪 | 从带噪样本中恢复干净数据 |
| forward process | 前向过程 | 向数据逐步加噪声的过程 |
| reverse process | 反向过程 | 从噪声逐步还原数据（生成）的过程 |
| latent space | 潜在空间 | 压缩后的低维特征空间，数据的高层表示所在 |
| latent variable | 潜在变量 | 不可直接观测的中间变量 |
| variational | 变分的 | VAE（变分自编码器）的核心词，近似推断 |
| encoder / decoder | 编码器 / 解码器 | 压缩到潜在空间 / 从潜在空间还原 |
| sampling | 采样 | 从概率分布中抽取样本 |
| score function | 得分函数 | 对数概率密度的梯度，扩散模型去噪的依据 |
| flow matching | 流匹配 | 一种生成建模范式（SD3/Flux 采用） |
| stochastic | 随机的 | 含随机性的过程 |
| deterministic | 确定性的 | 无随机性，给定输入输出固定 |
| quantization | 量化 | 把连续值映射到离散值 |
| codebook | 码本 | 离散 token 的查找表（VQVAE） |
| reconstruction | 重建 | 从潜在表示恢复原数据 |
| tokenizer | 分词器 / 离散化器 | 把连续信号切成离散 token 的模块 |
| autoregressive | 自回归的 | 逐个 token 预测下一个来生成 |
| temperature | 温度 | 控制生成随机性的采样参数 |
| perplexity | 困惑度 | 语言模型"意外程度"指标，越低越好 |
| fidelity | 保真度 | 生成结果与真实数据的相似程度 |

## B2 大模型与 Transformer

| 术语 | 中文 | 一句话解释 |
|---|---|---|
| attention | 注意力 | 让模型聚焦输入中重要部分的机制 |
| self-attention | 自注意力 | 序列内部元素互相关注的注意力 |
| query / key / value (QKV) | 查询 / 键 / 值 | 注意力的三个投影分量 |
| positional encoding | 位置编码 | 给 token 注入位置信息 |
| pre-training | 预训练 | 在大规模数据上先训练通用能力 |
| fine-tuning | 微调 | 在预训练基础上用任务数据继续训练 |
| instruction tuning | 指令微调 | 用"指令-回答"数据训练，让模型听话 |
| alignment | 对齐 | 让模型行为符合人类意图 |
| RLHF | 基于人类反馈的强化学习 | 用人类偏好训练奖励模型再优化策略 |
| in-context learning | 上下文学习 | 不更新参数，靠提示示例完成任务 |
| few-shot / zero-shot | 少样本 / 零样本 | 给几个示例 / 不给示例直接做 |
| scaling law | 缩放定律 | 模型/数据/算力与性能的幂律关系 |
| mixture of experts (MoE) | 专家混合 | 路由到部分专家计算，省算力扩容量 |
| sparse | 稀疏的 | 每次只激活一部分 |
| distillation | 蒸馏 | 用大模型训练小模型 |
| hallucination | 幻觉 | 生成看似合理但错误的内容 |
| reasoning | 推理 | 多步逻辑思考能力 |
| chain-of-thought | 思维链 | 让模型先想后答的提示方式 |
| context window | 上下文窗口 | 模型一次能处理的 token 数 |
| long-context | 长上下文 | 处理很长的输入 |
| emergent ability | 涌现能力 | 规模增大后突然出现的能力 |
| KV cache | 键值缓存 | 推理时缓存注意力 K/V 以加速 |
| speculative decoding | 投机解码 | 小模型猜、大模型验，加速生成 |
| retrieval-augmented generation (RAG) | 检索增强生成 | 先检索资料再生成回答 |

## B3 多模态（Multimodal）

| 术语 | 中文 | 一句话解释 |
|---|---|---|
| modality | 模态 | 数据形式：文本 / 图像 / 音频 / 视频 |
| multimodal | 多模态的 | 同时处理多种数据形式 |
| vision-language model (VLM) | 视觉语言模型 | 同时理解图像与文本的模型 |
| contrastive learning | 对比学习 | 拉近匹配样本对、推远不匹配对 |
| alignment | 对齐 | 把不同模态映射到同一表示空间 |
| caption | 描述；字幕 | image captioning 图像描述 |
| grounding | 锚定；接地 | 把语言词锚定到图像具体区域 |
| patch | 图像块 | ViT 把图像切成的小方块 |
| resolution | 分辨率 | 图像的精细程度 |
| segment | 分割 | 把图像划分成区域/物体 |
| detection | 检测 | 找出物体位置与类别 |
| embedding | 嵌入向量 | 对象（词/图/音）的向量表示 |
| retrieval | 检索 | 从库中找出相关内容 |
| cross-modal | 跨模态的 | 不同模态之间（如文字找图） |
| temporal | 时间维度的 | 与时间先后有关（视频） |
| frame | 帧 | 视频的一幅画面 |
| radiance field | 辐射场 | NeRF 用其建模 3D 场景 |
| gaussian splatting | 高斯泼溅 | 用高斯椭球渲染 3D 场景的方法 |
| view synthesis | 视角合成 | 从新角度渲染场景 |
| zero-shot transfer | 零样本迁移 | 未训练过的类别/模态直接用 |
| instruction following | 指令跟随 | 按自然语言指令执行 |
| visual encoder | 视觉编码器 | 提取图像特征的网络 |

## B4 音乐与音频（Music & Audio）

| 术语 | 中文 | 一句话解释 |
|---|---|---|
| audio | 音频 | 声音信号 |
| waveform | 波形 | 原始的声音振幅随时间变化 |
| spectrogram | 频谱图 | 时间-频率二维图，音频的"图像" |
| melody | 旋律 | 一段可哼唱的连贯音高序列 |
| harmony | 和声 | 同时发声的音的组合 |
| timbre | 音色 | 区分同一音高不同乐器的特质 |
| tempo | 速度 | 节拍快慢 |
| pitch | 音高 | 声音的高低 |
| rhythm | 节奏 | 时值长短的组合 |
| polyphonic | 复调的 | 多个音同时发声（如钢琴和弦） |
| synthesis | 合成 | 从参数/条件生成声音 |
| vocoder | 声码器 | 生成波形信号的网络（WaveNet 系） |
| accompaniment | 伴奏 | 主旋律之外的陪衬声部 |
| lyrics | 歌词 | 歌曲文字部分 |
| tagging | 打标签 | 给音乐标注风格/情感等属性 |
| audio codec | 音频编解码器 | 压缩/还原音频（EnCodec） |
| semantic tokens | 语义 token | 高层声音语义的离散表示 |
| acoustic tokens | 声学 token | 底层声学细节的离散表示 |
| text-to-music | 文本到音乐 | 用文字生成音乐 |
| music retrieval | 音乐检索 | 按文字/旋律找音乐 |
| recommendation | 推荐 | 根据偏好推音乐 |
| auto-tagging | 自动标注 | 自动给音乐打标签 |

## B5 世界模型与强化学习（World Models & RL）

| 术语 | 中文 | 一句话解释 |
|---|---|---|
| world model | 世界模型 | 学习环境变化规律、可预测未来的模型 |
| agent | 智能体 | 与环境交互并决策的主体 |
| environment | 环境 | 智能体所处、可交互的世界 |
| state | 状态 | 环境在某时刻的情况描述 |
| action | 动作 | 智能体采取的行为 |
| reward | 奖励 | 环境给智能体的反馈信号 |
| policy | 策略 | 状态到动作的映射（怎么决策） |
| value function | 价值函数 | 状态（或动作）的未来回报估计 |
| reinforcement learning | 强化学习 | 靠奖励信号试错学习决策 |
| model-based RL | 基于模型的强化学习 | 先学世界模型，再在其上规划/学习 |
| model-free RL | 免模型强化学习 | 不学环境模型，直接学策略 |
| planning | 规划 | 用模型推演未来，选择好动作 |
| dynamics | 动力学；环境动态 | 状态如何随时间/动作变化 |
| imagination | 想象 | 在学到的世界模型中推演未来 |
| rollout | 推演；展开 | 从某状态向前模拟一串动作 |
| latent state | 潜在状态 | 世界模型的压缩隐藏状态 |
| self-supervised | 自监督的 | 用数据自身构造监督信号 |
| JEPA | 联合嵌入预测架构 | 在表示空间做预测（LeCun 路线） |
| exploration | 探索 | 尝试未知以获取信息 |
| exploitation | 利用 | 使用已学到的策略 |
| episode | 回合，幕 | 从开始到结束的一次交互 |
| discount factor | 折扣因子 | 未来奖励的折算系数 |
| actor-critic | 演员-评论家 | 策略网络+价值网络配合的算法 |
| simulator | 模拟器 | 模拟环境的系统 |
| interactive | 可交互的 | 能实时响应用户操作的 |
| embodied | 具身的 | 有身体/实体的（机器人） |
| hindsight | 事后回顾 | 用失败经验反向学习 |

## B6 评估与基准（Evaluation）

| 术语 | 中文 | 一句话解释 |
|---|---|---|
| benchmark | 基准测试集 | 统一评测模型的标准任务集 |
| baseline | 基线 | 用于对比的最基本方法 |
| metric | 指标 | 衡量性能的数值标准 |
| accuracy | 准确率 | 预测正确的比例 |
| precision | 精确率 | 预测为正中真为正的比例 |
| recall | 召回率 | 真为正中被找出的比例 |
| F1 score | F1 分数 | 精确率与召回率的调和平均 |
| human evaluation | 人工评测 | 请人打分 |
| subjective | 主观的 | 依赖人的感受（如音质） |
| objective | 客观的 | 可用数值计算的 |
| ablation study | 消融实验 | 去掉某个组件看其贡献 |
| case study | 案例研究 | 具体例子分析 |

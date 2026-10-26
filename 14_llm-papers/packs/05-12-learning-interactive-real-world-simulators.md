---
type: paper-pack
paper_id: "05-12"
stage: 5
title: "Learning Interactive Real-World Simulators"
pdf: "/home/user/llm-papers/05_世界模型/PDF/12_UniSim_InteractiveRealWorldSimulators.pdf"
tags: [topic/paper, skill/reading, status/learning]
---

# 05-12 Learning Interactive Real-World Simulators

**中文标题**：学习交互式真实世界模拟器（UniSim）

**一句话概括**：探索用生成建模学习真实世界交互的通用模拟器 UniSim：精心编排图像、机器人、导航等多维数据，模拟高层指令与低层控制的视觉结果，纯仿真训练的策略可零样本部署到真实世界。

## 读前 2 分钟

| 词 | 音标 | 中文 | 级别 |
|---|---|---|---|
| milestone | /mˈaɪlstəʊn/ | 里程碑；标志性进展 | A |
| simulate | /sˈɪmjʊlˌeɪt/ | 模拟 | A |
| orchestration | /ˌɔːkɪstɹˈeɪʃən/ | 编排、协调组织 | B |
| embodied agents | /ɛmbˈɒdid ˈeɪdʒənts/ | 具身智能体；有物理身体并能行动的智能体 | B |
| zero shot | /zˈiəɹəʊ ʃˈɒt/ | 零样本；不经微调直接部署 | B |
| revolutionized | /ɹˌɛvəlˈuːʃənˌaɪzd/ | 彻底改变、变革 | B |
| densely sampled | /dˈɛnsli sˈampəld/ | 密集采样的；动作数据采样频率高 | B |
| deploy | /dɪplˈɔɪ/ | 部署；投入实际使用 | B |
| abundant | /ɐbˈʌndənt/ | 丰富的、大量的 | B |
| vision-language policies | /vˈɪʒənlˈaŋɡwɪdʒ pˈɒlɪsiz/ | 视觉-语言策略；理解语言指令并行动 | B |
| interactive agents | /ˌɪntəɹˈaktɪv ˈeɪdʒənts/ | 交互式智能体 | B |
| static | /stˈatɪk/ | 静态的；不动的 | B |

### 原句（保留完整句子）

- **milestone** — “Perhaps the next milestone for generative models is to simulate realistic experience in response to actions taken by humans, robots, and other interactive agents.”
- **simulate** — “Perhaps the next milestone for generative models is to simulate realistic experience in response to actions taken by humans, robots, and other interactive agents.”
- **orchestration** — “With careful orchestration of diverse datasets, each providing a different aspect of the overall experience, we can simulate the visual outcome of both high-level instructions such as “open the drawer” and low-level controls such as “move by ∆x, ∆y” from otherwise static scenes and objects.”
- **embodied agents** — “Applications of a real-world simulator range from controllable content creation in games and movies, to training embodied agents purely in simulation that can be directly deployed in the real world.”
- **zero shot** — “We use the simulator to train both high-level vision-language policies and low-level reinforcement learning policies, each of which can be deployed in the real world in zero shot after training purely in simulation.”
- **revolutionized** — “have revolutionized how text, image, and video content”
- **densely sampled** — “We first make the important observation that natural datasets available for learning a real-world simulator are often rich along different dimensions (e.g., abundant objects in image data, densely sampled actions in robotics data, and diverse movements in navigation data).”
- **deploy** — “We then directly deploy the RL policy trained in the simulator onto the real robot in zero-shot, and observe successful task executions as shown in Figure 8 (bottom row).”
- **abundant** — “We first make the important observation that natural datasets available for learning a real-world simulator are often rich along different dimensions (e.g., abundant objects in image data, densely sampled actions in robotics data, and diverse movements in navigation data).”
- **vision-language policies** — “We use the simulator to train both high-level vision-language policies and low-level reinforcement learning policies, each of which can be deployed in the real world in zero shot after training purely in simulation.”
- **interactive agents** — “Perhaps the next milestone for generative models is to simulate realistic experience in response to actions taken by humans, robots, and other interactive agents.”
- **static** — “With careful orchestration of diverse datasets, each providing a different aspect of the overall experience, we can simulate the visual outcome of both high-level instructions such as “open the drawer” and low-level controls such as “move by ∆x, ∆y” from otherwise static scenes and objects.”

## Abstract（自动提取）

> TITLE: Learning Interactive Real-World Simulators ABSTRACT: Generative models trained on internet data have revolutionized how text, image, and video content can be created. Perhaps the next milestone for generative models is to simulate realistic experience in response to actions taken by humans, robots, and other interactive agents. Applications of a real-world simulator range from controllable content creation in games and movies, to training embodied agents purely in simulation that can be directly deployed in the real world. We explore the possibility of learning a universal simulator (UniSim) of real-world interaction through generative modeling. We first make the important observation that natural datasets available for learning a real-world simulator are often rich along different dimensions (e.g., abundant objects in image data, densely sampled actions in robotics data, and diverse movements in navigation data). With careful orchestration of diverse datasets, each providing a different aspect of the overall experience, we can simulate the visual outcome of both high-level instructions such as "open the drawer" and low-level controls from otherwise static scenes and objects. We use the simulator to train both high-level vision-language policies and low-level reinforcement learning policies, each of which can be deployed in the real world in zero shot after training pure

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

PDF：`/home/user/llm-papers/05_世界模型/PDF/12_UniSim_InteractiveRealWorldSimulators.pdf`

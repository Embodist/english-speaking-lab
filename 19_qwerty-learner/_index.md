---
type: hub
title: "qwerty-learner 词库"
tags: [hub, library/word-bank, skill/speaking, status/learning]
created: 2026-11-05
updated: 2026-11-05
---

# qwerty-learner 词库

> 把本仓库的句子、短语、前后缀例词和全部单词导出成 [qwerty-learner](https://github.com/RealKai42/qwerty-learner) 可用的 JSON 词库，用**打字**的方式练拼写和反应。共 **20 个词库 / 22,145 张卡**。

> [!info] 格式
> qwerty-learner 的词库格式是 `[{"name": "...", "trans": ["..."]}]`；`name` 是你要打的内容，支持单词、短语和整句。

## 词库

| ID | 词库 | 卡数 | 适合 |
|---|---|---:|---|
| `english-lab-pronouns` | 代词 54 | 54 | 人称、物主、反身、指示、疑问、不定代词，附例句 |
| `english-lab-work-phrases` | 工作高频短语 90 | 90 | 先练开会、PR、报进度 |
| `english-lab-new-words` | 新词 3,463 | 3,463 | 排除常见功能词后的内容词，主力词库 |
| `english-lab-all-words` | 全部单词 3,625 | 3,625 | 内容里出现的每一个单词，完整版 |
| `english-lab-affix-examples` | 前后缀例词（去重） | 1,708 | 练单词拼写 + 词缀 |
| `english-lab-basic-phrases` | 基础短语 1125 | 1,125 | 固定搭配和介词短语 |
| `english-lab-affixes` | 前后缀 335 | 335 | 记词缀方向 |
| `english-lab-sentences-01`～`10` | 1200 句场景口语 | 每类 120 | 整句打字与节奏 |
| `english-lab-fsi-patterns` | FSI 句型 126 | 126 | 替换/应答句型 |
| `english-lab-paper-10k` | 论文 10k 词 | 10,127 | 论文阅读词表，AI/ML 词汇 |
| `english-lab-cpp-292` | C++ 术语 292 | 292 | C++ Core Guidelines 术语 |

单词卡释义来自本地 `ECDICT` 词典，带音标；22 个未收录词（缩写、所有格、复合词）已用本地规则补齐，**0 缺失**。

完整清单和计数见 `manifest.json`。

## 本地已装好

qwerty-learner 已克隆到 `~/english/qwerty-learner`，依赖已安装，20 个词库已注册。

```bash
cd ~/english/english-speaking-lab
bash scripts/start-qwerty.sh
```

打开 `http://127.0.0.1:5173/gallery`，选择分类 **English Lab**。如果 5173 被占用，可以 `PORT=5174 bash scripts/start-qwerty.sh`。

## 新机器从零安装

qwerty-learner 的在线站点不支持直接上传自定义词库，需要把 JSON 放进本地克隆的 `public/dicts/`，并在 `src/resources/dictionary.ts` 注册。

```bash
git clone https://github.com/RealKai42/qwerty-learner.git ~/english/qwerty-learner
python ~/english/english-speaking-lab/scripts/install_qwerty_dicts.py ~/english/qwerty-learner
cd ~/english/qwerty-learner
HUSKY=0 corepack yarn install --registry https://registry.npmmirror.com
bash ~/english/english-speaking-lab/scripts/start-qwerty.sh
```

> [!note] 重复执行
> 安装脚本可以重复运行；它会覆盖词库文件并替换 `englishLabDicts` 代码块，不会重复注册。

## 推荐顺序

1. **代词 54**：先过一遍，确保 he/him/his 这类形式不混。
2. **工作高频短语 90**：每天 20 张，先建立工作表达。
3. **新词 3,463**：每天 20 张，主力词库；不会的词回 ECDICT 释义。
4. **前后缀例词 1,708**：每天 20 张，配合 [[17_word-roots/_index|前后缀 335]]。
5. **基础短语 1,125**：每天 20 张，练固定搭配。
6. **1200 句场景口语**：每天 1 个分类的 20 句，打字较慢，重在整句节奏。
7. **FSI 句型 126**：配合 [[18_fsi-drills/_index|FSI 训练]] 做替换。
8. **论文 10k / C++ 292**：按需练，不要在基础阶段硬刷。

## 生成词库

```bash
cd ~/english/english-speaking-lab
python scripts/build_qwerty_dicts.py          # 重新生成 19_qwerty-learner/dicts/*.json
python scripts/install_qwerty_dicts.py /path/to/qwerty-learner
```

数据来源：

- [[08_sentence-library/1200-sentences/_index|1200 句场景口语]]
- [[12_word-phrase-bank/11-basic-phrases/_index|基础短语 1125]]
- [[17_word-roots/_index|前后缀 335]]
- [[18_fsi-drills/_index|FSI 句型]]

## 相关

- [[08_sentence-library/_index|句子库]]
- [[12_word-phrase-bank/_index|词与短语库]]
- [[LEARNING-PATH|学习路径]]
- [[scripts/README|脚本说明]]

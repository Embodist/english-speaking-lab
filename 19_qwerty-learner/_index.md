---
type: hub
title: "qwerty-learner 词库"
tags: [hub, library/word-bank, skill/speaking, status/learning]
created: 2026-11-05
updated: 2026-11-05
---

# qwerty-learner 词库

> 把本仓库的句子、短语、前后缀例词导出成 [qwerty-learner](https://github.com/RealKai42/qwerty-learner) 可用的 JSON 词库，用**打字**的方式练拼写和反应。共 **15 个词库 / 4,584 张卡**。

> [!info] 格式
> qwerty-learner 的词库格式是 `[{"name": "...", "trans": ["..."]}]`；`name` 是你要打的内容，支持单词、短语和整句。

## 词库

| ID | 词库 | 卡数 | 适合 |
|---|---|---:|---|
| `english-lab-work-phrases` | 工作高频短语 90 | 90 | 先练开会、PR、报进度 |
| `english-lab-affix-examples` | 前后缀例词（去重） | 1,708 | 练单词拼写 + 词缀 |
| `english-lab-basic-phrases` | 基础短语 1125 | 1,125 | 固定搭配和介词短语 |
| `english-lab-affixes` | 前后缀 335 | 335 | 记词缀方向 |
| `english-lab-sentences-01`～`10` | 1200 句场景口语 | 每类 120 | 整句打字与节奏 |
| `english-lab-fsi-patterns` | FSI 句型 126 | 126 | 替换/应答句型 |

完整清单和计数见 `manifest.json`。

## 安装到本地 qwerty-learner

qwerty-learner 的在线站点不支持直接上传自定义词库，需要把 JSON 放进本地克隆的 `public/dicts/`，并在 `src/resources/dictionary.ts` 注册。仓库里带了自动安装脚本。

```bash
# 1. 克隆 qwerty-learner（Windows 或 WSL 都可以）
git clone https://github.com/RealKai42/qwerty-learner.git ~/qwerty-learner
cd ~/qwerty-learner

# 2. 复制词库并注册
python ~/english/english-speaking-lab/scripts/install_qwerty_dicts.py .

# 3. 安装依赖并启动
yarn install
yarn dev
```

打开 `http://localhost:5173`，在词库分类里选择 **English Lab**。

> [!note] 重复执行
> 安装脚本可以重复运行；它会覆盖词库文件并替换 `englishLabDicts` 代码块，不会重复注册。

## 推荐顺序

1. **工作高频短语 90**：每天 20 张，先建立工作表达。
2. **前后缀例词 1,708**：每天 20 张，配合 [[17_word-roots/_index|前后缀 335]]。
3. **基础短语 1,125**：每天 20 张，练固定搭配。
4. **1200 句场景口语**：每天 1 个分类的 20 句，打字较慢，重在整句节奏。
5. **FSI 句型 126**：配合 [[18_fsi-drills/_index|FSI 训练]] 做替换。

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

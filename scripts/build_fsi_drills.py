#!/usr/bin/env python3
"""Generate Obsidian notes for the FSI-style drill module from drills.tsv.

Data:   18_fsi-drills/data/drills.tsv
Output: 18_fsi-drills/*.md
"""
import csv
from collections import OrderedDict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "18_fsi-drills"
DATA = OUT / "data" / "drills.tsv"
TODAY = date.today().isoformat()


def load():
    with DATA.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def esc(value):
    return value.replace("|", "\\|")


def frontmatter(title, note_type="guide"):
    return (
        "---\n"
        f"type: {note_type}\n"
        f'title: "{title}"\n'
        "tags: [skill/speaking, status/learning]\n"
        f"created: {TODAY}\n"
        f"updated: {TODAY}\n"
        "---\n\n"
    )


def group(rows, key):
    result = OrderedDict()
    for row in rows:
        result.setdefault(row[key], []).append(row)
    return result


def write_index(rows):
    counts = {}
    for row in rows:
        counts[row["set"]] = counts.get(row["set"], 0) + 1
    text = [
        frontmatter("FSI 式口语训练", "hub"),
        "# FSI 式口语训练\n\n",
        "> FSI（美国外交学院）语言课程的核心不是讲语法，而是**大量结构化重复**："
        "听懂 → 模仿 → 替换 → 变换 → 应答 → 对话。每天 20 分钟，练到不假思索。\n\n",
        "> [!info] 说明\n"
        "> 这是按 FSI 音频语言法（audio-lingual method）设计的训练材料，不是 FSI 原版教材的复制。\n\n",
        "## 四类训练\n\n",
        f"| 类型 | 练什么 | 数量 | 入口 |\n|---|---|---:|---|\n"
        f"| 替换 Drill | 固定句型，只换一个槽位 | {counts.get('sub', 0)} | [[18_fsi-drills/01-substitution|替换训练]] |\n"
        f"| 变换 Drill | 陈述↔疑问、主动↔被动、直接↔礼貌 | {counts.get('trans', 0)} | [[18_fsi-drills/02-transformation|变换训练]] |\n"
        f"| 应答 Drill | 听到问题，立刻给完整回答 | {counts.get('resp', 0)} | [[18_fsi-drills/03-response|应答训练]] |\n"
        f"| 情景 Drill | 站会、事故、评审、面试 | {counts.get('situation', 0)} | [[18_fsi-drills/04-situations|情景训练]] |\n\n",
        "## 每天 20 分钟\n\n"
        "| 时间 | 动作 |\n|---|---|\n"
        "| 3 min | 听/读 1 个模型句，跟读 3 遍，模仿重音和停顿 |\n"
        "| 7 min | 替换训练：同一句型换 6 个槽位，每个说 2 遍 |\n"
        "| 5 min | 变换或应答训练：看提示，先答，再看模型答案 |\n"
        "| 5 min | 录一段 60 秒自由应答，回听并只改 1 个问题 |\n\n",
        "## 五条规则\n\n",
        "1. **先出声，再看答案**：卡住 3 秒就看答案，然后立刻重说一遍。\n",
        "2. **一次只练一个结构**：替换时不要改句型，变换时不要加内容。\n",
        "3. **速度优先于完美**：先做到 2 秒内开口，再修发音。\n",
        "4. **录音才算练过**：每天至少留 1 段 60 秒录音。\n",
        "5. **练完立刻用**：当天至少把 1 句写进 Slack、PR 或日志。\n\n",
        "## 命令\n\n",
        "```bash\ncd ~/english/english-speaking-lab\n",
        "python scripts/study.py fsi --set sub --n 10\n",
        "python scripts/study.py fsi --set trans --n 10\n",
        "python scripts/study.py fsi --set resp --n 10\n",
        "python scripts/study.py fsi --set situation --n 8\n",
        "python scripts/study.py fsi --set resp --n 5 --tts   # 生成模型答案音频\n",
        "```\n\n",
        "## 相关\n\n",
        "- [[18_fsi-drills/learning-plan|4 周训练计划]]\n",
        "- [[12_word-phrase-bank/11-phrase-1200/_index|1200 短语训练库]]\n",
        "- [[12_word-phrase-bank/10-fixed-chunks|固定搭配与高频句型]]\n",
        "- [[02_daily-work/_index|日常工作表达]]\n",
        "- [[06_interview/_index|面试训练]]\n",
    ]
    (OUT / "_index.md").write_text("".join(text), encoding="utf-8")


def write_substitution(rows):
    sub = [r for r in rows if r["set"] == "sub"]
    frames = group(sub, "hint")
    lines = [
        frontmatter("替换训练", "guide"),
        "# 替换训练\n\n",
        "> 句型不变，只换槽位。每个槽位说 2 遍：第 1 遍看提示，第 2 遍不看。\n\n",
    ]
    for frame, items in frames.items():
        lines.append(f"## {esc(frame)}\n\n")
        lines.append("| 槽位 | 完整句 |\n|---|---|\n")
        for row in items:
            lines.append(f"| {esc(row['prompt'])} | {esc(row['answer'])} |\n")
        lines.append("\n")
    lines += [
        "## 进阶\n\n",
        "1. 遮住右列，只看槽位说完整句。\n",
        "2. 换一个你自己的项目名词，再说一遍。\n",
        "3. 用同一句型连续说 6 句，中间不停顿。\n\n",
        "## 相关\n\n- [[18_fsi-drills/_index|FSI 训练总览]]\n",
    ]
    (OUT / "01-substitution.md").write_text("".join(lines), encoding="utf-8")


def write_transformation(rows):
    trans = [r for r in rows if r["set"] == "trans"]
    kinds = group(trans, "kind")
    lines = [
        frontmatter("变换训练", "guide"),
        "# 变换训练\n\n",
        "> 看原句，立刻说出变换后的句子。先说，再看答案。\n\n",
    ]
    for kind, items in kinds.items():
        lines.append(f"## {kind}\n\n")
        lines.append("| 原句 | 变换后 |\n|---|---|\n")
        for row in items:
            lines.append(f"| {esc(row['prompt'])} | {esc(row['answer'])} |\n")
        lines.append("\n")
    lines += [
        "## 进阶\n\n",
        "把原句换成你项目的真实句子，再做同样的变换。\n\n",
        "## 相关\n\n- [[18_fsi-drills/_index|FSI 训练总览]]\n",
    ]
    (OUT / "02-transformation.md").write_text("".join(lines), encoding="utf-8")


def write_response(rows):
    resp = [r for r in rows if r["set"] == "resp"]
    lines = [
        frontmatter("应答训练", "guide"),
        "# 应答训练\n\n",
        "> 看问题，先用**完整句**回答，再看模型答案。不要只答一个词。\n\n",
        "| # | 问题 | 模型回答 |\n|---:|---|---|\n",
    ]
    for number, row in enumerate(resp, 1):
        lines.append(f"| {number} | {esc(row['prompt'])} | {esc(row['answer'])} |\n")
    lines += [
        "\n## 进阶\n\n",
        "1. 同一问题准备两个版本：一个 1 句，一个 3 句。\n",
        "2. 把问题里的项目换成你自己的，再说一遍。\n",
        "3. 录音后检查：有没有漏掉主语、时态、数字。\n\n",
        "## 相关\n\n- [[18_fsi-drills/_index|FSI 训练总览]]\n",
    ]
    (OUT / "03-response.md").write_text("".join(lines), encoding="utf-8")


def write_situations(rows):
    situ = [r for r in rows if r["set"] == "situation"]
    kinds = group(situ, "kind")
    lines = [
        frontmatter("情景训练", "guide"),
        "# 情景训练\n\n",
        "> 每个情景先不看答案，自己说 1–2 句，再对照模型句。\n\n",
    ]
    for kind, items in kinds.items():
        lines.append(f"## {kind}\n\n")
        lines.append("| 你要说什么 | 模型句 |\n|---|---|\n")
        for row in items:
            lines.append(f"| {esc(row['prompt'])} | {esc(row['answer'])} |\n")
        lines.append("\n")
    lines += [
        "## 进阶\n\n",
        "把四句话连成一段 60 秒独白，录音；第二天脱稿再说一遍。\n\n",
        "## 相关\n\n",
        "- [[18_fsi-drills/_index|FSI 训练总览]]\n",
        "- [[06_interview/mock-interview|模拟面试]]\n",
        "- [[02_daily-work/standup|站会]]\n",
    ]
    (OUT / "04-situations.md").write_text("".join(lines), encoding="utf-8")


def write_plan():
    lines = [
        frontmatter("FSI 4 周训练计划", "guide"),
        "# FSI 4 周训练计划\n\n",
        "> 每周主攻一种 Drill，同时每天保留 5 分钟应答。周末录音对比。\n\n",
        "| 周 | 主练 | 每天 | 周末产出 |\n|---|---|---|---|\n",
        "| 1 | 替换 | 1 个句型 × 6 槽位 + 5 个应答 | 2 分钟工作汇报 |\n",
        "| 2 | 变换 | 10 组变换 + 5 个应答 | 1 分钟 bug 说明 |\n",
        "| 3 | 应答 | 10 个问题 + 3 个替换 | 模拟问答 5 分钟 |\n",
        "| 4 | 情景 | 2 个情景 + 10 个应答 | 3 分钟项目复述 |\n\n",
        "## 每天 20 分钟\n\n",
        "1. **3 min 模仿**：模型句跟读 3 遍，标记重音。\n",
        "2. **7 min 主练**：当周 Drill 10 条，先答后看。\n",
        "3. **5 min 应答**：5 个问题，完整句回答。\n",
        "4. **5 min 录音**：60 秒自由说，回听只改 1 个问题。\n\n",
        "## 验收\n\n",
        "| 周 | 标准 |\n|---|---|\n",
        "| 第 1 周 | 同一句型能连续替换 6 次不停顿 |\n",
        "| 第 2 周 | 看到陈述句，2 秒内说出疑问/否定/被动形式 |\n",
        "| 第 3 周 | 工作问题能用 2–3 句完整回答 |\n",
        "| 第 4 周 | 站会/事故/面试情景能脱稿说 60 秒 |\n\n",
        "## 相关\n\n- [[18_fsi-drills/_index|FSI 训练总览]]\n",
    ]
    (OUT / "learning-plan.md").write_text("".join(lines), encoding="utf-8")


def main():
    rows = load()
    write_index(rows)
    write_substitution(rows)
    write_transformation(rows)
    write_response(rows)
    write_situations(rows)
    write_plan()
    print(f"rows={len(rows)}")
    print(f"output: {OUT}")


if __name__ == "__main__":
    main()

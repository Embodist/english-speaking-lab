#!/usr/bin/env python3
"""Generate Obsidian notes for the 1,200-phrase list from the canonical TSV.

Data:  12_word-phrase-bank/11-phrase-1200/data/phrases-1200.tsv
Output: 12_word-phrase-bank/11-phrase-1200/*.md

Edit the TSV, then rerun this script. Do not hand-edit generated notes.
"""
import csv
import math
from collections import OrderedDict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "12_word-phrase-bank" / "11-phrase-1200"
DATA = OUT / "data" / "phrases-1200.tsv"
TODAY = date.today().isoformat()

FEATURED = OrderedDict([
    ("沟通与协作", [
        "deal with", "figure out", "point out", "bring up", "come up with",
        "take over", "set up", "look into", "work on", "work out",
        "carry out", "check out", "get in touch", "meet with", "report on",
        "reply to", "agree on", "focus on", "depend on", "provide with",
    ]),
    ("时间与条件", [
        "in advance", "on time", "in time", "at least", "at the same time",
        "by the way", "in case", "right away", "from time to time",
        "all the time", "at times", "no longer", "in the meantime",
        "at short notice", "before long",
    ]),
    ("因果与逻辑", [
        "because of", "due to", "thanks to", "as a result", "result in",
        "result from", "according to", "in fact", "in general", "in short",
        "instead of", "in order to", "by means of", "in return", "as well",
    ]),
    ("状态与风险", [
        "at risk", "at stake", "in charge of", "under pressure",
        "under discussion", "out of order", "out of touch",
        "be responsible for", "be aware of", "be familiar with",
        "be used to", "look forward to", "be short of", "be sure of",
        "in common",
    ]),
    ("常用动词短语", [
        "apply for", "prepare for", "ask for", "pay for", "take care",
        "make sure", "make progress", "make a decision", "take place",
        "get ready", "get rid of", "get over", "get through", "go over",
        "go through", "hold on", "keep up", "put off", "put forward",
        "set aside", "turn out", "settle for", "put up with",
        "come across", "run into",
    ]),
])


def load_rows():
    with DATA.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    for row in rows:
        row["group"] = int(row["group"])
    return rows


def esc(text):
    return text.replace("|", "\\|")


def frontmatter(title, note_type="word-bank"):
    return (
        "---\n"
        f"type: {note_type}\n"
        f'title: "{title}"\n'
        "tags: [library/word-bank, skill/speaking, status/learning]\n"
        f"created: {TODAY}\n"
        f"updated: {TODAY}\n"
        "---\n\n"
    )


def chunk_groups(rows):
    groups = sorted({row["group"] for row in rows})
    chunks = []
    idx = 0
    while idx < len(groups):
        part = groups[idx:idx + 3]
        chunks.append((part[0], part[-1]))
        idx += 3
    return chunks


def write_group_notes(rows, chunks):
    files = []
    for number, (first, last) in enumerate(chunks, 1):
        selected = [r for r in rows if first <= r["group"] <= last]
        name = f"{number:02d}-group-{first:02d}-{last:02d}.md"
        title = f"1200 短语 · Group {first:02d}–{last:02d}"
        prev_link = ""
        next_link = ""
        if number > 1:
            pf, pl = chunks[number - 2]
            prev_link = f"[[12_word-phrase-bank/11-phrase-1200/{number - 1:02d}-group-{pf:02d}-{pl:02d}|← 上一组]]"
        if number < len(chunks):
            nf, nl = chunks[number]
            next_link = f"[[12_word-phrase-bank/11-phrase-1200/{number + 1:02d}-group-{nf:02d}-{nl:02d}|下一组 →]]"

        lines = [
            frontmatter(title),
            f"# {title}\n\n",
            f"> 共 **{len(selected)}** 条。先遮住中文说意思，再遮住英文说短语；错 3 次以上的抄进随身本。\n\n",
            "| # | 短语 | 中文 |\n|---:|---|---|\n",
        ]
        for row in selected:
            lines.append(f"| {row['id']} | {esc(row['phrase'])} | {esc(row['zh'])} |\n")
        lines.append(
            "\n## 这一册怎么练\n\n"
            "1. 每轮 20 条，中→英说 3 秒；卡住就标记，不解释。\n"
            "2. 挑 3 条放进你本周真实的工作句，各说一遍并录音。\n"
            "3. 第二天只复习标记过的条目。\n\n"
            "```bash\n"
            f"python scripts/study.py phrase --group {first} --n 20\n"
            "```\n\n"
            "## 导航\n\n"
            f"{prev_link} · [[12_word-phrase-bank/11-phrase-1200/_index|1200 短语总览]] · {next_link}\n"
        )
        path = OUT / name
        path.write_text("".join(lines), encoding="utf-8")
        files.append((name, title, len(selected), first, last))
    return files


def write_index(rows, files):
    total = len(rows)
    lines = [
        frontmatter("1200 短语训练库", "hub"),
        "# 1200 短语训练库\n\n",
        f"> 原始清单 1,200 条，去重合并多义后 **{total} 条**。按 Group 1–31 分组，"
        "适合每天 20–40 条滚动训练。\n\n",
        "> [!info] 来源\n"
        "> 知乎原文需要登录，无法直接抓取；本库使用公开同款清单，处理方式见 "
        "[[09_sources/03_1200-phrases|来源与处理说明]]。\n\n",
        "> [!warning] 释义边界\n"
        "> 这是基础短语清单，个别中文释义较粗（例如 `pull down` 标成“拆毁”）。"
        "训练时以例句、词典和真实语境为准，不要只背中文。\n\n",
        "## 每天 20 分钟\n\n",
        "| 时间 | 动作 |\n|---|---|\n",
        "| 5 min | 中→英抽认 20 条：3 秒内说出短语，卡住就标记 |\n",
        "| 5 min | 英→中反向过 20 条，只求认得 |\n",
        "| 5 min | 选 3 条，各造一句你工作里真会说的话 |\n",
        "| 5 min | 录音复述这 3 句，回听并只改 1 个问题 |\n\n",
        "## 三条规则\n\n",
        "1. **先整块，后拆解**：短语当预制块说，不逐词翻译。\n",
        "2. **一次只换一个槽位**：`look into the ___` 只替换名词。\n",
        "3. **说过才算学过**：没录音、没造句的条目留在原组重练。\n\n",
        "## 分册\n\n",
        "| 分册 | 组 | 条数 | 入口 |\n|---|---:|---:|---|\n",
    ]
    for name, title, count, first, last in files:
        lines.append(
            f"| {title} | {first:02d}–{last:02d} | {count} | "
            f"[[12_word-phrase-bank/11-phrase-1200/{name[:-3]}|打开]] |\n"
        )
    lines += [
        "\n## 专项入口\n\n",
        "- [[12_word-phrase-bank/11-phrase-1200/featured-work-90|工作高频 90 条]]：时间有限先练这份。\n",
        "- [[12_word-phrase-bank/11-phrase-1200/learning-plan|30 天刷完计划]]：每天 38 条 + 复习。\n",
        "- [[12_word-phrase-bank/10-fixed-chunks|固定搭配与高频句型]]：工作场景的整句框架。\n\n",
        "## 命令\n\n",
        "```bash\ncd ~/english/english-speaking-lab\n",
        "python scripts/study.py phrase --n 20                 # 中→英\n",
        "python scripts/study.py phrase --n 20 --reverse       # 英→中\n",
        "python scripts/study.py phrase --group 3 --n 20       # 按组\n",
        "python scripts/study.py phrase --featured --n 20      # 工作高频\n",
        "python scripts/study.py phrase --n 10 --tts           # 生成参考音\n",
        "~/english/.venv/bin/python scripts/build_phrase_roots_apkg.py             # 导出 Anki\n",
        "```\n\n",
        "## 相关\n\n",
        "- [[12_word-phrase-bank/_index|词与短语库]]\n",
        "- [[18_fsi-drills/_index|FSI 口语训练]]：把短语练成条件反射。\n",
        "- [[LEARNING-PATH|学习路径]]\n",
    ]
    (OUT / "_index.md").write_text("".join(lines), encoding="utf-8")


def write_learning_plan(rows):
    per_day = math.ceil(len(rows) / 30)
    lines = [
        frontmatter("1200 短语 30 天刷完计划", "guide"),
        "# 1200 短语 30 天刷完计划\n\n",
        f"每天 **{per_day} 条**，30 天覆盖全部 {len(rows)} 条。每天 25 分钟：抽认 → 造句 → 录音 → 标记。\n\n",
        "## 每天固定动作\n\n",
        "1. 中→英抽认当天条目，3 秒说不出的画 `×`。\n",
        "2. 只复习昨天和前天画 `×` 的条目。\n",
        "3. 从当天条目选 3 条，写进真实工作句并录音。\n",
        "4. 第 3、7、14 天回看同一条目；连续 3 次说对才算掌握。\n\n",
        "## 日程\n\n",
        "| 天 | 条目 | 组 | 任务 |\n|---:|---|---|---|\n",
    ]
    for day in range(1, 31):
        batch = rows[(day - 1) * per_day: day * per_day]
        if not batch:
            continue
        groups = sorted({r["group"] for r in batch})
        group_text = f"{groups[0]:02d}" if len(groups) == 1 else f"{groups[0]:02d}–{groups[-1]:02d}"
        if day % 7 == 0:
            task = "本周错题重练 + 录 2 分钟复述"
        elif day % 5 == 0:
            task = "把 5 条短语写进 Slack / PR / 日志"
        else:
            task = "抽认 + 3 句录音"
        lines.append(
            f"| D{day} | {batch[0]['id']}–{batch[-1]['id']} | {group_text} | {task} |\n"
        )
    lines += [
        "\n## 周末验收\n\n",
        "| 周 | 能做什么 |\n|---|---|\n",
        "| 第 1 周 | 任意抽 20 条，15 条能在 3 秒内说出 |\n",
        "| 第 2 周 | 用 10 条短语说 1 分钟工作进展 |\n",
        "| 第 3 周 | 用 10 条短语讲清一个 bug 或方案 |\n",
        "| 第 4 周 | 不看提示，用 20 条短语做 3 分钟项目复述 |\n\n",
        "## 相关\n\n",
        "- [[12_word-phrase-bank/11-phrase-1200/_index|1200 短语总览]]\n",
        "- [[12_word-phrase-bank/11-phrase-1200/featured-work-90|工作高频 90 条]]\n",
        "- [[18_fsi-drills/_index|FSI 口语训练]]\n",
    ]
    (OUT / "learning-plan.md").write_text("".join(lines), encoding="utf-8")


def write_featured(rows):
    lookup = {row["phrase"].lower(): row for row in rows}
    missing = [p for items in FEATURED.values() for p in items if p not in lookup]
    if missing:
        raise SystemExit(f"featured phrases missing from data: {missing}")

    total = sum(len(items) for items in FEATURED.values())
    lines = [
        frontmatter("工作高频 90 条", "word-bank"),
        "# 工作高频 90 条\n\n",
        f"> 从 1,125 条里挑出的 **{total}** 条，覆盖开会、写 PR、报进度、讲风险。"
        "时间有限时先练这份，再刷全量。\n\n",
        "## 练法\n\n",
        "每天 10 条：看中文 3 秒内说英文 → 放进一句工作场景 → 录音。"
        "第二天遮住英文复述。\n\n",
    ]
    number = 0
    for category, items in FEATURED.items():
        lines.append(f"## {category}\n\n")
        lines.append("| # | 短语 | 中文 |\n|---:|---|---|\n")
        for phrase in items:
            number += 1
            row = lookup[phrase]
            lines.append(f"| {number} | {esc(row['phrase'])} | {esc(row['zh'])} |\n")
        lines.append("\n")
    lines += [
        "## 命令\n\n",
        "```bash\ncd ~/english/english-speaking-lab\n",
        "python scripts/study.py phrase --featured --n 10\n",
        "python scripts/study.py phrase --featured --n 10 --reverse\n",
        "```\n\n",
        "## 相关\n\n",
        "- [[12_word-phrase-bank/11-phrase-1200/_index|1200 短语总览]]\n",
        "- [[12_word-phrase-bank/10-fixed-chunks|固定搭配与高频句型]]\n",
        "- [[18_fsi-drills/_index|FSI 口语训练]]\n",
    ]
    (OUT / "featured-work-90.md").write_text("".join(lines), encoding="utf-8")


def main():
    rows = load_rows()
    chunks = chunk_groups(rows)
    files = write_group_notes(rows, chunks)
    write_index(rows, files)
    write_learning_plan(rows)
    write_featured(rows)
    print(f"rows: {len(rows)}")
    print(f"group notes: {len(files)}")
    print(f"output: {OUT}")


if __name__ == "__main__":
    main()

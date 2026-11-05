#!/usr/bin/env python3
"""Generate Obsidian notes for the 1,200-scene-sentence library.

Data:   08_sentence-library/1200-sentences/data/sentences-1200.tsv
Output: 08_sentence-library/1200-sentences/*.md
"""
import csv
from collections import OrderedDict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "08_sentence-library" / "1200-sentences"
DATA = OUT / "data" / "sentences-1200.tsv"
TODAY = date.today().isoformat()

SLUGS = {
    1: "workplace",
    2: "meetings",
    3: "daily-social",
    4: "opinions",
    5: "problems",
    6: "shopping-dining",
    7: "travel-hotel",
    8: "family-health",
    9: "learning",
    10: "calls-online",
}


def load():
    with DATA.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    for row in rows:
        row["category_no"] = int(row["category_no"])
    return rows


def esc(value):
    return value.replace("|", "\\|")


def frontmatter(title, note_type="sentence"):
    return (
        "---\n"
        f"type: {note_type}\n"
        f'title: "{title}"\n'
        "tags: [library/sentence, skill/speaking, status/learning]\n"
        f"created: {TODAY}\n"
        f"updated: {TODAY}\n"
        "---\n\n"
    )


def categories(rows):
    result = OrderedDict()
    for row in rows:
        result.setdefault(row["category_no"], []).append(row)
    return result


def write_category_notes(rows):
    cats = categories(rows)
    files = []
    for number, items in cats.items():
        title = f"1200 句 · {number:02d} {items[0]['category']}"
        name = f"{number:02d}-{SLUGS[number]}.md"
        prev_link = ""
        next_link = ""
        if number > 1:
            prev_link = f"[[08_sentence-library/1200-sentences/{number - 1:02d}-{SLUGS[number - 1]}|← 上一类]]"
        if number < len(cats):
            next_link = f"[[08_sentence-library/1200-sentences/{number + 1:02d}-{SLUGS[number + 1]}|下一类 →]]"

        lines = [
            frontmatter(title, "topic"),
            f"# {title}\n\n",
            f"> 共 **{len(items)}** 句。先遮住英文，看中文说 3 秒；再遮住中文，看英文说意思。\n\n",
        ]
        sections = OrderedDict()
        for row in items:
            sections.setdefault(row["section"], []).append(row)
        if list(sections) == ["综合"]:
            lines.append("## 全部 120 句\n\n")
            lines.append("| # | 英文 | 中文 |\n|---:|---|---|\n")
            for row in items:
                lines.append(f"| {row['id'][1:]} | {esc(row['english'])} | {esc(row['chinese'])} |\n")
        else:
            for section, section_rows in sections.items():
                lines.append(f"## {section}\n\n")
                lines.append("| # | 英文 | 中文 |\n|---:|---|---|\n")
                for row in section_rows:
                    lines.append(f"| {row['id'][1:]} | {esc(row['english'])} | {esc(row['chinese'])} |\n")
                lines.append("\n")

        lines += [
            "## 这一类的练法\n\n"
            "1. 每轮 20 句：中→英 3 秒，卡住就标记。\n"
            "2. 选 3 句改成你真实生活的版本，说一遍并录音。\n"
            "3. 第二天只复习标记过的句子。\n\n"
            "```bash\n"
            f"python scripts/study.py sentence --category {number} --n 20\n"
            "```\n\n"
            "## 导航\n\n"
            " · ".join(x for x in [prev_link, "[[08_sentence-library/1200-sentences/_index|1200 句总览]]", next_link] if x) + "\n",
        ]
        (OUT / name).write_text("".join(lines), encoding="utf-8")
        files.append((number, name, items[0]["category"], len(items)))
    return files


def write_index(rows, files):
    text = [
        frontmatter("1200 句场景口语", "hub"),
        "# 1200 句场景口语\n\n",
        "> 10 大场景 × 120 句 = **1,200 句**。每句都带中文，适合每天 20 句：听 → 跟读 → 中→英 → 录音。\n\n",
        "> [!info] 来源\n"
        "> 来自你提供的知乎文章正文（2026-11-05），逐条整理；"
        "来源与解析说明见 [[09_sources/04_1200-sentences|1200 句来源说明]]。\n\n",
        "## 每天 20 分钟\n\n",
        "| 时间 | 动作 |\n|---|---|\n",
        "| 4 min | 听 5 句参考音，标重音和停顿（`--tts`） |\n",
        "| 4 min | 影子跟读 5 句，每句 3 遍 |\n",
        "| 7 min | 中→英抽认 20 句：3 秒内开口，卡住就标记 |\n",
        "| 5 min | 选 3 句改成你的真实场景，录音并回听 |\n\n",
        "## 三条规则\n\n",
        "1. **中文提示 → 英文反应**：不要先想语法，先说整句。\n",
        "2. **一次只改一个词**：把人名、地点、时间换成你的。\n",
        "3. **录音才算练过**：每天至少留 1 段 60 秒录音。\n\n",
        "## 分类\n\n",
        "| # | 场景 | 句数 | 入口 |\n|---:|---|---:|---|\n",
    ]
    for number, name, title, count in files:
        text.append(
            f"| {number:02d} | {title} | {count} | "
            f"[[08_sentence-library/1200-sentences/{name[:-3]}|打开]] |\n"
        )
    text += [
        "\n## 专项入口\n\n",
        "- [[08_sentence-library/1200-sentences/learning-plan|60 天刷完计划]]：每天 20 句。\n",
        "- [[18_fsi-drills/_index|FSI 口语训练]]：把句子练成条件反射。\n",
        "- [[12_word-phrase-bank/11-basic-phrases/_index|基础短语 1125（补充）]]：短语级搭配，作为补充。\n\n",
        "## 命令\n\n",
        "```bash\ncd ~/english/english-speaking-lab\n",
        "python scripts/study.py sentence --n 20                # 中→英\n",
        "python scripts/study.py sentence --n 20 --reverse      # 英→中\n",
        "python scripts/study.py sentence --category 1 --n 20   # 按场景\n",
        "python scripts/study.py sentence --n 5 --tts           # 生成参考音\n",
        "~/english/.venv/bin/python scripts/build_sentence_1200_apkg.py  # 导出 Anki\n",
        "```\n\n",
        "## 相关\n\n",
        "- [[08_sentence-library/_index|句子库]]\n",
        "- [[LEARNING-PATH|学习路径]]\n",
        "- [[17_word-roots/_index|前后缀 335]]\n",
        "- [[18_fsi-drills/_index|FSI 口语训练]]\n",
    ]
    (OUT / "_index.md").write_text("".join(text), encoding="utf-8")


def write_plan(rows):
    per_day = 20
    lines = [
        frontmatter("1200 句 60 天计划", "guide"),
        "# 1200 句 60 天计划\n\n",
        "每天 **20 句**，60 天覆盖全部 1,200 句。每天 20 分钟：听 → 跟读 → 中→英 → 录音。\n\n",
        "## 每天固定动作\n\n",
        "1. 中→英抽认当天 20 句，3 秒说不出的画 `×`。\n",
        "2. 只复习昨天和前天画 `×` 的句子。\n",
        "3. 从当天句子选 3 句，改成你的真实场景并录音。\n",
        "4. 第 3、7、14 天回看同一批句子；连续 3 次说对才算掌握。\n\n",
        "## 日程\n\n",
        "| 天 | 编号 | 场景 | 任务 |\n|---:|---|---|---|\n",
    ]
    for day in range(1, 61):
        batch = rows[(day - 1) * per_day: day * per_day]
        if not batch:
            continue
        categories_in_batch = []
        for row in batch:
            if row["category"] not in categories_in_batch:
                categories_in_batch.append(row["category"])
        category_text = " / ".join(categories_in_batch)
        if day % 7 == 0:
            task = "本周错题重练 + 录 2 分钟复述"
        elif day % 6 == 0:
            task = "本场景 120 句串联复述"
        else:
            task = "20 句抽认 + 3 句改写录音"
        lines.append(
            f"| D{day} | {batch[0]['id']}–{batch[-1]['id']} | {category_text} | {task} |\n"
        )
    lines += [
        "\n## 验收\n\n",
        "| 周 | 能做什么 |\n|---|---|\n",
        "| 第 1 周 | 职场 120 句里任意 20 句，15 句能 3 秒开口 |\n",
        "| 第 2 周 | 用会议与社交句子完成 2 分钟对话 |\n",
        "| 第 3 周 | 用观点/问题解决句子讲清一个立场 |\n",
        "| 第 4 周 | 购物、餐厅、旅行场景能即时反应 |\n",
        "| 第 5 周 | 家庭、健康、学习场景能自然表达 |\n",
        "| 第 6 周 | 电话/线上会议能连续说 2 分钟 |\n\n",
        "## 相关\n\n",
        "- [[08_sentence-library/1200-sentences/_index|1200 句总览]]\n",
        "- [[18_fsi-drills/learning-plan|FSI 4 周计划]]\n",
    ]
    (OUT / "learning-plan.md").write_text("".join(lines), encoding="utf-8")


def main():
    rows = load()
    files = write_category_notes(rows)
    write_index(rows, files)
    write_plan(rows)
    print(f"rows: {len(rows)}")
    print(f"categories: {len(files)}")
    print(f"output: {OUT}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Generate Obsidian notes for the word-root module from canonical TSVs.

Data:   17_word-roots/data/{roots,prefixes,suffixes,tech}.tsv
Output: 17_word-roots/*.md
"""
import csv
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "17_word-roots"
DATA = OUT / "data"
TODAY = date.today().isoformat()


def load(name):
    with (DATA / name).open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def esc(value):
    return value.replace("|", "\\|")


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


def write_index(roots, prefixes, suffixes, tech):
    text = [
        frontmatter("英语词根训练", "hub"),
        "# 英语词根训练\n\n",
        "> 词根是**记忆线索**，不是翻译公式。先认识一个词，再用词根解释它；"
        "不要反过来拿词根硬拼一个没见过的词。\n\n",
        "> [!warning] 使用边界\n"
        "> 词根含义来自历史语源，现代词义可能已经偏移（例如 `premise` 不能简单拆成“预先+送”）。"
        "拆解只用于辅助记忆，遇到不确定的词先查词典。\n\n",
        f"## 规模\n\n| 模块 | 数量 | 入口 |\n|---|---:|---|\n"
        f"| 核心词根 | {len(roots)} | [[17_word-roots/01-core-roots|词根表]] |\n"
        f"| 前缀 | {len(prefixes)} | [[17_word-roots/02-prefixes|前缀表]] |\n"
        f"| 后缀 | {len(suffixes)} | [[17_word-roots/03-suffixes|后缀表]] |\n"
        f"| 技术词拆解 | {len(tech)} | [[17_word-roots/04-tech-words|技术词]] |\n\n",
        "## 每天 15 分钟\n\n"
        "| 时间 | 动作 |\n|---|---|\n"
        "| 3 min | 复习昨天 5 个词根：遮住含义，各说 1 个例词 |\n"
        "| 5 min | 新学 5 个词根：每个读 3 个例词，只记一个核心含义 |\n"
        "| 4 min | 3 个技术词：先猜拆解，再看答案 |\n"
        "| 3 min | 挑 1 个词根，用它的例词说 2 句工作场景的话 |\n\n",
        "## 三条规则\n\n"
        "1. **一个词根只记一个含义**：`tain` 先记“握住”，不要背五种变体。\n"
        "2. **例词优先**：能说出 3 个例词，比背出词根定义有用。\n"
        "3. **技术服务表达**：技术词拆解要用在你的 PR、文档或面试句子里。\n\n",
        "## 命令\n\n",
        "```bash\ncd ~/english/english-speaking-lab\n",
        "python scripts/study.py root --n 10              # 词根→含义\n",
        "python scripts/study.py root --n 10 --reverse    # 含义→词根\n",
        "python scripts/study.py root --tech --n 10       # 技术词拆解\n",
        "~/english/.venv/bin/python scripts/build_phrase_roots_apkg.py        # 导出 Anki\n",
        "```\n\n",
        "## 相关\n\n",
        "- [[17_word-roots/learning-plan|6 周词根计划]]\n",
        "- [[17_word-roots/05-drills|词根练习卷]]\n",
        "- [[12_word-phrase-bank/_index|词与短语库]]\n",
        "- [[13_tech-frameworks/_index|技术与框架]]\n",
        "- [[18_fsi-drills/_index|FSI 口语训练]]\n",
    ]
    (OUT / "_index.md").write_text("".join(text), encoding="utf-8")


def write_roots(roots):
    lines = [
        frontmatter("核心词根 60", "word-bank"),
        "# 核心词根 60\n\n",
        "> 每个词根只记一个核心含义，再记 3 个例词。复习时遮住“含义”和“例词”。\n\n",
        "| # | 词根 | 含义 | 例词 | 记忆提示 |\n|---:|---|---|---|---|\n",
    ]
    for row in roots:
        lines.append(
            f"| {row['id'][1:]} | **{esc(row['root'])}** | {esc(row['meaning'])} | "
            f"{esc(row['examples'])} | {esc(row['note'])} |\n"
        )
    lines += [
        "\n## 练法\n\n",
        "1. 看词根说含义，看含义写词根，两个方向都过。\n",
        "2. 从例词里挑 1 个，造一句你工作里会用的话。\n",
        "3. 不认识的例词先查发音，不要默读。\n\n",
        "## 相关\n\n",
        "- [[17_word-roots/05-drills|词根练习卷]]\n",
        "- [[17_word-roots/04-tech-words|技术词拆解]]\n",
    ]
    (OUT / "01-core-roots.md").write_text("".join(lines), encoding="utf-8")


def write_affixes(prefixes, suffixes):
    lines = [
        frontmatter("前缀 44", "word-bank"),
        "# 前缀 44\n\n",
        "> 前缀改变方向或态度：否定、重复、反对、上下、内外。先记方向，再记例词。\n\n",
        "| # | 前缀 | 含义 | 例词 |\n|---:|---|---|---|\n",
    ]
    for row in prefixes:
        lines.append(
            f"| {row['id'][1:]} | **{esc(row['prefix'])}** | {esc(row['meaning'])} | {esc(row['examples'])} |\n"
        )
    lines += [
        "\n## 易混\n\n",
        "- `in-` 既可表示“不”（invisible），也可表示“进入”（inject）；看例词判断。\n",
        "- `de-` 既可表示“向下”（decrease），也可表示“去除/解码”（decode）。\n",
        "- `con-/com-/col-/cor-` 是同一个前缀在不同辅音前的拼写变体。\n\n",
        "## 相关\n\n- [[17_word-roots/03-suffixes|后缀]]\n- [[17_word-roots/01-core-roots|核心词根]]\n",
    ]
    (OUT / "02-prefixes.md").write_text("".join(lines), encoding="utf-8")

    lines = [
        frontmatter("后缀 21", "word-bank"),
        "# 后缀 21\n\n",
        "> 后缀主要决定**词性**：名词、形容词、动词。先判断词性，再猜含义。\n\n",
        "| # | 后缀 | 含义 / 词性 | 例词 |\n|---:|---|---|---|\n",
    ]
    for row in suffixes:
        lines.append(
            f"| {row['id'][1:]} | **{esc(row['suffix'])}** | {esc(row['meaning'])} | {esc(row['examples'])} |\n"
        )
    lines += [
        "\n## 练法\n\n",
        "看到一个生词，先只看后缀判断词性，再决定它在句子里能不能作主语/谓语/修饰语。\n\n",
        "## 相关\n\n- [[17_word-roots/02-prefixes|前缀]]\n- [[17_word-roots/01-core-roots|核心词根]]\n",
    ]
    (OUT / "03-suffixes.md").write_text("".join(lines), encoding="utf-8")


def write_tech(tech):
    lines = [
        frontmatter("技术词拆解 50", "word-bank"),
        "# 技术词拆解 50\n\n",
        "> 面向 AI / 后端 / RAG / Agent 的高频词。**先猜，再看**；拆解只用于记忆，不替代词典。\n\n",
        "| # | 单词 | 拆解 | 中文 | 记忆点 |\n|---:|---|---|---|---|\n",
    ]
    for row in tech:
        lines.append(
            f"| {row['id'][1:]} | **{esc(row['word'])}** | {esc(row['parts'])} | "
            f"{esc(row['meaning'])} | {esc(row['note'])} |\n"
        )
    lines += [
        "\n## 用法\n\n",
        "每个词配一句你项目里的真实句子，例如：\n\n",
        "> We **retain** the raw logs for 30 days, then **aggregate** them into daily metrics.\n\n",
        "## 相关\n\n",
        "- [[03_ai-agent-rag/_index|AI / Agent / RAG 表达]]\n",
        "- [[12_word-phrase-bank/06-ai-llm-terms|AI / LLM 术语]]\n",
    ]
    (OUT / "04-tech-words.md").write_text("".join(lines), encoding="utf-8")


def write_drills(roots, tech):
    root_pick = roots[::4][:15]
    meaning_pick = roots[2::6][:10]
    tech_pick = tech[::3][:15]

    lines = [
        frontmatter("词根练习卷", "guide"),
        "# 词根练习卷\n\n",
        "> 先全部做完，再对照文末答案。每部分限时 5 分钟。\n\n",
        "## A. 看词根，说含义（15）\n\n",
    ]
    for number, row in enumerate(root_pick, 1):
        lines.append(f"{number}. `{row['root']}` → ______\n")
    lines.append("\n## B. 看含义，写词根（10）\n\n")
    for number, row in enumerate(meaning_pick, 1):
        lines.append(f"{number}. {row['meaning']} → ______\n")
    lines.append("\n## C. 拆技术词（15）\n\n")
    for number, row in enumerate(tech_pick, 1):
        lines.append(f"{number}. `{row['word']}` → ______\n")
    lines.append("\n## D. 造句（10）\n\n")
    lines.append("从下面 10 个词里任选 5 个，各造一句工作场景的话，并录音：\n\n")
    lines.append("、".join(f"`{row['root']}`" for row in roots[:10]) + "\n")

    lines.append("\n---\n\n## 答案\n\n")
    lines.append("### A\n\n")
    for number, row in enumerate(root_pick, 1):
        lines.append(f"{number}. {row['meaning']}（{row['examples'].split(',')[0].strip()}）\n")
    lines.append("\n### B\n\n")
    for number, row in enumerate(meaning_pick, 1):
        lines.append(f"{number}. {row['root']}\n")
    lines.append("\n### C\n\n")
    for number, row in enumerate(tech_pick, 1):
        lines.append(f"{number}. {row['parts']} → {row['meaning']}\n")
    lines.append(
        "\n## 相关\n\n- [[17_word-roots/01-core-roots|核心词根]]\n"
        "- [[17_word-roots/04-tech-words|技术词拆解]]\n"
    )
    (OUT / "05-drills.md").write_text("".join(lines), encoding="utf-8")


def write_plan():
    lines = [
        frontmatter("词根 6 周计划", "guide"),
        "# 词根 6 周计划\n\n",
        "> 每周 10 个词根 + 8 个前缀/后缀 + 8 个技术词。每天 15 分钟，周末做练习卷。\n\n",
        "| 周 | 词根 | 词缀 | 技术词 | 周末输出 |\n|---:|---|---|---|---|\n",
        "| 1 | 1–10 | 前缀 1–8 | 1–8 | 用 5 个词根各造 1 句 |\n",
        "| 2 | 11–20 | 前缀 9–16 | 9–16 | 讲清 1 个 bug 的 5 句 |\n",
        "| 3 | 21–30 | 前缀 17–24 | 17–24 | 写 1 段技术选型说明 |\n",
        "| 4 | 31–40 | 前缀 25–32 | 25–32 | 做 A/B 部分练习卷 |\n",
        "| 5 | 41–50 | 前缀 33–40 | 33–40 | 做 C 部分并录音 |\n",
        "| 6 | 51–60 | 后缀 1–21 | 41–50 | 做完整练习卷 + 复盘 |\n\n",
        "## 每天 15 分钟\n\n",
        "1. 复习昨天 5 个词根，遮住含义说例词。\n",
        "2. 新学 5 个词根，每个只记 1 个含义。\n",
        "3. 3 个技术词，先猜拆解再看答案。\n",
        "4. 选 1 个词根造 2 句工作句并录音。\n\n",
        "## 验收\n\n",
        "| 周 | 标准 |\n|---|---|\n",
        "| 第 2 周 | 看到 20 个词根能说出含义和 1 个例词 |\n",
        "| 第 4 周 | 能把 10 个技术词拆开并解释 |\n",
        "| 第 6 周 | 能用词根线索猜出生词的大致方向，并查词典确认 |\n\n",
        "## 相关\n\n- [[17_word-roots/_index|词根训练]]\n- [[17_word-roots/05-drills|练习卷]]\n",
    ]
    (OUT / "learning-plan.md").write_text("".join(lines), encoding="utf-8")


def main():
    roots = load("roots.tsv")
    prefixes = load("prefixes.tsv")
    suffixes = load("suffixes.tsv")
    tech = load("tech.tsv")
    write_index(roots, prefixes, suffixes, tech)
    write_roots(roots)
    write_affixes(prefixes, suffixes)
    write_tech(tech)
    write_drills(roots, tech)
    write_plan()
    print(f"roots={len(roots)} prefixes={len(prefixes)} suffixes={len(suffixes)} tech={len(tech)}")
    print(f"output: {OUT}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Generate Obsidian notes and TSVs for the 164 prefixes + 171 suffixes article.

Source: 09_sources/media/zhihu-affixes.html
Output: 17_word-roots/{data/*.tsv,*.md}
"""
import csv
import html
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "17_word-roots"
DATA = OUT / "data"
SRC = ROOT / "09_sources" / "media" / "zhihu-affixes.html"
TODAY = date.today().isoformat()


def clean(text):
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"\s+", " ", html.unescape(text).replace("\xa0", " ")).strip()


def parse_section(section, kind):
    heads = re.findall(r"<h3>(.*?)</h3>\s*<p[^>]*>(.*?)</p>", section, flags=re.S)
    items = []
    for heading, para in heads:
        heading = clean(heading)
        match = re.match(r"^\d+\.\s*(.*?)\s*[（(](.*)[）)]\s*$", heading)
        if not match:
            raise SystemExit(f"bad heading ({kind}): {heading!r}")
        form = match.group(1).strip()
        meaning = re.sub(r"^表示\s*", "", match.group(2).strip()).strip()
        if len(meaning) >= 2 and meaning[0] in '“"' and meaning[-1] in '”"':
            meaning = meaning[1:-1]
        text = clean(para)
        if text.startswith("例词："):
            text = text[3:].strip()
        chunks = [x.strip() for x in re.split(r"(?<=[)）]),\s*", text) if x.strip()]
        examples = []
        for chunk in chunks:
            ex = re.match(r"^(.*?)\s*[（(]([^()（）]*)[）)]\s*$", chunk)
            if not ex:
                raise SystemExit(f"bad example ({kind} {form}): {chunk!r}")
            word, gloss = ex.group(1).strip(), ex.group(2).strip()
            pos_match = re.match(r"^([a-zA-Z./]+)\s+(.+)$", gloss)
            pos, zh = (pos_match.group(1), pos_match.group(2)) if pos_match else ("", gloss)
            examples.append((word, pos, zh))
        seen = set()
        unique = []
        for example in examples:
            key = example[0].lower()
            if key in seen:
                continue
            seen.add(key)
            unique.append(example)
        items.append((form, meaning, unique))
    return items


def load():
    source = SRC.read_text(encoding="utf-8")
    split = source.find("二、171个后缀")
    if split < 0:
        raise SystemExit("suffix section not found")
    prefixes = parse_section(source[:split], "prefix")
    suffixes = parse_section(source[split:], "suffix")
    return prefixes, suffixes


def write_tsv(prefixes, suffixes):
    DATA.mkdir(parents=True, exist_ok=True)
    affixes = []
    examples = []
    for kind, items, prefix_id in (("prefix", prefixes, "X"), ("suffix", suffixes, "S")):
        for number, (form, meaning, items_ex) in enumerate(items, 1):
            affix_id = f"{prefix_id}{number:03d}"
            affixes.append((affix_id, kind, form, meaning, len(items_ex)))
            for word, pos, zh in items_ex:
                examples.append((
                    f"E{len(examples) + 1:04d}", affix_id, kind, form, meaning, word, pos, zh,
                ))
    with (DATA / "affixes.tsv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
        writer.writerow(["id", "type", "form", "meaning", "examples_count"])
        writer.writerows(affixes)
    with (DATA / "affix-examples.tsv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
        writer.writerow(["id", "affix_id", "type", "form", "meaning", "word", "pos", "zh"])
        writer.writerows(examples)
    return affixes, examples


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


def example_text(items):
    return ", ".join(f"{word} ({pos} {zh})".strip() for word, pos, zh in items)


def write_range_notes(kind, items, start_number, filename, title):
    lines = [
        frontmatter(title),
        f"# {title}\n\n",
        f"> 共 **{len(items)}** 个{('前缀' if kind == 'prefix' else '后缀')}。"
        "先看词缀猜含义，再看例词验证；不要反过来用词缀硬拼生词。\n\n",
        f"| # | {'前缀' if kind == 'prefix' else '后缀'} | 含义 / 词性 | 例词 |\n"
        "|---:|---|---|---|\n",
    ]
    for offset, (form, meaning, examples) in enumerate(items):
        number = start_number + offset
        form_cell = form.replace("|", "\\|")
        meaning_cell = meaning.replace("|", "\\|")
        examples_cell = example_text(examples).replace("|", "\\|")
        lines.append(f"| {number} | **{form_cell}** | {meaning_cell} | {examples_cell} |\n")
    lines += [
        "\n## 练法\n\n",
        "1. 遮住“含义”，看词缀说方向或词性。\n",
        "2. 从例词里挑 2 个，各造一句你工作或生活里会用的话。\n",
        "3. 第二天只看例词，反推词缀。\n\n",
        "## 相关\n\n",
        "- [[17_word-roots/_index|前后缀总览]]\n",
        "- [[17_word-roots/09-drills|词缀练习卷]]\n",
    ]
    (OUT / filename).write_text("".join(lines), encoding="utf-8")


def write_index(prefixes, suffixes, examples):
    prefix_examples = sum(len(x[2]) for x in prefixes)
    suffix_examples = sum(len(x[2]) for x in suffixes)
    text = [
        frontmatter("英语前后缀 335", "hub"),
        "# 英语前后缀 335\n\n",
        f"> **164 个前缀 + 171 个后缀 + {len(examples):,} 个例词**，全部来自你提供的知乎原文。"
        "词缀是记忆线索，不是翻译公式；先认识例词，再用词缀解释它。\n\n",
        "> [!info] 来源\n"
        "> 知乎文章正文（2026-11-05 提供），逐条整理；"
        "见 [[09_sources/05_affixes-335|前后缀来源说明]]。\n\n",
        "## 规模\n\n"
        "| 模块 | 数量 | 例词 | 入口 |\n|---|---:|---:|---|\n",
        f"| 前缀 | {len(prefixes)} | {prefix_examples} | [[17_word-roots/01-prefixes-01-41|前缀 1–41]] → "
        "[[17_word-roots/04-prefixes-124-164|前缀 124–164]] |\n",
        f"| 后缀 | {len(suffixes)} | {suffix_examples} | [[17_word-roots/05-suffixes-01-43|后缀 1–43]] → "
        "[[17_word-roots/08-suffixes-130-171|后缀 130–171]] |\n\n",
        "## 每天 15 分钟\n\n"
        "| 时间 | 动作 |\n|---|---|\n"
        "| 4 min | 复习昨天 10 个例词：遮住词缀，说出它的方向/词性 |\n"
        "| 5 min | 新学 6 个词缀：读例词，只记一个核心含义 |\n"
        "| 4 min | 例词抽认 10 个：看单词，说词缀和大致意思 |\n"
        "| 2 min | 选 1 个例词造一句你工作里的句子 |\n\n",
        "## 三条规则\n\n"
        "1. **词缀只给方向**：`in-` 可能是否定，也可能是“进入”，看例词判断。\n"
        "2. **例词优先**：能说出 2 个例词，比背出词缀定义有用。\n"
        "3. **不确定就查词典**：词源会漂移，不要拿词缀硬猜具体词义。\n\n",
        "## 命令\n\n",
        "```bash\ncd ~/english/english-speaking-lab\n",
        "python scripts/study.py affix --type prefix --n 10\n",
        "python scripts/study.py affix --type suffix --n 10\n",
        "python scripts/study.py affix --examples --n 10       # 例词→词缀\n",
        "python scripts/study.py affix --type all --reverse --n 10\n",
        "~/english/.venv/bin/python scripts/build_affix_apkg.py  # 导出 Anki\n",
        "```\n\n",
        "## 分册\n\n",
        "| 分册 | 入口 |\n|---|---|\n",
        "| 前缀 1–41 | [[17_word-roots/01-prefixes-01-41|打开]] |\n",
        "| 前缀 42–82 | [[17_word-roots/02-prefixes-42-82|打开]] |\n",
        "| 前缀 83–123 | [[17_word-roots/03-prefixes-83-123|打开]] |\n",
        "| 前缀 124–164 | [[17_word-roots/04-prefixes-124-164|打开]] |\n",
        "| 后缀 1–43 | [[17_word-roots/05-suffixes-01-43|打开]] |\n",
        "| 后缀 44–86 | [[17_word-roots/06-suffixes-44-86|打开]] |\n",
        "| 后缀 87–129 | [[17_word-roots/07-suffixes-87-129|打开]] |\n",
        "| 后缀 130–171 | [[17_word-roots/08-suffixes-130-171|打开]] |\n\n",
        "## 相关\n\n",
        "- [[17_word-roots/learning-plan|8 周词缀计划]]\n",
        "- [[17_word-roots/09-drills|词缀练习卷]]\n",
        "- [[12_word-phrase-bank/11-basic-phrases/_index|基础短语 1125（补充）]]\n",
        "- [[08_sentence-library/1200-sentences/_index|1200 句场景口语]]\n",
        "- [[18_fsi-drills/_index|FSI 口语训练]]\n",
        "- [[19_qwerty-learner/_index|qwerty 打字练习]]\n",
    ]
    (OUT / "_index.md").write_text("".join(text), encoding="utf-8")


def write_drills(prefixes, suffixes, examples):
    prefix_pick = prefixes[::11][:15]
    meaning_pick = prefixes[3::16][:10]
    suffix_pick = suffixes[::11][:15]
    word_pick = examples[::120][:15]

    lines = [
        frontmatter("词缀练习卷", "guide"),
        "# 词缀练习卷\n\n",
        "> 先全部做完，再对照文末答案。每部分限时 5 分钟。\n\n",
        "## A. 看前缀，说含义（15）\n\n",
    ]
    for number, (form, meaning, items) in enumerate(prefix_pick, 1):
        lines.append(f"{number}. `{form}` → ______\n")
    lines.append("\n## B. 看含义，写前缀（10）\n\n")
    for number, (form, meaning, items) in enumerate(meaning_pick, 1):
        lines.append(f"{number}. {meaning} → ______\n")
    lines.append("\n## C. 看后缀，说词性/含义（15）\n\n")
    for number, (form, meaning, items) in enumerate(suffix_pick, 1):
        lines.append(f"{number}. `{form}` → ______\n")
    lines.append("\n## D. 看例词，反推词缀（15）\n\n")
    for number, row in enumerate(word_pick, 1):
        lines.append(f"{number}. `{row[5]}`（{row[7]}）→ ______\n")
    lines.append("\n## E. 造句（5）\n\n")
    lines.append("从下面 5 个例词里任选 3 个，各造一句工作/生活场景的话并录音：\n\n")
    lines.append("、".join(f"`{x[5]}`" for x in word_pick[:5]) + "\n")

    lines.append("\n---\n\n## 答案\n\n### A\n\n")
    for number, (form, meaning, items) in enumerate(prefix_pick, 1):
        lines.append(f"{number}. {meaning}\n")
    lines.append("\n### B\n\n")
    for number, (form, meaning, items) in enumerate(meaning_pick, 1):
        lines.append(f"{number}. {form}\n")
    lines.append("\n### C\n\n")
    for number, (form, meaning, items) in enumerate(suffix_pick, 1):
        lines.append(f"{number}. {meaning}\n")
    lines.append("\n### D\n\n")
    for number, row in enumerate(word_pick, 1):
        lines.append(f"{number}. {row[3]}（{row[7]}）\n")
    lines.append(
        "\n## 相关\n\n- [[17_word-roots/_index|前后缀总览]]\n"
        "- [[17_word-roots/learning-plan|8 周计划]]\n"
    )
    (OUT / "09-drills.md").write_text("".join(lines), encoding="utf-8")


def write_plan():
    lines = [
        frontmatter("8 周词缀计划", "guide"),
        "# 8 周词缀计划\n\n",
        "> 每周约 20 个前缀 + 21 个后缀 + 220 个例词。每天 15 分钟，周末做练习卷。\n\n",
        "| 周 | 前缀 | 后缀 | 例词 | 周末输出 |\n|---:|---|---|---|---|\n",
        "| 1 | 1–20 | 1–21 | 约 220 | 用 10 个词缀各说 1 个例词 |\n",
        "| 2 | 21–41 | 22–43 | 约 230 | 讲清 1 个技术概念里的 5 个词 |\n",
        "| 3 | 42–62 | 44–65 | 约 230 | 写 1 段技术选型说明 |\n",
        "| 4 | 63–82 | 66–86 | 约 220 | 做 A/B 部分练习卷 |\n",
        "| 5 | 83–103 | 87–108 | 约 230 | 做 C 部分并录音 |\n",
        "| 6 | 104–123 | 109–129 | 约 220 | 例词抽认 50 个 |\n",
        "| 7 | 124–144 | 130–150 | 约 220 | 用 20 个例词写一段话 |\n",
        "| 8 | 145–164 | 151–171 | 约 230 | 做完整练习卷 + 复盘 |\n\n",
        "## 每天 15 分钟\n\n",
        "1. 复习昨天 10 个例词，遮住词缀说方向/词性。\n",
        "2. 新学 6 个词缀，每个读 2–3 个例词。\n",
        "3. 例词抽认 10 个：看单词说词缀和大致意思。\n",
        "4. 选 1 个例词造句并录音。\n\n",
        "## 验收\n\n",
        "| 周 | 标准 |\n|---|---|\n",
        "| 第 2 周 | 看到 40 个词缀能说出方向/词性 |\n",
        "| 第 4 周 | 能把 20 个生词拆出词缀并猜方向 |\n",
        "| 第 6 周 | 例词抽认正确率 70% |\n",
        "| 第 8 周 | 能自觉用词缀辅助记忆，并查词典确认 |\n\n",
        "## 相关\n\n- [[17_word-roots/_index|前后缀总览]]\n- [[17_word-roots/09-drills|练习卷]]\n",
    ]
    (OUT / "learning-plan.md").write_text("".join(lines), encoding="utf-8")


def main():
    prefixes, suffixes = load()
    affixes, examples = write_tsv(prefixes, suffixes)
    write_range_notes("prefix", prefixes[:41], 1, "01-prefixes-01-41.md", "前缀 01–41")
    write_range_notes("prefix", prefixes[41:82], 42, "02-prefixes-42-82.md", "前缀 42–82")
    write_range_notes("prefix", prefixes[82:123], 83, "03-prefixes-83-123.md", "前缀 83–123")
    write_range_notes("prefix", prefixes[123:], 124, "04-prefixes-124-164.md", "前缀 124–164")
    write_range_notes("suffix", suffixes[:43], 1, "05-suffixes-01-43.md", "后缀 01–43")
    write_range_notes("suffix", suffixes[43:86], 44, "06-suffixes-44-86.md", "后缀 44–86")
    write_range_notes("suffix", suffixes[86:129], 87, "07-suffixes-87-129.md", "后缀 87–129")
    write_range_notes("suffix", suffixes[129:], 130, "08-suffixes-130-171.md", "后缀 130–171")
    write_index(prefixes, suffixes, examples)
    write_drills(prefixes, suffixes, examples)
    write_plan()
    print(f"prefixes={len(prefixes)} suffixes={len(suffixes)} examples={len(examples)}")
    print(f"output: {OUT}")


if __name__ == "__main__":
    main()

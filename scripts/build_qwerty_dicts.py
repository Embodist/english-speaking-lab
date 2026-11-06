#!/usr/bin/env python3
"""Build qwerty-learner dictionaries from the lab's canonical TSVs.

Output: 19_qwerty-learner/dicts/*.json + manifest.json
Format: [{"name": "...", "trans": ["...", "..."]}, ...]
"""
import csv
import json
from collections import OrderedDict
from pathlib import Path

from build_phrase_1200 import FEATURED
from build_sentence_1200 import SLUGS

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "19_qwerty-learner"
DICTS = OUT / "dicts"
SENTENCES = ROOT / "08_sentence-library" / "1200-sentences" / "data" / "sentences-1200.tsv"
PHRASES = ROOT / "12_word-phrase-bank" / "11-basic-phrases" / "data" / "phrases-1200.tsv"
AFFIXES = ROOT / "17_word-roots" / "data" / "affixes.tsv"
AFFIX_EXAMPLES = ROOT / "17_word-roots" / "data" / "affix-examples.tsv"
FSI = ROOT / "18_fsi-drills" / "data" / "drills.tsv"

CATEGORY = "English Lab"
TAG = "English Lab"


def normalize(text):
    return (text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("…", "..."))


def load(path):
    with Path(path).open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def write_dict(filename, entries, name, description, manifest):
    for entry in entries:
        entry["name"] = normalize(entry["name"])
    DICTS.mkdir(parents=True, exist_ok=True)
    path = DICTS / filename
    with path.open("w", encoding="utf-8") as fh:
        json.dump(entries, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    manifest.append({
        "id": filename.removesuffix(".json"),
        "file": filename,
        "name": name,
        "description": description,
        "category": CATEGORY,
        "length": len(entries),
        "language": "en",
        "languageCategory": "en",
        "tags": [TAG],
    })
    print(f"{filename}: {len(entries)}")


def affix_examples(manifest):
    rows = load(AFFIX_EXAMPLES)
    words = OrderedDict()
    for row in rows:
        key = row["word"].lower()
        item = words.setdefault(key, {"word": row["word"], "glosses": [], "forms": []})
        gloss = f"{row['pos']} {row['zh']}".strip()
        if gloss and gloss not in item["glosses"]:
            item["glosses"].append(gloss)
        form = f"{row['form']}：{row['meaning']}"
        if form not in item["forms"]:
            item["forms"].append(form)
    entries = []
    for item in words.values():
        trans = item["glosses"] + [f"词缀 {form}" for form in item["forms"]]
        entries.append({"name": item["word"], "trans": trans})
    write_dict(
        "english-lab-affix-examples.json", entries,
        "前后缀例词（去重）", "来自 164 前缀 + 171 后缀的 1,798 个例词，按单词去重并合并词缀信息。",
        manifest,
    )


def affixes(manifest):
    rows = load(AFFIXES)
    entries = []
    for row in rows:
        entries.append({
            "name": row["form"],
            "trans": [row["meaning"], f"{row['type']} · {row['examples_count']} 个例词"],
        })
    write_dict(
        "english-lab-affixes.json", entries,
        "前后缀 335", "164 个前缀 + 171 个后缀，含义与例词数量。",
        manifest,
    )


def basic_phrases(manifest):
    rows = load(PHRASES)
    entries = [{"name": row["phrase"], "trans": [row["zh"], "基础短语"]} for row in rows]
    write_dict(
        "english-lab-basic-phrases.json", entries,
        "基础短语 1125", "公开基础短语清单，去重合并多义。",
        manifest,
    )


def work_phrases(manifest):
    wanted = {phrase.lower() for items in FEATURED.values() for phrase in items}
    rows = [row for row in load(PHRASES) if row["phrase"].lower() in wanted]
    entries = []
    for row in rows:
        category = next(
            name for name, items in FEATURED.items()
            if row["phrase"].lower() in {x.lower() for x in items}
        )
        entries.append({"name": row["phrase"], "trans": [row["zh"], category]})
    write_dict(
        "english-lab-work-phrases.json", entries,
        "工作高频短语 90", "开会、写 PR、报进度、讲风险的高频短语。",
        manifest,
    )


def sentences(manifest):
    rows = load(SENTENCES)
    by_category = OrderedDict()
    for row in rows:
        by_category.setdefault(int(row["category_no"]), []).append(row)
    for number, items in by_category.items():
        entries = []
        for row in items:
            entries.append({
                "name": row["english"],
                "trans": [row["chinese"], f"{row['category']} · {row['section']}"],
            })
        title = items[0]["category"]
        write_dict(
            f"english-lab-sentences-{number:02d}-{SLUGS[number]}.json", entries,
            f"1200 句 · {number:02d} {title}", f"{title}：120 句场景口语。",
            manifest,
        )


def fsi(manifest):
    rows = load(FSI)
    entries = []
    for row in rows:
        entries.append({
            "name": row["answer"],
            "trans": [row["prompt"], f"FSI · {row['kind']}"],
        })
    write_dict(
        "english-lab-fsi-patterns.json", entries,
        "FSI 句型 126", "替换、变换、应答、情景的模型句。",
        manifest,
    )


def main():
    DICTS.mkdir(parents=True, exist_ok=True)
    for old in DICTS.glob("*.json"):
        old.unlink()
    manifest = []
    affix_examples(manifest)
    affixes(manifest)
    basic_phrases(manifest)
    work_phrases(manifest)
    sentences(manifest)
    fsi(manifest)
    with (OUT / "manifest.json").open("w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    total = sum(item["length"] for item in manifest)
    print(f"dicts={len(manifest)} cards={total}")


if __name__ == "__main__":
    main()

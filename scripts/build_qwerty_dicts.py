#!/usr/bin/env python3
"""Build qwerty-learner dictionaries from the lab's canonical TSVs.

Output: 19_qwerty-learner/dicts/*.json + manifest.json
Format: [{"name": "...", "trans": ["...", "..."]}, ...]
"""
import csv
import json
import os
import re
import sqlite3
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
ECDICT = Path(os.environ.get("ECDICT_SQLITE", "/home/user/english/data/ecdict.sqlite"))

CATEGORY = "English Lab"
TAG = "English Lab"

STOPWORDS = set("""
a an the about above across after against along among around at before behind below beneath beside
between beyond by down during except for from in inside into like near of off on onto out outside
over past since through throughout till to toward towards under until up upon with within without
and but or nor so yet because although though while whereas if unless when whenever where wherever
whether that which who whom whose am is are was were be been being have has had having do does did
doing will would shall should can could may might must not no yes very too also just only even still
already always never often sometimes usually soon now then here there again ever almost enough quite
rather really well as than both either neither each every all any some none many much more most few
little less least own same other another such sb sth etc
""".split())

PRONOUNS = [
    ("I", "我"), ("me", "我（宾格）"), ("my", "我的"), ("mine", "我的（名词性物主代词）"), ("myself", "我自己"),
    ("you", "你/你们"), ("your", "你的/你们的"), ("yours", "你的/你们的"), ("yourself", "你自己"), ("yourselves", "你们自己"),
    ("he", "他"), ("him", "他（宾格）"), ("his", "他的"), ("himself", "他自己"),
    ("she", "她"), ("her", "她/她的"), ("hers", "她的"), ("herself", "她自己"),
    ("it", "它"), ("its", "它的"), ("itself", "它自己"),
    ("we", "我们"), ("us", "我们（宾格）"), ("our", "我们的"), ("ours", "我们的"), ("ourselves", "我们自己"),
    ("they", "他们/她们/它们"), ("them", "他们（宾格）"), ("their", "他们的"), ("theirs", "他们的"), ("themselves", "他们自己"),
    ("this", "这个"), ("that", "那个"), ("these", "这些"), ("those", "那些"),
    ("who", "谁（主格）"), ("whom", "谁（宾格）"), ("whose", "谁的"), ("which", "哪一个/哪些"), ("what", "什么"),
    ("someone", "某人"), ("somebody", "某人"), ("anyone", "任何人"), ("anybody", "任何人"),
    ("everyone", "每个人"), ("everybody", "每个人"), ("nobody", "没有人"), ("no one", "没有人"),
    ("something", "某事"), ("anything", "任何事"), ("everything", "每件事"), ("nothing", "没有什么"),
    ("each other", "彼此"), ("one another", "互相"),
]

FALLBACK = {
    "canadiana": "加拿大史料",
    "children's": "孩子们的",
    "client's": "客户的",
    "company's": "公司的",
    "cryptocurrency": "加密货币",
    "demi-pension": "半食宿",
    "doctor's": "医生的",
    "everyone's": "每个人的",
    "liliacea": "百合科（植物）",
    "macroscope": "宏观观察仪",
    "ornithomorphic": "鸟形的",
    "other's": "他人的",
    "overthink": "过度思考",
    "people's": "人们的",
    "pseudo-intellectual": "伪知识分子",
    "quasi-scientific": "准科学的",
    "semi-conscious": "半清醒的",
    "supra-national": "超国家的",
    "supraclass": "超阶级的",
    "today's": "今天的",
    "trichad": "三叉的",
    "well-respected": "受尊敬的",
}


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


TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z'’\-]*")


def content_texts():
    entries = []
    for row in load(SENTENCES):
        entries.append((row["english"], "1200 句"))
    for row in load(PHRASES):
        entries.append((row["phrase"], "短语"))
    for row in load(AFFIX_EXAMPLES):
        entries.append((row["word"], "词缀例词"))
    for row in load(FSI):
        entries.append((row["answer"], "FSI"))
    return entries


def collect_words():
    words = {}
    for text, tag in content_texts():
        for token in TOKEN_RE.findall(text):
            display = token.replace("’", "'").strip("'-")
            low = display.lower()
            if len(low) == 1 and low not in ("a", "i"):
                continue
            if not low:
                continue
            item = words.setdefault(low, {"display": display, "tags": set()})
            item["tags"].add(tag)
    return words


def clean_translation(text):
    text = text.replace("\\r\\n", "\n").replace("\\n", "\n").replace("\\t", " ")
    lines = [line.strip() for line in text.splitlines() if line.strip() and not line.strip().startswith("[网络]")]
    return "；".join(lines[:3]) or text.strip()


def lookup_word(cur, word):
    if word in FALLBACK:
        return "", FALLBACK[word]
    row = cur.execute(
        "select phonetic, translation from entries where word=? collate nocase limit 1",
        (word,),
    ).fetchone()
    if row:
        return row[0] or "", clean_translation(row[1] or "")
    if word.endswith("'s"):
        base = word[:-2]
        row = cur.execute(
            "select phonetic, translation from entries where word=? collate nocase limit 1",
            (base,),
        ).fetchone()
        if row:
            return row[0] or "", clean_translation(row[1] or "") + "的"
    return "", ""


def find_example(rows, phrase):
    pattern = r"\b" + re.escape(phrase).replace(r"\ ", r"\s+") + r"\b"
    for row in rows:
        if re.search(pattern, row["english"], re.I):
            return row["english"]
    return ""


def word_decks(manifest):
    if not ECDICT.exists():
        print(f"skip word decks: ECDICT not found at {ECDICT}")
        return
    words = collect_words()
    rows = load(SENTENCES)
    con = sqlite3.connect(ECDICT)
    cur = con.cursor()
    pronoun_keys = {name.lower() for name, _ in PRONOUNS}
    all_entries = []
    new_entries = []
    missing = []
    for low, item in sorted(words.items()):
        phonetic, trans = lookup_word(cur, low)
        if not trans:
            missing.append(low)
            trans = "（待补）"
        entry = {
            "name": item["display"],
            "trans": [trans, "来源：" + " / ".join(sorted(item["tags"]))],
        }
        if phonetic:
            entry["usphone"] = phonetic
            entry["ukphone"] = phonetic
        all_entries.append(entry)
        if low not in STOPWORDS and low not in pronoun_keys:
            new_entries.append(entry)
    write_dict(
        "english-lab-all-words.json", all_entries,
        "全部单词 3625", "从 1200 句、短语、词缀例词和 FSI 句型中提取的全部单词，ECDICT 释义。",
        manifest,
    )
    write_dict(
        "english-lab-new-words.json", new_entries,
        "新词 3487", "排除常见功能词和代词后的内容词，ECDICT 释义。",
        manifest,
    )

    pronoun_entries = []
    for name, zh in PRONOUNS:
        phonetic, _ = lookup_word(cur, name.lower())
        example = find_example(rows, name)
        trans = [zh, "代词"]
        if example:
            trans.append(f"例句：{example}")
        entry = {"name": name, "trans": trans}
        if phonetic:
            entry["usphone"] = phonetic
            entry["ukphone"] = phonetic
        pronoun_entries.append(entry)
    write_dict(
        "english-lab-pronouns.json", pronoun_entries,
        "代词 54", "人称、物主、反身、指示、疑问和不定代词，附例句。",
        manifest,
    )
    con.close()
    print(f"words={len(all_entries)} new={len(new_entries)} pronouns={len(pronoun_entries)} missing={len(missing)}")
    if missing:
        print("missing translations:", ", ".join(missing))


PAPER_DIR = ROOT / "14_llm-papers" / "vocabulary-10k"
CPP_CSV = ROOT / "16_cpp-core-guidelines" / "master.csv"


def paper_words(manifest):
    words = OrderedDict()
    for path in sorted(PAPER_DIR.glob("anki-*.csv")):
        with path.open(encoding="utf-8-sig", newline="") as fh:
            for row in csv.DictReader(fh):
                word = (row.get("word") or "").strip()
                if word and word.lower() not in words:
                    words[word.lower()] = row
    entries = []
    for row in words.values():
        entry = {"name": row["word"].strip(), "trans": [row.get("chinese", "").strip(), "论文 10k"]}
        phonetic = (row.get("phonetic") or "").strip()
        if phonetic:
            entry["usphone"] = phonetic
            entry["ukphone"] = phonetic
        entries.append(entry)
    write_dict(
        "english-lab-paper-10k.json", entries,
        "论文 10k 词", "论文阅读词表去重后的 10,127 个词，含 ECDICT 释义与音标。",
        manifest,
    )


def cpp_words(manifest):
    words = OrderedDict()
    with CPP_CSV.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            word = (row.get("word") or "").strip()
            if word and word.lower() not in words:
                words[word.lower()] = row
    entries = []
    for row in words.values():
        entry = {
            "name": row["word"].strip(),
            "trans": [row.get("chinese", "").strip(), "C++ · " + row.get("section", "").strip()],
        }
        phonetic = (row.get("phonetic") or "").strip()
        if phonetic:
            entry["usphone"] = phonetic
            entry["ukphone"] = phonetic
        entries.append(entry)
    write_dict(
        "english-lab-cpp-292.json", entries,
        "C++ 术语 292", "C++ Core Guidelines 词表中的 292 个术语。",
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
    word_decks(manifest)
    paper_words(manifest)
    cpp_words(manifest)
    with (OUT / "manifest.json").open("w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    total = sum(item["length"] for item in manifest)
    print(f"dicts={len(manifest)} cards={total}")


if __name__ == "__main__":
    main()

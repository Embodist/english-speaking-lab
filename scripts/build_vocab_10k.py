#!/usr/bin/env python3
"""Build a 10k+ paper vocabulary from the LLM paper PDFs.

Inputs:
  ~/llm-papers/**.pdf
  ~/english/data/ecdict.sqlite       (ECDICT, MIT)
  14_llm-papers/vocabulary.csv       (per-paper vocabulary)
  14_llm-papers/core-vocabulary.csv  (core + domain terms)

Outputs:
  14_llm-papers/vocabulary-10k/master.csv
  14_llm-papers/vocabulary-10k/dictionary-01-1000.md ... 10
  14_llm-papers/vocabulary-10k/domain-phrases.md
  14_llm-papers/vocabulary-10k/anki-*.csv
"""
import argparse
import collections
import csv
import re
import sqlite3
import subprocess
import time
from pathlib import Path

import lemminflect
from wordfreq import zipf_frequency

ROOT = Path(__file__).resolve().parent.parent
PAPER_ROOT = Path.home() / "llm-papers"
TEXT_DIR = Path.home() / "english" / "data" / "paper-text"
ECDICT = Path.home() / "english" / "data" / "ecdict.sqlite"
OUT = ROOT / "14_llm-papers" / "vocabulary-10k"

STOP = set("""
a an the and or but if while of to in on at by for from with without as is are was were be been being
this that these those it its their our we you they he she i not no can could may might should would will
shall do does did done have has had also than then there here which who whom whose what when where why how
all any both each few more most other some such only own same so too very just about into over under again
further once during before after above below up down out off between through because both more most other
some such paper papers work works study studies show shows shown using used use uses used based propose
proposes proposed present presents presented provide provides provided result results method methods approach
approaches model models task tasks data dataset datasets training train trained learn learning learned
performance figure figures table tables section sections appendix arxiv preprint et al ieee conference
proceedings pages page doi url http https github com www email authors author corresponding supplementary
supplement algorithm algorithms equation equations eq fig tab reference references introduction related
abstract keywords keyword university institute department school inc ltd copyright license permission
""".split())

BOILER = set("""
arxiv preprint figure fig table tab equation eq appendix supplementary references reference doi url http https
github conference proceedings pages page volume journal ieee acm springer elsevier copyright license email
authors author corresponding university institute department school inc ltd
neurips nips iclr icml aaai ijcai acl emnlp naacl cvpr iccv eccv jmlr tmlr openai
""".split())

TOKEN = re.compile(r"[A-Za-z][A-Za-z'\-]{2,}")
CLEAN_TRANS = re.compile(r"\[[^\]]{1,8}\]")
SENSITIVE = re.compile(r"date rape|rape drug|child sexual|porn|suicide|self-harm|how to (?:kill|attack|harm)|attack someone|mass shooting|bomb", re.I)
BLOCK = {"self-harm", "suicide", "pornographic", "pornography", "porn", "rape", "bomb", "terrorist", "terrorism", "murder", "kill", "weapon", "sex", "sexual", "nude", "drug", "drugs", "sic", "acc", "pos"}


def md_escape(text: str) -> str:
    return text.replace("[", "\\[").replace("]", "\\]")


def normalize(text: str) -> str:
    text = (text.replace("ﬁ", "fi").replace("ﬂ", "fl").replace("ﬀ", "ff")
            .replace("ﬃ", "ffi").replace("ﬄ", "ffl"))
    text = re.sub(r"-\s*\n\s*", "", text)
    return re.sub(r"\s+", " ", text)


def sentences(text: str):
    text = normalize(text)
    text = re.split(r"\n\s*(?:References|REFERENCES|Bibliography|BIBLIOGRAPHY)\s*\n", text, maxsplit=1)[0]
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(0-9])", text)
    return [p.strip() for p in parts if 20 <= len(p.strip()) <= 700]


def lemma_of(word: str) -> str:
    if word.isupper() and 2 <= len(word) <= 6:
        return word
    best = None
    for pos in ("NOUN", "VERB", "ADJ", "ADV"):
        for lem in lemminflect.getAllLemmas(word).get(pos, ()):
            z = zipf_frequency(lem, "en")
            if best is None or z > best[1]:
                best = (lem, z)
    return best[0] if best else word


def load_source_rows():
    rows = []
    for name in ("vocabulary.csv", "core-vocabulary.csv"):
        path = ROOT / "14_llm-papers" / name
        if not path.exists():
            continue
        with path.open(encoding="utf-8-sig") as fh:
            for row in csv.DictReader(fh):
                word = (row.get("word") or "").strip()
                if not word or word.lower() in BLOCK:
                    continue
                rows.append({
                    "word": word,
                    "chinese": (row.get("chinese") or "").strip(),
                    "note": "" if SENSITIVE.search(row.get("note") or row.get("context") or "") else (row.get("note") or row.get("context") or "").strip(),
                    "pos": (row.get("pos") or "").strip(),
                    "level": (row.get("level") or "").strip(),
                    "paper_id": (row.get("paper_id") or "").strip(),
                    "paper_title": (row.get("paper_title") or "").strip(),
                    "stage": (row.get("stage") or "").strip(),
                })
    return rows


def parse_papers():
    papers = {}
    for f in sorted((ROOT / "14_llm-papers").glob("stage-*.md")):
        stage = int(f.name.split("-")[1])
        for line in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^## (\d{2}-\d{2}) (.+)$", line)
            if m:
                papers[m.group(1)] = (stage, m.group(2).strip())
    return papers


def pdf_map():
    dirs = {0: "00_总览综述", 1: "01_大模型", 2: "02_多模态", 3: "03_音乐检索理解",
            4: "04_音乐生成", 5: "05_世界模型", 6: "06_强化学习"}
    result = {}
    for stage, d in dirs.items():
        for p in (PAPER_ROOT / d / "PDF").glob("*.pdf"):
            m = re.match(r"^(\d{2})_", p.name)
            if m:
                result[(stage, int(m.group(1)))] = p
    return result


def ensure_text(papers, pdfs):
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    for pid, (stage, title) in papers.items():
        out = TEXT_DIR / f"{pid}.txt"
        if out.exists() and out.stat().st_size > 500:
            continue
        p = pdfs.get((stage, int(pid.split("-")[1])))
        text = ""
        if p:
            try:
                text = subprocess.run(
                    ["pdftotext", "-layout", "-enc", "UTF-8", str(p), "-"],
                    capture_output=True, text=True, timeout=90,
                ).stdout
            except Exception:
                text = ""
        out.write_text(text, encoding="utf-8")


def clean_translation(text: str) -> str:
    if not text:
        return ""
    text = text.replace("\\n", "\n")
    lines = []
    for line in text.splitlines():
        line = CLEAN_TRANS.sub("", line).strip(" ;，,")
        if line and line not in lines:
            lines.append(line)
    return "；".join(lines[:2])[:120]


def clean_definition(text: str) -> str:
    if not text:
        return ""
    lines = [CLEAN_TRANS.sub("", l).strip() for l in text.replace("\\n", "\n").splitlines()]
    return " ".join(l for l in lines if l)[:240]


def ipa(word: str, phonetic: str) -> str:
    if " " in word:
        parts = []
        for w in word.split():
            try:
                parts.append(subprocess.run(["espeak-ng", "--ipa", "-q", w], capture_output=True, text=True, timeout=5).stdout.strip())
            except Exception:
                parts.append("")
        return " ".join(p for p in parts if p) or phonetic.strip("/ ")
    try:
        out = subprocess.run(["espeak-ng", "--ipa", "-q", word], capture_output=True, text=True, timeout=5).stdout.strip()
        if out:
            return out
    except Exception:
        pass
    return phonetic.strip("/ ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=10000)
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)

    papers = parse_papers()
    pdfs = pdf_map()
    ensure_text(papers, pdfs)

    source_rows = load_source_rows()
    source_map = {}
    for row in source_rows:
        key = row["word"].lower()
        if key and key not in source_map:
            source_map[key] = row

    tf = collections.Counter()
    upper = collections.Counter()
    docs = collections.defaultdict(set)
    stages = collections.defaultdict(set)
    sentmap = {}
    paper_lemma_sentence = {}

    for pid, (stage, title) in papers.items():
        text = (TEXT_DIR / f"{pid}.txt").read_text(encoding="utf-8", errors="ignore")
        for s in sentences(text):
            for raw in TOKEN.findall(s):
                w = raw.lower().strip("'-")
                if w.endswith("'s"):
                    w = w[:-2]
                if len(w) < 3 or w in STOP or w in BOILER:
                    continue
                lem = lemma_of(w)
                tf[lem] += 1
                if raw[:1].isupper() or raw.isupper():
                    upper[lem] += 1
                docs[lem].add(pid)
                stages[lem].add(stage)
                if lem not in sentmap and 40 <= len(s) <= 450 and not SENSITIVE.search(s):
                    sentmap[lem] = (s, pid, title)
                if (pid, lem) not in paper_lemma_sentence and 40 <= len(s) <= 600 and not SENSITIVE.search(s):
                    paper_lemma_sentence[(pid, lem)] = s

    # add source words even if the PDF text was not extractable
    for row in source_rows:
        word = row["word"]
        key = word.lower()
        if " " in word or "-" in word:
            stages[key].add(int(row["stage"]) if row["stage"].isdigit() else -1)
            docs[key].add(row["paper_id"] or "source")
            tf[key] = max(tf[key], 1)
            if key not in sentmap and row["note"]:
                sentmap[key] = (row["note"], row["paper_id"], row["paper_title"])
        else:
            lem = lemma_of(key)
            stages[lem].add(int(row["stage"]) if row["stage"].isdigit() else -1)
            docs[lem].add(row["paper_id"] or "source")
            tf[lem] = max(tf[lem], 1)
            if lem not in sentmap and row["note"]:
                sentmap[lem] = (row["note"], row["paper_id"], row["paper_title"])

    # score and select
    candidates = []
    for word, count in tf.items():
        if word in STOP or word in BOILER or word in BLOCK:
            continue
        if len(word) < 3 and not word.isupper():
            continue
        d = len(docs[word])
        if d == 0:
            continue
        z = zipf_frequency(word, "en")
        if z >= 5.5 and word.lower() not in source_map:
            continue
        score = d * 10 + min(count, 100) + z * 2
        if word.lower() in source_map:
            score += 40
        candidates.append((score, word))
    candidates.sort(reverse=True)

    con = sqlite3.connect(ECDICT)
    con.row_factory = sqlite3.Row
    tag_cache = {}
    EXAM_TAGS = {"cet4", "cet6", "ky", "toefl", "ielts", "gre", "tem4", "tem8"}
    def tag_of(word):
        if word not in tag_cache:
            r = con.execute("select tag from entries where word=? collate nocase", (word,)).fetchone()
            tag_cache[word] = (r["tag"] if r else "") or ""
        return tag_cache[word]

    FRAGMENTS = {"tional", "ments", "tions", "sion", "ically", "ization", "isation"}
    selected = []
    for _, word in candidates:
        if word in FRAGMENTS and word not in source_map:
            continue
        if word in source_map:
            selected.append(word)
        else:
            tags = set(tag_of(word).split())
            # drop author/venue names that are mostly capitalised and unknown to ECDICT
            if (word not in source_map and not tags and upper[word] >= 0.6 * tf[word]
                    and not word.isupper()):
                continue
            if tags & EXAM_TAGS or (not tags and len(docs[word]) >= 2):
                selected.append(word)
        if len(selected) >= args.limit:
            break
    selected_set = set(selected)
    # always include source core/domain terms
    for row in source_rows:
        key = row["word"].lower()
        if key not in selected_set:
            selected.append(key)
            selected_set.add(key)
    rows = []
    for rank, word in enumerate(selected, 1):
        src = source_map.get(word) or source_map.get(word.lower())
        e = con.execute(
            "select word,phonetic,definition,translation,pos,tag,bnc,frq from entries where word=? collate nocase",
            (word,),
        ).fetchone()
        if e is None and word.endswith("s"):
            e = con.execute(
                "select word,phonetic,definition,translation,pos,tag,bnc,frq from entries where word=? collate nocase",
                (word[:-1],),
            ).fetchone()
        phonetic = (e["phonetic"] if e else "") or ""
        chinese = (src["chinese"] if src and src["chinese"] else "") or (clean_translation(e["translation"]) if e else "")
        definition = clean_definition(e["definition"]) if e else ""
        tags = (e["tag"] if e else "") or ""
        base_level = "S" if rank <= 3000 else ("A" if rank <= 7000 else "B")
        level = (src["level"] if src and src["level"] in ("S", "A") else base_level)
        sentence, pid, title = sentmap.get(word, ("", "", ""))
        if not sentence and src and src["note"]:
            sentence, pid, title = src["note"], src["paper_id"], src["paper_title"]
        rows.append({
            "rank": rank,
            "word": word,
            "pos": (src["pos"] if src else "") or (e["pos"] if e else "") or "",
            "phonetic": ipa(word, phonetic),
            "chinese": chinese[:160],
            "definition": definition,
            "tags": tags,
            "level": level,
            "bnc": e["bnc"] if e else "",
            "frq": e["frq"] if e else "",
            "zipf": round(zipf_frequency(word, "en"), 2),
            "paper_freq": tf.get(word, 0),
            "doc_freq": len(docs.get(word, ())),
            "stages": ",".join(str(x) for x in sorted(stages.get(word, ())) if x >= 0),
            "sentence": sentence,
            "paper_id": pid,
            "paper_title": title,
        })

    master = OUT / "master.csv"
    with master.open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {master} rows={len(rows)}")

    # dictionary pages of 1000
    bands = [rows[i:i+1000] for i in range(0, len(rows), 1000)]
    for i, band in enumerate(bands, 1):
        lo, hi = (i - 1) * 1000 + 1, (i - 1) * 1000 + len(band)
        lines = [
            "---", "type: dictionary", f"title: 论文词库 {lo}-{hi}", "tags: [library/word-bank, skill/reading]", "---", "",
            f"# 论文词库 {lo}-{hi}", "",
            "> 音标/释义来自 ECDICT；例句来自论文原文。先读例句，再记词。", "",
        ]
        for r in band:
            tags = f" · {r['tags']}" if r["tags"] else ""
            sentence = r["sentence"].strip()
            if sentence:
                sentence = f"｜“{sentence}”"
            lines.append(
                f"- **{r['word']}** /{r['phonetic']}/ — {md_escape(r['chinese'])}（{r['level']}{tags}）{md_escape(sentence)}"
            )
        (OUT / f"dictionary-{i:02d}-{lo}-{hi}.md").write_text("\n".join(lines), encoding="utf-8")

    # domain phrases from source rows
    phrases = []
    seen = set()
    for row in source_rows:
        word = row["word"].strip()
        if (" " in word or "-" in word) and word.lower() not in seen:
            seen.add(word.lower())
            phrases.append(row)
    plines = ["---", "type: dictionary", "title: 论文领域短语", "tags: [library/word-bank, skill/reading]", "---", "",
              "# 论文领域短语", "", "> 多词术语按论文原句保留；先理解结构，再记整块。", ""]
    for row in phrases[:800]:
        plines.append(f"- **{row['word']}** — {md_escape(row['chinese'])}｜“{md_escape(row['note'])}”")
    (OUT / "domain-phrases.md").write_text("\n".join(plines), encoding="utf-8")

    # Anki chunks
    for i in range(0, len(rows), 2000):
        chunk = rows[i:i+2000]
        (OUT / f"anki-{i//2000+1:02d}.csv").write_text("﻿", encoding="utf-8")
        with (OUT / f"anki-{i//2000+1:02d}.csv").open("a", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=["word", "phonetic", "chinese", "definition", "tags", "sentence", "paper_id"])
            w.writeheader()
            for r in chunk:
                w.writerow({k: r[k] for k in w.fieldnames})

    print("stats", {
        "selected": len(rows),
        "with_sentence": sum(1 for r in rows if r["sentence"]),
        "with_chinese": sum(1 for r in rows if r["chinese"]),
        "with_definition": sum(1 for r in rows if r["definition"]),
        "phrases": len(phrases),
    })


if __name__ == "__main__":
    main()

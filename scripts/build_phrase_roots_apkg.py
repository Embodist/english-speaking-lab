#!/usr/bin/env python3
"""Build Anki decks for the 1,200-phrase bank and the word-root module.

Outputs:
  12_word-phrase-bank/11-phrase-1200/1200-phrases.apkg
  17_word-roots/word-roots.apkg
  17_word-roots/affixes.apkg
  17_word-roots/tech-words.apkg
"""
import csv
import html
from pathlib import Path

import genanki

ROOT = Path(__file__).resolve().parent.parent
PHRASE_TSV = ROOT / "12_word-phrase-bank" / "11-phrase-1200" / "data" / "phrases-1200.tsv"
ROOT_DIR = ROOT / "17_word-roots" / "data"

CSS = """
.card {
  font-family: -apple-system, "Segoe UI", "Noto Sans CJK SC", sans-serif;
  font-size: 22px; line-height: 1.5; text-align: center;
  color: #1f2328; background: #ffffff;
}
.term { font-size: 34px; font-weight: 600; margin-bottom: 8px; }
.meaning { font-size: 26px; font-weight: 600; margin: 12px 0; }
.examples { font-size: 18px; color: #57606a; margin: 10px 0; }
.note { font-size: 16px; color: #8c959f; margin-top: 10px; }
.meta { font-size: 13px; color: #8c959f; margin-top: 10px; }
hr#answer { border: 0; border-top: 1px solid #d0d7de; margin: 14px 0; }
.nightMode .card { color: #e6edf3; background: #0d1117; }
.nightMode .examples, .nightMode .note, .nightMode .meta { color: #8b949e; }
.nightMode hr#answer { border-top-color: #30363d; }
"""

PHRASE_MODEL = genanki.Model(
    1436534931,
    "Phrase (EN-ZH)",
    fields=[{"name": n} for n in ["Phrase", "Chinese", "Group"]],
    templates=[
        {
            "name": "English to Chinese",
            "qfmt": '<div class="term">{{Phrase}}</div>',
            "afmt": (
                "{{FrontSide}}<hr id=answer>"
                '<div class="meaning">{{Chinese}}</div>'
                '<div class="meta">Group {{Group}}</div>'
            ),
        },
        {
            "name": "Chinese to English",
            "qfmt": '<div class="meaning">{{Chinese}}</div>',
            "afmt": (
                "{{FrontSide}}<hr id=answer>"
                '<div class="term">{{Phrase}}</div>'
                '<div class="meta">Group {{Group}}</div>'
            ),
        },
    ],
    css=CSS,
)

ROOT_MODEL = genanki.Model(
    1436534933,
    "Word Root",
    fields=[{"name": n} for n in ["Root", "Meaning", "Examples", "Note"]],
    templates=[
        {
            "name": "Root to meaning",
            "qfmt": '<div class="term">{{Root}}</div>',
            "afmt": (
                "{{FrontSide}}<hr id=answer>"
                '<div class="meaning">{{Meaning}}</div>'
                '<div class="examples">{{Examples}}</div>'
                '<div class="note">{{Note}}</div>'
            ),
        },
    ],
    css=CSS,
)

AFFIX_MODEL = genanki.Model(
    1436534935,
    "Prefix / Suffix",
    fields=[{"name": n} for n in ["Affix", "Type", "Meaning", "Examples"]],
    templates=[
        {
            "name": "Affix to meaning",
            "qfmt": '<div class="term">{{Affix}}</div><div class="meta">{{Type}}</div>',
            "afmt": (
                "{{FrontSide}}<hr id=answer>"
                '<div class="meaning">{{Meaning}}</div>'
                '<div class="examples">{{Examples}}</div>'
            ),
        },
    ],
    css=CSS,
)

TECH_MODEL = genanki.Model(
    1436534937,
    "Tech Word Roots",
    fields=[{"name": n} for n in ["Word", "Parts", "Meaning", "Note"]],
    templates=[
        {
            "name": "Word to breakdown",
            "qfmt": '<div class="term">{{Word}}</div>',
            "afmt": (
                "{{FrontSide}}<hr id=answer>"
                '<div class="examples">{{Parts}}</div>'
                '<div class="meaning">{{Meaning}}</div>'
                '<div class="note">{{Note}}</div>'
            ),
        },
    ],
    css=CSS,
)


def load(path):
    with Path(path).open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def clean(value):
    return html.escape((value or "").strip(), quote=False)


def build(deck_id, deck_name, model, rows, field_names, tag_fn, guid_prefix, out):
    deck = genanki.Deck(deck_id, deck_name)
    count = 0
    for row in rows:
        note = genanki.Note(
            model=model,
            fields=[clean(row[name]) for name in field_names],
            tags=tag_fn(row),
            guid=genanki.guid_for(guid_prefix, row.get("id") or row["word"]),
        )
        deck.add_note(note)
        count += 1
    out.parent.mkdir(parents=True, exist_ok=True)
    genanki.Package(deck).write_to_file(out)
    print(f"{deck_name}: {count} notes -> {out.relative_to(ROOT)} ({out.stat().st_size / 1024:.0f} KB)")


def main():
    phrases = load(PHRASE_TSV)
    build(
        1436534932,
        "English Phrases 1200",
        PHRASE_MODEL,
        phrases,
        ["phrase", "zh", "group"],
        lambda row: ["phrases-1200", f"group-{int(row['group']):02d}"],
        "phrases-1200",
        ROOT / "12_word-phrase-bank" / "11-phrase-1200" / "1200-phrases.apkg",
    )

    roots = load(ROOT_DIR / "roots.tsv")
    build(
        1436534934,
        "English Word Roots",
        ROOT_MODEL,
        roots,
        ["root", "meaning", "examples", "note"],
        lambda row: ["word-roots", "core"],
        "word-roots",
        ROOT / "17_word-roots" / "word-roots.apkg",
    )

    affixes = []
    for row in load(ROOT_DIR / "prefixes.tsv"):
        affixes.append({**row, "type": "前缀", "prefix": row["prefix"]})
    for row in load(ROOT_DIR / "suffixes.tsv"):
        affixes.append({**row, "type": "后缀", "prefix": row["suffix"]})
    build(
        1436534936,
        "English Prefixes & Suffixes",
        AFFIX_MODEL,
        affixes,
        ["prefix", "type", "meaning", "examples"],
        lambda row: ["word-roots", row["type"]],
        "affixes",
        ROOT / "17_word-roots" / "affixes.apkg",
    )

    tech = load(ROOT_DIR / "tech.tsv")
    build(
        1436534938,
        "Tech Word Roots",
        TECH_MODEL,
        tech,
        ["word", "parts", "meaning", "note"],
        lambda row: ["word-roots", "tech"],
        "tech-words",
        ROOT / "17_word-roots" / "tech-words.apkg",
    )


if __name__ == "__main__":
    main()

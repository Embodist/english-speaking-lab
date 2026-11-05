#!/usr/bin/env python3
"""Build Anki decks for the 164 prefixes, 171 suffixes, and 1,798 examples.

Outputs:
  17_word-roots/prefixes.apkg
  17_word-roots/suffixes.apkg
  17_word-roots/affix-examples.apkg
"""
import csv
import html
from pathlib import Path

import genanki

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "17_word-roots" / "data"

CSS = """
.card {
  font-family: -apple-system, "Segoe UI", "Noto Sans CJK SC", sans-serif;
  font-size: 22px; line-height: 1.5; text-align: center;
  color: #1f2328; background: #ffffff;
}
.term { font-size: 34px; font-weight: 600; margin-bottom: 8px; }
.meaning { font-size: 24px; font-weight: 600; margin: 12px 0; }
.examples { font-size: 16px; color: #57606a; text-align: left; margin: 10px 0; }
.meta { font-size: 13px; color: #8c959f; margin-top: 10px; }
hr#answer { border: 0; border-top: 1px solid #d0d7de; margin: 14px 0; }
.nightMode .card { color: #e6edf3; background: #0d1117; }
.nightMode .examples, .nightMode .meta { color: #8b949e; }
.nightMode hr#answer { border-top-color: #30363d; }
"""

AFFIX_MODEL = genanki.Model(
    1436534951,
    "Affix (prefix/suffix)",
    fields=[{"name": n} for n in ["Form", "Type", "Meaning", "Examples"]],
    templates=[
        {
            "name": "Affix to meaning",
            "qfmt": '<div class="term">{{Form}}</div><div class="meta">{{Type}}</div>',
            "afmt": (
                "{{FrontSide}}<hr id=answer>"
                '<div class="meaning">{{Meaning}}</div>'
                '<div class="examples">{{Examples}}</div>'
            ),
        },
    ],
    css=CSS,
)

EXAMPLE_MODEL = genanki.Model(
    1436534953,
    "Affix example",
    fields=[{"name": n} for n in ["Word", "Form", "Meaning", "POS", "Chinese"]],
    templates=[
        {
            "name": "Word to affix",
            "qfmt": '<div class="term">{{Word}}</div>',
            "afmt": (
                "{{FrontSide}}<hr id=answer>"
                '<div class="meaning">{{Form}} · {{Meaning}}</div>'
                '<div class="meta">{{POS}} {{Chinese}}</div>'
            ),
        },
    ],
    css=CSS,
)


def load(name):
    with (DATA / name).open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def clean(value):
    return html.escape((value or "").strip(), quote=False)


def build_affix_deck(kind, rows, examples_by_affix, deck_id, deck_name, out):
    deck = genanki.Deck(deck_id, deck_name)
    for row in rows:
        items = examples_by_affix.get(row["id"], [])
        examples = ", ".join(
            f"{x['word']} ({x['pos']} {x['zh']})".strip() for x in items
        )
        deck.add_note(
            genanki.Note(
                model=AFFIX_MODEL,
                fields=[clean(row["form"]), clean(kind), clean(row["meaning"]), clean(examples)],
                tags=["affixes-335", kind],
                guid=genanki.guid_for("affixes-335", row["id"]),
            )
        )
    genanki.Package(deck).write_to_file(out)
    print(f"{deck_name}: {len(rows)} notes -> {out.relative_to(ROOT)} ({out.stat().st_size / 1024:.0f} KB)")


def main():
    affixes = load("affixes.tsv")
    examples = load("affix-examples.tsv")
    by_affix = {}
    for row in examples:
        by_affix.setdefault(row["affix_id"], []).append(row)

    prefixes = [row for row in affixes if row["type"] == "prefix"]
    suffixes = [row for row in affixes if row["type"] == "suffix"]
    build_affix_deck(
        "prefix", prefixes, by_affix, 1436534952,
        "English Prefixes 164", ROOT / "17_word-roots" / "prefixes.apkg",
    )
    build_affix_deck(
        "suffix", suffixes, by_affix, 1436534954,
        "English Suffixes 171", ROOT / "17_word-roots" / "suffixes.apkg",
    )

    deck = genanki.Deck(1436534956, "Affix Examples 1798")
    for row in examples:
        deck.add_note(
            genanki.Note(
                model=EXAMPLE_MODEL,
                fields=[
                    clean(row["word"]), clean(row["form"]), clean(row["meaning"]),
                    clean(row["pos"]), clean(row["zh"]),
                ],
                tags=["affixes-335", "examples", row["type"]],
                guid=genanki.guid_for("affix-examples", row["id"]),
            )
        )
    out = ROOT / "17_word-roots" / "affix-examples.apkg"
    genanki.Package(deck).write_to_file(out)
    print(f"Affix Examples: {len(examples)} notes -> {out.relative_to(ROOT)} ({out.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()

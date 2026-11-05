#!/usr/bin/env python3
"""Build the Anki deck for the 1,200-scene-sentence library.

Output: 08_sentence-library/1200-sentences/1200-sentences.apkg
"""
import csv
import html
from pathlib import Path

import genanki

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "08_sentence-library" / "1200-sentences" / "data" / "sentences-1200.tsv"
OUT = DATA.parent.parent / "1200-sentences.apkg"

CSS = """
.card {
  font-family: -apple-system, "Segoe UI", "Noto Sans CJK SC", sans-serif;
  font-size: 22px; line-height: 1.5; text-align: center;
  color: #1f2328; background: #ffffff;
}
.term { font-size: 30px; font-weight: 600; margin-bottom: 8px; }
.meaning { font-size: 26px; font-weight: 600; margin: 12px 0; }
.meta { font-size: 13px; color: #8c959f; margin-top: 10px; }
hr#answer { border: 0; border-top: 1px solid #d0d7de; margin: 14px 0; }
.nightMode .card { color: #e6edf3; background: #0d1117; }
.nightMode .meta { color: #8b949e; }
.nightMode hr#answer { border-top-color: #30363d; }
"""

MODEL = genanki.Model(
    1436534941,
    "Sentence (EN-ZH)",
    fields=[{"name": n} for n in ["English", "Chinese", "Category", "Section"]],
    templates=[
        {
            "name": "Chinese to English",
            "qfmt": '<div class="meaning">{{Chinese}}</div>',
            "afmt": (
                "{{FrontSide}}<hr id=answer>"
                '<div class="term">{{English}}</div>'
                '<div class="meta">{{Category}} · {{Section}}</div>'
            ),
        },
        {
            "name": "English to Chinese",
            "qfmt": '<div class="term">{{English}}</div>',
            "afmt": (
                "{{FrontSide}}<hr id=answer>"
                '<div class="meaning">{{Chinese}}</div>'
                '<div class="meta">{{Category}} · {{Section}}</div>'
            ),
        },
    ],
    css=CSS,
)


def clean(value):
    return html.escape((value or "").strip(), quote=False)


def main():
    with DATA.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    deck = genanki.Deck(1436534942, "English 1200 Sentences")
    for row in rows:
        deck.add_note(
            genanki.Note(
                model=MODEL,
                fields=[
                    clean(row["english"]),
                    clean(row["chinese"]),
                    clean(row["category"]),
                    clean(row["section"]),
                ],
                tags=["sentences-1200", f"category-{int(row['category_no']):02d}"],
                guid=genanki.guid_for("sentences-1200", row["id"]),
            )
        )
    genanki.Package(deck).write_to_file(OUT)
    print(f"English 1200 Sentences: {len(rows)} notes -> {OUT.relative_to(ROOT)} ({OUT.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build Anki packages from the vocabulary CSVs.

Outputs:
  14_llm-papers/vocabulary-10k/10k-paper-vocabulary.apkg
  14_llm-papers/core-vocabulary.apkg
  14_llm-papers/vocabulary-dedup.apkg
  14_llm-papers/vocabulary.apkg
"""
import csv
import html
import re
from pathlib import Path

import genanki

ROOT = Path(__file__).resolve().parent.parent
VOCAB_DIR = ROOT / "14_llm-papers" / "vocabulary-10k"
PAPERS = ROOT / "14_llm-papers"
CTRL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")

CSS = """
.card {
  font-family: -apple-system, "Segoe UI", "Noto Sans CJK SC", sans-serif;
  font-size: 20px; line-height: 1.5; text-align: center;
  color: #1f2328; background: #ffffff;
}
.word { font-size: 34px; font-weight: 600; margin-bottom: 6px; }
.phonetic { color: #57606a; font-size: 18px; margin-bottom: 16px; }
.pos { color: #57606a; font-size: 18px; margin-bottom: 16px; font-style: italic; }
.meaning { font-size: 24px; font-weight: 600; margin: 12px 0; }
.def { font-size: 16px; color: #57606a; text-align: left; margin: 10px 0; }
.note { font-size: 16px; color: #57606a; text-align: left; margin: 10px 0; }
.sentence {
  font-size: 16px; font-style: italic; text-align: left;
  border-left: 3px solid #d0d7de; padding-left: 10px; margin: 12px 0;
}
.meta { font-size: 12px; color: #8c959f; }
hr#answer { border: 0; border-top: 1px solid #d0d7de; margin: 14px 0; }
.nightMode .card { color: #e6edf3; background: #0d1117; }
.nightMode .phonetic, .nightMode .def, .nightMode .note { color: #8b949e; }
.nightMode .sentence { border-left-color: #30363d; }
.nightMode .meta { color: #6e7681; }
.nightMode hr#answer { border-top-color: #30363d; }
"""

MODEL_10K = genanki.Model(
    1436534921,
    "Vocab (10k papers)",
    fields=[{"name": n} for n in ["Word", "Phonetic", "Chinese", "Definition", "Sentence", "PaperID"]],
    templates=[
        {
            "name": "Word to Meaning",
            "qfmt": (
                '<div class="word">{{Word}}</div>'
                '{{#Phonetic}}<div class="phonetic">/{{Phonetic}}/</div>{{/Phonetic}}'
            ),
            "afmt": (
                "{{FrontSide}}"
                '<hr id="answer">'
                '<div class="meaning">{{Chinese}}</div>'
                '{{#Definition}}<div class="def">{{Definition}}</div>{{/Definition}}'
                '{{#Sentence}}<div class="sentence">{{Sentence}}</div>{{/Sentence}}'
                '{{#PaperID}}<div class="meta">{{PaperID}}</div>{{/PaperID}}'
            ),
        }
    ],
    css=CSS,
)

MODEL_CORE = genanki.Model(
    1436534923,
    "Vocab (core academic)",
    fields=[{"name": n} for n in ["Word", "Chinese", "Note", "Type", "Category", "Level"]],
    templates=[
        {
            "name": "Word to Meaning",
            "qfmt": '<div class="word">{{Word}}</div>',
            "afmt": (
                "{{FrontSide}}"
                '<hr id="answer">'
                '<div class="meaning">{{Chinese}}</div>'
                '{{#Note}}<div class="note">{{Note}}</div>{{/Note}}'
                '<div class="meta">{{Category}} · 级别 {{Level}}</div>'
            ),
        }
    ],
    css=CSS,
)


MODEL_DEDUP = genanki.Model(
    1436534925,
    "Vocab (paper words)",
    fields=[{"name": n} for n in [
        "Word", "POS", "Chinese", "Context", "Frequency",
        "Level", "Papers", "Stage", "PaperID", "PaperTitle",
    ]],
    templates=[
        {
            "name": "Word to Meaning",
            "qfmt": (
                '<div class="word">{{Word}}</div>'
                '{{#POS}}<div class="pos">{{POS}}</div>{{/POS}}'
            ),
            "afmt": (
                "{{FrontSide}}"
                '<hr id="answer">'
                '<div class="meaning">{{Chinese}}</div>'
                '{{#Context}}<div class="sentence">{{Context}}</div>{{/Context}}'
                '<div class="meta">出现 {{Frequency}} 次 · {{Papers}} 篇论文 · 级别 {{Level}} · 阶段 {{Stage}}</div>'
                '{{#PaperTitle}}<div class="meta">{{PaperTitle}}</div>{{/PaperTitle}}'
            ),
        }
    ],
    css=CSS,
)

MODEL_EXT = genanki.Model(
    1436534927,
    "Vocab (paper context)",
    fields=[{"name": n} for n in [
        "Word", "POS", "Chinese", "Context", "Stage",
        "PaperID", "PaperTitle", "Frequency", "Level",
    ]],
    templates=[
        {
            "name": "Word to Meaning",
            "qfmt": (
                '<div class="word">{{Word}}</div>'
                '{{#POS}}<div class="pos">{{POS}}</div>{{/POS}}'
            ),
            "afmt": (
                "{{FrontSide}}"
                '<hr id="answer">'
                '<div class="meaning">{{Chinese}}</div>'
                '{{#Context}}<div class="sentence">{{Context}}</div>{{/Context}}'
                '<div class="meta">{{PaperID}} · {{PaperTitle}}</div>'
                '<div class="meta">级别 {{Level}} · 阶段 {{Stage}} · 频次 {{Frequency}}</div>'
            ),
        }
    ],
    css=CSS,
)


def clean(value):
    return html.escape(CTRL.sub("", value or "").strip(), quote=False)


def clean_context(value):
    text = CTRL.sub("", value or "").strip()
    if len(text) > 2 and text.startswith('"') and text.endswith('"'):
        text = text[1:-1].strip()
    return html.escape(text, quote=False)


def build_10k():
    deck = genanki.Deck(1436534922, "10k Paper Vocabulary")
    columns = ["word", "phonetic", "chinese", "definition", "sentence", "paper_id"]
    count = 0
    for path in sorted(VOCAB_DIR.glob("anki-*.csv")):
        with path.open(newline="", encoding="utf-8-sig") as fh:
            for row in csv.DictReader(fh):
                word = (row["word"] or "").strip()
                if not word:
                    continue
                deck.add_note(
                    genanki.Note(
                        model=MODEL_10K,
                        fields=[clean(row[col]) for col in columns],
                        tags=sorted(set((row["tags"] or "").split())),
                        guid=genanki.guid_for("10k-paper-vocab", word),
                    )
                )
                count += 1
    out = VOCAB_DIR / "10k-paper-vocabulary.apkg"
    genanki.Package(deck).write_to_file(out)
    print(f"10k:   {count} notes -> {out} ({out.stat().st_size / 1_048_576:.1f} MB)")


def build_core():
    deck = genanki.Deck(1436534924, "Core Academic")
    columns = ["word", "chinese", "note", "type", "category", "level"]
    count = 0
    with (PAPERS / "core-vocabulary.csv").open(newline="", encoding="utf-8-sig") as fh:
        for row in csv.DictReader(fh):
            word = (row["word"] or "").strip()
            if not word:
                continue
            tags = ["core-vocab", row["type"], f"level-{row['level']}"]
            deck.add_note(
                genanki.Note(
                    model=MODEL_CORE,
                    fields=[clean(row[col]) for col in columns],
                    tags=sorted({t for t in tags if t}),
                    guid=genanki.guid_for(
                        "core-vocab", word, row["category"], row["chinese"].strip()
                    ),
                )
            )
            count += 1
    out = PAPERS / "core-vocabulary.apkg"
    genanki.Package(deck).write_to_file(out)
    print(f"core:  {count} notes -> {out} ({out.stat().st_size / 1_048_576:.1f} MB)")


def build_dedup():
    deck = genanki.Deck(1436534926, "Paper Words")
    columns = [
        "word", "pos", "chinese", "context", "freq",
        "level", "papers", "stage", "paper_id", "paper_title",
    ]
    count = 0
    with (PAPERS / "vocabulary-dedup.csv").open(newline="", encoding="utf-8-sig") as fh:
        for row in csv.DictReader(fh):
            word = (row["word"] or "").strip()
            if not word:
                continue
            fields = [clean(row[col]) for col in columns]
            fields[columns.index("context")] = clean_context(row["context"])
            deck.add_note(
                genanki.Note(
                    model=MODEL_DEDUP,
                    fields=fields,
                    tags=sorted({f"level-{row['level']}", f"stage-{row['stage']}"}),
                    guid=genanki.guid_for("paper-words", word),
                )
            )
            count += 1
    out = PAPERS / "vocabulary-dedup.apkg"
    genanki.Package(deck).write_to_file(out)
    print(f"dedup: {count} notes -> {out} ({out.stat().st_size / 1_048_576:.1f} MB)")


def build_extended():
    deck = genanki.Deck(1436534928, "Paper Context")
    columns = [
        "word", "pos", "chinese", "context", "stage",
        "paper_id", "paper_title", "freq", "level",
    ]
    count = 0
    with (PAPERS / "vocabulary.csv").open(newline="", encoding="utf-8-sig") as fh:
        for row in csv.DictReader(fh):
            word = (row["word"] or "").strip()
            if not word:
                continue
            fields = [clean(row[col]) for col in columns]
            fields[columns.index("context")] = clean_context(row["context"])
            deck.add_note(
                genanki.Note(
                    model=MODEL_EXT,
                    fields=fields,
                    tags=sorted({
                        f"level-{row['level']}",
                        f"stage-{row['stage']}",
                        f"paper-{row['paper_id']}",
                    }),
                    guid=genanki.guid_for("paper-context", word, row["paper_id"]),
                )
            )
            count += 1
    out = PAPERS / "vocabulary.apkg"
    genanki.Package(deck).write_to_file(out)
    print(f"ext:   {count} notes -> {out} ({out.stat().st_size / 1_048_576:.1f} MB)")


def main():
    build_10k()
    build_core()
    build_dedup()
    build_extended()


if __name__ == "__main__":
    main()

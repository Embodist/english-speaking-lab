#!/usr/bin/env python3
"""Interactive drills for sentences, phrases, affixes, and FSI patterns.

Examples:
  study.py sentence --n 20                  # Chinese -> English
  study.py sentence --n 20 --reverse        # English -> Chinese
  study.py sentence --category 1 --n 20
  study.py phrase --n 20                    # basic phrases
  study.py phrase --featured --n 10
  study.py affix --type prefix --n 10       # prefix -> meaning
  study.py affix --type suffix --n 10
  study.py affix --examples --n 10          # word -> affix
  study.py fsi --set sub --n 10
  study.py fsi --set resp --n 5 --tts
"""
import argparse
import csv
import random
import shutil
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
SENTENCE_TSV = ROOT / "08_sentence-library" / "1200-sentences" / "data" / "sentences-1200.tsv"
PHRASE_TSV = ROOT / "12_word-phrase-bank" / "11-basic-phrases" / "data" / "phrases-1200.tsv"
AFFIX_TSV = ROOT / "17_word-roots" / "data" / "affixes.tsv"
AFFIX_EX_TSV = ROOT / "17_word-roots" / "data" / "affix-examples.tsv"
FSI_TSV = ROOT / "18_fsi-drills" / "data" / "drills.tsv"


def load_tsv(path):
    with Path(path).open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def pick(rows, count, seed):
    rng = random.Random(seed)
    rows = list(rows)
    rng.shuffle(rows)
    return rows[:count]


def speak(text, play):
    proc = subprocess.run(
        [str(SCRIPTS / "tts.sh"), text],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        print(f"  ! TTS failed: {(proc.stderr or proc.stdout).strip()}", file=sys.stderr)
        return
    audio = proc.stdout.strip()
    print(f"  audio: {audio}")
    if play and shutil.which("ffplay"):
        subprocess.run(
            ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", audio],
            check=False,
        )


def run_pairs(items, no_input, tts, play):
    done = 0
    for number, (front, back, hint, speak_text) in enumerate(items, 1):
        print(f"\n[{number}/{len(items)}] {front}")
        if hint:
            print(f"  {hint}")
        if no_input:
            print(f"  → {back}")
            done += 1
            continue
        try:
            answer = input("  Enter 看答案 / q 退出: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if answer == "q":
            break
        print(f"  → {back}")
        if tts:
            speak(speak_text or back, play)
        done += 1
    print(f"\n完成 {done} 条。下一步：选 2 条写进今天的日志或 Slack。")


def cmd_sentence(args):
    rows = load_tsv(SENTENCE_TSV)
    if args.category:
        rows = [row for row in rows if int(row["category_no"]) == args.category]
    if not rows:
        raise SystemExit("no sentences matched the filter")

    items = []
    for row in pick(rows, args.n, args.seed):
        hint = f"{row['category']} · {row['section']}"
        if args.reverse:
            items.append((row["english"], row["chinese"], hint, row["english"]))
        else:
            items.append((row["chinese"], row["english"], hint, row["english"]))
    run_pairs(items, args.no_input, args.tts, args.play)


def cmd_phrase(args):
    rows = load_tsv(PHRASE_TSV)
    if args.featured:
        from build_phrase_1200 import FEATURED

        wanted = {phrase.lower() for items in FEATURED.values() for phrase in items}
        rows = [row for row in rows if row["phrase"].lower() in wanted]
    if args.group:
        rows = [row for row in rows if int(row["group"]) == args.group]
    if not rows:
        raise SystemExit("no phrases matched the filter")

    items = []
    for row in pick(rows, args.n, args.seed):
        if args.reverse:
            items.append((row["phrase"], row["zh"], "", row["phrase"]))
        else:
            items.append((row["zh"], row["phrase"], "", row["phrase"]))
    run_pairs(items, args.no_input, args.tts, args.play)


def cmd_affix(args):
    affixes = load_tsv(AFFIX_TSV)
    examples = load_tsv(AFFIX_EX_TSV)
    if args.type != "all":
        affixes = [row for row in affixes if row["type"] == args.type]
        examples = [row for row in examples if row["type"] == args.type]
    if not affixes:
        raise SystemExit("no affixes matched the filter")

    by_affix = {}
    for row in examples:
        by_affix.setdefault(row["affix_id"], []).append(row)

    items = []
    if args.examples:
        for row in pick(examples, args.n, args.seed):
            back = f"{row['form']} · {row['meaning']} · {row['pos']} {row['zh']}".strip()
            items.append((row["word"], back, f"{row['type']} 例词", row["word"]))
    else:
        for row in pick(affixes, args.n, args.seed):
            sample = by_affix.get(row["id"], [])[:2]
            sample_text = ", ".join(x["word"] for x in sample)
            hint = "前缀" if row["type"] == "prefix" else "后缀"
            if args.reverse:
                items.append((row["meaning"], f"{row['form']} · e.g. {sample_text}", hint, sample_text))
            else:
                items.append((row["form"], f"{row['meaning']} · e.g. {sample_text}", hint, sample_text))
    run_pairs(items, args.no_input, args.tts, args.play)


def cmd_fsi(args):
    rows = load_tsv(FSI_TSV)
    if args.set != "all":
        rows = [row for row in rows if row["set"] == args.set]
    if not rows:
        raise SystemExit("no drills matched the filter")

    items = []
    for row in pick(rows, args.n, args.seed):
        hint = f"句型: {row['hint']}" if row["hint"] else ""
        items.append((row["prompt"], row["answer"], hint, row["answer"]))
    run_pairs(items, args.no_input, args.tts, args.play)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("sentence", help="practice the 1,200-scene-sentence library")
    p.add_argument("--n", type=int, default=20)
    p.add_argument("--category", type=int, help="only this category number (1-10)")
    p.add_argument("--reverse", action="store_true", help="English -> Chinese")
    p.add_argument("--tts", action="store_true")
    p.add_argument("--play", action="store_true")
    p.add_argument("--seed", type=int)
    p.add_argument("--no-input", action="store_true")
    p.set_defaults(func=cmd_sentence)

    p = sub.add_parser("phrase", help="practice the basic phrase bank")
    p.add_argument("--n", type=int, default=20)
    p.add_argument("--group", type=int, help="only this Group number (1-31)")
    p.add_argument("--featured", action="store_true", help="work-focused 90 phrases")
    p.add_argument("--reverse", action="store_true", help="English -> Chinese")
    p.add_argument("--tts", action="store_true")
    p.add_argument("--play", action="store_true")
    p.add_argument("--seed", type=int)
    p.add_argument("--no-input", action="store_true")
    p.set_defaults(func=cmd_phrase)

    p = sub.add_parser("affix", help="practice prefixes, suffixes, or example words")
    p.add_argument("--type", choices=["prefix", "suffix", "all"], default="all")
    p.add_argument("--examples", action="store_true", help="word -> affix drill")
    p.add_argument("--reverse", action="store_true", help="meaning -> affix")
    p.add_argument("--n", type=int, default=10)
    p.add_argument("--tts", action="store_true")
    p.add_argument("--play", action="store_true")
    p.add_argument("--seed", type=int)
    p.add_argument("--no-input", action="store_true")
    p.set_defaults(func=cmd_affix)

    p = sub.add_parser("fsi", help="run FSI-style pattern drills")
    p.add_argument("--set", choices=["sub", "trans", "resp", "situation", "all"], default="resp")
    p.add_argument("--n", type=int, default=10)
    p.add_argument("--tts", action="store_true")
    p.add_argument("--play", action="store_true")
    p.add_argument("--seed", type=int)
    p.add_argument("--no-input", action="store_true")
    p.set_defaults(func=cmd_fsi)

    args = parser.parse_args()
    try:
        args.func(args)
    except KeyboardInterrupt:
        print()
        return 130
    return 0


if __name__ == "__main__":
    sys.exit(main())

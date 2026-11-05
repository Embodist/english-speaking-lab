#!/usr/bin/env python3
"""Interactive drills for phrases, word roots, and FSI patterns.

Examples:
  study.py phrase --n 20                 # Chinese -> English
  study.py phrase --n 20 --reverse       # English -> Chinese
  study.py phrase --group 3 --n 20
  study.py phrase --featured --n 10
  study.py root --n 10                   # root -> meaning
  study.py root --n 10 --reverse
  study.py root --tech --n 10
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
PHRASE_TSV = ROOT / "12_word-phrase-bank" / "11-phrase-1200" / "data" / "phrases-1200.tsv"
ROOT_DIR = ROOT / "17_word-roots" / "data"
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
    for number, (front, back, hint) in enumerate(items, 1):
        print(f"\n[{number}/{len(items)}] {front}")
        if hint:
            print(f"  句型: {hint}")
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
            speak(back, play)
        done += 1
    print(f"\n完成 {done} 条。下一步：选 2 条写进今天的日志或 Slack。")


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
            items.append((row["phrase"], row["zh"], ""))
        else:
            items.append((row["zh"], row["phrase"], ""))
    run_pairs(items, args.no_input, args.tts, args.play)


def cmd_root(args):
    name = "tech.tsv" if args.tech else "roots.tsv"
    rows = load_tsv(ROOT_DIR / name)
    items = []
    for row in pick(rows, args.n, args.seed):
        if args.tech:
            if args.reverse:
                items.append((row["meaning"], f"{row['word']} = {row['parts']}", ""))
            else:
                items.append((row["word"], f"{row['parts']} → {row['meaning']}", ""))
        elif args.reverse:
            items.append((row["meaning"], f"{row['root']} · {row['examples']}", ""))
        else:
            items.append((row["root"], f"{row['meaning']} · {row['examples']}", ""))
    run_pairs(items, args.no_input, args.tts, args.play)


def cmd_fsi(args):
    rows = load_tsv(FSI_TSV)
    if args.set != "all":
        rows = [row for row in rows if row["set"] == args.set]
    if not rows:
        raise SystemExit("no drills matched the filter")

    items = []
    for row in pick(rows, args.n, args.seed):
        items.append((row["prompt"], row["answer"], row["hint"]))
    run_pairs(items, args.no_input, args.tts, args.play)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("phrase", help="practice the 1,200-phrase bank")
    p.add_argument("--n", type=int, default=20)
    p.add_argument("--group", type=int, help="only this Group number (1-31)")
    p.add_argument("--featured", action="store_true", help="work-focused 90 phrases")
    p.add_argument("--reverse", action="store_true", help="English -> Chinese")
    p.add_argument("--tts", action="store_true", help="generate audio for each answer")
    p.add_argument("--play", action="store_true", help="play generated audio with ffplay")
    p.add_argument("--seed", type=int, help="reproducible shuffle")
    p.add_argument("--no-input", action="store_true", help="print answers without prompting")
    p.set_defaults(func=cmd_phrase)

    p = sub.add_parser("root", help="practice word roots or tech words")
    p.add_argument("--n", type=int, default=10)
    p.add_argument("--tech", action="store_true", help="use the tech-word dataset")
    p.add_argument("--reverse", action="store_true", help="meaning -> root/word")
    p.add_argument("--tts", action="store_true")
    p.add_argument("--play", action="store_true")
    p.add_argument("--seed", type=int)
    p.add_argument("--no-input", action="store_true")
    p.set_defaults(func=cmd_root)

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

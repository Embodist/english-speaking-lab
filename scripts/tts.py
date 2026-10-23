#!/usr/bin/env python3
"""Generate a reference WAV with the local Piper voice.

Usage: .venv/bin/python scripts/tts.py "Sentence to speak" [-o out.wav]
"""
import argparse
import os
import sys
from pathlib import Path

os.environ.setdefault("OPENPRONOUNCE_TTS", "piper")
os.environ.setdefault("OPENPRONOUNCE_TTS_VOICE", "en_US-lessac-medium")

from openpronounce.audio import text2speech

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DIR = ROOT / "11_attachments" / "reference"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("text", help="sentence to synthesize")
    parser.add_argument("-o", "--out", help="output wav path")
    args = parser.parse_args()

    if args.out:
        out = Path(args.out).expanduser().resolve()
    else:
        DEFAULT_DIR.mkdir(parents=True, exist_ok=True)
        slug = "".join(c if c.isalnum() else "-" for c in args.text.lower())[:40].strip("-")
        out = DEFAULT_DIR / f"{slug}.wav"

    out.parent.mkdir(parents=True, exist_ok=True)
    path = text2speech(args.text, "en", filename=str(out))
    print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())

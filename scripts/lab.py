#!/usr/bin/env python3
"""Unified English practice pipeline: TTS + ASR + pronunciation + report.

Examples:
  lab analyze recording.wav "I haven't identified the root cause yet."
  lab analyze recording.wav "Sentence." --engine both
  lab tts "Sentence to read"
  lab asr recording.wav --engine vosk
  lab pronounce recording.wav "Sentence."
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
REPORTS = ROOT / "07_review-log" / "reports"
ATTACH = ROOT / "11_attachments"

os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")
_HF = Path.home() / ".cache" / "huggingface" / "hub"
if (_HF / "models--facebook--wav2vec2-large-960h").is_dir() and (_HF / "models--rhasspy--piper-voices").is_dir():
    # Cached models: skip slow online HEAD checks.
    os.environ.setdefault("HF_HUB_OFFLINE", "1")


def run(cmd, **kwargs):
    proc = subprocess.run(cmd, capture_output=True, text=True, **kwargs)
    if proc.returncode != 0:
        msg = (proc.stderr or proc.stdout or "").strip()
        raise RuntimeError(f"command failed ({proc.returncode}): {' '.join(map(str, cmd))}\n{msg}")
    return proc.stdout.strip()


def slugify(text, limit=48):
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return (slug or "sentence")[:limit].strip("-")


def rel(path):
    path = Path(path)
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def generate_tts(sentence):
    out = run([str(SCRIPTS / "tts.sh"), sentence])
    return Path(out).resolve()


def transcribe(audio, engine):
    return run([str(SCRIPTS / "asr.sh"), str(audio), "--engine", engine])


def analyze_pronunciation(audio, sentence):
    raw = run([str(SCRIPTS / "pronounce.sh"), str(audio), sentence, "--json"])
    return json.loads(raw)


def write_report(sentence, audio, reference, asr, pron, engines):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    stamp = now.strftime("%H%M%S")
    REPORTS.mkdir(parents=True, exist_ok=True)

    diffs = pron.get("differences", {})
    errors = diffs.get("errors", [])
    error_words = [e.get("word", "") for e in errors if e.get("word")]
    heard = diffs.get("heard_phones", [])
    score = pron.get("score")

    report = REPORTS / f"{date}_{stamp}_{slugify(sentence)}.md"
    asr_rows = "\n".join(f"| {name} | {text or '(empty)'} |" for name, text in asr.items())
    error_rows = "\n".join(
        f"| {e.get('word','')} | /{e.get('expected','')}/ | /{e.get('actual','')}/ |"
        for e in errors
    ) or "| - | - | - |"
    heard_text = " ".join(heard)

    content = f"""---
type: report
title: "练习报告 {date} {now.strftime('%H:%M')}"
sentence: {json.dumps(sentence, ensure_ascii=False)}
audio: "{rel(audio)}"
reference: "{rel(reference) if reference else ''}"
engine: "{','.join(engines)}"
score: {score}
tags: [status/learning, skill/pronunciation]
created: {date}
---

# 练习报告 · {now.strftime('%Y-%m-%d %H:%M')}

## 句子

> {sentence}

## 结果

| 项目 | 值 |
|---|---|
| OpenPronounce 分数 | {score} |
| 转写 | {pron.get('transcribe','')} |
| 识别音素 | /{heard_text}/ |
| 误发音词 | {', '.join(error_words) if error_words else '无'} |

## ASR 可懂度

| 引擎 | 转写 |
|---|---|
{asr_rows}

## 音素错误

| 词 | 期望 | 实际 |
|---|---|---|
{error_rows}

## 文件

- 我的录音：`{rel(audio)}`
- 参考音：`{rel(reference) if reference else '(未生成)'}`

## 下一步

- [ ] 只选 1–2 个最影响理解的问题
- [ ] 重录一次并对比
- [ ] 把问题记到 [[01_pronunciation/error-notebook|发音错题本]]

## 相关

- [[07_review-log/{date}|{date} 练习记录]]
"""
    report.write_text(content, encoding="utf-8")

    daily = ROOT / "07_review-log" / f"{date}.md"
    if not daily.exists():
        subprocess.run([str(SCRIPTS / "new-day.sh"), date], stdout=subprocess.DEVNULL)
    if daily.exists():
        text = daily.read_text(encoding="utf-8")
        marker = "## 自动记录"
        if marker not in text:
            text = text.rstrip() + f"\n\n{marker}\n"
        link = report.relative_to(ROOT).with_suffix("").as_posix()
        text += f"- {now.strftime('%H:%M')} [[{link}|{sentence[:40]}]] · score {score}\n"
        daily.write_text(text, encoding="utf-8")

    return report


def cmd_analyze(args):
    audio = Path(args.audio).expanduser().resolve()
    if not audio.exists():
        raise SystemExit(f"audio not found: {audio}")
    sentence = args.sentence.strip()
    if not sentence:
        raise SystemExit("sentence is empty")

    if not audio.is_relative_to(ROOT):
        ATTACH.mkdir(parents=True, exist_ok=True)
        dest = ATTACH / "recordings" / f"{datetime.now():%Y-%m-%d_%H%M%S}_{slugify(sentence)}.wav"
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(audio, dest)
        audio = dest

    reference = None if args.no_tts else generate_tts(sentence)
    engines = ["whisper", "vosk"] if args.engine == "both" else [args.engine]
    asr = {engine: transcribe(audio, engine) for engine in engines}
    pron = analyze_pronunciation(audio, sentence)

    report = None
    if not args.no_save:
        report = write_report(sentence, audio, reference, asr, pron, engines)

    summary = {
        "sentence": sentence,
        "audio": rel(audio),
        "reference": rel(reference) if reference else None,
        "score": pron.get("score"),
        "transcription": pron.get("transcribe"),
        "asr": asr,
        "mispronounced": [e.get("word") for e in pron.get("differences", {}).get("errors", [])],
        "report": rel(report) if report else None,
    }

    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return

    print(f"Sentence      : {sentence}")
    print(f"Score         : {pron.get('score')}")
    print(f"Transcription : {pron.get('transcribe')}")
    for engine, text in asr.items():
        print(f"ASR ({engine:6}): {text}")
    errors = summary["mispronounced"]
    print(f"Mispronounced : {', '.join(errors) if errors else 'none'}")
    if report:
        print(f"Report        : {rel(report)}")
        print(f"Daily log     : 07_review-log/{datetime.now():%Y-%m-%d}.md")


def passthrough(script, args):
    return subprocess.call([str(SCRIPTS / script), *args])


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("analyze", help="TTS + ASR + pronunciation + report")
    p.add_argument("audio")
    p.add_argument("sentence")
    p.add_argument("--engine", choices=["whisper", "vosk", "both"], default="whisper")
    p.add_argument("--no-tts", action="store_true", help="skip reference audio generation")
    p.add_argument("--no-save", action="store_true", help="do not write a report or daily log entry")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_analyze)

    p = sub.add_parser("tts", help="generate reference audio with Piper")
    p.add_argument("args", nargs=argparse.REMAINDER)
    p.set_defaults(func=lambda a: passthrough("tts.sh", a.args))

    p = sub.add_parser("asr", help="transcribe audio (Whisper or Vosk)")
    p.add_argument("args", nargs=argparse.REMAINDER)
    p.set_defaults(func=lambda a: passthrough("asr.sh", a.args))

    p = sub.add_parser("pronounce", help="phoneme-level pronunciation analysis")
    p.add_argument("args", nargs=argparse.REMAINDER)
    p.set_defaults(func=lambda a: passthrough("pronounce.sh", a.args))

    p = sub.add_parser("translate", help="Chinese -> English draft (Hy-MT2, GPU)")
    p.add_argument("args", nargs=argparse.REMAINDER)
    p.set_defaults(func=lambda a: passthrough("translate.sh", a.args))

    p = sub.add_parser("status", help="run environment check")
    p.set_defaults(func=lambda a: passthrough("check-env.sh", []))

    args = parser.parse_args()
    try:
        return args.func(args) or 0
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

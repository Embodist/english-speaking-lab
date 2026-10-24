#!/usr/bin/env python3
"""Transcribe a recording to check intelligibility.

Usage:
  .venv/bin/python scripts/asr.py recording.wav            # Whisper base.en
  .venv/bin/python scripts/asr.py recording.wav --engine vosk
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VOSK_DEFAULT = ROOT.parent / "models" / "vosk-model-small-en-us-0.15"


def transcribe_whisper(path: Path) -> str:
    import torch
    import whisper

    if torch.cuda.is_available() and os.environ.get("WHISPER_DEVICE", "cuda") != "cpu":
        device = os.environ.get("WHISPER_DEVICE", "cuda")
    else:
        device = "cpu"

    model = whisper.load_model("base.en", device=device)

    # Pascal (sm_61, e.g. Quadro P1000) has very slow FP16 throughput.
    fp16 = False
    if device.startswith("cuda"):
        major = torch.cuda.get_device_capability(0)[0]
        fp16 = major >= 7 and os.environ.get("WHISPER_FP16", "1") != "0"

    print(f"[asr] whisper device={device} fp16={fp16}", file=sys.stderr)
    result = model.transcribe(str(path), language="en", fp16=fp16)
    return result["text"].strip()


def transcribe_vosk(path: Path, model_dir: Path) -> str:
    from vosk import KaldiRecognizer, Model, SetLogLevel

    SetLogLevel(-1)
    model = Model(str(model_dir))

    fd, tmp = tempfile.mkstemp(suffix=".wav", prefix="asr-16k-")
    os.close(fd)
    try:
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-i", str(path),
             "-ar", "16000", "-ac", "1", "-f", "wav", tmp],
            check=True,
        )
        with wave.open(tmp, "rb") as wf:
            rec = KaldiRecognizer(model, wf.getframerate())
            chunks = []
            while True:
                data = wf.readframes(4000)
                if not data:
                    break
                if rec.AcceptWaveform(data):
                    chunks.append(json.loads(rec.Result()).get("text", ""))
            chunks.append(json.loads(rec.FinalResult()).get("text", ""))
        return " ".join(c for c in chunks if c).strip()
    finally:
        os.unlink(tmp)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audio", type=Path)
    parser.add_argument("--engine", choices=["whisper", "vosk"], default="whisper")
    parser.add_argument("--vosk-model", type=Path, default=VOSK_DEFAULT)
    args = parser.parse_args()

    if not args.audio.exists():
        print(f"File not found: {args.audio}", file=sys.stderr)
        return 1

    if args.engine == "vosk" and not args.vosk_model.exists():
        print(
            f"Vosk model not found: {args.vosk_model}\n"
            "Download: https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip\n"
            f"Unzip it into: {args.vosk_model.parent}",
            file=sys.stderr,
        )
        return 1

    text = transcribe_whisper(args.audio) if args.engine == "whisper" else transcribe_vosk(args.audio, args.vosk_model)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())

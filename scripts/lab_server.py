"""OpenPronounce server plus the unified lab page and Whisper/Vosk ASR.

Run from this directory:
  uvicorn lab_server:app --host 127.0.0.1 --port 8000
"""
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
REPO = Path(os.environ.get("REPO", ROOT.parent / "OpenPronounce"))
VENV = Path(os.environ.get("ENVDIR", ROOT.parent / ".venv"))

os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")
os.environ.setdefault("OPENPRONOUNCE_TTS", "piper")
os.environ.setdefault("OPENPRONOUNCE_TTS_VOICE", "en_US-lessac-medium")
_HF = Path.home() / ".cache" / "huggingface" / "hub"
if (_HF / "models--facebook--wav2vec2-large-960h").is_dir() and (_HF / "models--rhasspy--piper-voices").is_dir():
    os.environ.setdefault("HF_HUB_OFFLINE", "1")

sys.path.insert(0, str(REPO))
from server import app  # noqa: E402  (imports the upstream FastAPI app)

from fastapi import File, Form, HTTPException, UploadFile  # noqa: E402
from fastapi.responses import FileResponse  # noqa: E402


@app.get("/lab")
async def lab_page():
    page = SCRIPTS / "lab-web.html"
    if not page.exists():
        raise HTTPException(status_code=404, detail="lab-web.html not found")
    return FileResponse(page, media_type="text/html")


@app.post("/lab/asr")
async def lab_asr(file: UploadFile = File(...), engine: str = Form("whisper"), lang: str = Form("en")):
    """Transcribe with Whisper, Vosk, or both. Returns {"engine": ..., "transcripts": {...}}."""
    if engine not in {"whisper", "vosk", "both"}:
        raise HTTPException(status_code=422, detail="engine must be whisper, vosk, or both")

    suffix = Path(file.filename or "audio.webm").suffix or ".webm"
    fd, path = tempfile.mkstemp(suffix=suffix, prefix="lab-asr-")
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(await file.read())

        engines = ["whisper", "vosk"] if engine == "both" else [engine]
        transcripts = {}
        for name in engines:
            proc = subprocess.run(
                [str(VENV / "bin/python"), str(SCRIPTS / "asr.py"), path, "--engine", name],
                capture_output=True,
                text=True,
            )
            if proc.returncode != 0:
                detail = (proc.stderr or proc.stdout or "").strip()[-600:]
                raise HTTPException(status_code=500, detail=f"{name} failed: {detail}")
            transcripts[name] = proc.stdout.strip()
        return {"engine": engine, "lang": lang, "transcripts": transcripts}
    finally:
        try:
            os.unlink(path)
        except OSError:
            pass


@app.post("/lab/save")
async def lab_save(markdown: str = Form(...), filename: str = Form("english-report")):
    """Save a Markdown report under 07_review-log/reports and return its vault-relative path."""
    reports = ROOT / "07_review-log" / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", filename).strip("-")[:48] or "english-report"
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    path = reports / f"{stamp}_{slug}.md"
    path.write_text(markdown, encoding="utf-8")
    return {"path": path.relative_to(ROOT).as_posix()}

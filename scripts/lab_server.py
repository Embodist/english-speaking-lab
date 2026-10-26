"""OpenPronounce server plus the unified lab page and Whisper/Vosk ASR.

Run from this directory:
  uvicorn lab_server:app --host 127.0.0.1 --port 8000
"""
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
REPO = Path(os.environ.get("REPO", ROOT.parent / "OpenPronounce"))
VENV = Path(os.environ.get("ENVDIR", ROOT.parent / ".venv"))
TRANSLATE_URL = os.environ.get("TRANSLATE_URL", "http://127.0.0.1:8081/v1/chat/completions")
DEFAULT_GLOSSARY = ROOT / "15_resume" / "translation-glossary.txt"

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


@app.post("/lab/translate")
async def lab_translate(
    text: str = Form(...),
    target: str = Form("英语"),
    style: str = Form(""),
    use_glossary: str = Form("1"),
    max_tokens: int = Form(1024),
):
    """Proxy a Chinese-to-English draft request to the local Hy-MT2 llama-server."""
    if not text.strip():
        raise HTTPException(status_code=422, detail="empty text")

    lines: list[str] = []
    if use_glossary == "1" and DEFAULT_GLOSSARY.exists():
        lines.append("参考下面的翻译：")
        for line in DEFAULT_GLOSSARY.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                zh, en = line.split("=", 1)
                lines.append(f"{zh.strip()} 翻译成 {en.strip()}")
        lines.append("")
    if style:
        lines.append(f"请将以下文本翻译为{target}。注意翻译的风格要严格符合【{style}】：")
    else:
        lines.append(f"将以下文本翻译为{target}，注意只需要输出翻译后的结果，不要额外解释：")
    lines += ["", text]

    payload = {
        "model": "hy-mt2-1.8b",
        "messages": [{"role": "user", "content": "\n".join(lines)}],
        "temperature": 0.3,
        "top_p": 0.6,
        "top_k": 20,
        "max_tokens": max_tokens,
        "stream": False,
    }
    started = time.time()
    req = urllib.request.Request(
        TRANSLATE_URL,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:300]
        raise HTTPException(status_code=503, detail=f"translation server error: {detail}") from exc
    except urllib.error.URLError as exc:
        raise HTTPException(
            status_code=503,
            detail="translation server not reachable; start scripts/start-translate.sh --background",
        ) from exc

    try:
        translation = data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError) as exc:
        raise HTTPException(status_code=502, detail=f"unexpected translation response: {data}") from exc
    return {
        "translation": translation,
        "model": "hy-mt2-1.8b",
        "elapsed_ms": round((time.time() - started) * 1000),
    }


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

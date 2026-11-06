#!/usr/bin/env python3
"""Local Piper TTS endpoint for qwerty-learner.

GET /tts?word=...&lang=us
Returns a cached WAV with CORS enabled. Run with the lab venv:
  ~/english/.venv/bin/python scripts/qwerty_tts_server.py
"""
import hashlib
import os
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

os.environ.setdefault("OPENPRONOUNCE_TTS", "piper")
os.environ.setdefault("OPENPRONOUNCE_TTS_VOICE", "en_US-lessac-medium")

from openpronounce.audio import text2speech  # noqa: E402

CACHE = Path(os.environ.get("QWERTY_TTS_CACHE", "~/.cache/qwerty-tts")).expanduser()
PORT = int(os.environ.get("QWERTY_TTS_PORT", "8010"))
LOCK = threading.Lock()


class Handler(BaseHTTPRequestHandler):
    server_version = "EnglishLabTTS/1.0"

    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self._cors()
            self.end_headers()
            self.wfile.write(b"ok")
            return
        if parsed.path != "/tts":
            self.send_response(404)
            self.end_headers()
            return

        word = (parse_qs(parsed.query).get("word") or [""])[0].strip()
        if not word:
            self.send_response(400)
            self._cors()
            self.end_headers()
            return
        if len(word) > 300:
            word = word[:300]

        CACHE.mkdir(parents=True, exist_ok=True)
        key = hashlib.sha1(word.encode("utf-8")).hexdigest()
        path = CACHE / f"{key}.wav"
        if not path.exists():
            with LOCK:
                if not path.exists():
                    text2speech(word, "en", filename=str(path))

        data = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "audio/wav")
        self.send_header("Content-Length", str(len(data)))
        self._cors()
        self.end_headers()
        self.wfile.write(data)


def main():
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"qwerty TTS on http://127.0.0.1:{PORT}/tts (cache: {CACHE})", file=sys.stderr)
    server.serve_forever()


if __name__ == "__main__":
    main()

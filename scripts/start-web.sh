#!/usr/bin/env bash
# Start the OpenPronounce web UI. Open http://localhost:8000 in the Windows browser.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENVDIR="${ENVDIR:-$ROOT/../.venv}"
REPO="${REPO:-$ROOT/../OpenPronounce}"
PORT="${PORT:-8000}"

if [[ ! -d "$REPO" ]]; then
  echo "OpenPronounce repo not found at $REPO" >&2
  echo "Run: git clone https://github.com/Halleck45/OpenPronounce.git $REPO" >&2
  exit 1
fi

export HF_ENDPOINT="${HF_ENDPOINT:-https://hf-mirror.com}"
# Local TTS: the default gTTS backend needs Google access and will hang offline.
export OPENPRONOUNCE_TTS="${OPENPRONOUNCE_TTS:-piper}"
export OPENPRONOUNCE_TTS_VOICE="${OPENPRONOUNCE_TTS_VOICE:-en_US-lessac-medium}"

LAB_PAGE="$ROOT/scripts/lab-web.html"
if [[ -f "$LAB_PAGE" ]]; then
  mkdir -p "$REPO/static"
  cp "$LAB_PAGE" "$REPO/static/lab.html"
fi

echo "Starting OpenPronounce on http://localhost:$PORT"
echo "Unified lab page:    http://localhost:$PORT/lab"
echo "OpenPronounce UI:    http://localhost:$PORT/"
echo "Press Ctrl+C to stop."
cd "$ROOT/scripts"
export PYTHONPATH="$REPO${PYTHONPATH:+:$PYTHONPATH}"
exec "$ENVDIR/bin/uvicorn" lab_server:app --host 127.0.0.1 --port "$PORT"

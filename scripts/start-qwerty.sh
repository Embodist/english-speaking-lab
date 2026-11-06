#!/usr/bin/env bash
# Start the local qwerty-learner dev server and the local Piper TTS endpoint.
# Usage: bash scripts/start-qwerty.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPO="${QWERTY_REPO:-$HOME/english/qwerty-learner}"
VENV_PY="${ENVDIR:-$HOME/english/.venv}/bin/python"
PORT="${PORT:-5173}"
TTS_PORT="${QWERTY_TTS_PORT:-8010}"

if [[ ! -f "$REPO/package.json" ]]; then
  echo "qwerty-learner not found: $REPO" >&2
  echo "Clone it first: git clone https://github.com/RealKai42/qwerty-learner.git ~/english/qwerty-learner" >&2
  exit 1
fi

if ! curl -sf "http://127.0.0.1:$TTS_PORT/health" >/dev/null 2>&1; then
  echo "Starting local TTS on port $TTS_PORT..."
  QWERTY_TTS_PORT="$TTS_PORT" setsid nohup "$VENV_PY" "$ROOT/scripts/qwerty_tts_server.py" \
    > /tmp/qwerty-tts.log 2>&1 < /dev/null &
  echo $! > /tmp/qwerty-tts.pid
  sleep 1
fi

cd "$REPO"
echo "Starting qwerty-learner at http://127.0.0.1:$PORT/gallery"
exec corepack yarn dev --host 127.0.0.1 --port "$PORT"

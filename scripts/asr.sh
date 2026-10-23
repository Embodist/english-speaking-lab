#!/usr/bin/env bash
# Transcribe a recording to check intelligibility.
# Usage: scripts/asr.sh recording.wav [--engine whisper|vosk]
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENVDIR="${ENVDIR:-$ROOT/../.venv}"
exec "$ENVDIR/bin/python" "$ROOT/scripts/asr.py" "$@"

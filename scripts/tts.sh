#!/usr/bin/env bash
# Generate a reference WAV with the local Piper voice.
# Usage: scripts/tts.sh "Sentence to speak" [-o out.wav]
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENVDIR="${ENVDIR:-$ROOT/../.venv}"
exec "$ENVDIR/bin/python" "$ROOT/scripts/tts.py" "$@"

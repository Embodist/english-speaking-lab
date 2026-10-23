#!/usr/bin/env bash
# Score a recording against the expected sentence.
# Usage: scripts/pronounce.sh path/to/recording.wav "The sentence I said."
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENVDIR="${ENVDIR:-$ROOT/../.venv}"

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <audio-file> \"<expected sentence>\" [--json]" >&2
  exit 1
fi

export HF_ENDPOINT="${HF_ENDPOINT:-https://hf-mirror.com}"
# Set OPENPRONOUNCE_TTS=piper to keep reference audio offline.
export OPENPRONOUNCE_TTS="${OPENPRONOUNCE_TTS:-piper}"
export OPENPRONOUNCE_TTS_VOICE="${OPENPRONOUNCE_TTS_VOICE:-en_US-lessac-medium}"

exec "$ENVDIR/bin/openpronounce" "$@"

#!/usr/bin/env bash
# Stop the local qwerty-learner dev server and TTS endpoint.
set -euo pipefail

if [[ -f /tmp/qwerty-tts.pid ]]; then
  kill "$(cat /tmp/qwerty-tts.pid)" 2>/dev/null || true
  rm -f /tmp/qwerty-tts.pid
fi
pkill -f "vite --host 127.0.0.1" 2>/dev/null || true
echo "stopped qwerty dev server and local TTS"

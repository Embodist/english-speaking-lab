#!/usr/bin/env bash
# Verify the study environment and downloaded models.
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENVDIR="${ENVDIR:-$ROOT/../.venv}"

echo "== System tools =="
for c in ffmpeg espeak-ng git curl; do
  if command -v "$c" >/dev/null; then
    printf "%-12s %s\n" "$c" "$(command -v "$c")"
  else
    printf "%-12s MISSING\n" "$c"
  fi
done

echo
echo "== Python environment =="
if [[ -x "$ENVDIR/bin/python" ]]; then
  "$ENVDIR/bin/python" -c "import torch, openpronounce; print('python     ', __import__('sys').version.split()[0]); print('torch      ', torch.__version__); print('openpronounce', openpronounce.__version__)"
else
  echo "venv missing at $ENVDIR"
fi

echo
echo "== Optional tools =="
"$ENVDIR/bin/python" - <<'EOF' 2>/dev/null || true
mods = {
    "piper": "Piper TTS",
    "whisper": "Whisper ASR",
    "vosk": "Vosk ASR",
}
import importlib.util
for m, label in mods.items():
    print(f"{label:<14}", "ok" if importlib.util.find_spec(m) else "MISSING")
EOF

echo
echo "== Models =="
HF_CACHE="${HF_HOME:-$HOME/.cache/huggingface}"
echo "HF cache: $HF_CACHE"
du -sh "$HF_CACHE" 2>/dev/null || echo "  (not downloaded yet)"
echo "Whisper : $HOME/.cache/whisper"
ls -lh "$HOME/.cache/whisper" 2>/dev/null | tail -3 || echo "  (not downloaded yet)"
echo "Vosk    : $ROOT/../models/vosk-model-small-en-us-0.15"
[[ -d "$ROOT/../models/vosk-model-small-en-us-0.15" ]] && echo "  ok" || echo "  (not downloaded yet)"

echo
echo "== OpenPronounce web UI =="
[[ -f "$ROOT/../OpenPronounce/server.py" ]] && echo "repo ok: $ROOT/../OpenPronounce" || echo "repo missing"

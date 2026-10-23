#!/usr/bin/env bash
# Reproduce the English study toolchain. Safe to re-run; completed steps are skipped.
# Optional: SKIP_MODELS=1 to skip the ~2.7 GB model downloads.
set -euo pipefail

ROOT="${ROOT:-$HOME/english}"
VENV="${ENVDIR:-$ROOT/.venv}"
REPO="${REPO:-$ROOT/OpenPronounce}"
MODELS="$ROOT/models"
MIRROR="${HF_ENDPOINT:-https://hf-mirror.com}"
export HF_ENDPOINT="$MIRROR"

log() { printf '\n== %s\n' "$*"; }
have() { command -v "$1" >/dev/null 2>&1; }

log "System dependencies"
if ! have ffmpeg || ! have espeak-ng || ! have git || ! have curl; then
  SUDO=""
  if [[ $EUID -ne 0 ]]; then SUDO="sudo"; fi
  $SUDO apt-get update
  $SUDO apt-get install -y ffmpeg espeak-ng git curl python3-venv
else
  echo "ffmpeg / espeak-ng / git / curl present"
fi

log "Python virtual environment"
mkdir -p "$ROOT"
if [[ ! -x "$VENV/bin/python" ]]; then
  python3 -m venv "$VENV"
  echo "created $VENV"
else
  echo "using $VENV"
fi
"$VENV/bin/python" -m pip install --upgrade pip

log "PyTorch (CPU)"
if ! "$VENV/bin/python" -c "import torch" >/dev/null 2>&1; then
  "$VENV/bin/pip" install torch --index-url https://download.pytorch.org/whl/cpu
else
  echo "torch present"
fi

log "Python packages"
install_if_missing() {
  local module="$1" pkg="$2"
  if "$VENV/bin/python" -c "import importlib.util,sys; sys.exit(0 if importlib.util.find_spec('$module') else 1)" >/dev/null 2>&1; then
    echo "$pkg present"
  else
    "$VENV/bin/pip" install "$pkg"
  fi
}
if "$VENV/bin/python" -c "import openpronounce, fastapi, uvicorn" >/dev/null 2>&1; then
  echo "openpronounce[app] present"
else
  "$VENV/bin/pip" install "openpronounce[app]"
fi
install_if_missing piper "openpronounce[tts-piper]"
install_if_missing whisper "openai-whisper"
install_if_missing vosk "vosk"

log "OpenPronounce web source"
if [[ ! -f "$REPO/server.py" ]]; then
  git clone --depth 1 https://github.com/Halleck45/OpenPronounce.git "$REPO"
else
  echo "repo present: $REPO"
fi

if [[ "${SKIP_MODELS:-0}" == "1" ]]; then
  log "SKIP_MODELS=1: skipping model downloads"
else
  log "Piper voice"
  "$VENV/bin/python" - <<'EOF'
import os
from pathlib import Path
import soundfile as sf
from openpronounce import tts

voice = tts.piper_default_voice("en")
out = Path("/tmp/piper_check.wav")
try:
    wav, sr = tts.synthesize("Hello, this is a reference voice.", "en", "piper", voice)
    sf.write(out, wav, sr)
    print("Piper voice ready:", voice)
except Exception as e:
    raise SystemExit(f"Piper voice download failed: {e}")
EOF

  log "Whisper base.en"
  if [[ -f "$HOME/.cache/whisper/base.en.pt" ]]; then
    echo "Whisper model present"
  else
    "$VENV/bin/python" -c "import whisper; whisper.load_model('base.en'); print('Whisper base.en ready')"
  fi

  log "Vosk English model"
  VOSK_DIR="$MODELS/vosk-model-small-en-us-0.15"
  if [[ -d "$VOSK_DIR" ]]; then
    echo "Vosk model present"
  else
    mkdir -p "$MODELS"
    TMP="$MODELS/vosk.tar.gz"
    curl -L -o "$TMP" "$MIRROR/zzzlll/vosk-model-small-en-us-0.15/resolve/main/vosk-model-small-en-us-0.15.tar.gz"
    tar xzf "$TMP" -C "$MODELS"
    rm -f "$TMP"
    echo "Vosk model ready: $VOSK_DIR"
  fi

  log "OpenPronounce checkpoints (about 2.5 GB on first run)"
  "$VENV/bin/python" - <<'EOF'
from pathlib import Path
import soundfile as sf
from openpronounce import tts
wav, sr = tts.synthesize("I haven't identified the root cause yet.", "en", "piper", tts.piper_default_voice("en"))
sf.write("/tmp/openpronounce_check.wav", wav, sr)
EOF
  "$VENV/bin/openpronounce" /tmp/openpronounce_check.wav "I haven't identified the root cause yet."
fi

log "Dependency check"
"$VENV/bin/python" -m pip check

log "Environment check"
if [[ -x "$ROOT/english-speaking-lab/scripts/check-env.sh" ]]; then
  bash "$ROOT/english-speaking-lab/scripts/check-env.sh"
fi

log "Done"
echo "Next: cd $ROOT/english-speaking-lab && bash scripts/start-web.sh"

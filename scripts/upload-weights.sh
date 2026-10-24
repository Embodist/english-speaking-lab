#!/usr/bin/env bash
# Package local model caches and upload them to RustFS/S3.
#
# Required:
#   RUSTFS_ENDPOINT   e.g. http://172.19.160.1:9000
#   RUSTFS_ACCESS_KEY
#   RUSTFS_SECRET_KEY
# Optional:
#   RUSTFS_BUCKET     default storage1
#   RUSTFS_PREFIX     default rustfs/english-lab/models
#   RUSTFS_REGION     default us-east-1
#   BUNDLE            default ~/english/model-bundle
#
# Usage:
#   source deploy/rustfs.env
#   RUSTFS_ACCESS_KEY=... RUSTFS_SECRET_KEY=... bash scripts/upload-weights.sh
#   bash scripts/upload-weights.sh --bundle-only
#   bash scripts/upload-weights.sh --skip-build
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUNDLE="${BUNDLE:-$HOME/english/model-bundle}"
ENDPOINT="${RUSTFS_ENDPOINT:-}"
BUCKET="${RUSTFS_BUCKET:-storage1}"
PREFIX="${RUSTFS_PREFIX:-rustfs/english-lab/models}"
REGION="${RUSTFS_REGION:-us-east-1}"
ACCESS="${RUSTFS_ACCESS_KEY:-}"
SECRET="${RUSTFS_SECRET_KEY:-}"
MODE="upload"

for arg in "$@"; do
  case "$arg" in
    --bundle-only) MODE="bundle" ;;
    --skip-build) MODE="upload" ;;
    -h|--help) sed -n '1,30p' "$0"; exit 0 ;;
    *) echo "unknown argument: $arg" >&2; exit 2 ;;
  esac
done

build_bundle() {
  echo "== Building model bundle =="
  rm -rf "$BUNDLE"
  mkdir -p "$BUNDLE/root/huggingface/hub" "$BUNDLE/root/home/.cache/whisper"
  cp -al "$HOME/.cache/huggingface/hub/models--facebook--wav2vec2-large-960h" "$BUNDLE/root/huggingface/hub/"
  cp -al "$HOME/.cache/huggingface/hub/models--facebook--wav2vec2-lv-60-espeak-cv-ft" "$BUNDLE/root/huggingface/hub/"
  cp -al "$HOME/.cache/huggingface/hub/models--rhasspy--piper-voices" "$BUNDLE/root/huggingface/hub/"
  cp -al "$HOME/.cache/whisper/base.en.pt" "$BUNDLE/root/home/.cache/whisper/"
  cp -al "$HOME/english/models/vosk-model-small-en-us-0.15" "$BUNDLE/root/"
  cat > "$BUNDLE/root/MANIFEST.txt" <<EOF
English Lab model bundle
created: $(date -Is)
hf_home: /models/huggingface
home: /models/home
vosk: /models/vosk-model-small-en-us-0.15
extract: tar -C /models -xf models.tar
EOF
  tar -C "$BUNDLE/root" -cf "$BUNDLE/models.tar" .
  (cd "$BUNDLE" && sha256sum models.tar > models.tar.sha256)
  du -sh "$BUNDLE/models.tar"
  cat "$BUNDLE/models.tar.sha256"
}

if [[ "$MODE" == "upload" ]]; then
  [[ -f "$BUNDLE/models.tar" ]] || build_bundle
fi
if [[ "$MODE" == "bundle" ]]; then
  build_bundle
  exit 0
fi

: "${ENDPOINT:?set RUSTFS_ENDPOINT (e.g. http://172.19.160.1:9000)}"
: "${ACCESS:?set RUSTFS_ACCESS_KEY}"
: "${SECRET:?set RUSTFS_SECRET_KEY}"
command -v rclone >/dev/null || { echo "rclone is required: sudo apt-get install -y rclone" >&2; exit 1; }

export RCLONE_CONFIG_RUSTFS_TYPE=s3
export RCLONE_CONFIG_RUSTFS_PROVIDER=Other
export RCLONE_CONFIG_RUSTFS_ENDPOINT="$ENDPOINT"
export RCLONE_CONFIG_RUSTFS_ACCESS_KEY_ID="$ACCESS"
export RCLONE_CONFIG_RUSTFS_SECRET_ACCESS_KEY="$SECRET"
export RCLONE_CONFIG_RUSTFS_REGION="$REGION"
export RCLONE_CONFIG_RUSTFS_FORCE_PATH_STYLE="${RUSTFS_FORCE_PATH_STYLE:-true}"

TARGET="rustfs:${BUCKET}/${PREFIX}"
echo "== Uploading to $TARGET =="
rclone copy "$BUNDLE/models.tar" "$TARGET/" --progress --transfers 1 --checkers 4 --timeout 5m --retries 3
rclone copy "$BUNDLE/models.tar.sha256" "$TARGET/" --timeout 1m --retries 3
echo "== Verifying =="
rclone check "$BUNDLE" "$TARGET/" --include "models.tar" --include "models.tar.sha256" --timeout 5m
rclone ls "$TARGET/" --timeout 1m
echo "DONE: $TARGET/models.tar"

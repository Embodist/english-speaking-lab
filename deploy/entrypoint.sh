#!/usr/bin/env bash
set -euo pipefail

read_secret() {
  local name="$1" file="/run/secrets/$1"
  if [[ -f "$file" ]]; then cat "$file"; else printf '%s' "${!name:-}"; fi
}

ACCESS_KEY="$(read_secret rustfs_access_key)"
SECRET_KEY="$(read_secret rustfs_secret_key)"

if [[ "${LAB_SYNC_MODELS:-1}" == "1" && -n "${RUSTFS_ENDPOINT:-}" && ! -f /models/.ready ]]; then
  if [[ -z "$ACCESS_KEY" || -z "$SECRET_KEY" ]]; then
    echo "ERROR: RustFS credentials are missing (secrets rustfs_access_key/rustfs_secret_key)" >&2
    exit 1
  fi

  export RCLONE_CONFIG_RUSTFS_TYPE=s3
  export RCLONE_CONFIG_RUSTFS_PROVIDER=Other
  export RCLONE_CONFIG_RUSTFS_ENDPOINT="$RUSTFS_ENDPOINT"
  export RCLONE_CONFIG_RUSTFS_ACCESS_KEY_ID="$ACCESS_KEY"
  export RCLONE_CONFIG_RUSTFS_SECRET_ACCESS_KEY="$SECRET_KEY"
  export RCLONE_CONFIG_RUSTFS_REGION="${RUSTFS_REGION:-us-east-1}"
  export RCLONE_CONFIG_RUSTFS_FORCE_PATH_STYLE="${RUSTFS_FORCE_PATH_STYLE:-true}"

  TARGET="rustfs:${RUSTFS_BUCKET:-storage1}/${RUSTFS_PREFIX:-rustfs/english-lab/models}"
  echo "Syncing models from $TARGET to /models"
  mkdir -p /models
  rclone copy "$TARGET/" /models --include "models.tar" --include "models.tar.sha256" \
    --transfers 1 --checkers 4 --timeout 10m --retries 5

  cd /models
  if [[ -f models.tar && -f models.tar.sha256 ]]; then
    sha256sum -c models.tar.sha256
    tar -xf models.tar
    rm -f models.tar models.tar.sha256
    touch /models/.ready
  else
    echo "WARNING: models.tar not found at $TARGET" >&2
  fi
fi

if [[ -d /models/huggingface/hub/models--facebook--wav2vec2-large-960h && \
      -d /models/vosk-model-small-en-us-0.15 ]]; then
  touch /models/.ready
  export HF_HUB_OFFLINE=1
fi

exec uvicorn lab_server:app --host 0.0.0.0 --port 8000 --app-dir /app/scripts

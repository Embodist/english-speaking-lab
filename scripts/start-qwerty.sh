#!/usr/bin/env bash
# Start the local qwerty-learner dev server.
# Usage: bash scripts/start-qwerty.sh
set -euo pipefail

REPO="${QWERTY_REPO:-$HOME/english/qwerty-learner}"
PORT="${PORT:-5173}"

if [[ ! -f "$REPO/package.json" ]]; then
  echo "qwerty-learner not found: $REPO" >&2
  echo "Clone it first: git clone https://github.com/RealKai42/qwerty-learner.git ~/english/qwerty-learner" >&2
  exit 1
fi

cd "$REPO"
echo "Starting qwerty-learner at http://127.0.0.1:$PORT/gallery"
exec corepack yarn dev --host 127.0.0.1 --port "$PORT"

#!/usr/bin/env bash
# Sync the WSL vault with the native Windows Obsidian mirror.
#
# Usage:
#   bash scripts/sync-windows.sh status          # show differences
#   bash scripts/sync-windows.sh push            # WSL -> D: (mirror, deletes extras)
#   bash scripts/sync-windows.sh pull            # D: -> WSL (keeps WSL-only files)
#   bash scripts/sync-windows.sh pull-delete     # D: -> WSL (mirror, deletes extras)
#
# Default target: /mnt/d/Obsidian/EnglishVault
# Override: WIN_VAULT=/mnt/d/Other/Vault
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WIN="${WIN_VAULT:-/mnt/d/Obsidian/EnglishVault}"
MODE="${1:-status}"
EXCLUDES=(--exclude=.git --exclude=.obsidian/workspace.json --exclude=.trash)

if [[ ! -d "$WIN" ]]; then
  echo "Windows vault not found: $WIN" >&2
  echo "Create it first, or set WIN_VAULT." >&2
  exit 1
fi

case "$MODE" in
  status)
    echo "WSL: $ROOT"
    echo "Win: $WIN"
    rsync -rni --delete "${EXCLUDES[@]}" "$ROOT/" "$WIN/" | head -40
    ;;
  push)
    echo "Pushing WSL -> Windows (mirror; Windows-only edits may be overwritten)…"
    rsync -r --delete "${EXCLUDES[@]}" "$ROOT/" "$WIN/"
    echo "Done. Open in Obsidian: D:\\Obsidian\\EnglishVault"
    ;;
  pull)
    echo "Pulling Windows -> WSL (keeps WSL-only files)…"
    rsync -r "${EXCLUDES[@]}" "$WIN/" "$ROOT/"
    echo "Done."
    ;;
  pull-delete)
    echo "Pulling Windows -> WSL (mirror; WSL-only files may be deleted)…"
    rsync -r --delete "${EXCLUDES[@]}" "$WIN/" "$ROOT/"
    echo "Done."
    ;;
  *)
    echo "usage: $0 status|push|pull|pull-delete" >&2
    exit 2
    ;;
esac

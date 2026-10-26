#!/usr/bin/env bash
# Chinese -> English draft translation. Requires start-translate.sh.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENVDIR="${ENVDIR:-$HOME/english/.venv}"
exec "$ENVDIR/bin/python" "$ROOT/scripts/translate.py" "$@"

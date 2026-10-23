#!/usr/bin/env bash
# Unified English practice entry point. See scripts/lab.py --help.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENVDIR="${ENVDIR:-$ROOT/../.venv}"
exec "$ENVDIR/bin/python" "$ROOT/scripts/lab.py" "$@"

#!/usr/bin/env bash
# Stop the background llama-server started by start-translate.sh.
set -euo pipefail

PIDFILE="${PIDFILE:-/tmp/llama-translate.pid}"
if [[ -f "$PIDFILE" ]]; then
  pid="$(cat "$PIDFILE")"
  if ps -p "$pid" >/dev/null 2>&1; then
    kill "$pid"
    echo "stopped llama-server pid $pid"
  else
    echo "stale pid file; llama-server not running"
  fi
  rm -f "$PIDFILE"
else
  echo "no pid file at $PIDFILE"
  pgrep -af 'llama-server.*hy-mt2' || true
fi

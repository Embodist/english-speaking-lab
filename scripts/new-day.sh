#!/usr/bin/env bash
# Create today's practice log from the daily template (never overwrites).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_DIR="$ROOT/07_review-log"
TEMPLATE="$ROOT/10_templates/daily-practice.md"
DATE="${1:-$(date +%F)}"
OUT="$LOG_DIR/$DATE.md"

if [[ -e "$OUT" ]]; then
  echo "Already exists: $OUT"
  exit 0
fi

sed "s/{{date}}/$DATE/g" "$TEMPLATE" > "$OUT"
echo "Created $OUT"

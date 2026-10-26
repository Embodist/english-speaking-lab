#!/usr/bin/env bash
# Start Tencent Hy-MT2-1.8B with llama-server on the GPU (port 8081 by default).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LLAMA_DIR="${LLAMA_DIR:-$HOME/english/llama.cpp-cuda}"
SERVER="$LLAMA_DIR/llama-b11889/llama-server"
CUDART="$LLAMA_DIR/cudart-llama-b11889-bin-ubuntu-cuda-12.8-x64"
MODEL="${HYMT2_MODEL:-$HOME/english/models/hy-mt2-1.8b/Hy-MT2-1.8B-Q6_K.gguf}"
PORT="${PORT:-8081}"
CTX="${CTX:-2048}"

if [[ ! -x "$SERVER" ]]; then
  echo "llama-server not found: $SERVER" >&2
  echo "Download the CUDA build first; see 13_tech-frameworks/translation-model.md" >&2
  exit 1
fi
if [[ ! -f "$MODEL" ]]; then
  echo "Model not found: $MODEL" >&2
  exit 1
fi
if command -v nvidia-smi >/dev/null 2>&1; then
  free_mib=$(nvidia-smi --query-gpu=memory.free --format=csv,noheader,nounits | head -1 | tr -d ' ')
  if [[ -n "$free_mib" && "$free_mib" -lt 2000 ]]; then
    echo "Warning: only ${free_mib} MiB VRAM free; Q6_K may OOM. Close GPU workloads or use Q4_K_M." >&2
  fi
fi

export LD_LIBRARY_PATH="$CUDART${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
ARGS=(
  --model "$MODEL"
  --host 127.0.0.1
  --port "$PORT"
  --n-gpu-layers 99
  --ctx-size "$CTX"
  --jinja
  --alias hy-mt2-1.8b
  --parallel 1
  --threads 6
)

if [[ "${1:-}" == "--background" ]]; then
  setsid nohup "$SERVER" "${ARGS[@]}" > /tmp/llama-translate.log 2>&1 < /dev/null &
  echo $! > /tmp/llama-translate.pid
  echo "started pid $(cat /tmp/llama-translate.pid); log: /tmp/llama-translate.log"
  echo "url: http://localhost:$PORT"
  exit 0
fi

echo "Starting Hy-MT2-1.8B on GPU (ctx=$CTX, port=$PORT)"
echo "OpenAI API: http://localhost:$PORT/v1/chat/completions"
echo "Press Ctrl-C to stop."
exec "$SERVER" "${ARGS[@]}"

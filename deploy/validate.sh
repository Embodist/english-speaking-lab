#!/usr/bin/env bash
# Static validation + prerequisite checks for the Swarm stack.
set -uo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."
status=0
ok()  { printf 'ok   %s\n' "$*"; }
bad() { printf 'FAIL %s\n' "$*" >&2; status=1; }
warn() { printf 'warn %s\n' "$*"; }

echo "== Files =="
for f in \
  deploy/Dockerfile deploy/Dockerfile.gpu \
  deploy/entrypoint.sh deploy/swarm-stack.yml deploy/swarm-stack.gpu.yml \
  deploy/rustfs.env.example scripts/lab_server.py scripts/lab-web.html \
  scripts/asr.py scripts/upload-weights.sh; do
  [[ -f "$f" ]] && ok "$f" || bad "missing $f"
done

echo "== YAML =="
if python3 - <<'PY'
import yaml, sys
for f in ['deploy/swarm-stack.yml', 'deploy/swarm-stack.gpu.yml']:
    d = yaml.safe_load(open(f, encoding='utf-8'))
    assert isinstance(d, dict) and 'services' in d and 'lab' in d['services'], f
    print('ok   yaml', f)
PY
then :; else bad "YAML parse failed"; fi

echo "== Compose config =="
for f in deploy/swarm-stack.yml deploy/swarm-stack.gpu.yml; do
  if docker compose -f "$f" config >/dev/null 2>&1; then
    ok "compose config $f"
  else
    bad "compose config $f"
  fi
done

echo "== Shell / Python syntax =="
bash -n deploy/entrypoint.sh && ok "entrypoint.sh" || bad "entrypoint.sh"
bash -n scripts/upload-weights.sh && ok "upload-weights.sh" || bad "upload-weights.sh"
PY="$HOME/english/.venv/bin/python"
[[ -x "$PY" ]] || PY=python3
if "$PY" -m py_compile scripts/lab_server.py scripts/asr.py scripts/tts.py; then
  ok "python scripts"
else
  bad "python scripts"
fi

echo "== Prerequisites =="
[[ -f deploy/rustfs.env ]] && ok "deploy/rustfs.env" || warn "deploy/rustfs.env missing (see rustfs.env.example)"
if [[ -f "$HOME/english/model-bundle/models.tar.sha256" ]]; then
  if awk '{print $2}' "$HOME/english/model-bundle/models.tar.sha256" | grep -qx 'models.tar'; then
    ok "checksum uses relative models.tar"
  else
    bad "checksum must use relative filename models.tar"
  fi
fi

if docker info >/dev/null 2>&1; then
  ok "docker daemon"
  for s in rustfs_access_key rustfs_secret_key; do
    if docker secret inspect "$s" >/dev/null 2>&1; then ok "secret $s"; else bad "missing secret $s"; fi
  done
  if docker node ls >/dev/null 2>&1; then ok "swarm active"; else warn "docker swarm not initialized"; fi
else
  warn "docker daemon not running: skipped secret/swarm/runtime checks"
fi

echo
if ((status == 0)); then
  echo "RESULT: static checks passed"
else
  echo "RESULT: issues found" >&2
fi
exit "$status"

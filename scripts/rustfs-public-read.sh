#!/usr/bin/env bash
# Manage a prefix-scoped public-read bucket policy on RustFS/S3.
#
# Usage:
#   RUSTFS_ENDPOINT=http://172.19.160.1:9000 \
#   RUSTFS_ACCESS_KEY=... RUSTFS_SECRET_KEY=... \
#   bash scripts/rustfs-public-read.sh apply|status|remove
#
# Optional:
#   RUSTFS_BUCKETS="english-lab storage1"
#   RUSTFS_PUBLIC_PREFIX="rustfs/english-lab/models"
#
# This only changes bucket policy; it does not restart RustFS or the lab service.
set -euo pipefail

MODE="${1:-apply}"
ENDPOINT="${RUSTFS_ENDPOINT:?set RUSTFS_ENDPOINT (e.g. http://172.19.160.1:9000)}"
ACCESS="${RUSTFS_ACCESS_KEY:?set RUSTFS_ACCESS_KEY}"
SECRET="${RUSTFS_SECRET_KEY:?set RUSTFS_SECRET_KEY}"
BUCKETS="${RUSTFS_BUCKETS:-english-lab storage1}"
PREFIX="${RUSTFS_PUBLIC_PREFIX:-rustfs/english-lab/models}"

command -v aws >/dev/null || { echo "aws CLI required: sudo apt-get install -y awscli" >&2; exit 1; }
command -v curl >/dev/null || { echo "curl required" >&2; exit 1; }

export AWS_ACCESS_KEY_ID="$ACCESS"
export AWS_SECRET_ACCESS_KEY="$SECRET"
export AWS_DEFAULT_REGION="${RUSTFS_REGION:-us-east-1}"

TMPDIR="$(mktemp -d)"
trap 'rm -rf "$TMPDIR"' EXIT

policy_json() {
  local bucket="$1" out="$2" mode="$3" old="$4"
  python3 - "$bucket" "$out" "$mode" "$old" "$PREFIX" <<'PY'
import json, sys
bucket, out, mode, old_path, prefix = sys.argv[1:6]
try:
    old = json.load(open(old_path, encoding='utf-8'))
    if isinstance(old, str):
        old = json.loads(old)
except Exception:
    old = {"Version": "2012-10-17", "Statement": []}
statements = [s for s in old.get("Statement", []) if s.get("Sid") not in {"PublicReadModels", "PublicListModelsPrefix"}]
if mode == "apply":
    statements += [
        {
            "Sid": "PublicReadModels",
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:GetObject"],
            "Resource": [f"arn:aws:s3:::{bucket}/{prefix}/*"],
        },
        {
            "Sid": "PublicListModelsPrefix",
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:ListBucket"],
            "Resource": [f"arn:aws:s3:::{bucket}"],
            "Condition": {"StringLike": {"s3:prefix": [f"{prefix}/", f"{prefix}/*"]}},
        },
    ]
policy = {"Version": "2012-10-17", "Statement": statements}
if not statements:
    print("EMPTY")
else:
    json.dump(policy, open(out, 'w', encoding='utf-8'), indent=2)
    print(out)
PY
}

anon_check() {
  local bucket="$1"
  local url="${ENDPOINT}/${bucket}/${PREFIX}/models.tar.sha256"
  local code
  code="$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 "$url" || echo 000)"
  printf '%-14s anonymous GET models.tar.sha256 -> %s\n' "$bucket" "$code"
}

for bucket in $BUCKETS; do
  echo "== $bucket =="
  old="$TMPDIR/$bucket.old.json"
  new="$TMPDIR/$bucket.new.json"
  if aws --endpoint-url "$ENDPOINT" s3api get-bucket-policy --bucket "$bucket" --query Policy --output text >"$old" 2>/dev/null; then
    :
  else
    echo '{"Version":"2012-10-17","Statement":[]}' >"$old"
  fi

  case "$MODE" in
    status)
      python3 - "$old" <<'PY'
import json, sys
try:
    d = json.load(open(sys.argv[1], encoding='utf-8'))
    print("policy:", ", ".join(s.get("Sid", "(no sid)") for s in d.get("Statement", [])) or "(none)")
except Exception:
    print("policy: (none)")
PY
      anon_check "$bucket"
      ;;
    apply|remove)
      result="$(policy_json "$bucket" "$new" "$MODE" "$old")"
      if [[ "$result" == "EMPTY" ]]; then
        aws --endpoint-url "$ENDPOINT" s3api delete-bucket-policy --bucket "$bucket"
        echo "removed bucket policy (no statements left)"
      else
        aws --endpoint-url "$ENDPOINT" s3api put-bucket-policy --bucket "$bucket" --policy "file://$new"
        echo "applied policy: $result"
      fi
      ;;
    *)
      echo "usage: $0 apply|status|remove" >&2
      exit 2
      ;;
  esac
done

if [[ "$MODE" == "apply" || "$MODE" == "status" ]]; then
  echo "== anonymous checks =="
  for bucket in $BUCKETS; do anon_check "$bucket"; done
fi

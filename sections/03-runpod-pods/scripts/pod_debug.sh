#!/usr/bin/env bash
set -euo pipefail

echo "== GPU =="
command -v nvidia-smi >/dev/null 2>&1 && nvidia-smi || echo "nvidia-smi unavailable"

echo "== Disk =="
df -h

echo "== Common RunPod paths =="
du -sh /workspace /runpod-volume 2>/dev/null || true

echo "== Environment excerpt =="
printenv | sort | sed -n '1,80p'

echo "== Local health check =="
curl -fsS http://localhost:${PORT:-8000}/health || true

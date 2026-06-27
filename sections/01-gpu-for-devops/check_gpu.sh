#!/usr/bin/env bash
set -euo pipefail

echo "== Host GPU check =="
if command -v nvidia-smi >/dev/null 2>&1; then
  nvidia-smi
else
  echo "nvidia-smi is not available on this host. Run this on a GPU machine or RunPod Pod."
fi

echo "== Docker GPU smoke test =="
echo "docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi"

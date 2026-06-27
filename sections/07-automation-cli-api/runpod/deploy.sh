#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME=${IMAGE_NAME:-registry.example.com/ai-devops-demo:latest}
CONFIG_PATH=${CONFIG_PATH:-runpod/endpoint_config.json}

echo "Build and push your image before deploying: ${IMAGE_NAME}"
echo "Use RunPod CLI or REST API with config: ${CONFIG_PATH}"
echo "TODO: replace this echo-only script with your organization-specific runpodctl/API commands."

# AIOps — AI DevOps / LLMOps RunPod Training Path

This repository is a practical curriculum for a DevOps engineer who needs to become an **AI DevOps / LLMOps Engineer**. The goal is not to turn the learner into a Data Scientist. The goal is to make them able to package, deploy, monitor, debug and operate AI/LLM inference services on GPU infrastructure and RunPod.

## Role Definition

By the end of the path, the learner should be able to:

| Area | Expected Outcome |
| --- | --- |
| GPU Infrastructure | Understand CUDA, drivers, VRAM, `nvidia-smi` and GPU utilization |
| Docker for AI | Build GPU-compatible images and understand NVIDIA runtime behavior |
| Model Serving | Serve models with vLLM, Ollama, FastAPI, ComfyUI or TGI |
| RunPod Pods | Create GPU development/test environments with SSH, Jupyter or VS Code |
| RunPod Serverless | Build scalable inference endpoints with workers and queues |
| Storage | Manage model weights, datasets and cache with Network Volumes or S3 |
| Observability | Monitor latency, tokens/sec, queue time, cold start and GPU memory |
| Cost Control | Choose Pods vs Serverless and tune active/max workers |
| CI/CD | Automate image build, registry push, deployment, smoke tests and rollback |

## 8-Week Roadmap

| Week | Focus | Practical Output |
| --- | --- | --- |
| 1 | GPU for DevOps | GPU debug checklist and container run with `--gpus` |
| 2 | AI Docker Image | FastAPI image with `/health`, `/ready` and `/metrics` |
| 3 | RunPod Pods | Pod deployment runbook and external endpoint test |
| 4 | Storage and Model Cache | Storage decision matrix and Network Volume/S3 cache test |
| 5 | Model Serving | vLLM/FastAPI service, latency benchmark and tokens/sec report |
| 6 | RunPod Serverless | Worker and endpoint with cold vs warm latency comparison |
| 7 | Automation with CLI/API | build → push → deploy → smoke test pipeline |
| 8 | Production Readiness | Production-like endpoint with monitoring, logging and cost guardrails |

## Repository Structure

```text
.
├── README.md              # Persian overview
├── README.en.md           # English overview
├── docs/                  # Persian docs
├── docs/en/               # English docs
├── labs/                  # Persian lab instructions
├── labs/en/               # English lab instructions
├── sections/              # Runnable starter code for each course section
└── projects/              # Place for learner projects and final submissions
```

## How to Use This Repo

1. Read `docs/roadmap.md` or `docs/en/roadmap.md`.
2. Open the matching lab in `labs/` or `labs/en/`.
3. Use the matching folder under `sections/` for starter code.
4. Put learner work and final submissions under `projects/`.
5. Keep deployments reproducible: image for dependencies, volume/S3 for large models, env vars/secrets for config, scripts/API for deployment.

## Final Project

The final deliverable is an **AI Inference Platform on RunPod** with:

- Custom Docker image
- RunPod template
- Pod deployment
- Serverless endpoint
- Network Volume or S3 storage strategy
- vLLM/FastAPI API
- Health, readiness and metrics endpoints
- Load test / benchmark
- CI/CD script
- Cost report
- Incident runbook

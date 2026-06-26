# Final Skills Checklist

## GPU and Runtime

- [ ] I can read `nvidia-smi` output and explain GPU, driver, VRAM and running processes.
- [ ] I understand host driver vs CUDA runtime inside a container.
- [ ] I have run a container with `--gpus all`.
- [ ] I can distinguish GPU OOM from CPU RAM OOM.
- [ ] I can debug CUDA mismatch and library mismatch issues.

## Docker for AI

- [ ] I have written a GPU-oriented Dockerfile.
- [ ] I know what belongs in the image and what belongs on a volume or S3.
- [ ] I have implemented or tested `/health`, `/ready` and `/metrics`.
- [ ] I can manage image size, startup command, env vars and exposed ports.

## RunPod

- [ ] I have created a GPU Pod.
- [ ] I have connected with SSH, Jupyter or VS Code.
- [ ] I have tested an externally exposed API port.
- [ ] I have deployed or designed a Serverless worker and endpoint.
- [ ] I can explain active workers, max workers, cold start and queue delay.

## Serving and Production

- [ ] I have served a model with vLLM, Ollama or FastAPI.
- [ ] I have measured latency, p95, tokens/sec, TTFT and TPOT.
- [ ] I have monitored VRAM and GPU utilization during inference.
- [ ] I have a CI/CD deployment script or workflow.
- [ ] I have cost guardrails and an incident runbook.

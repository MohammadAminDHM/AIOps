# RunPod Mental Model for AI DevOps

RunPod should be understood as four operational building blocks: Pods, Serverless Endpoints, Templates and Storage.

## Pods

Pods are best for development, testing, light training, long-running jobs and direct GPU debugging.

Expected abilities:

- Choose a GPU based on VRAM and cost
- Connect with SSH, Jupyter or VS Code
- Run an API on an exposed port
- Inspect startup logs and CUDA/OOM errors
- Stop or terminate resources to control cost

## Serverless Endpoints

Serverless is best for product inference APIs and bursty workloads.

Key concepts:

- Worker: request-processing container
- Endpoint: public API entry point
- Active workers: always-warm workers
- Max workers: scale and cost limit
- Cold start: image pull, container start, model cache/download, RAM/VRAM load and warmup
- Queue delay and timeout

## Templates

Templates make environments repeatable. They should define image, env vars, exposed ports, startup command, storage mount path and secrets/registry auth when needed.

## Storage Rule

```text
Stable dependency → Docker image
Large/changeable model → Network Volume / S3
Config and secret → env vars / secrets
Deploy → script / CLI / API / CI/CD
```

# Section 02 — AI Docker Image Starter Code

```bash
docker build -t ai-devops-fastapi:local .
docker run --rm -p 8000:8000 -e MODEL_CACHE_DIR=/models ai-devops-fastapi:local
curl http://localhost:8000/health
curl http://localhost:8000/ready
curl -X POST http://localhost:8000/predict -H 'content-type: application/json' -d '{"prompt":"hello"}'
```

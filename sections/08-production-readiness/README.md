# Section 08 — Production Readiness Starter Code

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
curl http://localhost:8000/health
curl http://localhost:8000/ready
curl http://localhost:8000/metrics
```

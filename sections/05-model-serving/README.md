# Section 05 — Model Serving Starter Code

Start your vLLM/FastAPI server, then run:

```bash
python scripts/benchmark_http.py --url http://localhost:8000/health --requests 20 --concurrency 4
```

Example vLLM command:

```bash
vllm serve Qwen/Qwen2.5-1.5B-Instruct
```

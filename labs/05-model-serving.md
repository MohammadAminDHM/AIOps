# Lab 05 — Model Serving با vLLM / FastAPI

## هدف

مدل را به API قابل استفاده تبدیل کنید و performance آن را اندازه بگیرید.

## گزینه‌های runtime

| Runtime | کاربرد |
| --- | --- |
| vLLM | LLM serving جدی و OpenAI-compatible API |
| Ollama | تست سریع و prototype |
| FastAPI + Transformers | مدل custom یا embedding ساده |
| ComfyUI API | image generation workflow |
| TGI | text generation production |

## تمرین vLLM

```bash
vllm serve Qwen/Qwen2.5-1.5B-Instruct
```

سپس این موارد را تست کنید:

```text
1. /v1/chat/completions
2. latency تک request
3. concurrent requests
4. مصرف VRAM با nvidia-smi
5. /metrics
```

## شاخص‌هایی که باید گزارش شوند

- request count
- error count
- latency p50/p95/p99
- TTFT
- TPOT
- tokens/sec
- GPU memory
- GPU utilization
- queue time

## خروجی هفته

یک benchmark کوتاه و توضیح اینکه bottleneck اصلی latency، VRAM، model load time، queue یا شبکه است.

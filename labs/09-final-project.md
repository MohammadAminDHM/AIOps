# Lab 09 — پروژه نهایی: Deploy یک LLM API روی RunPod

## هدف

یک demo کامل از AI DevOps / LLMOps بسازید که از Docker image تا RunPod Pod، Serverless endpoint، monitoring، benchmark، cost report و incident runbook را پوشش دهد.

## سناریو

```text
یک مدل LLM یا embedding model باید به صورت API بالا بیاید.
کاربر request می‌فرستد.
سرویس پاسخ می‌دهد.
مدل روی GPU اجرا می‌شود.
مدل cache شده و هر بار دانلود نمی‌شود.
endpoint healthcheck، readiness و metrics دارد.
deployment با script یا pipeline انجام می‌شود.
```

## اجزای الزامی

| بخش | الزام |
| --- | --- |
| Docker Image | custom image با dependency ثابت |
| Runtime | vLLM یا FastAPI |
| RunPod Pod | تست اولیه و debug |
| RunPod Serverless | endpoint نهایی |
| Storage | Network Volume یا S3 |
| Monitoring | metrics و structured logs |
| CI/CD | build، push، deploy و smoke test |
| Documentation | runbook کامل و cost report |

## معیار قبولی

نیرو باید بتواند این‌ها را توضیح دهد:

1. چرا این GPU انتخاب شد؟
2. مدل چقدر VRAM مصرف می‌کند؟
3. cold start چقدر است؟
4. اگر request زیاد شود چه اتفاقی می‌افتد؟
5. اگر GPU unavailable شود چه می‌کنیم؟
6. اگر مدل هر بار دانلود شود مشکل کجاست؟
7. فرق Pod و Serverless در این پروژه چیست؟
8. چه چیزی داخل image است و چه چیزی روی volume؟
9. endpoint چطور مانیتور می‌شود؟
10. هزینه چطور کنترل می‌شود؟

## قالب README پروژه نهایی

```markdown
# AI Inference Platform on RunPod

## Problem

## Architecture

## Model and GPU Choice

## Docker Image

## Storage Strategy

## Pod Deployment

## Serverless Endpoint

## Health / Readiness / Metrics

## Benchmark Results

## Cost Report

## Incident Runbook

## Security Notes

## Limitations and Next Steps
```

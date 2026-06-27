# Lab 06 — RunPod Serverless

## هدف

یک inference endpoint مقیاس‌پذیر بسازید و cold start را با warm latency مقایسه کنید.

## مفاهیم کلیدی

- Worker: container پردازش‌کننده request
- Endpoint: URL/API عمومی
- Active Workers: worker همیشه گرم
- Max Workers: سقف scale و هزینه
- Cold Start: آماده شدن کامل container و مدل
- Queue Delay: عامل مهم در scale out
- Timeout: محافظ requestهای سنگین

## تمرین عملی

یک worker بسازید:

```text
input: prompt
output: response
model: small LLM یا embedding model
storage: model cache روی Network Volume یا S3
```

دو حالت را benchmark کنید:

| حالت | انتظار |
| --- | --- |
| `workersMin=0` | cold start بیشتر، هزینه کمتر |
| `workersMin=1` | latency کمتر، هزینه idle بیشتر |

## خروجی هفته

```text
Model:
GPU:
Image size:
Storage strategy:
Cold start:
Warm latency:
p95 latency:
Max concurrency:
Cost behavior:
Failure cases:
```

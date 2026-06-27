# Lab 08 — Production Readiness

## هدف

از «مدل بالا آمده» به «سرویس inference قابل اعتماد» برسید.

## الزامات endpoint

```text
- /health
- /ready
- /metrics
- structured logs
- request id
- timeout
- retry policy
- GPU memory logging
- cost note
```

## مباحث

| حوزه | سؤال کلیدی |
| --- | --- |
| Healthcheck | آیا فقط container بالا است یا مدل هم سالم است؟ |
| Readiness | آیا مدل load شده و GPU آماده است؟ |
| Retry | کدام خطاها transient هستند؟ |
| Timeout | request سنگین چطور کنترل می‌شود؟ |
| Rate Limit | endpoint چطور محافظت می‌شود؟ |
| Logging | prompt length، response time و error reason کجا ثبت می‌شود؟ |
| Monitoring | latency، tokens/sec، queue و GPU memory کجا دیده می‌شود؟ |
| Cost Guardrail | max workers و shutdown policy چیست؟ |
| Security | secret، API key و private registry چطور مدیریت می‌شوند؟ |

## خروجی هفته

یک production readiness checklist و یک incident runbook برای حداقل دو خطا:

1. GPU OOM یا model load failure
2. افزایش p95 latency یا queue time

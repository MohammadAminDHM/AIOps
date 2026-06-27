# Lab 02 — Docker Image مخصوص AI

## هدف

برای یک inference service ساده، image تمیز، قابل deploy و سازگار با GPU بسازید.

## الزامات API

```text
POST /predict
GET /health
GET /ready
GET /metrics
```

## کارها

1. یک FastAPI app کوچک بسازید.
2. endpoint سلامت container و readiness مدل را جدا کنید.
3. مسیر cache مدل را با env var قابل تنظیم کنید.
4. Dockerfile بنویسید.
5. image را build و run کنید.
6. اگر GPU دارید، container را با `--gpus all` تست کنید.

## قانون طراحی

```text
Dependency ثابت → Docker image
Model بزرگ → Network Volume / S3
Config → env vars
Deploy → script/API
```

## خروجی مورد انتظار

- Dockerfile
- دستور build و run
- نمونه response برای `/health` و `/ready`
- توضیح اینکه چه چیزی داخل image است و چه چیزی روی volume/S3 قرار می‌گیرد

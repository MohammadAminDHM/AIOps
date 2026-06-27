# Lab 07 — Automation با runpodctl، REST API و CI/CD

## هدف

deploy دستی حذف شود و همه چیز scriptable باشد.

## ابزارها

| ابزار | کاربرد |
| --- | --- |
| runpodctl | مدیریت Pod، Endpoint، Template، Volume و diagnostics |
| REST API | automation از CI/CD و سیستم‌های داخلی |
| GitHub Actions / GitLab CI | build و deploy |
| Docker Registry | نگهداری image |
| Secrets | API key، token و env vars |

## pipeline پیشنهادی

```text
git push
  ↓
build docker image
  ↓
push to registry
  ↓
update RunPod template
  ↓
deploy endpoint
  ↓
smoke test
  ↓
report result
```

## ساختار repo نمونه

```text
ai-devops-runpod-demo/
├── app/
│   ├── main.py
│   └── model.py
├── Dockerfile
├── requirements.txt
├── runpod/
│   ├── worker.py
│   ├── endpoint_config.json
│   └── deploy.sh
├── .github/workflows/
│   └── deploy.yml
└── README.md
```

## خروجی هفته

- script deploy
- smoke test
- مستندات secrets
- rollback یا teardown command

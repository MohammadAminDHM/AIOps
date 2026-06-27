# Lab 03 — RunPod Pods

## هدف

یک GPU Pod بسازید، به آن وصل شوید، سرویس را بالا بیاورید و endpoint را از بیرون تست کنید.

## سناریو

```text
1. ساخت Pod با GPU مناسب مثل RTX 4090 یا A100
2. انتخاب template یا custom image
3. اتصال با SSH
4. اجرای FastAPI یا vLLM
5. باز کردن port
6. تست endpoint از بیرون
7. stop/terminate برای کنترل هزینه
```

## دستورهای debug پیشنهادی

```bash
nvidia-smi
df -h
du -sh /workspace /runpod-volume 2>/dev/null || true
printenv | sort
curl -f http://localhost:8000/health
```

## خروجی هفته

```text
RunPod Pod Deployment Runbook
- GPU انتخابی و دلیل آن
- template/image
- env vars
- exposed ports
- startup command
- storage path
- debug commands
- teardown checklist
- cost note
```

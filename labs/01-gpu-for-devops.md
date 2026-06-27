# Lab 01 — GPU برای DevOps

## هدف

بفهمید چرا deployment مدل AI با deployment یک web service معمولی فرق دارد.

## مباحث

- CUDA، Driver، VRAM و GPU utilization
- تفاوت CUDA runtime داخل container با driver روی host
- اجرای container با GPU
- خطاهای CUDA mismatch، OOM و library mismatch

## تمرین عملی

```bash
docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi
```

اگر این دستور اجرا نشد، failure را مستند کنید:

- آیا NVIDIA Container Toolkit نصب است؟
- آیا host driver درست نصب شده؟
- آیا GPU در اختیار container قرار گرفته؟
- آیا خطا از runtime است یا image؟

## پرسش‌های تحویل

1. چرا container خودش driver کامل ندارد؟
2. چرا CUDA version مهم است؟
3. چرا بعضی مدل‌ها روی یک GPU بالا می‌آیند ولی روی GPU دیگر نه؟
4. فرق VRAM OOM با CPU RAM OOM چیست؟

## خروجی هفته

```text
GPU Debug Checklist:
- driver version
- CUDA version
- nvidia-smi output
- container runtime
- visible devices
- VRAM free/used
- model size
- quantization
```

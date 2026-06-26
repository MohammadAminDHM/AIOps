# Lab 00 — آماده‌سازی محیط AI DevOps

## هدف

محیط پایه برای تمرین‌های GPU، Docker و RunPod آماده شود.

## کارها

1. نسخه Git، Docker و Python را بررسی کنید.
2. اگر GPU محلی دارید، `nvidia-smi` را اجرا کنید.
3. اگر GPU محلی ندارید، آماده باشید تمرین‌های GPU را روی RunPod Pod انجام دهید.
4. یک Docker Registry برای imageهای آموزشی انتخاب کنید.
5. یک روش امن برای نگهداری API keyها و secretها مشخص کنید.

## دستورات پیشنهادی

```bash
git --version
docker --version
python --version
nvidia-smi
```

## خروجی مورد انتظار

- فهرست ابزارهای نصب‌شده و نسخه‌ها
- تصمیم درباره registry
- یادداشت درباره محل نگهداری secretها

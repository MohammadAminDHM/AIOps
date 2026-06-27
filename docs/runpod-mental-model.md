# نقشه ذهنی RunPod برای AI DevOps

RunPod در این مسیر آموزشی به‌عنوان محیط اصلی GPU deployment استفاده می‌شود. نیرو باید RunPod را در چهار بخش بفهمد: Pods، Serverless Endpoints، Templates و Storage.

## Pods

Pods برای توسعه، تست، training سبک، jobs طولانی و debug مستقیم روی GPU مناسب‌اند.

خروجی مورد انتظار:

- انتخاب GPU مناسب مثل RTX 4090 یا A100 بر اساس VRAM و هزینه
- اتصال با SSH، Jupyter یا VS Code
- اجرای API روی port مشخص
- دیدن logهای startup و خطاهای CUDA/OOM
- stop یا terminate برای کنترل هزینه

## Serverless Endpoints

Serverless برای inference API محصولی و workloadهای bursty مناسب است.

نیرو باید این مفاهیم را بداند:

- worker: container پردازش‌کننده request
- endpoint: ورودی عمومی/API
- active workers: workerهای همیشه گرم
- max workers: سقف scale و هزینه
- cold start: pull image، start container، download/cache model، load to RAM/VRAM و warmup
- queue delay و timeout

## Templates

Template باید محیط را تکرارپذیر کند.

موارد ضروری:

- Docker image
- env vars
- exposed ports
- startup command
- storage mount path
- secrets و registry auth در صورت نیاز

## Storage

| نوع storage | کاربرد |
| --- | --- |
| Container Disk | پردازش موقت و cache کوتاه‌مدت |
| Network Volume | model weights، dataset، checkpoint و cache پایدار |
| S3-compatible | فایل‌های بزرگ، backup، exchange بین region/datacenter |

## قانون طراحی

```text
Dependency ثابت → Docker image
Model بزرگ و قابل تغییر → Network Volume / S3
Config و secret → env vars / secrets
Deploy → script / CLI / API / CI-CD
```

## هشدار عملیاتی

Network Volume برای cache مدل عالی است، اما می‌تواند deployment را به دیتاسنتر همان volume محدود کند. بنابراین برای availability و failover باید از S3 یا چند volume در چند دیتاسنتر هم فکر کرد.

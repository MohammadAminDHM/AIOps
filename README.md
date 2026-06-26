# AIOps — مسیر آموزشی AI DevOps / LLMOps با محور RunPod

این ریپو یک مسیر آموزشی عملی برای نیرویی است که **DevOps بلد است** و حالا باید به **AI DevOps / LLMOps Engineer** تبدیل شود؛ نه Data Scientist.

هدف دوره این است که نیرو بتواند یک مدل AI/LLM را بگیرد، کانتینری کند، روی GPU و RunPod deploy کند، storage و cache و model loading را درست طراحی کند، endpoint پایدار بدهد، latency و هزینه را کنترل کند و در زمان خرابی بفهمد مشکل از کجاست.

## تعریف نقش

این مسیر روی مهارت‌های عملیاتی AI تمرکز دارد:

| حوزه | خروجی مورد انتظار |
| --- | --- |
| GPU Infrastructure | فهم CUDA، Driver، VRAM، `nvidia-smi` و GPU utilization |
| Docker for AI | ساخت image سازگار با GPU و NVIDIA runtime |
| Model Serving | بالا آوردن مدل با vLLM، Ollama، FastAPI، ComfyUI یا TGI |
| RunPod Pods | ساخت محیط توسعه و تست GPU با SSH، Jupyter یا VS Code |
| RunPod Serverless | ساخت inference API مقیاس‌پذیر با worker و endpoint |
| Storage | مدیریت model weights، dataset و cache روی Network Volume یا S3 |
| Observability | مانیتور latency، tokens/sec، queue، cold start و GPU memory |
| Cost Control | انتخاب درست بین Pod و Serverless و تنظیم active/max workers |
| CI/CD | خودکارسازی build، push، deploy، smoke test و rollback |

## نقشه ذهنی RunPod

```text
AI DevOps روی RunPod
│
├── Pods
│   ├── مناسب توسعه، تست، training و long-running jobs
│   ├── SSH / Jupyter / VS Code
│   └── کنترل کامل روی محیط GPU
│
├── Serverless Endpoints
│   ├── مناسب inference API
│   ├── auto-scaling workers
│   ├── queue-based یا load-balancing
│   └── مدیریت cold start و concurrency
│
├── Templates
│   ├── Docker image آماده یا سفارشی
│   ├── env vars
│   ├── exposed ports
│   └── startup command
│
├── Storage
│   ├── Container Disk: سریع ولی موقت
│   ├── Network Volume: پایدار برای مدل و دیتاست
│   └── S3-compatible: برای فایل‌های بزرگ و external storage
│
└── Automation
    ├── runpodctl
    ├── REST API
    ├── CI/CD
    └── monitoring / cost control
```

## مسیر ۸ هفته‌ای

| هفته | تمرکز | خروجی عملی |
| --- | --- | --- |
| 1 | GPU برای DevOps | GPU debug checklist و اجرای container با `--gpus` |
| 2 | Docker Image مخصوص AI | FastAPI image با `/health`، `/ready` و `/metrics` |
| 3 | RunPod Pods | Pod deployment runbook و تست endpoint بیرونی |
| 4 | Storage و Model Cache | تصمیم‌نامه storage و تست Network Volume / S3 |
| 5 | Model Serving | سرویس vLLM/FastAPI، benchmark latency و tokens/sec |
| 6 | RunPod Serverless | worker و endpoint با مقایسه cold/warm latency |
| 7 | Automation با CLI/API | pipeline build → push → deploy → smoke test |
| 8 | Production Readiness | endpoint production-like با monitoring، logging و cost guardrail |

## ساختار ریپو

```text
.
├── README.md
├── README.en.md
├── docs/
│   ├── glossary.md
│   ├── learning-checklist.md
│   ├── references.md
│   ├── roadmap.md
│   └── runpod-mental-model.md
├── labs/
    ├── 00-setup.md
    ├── 01-gpu-for-devops.md
    ├── 02-ai-docker-image.md
    ├── 03-runpod-pods.md
    ├── 04-storage-model-cache.md
    ├── 05-model-serving.md
    ├── 06-runpod-serverless.md
    ├── 07-automation-cli-api.md
    ├── 08-production-readiness.md
    └── 09-final-project.md
├── sections/
│   ├── 01-gpu-for-devops/
│   ├── 02-ai-docker-image/
│   ├── 03-runpod-pods/
│   ├── 04-storage-model-cache/
│   ├── 05-model-serving/
│   ├── 06-runpod-serverless/
│   ├── 07-automation-cli-api/
│   ├── 08-production-readiness/
│   └── 09-final-project-template/
└── projects/
    └── README.md
```


## نسخه انگلیسی و کدهای هر بخش

- نسخه انگلیسی مسیر در `README.en.md` و پوشه `docs/en/` قرار دارد.
- برای هر بخش آموزشی، یک فولدر متناظر در `sections/` ساخته شده که starter code، اسکریپت یا template اصلی همان بخش را نگه می‌دارد.
- پروژه‌های تمرینی و پروژه نهایی نیروها باید داخل `projects/` قرار بگیرند.

## ترتیب یادگیری خیلی عملی

1. **AI Infra:** Linux GPU، Docker GPU، CUDA/Driver، `nvidia-smi`، VRAM debugging
2. **RunPod عملیاتی:** Pods، Templates، SSH، Ports، Network Volumes، `runpodctl`، REST API
3. **Serving:** FastAPI، vLLM، Ollama، OpenAI-compatible APIs، batching، concurrency، tokens/sec
4. **Serverless:** Worker، Endpoint، cold start، active workers، max workers، queue delay، timeout
5. **Production:** CI/CD، monitoring، logs، cost control، security، runbook و incident handling

## پروژه نهایی

پروژه نهایی دوره، ساخت یک **AI Inference Platform on RunPod** است:

```text
AI Inference Platform on RunPod
│
├── Custom Docker Image
├── RunPod Template
├── Pod Deployment
├── Serverless Endpoint
├── Network Volume یا S3
├── vLLM/FastAPI API
├── Healthcheck / Readiness / Metrics
├── Load Test
├── CI/CD Script
├── Cost Report
└── Incident Runbook
```

## معیار قبولی نیرو

نیرو وقتی آماده است که بتواند به این سؤال‌ها دقیق جواب بدهد:

1. چرا این GPU انتخاب شد؟
2. مدل چقدر VRAM مصرف می‌کند؟
3. cold start چقدر است و از چه بخش‌هایی تشکیل می‌شود؟
4. اگر request زیاد شود چه اتفاقی می‌افتد؟
5. اگر GPU unavailable شود چه می‌کنیم؟
6. اگر مدل هر بار دانلود شود مشکل کجاست؟
7. فرق Pod و Serverless در این پروژه چیست؟
8. چه چیزی داخل image است و چه چیزی روی volume یا object storage؟
9. endpoint چطور مانیتور می‌شود؟
10. هزینه چطور کنترل می‌شود؟

## ضدالگوهایی که از روز اول باید جلوی آن‌ها گرفته شود

- نصب دستی داخل Pod به جای image و script تکرارپذیر
- گذاشتن model weights بزرگ داخل Docker image
- بی‌توجهی به cold start و model load time
- مانیتور کردن صرفاً GPU utilization و ندیدن TTFT، TPOT، tokens/sec، queue time و p95 latency
- deploy دستی بدون CLI/API/CI-CD
- نداشتن shutdown policy و cost guardrail

## جمع‌بندی

برای نیروی DevOps، مسیر را از ML سنگین شروع نکنید. اول **GPU + Docker + RunPod + Serving + Monitoring** را عملی کنید؛ بعد اگر واقعاً لازم شد سراغ Kubernetes، Ray، Triton، multi-node training یا autoscaling پیشرفته بروید.

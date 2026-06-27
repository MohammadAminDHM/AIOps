# نقشه راه ۸ هفته‌ای AI DevOps / LLMOps با محور RunPod

این مسیر برای کسی طراحی شده که DevOps بلد است و باید بتواند سرویس‌های AI/LLM را روی GPU و RunPod عملیاتی کند.

## هفته ۱ — GPU برای DevOps

**هدف:** فهم تفاوت AI deployment با web deployment.

مباحث:

- CUDA Core، Tensor Core، VRAM و Memory Bandwidth
- تفاوت driver host و CUDA داخل container
- خواندن `nvidia-smi`: memory، utilization و processها
- اجرای Docker container با GPU
- خطاهای CUDA mismatch، OOM و driver/library mismatch

خروجی: `GPU Debug Checklist` شامل driver version، CUDA version، visible devices، VRAM free/used، model size و quantization.

## هفته ۲ — Docker Image مخصوص AI

**هدف:** ساخت image تمیز، قابل deploy و سازگار با GPU.

مباحث:

- انتخاب base image مثل `nvidia/cuda` یا `pytorch/pytorch`
- مدیریت Python environment با venv، pip، uv یا poetry
- cache مدل در مسیرهایی مثل `/models`، `/workspace` یا `/runpod-volume`
- entrypoint و startup command
- expose کردن API و healthcheck
- کم کردن image size

خروجی: FastAPI image با endpointهای `POST /predict`، `GET /health`، `GET /ready` و `GET /metrics`.

## هفته ۳ — RunPod Pods

**هدف:** ساخت Pod، اتصال، اجرای مدل و debug روی GPU.

مباحث:

- انتخاب GPU، template و disk
- اتصال با SSH، Jupyter یا VS Code
- باز کردن port و تست endpoint از بیرون
- خواندن logهای startup
- stop/terminate برای کنترل هزینه
- ساخت template تکرارپذیر

خروجی: `RunPod Pod Deployment Runbook` شامل GPU، template، env vars، ports، startup command، storage path، debug commands و teardown checklist.

## هفته ۴ — Storage، Volume و Model Cache

**هدف:** جلوگیری از دانلود تکراری مدل و طراحی storage درست.

مباحث:

- Container Disk برای کار موقت
- Network Volume برای مدل، dataset، checkpoint و cache پایدار
- S3-compatible storage برای فایل‌های بزرگ، backup و artifact exchange
- اثر locality دیتاسنتر روی availability و failover

خروجی: تصمیم‌نامه storage برای سناریوهای تست سریع، مدل بزرگ، چند دیتاسنتر، artifact بلندمدت و checkpoint آموزشی.

## هفته ۵ — Model Serving

**هدف:** تبدیل مدل به API قابل استفاده.

Runtimeهای پیشنهادی:

| Runtime | کاربرد |
| --- | --- |
| vLLM | LLM serving جدی و پرسرعت |
| Ollama | تست سریع و prototype |
| FastAPI + Transformers | مدل‌های custom |
| ComfyUI API | image generation workflow |
| TGI | text generation production |

خروجی: سرویس vLLM یا FastAPI با اندازه‌گیری latency، concurrent requests، VRAM و endpoint `/metrics`.

## هفته ۶ — RunPod Serverless

**هدف:** ساخت inference endpoint مقیاس‌پذیر.

مباحث:

- worker و endpoint
- active workers و max workers
- cold start، warm latency و queue delay
- timeout و failure handling
- cache مدل روی Network Volume یا object storage

خروجی: benchmark مقایسه‌ای بین `workersMin=0` و `workersMin=1` شامل cold start، warm latency، p95 latency، max concurrency، هزینه و failure cases.

## هفته ۷ — Automation با CLI و API

**هدف:** حذف deploy دستی و scriptable کردن عملیات.

مباحث:

- `runpodctl` برای مدیریت Pod، Endpoint، Template و Volume
- REST API برای automation از CI/CD
- Docker Registry و private image
- secrets، API key و env vars
- smoke test بعد از deploy

خروجی: pipeline با جریان `git push → build image → push registry → update template → deploy endpoint → smoke test → report`.

## هفته ۸ — Production Readiness

**هدف:** تبدیل «مدل بالا آمده» به «سرویس قابل اعتماد».

مباحث:

- healthcheck واقعی در برابر container-only health
- readiness بر اساس load شدن مدل و آماده بودن GPU
- timeout، retry، rate limit و request id
- structured logging شامل prompt length، response time و error reason
- monitoring برای latency، tokens/sec، queue time، GPU memory و cost
- security برای secret، API key و private registry

خروجی: endpoint production-like با `/health`، `/ready`، `/metrics`، structured logs، timeout، retry policy، GPU memory logging و cost note.

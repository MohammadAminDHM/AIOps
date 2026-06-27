# واژه‌نامه AI DevOps / LLMOps

## AI DevOps / LLMOps Engineer

نقشی عملیاتی که مدل AI/LLM را کانتینری، deploy، monitor و debug می‌کند و مسئول latency، cost، reliability، storage و automation سرویس inference است.

## GPU Driver

درایور نصب‌شده روی host که امکان ارتباط سیستم‌عامل و container runtime با GPU را فراهم می‌کند. container معمولاً driver کامل را با خود حمل نمی‌کند.

## CUDA

لایه نرم‌افزاری NVIDIA برای اجرای محاسبات روی GPU. سازگاری CUDA runtime داخل container با driver host در خطاهای AI deployment بسیار مهم است.

## VRAM

حافظه GPU. وزن مدل، KV cache، batch و tensorهای inference داخل VRAM جا می‌گیرند و کمبود آن باعث GPU OOM می‌شود.

## `nvidia-smi`

ابزار اصلی debug برای دیدن GPU، driver، memory usage، utilization و processهای فعال.

## GPU OOM

خطای کمبود VRAM. با CPU RAM OOM فرق دارد و معمولاً با مدل کوچک‌تر، quantization، batch کمتر یا GPU با VRAM بیشتر کنترل می‌شود.

## Pod

در RunPod محیط compute مستقیم و قابل‌سفارشی‌سازی برای توسعه، تست، training یا job طولانی روی GPU.

## Serverless Endpoint

در RunPod ورودی API برای inference که requestها را به workerها می‌دهد و می‌تواند بر اساس queue/concurrency scale شود.

## Worker

container پردازش‌کننده request در Serverless. worker باید مدل را load کند، inference انجام دهد و خروجی برگرداند.

## Active Worker

worker همیشه روشن برای حذف یا کاهش cold start. سرعت را بهتر می‌کند اما هزینه idle دارد.

## Cold Start

زمان آماده شدن کامل سرویس از pull/start container تا download/cache model، load مدل در RAM/VRAM و warmup inference.

## Network Volume

storage پایدار برای مدل، dataset، checkpoint و cache. برای جلوگیری از دانلود تکراری مدل مفید است ولی locality دیتاسنتر آن روی availability اثر دارد.

## S3-compatible Storage

object storage مناسب فایل‌های بزرگ، backup، artifact exchange و سناریوهای چند دیتاسنتری.

## vLLM

runtime پرکاربرد برای LLM serving با OpenAI-compatible API و metric endpoint برای production monitoring.

## TTFT

Time To First Token؛ مدت زمان تا دریافت اولین توکن خروجی در LLM serving.

## TPOT

Time Per Output Token؛ زمان متوسط تولید هر توکن خروجی.

## Tokens/sec

توان عملیاتی تولید توکن. یکی از شاخص‌های مهم performance در LLM inference.

## Runbook

راهنمای عملیاتی مرحله‌به‌مرحله برای deploy، debug، rollback، teardown و پاسخ به incident.

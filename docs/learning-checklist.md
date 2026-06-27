# چک‌لیست مهارت‌های پایان دوره

این چک‌لیست برای ارزیابی نیروی DevOps طراحی شده که باید به AI DevOps / LLMOps Engineer تبدیل شود.

## GPU و Runtime

- [ ] خروجی `nvidia-smi` را می‌خوانم و GPU، driver، VRAM و processها را توضیح می‌دهم.
- [ ] تفاوت driver host و CUDA داخل container را می‌دانم.
- [ ] container را با `--gpus all` اجرا کرده‌ام.
- [ ] GPU OOM را از CPU RAM OOM تشخیص می‌دهم.
- [ ] خطاهای CUDA mismatch و library mismatch را مرحله‌به‌مرحله debug می‌کنم.

## Docker for AI

- [ ] Dockerfile مخصوص GPU نوشته‌ام.
- [ ] می‌دانم چه چیزی باید داخل image باشد و چه چیزی روی volume/S3.
- [ ] endpointهای `/health`، `/ready` و `/metrics` را پیاده یا تست کرده‌ام.
- [ ] image size، startup command، env vars و exposed ports را مدیریت می‌کنم.
- [ ] نصب دستی داخل Pod را با image/script تکرارپذیر جایگزین کرده‌ام.

## RunPod Pods

- [ ] Pod با GPU مناسب ساخته‌ام.
- [ ] با SSH، Jupyter یا VS Code وصل شده‌ام.
- [ ] API را روی port مشخص از بیرون تست کرده‌ام.
- [ ] logهای startup و خطاهای model loading را بررسی کرده‌ام.
- [ ] stop/terminate و teardown checklist برای کنترل هزینه دارم.

## Storage و Cache

- [ ] تفاوت Container Disk، Network Volume و S3-compatible storage را می‌دانم.
- [ ] مدل را روی volume یا object storage cache کرده‌ام.
- [ ] Pod جدید را بدون دانلود دوباره مدل اجرا کرده‌ام.
- [ ] اثر دیتاسنتر/volume locality روی availability را توضیح می‌دهم.
- [ ] برای model weights، dataset، checkpoint و artifact strategy دارم.

## Model Serving

- [ ] یک مدل را با vLLM، Ollama یا FastAPI بالا آورده‌ام.
- [ ] OpenAI-compatible endpoint را تست کرده‌ام.
- [ ] latency، p95، tokens/sec، TTFT و TPOT را اندازه‌گیری کرده‌ام.
- [ ] VRAM و GPU utilization را هنگام inference مانیتور کرده‌ام.
- [ ] `/metrics` یا خروجی قابل scrape برای monitoring دارم.

## RunPod Serverless

- [ ] worker و endpoint ساخته‌ام.
- [ ] تفاوت `workersMin=0` و `workersMin=1` را benchmark کرده‌ام.
- [ ] cold start و warm latency را گزارش کرده‌ام.
- [ ] max workers، timeout و queue delay را تنظیم یا تحلیل کرده‌ام.
- [ ] failure cases و cost behavior را مستند کرده‌ام.

## Automation و CI/CD

- [ ] با `runpodctl` یا REST API کار کرده‌ام.
- [ ] build و push Docker image را خودکار کرده‌ام.
- [ ] update template یا deploy endpoint را script کرده‌ام.
- [ ] smoke test بعد از deploy اجرا می‌شود.
- [ ] secrets و API key را داخل کد hardcode نکرده‌ام.

## Production Readiness

- [ ] healthcheck و readiness واقعی دارم.
- [ ] structured logs با request id، latency، prompt length و error reason تولید می‌کنم.
- [ ] timeout، retry و rate limit را طراحی کرده‌ام.
- [ ] cost guardrail مثل max workers و shutdown policy دارم.
- [ ] incident runbook و rollback/teardown procedure نوشته‌ام.

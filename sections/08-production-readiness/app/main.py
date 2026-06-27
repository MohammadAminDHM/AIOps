import logging
import os
import time
import uuid
from typing import Any

from fastapi import FastAPI, Request
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, Gauge, generate_latest
from starlette.responses import Response

logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"), format="%(message)s")
logger = logging.getLogger("ai-devops-prod")

app = FastAPI(title="Production Readiness Starter")
STARTED_AT = time.time()
MODEL_LOADED = os.getenv("MODEL_LOADED", "true").lower() == "true"

REQUESTS = Counter("inference_requests_total", "Inference requests", ["path", "status"])
LATENCY = Histogram("inference_latency_seconds", "Inference latency", ["path"])
GPU_MEMORY_BYTES = Gauge("gpu_memory_bytes", "GPU memory placeholder gauge")


@app.middleware("http")
async def add_request_logging(request: Request, call_next):
    request_id = request.headers.get("x-request-id", str(uuid.uuid4()))
    started = time.time()
    response = await call_next(request)
    elapsed = time.time() - started
    REQUESTS.labels(path=request.url.path, status=str(response.status_code)).inc()
    LATENCY.labels(path=request.url.path).observe(elapsed)
    logger.info({"request_id": request_id, "path": request.url.path, "status": response.status_code, "latency_ms": round(elapsed * 1000, 3)})
    response.headers["x-request-id"] = request_id
    return response


@app.get("/health")
def health() -> dict[str, Any]:
    return {"status": "ok", "uptime_seconds": round(time.time() - STARTED_AT, 3)}


@app.get("/ready")
def ready() -> dict[str, Any]:
    return {"ready": MODEL_LOADED}


@app.post("/predict")
def predict(payload: dict[str, Any]) -> dict[str, Any]:
    prompt = str(payload.get("prompt", ""))
    return {"output": f"echo: {prompt}", "prompt_length": len(prompt)}


@app.get("/metrics")
def metrics() -> Response:
    GPU_MEMORY_BYTES.set(float(os.getenv("GPU_MEMORY_BYTES", "0")))
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

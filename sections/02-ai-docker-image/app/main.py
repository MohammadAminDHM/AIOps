import os
import time
from typing import Any

from fastapi import FastAPI
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest
from starlette.responses import Response

APP_STARTED_AT = time.time()
MODEL_CACHE_DIR = os.getenv("MODEL_CACHE_DIR", "/models")
MODEL_READY = os.getenv("MODEL_READY", "true").lower() == "true"

REQUESTS = Counter("ai_requests_total", "Total inference requests", ["endpoint"])
LATENCY = Histogram("ai_request_latency_seconds", "Inference request latency", ["endpoint"])

app = FastAPI(title="AI DevOps Starter API")


@app.get("/health")
def health() -> dict[str, Any]:
    return {"status": "ok", "uptime_seconds": round(time.time() - APP_STARTED_AT, 3)}


@app.get("/ready")
def ready() -> dict[str, Any]:
    return {"ready": MODEL_READY, "model_cache_dir": MODEL_CACHE_DIR}


@app.post("/predict")
def predict(payload: dict[str, Any]) -> dict[str, Any]:
    started = time.time()
    REQUESTS.labels(endpoint="predict").inc()
    prompt = str(payload.get("prompt", ""))
    result = {"output": f"echo: {prompt}", "prompt_length": len(prompt)}
    LATENCY.labels(endpoint="predict").observe(time.time() - started)
    return result


@app.get("/metrics")
def metrics() -> Response:
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

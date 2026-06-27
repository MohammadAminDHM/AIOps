import os
import time
from typing import Any


def handler(event: dict[str, Any]) -> dict[str, Any]:
    started = time.time()
    payload = event.get("input", {})
    prompt = payload.get("prompt", "")
    model_name = os.getenv("MODEL_NAME", "demo-model")
    return {
        "model": model_name,
        "response": f"echo: {prompt}",
        "latency_ms": round((time.time() - started) * 1000, 3),
    }

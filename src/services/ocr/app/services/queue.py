from __future__ import annotations

import json
from typing import Any

from redis.asyncio import Redis

from app.core.config import settings

STATUS_QUEUED = "queued"
STATUS_PROCESSING = "processing"
STATUS_COMPLETED = "completed"
STATUS_FAILED = "failed"


def status_key(job_id: str) -> str:
    return f"ocr:status:{job_id}"


def result_key(job_id: str) -> str:
    return f"ocr:result:{job_id}"


def payload_key(job_id: str) -> str:
    return f"ocr:payload:{job_id}"


async def set_status(redis: Redis, job_id: str, status: str) -> None:
    await redis.set(status_key(job_id), status, ex=settings.ocr_result_ttl_seconds)


async def get_status(redis: Redis, job_id: str) -> str | None:
    value = await redis.get(status_key(job_id))
    return value.decode() if isinstance(value, bytes) else value


async def store_payload(redis: Redis, job_id: str, payload: dict[str, Any]) -> None:
    await redis.set(payload_key(job_id), json.dumps(payload), ex=settings.ocr_result_ttl_seconds)


async def load_payload(redis: Redis, job_id: str) -> dict[str, Any] | None:
    raw = await redis.get(payload_key(job_id))
    if raw is None:
        return None
    return json.loads(raw)


async def store_result(redis: Redis, job_id: str, result: dict[str, Any]) -> None:
    await redis.set(result_key(job_id), json.dumps(result, default=str), ex=settings.ocr_result_ttl_seconds)


async def load_result(redis: Redis, job_id: str) -> dict[str, Any] | None:
    raw = await redis.get(result_key(job_id))
    if raw is None:
        return None
    return json.loads(raw)

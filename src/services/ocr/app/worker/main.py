from __future__ import annotations

from arq.connections import RedisSettings
from redis.asyncio import Redis

from app.core.config import settings
from app.worker.tasks import process_ocr_job


async def startup(ctx: dict) -> None:
    ctx["redis"] = Redis.from_url(settings.redis_url, decode_responses=False)


async def shutdown(ctx: dict) -> None:
    redis: Redis = ctx.get("redis")
    if redis is not None:
        await redis.close()


class WorkerSettings:
    functions = [process_ocr_job]
    on_startup = startup
    on_shutdown = shutdown
    redis_settings = RedisSettings.from_dsn(settings.redis_url)

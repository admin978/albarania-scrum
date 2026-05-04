from __future__ import annotations

from contextlib import asynccontextmanager

from arq import create_pool
from arq.connections import RedisSettings
from fastapi import FastAPI
from redis.asyncio import Redis

from app.api.routes import health, scan
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = Redis.from_url(settings.redis_url, decode_responses=False)
    arq_pool = await create_pool(RedisSettings.from_dsn(settings.redis_url))

    app.state.redis = redis
    app.state.arq_pool = arq_pool

    try:
        yield
    finally:
        await arq_pool.close()
        await redis.close()


app = FastAPI(title="AlbaranIA OCR", version="0.1.0", lifespan=lifespan)

app.include_router(health.router)
app.include_router(scan.router)

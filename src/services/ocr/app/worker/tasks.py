from __future__ import annotations

import base64
import logging
from typing import Any

from app.services import queue
from app.services.ocr import extract_albaran

logger = logging.getLogger(__name__)


async def process_ocr_job(ctx: dict[str, Any], job_id: str) -> None:
    redis = ctx["redis"]

    payload = await queue.load_payload(redis, job_id)
    if payload is None:
        logger.warning("payload missing for job_id=%s", job_id)
        await queue.set_status(redis, job_id, queue.STATUS_FAILED)
        return

    await queue.set_status(redis, job_id, queue.STATUS_PROCESSING)

    try:
        file_bytes = base64.b64decode(payload["file_b64"])
        result = await extract_albaran(
            file_bytes=file_bytes,
            content_type=payload["content_type"],
            empresa_nombre=payload.get("empresa_nombre", ""),
            empresa_cif=payload.get("empresa_cif", ""),
        )
        await queue.store_result(redis, job_id, result.model_dump(mode="json"))
        await queue.set_status(redis, job_id, queue.STATUS_COMPLETED)
    except Exception:
        logger.exception("OCR job failed: %s", job_id)
        await queue.set_status(redis, job_id, queue.STATUS_FAILED)
        raise

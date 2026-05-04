from __future__ import annotations

import base64
import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, Request, UploadFile, status

from app.core.auth import AuthContext, require_role
from app.core.config import settings
from app.services import queue

router = APIRouter()

ALLOWED_CONTENT_TYPES = {"application/pdf", "image/png", "image/jpeg"}


@router.post("/scan", status_code=status.HTTP_202_ACCEPTED)
async def enqueue_scan(
    request: Request,
    file: Annotated[UploadFile, File(...)],
    ctx: Annotated[AuthContext, Depends(require_role("Admin", "Operario"))],
) -> dict[str, str]:
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"Content type {file.content_type} no soportado",
        )

    raw = await file.read()
    if len(raw) > settings.ocr_max_file_size_mb * 1024 * 1024:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"Archivo excede {settings.ocr_max_file_size_mb} MB",
        )

    job_id = str(uuid.uuid4())
    payload = {
        "empresa_id": ctx.empresa_id,
        "user_id": ctx.user_id,
        "content_type": file.content_type,
        "file_b64": base64.b64encode(raw).decode("ascii"),
    }

    redis = request.app.state.redis
    arq_pool = request.app.state.arq_pool

    await queue.store_payload(redis, job_id, payload)
    await queue.set_status(redis, job_id, queue.STATUS_QUEUED)
    await arq_pool.enqueue_job("process_ocr_job", job_id)

    return {"job_id": job_id, "status": queue.STATUS_QUEUED}


@router.get("/scan/status/{job_id}")
async def scan_status(
    request: Request,
    job_id: str,
    ctx: Annotated[AuthContext, Depends(require_role("Admin", "Operario", "Supervisor"))],
):
    redis = request.app.state.redis

    payload = await queue.load_payload(redis, job_id)
    if payload is None or payload.get("empresa_id") != ctx.empresa_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="job_id desconocido")

    job_status = await queue.get_status(redis, job_id)

    if job_status == queue.STATUS_COMPLETED:
        result = await queue.load_result(redis, job_id)
        return {"job_id": job_id, "status": job_status, "result": result}

    if job_status == queue.STATUS_FAILED:
        return {"job_id": job_id, "status": job_status}

    return {"job_id": job_id, "status": job_status or queue.STATUS_PROCESSING}

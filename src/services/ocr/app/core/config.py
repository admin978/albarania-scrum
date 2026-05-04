import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    jwt_secret: str
    openai_api_key: str
    redis_url: str
    ocr_result_ttl_seconds: int
    ocr_max_file_size_mb: int


def _required(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Missing required env var: {name}")
    return value


settings = Settings(
    jwt_secret=_required("JWT_SECRET") if os.environ.get("APP_ENV") != "test" else os.environ.get("JWT_SECRET", "test-secret"),
    openai_api_key=os.environ.get("OPENAI_API_KEY", "test-key"),
    redis_url=os.environ.get("REDIS_URL", "redis://localhost:6379/0"),
    ocr_result_ttl_seconds=int(os.environ.get("OCR_RESULT_TTL_SECONDS", "3600")),
    ocr_max_file_size_mb=int(os.environ.get("OCR_MAX_FILE_SIZE_MB", "10")),
)

from __future__ import annotations

import base64
import json
import logging
from io import BytesIO
from typing import Any

from openai import AsyncOpenAI
from pdf2image import convert_from_bytes

from app.core.config import settings
from app.schemas.albaran import AlbaranExtraido

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """Eres un extractor determinista de datos de albaranes en español.

Reglas estrictas:
- Devuelve EXCLUSIVAMENTE un JSON válido, sin markdown, sin explicación.
- Si un campo no está presente en el albarán, devuelve `null`. NUNCA inventes datos.
- Importes en EUR, números decimales con punto. Fechas en formato `YYYY-MM-DD`.
- Si el documento no parece un albarán (factura, presupuesto, otro), pon `es_albaran: false` y `confianza_extraccion` baja (<0.4).
- Las unidades válidas son: ud, kg, m, l, h, pack. Si no encaja, usa `ud`.

Schema obligatorio:
{
  "es_albaran": bool,
  "confianza_extraccion": float (0..1),
  "numero_documento": str | null,
  "fecha": "YYYY-MM-DD" | null,
  "proveedor_nombre": str | null,
  "proveedor_cif": str | null,
  "base_imponible": number,
  "iva_total": number,
  "importe_total": number,
  "lineas": [
    {"descripcion": str, "cantidad": number, "unidad": str, "precio_unitario": number, "subtotal": number}
  ],
  "observaciones": str | null
}
"""


def _user_prompt(empresa_nombre: str, empresa_cif: str) -> str:
    return (
        f"Procesa este albarán para la empresa receptora:\n"
        f"- Nombre: {empresa_nombre}\n"
        f"- CIF: {empresa_cif}\n\n"
        "Extrae los datos en el JSON definido en las instrucciones. Devuelve solo JSON."
    )


def _to_data_url(image_bytes: bytes, mime: str) -> str:
    encoded = base64.b64encode(image_bytes).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def _file_to_image_data_urls(file_bytes: bytes, content_type: str) -> list[str]:
    if content_type == "application/pdf":
        pages = convert_from_bytes(file_bytes, fmt="png", dpi=200)
        urls: list[str] = []
        for page in pages:
            buf = BytesIO()
            page.save(buf, format="PNG")
            urls.append(_to_data_url(buf.getvalue(), "image/png"))
        return urls
    if content_type in {"image/png", "image/jpeg"}:
        return [_to_data_url(file_bytes, content_type)]
    raise ValueError(f"Unsupported content_type: {content_type}")


async def extract_albaran(
    file_bytes: bytes,
    content_type: str,
    empresa_nombre: str,
    empresa_cif: str,
) -> AlbaranExtraido:
    client = AsyncOpenAI(api_key=settings.openai_api_key)
    image_data_urls = _file_to_image_data_urls(file_bytes, content_type)

    user_content: list[dict[str, Any]] = [{"type": "text", "text": _user_prompt(empresa_nombre, empresa_cif)}]
    user_content.extend({"type": "image_url", "image_url": {"url": url}} for url in image_data_urls)

    response = await client.chat.completions.create(
        model="gpt-4o",
        temperature=0,
        top_p=0.1,
        max_tokens=4000,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_content},
        ],
    )

    raw = response.choices[0].message.content or "{}"
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        logger.error("GPT-4o returned non-JSON: %s", raw[:500])
        raise ValueError("Modelo devolvió JSON inválido") from exc

    return AlbaranExtraido.model_validate(data)

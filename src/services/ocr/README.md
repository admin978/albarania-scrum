# AlbaranIA — Servicio OCR

Microservicio FastAPI + arq + Redis + GPT-4o Vision que extrae datos estructurados de albaranes en PDF/imagen.

Forma parte del Sprint 2 de AlbaranIA (US-09). Patrón inspirado en el OCR de Vanguard Quest, adaptado a multi-tenant por `empresa_id` en JWT.

## Arquitectura

```
Cliente (frontend) ──Bearer JWT──▶ POST /scan ──encola arq──▶ worker ──GPT-4o─▶ JSON
                                              │                        │
                                              └──Redis (status/result)─┘
                          GET /scan/status/{job_id} ◀────polling────────
```

- **API:** FastAPI, expone `POST /scan` y `GET /scan/status/{job_id}`.
- **Worker:** `arq` consume jobs y llama a GPT-4o Vision.
- **Cola/cache:** Redis con keys `ocr:status:{job_id}`, `ocr:result:{job_id}`, `ocr:payload:{job_id}` (TTL configurable).
- **Auth:** JWT HS256 con `JWT_SECRET` compartido con el backend Node.

## Endpoints

| Método | Path | Status | Body |
|--------|------|--------|------|
| POST   | `/scan`                    | 202 | multipart `file: UploadFile` (PDF/PNG/JPG, máx 10 MB) |
| GET    | `/scan/status/{job_id}`    | 200 / 202 / 404 | — |
| GET    | `/health`                  | 200 | — |

`POST /scan` devuelve `{job_id, status: "queued"}`.
`GET /scan/status/{job_id}`:
- 202 + `{status: "processing"}` mientras se procesa.
- 200 + `{status: "completed", result: AlbaranExtraido}` al terminar.
- 404 si el `job_id` no pertenece a la `empresa_id` del JWT o no existe.

## Schema de salida

`app/schemas/albaran.py` define `AlbaranExtraido` y `LineaAlbaran` con Pydantic v2. Campos clave: `numero_documento`, `fecha`, `proveedor_nombre`, `proveedor_cif`, `confianza_extraccion`, `base_imponible`, `iva_total`, `importe_total`, `lineas[]`. Unidades coercionadas al set `{ud, kg, m, l, h, pack}`.

## Levantar localmente

```bash
cp .env.example .env   # rellenar OPENAI_API_KEY y JWT_SECRET
docker compose up --build
```

API en `http://localhost:8000`, healthcheck:

```bash
curl http://localhost:8000/health
```

## Tests

```bash
pip install -r requirements.txt
pytest tests/
```

Tests incluidos:
- `test_health.py` — endpoint `/health` devuelve 200.
- `test_schema.py` — schema `AlbaranExtraido` valida fixture válida y rechaza inválida.

Pendiente Sprint 2 Day 6: tests con `respx` mockeando OpenAI + smoke E2E sobre 3 albaranes reales.

## Variables de entorno

| Variable | Default | Uso |
|----------|---------|-----|
| `JWT_SECRET` | — (obligatorio) | Verificación HS256, mismo valor que el backend Node |
| `OPENAI_API_KEY` | — (obligatorio) | Cliente GPT-4o |
| `REDIS_URL` | `redis://localhost:6379/0` | Cola arq + cache |
| `OCR_RESULT_TTL_SECONDS` | `3600` | TTL del resultado en Redis |
| `OCR_MAX_FILE_SIZE_MB` | `10` | Límite de upload |

## Decisiones del spike (Sprint 2 Day 1–5)

- **Storage del binario:** disco local en `tmp/` para Sprint 2; S3/Supabase en Sprint 3.
- **Modelo:** `gpt-4o`, `temperature=0`, `top_p=0.1`, `max_tokens=4000`. Determinismo > variedad.
- **Multi-tenant:** `empresa_id` se guarda con el payload al encolar y se verifica en `GET /scan/status`.
- **Concurrencia:** worker arq por defecto en concurrencia 10; ajustar si la API key tiene rate limits estrictos.

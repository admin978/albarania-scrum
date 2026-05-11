# Sprint Planning — Sprint 2

## Fecha
2026-04-30 (jueves) · 16:00–17:30 · vía Google Meet + Slack \#scrum

## Asistentes
- Lorena López Bermúdez — Scrum Master
- Marcos García Manzano — Product Owner + Developer
- Camilo — invitado, no asistió (sin respuesta tras intentos por Slack y email)

Omar (profesor) se unió 5 min al inicio para confirmar la decisión sobre US-04/US-06/US-10 acordada en la retrospectiva del 2026-04-29.

## Inputs
- Velocity Sprint 1: 14 SP (con 2 miembros activos).
- Sprint Review Sprint 1: US-04 y US-06 devueltas al backlog.
- Retrospectiva Sprint 1: 5 acciones de mejora con dueño y plazo.
- Backlog priorizado: US-09 ancla, US-07 catálogo, US-11 (versión mínima) supervisor.

## Decisiones tomadas

### Capacidad
Equipo activo: 2 personas. Capacidad real ≈ velocity ajustada = **14 SP**. Para cubrir el riesgo OCR (curva FastAPI/arq + GPT-4o + spike pendiente) se reserva ~0.5 SP de buffer → **plan = 13.5 SP**.

### Sprint Goal
> "Entregar el flujo core de OCR: subir un albarán, extraer datos con IA y validarlos manualmente, dejando la base lista para que un supervisor pueda revisarlos."

### Reparto
| Miembro | Historias | SP |
|---------|-----------|-----|
| Marcos  | US-09 (OCR backend completo) | 8 |
| Lorena  | US-07 (CRUD artículos) + US-11 versión backend mínima | 3 + 2.5 = 5.5 |

### US-10 fuera del sprint
US-10 (revisión y corrección de datos extraídos) se queda fuera del Sprint 2: sin Camilo el equipo no la puede absorber sin reventar el Sprint Goal. Queda como top del backlog para Sprint 3. Omar avala la decisión.

### Política de re-asignación (Acción 1 de la retro)
Si un miembro no se conecta a 2 dailies seguidos sin previo aviso, el SM convoca reunión de re-planificación al día siguiente. Las historias asignadas vuelven al backlog o se reparten según capacidad.

### Pareo en US-09 (Acción 2 de la retro)
Lorena participa con Marcos en sesiones de pareo durante el spike técnico de US-09 (Days 1–3) para garantizar que conoce la arquitectura del servicio OCR aunque la implementación principal corra a cargo de Marcos.

### Refinement de US-04 y US-06 (Acción 4 de la retro)
Lorena reescribe criterios de aceptación durante Day 4 (2026-05-03) y los presenta a Marcos en un mini-refinement de 30 min. No entran al Sprint 2; quedan listos para el Sprint 3.

## Spike técnico US-09 — alcance acordado

Tres entregables previos a la implementación de US-09 propiamente dicha. Están dentro del SP de la historia (los 8 SP los cubren).

1. **Esqueleto del servicio OCR** en `src/services/ocr/` con FastAPI, health check, endpoints `POST /scan` y `GET /scan/status/{job_id}`, autenticación JWT compartida con el backend Node, worker `arq` apuntando a Redis. Patrón de referencia: `repos/Vanguard Quest/vanguard-quest-ocr-scanner/` (no copy-paste).
2. **Prueba manual del prompt GPT-4o Vision** sobre 3 albaranes reales para calibrar prompt y campos. **Bloqueo abierto:** `docs/referencias/` solo contiene un PDF irrelevante (directorio CYL). Marcos descarga 3 albaranes de muestra antes del Day 6 (2026-05-05).
3. **Schema de respuesta Pydantic** `AlbaranExtraido` con `LineaAlbaran` anidado, validación de tipos y unidades coercionadas a un set cerrado. Tests de schema con fixture válida e inválida.

## Tooling
- **Modelo OCR:** GPT-4o, `temperature=0`, `top_p=0.1`, `max_tokens=4000`.
- **Cola:** `arq>=0.25` sobre Redis 7.
- **Storage del binario subido:** disco local en `tmp/` para Sprint 2; migración a S3/Supabase Storage queda para Sprint 3.
- **Tests:** `pytest` + `httpx` + `pytest-asyncio`. Mock de OpenAI con `respx`.
- **Docker:** `docker compose` con 3 servicios (api, worker, redis).

## Variables de entorno requeridas
Archivo `src/services/ocr/.env.example`:
- `JWT_SECRET` — compartido con backend Node.
- `OPENAI_API_KEY`.
- `REDIS_URL` (default `redis://redis:6379/0`).
- `OCR_RESULT_TTL_SECONDS=3600`.
- `OCR_MAX_FILE_SIZE_MB=10`.

## Definition of Done (recordatorio)
Sprint 1 + nuevos:
- Tests `pytest` mínimos verdes.
- `.env.example` actualizado, sin secretos en commits.
- Servicio levantable con `docker compose up`.

## Próximos hitos
- **Day 1 (2026-04-30):** kickoff, spike inicia.
- **Day 3 (2026-05-02):** sesión de pareo Lorena↔Marcos en spike OCR.
- **Day 4 (2026-05-03):** refinement de US-04/US-06.
- **Day 5 (2026-05-04):** spike completado (esqueleto + schema). Pendiente: 3 PDFs de fixture.
- **Day 8 (2026-05-07):** US-07 lista para review.
- **Day 13 (2026-05-12):** code freeze, smoke E2E del flujo.
- **Day 14 (2026-05-13):** Sprint Review + Retrospectiva.

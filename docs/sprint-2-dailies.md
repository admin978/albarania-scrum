# Daily Scrums — Sprint 2

Equipo activo: Lorena, Marcos · Camilo: ausente, sin contacto · Duración objetivo: 5 min · Canal: Slack \#scrum.

---

## Daily 1 — 2026-04-30

| Miembro | ¿Qué hice ayer? | ¿Qué haré hoy? | Impedimentos |
|---------|-----------------|----------------|--------------|
| Lorena  | Sprint Review + Retrospectiva del Sprint 1 | Sprint Planning a las 16:00 + abrir borrador de US-07 (Prisma + endpoint) | Ninguno |
| Marcos  | Cierre de ALB-5; preparación del Planning | Sprint Planning + arrancar spike US-09 (estructura `src/services/ocr/`) | Ninguno |

**Notas:** Planning cerrado con 13.5 SP comprometidos. Decisión clave: US-10 fuera del sprint. Política nueva de re-asignación documentada.

---

## Daily 2 — 2026-05-01

| Miembro | ¿Qué hice ayer? | ¿Qué haré hoy? | Impedimentos |
|---------|-----------------|----------------|--------------|
| Lorena  | Modelo Prisma `Articulo` con `empresa_id` + migración local | Endpoint `POST /api/articulos` + validaciones | Ninguno |
| Marcos  | Estructura del servicio OCR + `Dockerfile` + `docker-compose.yml` con redis | `app/main.py` con lifespan(redis,arq) y `GET /health` | Ninguno |

---

## Daily 3 — 2026-05-02 (sesión de pareo)

| Miembro | ¿Qué hice ayer? | ¿Qué haré hoy? | Impedimentos |
|---------|-----------------|----------------|--------------|
| Lorena  | `POST /api/articulos` funcional + tests manuales | Pareo con Marcos en US-09 (10:00–12:00) + listado y edición de artículos | Ninguno |
| Marcos  | Lifespan + health funcionando, JWT auth implementado | Pareo con Lorena: revisar arquitectura OCR + arrancar `POST /scan` | Decidir si guardar binario en disco o memoria — acordamos disco temporal |

**Notas (pareo 10:00–12:00):** Lorena entendió flujo completo (upload → encolar → arq worker → GPT-4o → cachear resultado en Redis). Documentado en \texttt{src/services/ocr/README.md}. Bus factor reducido de 1 a 2 en al menos las decisiones arquitectónicas.

---

## Daily 4 — 2026-05-03

| Miembro | ¿Qué hice ayer? | ¿Qué haré hoy? | Impedimentos |
|---------|-----------------|----------------|--------------|
| Lorena  | Pareo OCR + endpoints listado/edición de artículos | Refinement de US-04 y US-06 (2026-05-03) + cerrar US-07 | Ninguno |
| Marcos  | `POST /scan` con multipart, encola job en arq, devuelve 202 | Endpoint `GET /scan/status/{job_id}` con verificación multi-tenant | Ninguno |

**Notas:** Refinement completado por Lorena. US-04 y US-06 quedan listas con criterios verificables para Sprint 3. Marcos integra `requireRole` en el flujo de scan (sólo Operario y Admin pueden subir).

---

## Daily 5 — 2026-05-04 (hoy)

| Miembro | ¿Qué hice ayer? | ¿Qué haré hoy? | Impedimentos |
|---------|-----------------|----------------|--------------|
| Lorena  | US-07 cerrada; refinement US-04/US-06 entregado | Empezar US-11 versión backend (endpoint `GET /api/albaranes/pendientes`) | Necesita formato exacto del response del OCR para enlazar |
| Marcos  | `GET /scan/status/{job_id}` + multi-tenant check + tests health/schema | Implementar `process_ocr_job` en `app/worker/tasks.py` con prompt GPT-4o | Pendiente conseguir 3 PDFs de muestra (acción Day 6) |

**Estado del spike US-09:**
- ✅ Esqueleto FastAPI + endpoints + auth + worker scaffold.
- ✅ Schema `AlbaranExtraido` + `LineaAlbaran` con tests.
- ⏳ Prompt GPT-4o Vision en draft, pendiente de validar con 3 albaranes reales.

**Notas:** Lorena necesita el schema final del OCR para terminar US-11; Marcos lo congela y se lo pasa por Slack a las 18:00. Camilo: sin novedades, sin contacto en todo el sprint hasta hoy.

---

## Pendiente para días 6–10
- 2026-05-05 (Day 6): Marcos descarga 3 albaranes reales y valida prompt.
- 2026-05-06 (Day 7): primer end-to-end OCR (subir → JSON válido).
- 2026-05-07 (Day 8): Lorena cierra US-11 backend.
- 2026-05-08 (Day 9): tests con mock OpenAI verdes; Marcos prepara demo.
- 2026-05-11–12 (Day 12–13): code freeze + smoke E2E.
- 2026-05-13 (Day 14): Sprint Review + Retrospectiva.

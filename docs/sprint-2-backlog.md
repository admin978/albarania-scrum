# Sprint 2 Backlog — AlbaranIA

Acordado en el Sprint Planning del 2026-04-30. Sustituye al borrador previo del Sprint 1.

## Sprint Goal
> "Entregar el flujo core de OCR: subir un albarán, extraer datos con IA y validarlos manualmente, dejando la base lista para que un supervisor pueda revisarlos."

Este goal aprovecha el feedback del Sprint Review (re-priorización de US-09 como historia ancla) y entrega el valor diferencial del producto.

## Duración
2 semanas · 2026-04-30 → 2026-05-13 (10 días laborables).

## Capacidad real
- Velocity Sprint 1: **14 SP** (con 2 miembros activos).
- Camilo: ausencia documentada; el equipo asume 2 miembros para este sprint salvo notificación de Omar.
- Plan: **13.5 SP** (debajo de velocity para dejar buffer ante complejidad de OCR + curva de aprendizaje FastAPI/arq).

## Historias seleccionadas

| ID | Jira | Historia | Épica | SP | Asignado | Estado |
|----|------|----------|-------|-----|----------|--------|
| US-09 | ALB-9  | Subir PDF/imagen y extraer datos con GPT-4o | E3 | 8 | Marcos | To Do |
| US-07 | ALB-7  | CRUD de artículos por empresa               | E2 | 3 | Lorena | To Do |
| US-11 | ALB-11 | Supervisor revisa pendientes (aprobar/rechazar) — versión backend mínima | E4 | 2.5 | Lorena | To Do |

**Total: 13.5 SP** · Reparto: Marcos 8 SP · Lorena 5.5 SP.

## Historias devueltas al backlog (no entran en Sprint 2)

| ID | Razón |
|----|-------|
| US-04 | Pendiente de refinement por Lorena (Day 4). Sin owner activo todavía. |
| US-06 | Pendiente de refinement; depende de criterios estables de US-07. |
| US-10 | Sin owner: era de Camilo. El equipo de 2 personas no puede absorberla sin reventar Sprint Goal. Top del backlog para Sprint 3. |
| US-16 | Nice-to-have del feedback del Sprint Review. Pendiente de priorizar. |

## Dependencias Sprint 1 → Sprint 2
- US-09 depende de US-01 (empresa) + US-03 (login JWT) → ambas Done.
- US-07 depende de US-01.
- US-11 (parcial) depende de US-09 entregando registros en estado `pendiente_revision`.

## Spike técnico US-09 — completado el 2026-05-04 (Day 5)
1. ✅ Esqueleto `src/services/ocr/` con FastAPI + health check + endpoints `POST /scan` y `GET /scan/status/{job_id}`.
2. ⏳ Prueba manual de prompt GPT-4o Vision sobre 3 albaranes reales — pendiente de obtener fixtures (Marcos, Day 6).
3. ✅ Schema Pydantic `AlbaranExtraido` definido con tests.

Detalle en `sprint-2-planning.md` y `sprint-2-dailies.md`.

## Riesgos identificados
- **Bus factor:** US-09 depende totalmente de Marcos. Mitigación: pareo Lorena↔Marcos en fase spike (Day 3).
- **GPT-4o Vision API:** coste y latencia variables. Mitigación: timeout 30s + caché Redis del resultado por hash de archivo.
- **Calidad del OCR:** albaranes escaneados de baja calidad pueden dar <80% de acierto. Mitigación: campo `confianza_extraccion` en el schema; UI futura puede pedir revisión manual.
- **Sin Camilo:** si reaparece a mitad de sprint, no hay margen para incorporarlo a una historia activa; sólo refinement o tests.

## Definition of Done (Sprint 2)
Idéntico al Sprint 1, más:
- [ ] Tests \texttt{pytest} mínimos verdes (health, schema, mock OpenAI).
- [ ] Variables sensibles documentadas en `.env.example`; nada de secretos en commits.
- [ ] Servicio OCR levantable localmente con `docker compose up`.

## Criterios de éxito del sprint
- Usuario sube un PDF desde la API y obtiene un `job_id`; al hacer polling recibe el JSON extraído en <30s para PDFs de 1 página.
- Lorena puede dar de alta artículos por empresa.
- Endpoint mínimo de "albaranes pendientes de revisión" devuelve la lista filtrada por `empresa_id` (UI completa va a Sprint 3).
- Demo en Sprint Review con 1 albarán real procesado punta a punta.

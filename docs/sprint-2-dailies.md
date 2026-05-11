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

## Daily 6 — 2026-05-05

| Miembro | ¿Qué hice ayer? | ¿Qué haré hoy? | Impedimentos |
|---------|-----------------|----------------|--------------|
| Lorena  | Recibí el schema `AlbaranExtraido` por Slack | Arrancar US-11 backend (`GET /api/albaranes/pendientes`) con filtro `empresa_id` desde JWT | Ninguno |
| Marcos  | Schema congelado y compartido con Lorena | Descargar 3 albaranes de muestra y validar prompt GPT-4o sobre ellos | Necesito decidir si uso muestras propias o pido a Omar acceso a fixtures de la práctica |

**Notas:** Marcos opta por generar 3 PDFs sintéticos representativos (logística, construcción, alimentación) para no bloquearse esperando a Omar. Prompt iterado 4 veces hasta que las 3 pruebas devuelven JSON conforme al schema con `confianza_extraccion ≥ 0.85`. Camilo: sin contacto.

---

## Daily 7 — 2026-05-06

| Miembro | ¿Qué hice ayer? | ¿Qué haré hoy? | Impedimentos |
|---------|-----------------|----------------|--------------|
| Lorena  | Endpoint `GET /api/albaranes/pendientes` esqueletado en backend Node | Filtrado por `estado='pendiente_revision'` + paginación + tests manuales con Postman | Ninguno |
| Marcos  | Prompt validado contra 3 PDFs sintéticos | Primer E2E manual: subir PDF → encolar arq → llamar GPT-4o → cachear resultado en Redis | Ninguno |

**Notas:** Primer end-to-end OCR funcional en local a las 17:40. PDF de 1 página procesado en 18 segundos (dentro del objetivo de 30 s). El JSON devuelto encaja con el schema sin coerción manual. Detectado un edge case: cuando GPT-4o devuelve unidades fuera del set cerrado (ej. "uds." en vez de "ud"), el validador Pydantic lanza error y arq marca el job como `failed`. Marcos abre un TODO para añadir un normalizador de unidades antes de la validación.

---

## Daily 8 — 2026-05-07

| Miembro | ¿Qué hice ayer? | ¿Qué haré hoy? | Impedimentos |
|---------|-----------------|----------------|--------------|
| Lorena  | Endpoint pendientes listo + tests Postman verdes | Cierre US-11: review con Marcos, merge a master y abrir mi sección del informe (rol SM) | Ninguno |
| Marcos  | E2E OCR funcional + TODO normalizador de unidades | Implementar normalizador de unidades + manejo de errores del worker (retry con backoff) | Ninguno |

**Notas:** US-11 backend cerrada a las 12:30. Lorena abre PR; Marcos revisa y mergea. Burndown baja a 8 SP (sólo queda US-09). Tarde: Lorena trabaja en su sección del informe; Marcos endurece el worker (timeouts, captura de excepciones, log estructurado). Pareo corto a las 18:00 para que Lorena entienda el flujo de errores del worker y pueda contarlo en el informe.

---

## Daily 9 — 2026-05-08 (hoy)

| Miembro | ¿Qué hice ayer? | ¿Qué haré hoy? | Impedimentos |
|---------|-----------------|----------------|--------------|
| Lorena  | US-11 cerrada + arrancada sección del informe | Continuar informe (sección Scrum Master + métricas Sprint 1) | Ninguno |
| Marcos  | Normalizador de unidades + retry con backoff en worker | Tests `pytest` con mock OpenAI vía `respx` y preparación de la demo | Ninguno |

**Notas:** Día centrado en cerrar deuda técnica del DoD (tests automáticos) y avanzar el informe. Sin reunión con Omar todavía sobre la consulta de Lorena (alcance de AA1). Plan: si responde antes del Day 12, ajustamos el cierre del informe; si no, entregamos con el alcance actual. Camilo: sin contacto en todo el sprint, ausencia ya documentada como impedimento crítico cerrado.

---

## Daily 10 — 2026-05-11

| Miembro | ¿Qué hice ayer? | ¿Qué haré hoy? | Impedimentos |
|---------|-----------------|----------------|--------------|
| Lorena  | Sección SM del informe (PR #2 con capturas de Jira) + análisis del historial del proyecto | Cerrar Sprint 1 en Jira (ALB-1/2/3/5 a Done, ALB-4/6 al backlog con comentario de devolución) + escribir a Camilo para ofrecerle reincorporación | Sin permisos write directos en el repo → resuelto: invitación de colaboradora enviada hoy |
| Marcos  | Tests con mock OpenAI vía `respx` + revisión del PR de Lorena con feedback inline | Redactar la sección PO/Developer del informe en rama `feature/seccion-marcos-informe` (sirve también para AA4 como PR cruzado) | Esperando las 10 imágenes de Lorena para integrar su PR sobre el informe principal |

**Notas:**
- Respuesta de Omar (vía Lorena): AA1 es simulación, basta nivel representativo, no hace falta código funcional completo y el informe es de 6 páginas máximo. Reorienta el cierre: la demo del Sprint Review se centra en mockups y arquitectura, no en E2E completo.
- Camilo: Lorena le contactará, pero sin asignación activa en Sprint 2 (quedan 3 días laborables y onboardarlo en US-09 a estas alturas pone en riesgo la demo). Plan: refinement de US-10 para Sprint 3.
- AA4 (Git colaborativo): planificada como (a) PR de Marcos hacia master con la sección PO/Dev → Lorena revisa; (b) PR cruzado de Lorena con capturas → Marcos revisa; (c) edición simultánea de la tabla de roles para provocar conflicto controlado y resolverlo en pareja.

---

## Pendiente para días 11–14
- 2026-05-12 (Day 11): mergear PR #2 (informe Lorena) + PR #3 (sección Marcos) tras review cruzado. Integrar la sección de Marcos en el informe principal vía `\input`.
- 2026-05-12 (Day 11): provocar y resolver conflicto de merge controlado (AA4).
- 2026-05-12–13 (Day 12–13): code freeze + smoke E2E con un albarán real.
- 2026-05-13 (Day 14): Sprint Review + Retrospectiva.

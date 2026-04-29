# Daily Scrums — Sprint 1

Equipo: Lorena, Marcos, Camilo · Duración objetivo: 5 min · Canal: Slack #scrum

---

## Daily 1 — 2026-04-21

| Miembro | ¿Qué hice ayer? | ¿Qué haré hoy? | Impedimentos |
|---------|-----------------|----------------|--------------|
| Lorena  | Configuré tablero Jira (ALB) y arquitectura propuesta | Empezar ALB-1 (crear empresa) | Ninguno |
| Marcos  | Revisé backlog y setup del repo | Empezar ALB-3 (login JWT) | Decidir librería JWT (`jsonwebtoken` vs `jose`) |
| Camilo  | Incorporación al tablero | Autoasignarme ALB-4 y ALB-6; empezar ALB-4 | Pendiente de confirmar acceso a Jira |

**Impedimentos registrados:** 1 (decisión técnica JWT) · **Notas:** Sprint arrancado con 6 días de retraso; fechas oficiales se mantienen (fin 2026-04-29).

---

## Daily 2 — 2026-04-22

| Miembro | ¿Qué hice ayer? | ¿Qué haré hoy? | Impedimentos |
|---------|-----------------|----------------|--------------|
| Lorena  | Repaso del backlog y de los criterios de aceptación de ALB-1 | Modelar la entidad Empresa en Prisma y empezar el formulario | Necesito que validemos el listado de campos obligatorios |
| Marcos  | Decisión de librería JWT: nos quedamos con `jsonwebtoken` | Endpoint `POST /api/auth/login` con validación básica | Ninguno |
| Camilo  | Sin avances reportados | — | No conectado al daily |

**Notas:** acordamos que Marcos prepara también el middleware `requireRole` para reutilizar en ALB-2 y ALB-4.

---

## Daily 3 — 2026-04-23

| Miembro | ¿Qué hice ayer? | ¿Qué haré hoy? | Impedimentos |
|---------|-----------------|----------------|--------------|
| Lorena  | Modelo Empresa en Prisma + migración aplicada en local | Formulario de alta y endpoint `POST /api/empresas` | Ninguno |
| Marcos  | Login funcionando contra usuario de prueba; token contiene `empresa_id` y `rol` | Hashear passwords con bcrypt e integrar logout en el frontend | Ninguno |
| Camilo  | Sin avances reportados | — | Sin respuesta en Slack |

**Notas:** Lorena y Marcos están sincronizados. Falta volver a contactar con Camilo — Marcos lo intenta por WhatsApp.

---

## Daily 4 — 2026-04-24

| Miembro | ¿Qué hice ayer? | ¿Qué haré hoy? | Impedimentos |
|---------|-----------------|----------------|--------------|
| Lorena  | ALB-1 al 70%: alta de empresa funcional, falta validación de CIF | Cerrar ALB-1 y empezar ALB-2 (alta de usuarios) | Ninguno |
| Marcos  | Login y logout cerrados; sesión persistente en localStorage | Empezar ALB-5 (CRUD proveedores) | Ninguno |
| Camilo  | Sin avances reportados | — | Sin contacto |

**Impedimentos:** la falta de respuesta de Camilo se está convirtiendo en un riesgo para ALB-4 y ALB-6. Lorena propone hablarlo con el profesor (Omar).

---

## Daily 5 — 2026-04-27

| Miembro | ¿Qué hice ayer? | ¿Qué haré hoy? | Impedimentos |
|---------|-----------------|----------------|--------------|
| Lorena  | ALB-1 cerrada (validación CIF añadida); ALB-2 al 30% | Terminar ALB-2 y empezar a redactar el informe en LaTeX | Ninguno |
| Marcos  | ALB-3 lista para review; tablas Prisma de proveedores creadas | Cerrar ALB-5 (CRUD proveedores) y soportar a Lorena con el informe | Ninguno |
| Camilo  | Sin avances reportados | — | Sin contacto en toda la semana |

**Decisión de equipo:** Lorena hablará con Omar para gestionar la situación de Camilo de cara a la entrega. Si no hay respuesta antes del 2026-04-29, ALB-4 y ALB-6 entrarán en el Sprint Retrospective como impedimento crítico y se documentará en el informe.

---

## Daily 6 — 2026-04-28

| Miembro | ¿Qué hice ayer? | ¿Qué haré hoy? | Impedimentos |
|---------|-----------------|----------------|--------------|
| Lorena  | ALB-2 al 80%, integrado con `requireRole` de Marcos | Cerrar ALB-2 y abrir borrador del informe LaTeX | Ninguno |
| Marcos  | ALB-5 funcional (CRUD + soft delete + paginación) | Cerrar ALB-5 (búsqueda por nombre) y preparar Sprint Review | Ninguno |
| Camilo  | Sin avances reportados | — | Sin contacto; Lorena escala formalmente a Omar por Slack |

**Notas:** Omar responde por Slack a las 19:30 confirmando que se puede documentar la ausencia como impedimento crítico y que ALB-4/ALB-6 vuelven a backlog sin penalizar la nota grupal. Marcos avisa al equipo en `#scrum`.

---

## Daily 7 — 2026-04-29

| Miembro | ¿Qué hice ayer? | ¿Qué haré hoy? | Impedimentos |
|---------|-----------------|----------------|--------------|
| Lorena  | ALB-2 cerrada con validaciones + tests manuales | Sprint Review + Retrospectiva + cierre del informe | Ninguno |
| Marcos  | ALB-5 cerrada (búsqueda + paginación + filtrado) | Apoyar review/retro y empezar a sondear US-09 (FastAPI/OCR) | Ninguno |
| Camilo  | Sin avances reportados | — | Ausencia confirmada; impedimento documentado |

**Notas:** último día del Sprint 1. Velocity real = 14/22 SP (64%). Review y retro a las 17:00 con Omar presente. Se acuerda volcar US-04 y US-06 al Product Backlog con prioridad alta y re-priorizarlas en el Planning del Sprint 2.

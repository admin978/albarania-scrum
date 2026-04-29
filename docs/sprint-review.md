# Sprint Review — Sprint 1

## Fecha
2026-04-29

## Asistentes
- Lorena López Bermúdez — Product Owner
- Marcos García Manzano — Scrum Master + Dev
- Camilo — Dev (ausente, sin contacto desde el día 1)
- Stakeholders (otros grupos de clase) + Omar (profesor)

## Sprint Goal
> "Construir la base de la plataforma: que un administrador pueda crear una empresa, dar de alta usuarios y proveedores, y que un operario pueda hacer login y ver el panel principal."

## Sprint Goal alcanzado: ⚠️ Parcial

El núcleo del goal (alta de empresa + usuarios + login + proveedores) sí se cubre. Las dos historias asignadas a Camilo (panel por rol e importación CSV) no se entregaron por la ausencia del miembro durante todo el sprint.

## Incremento presentado

### US-01 — ALB-1: Crear empresa ✅ (5 SP)
- Un administrador puede crear una nueva empresa con nombre, CIF y configuración básica.
- Validación de CIF añadida en la última iteración.
- Datos persistidos en PostgreSQL aislados por `empresa_id`.

### US-02 — ALB-2: Alta de usuarios con roles ✅ (3 SP)
- Creación de usuarios asociados a una empresa con rol Admin/Supervisor/Operario.
- Validaciones de email único y campos obligatorios.

### US-03 — ALB-3: Login con email y contraseña ✅ (3 SP)
- Login funcional con JWT (`jsonwebtoken`, HS256).
- Token incluye `empresa_id` y `rol`.
- Sesión persistente en localStorage; logout integrado.
- Middleware `requireRole` reutilizable para futuras historias.

### US-04 — ALB-4: Panel principal por rol ❌ NO ENTREGADA (3 SP)
- Asignada a Camilo. Sin avances reportados.
- Devuelta al Product Backlog con prioridad alta para Sprint 2.

### US-05 — ALB-5: CRUD de proveedores ✅ (3 SP)
- Listado, alta, edición y eliminación (soft delete) por empresa.
- Búsqueda y filtrado por nombre.
- Paginación.

### US-06 — ALB-6: Importación CSV de proveedores ❌ NO ENTREGADA (5 SP)
- Asignada a Camilo. Sin avances reportados.
- Devuelta al Product Backlog. Re-priorizar contra US-09 en el siguiente Planning.

## Velocidad del sprint
**14 / 22 SP completados = 64%**

| Estado | Historias | SP |
|--------|-----------|-----|
| ✅ Done | US-01, US-02, US-03, US-05 | 14 |
| ❌ Not Done | US-04, US-06 | 8 |

Velocity de referencia para Sprint 2: **14 SP** (capacidad real con 2 miembros activos).

## Incidencia mayor — Ausencia de un miembro del equipo
Camilo no participó en ninguna ceremonia ni daily desde el 2026-04-22. La situación fue escalada al profesor (Omar) el 2026-04-27 vía Slack y autorizada el 2026-04-29 a documentar como impedimento crítico. Detalles en `retrospectiva.md` y en el informe.

## Feedback recibido
- "Estaría bien poder exportar también los proveedores a CSV, no solo importar." — grupo de Marketplace
- "¿Se podría añadir un buscador global en el panel?" — grupo de E-Commerce
- "El flujo de login → CRUD proveedores está muy limpio, buen trabajo en lo entregado." — grupo de Logística
- Omar: "Buena gestión del impedimento; documentadlo bien en la retro y el informe."

## Backlog actualizado
- **Re-incorporadas con prioridad alta:** US-04 (panel por rol), US-06 (import CSV).
- **Nuevas:** US-16 — exportar proveedores a CSV (sugerencia stakeholder).
- **Re-priorizada:** US-09 (OCR) sigue como historia ancla del Sprint 2 (entrega valor diferencial del producto).

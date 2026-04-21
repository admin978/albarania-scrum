# Sprint 1 Backlog — AlbaranIA

## Sprint Goal
> "Construir la base de la plataforma: que un administrador pueda crear una empresa, dar de alta usuarios y proveedores, y que un operario pueda hacer login y ver el panel principal."

## Duración
2 semanas (2026-04-15 → 2026-04-29)

## Equipo (3 miembros)
- Lorena López Bermúdez
- Marcos García Manzano
- Camilo

## Historias seleccionadas

| ID | Jira | Historia | SP | Asignado | Estado |
|----|------|----------|-----|----------|--------|
| US-01 | ALB-1 | Crear empresa en la plataforma | 5 | Lorena | To Do |
| US-02 | ALB-2 | Alta de usuarios con roles | 3 | Lorena | To Do |
| US-03 | ALB-3 | Login con email y contraseña | 3 | Marcos | To Do |
| US-04 | ALB-4 | Panel principal con navegación por rol | 3 | Camilo | To Do |
| US-05 | ALB-5 | CRUD de proveedores | 3 | Marcos | To Do |
| US-06 | ALB-6 | Importación de proveedores desde CSV | 5 | Camilo | To Do |

**Total: 22 SP** · Reparto por persona: Lorena 8 SP · Marcos 6 SP · Camilo 8 SP

## Tablero Scrum (Jira)
https://agente404.atlassian.net/jira/software/projects/ALB/boards/133

### Columnas del tablero
- **To Do** — Pendiente de empezar
- **In Progress** — En desarrollo (WIP máx: 2 por persona)
- **In Review** — Esperando revisión de otro miembro
- **Done** — Cumple Definition of Done

## Definition of Done
Una historia se considera **Done** cuando cumple todos los puntos:

- [ ] Todos los criterios de aceptación de la issue Jira verificados.
- [ ] Código en rama `feature/US-XX-*`, PR abierto contra `master`.
- [ ] PR revisado y aprobado por al menos 1 compañero.
- [ ] Sin conflictos con `master`; mergeado vía squash.
- [ ] Pruebas manuales del happy path + 1 caso de error documentadas en el PR.
- [ ] Documentación actualizada si el cambio afecta a arquitectura o API (`docs/` o `README.md`).
- [ ] Issue Jira movida a `Done` con comentario del commit/PR que la cierra.

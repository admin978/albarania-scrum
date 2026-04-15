# CLAUDE.md — AlbaranIA (Práctica Scrum)

## Contexto del proyecto

Práctica de la asignatura **Metodologías Ágiles** (Universidad Europea).
Simulación de un equipo Scrum de 4 personas construyendo **AlbaranIA** desde cero:
una plataforma web SaaS para digitalizar albaranes de proveedores con IA.

## Objetivo académico

Documentar un sprint completo (Planning → Dailies → Review → Retro) y entregar un informe LaTeX de máx. 6 páginas.

## Arquitectura propuesta

- **Frontend:** React + Tailwind CSS
- **Backend:** Node.js + Express + PostgreSQL (Prisma ORM)
- **Servicio OCR:** Python + FastAPI + GPT-4o
- **Auth:** JWT
- **Multi-tenant:** filtrado por empresa_id

## Épicas del Product Backlog

| ID | Épica | Prioridad |
|----|-------|-----------|
| E1 | Autenticación y gestión de usuarios | Alta |
| E2 | Gestión de catálogos (proveedores, artículos) | Alta |
| E3 | Carga y procesamiento OCR de albaranes | Alta |
| E4 | Flujo de validación de albaranes | Media |
| E5 | Facturación y exportación | Media |
| E6 | Dashboard y reporting | Baja |

## Sprint 1 — Historias seleccionadas

Sprint Goal: "Construir la base: alta de empresa, usuarios, proveedores y login funcional."

- US-01: Crear empresa en la plataforma (5 SP)
- US-02: Alta de usuarios con roles (3 SP)
- US-03: Login con email y contraseña (3 SP)
- US-04: Panel principal con navegación por rol (3 SP)
- US-05: CRUD de proveedores (3 SP)
- US-06: Importación masiva de proveedores desde CSV (5 SP)

Total: 22 SP

## Roles Scrum

- Product Owner: [por asignar]
- Scrum Master: [por asignar]
- Developers: los 4 miembros del equipo

## Herramientas

- **Jira:** tablero Scrum en agente404.atlassian.net
- **Slack:** workspace "UE - Metodologías Ágiles/Scrum"
- **GitHub:** este repo
- **LaTeX:** informe final

## Convenciones de código

- Commits en español con prefijo: `feat:`, `fix:`, `docs:`, `refactor:`
- Ramas: `main`, `develop`, `feature/US-XX-descripcion`
- PRs requieren al menos 1 review

## Estructura del repo

```
albarania-scrum/
├── CLAUDE.md
├── README.md
├── docs/
│   ├── product-backlog.md
│   ├── sprint-backlog.md
│   ├── dailies.md
│   ├── sprint-review.md
│   ├── retrospectiva.md
│   └── informe/          # LaTeX del informe final
├── mockups/               # Capturas o mockups del incremento
└── src/                   # Código fuente (si aplica)
```

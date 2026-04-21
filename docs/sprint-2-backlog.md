# Sprint 2 Backlog — AlbaranIA (DRAFT)

> Borrador preparado durante el Sprint 1 para acelerar el Planning del Sprint 2. Revisar y ajustar en la ceremonia de Planning.

## Sprint Goal (propuesto)
> "Entregar el flujo core de OCR: subir un albarán, extraer datos con IA y validarlos manualmente."

Este goal aprovecha la feedback del Sprint Review (re-priorización de US-09 como primera historia) y entrega el valor diferencial del producto.

## Duración (propuesta)
2 semanas · 2026-04-30 → 2026-05-13

## Capacidad
Velocity de referencia del Sprint 1: **22 SP**. Plan de 21 SP para dejar buffer por la complejidad del OCR.

## Historias propuestas

| ID | Jira | Historia | Épica | SP | Prioridad |
|----|------|----------|-------|-----|-----------|
| US-09 | (crear) | Subir PDF/imagen y extraer datos con GPT-4o | E3 | 8 | Highest |
| US-10 | (crear) | Revisar y corregir datos extraídos antes de confirmar | E3 | 5 | Highest |
| US-11 | (crear) | Supervisor revisa albaranes pendientes (aprobar/rechazar) | E4 | 5 | High |
| US-07 | (crear) | CRUD de artículos por empresa | E2 | 3 | Medium |

**Total: 21 SP**

## Dependencias con Sprint 1
- US-09 requiere US-01 (empresa) + US-03 (login) → ambas en Done al cerrar Sprint 1.
- US-09/US-10 requieren servicio OCR (Python + FastAPI + GPT-4o) levantado — trabajo técnico previo.
- US-11 requiere US-10 (datos ya validables manualmente).

## Reparto tentativo (3 personas, ~7 SP/pers.)

| Miembro | Historias | SP |
|---------|-----------|-----|
| Lorena  | US-07 + mitad US-11 | 3 + 2.5 = 5.5 |
| Marcos  | US-09 (backend OCR + Redis/arq) | 8 |
| Camilo  | US-10 + mitad US-11 | 5 + 2.5 = 7.5 |

Ajustable según roles Scrum cuando se decidan.

## Riesgos identificados
- **GPT-4o Vision API:** coste y latencia impredecibles; conviene cachear y poner timeout.
- **Calidad del OCR:** albaranes escaneados con baja calidad pueden dar <80% de acierto.
- **Onboarding OCR:** si nadie ha tocado FastAPI/arq antes, US-09 puede reventar la estimación.

## Tareas técnicas previas al Planning (spike)
1. Levantar esqueleto del servicio Python `services/ocr/` con FastAPI + health check.
2. Probar manualmente un prompt de GPT-4o Vision sobre 3 albaranes reales del directorio `docs/referencias/`.
3. Definir el schema de respuesta del OCR (JSON con fecha, proveedor, líneas, importes).

Estas tareas NO cuentan para el Sprint 2 — son investigación para que la Planning pueda estimar con datos.

## Criterios de éxito del sprint
- Usuario puede subir un PDF desde el panel y ver los datos extraídos en <30s.
- Puede editar los datos antes de confirmar.
- Supervisor puede aprobar/rechazar en un flujo separado.
- Demo en Sprint Review con 1 albarán real procesado de punta a punta.

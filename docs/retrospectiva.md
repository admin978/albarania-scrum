# Retrospectiva — Sprint 1

## Fecha
2026-04-29 (tras Sprint Review, sesión de 45 min)

## Asistentes
Lorena, Marcos. Camilo no asistió (ausencia documentada). Omar (profesor) presente como observador en los primeros 10 min.

## Formato
Start / Stop / Continue + plan de acciones con responsable y plazo.

---

## ✅ ¿Qué fue bien?
- Comunicación Lorena↔Marcos: alta frecuencia en Slack, reuniones cortas pero efectivas.
- Tablero Jira (ALB) mantenido al día: cualquiera podía ver el estado en menos de un minuto.
- Decisiones técnicas resueltas rápido (JWT con `jsonwebtoken`, `requireRole` reutilizable).
- Las 4 historias de los miembros activos (US-01, US-02, US-03, US-05) cerradas con DoD.
- Escalado del impedimento Camilo gestionado a tiempo: avisamos a Omar en el día 8 y obtuvimos respuesta antes del cierre.

## ❌ ¿Qué no fue bien?
- **Bus factor de 1 en historias asignadas:** US-04 y US-06 dependían 100% de Camilo, sin plan B. Cuando dejó de responder, no había forma de redistribuir sin desbordar al resto.
- **Detección tardía de la ausencia:** se asumió 4 días que volvería a aparecer antes de tomar medidas. La regla de "esperar al siguiente daily" no escala cuando un miembro no se conecta.
- **Arranque lento:** los primeros 6 días la curva se mantuvo plana en 22 SP. La mayor parte del trabajo se concentró en los 3 últimos días (efecto hockey-stick).
- **Criterios de aceptación incompletos al inicio:** US-04 y US-06 entraron al sprint con bullets vagos. Si Camilo hubiera estado, tampoco habría sido fácil verificarlas.
- **Sin tests automáticos:** todo se validó con pruebas manuales. Para Sprint 2 (OCR) eso no es viable.

## 💡 Acciones de mejora

### Acción 1 — Política de re-asignación si un miembro no responde
**Problema:** US-04 y US-06 quedaron huérfanas durante 7 días sin acción correctiva.
**Acción:** Definir umbral: si un miembro no se conecta a 2 dailies seguidos sin previo aviso, el SM convoca reunión de re-planificación al día siguiente. Las historias asignadas se devuelven a backlog o se reparten entre quien tenga capacidad.
**Responsable:** Marcos (Scrum Master)
**Plazo:** Sprint 2, Day 1 (2026-04-30) — documentado en `sprint-2-planning.md`.

### Acción 2 — Pareo en historia ancla del Sprint 2
**Problema:** Si Marcos cae con US-09 (OCR, 8 SP), el sprint se hunde igual que pasó con Camilo.
**Acción:** Pareo Lorena↔Marcos en US-09 al menos en la fase de spike técnico (esqueleto FastAPI + schema). Sesiones cortas y documentadas en `sprint-2-dailies.md`.
**Responsable:** Equipo (Lorena + Marcos)
**Plazo:** Sprint 2, Day 3 (2026-05-02).

### Acción 3 — Tests unitarios mínimos en US-09
**Problema:** Validación manual no escala con OCR (latencia + coste GPT-4o + variación de input).
**Acción:** Añadir `pytest` con al menos: (a) test de health, (b) test del schema Pydantic `AlbaranExtraido` con fixture válida e inválida, (c) test de extracción de la cola con mock de OpenAI.
**Responsable:** Marcos
**Plazo:** Antes del Sprint Review del Sprint 2 (2026-05-13).

### Acción 4 — Refinar criterios de aceptación de US-04 y US-06 antes de re-priorizar
**Problema:** Las dos historias devueltas al backlog no son ejecutables tal como están.
**Acción:** En el Refinement de Sprint 2 (Day 4, 2026-05-03), reescribir cada historia con criterios verificables, mockup y definición técnica básica.
**Responsable:** Lorena (PO)
**Plazo:** 2026-05-03.

### Acción 5 — Daily de 5 min con regla de "no avance = decisión"
**Problema:** Daily 2 a 5 todos reportaron "sin avances de Camilo" sin tomar acción.
**Acción:** Cualquier impedimento que aparezca en 2 dailies seguidos sin resolución se convierte en decisión obligatoria del equipo en ese segundo daily, no más tarde.
**Responsable:** Marcos (Scrum Master)
**Plazo:** Sprint 2, desde Day 1.

---

## Resumen
Sprint 1 cerró con 14/22 SP entregados (64%). El equipo activo cumplió DoD en todas sus historias. La incidencia central fue la ausencia no comunicada de un miembro, que costó 8 SP y dejó dos historias core sin terminar. Las 5 acciones acordadas atacan el problema de raíz (políticas de equipo + tests + refinamiento) y deben aplicarse desde el Day 1 del Sprint 2.

La lección principal: **sin redundancia, una baja silenciosa equivale a perder un tercio del sprint**. Sprint 2 incorpora pareo y políticas explícitas para que esto no vuelva a pasar.

# Definición de Hecho (Definition of Done) — AlbaranIA

**Autora:** Lorena López Bermúdez (Scrum Master)  
**Sprint:** Sprint 1

La Definición de Hecho establece, de forma compartida por el equipo, cuándo una
historia o un sprint se consideran realmente terminados. Complementa a los
criterios de aceptación: los criterios dicen *qué* debe hacer cada historia; la
DoD dice *qué calidad mínima* debe cumplir cualquier incremento antes de darse
por hecho.

## A nivel de Historia de Usuario

Una historia está "Hecha" cuando:

- Cumple todos sus criterios de aceptación (Given-When-Then) verificados.
- El código está integrado en `master` vía Pull Request revisado y aprobado por
  al menos un compañero.
- Respeta el aislamiento multi-tenant: filtra por `empresa_id` (ver ADR-001).
- Maneja los casos de error definidos en los criterios (mensaje, qué NO hace,
  dónde queda el usuario).
- No introduce regresiones en historias ya cerradas.

## A nivel de Sprint

Un sprint está "Hecho" cuando:

- Todas las historias comprometidas están "Hechas" o explícitamente devueltas al
  Product Backlog con justificación (p. ej. US-04 y US-06 del Sprint 1).
- El incremento es demostrable en la Sprint Review.
- La retrospectiva está documentada con acciones de mejora.
- El backlog queda actualizado y repriorizado para el siguiente sprint.

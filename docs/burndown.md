# Burndown — Sprint 1

Sprint: 2026-04-15 → 2026-04-29 (10 días laborables) · Capacidad: 22 SP

Registro diario de SP pendientes al finalizar cada día. Ideal = línea recta de 22 → 0. Real = curva 22 → 8 (8 SP no entregados por ausencia de Camilo en US-04 y US-06).

| Día | Fecha       | SP pendientes | SP hechos | Historias cerradas | Notas |
|-----|-------------|---------------|-----------|--------------------|-------|
| 0   | 2026-04-15  | 22 | 0  | — | Sprint Planning. Arranque oficial. |
| 1   | 2026-04-21  | 22 | 0  | — | Retraso de 6 días por confirmación de equipos; Camilo sin respuesta tras onboarding. |
| 2   | 2026-04-22  | 22 | 0  | — | Marcos arranca login (ALB-3); Lorena modela Empresa en Prisma. |
| 3   | 2026-04-23  | 22 | 0  | — | Login funcional contra usuario de prueba; sin avances de Camilo. |
| 4   | 2026-04-24  | 22 | 0  | — | ALB-1 al 70%, ALB-3 al 80%; ALB-5 arrancada. Riesgo Camilo flagged. |
| 5   | 2026-04-25  | 22 | 0  | — | Sábado, sin trabajo planificado. |
| 6   | 2026-04-26  | 22 | 0  | — | Domingo, sin trabajo planificado. |
| 7   | 2026-04-27  | 17 | 5  | US-01 | ALB-1 cerrada (validación CIF). ALB-3 a review. ALB-2 al 30%. |
| 8   | 2026-04-28  | 11 | 11 | US-03, US-05 | ALB-3 mergeada, ALB-5 cerrada. Omar autoriza documentar ausencia de Camilo. |
| 9   | 2026-04-28→29 | 8 | 14 | US-02 | ALB-2 cerrada en la mañana del 29. |
| 10  | 2026-04-29  | 8 | 14 | — | Cierre del sprint. US-04 y US-06 sin entregar (asignadas a Camilo). |

## Referencia ideal (línea recta 22 → 0)

| Día | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|-----|---|---|---|---|---|---|---|---|---|---|----|
| SP ideales  | 22 | 19.8 | 17.6 | 15.4 | 13.2 | 11 | 8.8 | 6.6 | 4.4 | 2.2 | 0 |
| SP reales   | 22 | 22   | 22   | 22   | 22   | 22 | 22  | 17  | 11  | 8   | 8 |

## Velocity

**Velocity Sprint 1 = 14 SP** (14 entregados / 22 planificados = 64%).

Esta cifra es la referencia de capacidad para el Sprint 2 con el equipo activo de 2 miembros. Si Camilo no se reincorpora, planificar Sprint 2 ≤ 14 SP.

## Lectura de la curva

- Tramo 1–6: estancada en 22 SP → arranque lento + fin de semana sin commits.
- Tramo 7–9: caída acelerada (de 22 a 8 en 3 días) → la mayor parte del trabajo se concentró en la última semana.
- Día 10: meseta en 8 SP → no se cerraron las historias de Camilo. Documentado en review/retro.

Acción para Sprint 2: empezar entregas desde el día 1 para evitar el patrón hockey-stick.

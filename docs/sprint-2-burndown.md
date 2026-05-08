# Burndown — Sprint 2

Sprint: 2026-04-30 → 2026-05-13 (10 días laborables) · Capacidad comprometida: 13.5 SP

Plan conservador: 13.5 SP por debajo de la velocity de 14 SP del Sprint 1 para absorber riesgo OCR. El spike técnico de US-09 se considera dentro de los 8 SP de la historia, por lo que el burndown empieza en 13.5 y solo descuenta cuando una historia llega a Done.

| Día | Fecha       | SP pendientes | SP hechos | Historias cerradas | Notas |
|-----|-------------|---------------|-----------|--------------------|-------|
| 1   | 2026-04-30  | 13.5 | 0   | — | Sprint Planning + arranque spike US-09. |
| 2   | 2026-05-01  | 13.5 | 0   | — | OCR scaffold + Prisma `Articulo`. |
| 3   | 2026-05-02  | 13.5 | 0   | — | Pareo Lorena↔Marcos en arquitectura OCR. |
| 4   | 2026-05-03  | 13.5 | 0   | — | Refinement US-04/US-06 (no cuenta SP). Endpoints listado/edición artículos. |
| 5   | 2026-05-04  | 10.5 | 3   | US-07 | US-07 cerrada por Lorena. Spike OCR completado salvo prompt-validation. |
| 6   | 2026-05-05  | 10.5 | 3   | —     | Prompt GPT-4o validado contra 3 PDFs sintéticos. US-11 arrancada. |
| 7   | 2026-05-06  | 10.5 | 3   | —     | Primer E2E OCR funcional en local (≈18 s para 1 página). TODO normalizador de unidades. |
| 8   | 2026-05-07  | 8    | 5.5 | US-11 | US-11 backend mergeada por la mañana. Tarde: hardening worker (timeouts, retries). |
| 9   | 2026-05-08  | 8    | 5.5 | —     | Normalizador de unidades + retry con backoff. Pendiente tests mock OpenAI. |
| 10  | 2026-05-13  |      |     |       | Sprint Review + Retrospectiva. |

> Días 10–13 se rellenan al final de cada jornada.

## Referencia ideal (línea recta 13.5 → 0)

| Día | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|-----|---|---|---|---|---|---|---|---|---|----|
| SP ideales | 12.15 | 10.8 | 9.45 | 8.1 | 6.75 | 5.4 | 4.05 | 2.7 | 1.35 | 0 |
| SP reales  | 13.5  | 13.5 | 13.5 | 13.5 | 10.5 | 10.5 | 10.5 | 8 | 8 | — |

## Lectura preliminar

- Días 1–4: meseta esperada porque ninguna historia entera se cierra durante el spike (US-07 estaba en curso, no terminada).
- Día 5: primer descuento (US-07 = 3 SP).
- Días 6–7: la curva debe acelerar cuando US-09 entregue valor verificable.
- Día 8: si US-11 (2.5 SP) cae el día 8, quedarían 8 SP (todo US-09) por cerrar entre días 9 y 13.

## Riesgo abierto
US-09 concentra 8 SP en un único miembro (Marcos). Si tiene un imprevisto entre Day 7 y Day 12, el sprint se hunde. El pareo del Day 3 mitiga el riesgo de conocimiento, no el de capacidad. Plan B: bajar US-11 a backlog si en Day 9 US-09 sigue por debajo del 50%.

## Velocity esperada
13.5 SP si se cumple el plan. Servirá como referencia para Sprint 3, que retomará US-04, US-06, US-10 y posiblemente US-16.

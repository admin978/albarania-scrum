# ADR-001 — Aislamiento multi-tenant vía `empresa_id` en el JWT

**Estado:** Propuesto · Sprint 1
**Autor:** Marcos García Manzano (Product Owner + Developer)

## Contexto

AlbaranIA es multi-empresa: cada empresa cliente ve únicamente sus propios
datos (usuarios, proveedores, albaranes, facturas). El Sprint 1 necesitaba un
mecanismo de aislamiento que fuera (a) simple de implementar en el MVP, (b)
coherente entre el backend Node/Express y el servicio OCR en Python, y (c) sin
introducir una capa de autorización por fila en base de datos antes de tiempo.

El dato de pertenencia (`empresa_id`) debe estar disponible en cada petición sin
obligar a una consulta extra a la base de datos por request, y debe propagarse
de forma fiable al servicio OCR, que valida el mismo token.

## Decisión

El token JWT emitido en el login incluye en su *payload* `user_id`, `empresa_id`
y `rol`. Todos los servicios derivan el `empresa_id` **del token**, nunca del
cuerpo de la petición, y filtran cada consulta por ese `empresa_id`. El
`JWT_SECRET` es compartido entre el backend Node y el servicio OCR (HS256), de
modo que el OCR valida el mismo token sin lógica de sesión propia.

El aislamiento se aplica, por tanto, en la **capa de servicios** (scoping por
`empresa_id`), no a nivel de base de datos.

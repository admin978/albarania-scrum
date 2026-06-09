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

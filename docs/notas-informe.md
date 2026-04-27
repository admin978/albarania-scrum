# Notas para el informe

Material crudo de las historias que ha llevado Marcos (US-03 y US-05). Pensado para que Lorena lo integre en las secciones del informe LaTeX donde haga falta.

## US-03 — Login con email y contraseña (ALB-3)

### Decisiones tomadas
- Librería JWT: `jsonwebtoken`. Se descartó `jose` por simplicidad y porque el servicio OCR (Python) ya valida tokens firmados con HS256.
- `JWT_SECRET` compartido entre el backend Node y el servicio OCR vía variable de entorno.
- Expiración del token: 24h. Suficiente para la jornada del operario; se puede ajustar más adelante.
- Passwords hasheadas con `bcrypt` (saltRounds=10).

### Implementación
- Endpoint `POST /api/auth/login` que devuelve `{ token, user: { id, empresa_id, rol } }`.
- El token incluye `empresa_id` y `rol` en el payload para que el resto de servicios filtren por tenant sin consultar la BD.
- En el frontend, sesión persistida en `localStorage`. Logout = limpiar token + redirección a `/login`.
- Mensaje de error genérico ("Email o contraseña incorrectos") para no filtrar si un email existe.

### Riesgos / mejoras futuras
- Refresh tokens: hoy si el token caduca el usuario re-loguea. En producción habría que implementar refresh.
- Rate limiting en el login para evitar fuerza bruta. Dejado fuera del Sprint 1.

## US-05 — CRUD de proveedores (ALB-5)

### Decisiones tomadas
- Soft delete (`deleted_at`) en lugar de borrado físico. Permite auditoría y recuperación.
- Filtrado por `empresa_id` extraído del JWT en cada request, no del body. Evita que un admin de una empresa borre proveedores de otra.
- Búsqueda por `nombre` y `CIF` con `LIKE` en Postgres; suficiente para los volúmenes que esperamos.

### Implementación
- Tabla Prisma `proveedores` con `empresa_id` indexado y restricción de unicidad `(empresa_id, cif)`.
- Endpoints REST: `GET /api/proveedores` (paginado), `POST`, `PUT /:id`, `DELETE /:id`.
- Validación de CIF en backend (mismo regex que en US-01 para consistencia).
- Frontend: tabla con paginación, búsqueda y acciones inline (editar, eliminar). Modal compartido para crear/editar.

### Riesgos / mejoras futuras
- Importación masiva (US-06) la lleva Camilo y depende de esta historia.
- El listado todavía no soporta filtrado avanzado (por estado, fecha de alta, etc.). Dejado para Sprint 2.

## Conclusiones que se pueden incluir en el informe

- La decisión de poner `empresa_id` en el JWT simplifica todo el aislamiento multi-tenant aguas abajo: ni el servicio OCR ni los endpoints de catálogos necesitan resolverlo de otra forma.
- El reparto inicial fue equilibrado en SP, pero la falta de participación de Camilo ha hecho que ALB-4 y ALB-6 queden bloqueadas. Es la principal lección del sprint.
- Las dependencias entre historias (ALB-2 depende de ALB-1; ALB-6 depende de ALB-5) hicieron que el orden de ejecución fuera bastante rígido. Para Sprint 2 conviene paralelizar mejor.

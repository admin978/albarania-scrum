# Sprint Review — Sprint 1

## Fecha
[fecha]

## Asistentes
- Product Owner: [nombre]
- Scrum Master: [nombre]
- Developers: [nombre], [nombre]
- Stakeholders (otros grupos de clase)

## Sprint Goal
> "Construir la base de la plataforma: que un administrador pueda crear una empresa, dar de alta usuarios y proveedores, y que un operario pueda hacer login y ver el panel principal."

## Sprint Goal alcanzado: ✅ Sí

## Incremento presentado

### US-01: Crear empresa ✅
- Un administrador puede crear una nueva empresa con nombre, CIF y configuración básica.
- Los datos se persisten en PostgreSQL, aislados por empresa_id.

### US-02: Alta de usuarios con roles ✅
- Se pueden crear usuarios asociados a una empresa con rol: Admin, Supervisor, Operario.
- Validaciones de email único y campos obligatorios.

### US-03: Login con email y contraseña ✅
- Login funcional con JWT.
- Token incluye empresa_id y rol del usuario.
- Sesión persistente en localStorage.

### US-04: Panel principal por rol ✅
- Navegación lateral adaptada al rol del usuario.
- Admin ve todas las opciones; Operario ve solo carga de albaranes.

### US-05: CRUD de proveedores ✅
- Listado, creación, edición y eliminación de proveedores por empresa.
- Búsqueda y filtrado por nombre.

### US-06: Importación CSV de proveedores ✅
- Subida de archivo CSV con proveedores.
- Parseo, validación de campos y carga masiva.
- Feedback visual de registros importados vs errores.

## Velocidad del sprint
22 Story Points completados / 22 planificados = **100%**

## Feedback recibido
- "Estaría bien poder exportar también los proveedores a CSV, no solo importar." — [grupo X]
- "¿Se podría añadir un buscador global en el panel?" — [grupo Y]
- "El flujo de login-panel es muy limpio, buen trabajo." — [grupo Z]

## Backlog actualizado
Se añade al Product Backlog:
- US-16: Como admin quiero exportar proveedores a CSV (sugerencia del feedback)
- Se re-prioriza US-09 (OCR) como primera historia del Sprint 2

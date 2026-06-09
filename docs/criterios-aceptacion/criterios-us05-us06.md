# Criterios de Aceptación — US-05, US-06 y Resumen

**Proyecto:** AlbaranIA  
**Redactado por:** Lorena López Bermúdez (Scrum Master)  
**Sprint:** Sprint 1 (24–29 abril 2026)

---

## US-05: CRUD de proveedores (ALB-5) — 3 SP

### Criterio 1 — Alta exitosa de proveedor

    GIVEN el usuario con rol "Admin" está autenticado en "AlbaranIA SL"
          y no existe ningún proveedor con CIF "B87654321"
    WHEN el admin completa el formulario con nombre "Proveedor X",
         CIF "B87654321", contacto "Juan Pérez" y hace clic en "Guardar"
    THEN se crea el proveedor con empresa_id de "AlbaranIA SL"
         y aparece en el listado de proveedores

### Criterio 2 — Validación CIF duplicado dentro de la misma empresa

    GIVEN ya existe un proveedor con CIF "B87654321" en "AlbaranIA SL"
    WHEN el admin intenta crear otro proveedor con CIF "B87654321"
    THEN el sistema muestra "Ya existe un proveedor con este CIF en tu empresa",
         NO crea el proveedor duplicado

### Criterio 3 — Validación de formato CIF

    GIVEN el usuario con rol "Supervisor" está autenticado
    WHEN el supervisor intenta crear un proveedor con CIF "12345ABC"
         (formato inválido)
    THEN el sistema muestra "El CIF debe tener formato válido español
         (letra + 8 dígitos o letra + 7 dígitos + letra)",
         NO crea el proveedor

### Criterio 4 — Proveedor con CIF existente en otra empresa (caso límite)

    GIVEN el admin está autenticado en "Construcciones López SL"
    WHEN el admin intenta crear un proveedor con CIF "B87654321"
         que ya existe en otra empresa cliente ("Transportes García SL")
    THEN el sistema permite la creación (datos independientes por empresa),
         lo asocia a empresa_id de "Construcciones López SL",
         y NO revela que ese CIF pertenece a otra empresa cliente

**Nota técnica (Privacy by Design):** Aislamiento multi-tenant.
En el MVP se permite el duplicado entre empresas para no exponer
información de otros clientes. Mejora futura: integración con AEAT
para verificación de datos oficiales.

### Criterio 5 — Validación de permisos (solo Admin y Supervisor)

    GIVEN existe un usuario con rol "Operario" autenticado
    WHEN el operario intenta acceder a la pantalla de alta de proveedores
    THEN el sistema muestra "No tienes permisos para esta acción.
         Solo Admins y Supervisores pueden gestionar proveedores"
         y redirige al panel principal

---

## US-06: Importación de proveedores desde CSV (ALB-6) — 5 SP

> **Nota:** Esta historia fue devuelta al Product Backlog sin completarse
> durante el Sprint 1 debido a impedimentos del equipo.

### Criterio 1 — Importación exitosa de archivo válido

    GIVEN el admin está autenticado en "Transportes Portes SL"
          y NO existen proveedores registrados previamente
    WHEN el admin sube un CSV con 3 líneas válidas:
         "Proveedor A,B11111111,Juan Pérez"
         "Proveedor B,B22222222,Ana Gómez"
         "Proveedor C,B33333333,Pedro López"
    THEN se crean 3 proveedores asociados a la empresa,
         el sistema muestra "✓ 3 proveedores importados exitosamente"
         y redirige al listado donde aparecen ordenados alfabéticamente

### Criterio 2 — Archivo con líneas inválidas (éxito parcial)

    GIVEN el admin está autenticado y ya existe 1 proveedor con CIF "B11111111"
    WHEN el admin sube un CSV con 5 líneas:
         2 válidas, 1 con CIF duplicado, 1 con nombre vacío, 1 con CIF inválido
    THEN se crean solo los 2 proveedores válidos,
         el sistema muestra un resumen detallando los errores
         línea por línea (CIF duplicado, nombre vacío, formato inválido)
         y redirige al listado mostrando 3 proveedores totales

### Criterio 3 — Supervisor sin permisos para importar

    GIVEN el usuario con rol "Supervisor" está autenticado
    WHEN el supervisor intenta acceder a /proveedores/importar
    THEN el sistema muestra "No tienes permisos para importar proveedores.
         Solo los Admins pueden realizar importaciones masivas"
         y redirige al listado de proveedores

---

## Resumen estadístico

| Historia | SP | Criterios | Casos éxito | Casos error |
|---|---|---|---|---|
| US-01 Crear empresa | 5 | 3 | 1 | 2 |
| US-02 Alta usuarios | 3 | 3 | 1 | 2 |
| US-03 Login | 3 | 4 | 1 | 3 |
| US-04 Panel principal | 3 | 3 | 2 | 1 |
| US-05 CRUD proveedores | 3 | 5 | 2 | 3 |
| US-06 Importar CSV | 5 | 3 | 2 (1 parcial) | 1 |
| **TOTAL** | **22** | **21** | **9** | **12** |

> **Nota:** recuento corregido tras la revisión de Marcos en el PR #5.
> Los criterios de permisos por rol se contabilizan como casos de error
> (deniegan una acción), no como categoría aparte. 9 + 12 = 21 criterios.

---

## Patrones aplicados

**Estructura consistente:** Todos los criterios siguen
`GIVEN [estado] / WHEN [acción] / THEN [resultado + qué NO hace]`.

**Datos concretos:** emails específicos, CIFs reales de ejemplo,
nombres concretos — reproducibles para testing.

**Privacy by Design:**
- Contraseñas hasheadas (bcrypt)
- Mensajes genéricos en login (anti-enumeración de usuarios)
- Filtrado por `empresa_id` desde JWT (multi-tenant seguro)
- Aislamiento de datos entre empresas (caso límite US-05 C4)
- Tokens con expiración

---

**Autor:** Lorena López Bermúdez (Scrum Master)  
**Fecha:** 4 mayo 2026

---

## Mejoras futuras identificadas en revisión

Surgidas del code review de Marcos (PR #5):

- **Validación de CIF con dígito de control:** los criterios actuales
  validan el *formato* del CIF (letra + dígitos), pero no el dígito de
  control oficial. Un "B00000000" pasaría el regex siendo inválido. En
  una iteración futura debería comprobarse el dígito de control según
  el algoritmo de la AEAT, no solo la forma.

- **Criterios explícitos de campos vacíos:** conviene añadir criterios
  Given-When-Then dedicados a la validación de campos obligatorios vacíos
  (nombre, email, etc.) de forma sistemática en todas las historias, no
  solo donde aparece de forma incidental (como en US-06).

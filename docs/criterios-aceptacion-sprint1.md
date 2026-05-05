# Criterios de Aceptación - Sprint 1
 
**Proyecto:** AlbaranIA  
**Formato:** Given-When-Then  
**Redactado por:** Lorena López Bermúdez (Scrum Master)  
**Fecha:** 4 mayo 2026  
**Sprint:** Sprint 1 (24-29 abril 2026)  
**Total Story Points:** 22 SP  
**Total Criterios:** 21
 
---
 
## US-01: Crear empresa en la plataforma (ALB-1) - 5 SP
 
### Criterio 1 — Alta exitosa de empresa
 
```
GIVEN el visitante accede al formulario de registro 
      y no existe ninguna empresa con CIF "B87654321" 
      ni usuario con email "juan.lopez@transportesportes.es"
WHEN el visitante completa el formulario con nombre "Transportes Portes", 
     CIF "B87654321", email admin "juan.lopez@transportesportes.es", 
     sector "Logística", contraseña "Pass1234!" y hace clic en "Crear cuenta"
THEN se crea la empresa en la tabla `empresas` con `empresa_id` único generado, 
     `nombre`="Transportes Portes", `cif`="B87654321", 
     `email_admin`="juan.lopez@transportesportes.es", `sector`="Logística", 
     se crea el usuario admin en la tabla `usuarios` con `usuario_id` único, 
     `empresa_id` apuntando a la empresa creada, 
     `email`="juan.lopez@transportesportes.es", 
     `nombre`="Juan López", `rol`="Admin", contraseña hasheada, 
     se genera un token JWT que contiene `user_id`, `empresa_id` y `rol`="Admin", 
     se guarda en localStorage y se redirige a /panel
```
 
### Criterio 2 — Validación CIF duplicado
 
```
GIVEN ya existe una empresa registrada con CIF "B87654321"
WHEN el visitante intenta crear otra empresa con nombre "Nueva Empresa SL", 
     CIF "B87654321", email admin "ana.garcia@nuevaempresa.com", 
     sector "Construcción", contraseña "Pass5678!" y hace clic en "Crear cuenta"
THEN el sistema muestra el error "Ya existe una empresa registrada con este CIF", 
     NO crea la empresa, NO crea ningún usuario y permanece en el formulario 
     con los datos ingresados
```
 
### Criterio 3 — Validación email duplicado
 
```
GIVEN ya existe un usuario con email "juan.lopez@transportesportes.es"
WHEN el visitante intenta crear una empresa con nombre "Otra Empresa SL", 
     CIF "B11111111", email admin "juan.lopez@transportesportes.es", 
     sector "Tecnología", contraseña "Pass9012!" y hace clic en "Crear cuenta"
THEN el sistema muestra el error "Este email ya está registrado", 
     NO crea la empresa, NO crea ningún usuario y permanece en el formulario 
     con los datos ingresados
```
 
---
 
## US-02: Alta de usuarios con roles (ALB-2) - 3 SP
 
### Criterio 1 — Alta exitosa de usuario
 
```
GIVEN el admin está autenticado en la empresa "AlbaranIA SL" 
      y no existe ningún usuario con email "juan.garcia@albarania.com"
WHEN el admin completa el formulario con nombre "Juan García", 
     email "juan.garcia@albarania.com", rol "Supervisor", 
     contraseña "Pass123!" y hace clic en "Guardar"
THEN se crea el usuario en la tabla `usuarios` con `usuario_id` único generado, 
     `empresa_id` de "AlbaranIA SL", `nombre`="Juan García", 
     `email`="juan.garcia@albarania.com", `rol`="Supervisor", 
     contraseña hasheada, y aparece en el listado de usuarios de la empresa
```
 
### Criterio 2 — Validación email duplicado
 
```
GIVEN el admin está autenticado en la empresa "AlbaranIA SL" 
      y ya existe un usuario con email "juan.garcia@albarania.com"
WHEN el admin intenta crear otro usuario con email "juan.garcia@albarania.com", 
     nombre "Juan García Pérez", rol "Operario" y hace clic en "Guardar"
THEN el sistema muestra el error "Este email ya está registrado", 
     NO crea el usuario duplicado y permanece en el formulario
```
 
### Criterio 3 — Validación de permisos por rol
 
```
GIVEN existe un usuario con rol "Supervisor" autenticado en "AlbaranIA SL"
WHEN el supervisor intenta acceder a la pantalla de alta de usuarios
THEN el sistema muestra el error "No tienes permisos para esta acción. 
     Solo los Admins pueden crear usuarios" y redirige al panel principal
```
 
---
 
## US-03: Login con email y contraseña (ALB-3) - 3 SP
 
### Criterio 1 — Login exitoso
 
```
GIVEN existe un usuario con email "lorena@albarania.com", 
      contraseña "Pass123!" y rol "Admin" en la empresa "AlbaranIA SL"
WHEN el usuario ingresa email "lorena@albarania.com", 
     contraseña "Pass123!" y hace clic en "Iniciar sesión"
THEN el sistema devuelve un token JWT que contiene `user_id`, 
     `empresa_id` y `rol`="Admin", guarda el token en localStorage 
     y redirige al panel en /panel
```
 
### Criterio 2 — Login fallido por contraseña incorrecta
 
```
GIVEN existe un usuario con email "lorena@albarania.com" 
      y contraseña "Pass123!"
WHEN el usuario ingresa email "lorena@albarania.com" 
     y contraseña "PassIncorrecta456" y hace clic en "Iniciar sesión"
THEN el sistema muestra el error "Email o contraseña incorrectos", 
     NO genera token JWT y permanece en la página de login
```
 
### Criterio 3 — Login fallido por email no registrado
 
```
GIVEN no existe ningún usuario con email "noexiste@albarania.com"
WHEN el usuario ingresa email "noexiste@albarania.com", 
     contraseña "Pass123!" y hace clic en "Iniciar sesión"
THEN el sistema muestra el error "Email o contraseña incorrectos", 
     NO genera token JWT y permanece en la página de login
```
 
**Nota de seguridad:** El mensaje es idéntico en ambos casos de error (contraseña incorrecta o email no existe) para no revelar si el email está registrado o no. Esto previene ataques de enumeración de usuarios.
 
### Criterio 4 — Token expirado
 
```
GIVEN el usuario tiene un token JWT expirado guardado en localStorage
WHEN el usuario intenta acceder a /panel
THEN el sistema muestra el mensaje "Tu sesión ha expirado. 
     Por favor, inicia sesión de nuevo", borra el token expirado 
     del localStorage y redirige a la página de login
```
 
---
 
## US-04: Panel principal con navegación por rol (ALB-4) - 3 SP
 
**Nota:** Esta historia fue devuelta al Product Backlog sin completarse durante el Sprint 1 debido a impedimentos del equipo. Los criterios se mantienen como referencia para futuros sprints.
 
### Criterio 1 — Navegación adaptada a rol Admin
 
```
GIVEN el usuario con rol "Admin" está autenticado en la empresa "Transportes Portes SL"
WHEN el usuario accede al panel principal en /panel
THEN el sistema muestra el menú lateral con todas las opciones disponibles: 
     Empresa, Usuarios, Proveedores, Artículos, Albaranes, Facturas y Dashboard, 
     y el panel principal muestra un resumen con widgets de albaranes procesados, 
     pendientes y facturas
```
 
### Criterio 2 — Navegación adaptada a rol Operario
 
```
GIVEN el usuario con rol "Operario" está autenticado en la empresa "Transportes Portes SL"
WHEN el usuario accede al panel principal en /panel
THEN el sistema muestra el menú lateral únicamente con las opciones: 
     "Subir albarán" y "Mis albaranes", 
     y el panel principal muestra solo los albaranes que el operario ha subido
```
 
### Criterio 3 — Validación de permisos en navegación
 
```
GIVEN el usuario con rol "Operario" está autenticado en la empresa "Transportes Portes SL"
WHEN el operario intenta acceder manualmente a la URL /proveedores 
     (ruta restringida para su rol)
THEN el sistema muestra el error "No tienes permisos para acceder a esta sección" 
     y redirige al panel principal en /panel
```
 
---
 
## US-05: CRUD de proveedores (ALB-5) - 3 SP
 
### Criterio 1 — Alta exitosa de proveedor
 
```
GIVEN el usuario con rol "Admin" está autenticado en la empresa 
      "AlbaranIA SL" y no existe ningún proveedor con CIF "B87654321"
WHEN el admin completa el formulario con nombre "Proveedor X", 
     CIF "B87654321", contacto "Juan Pérez" y hace clic en "Guardar"
THEN se crea el proveedor en la tabla `proveedores` con `proveedor_id` 
     único generado, `empresa_id` de "AlbaranIA SL", 
     `nombre`="Proveedor X", `cif`="B87654321", 
     `contacto`="Juan Pérez", y aparece en el listado de proveedores 
     de la empresa
```
 
### Criterio 2 — Validación CIF duplicado dentro de la misma empresa
 
```
GIVEN el usuario con rol "Admin" está autenticado en la empresa 
      "AlbaranIA SL" y ya existe un proveedor con CIF "B87654321"
WHEN el admin intenta crear otro proveedor con nombre "Proveedor Y", 
     CIF "B87654321", contacto "Ana Gómez" y hace clic en "Guardar"
THEN el sistema muestra el error "Ya existe un proveedor con este CIF 
     en tu empresa", NO crea el proveedor duplicado y permanece en 
     el formulario con los datos ingresados
```
 
### Criterio 3 — Validación de formato CIF
 
```
GIVEN el usuario con rol "Supervisor" está autenticado en "AlbaranIA SL"
WHEN el supervisor completa el formulario con nombre "Proveedor Z", 
     CIF "12345ABC" (formato inválido), contacto "Pedro López" 
     y hace clic en "Guardar"
THEN el sistema muestra el error "El CIF debe tener formato válido 
     español (letra + 8 dígitos o letra + 7 dígitos + letra)", 
     NO crea el proveedor y permanece en el formulario
```
 
### Criterio 4 — Proveedor con CIF existente en otra empresa (caso límite)
 
```
GIVEN el usuario con rol "Admin" está autenticado en la empresa 
      "Construcciones López SL"
WHEN el admin intenta crear un proveedor con CIF "B87654321" 
     que ya existe como proveedor en otra empresa cliente de AlbaranIA 
     ("Transportes García SL")
THEN el sistema permite la creación del proveedor (datos independientes 
     por empresa), lo asocia a `empresa_id` de "Construcciones López SL", 
     y NO revela que ese CIF pertenece a otra empresa cliente de la plataforma
```
 
**Nota técnica:** Este criterio documenta explícitamente el comportamiento en el caso límite identificado. En el MVP se permite el duplicado entre empresas. Mejora futura: integración con AEAT para verificación de datos oficiales.
 
### Criterio 5 — Validación de permisos (solo Admin y Supervisor)
 
```
GIVEN existe un usuario con rol "Operario" autenticado en "AlbaranIA SL"
WHEN el operario intenta acceder a la pantalla de alta de proveedores
THEN el sistema muestra el error "No tienes permisos para esta acción. 
     Solo Admins y Supervisores pueden gestionar proveedores" 
     y redirige al panel principal
```
 
---
 
## US-06: Importación de proveedores desde CSV (ALB-6) - 5 SP
 
**Nota:** Esta historia fue devuelta al Product Backlog sin completarse durante el Sprint 1 debido a impedimentos del equipo. Los criterios se mantienen como referencia para futuros sprints.
 
### Criterio 1 — Importación exitosa de archivo válido
 
```
GIVEN el usuario con rol "Admin" está autenticado en la empresa 
      "Transportes Portes SL" y NO existen proveedores registrados previamente
WHEN el admin sube un archivo CSV con 3 líneas válidas:
     "Proveedor A,B11111111,Juan Pérez"
     "Proveedor B,B22222222,Ana Gómez"
     "Proveedor C,B33333333,Pedro López"
     y hace clic en "Importar"
THEN se crean 3 proveedores en la tabla `proveedores` asociados 
     a `empresa_id` de "Transportes Portes SL" con los datos del archivo, 
     el sistema muestra el mensaje "✓ 3 proveedores importados exitosamente", 
     y redirige al listado de proveedores en /proveedores donde aparecen 
     los 3 nuevos proveedores ordenados alfabéticamente
```
 
### Criterio 2 — Archivo con líneas inválidas (éxito parcial)
 
```
GIVEN el usuario con rol "Admin" está autenticado en la empresa 
      "Transportes Portes SL" y ya existe 1 proveedor registrado: 
      "Proveedor Duplicado" (CIF B11111111, contacto: Carlos Ruiz)
WHEN el admin sube un archivo CSV con 5 líneas:
     "Proveedor A,B22222222,Juan Pérez" (válido)
     "Proveedor B,B33333333,Ana Gómez" (válido)
     "Proveedor Duplicado,B11111111,Pedro López" (CIF duplicado)
     ",B44444444,María Sanz" (nombre vacío)
     "Proveedor E,INVALIDO,Luis Torres" (CIF formato incorrecto)
     y hace clic en "Importar"
THEN se crean 2 proveedores en la tabla `proveedores`: 
     "Proveedor A" (B22222222) y "Proveedor B" (B33333333), 
     el sistema muestra el mensaje de resumen:
     "✓ 2 proveedores importados exitosamente
      ✗ 3 líneas con errores:
      - Línea 3: El CIF B11111111 ya existe en tu empresa
      - Línea 4: El nombre del proveedor no puede estar vacío
      - Línea 5: El CIF 'INVALIDO' no tiene formato válido (debe ser letra + 8 dígitos)"
     y redirige al listado de proveedores mostrando 3 proveedores totales 
     (1 existente + 2 recién importados)
```
 
### Criterio 3 — Supervisor sin permisos para importar
 
```
GIVEN el usuario con rol "Supervisor" está autenticado en la empresa 
      "Transportes Portes SL"
WHEN el supervisor intenta acceder a la pantalla de importación 
     de proveedores en /proveedores/importar
THEN el sistema muestra el error "No tienes permisos para importar proveedores. 
     Solo los Admins pueden realizar importaciones masivas", 
     NO muestra el formulario de importación 
     y redirige al listado de proveedores en /proveedores
```
 
---
 
## Resumen Estadístico
 
| Historia | SP | Criterios | Casos éxito | Casos error | Validaciones |
|---|---|---|---|---|---|
| US-01 Crear empresa | 5 | 3 | 1 | 2 | Email + CIF |
| US-02 Alta usuarios | 3 | 3 | 1 | 1 | 1 permisos |
| US-03 Login | 3 | 4 | 1 | 2 | 1 token |
| US-04 Panel principal | 3 | 3 | 2 | 0 | 1 permisos |
| US-05 CRUD proveedores | 3 | 5 | 1 | 2 | 1 permisos + 1 caso límite |
| US-06 Importar CSV | 5 | 3 | 1 + 1 parcial | 0 | 1 permisos |
| **TOTAL** | **22 SP** | **21** | **9** | **7** | **5** |
 
---
 
## Patrones Identificados
 
### Estructura consistente
Todos los criterios siguen el patrón:
```
GIVEN [autenticación + estado de datos]
WHEN [acción específica con datos concretos]
THEN [resultado observable + qué NO hace en caso de error]
```
 
### Datos concretos
- ✅ Emails específicos (no genéricos como "usuario@example.com")
- ✅ CIFs específicos de ejemplo (B87654321, B11111111)
- ✅ Nombres concretos de empresas y personas
- ✅ Datos reproducibles para testing
### Casos de error completos
Todo error especifica:
1. **Mensaje exacto** mostrado al usuario
2. **Qué NO hace** el sistema (no crea, no genera token)
3. **Dónde permanece** el usuario (en el formulario, en login)
### Seguridad by design
- Contraseñas hasheadas (bcrypt)
- Mensajes de error genéricos en login (anti-enumeración de usuarios)
- Mensajes de error específicos en registro (UX clara)
- Validación de permisos por rol
- Tokens con expiración
- Filtrado por `empresa_id` desde JWT (multi-tenant seguro)
---
 
## Notas de Implementación
 
### Multi-tenant
Todos los criterios respetan el aislamiento por `empresa_id`:
- Cada empresa ve SOLO sus propios datos
- El `empresa_id` se extrae del JWT (no del body de la request)
- Las validaciones de duplicados son por empresa (excepto emails globales)
### Consistencia de validaciones
- **CIF:** Formato español validado en backend
- **Email:** Único globalmente (no por empresa)
- **Roles:** Admin > Supervisor > Operario (jerarquía de permisos)
### Casos límite documentados
- **US-05 Criterio 4:** Proveedor con CIF existente en otra empresa
  - Decisión: permitir duplicados entre empresas
  - Razón: privacidad multi-tenant
  - Mejora futura: integración AEAT
---
 
**Documento generado:** 4 mayo 2026  
**Autor:** Lorena López Bermúdez (Scrum Master)  
**Proyecto:** AlbaranIA - Metodologías Ágiles (Universidad Europea)
 

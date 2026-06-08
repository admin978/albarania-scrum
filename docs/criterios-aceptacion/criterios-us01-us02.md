# Criterios de Aceptación — US-01 y US-02

**Proyecto:** AlbaranIA  
**Redactado por:** Lorena López Bermúdez (Scrum Master)  
**Sprint:** Sprint 1 (24–29 abril 2026)

---

## US-01: Crear empresa en la plataforma (ALB-1) — 5 SP

### Criterio 1 — Alta exitosa de empresa

    GIVEN el visitante accede al formulario de registro
          y no existe ninguna empresa con CIF "B87654321"
          ni usuario con email "juan.lopez@transportesportes.es"
    WHEN el visitante completa el formulario con nombre "Transportes Portes",
         CIF "B87654321", email admin "juan.lopez@transportesportes.es",
         sector "Logística", contraseña "Pass1234!" y hace clic en "Crear cuenta"
    THEN se crea la empresa en la tabla empresas con empresa_id único generado,
         se crea el usuario admin con rol="Admin" y contraseña hasheada,
         se genera un token JWT con user_id, empresa_id y rol="Admin",
         se guarda en localStorage y se redirige a /panel

### Criterio 2 — Validación CIF duplicado

    GIVEN ya existe una empresa registrada con CIF "B87654321"
    WHEN el visitante intenta crear otra empresa con CIF "B87654321"
    THEN el sistema muestra "Ya existe una empresa registrada con este CIF",
         NO crea la empresa, NO crea ningún usuario

### Criterio 3 — Validación email duplicado

    GIVEN ya existe un usuario con email "juan.lopez@transportesportes.es"
    WHEN el visitante intenta crear una empresa con ese mismo email de admin
    THEN el sistema muestra "Este email ya está registrado",
         NO crea la empresa, NO crea ningún usuario

---

## US-02: Alta de usuarios con roles (ALB-2) — 3 SP

### Criterio 1 — Alta exitosa de usuario

    GIVEN el admin está autenticado en "AlbaranIA SL"
          y no existe usuario con email "juan.garcia@albarania.com"
    WHEN el admin completa el formulario con nombre "Juan García",
         email "juan.garcia@albarania.com", rol "Supervisor"
         y hace clic en "Guardar"
    THEN se crea el usuario con empresa_id de "AlbaranIA SL",
         contraseña hasheada, y aparece en el listado de usuarios

### Criterio 2 — Validación email duplicado

    GIVEN ya existe un usuario con email "juan.garcia@albarania.com"
    WHEN el admin intenta crear otro usuario con ese email
    THEN el sistema muestra "Este email ya está registrado",
         NO crea el usuario duplicado

### Criterio 3 — Validación de permisos por rol

    GIVEN existe un usuario con rol "Supervisor" autenticado
    WHEN el supervisor intenta acceder a la pantalla de alta de usuarios
    THEN el sistema muestra "No tienes permisos para esta acción.
         Solo los Admins pueden crear usuarios"
         y redirige al panel principal

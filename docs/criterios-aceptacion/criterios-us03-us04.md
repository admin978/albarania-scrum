# Criterios de Aceptación — US-03 y US-04

**Proyecto:** AlbaranIA  
**Redactado por:** Lorena López Bermúdez (Scrum Master)  
**Sprint:** Sprint 1 (24–29 abril 2026)

---

## US-03: Login con email y contraseña (ALB-3) — 3 SP

### Criterio 1 — Login exitoso

    GIVEN existe un usuario con email "lorena@albarania.com",
          contraseña "Pass123!" y rol "Admin" en la empresa "AlbaranIA SL"
    WHEN el usuario ingresa email "lorena@albarania.com",
         contraseña "Pass123!" y hace clic en "Iniciar sesión"
    THEN el sistema devuelve un token JWT que contiene user_id,
         empresa_id y rol="Admin", guarda el token en localStorage
         y redirige al panel en /panel

### Criterio 2 — Login fallido por contraseña incorrecta

    GIVEN existe un usuario con email "lorena@albarania.com"
          y contraseña "Pass123!"
    WHEN el usuario ingresa la contraseña "PassIncorrecta456"
    THEN el sistema muestra "Email o contraseña incorrectos",
         NO genera token JWT y permanece en la página de login

### Criterio 3 — Login fallido por email no registrado

    GIVEN no existe ningún usuario con email "noexiste@albarania.com"
    WHEN el usuario ingresa email "noexiste@albarania.com"
    THEN el sistema muestra "Email o contraseña incorrectos",
         NO genera token JWT y permanece en la página de login

**Nota de seguridad (Privacy by Design):** El mensaje es idéntico en
ambos casos de error para no revelar si el email está registrado.
Esto previene ataques de enumeración de usuarios.

### Criterio 4 — Token expirado

    GIVEN el usuario tiene un token JWT expirado en localStorage
    WHEN el usuario intenta acceder a /panel
    THEN el sistema muestra "Tu sesión ha expirado.
         Por favor, inicia sesión de nuevo",
         borra el token expirado del localStorage
         y redirige a la página de login

---

## US-04: Panel principal con navegación por rol (ALB-4) — 3 SP

> **Nota:** Esta historia fue devuelta al Product Backlog sin completarse
> durante el Sprint 1 debido a impedimentos del equipo. Los criterios se
> mantienen como referencia para futuros sprints.

### Criterio 1 — Navegación adaptada a rol Admin

    GIVEN el usuario con rol "Admin" está autenticado en "Transportes Portes SL"
    WHEN el usuario accede al panel principal en /panel
    THEN el sistema muestra el menú lateral con todas las opciones:
         Empresa, Usuarios, Proveedores, Artículos, Albaranes,
         Facturas y Dashboard,
         y el panel muestra widgets de albaranes procesados,
         pendientes y facturas

### Criterio 2 — Navegación adaptada a rol Operario

    GIVEN el usuario con rol "Operario" está autenticado en "Transportes Portes SL"
    WHEN el usuario accede al panel principal en /panel
    THEN el sistema muestra el menú lateral únicamente con:
         "Subir albarán" y "Mis albaranes",
         y el panel muestra solo los albaranes que el operario ha subido

### Criterio 3 — Validación de permisos en navegación

    GIVEN el usuario con rol "Operario" está autenticado
    WHEN el operario intenta acceder manualmente a /proveedores
         (ruta restringida para su rol)
    THEN el sistema muestra "No tienes permisos para acceder a esta sección"
         y redirige al panel principal en /panel

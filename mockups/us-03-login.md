# US-03 — Login (ALB-3)

Pantalla pública. JWT emitido al autenticar.

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│                      AlbaranIA                           │
│                                                          │
│          ┌────────────────────────────────────┐          │
│          │                                    │          │
│          │   Iniciar sesión                   │          │
│          │                                    │          │
│          │   Email                            │          │
│          │   [______________________________] │          │
│          │                                    │          │
│          │   Contraseña                       │          │
│          │   [______________________________] │          │
│          │                                    │          │
│          │   ☐ Mantener sesión iniciada      │          │
│          │                                    │          │
│          │          [  Entrar  → ]            │          │
│          │                                    │          │
│          │   ¿Olvidaste tu contraseña?        │          │
│          │   ¿Nueva empresa? Crear cuenta     │          │
│          │                                    │          │
│          └────────────────────────────────────┘          │
│                                                          │
└──────────────────────────────────────────────────────────┘

Error credenciales inválidas (sin filtrar si existe email):
  ⚠️  Email o contraseña incorrectos
```

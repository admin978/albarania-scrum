# US-06 — Importar CSV proveedores (ALB-6)

Flujo en 3 pasos: subida → preview → resultado.

```
Paso 1 — Subida
┌──────────────────────────────────────────────────────────┐
│  Importar proveedores desde CSV                   [ X ]  │
├──────────────────────────────────────────────────────────┤
│                                                          │
│   ┌────────────────────────────────────────────────┐    │
│   │                                                │    │
│   │     📄  Arrastra un .csv aquí                  │    │
│   │                                                │    │
│   │            o haz click para elegir             │    │
│   │                                                │    │
│   └────────────────────────────────────────────────┘    │
│                                                          │
│   Columnas esperadas:                                    │
│   nombre, cif, email, telefono, direccion                │
│                                                          │
│   Máx. 5 MB · Encoding UTF-8 o Latin-1                   │
│                                                          │
└──────────────────────────────────────────────────────────┘

Paso 2 — Preview (10 primeras filas)
┌──────────────────────────────────────────────────────────┐
│  proveedores.csv  (342 filas detectadas)                 │
├──────────────────────────────────────────────────────────┤
│  ┌────┬─────────────┬───────────┬──────────┬──────────┐  │
│  │ #  │ Nombre      │ CIF       │ Email    │ Teléfono │  │
│  ├────┼─────────────┼───────────┼──────────┼──────────┤  │
│  │ 1  │ Papelería.. │ B1234567. │ p@...    │ 9...     │  │
│  │ 2  │ Tecno Ibé.. │ A9876543. │ t@...    │ 9...     │  │
│  │ .. │ ...                                            │  │
│  └────┴─────────────┴───────────┴──────────┴──────────┘  │
│                                                          │
│       [ Cancelar ]        [ Importar 342 filas  → ]      │
└──────────────────────────────────────────────────────────┘

Paso 3 — Resultado
┌──────────────────────────────────────────────────────────┐
│   ✅  Importación completada                             │
│                                                          │
│       Importados:     338                                │
│       Errores:          4                                │
│                                                          │
│   Detalles de errores:                                   │
│   • Línea 47: CIF inválido                               │
│   • Línea 112: email duplicado                           │
│   • Línea 201: nombre vacío                              │
│   • Línea 284: encoding ilegible                         │
│                                                          │
│                      [ Ver proveedores ]                 │
└──────────────────────────────────────────────────────────┘
```

**Transacción:** si >50% de filas fallan → rollback completo, no importa ninguna.

# Product Backlog — AlbaranIA

## Épicas

### E1: Autenticación y gestión de usuarios (Alta)
Registro de empresas, alta de usuarios, login JWT, roles (Admin, Supervisor, Operario).

### E2: Gestión de catálogos (Alta)
CRUD de proveedores y artículos por empresa. Importación masiva desde CSV.

### E3: Carga y procesamiento OCR (Alta)
Subida de PDF/imagen, procesamiento con IA (GPT-4o), extracción de datos, vista previa.

### E4: Flujo de validación (Media)
Máquina de estados (Borrador → Pendiente → Validado → Anulado), gate de ingeniería, auditoría.

### E5: Facturación y exportación (Media)
Agrupación en facturas, generación de PDF, exportación para ERP.

### E6: Dashboard y reporting (Baja)
Panel de control: albaranes procesados, pendientes, importes, métricas OCR.

---

## Historias de usuario

| ID | Épica | Historia | Prioridad | SP |
|----|-------|----------|-----------|-----|
| US-01 | E1 | Como admin quiero crear una empresa para gestionar sus datos de forma aislada | Alta | 5 |
| US-02 | E1 | Como admin quiero dar de alta usuarios y asignarles rol | Alta | 3 |
| US-03 | E1 | Como usuario quiero hacer login con email/contraseña | Alta | 3 |
| US-04 | E1 | Como usuario quiero ver el panel principal según mi rol | Alta | 3 |
| US-05 | E2 | Como admin quiero crear, editar y eliminar proveedores | Alta | 3 |
| US-06 | E2 | Como admin quiero importar proveedores desde CSV | Alta | 5 |
| US-07 | E2 | Como admin quiero crear, editar y eliminar artículos | Media | 3 |
| US-08 | E2 | Como admin quiero importar artículos desde CSV | Media | 5 |
| US-09 | E3 | Como operario quiero subir un PDF de albarán y que se extraigan los datos con IA | Alta | 8 |
| US-10 | E3 | Como operario quiero revisar y corregir los datos extraídos antes de confirmar | Alta | 5 |
| US-11 | E4 | Como supervisor quiero revisar albaranes pendientes y aprobarlos o rechazarlos | Media | 5 |
| US-12 | E4 | Como admin quiero configurar el umbral de importe que requiere validación | Media | 2 |
| US-13 | E5 | Como admin quiero agrupar albaranes validados en una factura | Media | 5 |
| US-14 | E5 | Como admin quiero exportar facturas en PDF | Baja | 3 |
| US-15 | E6 | Como admin quiero ver un dashboard con métricas de albaranes procesados | Baja | 5 |

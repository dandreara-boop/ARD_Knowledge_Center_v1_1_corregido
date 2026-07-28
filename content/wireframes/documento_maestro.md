# Wireframes

## Ficha estándar

Cada wireframe del Documento Maestro se registra con código, nombre, estado, versión, objetivo, descripción, flujo, reglas, decisiones relacionadas e imagen.

## WF-001 — Lista de Remitos de Entrada

| Campo | Valor |
|---|---|
| Código | WF-001 |
| Nombre | Lista de Remitos de Entrada |
| Estado | Preparado para documentación |
| Versión | Pendiente |
| Objetivo | Acceder y administrar remitos de entrada. |

### Descripción

Pantalla prevista dentro del flujo principal de recepción.

### Flujo

Recepción de Mercadería → Lista de Remitos de Entrada.

### Reglas

Debe permitir iniciar, consultar y continuar remitos.

### Decisiones relacionadas

DEC-032, DEC-038, DEC-039.

### Imagen

Pendiente de incorporación.

## WF-002 — Carga rápida de códigos existentes

| Campo | Valor |
|---|---|
| Código | WF-002 |
| Nombre | Carga rápida de códigos existentes |
| Estado | Preparado para documentación |
| Versión | Pendiente |
| Objetivo | Agregar productos existentes al remito sin abrir la ficha completa. |

### Descripción

Pantalla prevista dentro del flujo de recepción.

### Flujo

Código → Producto encontrado → Agregar al remito.

### Reglas

Prioriza productos existentes por código.

### Decisiones relacionadas

DEC-029, DEC-030, DEC-031.

### Imagen

Pendiente de incorporación.

## WF-003 — Creación o edición de productos

| Campo | Valor |
|---|---|
| Código | WF-003 |
| Nombre | Creación o edición de productos |
| Estado | Preparado para documentación |
| Versión | Pendiente |
| Objetivo | Crear producto cuando el código no existe. |

### Descripción

Pantalla prevista para asignar código y precio antes de agregar el producto al remito.

### Flujo

Código no encontrado → Crear producto → Asignar código y precio.

### Reglas

Producto y atributos permanecen separados.

### Decisiones relacionadas

DEC-022, DEC-028, DEC-032.

### Imagen

Pendiente de incorporación.

## WF-004 — Caja de Venta

{{include:modulos/venta_salon/wf004_caja}}

## WF-005 — Catálogo Visual de Artículos sin Código

{{include:modulos/venta_salon/wf005_catalogo_visual}}

## WF-006 — Carga de cantidades y atributos

| Campo | Valor |
|---|---|
| Código | WF-006 |
| Nombre | Carga de cantidades y atributos |
| Estado | Preparado para documentación |
| Versión | Pendiente |
| Objetivo | Registrar cantidades por combinación de atributos. |

### Descripción

Pantalla prevista para depósito dentro del flujo de recepción.

### Flujo

Producto → Atributos visibles → Conteo por combinación.

### Reglas

Depósito muestra solo atributos definidos por Administración.

### Decisiones relacionadas

DEC-033, DEC-036.

### Imagen

![Atributos dinámicos](/static/images/recepcion_atributos_dinamicos.png)

## WF-007 — Distribución entre locales y web

| Campo | Valor |
|---|---|
| Código | WF-007 |
| Nombre | Distribución entre locales y web |
| Estado | Preparado para documentación |
| Versión | Pendiente |
| Objetivo | Distribuir cantidades recibidas hacia destinos. |

### Descripción

Pantalla prevista para asignar cantidades a locales, depósito y stock web.

### Flujo

Cantidad recibida → Destino → Movimiento auditable.

### Reglas

La distribución usa cantidades, no porcentajes.

### Decisiones relacionadas

DEC-034, DEC-037, DEC-038.

### Imagen

![Flujo de recepción en cinco pantallas](/static/images/recepcion_flujo_5_pantallas.png)

## WF-008 — Arqueo y Cierre de Caja

{{include:modulos/venta_salon/wf008_arqueo_caja}}

## WF-009 — Cambios y Crédito Comercial

| Campo | Valor |
|---|---|
| Código | WF-009 |
| Nombre | Cambios y Crédito Comercial |
| Estado | Preparado para documentación |
| Versión | Pendiente |
| Objetivo | Registrar cambio y aplicar o emitir Crédito Comercial. |

### Descripción

Pantalla prevista para gestionar prendas recibidas para cambio, valor reconocido, crédito total, aplicación a venta nueva y comprobante.

### Flujo

Cambio → Valor reconocido → Crédito Comercial → Aplicación total, parcial o comprobante futuro.

### Reglas

No genera entrega de dinero. El Crédito Comercial puede tener QR o código de barras.

### Decisiones relacionadas

DEC-061 a DEC-077.

### Imagen

Pendiente de incorporación.

# Modelo de Datos

## Objetivo

Documentar entidades funcionales sin programar tablas físicas. Cada entidad se relaciona con el módulo correspondiente.

Estado actual: **Sprint 5 — Motor de Inventario finalizado y validado**.

{{include:general/modelo_conceptual}}

## Entidades por módulo

| Entidad | Módulo principal | Descripción funcional |
|---|---|---|
| Empresa | General | Organización propietaria de la operación. |
| Sucursal | General / Venta / Caja | Punto operativo con base local, caja y stock. |
| Destino de Inventario | Recepción / Venta / Logística / Web | Local, web, depósito u otro destino operativo de stock. |
| Producto | Recepción / Administración | Identidad comercial del artículo. |
| Atributo | Recepción / Administración | Característica configurable del producto. |
| Familia de atributos | Administración | Plantilla reutilizable de atributos para configurar artículos. |
| Valor de atributo | Recepción | Valor específico dentro de un atributo. |
| Curva | Recepción / Administración | Conjunto versionable de talles o valores. |
| Variante | Recepción / Venta | Presentación concreta del artículo resuelta cuando existe necesidad real. |
| Servicio Interno de Generación de Variantes | Recepción / Administración / API | Componente reutilizable que busca o crea variantes automáticamente. |
| Proveedor | Recepción / Administración | Origen comercial de mercadería. |
| Cliente | Venta / Cambios / Administración | Persona asociada a venta, crédito o historial. |
| Remito de Entrada | Recepción | Documento de ingreso de mercadería. |
| Ítem del remito | Recepción | Producto incluido dentro de un remito. |
| Conteo | Recepción | Cantidad recibida por combinación de atributos. |
| Asignación inicial | Recepción / Logística | Distribución de cantidad recibida hacia destinos. |
| Movimiento de stock | Recepción / Venta / Logística | Libro histórico auditable de toda variación de stock. |
| StockActual | Recepción / Venta / Logística / Web | Saldo materializado por variante, destino de inventario y estado. |
| Evento de dominio | Venta / Inventario / Sincronización | Punto de integración preparado para desacoplar procesos derivados sin bus completo todavía. |
| Venta | Venta | Operación comercial presencial. |
| Renglón de venta | Venta | Línea vendida con precio, descuento y valor reconocido. |
| Pago | Venta / Caja | Cobro por medio de pago. |
| Caja | Caja | Unidad operativa de cobro por sucursal. |
| Turno de caja | Caja | Apertura, operación, arqueo y cierre de un cajero. |
| Arqueo | Caja | Control de efectivo contado contra esperado. |
| Corrección de cobro | Caja | Cambio auditable de medio de pago. |
| Operación de cambio | Cambios | Registro funcional de prendas recibidas para cambio. |
| Renglón de cambio | Cambios | Prenda y valor reconocido dentro de una operación. |
| Crédito Comercial | Cambios | Saldo comercial generado por un cambio. |
| Campaña | Venta / Administración | Regla temporal de acción comercial. |
| Promoción | Venta / Administración | Regla que modifica precio sin crear productos ficticios. |
| Cola de sincronización | Venta / General | Operaciones locales pendientes de enviarse a la nube. |
| Usuario | Usuarios / Administración | Persona con acceso al sistema. |
| Permiso | Usuarios / Administración | Acción permitida por rol o usuario. |
| Excepción | Administración | Evento operativo que requiere revisión. |
| Evento de sincronización | Sincronización | Cambio local o central transmitido mediante protocolo idempotente. |
| Paquete de contingencia | Sincronización | Archivo excepcional para intercambio manual de actualizaciones o eventos pendientes. |

## Modelos específicos existentes

### Recepción

{{include:modulos/carga_productos/datos}}

### Venta

{{include:modulos/venta_salon/datos}}

### Cambios y Crédito Comercial

El modelo conceptual está integrado en el capítulo Cambios y Crédito Comercial.

### Caja

El modelo conceptual está integrado en WF-008 Arqueo y Cierre de Caja.

### Motor de Inventario

{{include:general/motor_inventario}}

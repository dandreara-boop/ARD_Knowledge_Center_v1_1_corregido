# Módulo 2 — Venta en Salón

## Estado

**Sprint 9.3 — Sesiones de Caja implementadas dentro de Operación de Caja y Flujo de Venta en Salón.**

Sprint 6, Sprint 7, Sprint 8 y Sprint 9.3 se mantienen como implementados y validados. Sprint 9.3 registra sesiones de caja, captura explícita para cobro y confirmación por cajero responsable.

Sprint 9.4 documenta decisiones previas a implementación para movimientos operativos de caja: `INGRESO`, `RETIRO` y `EGRESO/PAGO`. Cierre de caja, arqueo, correcciones, supervisión, frontend, contabilidad, cuenta corriente de proveedores y sincronización cloud siguen fuera de lo implementado.

## Objetivo

Registrar ventas presenciales con la menor fricción posible para el vendedor y sin depender de Internet.

## Principios

- Vendedor, cajero, dispositivo, caja y sesión de caja son conceptos separados; la sesión no pertenece a la PC/tablet.
- Una caja puede tener una sola sesión abierta y un cajero puede tener varias sesiones abiertas en cajas distintas.
- Si un cajero tiene varias sesiones abiertas, debe seleccionar explícitamente con cuál cobra.
- Los movimientos operativos de caja se asocian a una sesión abierta y al cajero responsable.
- En modo normal, caja puede crear y cobrar la venta.
- En modo alta demanda, vendedor prepara y envía a caja.
- No selecciona variantes manualmente.
- No recibe advertencias por stock negativo.
- No elige promociones.
- El sistema aplica la opción más conveniente para el cliente.
- La venta se guarda primero localmente.
- El historial se envía a la nube.
- La operación esencial del POS no depende de Internet.

## Componentes funcionales del módulo

- Venta.
- Renglones de venta.
- Motor comercial.
- Motor comercial de precios por Artículo.
- Resolución comercial y cobro del POS.
- Operación de caja y flujo de venta en salón.
- Caja.
- Pagos.
- Cambios.
- Stock local.
- Sincronización.
- Historial central.

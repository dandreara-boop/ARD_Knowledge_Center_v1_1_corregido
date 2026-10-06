# Módulo 2 — Venta en Salón

## Estado

**Sprint 9 — Operación de Caja y Flujo de Venta en Salón con diseño funcional cerrado y pendiente de implementación.**

Sprint 6, Sprint 7 y Sprint 8 se mantienen como implementados y validados. Sprint 9 documenta el flujo operativo de salón y caja, sin backend implementado todavía.

## Objetivo

Registrar ventas presenciales con la menor fricción posible para el vendedor y sin depender de Internet.

## Principios

- Vendedor, cajero, dispositivo, caja y sesión de caja son conceptos separados.
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

# Módulo Venta en Salón

## Objetivos

{{include:modulos/venta_salon/resumen}}

## Proceso completo

{{include:modulos/venta_salon/flujo}}

## Arquitectura local y nube

{{include:modulos/venta_salon/arquitectura}}

## Sprint 6 — Motor de Venta Local

Sprint 6 implementó y validó el núcleo transaccional de venta local: venta, detalles, pagos, outbox local, evento `VENTA_FINALIZADA` e integración posterior con inventario.

La finalización de venta guarda `Venta CERRADA` y `VENTA_FINALIZADA` en una misma transacción rápida. Inventario queda fuera del camino crítico del POS y se procesa luego reutilizando `InventoryService`.

Detalle completo: [Sprint 6 — Motor de Venta Local](/doc/modulos/venta_salon/sprint_6_motor_venta_local).

## Sprint 7 — Motor Comercial de Precios

Sprint 7 implementó y validó el motor comercial de precios a nivel de Artículo: condiciones comerciales, precios por artículo, recálculo derivado, preview de impacto, políticas para manuales y auditoría de cambios efectivos.

El precio comercial pertenece al Artículo, no a la Variante. Las ventas históricas conservan `precio_unitario` como snapshot y no se recalculan por cambios posteriores.

Detalle completo: [Sprint 7 — Motor Comercial de Precios](/doc/modulos/venta_salon/sprint_7_motor_comercial_precios).

## Búsqueda de artículos

La venta puede iniciarse por código, catálogo visual o ambos. El vendedor no selecciona variantes manualmente y el sistema prioriza velocidad operativa.

## Búsqueda manual

La búsqueda manual queda disponible desde la caja para artículos sin etiqueta, código ilegible o desconocido.

## Búsqueda gráfica de artículos sin etiqueta

{{include:modulos/venta_salon/wf005_catalogo_visual}}

## Escáner

El campo principal de caja recibe códigos de barras y conserva el foco operativo después de cada carga.

## Ventas abiertas

La caja puede mantener varios remitos de venta abiertos o suspendidos simultáneamente. Una venta suspendida conserva artículos, cliente, promociones preliminares y última actividad.

## Remitos de venta

El número de remito de venta permanece visible y de solo lectura en la pantalla de caja.

## Promociones

{{include:modulos/venta_salon/promociones}}

## Precios contado

Los precios de contado dependen de la condición comercial configurada para los medios de pago utilizados.

Sprint 7 implementa condiciones comerciales de precio por artículo. No implementa todavía el motor completo de medios de pago ni pagos mixtos.

## Precios financiados

Cuando una unidad o grupo promocional combina contado y financiado, pierde el beneficio de contado y se registra como financiado según política comercial.

## Pagos mixtos

{{include:modulos/venta_salon/pagos_mixtos}}

## Caja

{{include:modulos/venta_salon/wf004_caja}}

## Flujo completo

El flujo funcional completo integra escaneo, carga o búsqueda de artículos, cálculo automático de promociones, carga de medios de pago, confirmación local, comprobante y sincronización con la nube. Sprint 7 sólo concreta el backend de precios por artículo y condiciones comerciales de precio.

## Wireframes

- WF-004 — Caja de Venta.
- WF-005 — Catálogo Visual de Artículos sin Código.
- WF-008 — Arqueo y Cierre de Caja.

## Modelo de datos

{{include:modulos/venta_salon/datos}}

## Reglas de negocio

- El cajero no elige promociones.
- La venta se guarda primero localmente.
- El historial se envía a la nube.
- Cada artículo conserva precio de lista, precio aplicado, promoción, explicación y valor reconocido para cambio.
- La falta de Internet no impide vender.

## Casos especiales

- Venta con stock negativo: se registra localmente y la nube genera excepción administrativa.
- Artículo sin etiqueta: se carga desde catálogo visual o búsqueda manual.
- Pago mixto: el motor optimiza la combinación permitida como definición funcional prevista; Sprint 7 no implementa el optimizador de pagos mixtos.
- Venta suspendida: conserva toda la información cargada.

## Decisiones

{{include:modulos/venta_salon/decisiones}}

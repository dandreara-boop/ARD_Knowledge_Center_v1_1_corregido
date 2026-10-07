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

## Sprint 8 — Resolución Comercial y Cobro del POS

Sprint 8 se encuentra implementado, con solver HiGHS integrado, migración aplicada y QA automático y manual aprobado.

El diseño conecta el Motor de Venta Local, el Motor Comercial de Precios, medios de pago y resolución de pagos simples o mixtos. El backend deberá permitir cotización reversible, múltiples medios, cero o un `RESTO`, resolución de menor costo final para el cliente, redondeo final por medio, traza estructurada, snapshot histórico y confirmación local atómica.

HiGHS mediante `highspy` fue seleccionado como solver técnico preliminar. La implementación deberá encapsularlo detrás del optimizador comercial y validar la solución con `Decimal` antes de confirmar.

El frontend POS definitivo, caja completa, promociones, bancos, cuotas y sincronización cloud quedan fuera del Sprint 8.

Detalle completo: [Sprint 8 — Resolución Comercial y Cobro del POS](/doc/modulos/venta_salon/sprint_8_resolucion_comercial_cobro_pos).

## Sprint 9 — Operación de Caja y Flujo de Venta en Salón

SPRINT 9.3 IMPLEMENTADO.

Sprint 9 define la operación cotidiana del salón y de las cajas: separa dispositivo, vendedor, cajero, caja y sesión de caja; habilita modo normal y modo alta demanda; formaliza venta preparada, captura por caja, verificación de mercadería, apertura manual de sesión, arqueo ciego, pendientes de supervisión y correcciones administrativas auditables.

Sprint 9.3 implementa la sesión de caja independiente del dispositivo, responsable único, una sesión abierta por caja, varias sesiones abiertas por cajero en cajas distintas, advertencia no bloqueante, selección explícita de sesión, captura `EN_COBRO` ligada a `caja_captura_id` y `sesion_caja_id`, y confirmación por cajero responsable.

Sprint 9.4 implementa movimientos operativos de caja: `INGRESO`, `RETIRO` y `EGRESO`, asociados a sesión abierta, cajero responsable, trazabilidad e impacto sobre efectivo esperado.

Sprint 9.5 documenta decisiones previas a implementación para efectivo físico, cierre y alcance del arqueo: `EFECTIVO` como único medio que mueve dinero físico, pagos mixtos con impacto parcial en caja, conteo exclusivo del cajón, retiros fuera del conteo y verificación posterior sin reescribir el primer conteo.

Detalle completo: [Sprint 9 — Operación de Caja y Flujo de Venta en Salón](/doc/modulos/venta_salon/sprint_9_operacion_caja_flujo_venta_salon).

## Búsqueda de artículos

La venta puede iniciarse por código, catálogo visual o ambos. El vendedor no selecciona variantes manualmente y el sistema prioriza velocidad operativa.

## Búsqueda manual

La búsqueda manual queda disponible desde la caja para artículos sin etiqueta, código ilegible o desconocido.

## Búsqueda gráfica de artículos sin etiqueta

{{include:modulos/venta_salon/wf005_catalogo_visual}}

## Escáner

El campo principal de caja recibe códigos de barras y conserva el foco operativo después de cada carga.

## Ventas abiertas

La operación admite ventas abiertas o suspendidas cuando corresponda y, desde Sprint 9, ventas preparadas para caja durante alta demanda.

Estados operativos definidos para el flujo de venta preparada:

```text
ABIERTA
→ LISTA_PARA_COBRAR
→ EN_COBRO
→ CERRADA
```

Una venta `EN_COBRO` puede liberarse y volver a `LISTA_PARA_COBRAR`. Se mantiene `ANULADA` para operaciones que no continuarán.

## Remitos de venta

El número de remito de venta permanece visible y de solo lectura en la pantalla de caja.

## Promociones

{{include:modulos/venta_salon/promociones}}

## Precios contado

Los precios de contado dependen de la condición comercial configurada para los medios de pago utilizados.

Sprint 7 implementa condiciones comerciales de precio por artículo. No implementa todavía el motor completo de medios de pago ni pagos mixtos.

Sprint 8 define el diseño backend para asociar medios de pago configurables a condiciones comerciales, sin hardcodear relaciones como Visa = `PRECIO_2`.

## Precios financiados

Cuando una unidad o grupo promocional combina contado y financiado, pierde el beneficio de contado y se registra como financiado según política comercial.

## Pagos mixtos

{{include:modulos/venta_salon/pagos_mixtos}}

## Caja

{{include:modulos/venta_salon/wf004_caja}}

## Flujo completo

El flujo funcional completo integra escaneo, carga o búsqueda de artículos, cálculo automático de promociones, carga de medios de pago, confirmación local, comprobante y sincronización con la nube.

Sprint 7 concreta el backend de precios por artículo y condiciones comerciales de precio.

Sprint 8 define la resolución comercial y cobro, pero no implementa todavía frontend POS definitivo ni sincronización cloud nueva.

Sprint 9 agrega el contexto operativo de salón y caja. Sprint 9.3 deja implementadas las reglas backend de sesión, captura y confirmación. Sprint 9.4 deja implementados movimientos operativos de caja. Sprint 9.5 documenta cierre y arqueo como decisiones previas a implementación; cierre de caja, arqueo, correcciones, supervisión, frontend y sincronización cloud siguen pendientes.

## Wireframes

- WF-004 — Caja de Venta.
- WF-005 — Catálogo Visual de Artículos sin Código.
- WF-008 — Arqueo y Cierre de Caja.

## Modelo de datos

{{include:modulos/venta_salon/datos}}

## Reglas de negocio

- El cajero no elige promociones.
- Cajero y vendedor son responsabilidades separadas; no se asume que el usuario que cobra sea el vendedor.
- AUTOSERVICIO se registra con `vendedor_id = null`.
- Para cobrar no alcanza con tener permiso: debe existir una sesión de caja abierta, válida y seleccionada explícitamente.
- Una sesión pertenece a una caja concreta, a un único cajero responsable y no se traslada entre cajas ni entre dispositivos.
- Una caja puede tener una sola sesión abierta; un cajero puede tener varias sesiones abiertas en cajas distintas.
- Una venta `EN_COBRO` conserva `caja_captura_id` y `sesion_caja_id`, y sólo puede confirmarla el cajero responsable de esa sesión.
- `INGRESO`, `RETIRO` y `EGRESO/PAGO` sólo pueden registrarse sobre una sesión abierta y por el cajero responsable.
- La selección automática de la única sesión abierta es una simplificación de UI sólo para movimientos de caja; no modifica la regla de sesión explícita del cobro.
- En arqueo, el cajero cuenta sólo el efectivo físico restante en su cajón; los retiros no se recuperan para ese conteo.
- En pagos mixtos, sólo la porción `EFECTIVO` modifica el efectivo físico esperado.
- El efectivo inicial de cada sesión se declara manualmente y no se hereda automáticamente del cierre anterior.
- Venta `CERRADA` permanece inmutable; los errores posteriores se resuelven con registros separados auditables o anulación y nueva venta cuando corresponda.
- La venta se guarda primero localmente.
- El historial se envía a la nube.
- Cada artículo conserva precio de lista, precio aplicado, promoción, explicación y valor reconocido para cambio.
- La falta de Internet no impide vender.

## Casos especiales

- Venta con stock negativo: se registra localmente y la nube genera excepción administrativa.
- Artículo sin etiqueta: se carga desde catálogo visual o búsqueda manual.
- Pago mixto: Sprint 8 implementa la resolución por menor total final, múltiples medios, cero o un `RESTO`, redondeo final por medio, solver HiGHS encapsulado y traza explicable. Implementación y QA aprobados.
- Venta suspendida: conserva toda la información cargada.

## Decisiones

{{include:modulos/venta_salon/decisiones}}

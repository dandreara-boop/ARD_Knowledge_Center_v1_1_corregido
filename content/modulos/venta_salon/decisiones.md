# Decisiones — Venta en Salón y Caja

| Código | Decisión |
|---|---|
| DEC-014 | Las promociones no generan productos nuevos. |
| DEC-015 | Se aplica la promoción más conveniente para el cliente. |
| DEC-017 | Toda decisión automática debe ser explicable y auditable. |
| DEC-018 | Cada unidad conserva el precio aplicado y el valor reconocido para cambios. |
| DEC-020 | La política de cambios es global y no la decide el cajero. |
| DEC-041 | Cada sucursal tiene una base local independiente. |
| DEC-042 | La venta presencial se registra primero localmente. |
| DEC-043 | La sincronización utiliza identificadores globales para evitar duplicados. |
| DEC-044 | La nube conserva el historial consolidado. |
| DEC-045 | Cada tipo de información tiene una autoridad definida. |
| DEC-046 | La falta de Internet no impide vender. |
| DEC-047 | La forma de pago participa en el cálculo comercial. |
| DEC-048 | Medio de pago y condición comercial son conceptos separados. |
| DEC-049 | Las cobranzas se administran separadamente por medio de pago. |
| DEC-050 | La venta se recalcula al modificar los importes antes de confirmarse. |
| DEC-051 | El tratamiento del pago mixto se define mediante políticas globales. |
| DEC-052 | El motor optimiza el pago mixto para obtener el mejor resultado permitido. |
| DEC-053 | Los pagos mixtos admiten límites disponibles o carga progresiva de importes. |
| DEC-054 | La empresa configura qué medios se consideran contado. |
| DEC-055 | Se priorizan unidades completas y grupos promocionales completos. |
| DEC-056 | El cálculo comercial se actualiza continuamente. |
| DEC-057 | Una unidad o grupo que combine contado y financiado pierde el beneficio de contado. |
| DEC-058 | Existirá un catálogo visual configurable para artículos sin etiqueta individual. |
| DEC-059 | Un producto puede venderse por código, catálogo visual o ambos. |
| DEC-060 | La pantalla de caja muestra solo la información imprescindible para trabajar con rapidez. |
| DAT-SALE-001 | La venta local se materializa antes de ejecutar trabajos derivados. |
| DAT-SALE-002 | Venta cerrada y evento pendiente se guardan atómicamente. |
| DAT-SALE-003 | Inventario queda fuera del camino crítico del POS. |
| DAT-SALE-004 | Los detalles conservan snapshot comercial histórico. |
| DAT-SALE-005 | El outbox local persistente representa obligaciones derivadas. |
| DAT-SALE-006 | El procesamiento de eventos es reintentable. |
| DAT-SALE-007 | Los efectos derivados de venta son idempotentes. |
| DAT-SALE-008 | Los movimientos derivados de venta usan UUID5 determinístico compatible con `String(36)`. |
| DAT-SALE-009 | Los eventos con error no se pierden. |
| DAT-SALE-010 | Los eventos procesados no vuelven a aplicar inventario. |
| DAT-SALE-011 | El stock negativo no bloquea la venta local. |
| DAT-PRICE-001 | El precio comercial pertenece al Artículo, no a la Variante. |
| DAT-PRICE-002 | Las reglas pertenecen a condiciones comerciales y no a cada artículo. |
| DAT-PRICE-003 | El motor usa reglas Python tipadas y controladas, sin fórmulas libres. |
| DAT-PRICE-004 | Los cálculos monetarios utilizan Decimal. |
| DAT-PRICE-005 | Cambiar el precio BASE de un artículo recalcula derivados activos en forma atómica. |
| DAT-PRICE-006 | El cambio general de una regla requiere preview y aplicación explícita. |
| DAT-PRICE-007 | El preview no persiste cambios en PrecioArticulo. |
| DAT-PRICE-008 | La política frente a precios manuales se define explícitamente al aplicar recálculo masivo. |
| DAT-PRICE-009 | La auditoría de precios se genera sólo ante cambios efectivos de precio u origen. |
| DAT-PRICE-010 | Las ventas históricas conservan snapshot de precio y no se recalculan por cambios actuales. |
| DAT-PRICE-011 | La condición BASE activa única se valida en servicio por compatibilidad con MariaDB. |
| DAT-POS-001 | MedioPago y CondicionComercialPrecio son conceptos separados. |
| DAT-POS-002 | Toda venta nueva inicia valorizada con la condición comercial BASE. |
| DAT-POS-003 | La consulta o simulación comercial no persiste snapshot ni pagos definitivos. |
| DAT-POS-004 | El futuro POS podrá usar una condición o medio de visualización reversible durante la carga. |
| DAT-POS-005 | Una distribución de pagos admite múltiples medios y cero o un RESTO. |
| DAT-POS-006 | El mismo algoritmo debe resolver pagos simples, mixtos y N medios. |
| DAT-POS-007 | La resolución debe minimizar el costo final para el cliente respetando los importes solicitados. |
| DAT-POS-008 | La unidad física se prioriza antes del fraccionamiento monetario. |
| DAT-POS-009 | La conversión proporcional entre condiciones es simétrica y usa Decimal. |
| DAT-POS-010 | El redondeo monetario de cobro se aplica sólo al importe final calculado por medio y sube al siguiente múltiplo configurable de 0,05. |
| DAT-POS-011 | La resolución debe generar una traza estructurada explicable. |
| DAT-POS-012 | La venta confirmada conserva snapshot histórico completo de la resolución. |
| DAT-POS-013 | Una venta CERRADA es inmutable. |
| DAT-POS-014 | Un error posterior al cierre se corrige mediante anulación explícita y nueva venta. |
| DAT-POS-015 | Confirmar cobro es una operación local y atómica. |
| DAT-POS-016 | El motor comercial no mueve stock y conserva el mecanismo de inventario existente. |
| DAT-POS-017 | Los fragmentos internos no se redondean individualmente; se conserva precisión suficiente hasta el subtotal por medio. |
| DAT-POS-018 | Los importes fijos ingresados por cliente o cajero se respetan sin alterarlos por redondeo. |
| DAT-POS-019 | La resolución monetaria se modela como LP y, al minimizar unidades fraccionadas, como MILP. |
| DAT-POS-020 | HiGHS mediante highspy es el solver técnico elegido para la implementación definitiva. |
| DAT-POS-021 | highspy debe quedar encapsulado detrás de CommercialOptimizer; dominio, routers y endpoints no dependen directamente del solver. |
| DAT-POS-022 | La solución del solver debe reconstruirse y validarse con Decimal antes de permitir la confirmación. |
| DAT-POS-023 | El orden de medios del request no tiene prioridad comercial; los desempates usan criterio canónico interno. |
| DAT-POS-024 | El optimizador usa precios efectivos de PrecioArticulo y no reconstruye reglas del Sprint 7. |
| DAT-POS-025 | No se aprueban límites arbitrarios de ticket sin medición y documentación previas. |
| DAT-POS-026 | La implementación productiva debe compararse contra un oráculo independiente en escenarios pequeños. |
| DAT-POS-027 | ARD debe soportar Windows y Linux; la integración Linux de Sprint 8 queda pendiente de validación automatizada. |
| DAT-POS-028 | highspy queda pendiente de incorporación formal, pin de versión y validación CI durante implementación. |

## Cambios y créditos comerciales

- DEC-061 a DEC-077: valor reconocido, cambios múltiples, ventas abiertas y Crédito Comercial.

## Arqueo y cierre de caja

- DEC-078 a DEC-087: arqueo ciego, revisión guiada, tolerancia, cierre con diferencia y movimientos explícitos de efectivo.

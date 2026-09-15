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

## Cambios y créditos comerciales

- DEC-061 a DEC-077: valor reconocido, cambios múltiples, ventas abiertas y Crédito Comercial.

## Arqueo y cierre de caja

- DEC-078 a DEC-087: arqueo ciego, revisión guiada, tolerancia, cierre con diferencia y movimientos explícitos de efectivo.

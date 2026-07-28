# Módulo Anulación

## Concepto funcional

Una anulación no es un cambio. No genera Crédito Comercial y no representa una entrega de dinero. Su objetivo es revertir completamente una operación, manteniendo auditoría.

## Diferencia con cambio

| Operación | Resultado |
|---|---|
| Cambio | Genera Crédito Comercial según política. |
| Anulación | Revierte la operación original. |

## Stock

La anulación debe revertir los movimientos de stock generados por la operación original.

## Caja

La anulación debe ajustar la caja o dejar el movimiento compensatorio correspondiente, sin borrar el historial.

## Medios de pago

Cada medio de pago utilizado debe quedar revertido o compensado de acuerdo con su naturaleza operativa.

## Promociones

Las promociones aplicadas en la venta anulada quedan documentadas en la auditoría de la anulación. No se recalculan como una venta nueva.

## Créditos utilizados

Si la operación anulada utilizó Crédito Comercial, el sistema debe restituir o dejar trazado el saldo afectado según reglas configurables.

## Movimientos

Toda anulación genera movimientos auditables. No se eliminan ventas, pagos ni renglones originales.

## Auditoría

La anulación conserva usuario, fecha, hora, motivo, operación original, importes, medios afectados, stock revertido y observaciones.

## Casos especiales

- Anulación parcial no definida en esta etapa.
- Anulación desde arqueo se documenta dentro del módulo Caja.
- Anulación de operación sincronizada requiere trazabilidad local y central.

# Pagos mixtos

## Estado implementado

Sprint 7 no implementa el optimizador de pagos mixtos ni prorrateo de pagos.

Esta página conserva la definición funcional prevista para venta y caja.

## Objetivo

Permitir que el cliente utilice varios medios de pago y que el sistema encuentre la mejor combinación comercial permitida.

## Formas de carga

1. Informar el máximo disponible en uno o más medios.
2. Agregar importes progresivamente hasta completar la venta.
3. Usar la flecha para asignar todo el saldo pendiente a un medio.

## Regla de unidad completa

El beneficio de contado se aplica solo cuando una unidad completa o un grupo promocional completo queda cubierto por medios configurados como contado.

Ejemplo:

```text
Prenda contado:    $40.000
Prenda financiada: $45.000
Pago: $20.000 efectivo + $25.000 crédito
Resultado: precio financiado de $45.000
```

El efectivo sigue registrado como medio de cobro, pero no genera un descuento parcial de contado.

## Optimización

Con varios productos, el motor puede asignar unidades completas al contado y otras al financiado para obtener el menor total permitido.

## Historial

Se conserva:

- medios e importes;
- condición asignada a cada unidad o grupo;
- promociones evaluadas;
- combinación elegida;
- ahorro;
- explicación del cálculo.

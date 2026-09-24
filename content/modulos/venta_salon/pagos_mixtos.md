# Pagos mixtos

## Estado implementado

Sprint 7 no implementa el optimizador de pagos mixtos ni prorrateo de pagos.

Esta página conserva la definición funcional prevista para venta y caja.

Sprint 8 define comercialmente la resolución de pagos simples y mixtos, selecciona HiGHS como solver técnico y queda pendiente de implementación definitiva y QA.

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

Con varios productos, el motor deberá asignar unidades completas y fracciones monetarias cuando sea necesario para obtener el menor costo final para el cliente, respetando los importes solicitados.

La resolución deberá aceptar N medios, cero o un `RESTO`, importes fijos desde cualquier condición y conversión proporcional con `Decimal`.

El redondeo comercial de pagos mixtos se aplica sólo al importe final calculado por cada medio, hacia arriba a múltiplos de `0,05`. Los fragmentos internos no se redondean individualmente y los importes fijos cargados por el cliente o cajero se respetan sin alterarlos.

La implementación definitiva deberá encapsular HiGHS detrás del optimizador comercial y validar la solución reconstruida con `Decimal` antes de confirmar una venta.

Detalle aprobado: [Sprint 8 — Resolución Comercial y Cobro del POS](/doc/modulos/venta_salon/sprint_8_resolucion_comercial_cobro_pos).

## Historial

Se conserva:

- medios e importes;
- condición asignada a cada unidad o grupo;
- promociones evaluadas;
- combinación elegida;
- ahorro;
- explicación del cálculo.

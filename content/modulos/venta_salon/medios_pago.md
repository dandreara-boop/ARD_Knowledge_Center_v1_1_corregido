# Medios de pago y condiciones comerciales

## Estado implementado

Sprint 7 implementa condiciones comerciales de precio por Artículo.

No implementa bancos, tarjetas, cuotas, caja ni el motor completo de medios de pago.

Sprint 8 implementa la configuración backend de medios de pago y su asociación a condiciones comerciales.

## Separación conceptual

Un **medio de pago** indica cómo se recibe el dinero. Una **condición comercial** determina qué precios y promociones se aplican.

| Medio posible | Condición posible |
|---|---|
| Efectivo | Contado |
| Transferencia | Contado, según configuración |
| Tarjeta de débito | Configurable |
| Tarjeta de crédito | Financiado |
| Mercado Pago | Configurable |
| Cuenta corriente | Cuenta corriente |

La clasificación es global y no la decide el cajero.

Sprint 8 mantiene como decisión vigente que `MedioPago` y `CondicionComercialPrecio` son conceptos distintos.

Sprint 9.5 agrega una regla funcional para caja: el único `MedioPago` que mueve efectivo físico dentro del cajón es `EFECTIVO`.

Los demás medios pueden representar cobros pero no modifican el efectivo físico esperado: tarjetas, transferencias, QR y otros medios electrónicos forman parte de la información de la sesión, no del dinero físico contado en el cajón.

Esta condición no debe resolverse comparando el texto visible o nombre del medio de pago. El modelo deberá contar con una identificación explícita y estable que permita reconocer al único medio que representa efectivo físico. La implementación concreta se revisará contra el modelo actual antes de programar.

Ejemplo:

```text
EFECTIVO       -> PRECIO_1
TRANSFERENCIA  -> PRECIO_1
VISA           -> PRECIO_2
MASTERCARD     -> PRECIO_2
QR             -> PRECIO_2
```

Varios medios pueden compartir una misma condición comercial y la relación debe ser configurable.

No se debe hardcodear que un medio específico usa siempre una condición determinada.

La identificación de `EFECTIVO` como medio que mueve dinero físico es una regla distinta de la condición comercial de precio. Un medio electrónico puede compartir una condición comercial de contado y aun así no sumar efectivo al cajón.

En pagos mixtos, sólo la porción cobrada mediante `EFECTIVO` incrementa el efectivo físico esperado. Ejemplo: si una venta de `$30.000` se cobra con `$10.000` en `EFECTIVO` y `$20.000` en `VISA`, el impacto sobre efectivo físico es `+10.000`.

## Formulario de cobro

Cada medio tiene:

- nombre;
- casillero de importe;
- flecha para completar el saldo pendiente.

El sistema recalcula automáticamente después de cada modificación.

## Administración separada

Los cobros se registran por medio para permitir:

- caja de efectivo;
- conciliación de transferencias;
- liquidaciones de tarjetas;
- Mercado Pago;
- cuenta corriente;
- cierres y reportes separados.

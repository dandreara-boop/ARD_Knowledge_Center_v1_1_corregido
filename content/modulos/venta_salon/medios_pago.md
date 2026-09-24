# Medios de pago y condiciones comerciales

## Estado implementado

Sprint 7 implementa condiciones comerciales de precio por Artículo.

No implementa bancos, tarjetas, cuotas, caja ni el motor completo de medios de pago.

Sprint 8 aprueba el diseño funcional backend para configurar medios de pago y asociarlos a condiciones comerciales. Queda pendiente de implementación.

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

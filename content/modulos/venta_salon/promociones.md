# Promociones y precios en la venta

## Estado implementado

Sprint 7 implementa el motor comercial de precios por Artículo y condiciones comerciales de precio.

Las promociones descriptas en esta página siguen siendo alcance funcional de venta. No quedan documentadas como implementadas por Sprint 7.

## Principios

- La forma de pago participa en el cálculo comercial.
- Los precios de contado y financiado pueden ser distintos.
- Las promociones también pueden depender de la condición comercial.
- El cajero no elige manualmente la promoción.
- Si existen varias promociones compatibles, se aplica la más conveniente para el cliente.
- Las promociones no crean productos ficticios.

## Ejemplo

```text
Escanear remera A
Escanear remera B
        ↓
El motor detecta una promoción de 2 unidades
        ↓
Al conocer los medios de pago calcula la versión aplicable
        ↓
Registra el precio aplicado por unidad y la explicación
```

## Cambios

Cada unidad conserva el valor realmente reconocido para un cambio, aun cuando haya formado parte de una promoción.

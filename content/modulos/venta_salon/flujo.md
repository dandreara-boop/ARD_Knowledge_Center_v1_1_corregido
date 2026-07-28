# Flujo operativo — Venta en Salón

## Flujo preliminar

```text
Escanear producto
        ↓
Agregar a la venta
        ↓
Detectar promociones
        ↓
Aplicar la más conveniente
        ↓
Registrar medios de pago
        ↓
Confirmar localmente
        ↓
Emitir comprobante
        ↓
Sincronizar con la nube
```

## Promociones

No se crean artículos ficticios.

Ejemplo:

```text
Escanear remera A
Escanear remera B
        ↓
El sistema detecta 2 remeras
        ↓
Aplica automáticamente la promoción
```

## Historial

Cada artículo conserva:

- Precio de lista.
- Precio aplicado.
- Promoción.
- Explicación.
- Valor reconocido para cambios.

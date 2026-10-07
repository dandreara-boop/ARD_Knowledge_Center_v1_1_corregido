# Flujo operativo — Venta en Salón

## Modo normal — Caja crea y cobra

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

En este modo el cajero puede crear la venta, cargar o escanear artículos y cobrar, siempre que tenga permisos y una sesión de caja abierta y válida.

El cajero que cobra no queda automáticamente registrado como vendedor. Cuando no existió atención atribuible a un vendedor, la venta se registra como `AUTOSERVICIO` con `vendedor_id = null`.

## Modo alta demanda — Vendedor prepara y caja cobra

```text
ABIERTA
        ↓
LISTA_PARA_COBRAR
        ↓
EN_COBRO
        ↓
CERRADA
```

El vendedor puede preparar una venta sin sesión de caja. La venta conserva `global_id`, `numero_corto`, `referencia_cliente`, vendedor, local y estado.

Una venta `LISTA_PARA_COBRAR` queda disponible para cajas del mismo local. Una sola caja puede capturarla; al capturarla pasa a `EN_COBRO`.

La captura se realiza con una sesión de caja explícita. La venta `EN_COBRO` queda ligada a `caja_captura_id` y `sesion_caja_id`; la caja se obtiene de la sesión.

Si la venta debe volver al vendedor, primero se libera desde `EN_COBRO` a `LISTA_PARA_COBRAR`. La liberación se audita y no equivale a anulación.

Una venta anulada permanece en historial y no reutiliza su número corto.

Para confirmar `EN_COBRO -> CERRADA`, el cajero debe ser el responsable de la sesión abierta asociada a la venta.

## Verificación de mercadería

La caja puede operar con:

- `SIN_VERIFICACION`.
- `VERIFICACION_VISUAL`.
- `VERIFICACION_POR_ESCANEO`.

Las diferencias detectadas pueden corregirse antes del cobro. No se pide motivo por cada corrección durante la verificación; el sistema registra automáticamente usuario, fecha/hora, valor anterior y valor nuevo.

Una diferencia no implica automáticamente error del vendedor.

## Cierre y pendientes

Durante el cierre el cajero puede revisar operaciones de su sesión y marcar posibles errores de medio de pago. La venta cerrada no se edita silenciosamente; el caso queda como pendiente de supervisión.

Las solicitudes de corrección de arqueo y los posibles errores de pago no bloquean la apertura de la siguiente sesión.

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

Además, Sprint 9 requiere auditoría de creación, envío a caja, captura, liberación, modificaciones, cobro, anulación, verificación, cierre y pendientes de supervisión.

# Arquitectura local y nube — Venta en Salón

## Flujo de persistencia

```text
Escaneo
  ↓
Venta local cerrada
  ↓
Evento pendiente VENTA_FINALIZADA
  ↓
Comprobante
  ↓
Procesamiento posterior
  ↓
Stock local actualizado
  ↓
Sincronización futura
  ↓
Base central
  ↓
Historial consolidado
```

Sprint 6 implementa el cierre local y el outbox `VENTA_FINALIZADA`. El procesamiento explícito de eventos pendientes actualiza inventario después del `COMMIT`.

La sincronización cloud, el worker definitivo y la publicación automática a Base Central no forman parte del alcance implementado en Sprint 6.

## Identificador global

Toda venta tendrá un identificador único para evitar duplicaciones en los reintentos.

## Eventos pendientes

Sprint 6 utiliza `EventoPendiente` como outbox local.

Estados implementados:

- `PENDIENTE`.
- `PROCESANDO`.
- `PROCESADO`.
- `ERROR`.

## Venta con stock negativo

Se registra localmente y no bloquea al vendedor.

El procesamiento posterior de inventario mantiene la consistencia mediante movimientos idempotentes.

El vendedor continúa trabajando sin advertencias.

# Sprint 6 — Motor de Venta Local

## Estado

Sprint 6 implementado y validado funcionalmente.

El Sprint 6 construyó el núcleo transaccional de venta local y conectó:

```text
Catálogo
  ↓
Variante
  ↓
Venta
  ↓
Evento pendiente
  ↓
Inventario
```

La venta debe materializarse rápidamente. El procesamiento derivado no debe ralentizar el POS.

## Alcance implementado

Sprint 6 documenta como existentes:

- `Venta`.
- `DetalleVenta`.
- `PagoVenta`.
- `EventoPendiente` como outbox local.
- Endpoint de finalización local.
- Evento `VENTA_FINALIZADA`.
- Procesamiento explícito de eventos pendientes.
- Integración posterior con `InventoryService`.
- Idempotencia de movimientos derivados mediante UUID5 determinístico.

No se documentan como implementados en este sprint:

- Frontend POS.
- Promociones.
- Motor completo de precios.
- Clientes.
- Cambios.
- Devoluciones.
- Anulación completa.
- Caja.
- Arqueo.
- Cierre de turno.
- Sincronización cloud.
- Worker definitivo.
- Redis.
- RabbitMQ.
- Kafka.
- Facturación fiscal.

## Modelo de venta

Estados preparados de `Venta`:

- `ABIERTA`.
- `SUSPENDIDA`.
- `EN_PAGO`.
- `CERRADA`.
- `ANULADA`.

Sprint 6 no implementa todavía toda la funcionalidad operativa de suspensión, anulación, caja, promociones ni procesos relacionados. Los estados quedan preparados para evolución posterior.

`DetalleVenta` conserva snapshot comercial:

- Variante.
- Código de artículo.
- Código de barras.
- Descripción.
- Cantidad.
- Precio unitario.
- Importe.

Una venta histórica no depende de cambios posteriores en catálogo.

`PagoVenta` registra los pagos asociados a la venta. Sprint 6 valida que el pago sea suficiente para permitir la finalización, sin documentar todavía el módulo completo de caja.

## Flujo de finalización

Endpoint implementado:

```text
POST /api/ventas/{venta_id}/finalizar
```

La operación realiza conceptualmente:

```text
BEGIN

validar venta
validar líneas
validar pagos
recalcular/verificar total
marcar Venta CERRADA
crear VENTA_FINALIZADA en outbox

COMMIT
```

`Venta CERRADA` y `VENTA_FINALIZADA` se guardan en la misma transacción.

Después del `COMMIT`, el POS puede considerar terminada la operación crítica.

Inventario no se procesa dentro de ese cierre.

## Prioridad operativa

La facturación y la venta al cliente tienen prioridad sobre trabajos derivados.

No deben estar en el camino crítico del cajero:

- Sincronización cloud.
- Estadísticas.
- Procesamiento pesado.
- Reconstrucción de inventario.
- Servicios externos.

Internet no es necesario para cerrar una venta local.

## Outbox local

Evento documentado:

```text
VENTA_FINALIZADA
```

Estados de `EventoPendiente`:

- `PENDIENTE`.
- `PROCESANDO`.
- `PROCESADO`.
- `ERROR`.

Datos relevantes:

- `global_id`.
- `tipo`.
- `payload`.
- `estado`.
- `intentos`.
- `created_at`.
- `processed_at`.
- `ultimo_error`.

Payload mínimo de `VENTA_FINALIZADA`:

- `venta_id`.
- `venta_global_id`.
- `destino_id`.

El evento constituye la obligación persistente de ejecutar los efectos derivados de la venta.

## Procesamiento de inventario

`VENTA_FINALIZADA` se procesa posteriormente.

Por cada `DetalleVenta`, el procesador:

- Reutiliza `InventoryService`.
- Genera un `MovimientoStock` tipo `VENTA`.
- Registra cantidad negativa.
- Usa el destino de la venta.
- Usa estado `DISPONIBLE`.
- Usa `origen_tipo` igual a `VENTA`.

No se duplica lógica de inventario.

Stock negativo sigue permitido y no bloquea la venta local.

El procesamiento explícito mediante endpoint es la solución actual de Sprint 6. No constituye todavía un worker definitivo.

## Idempotencia validada

La solución final validada usa UUID5 determinístico para los movimientos de stock derivados de venta.

Inicialmente Sprint 6 utilizó este valor conceptual como `global_id` del `MovimientoStock`:

```text
sale:{venta_global_id}:line:{detalle_id}
```

Durante una prueba manual se detectó que esa cadena tenía 48 caracteres para el caso real probado.

`movimientos_stock.global_id` está definido como:

```text
String(36)
unique
index
```

MariaDB produjo:

```text
DataError 1406
Data too long for column 'global_id'
```

La solución final no fue ampliar la columna.

Se implementó UUID5 determinístico. La fuente conceptual:

```text
sale:{venta_global_id}:line:{detalle_id}
```

se transforma mediante UUID5 utilizando namespace fijo:

```text
8a248879-2d85-4e15-98f1-c769b5ed77cb
```

El resultado es un UUID determinístico de 36 caracteres.

Propiedades:

- Misma venta y misma línea generan el mismo UUID.
- Una línea diferente genera un UUID diferente.
- El valor mantiene compatibilidad con `global_id String(36)`.
- La idempotencia se conserva ante reintentos.

No se usa UUID4 para este caso porque rompería la idempotencia.

## Recuperación ante error

Prueba real documentada:

Situación inicial:

- Venta 1: `CERRADA`.
- Evento: `VENTA_FINALIZADA` en estado `PENDIENTE`.
- Stock variante 2 / destino 1 / `DISPONIBLE`: `-2`.

Primer procesamiento:

- MariaDB rechazó `global_id` por longitud.
- El evento quedó en `ERROR`.
- El stock permaneció en `-2`.
- No quedó modificación parcial.

El evento conservó:

- Estado `ERROR`.
- Intentos.
- `ultimo_error`.
- `processed_at` en `NULL`.

Después de implementar UUID5 se reintentó el mismo evento.

Resultado:

- Evento `ERROR` pasó a `PROCESADO`.
- Stock `-2` pasó a `-3`.
- `intentos = 3`.
- `ultimo_error = NULL`.
- `processed_at` asignado.

Luego se volvió a ejecutar el procesador.

Resultado:

- `procesados = 0`.
- `errores = 0`.
- Stock permaneció en `-3`.
- No pasó a `-4`.

Esta prueba validó:

- Recuperación de evento en `ERROR`.
- Idempotencia.
- Ausencia de doble descuento.
- Conservación de la venta.
- Consistencia del inventario.
- Rollback ante error de procesamiento.

## Endpoints implementados

```text
POST /api/ventas
GET /api/ventas
GET /api/ventas/{venta_id}

POST /api/ventas/{venta_id}/items
DELETE /api/ventas/{venta_id}/items/{item_id}

POST /api/ventas/{venta_id}/pagos
DELETE /api/ventas/{venta_id}/pagos/{pago_id}

POST /api/ventas/{venta_id}/finalizar

GET /api/ventas/eventos/pendientes
POST /api/ventas/eventos/procesar
```

## Reglas implementadas

Se mantiene el patrón existente de reglas Python tipadas.

Reglas documentadas:

- `SALE_EMPTY`.
- `SALE_INVALID_STATE`.
- `SALE_INVALID_LINE_QUANTITY`.
- `SALE_INVALID_LINE_PRICE`.
- `SALE_PAYMENT_INSUFFICIENT`.
- `SALE_ALREADY_CLOSED`.
- `SALE_TOTAL_INCONSISTENT`.
- `SALE_CAN_BE_FINALIZED`.

## Migración

Migración implementada:

```text
20260908_0005_sales_engine.py
```

Es posterior a:

```text
20260901_0004
```

Crea las estructuras correspondientes a:

- `ventas`.
- `detalles_venta`.
- `pagos_venta`.
- `eventos_pendientes`.

No se modifican migraciones anteriores.

## Tests automáticos

Comando utilizado:

```text
python -m pytest -p no:cacheprovider
```

Se utiliza `-p no:cacheprovider` por el problema conocido de permisos con `.pytest_cache` en el entorno Windows.

Antes de la corrección de UUID5:

- 48 tests passed.

Después de incorporar regresión para UUID5 y reintentos:

- 50 tests passed.

Los tests incluyen validaciones de:

- Creación de venta.
- Items.
- Pagos.
- Finalización.
- Venta vacía.
- Pago insuficiente.
- Evento `VENTA_FINALIZADA`.
- Procesamiento de inventario.
- Stock negativo.
- Idempotencia.
- UUID5 determinístico.
- Longitud compatible.
- Evento `ERROR` y reintento.
- Evento `PROCESADO` no reaplicado.
- Rollback ante error.

## Decisiones asociadas

| Código | Decisión |
|---|---|
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

## Referencias relacionadas

- [Módulo Venta en Salón](/doc/modulos/venta_salon/documento_maestro).
- [Motor de Inventario](/doc/general/motor_inventario).
- [Principios de Arquitectura](/doc/general/principios_arquitectura).
- [Modelo de Datos](/doc/modelo_datos/documento_maestro).
- [Registro de Decisiones](/doc/referencias/decisiones_agrupadas).

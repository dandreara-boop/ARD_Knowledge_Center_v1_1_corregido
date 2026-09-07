# Motor de Inventario

## Estado

Sprint 5 finalizado y validado.

El Motor de Inventario define cómo ARD Suite registra, consulta y mantiene el stock operativo.

## Principio general

El stock nunca se modifica directamente.

Toda variación genera un `MovimientoStock`.

Se mantienen dos niveles complementarios:

- `MovimientoStock`: libro histórico y auditable.
- `StockActual`: saldo materializado para consultas rápidas.

`StockActual` se actualiza incrementalmente con cada operación aceptada.

No se recalcula todo el historial para cada operación.

## Unidad de stock

El stock pertenece a la combinación:

```text
Variante + Destino de Inventario + Estado
```

No pertenece directamente al Artículo.

El stock total de un artículo se obtiene agregando sus variantes cuando una consulta lo requiere.

## Destino de Inventario

Sprint 5 introduce el concepto `DestinoInventario`.

Un destino de inventario no debe asumirse siempre como sucursal.

Tipos iniciales:

- `LOCAL`.
- `WEB`.
- `DEPOSITO`.
- `OTRO`.

El modelo queda preparado para extender destinos sin modificar el principio general de stock.

## Estados de stock

Estados iniciales:

- `DISPONIBLE`.
- `RESERVADO`.
- `EN_TRANSITO`.
- `NO_DISPONIBLE`.

## Movimiento de stock

Todo movimiento registra como mínimo:

- Identificador global.
- Variante.
- Destino.
- Estado.
- Cantidad firmada.
- Tipo.
- Fecha.
- Usuario opcional.
- Tipo de origen.
- Id de origen.
- Referencia.
- Motivo.
- Observación.
- Saldo anterior.
- Saldo resultante.

Una cantidad positiva representa una entrada.

Una cantidad negativa representa una salida.

Tipos de movimiento preparados:

- `RECEPCION_COMPRA`.
- `VENTA`.
- `ANULACION_VENTA`.
- `CAMBIO_ENTRADA`.
- `CAMBIO_SALIDA`.
- `TRANSFERENCIA_SALIDA`.
- `TRANSFERENCIA_ENTRADA`.
- `AJUSTE_POSITIVO`.
- `AJUSTE_NEGATIVO`.
- `MERMA`.

Estos tipos preparan el modelo para distintos procesos operativos, sin afirmar que todos los módulos que los generan estén implementados.

## Ajustes

No existe una operación conceptual de asignación directa:

```text
stock = nuevo_valor
```

El usuario informa el stock contado.

Ejemplo:

```text
Stock teórico: 6
Stock contado: 3
```

El sistema genera:

```text
AJUSTE_NEGATIVO -3
```

De esta manera conserva trazabilidad y permite auditar la diferencia.

## Stock negativo

El Motor de Inventario permite saldo negativo.

Una venta presencial no debe bloquearse porque el stock teórico sea insuficiente.

Las futuras excepciones administrativas podrán detectar estos casos, pero no deben interrumpir al vendedor.

## Idempotencia

Cada `MovimientoStock` posee un `global_id` único.

Si el mismo evento llega nuevamente:

- No se genera otro movimiento.
- `StockActual` no vuelve a modificarse.
- El evento se identifica como ya procesado.

Esto prepara el sistema para sincronización futura y reenvíos después de fallas de conectividad.

## Concurrencia

La actualización del saldo debe ser segura ante operaciones simultáneas de distintas cajas contra una misma base local.

El saldo se actualiza transaccionalmente.

No debe depender de una secuencia insegura de leer, modificar y guardar sin protección.

## Prioridad operativa

La materialización de una venta presencial tiene prioridad sobre procesos secundarios.

Las acciones que interactúan directamente con el cliente, especialmente cobrar y finalizar una venta, deben tener el camino de ejecución más corto posible.

Todo proceso que pueda diferirse sin comprometer la integridad de los datos se realizará fuera del camino crítico del POS.

La venta futura deberá guardar en una misma transacción rápida:

- Venta.
- Ítems.
- Pagos.
- Evento pendiente.

Una vez realizado el `COMMIT`, el cajero puede continuar.

Inventario, estadísticas, sincronización y otros procesos derivados podrán ejecutarse después.

La creación del evento pendiente debe ocurrir dentro de la misma transacción que materializa la venta para impedir una venta registrada sin obligación posterior de procesamiento.

## Eventos de dominio

Sprint 5 deja preparado un punto de integración mediante eventos de dominio.

No existe todavía un bus completo.

No se documentan como existentes:

- Redis.
- RabbitMQ.
- Kafka.
- Workers distribuidos.

La intención es desacoplar progresivamente:

```text
Venta
  ↓
Evento
  ↓
Inventario
```

Esto permitirá posteriormente consumidores como:

- Sincronización.
- Auditoría.
- Estadísticas.

## Validación realizada

Sprint 5 fue validado mediante pruebas manuales y automáticas.

Pruebas manuales:

- Movimiento positivo.
- Movimiento negativo.
- Idempotencia.
- Ajuste positivo.
- Ajuste negativo.
- Stock negativo permitido.
- Movimiento de cantidad cero rechazado.
- Consistencia entre `MovimientoStock` y `StockActual`.

Pruebas automáticas:

- 39 tests totales aprobados en el proyecto.

Alembic:

- `20260901_0004` es `HEAD`.

Los datos temporales utilizados durante QA no constituyen reglas de negocio.

## Decisiones asociadas

| Código | Decisión |
|---|---|
| DAT-STK-001 | El stock se registra por variante y destino de inventario. |
| DAT-STK-002 | Todo cambio de stock genera un movimiento. |
| DAT-STK-003 | El modelo mantiene historial auditable y saldo materializado. |
| DAT-STK-004 | Los movimientos de stock están tipificados. |
| DAT-STK-005 | Todo movimiento conserva documento u origen trazable. |
| DAT-STK-006 | El stock negativo está permitido en salón. |
| DAT-STK-007 | Los ajustes se realizan mediante movimientos compensatorios. |
| DAT-STK-008 | Cada movimiento posee identificador global para idempotencia. |
| DAT-STK-009 | La materialización de venta tiene prioridad operativa. |
| DAT-STK-010 | Venta y evento pendiente deben persistirse atómicamente. |
| DAT-STK-011 | Inventario podrá procesarse fuera del camino crítico del POS. |
| DAT-STK-012 | Los procesos pesados no deben ralentizar la facturación. |
| DAT-STK-013 | `StockActual` se actualiza incrementalmente. |

## Referencias relacionadas

- [Modelo Conceptual](/doc/general/modelo_conceptual).
- [Principios de Arquitectura](/doc/general/principios_arquitectura).
- [Modelo de Datos](/doc/modelo_datos/documento_maestro).
- [Registro de Decisiones](/doc/referencias/decisiones_agrupadas).

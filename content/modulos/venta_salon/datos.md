# Modelo de datos — Venta en Salón

## Estado

Sprint 7 implementó y validó funcionalmente el motor comercial de precios por Artículo.

Sprint 6 implementó y validó funcionalmente el núcleo transaccional de venta local.

Sprint 8 tiene implementada la resolución comercial y cobro del POS, con solver HiGHS integrado, migración aplicada y QA automático y manual aprobado.

Sprint 9.3 implementó las reglas backend de sesiones de caja, captura explícita para cobro y confirmación por cajero responsable. No requirió nueva migración; Alembic continúa en `20261006_0009` (head).

Sprint 9.4 implementó movimientos operativos de caja reutilizando `MovimientoCaja` sin cambios de schema, sin migración, con Alembic en `20261006_0009` (head), 132 tests aprobados y movimientos append-only.

Sprint 9.5 documenta decisiones previas a implementación para efectivo físico, cierre y alcance del arqueo. No está implementado todavía.

## CondicionComercialPrecio

- Identificador.
- Nombre o código de condición.
- Tipo `BASE` o derivada.
- Condición base de referencia, cuando corresponde.
- Tipo de regla.
- Porcentaje.
- Tipo de redondeo.
- Múltiplo de redondeo, cuando corresponde.
- Estado activo.

Sólo puede existir una condición `BASE` activa según validación de servicio.

Las reglas pertenecen a la condición comercial, no a cada artículo.

## PrecioArticulo

- Artículo.
- Condición comercial.
- Precio.
- Origen `REGLA` o `MANUAL`.
- Fechas de creación y actualización.

La unicidad conceptual es:

```text
Artículo + Condición comercial
```

El precio pertenece al Artículo. La Variante no define precio independiente en Sprint 7.

## AuditoriaPrecioArticulo

- Artículo.
- Condición comercial.
- Precio anterior.
- Precio nuevo.
- Origen anterior.
- Origen nuevo.
- Motivo.
- Usuario opcional.
- Timestamp.

La auditoría se genera sólo cuando cambia el precio o el origen.

## MedioPago

Concepto aprobado para Sprint 8:

- Identificador.
- Nombre.
- Estado activo.
- Condición comercial asociada.
- Identificación explícita y estable de si representa efectivo físico, cuando corresponda definirla técnicamente.

`MedioPago` y `CondicionComercialPrecio` son conceptos separados.

La relación entre ambos debe ser configurable.

Sprint 9.5 define funcionalmente que existe un único `MedioPago` que representa efectivo físico dentro del cajón: `EFECTIVO`. No debe identificarse comparando el texto visible o nombre del medio de pago; el modelo deberá permitir reconocerlo mediante una identificación explícita y estable. La implementación técnica concreta se revisará contra el modelo actual antes de programar.

## ResolucionComercialCobro

Concepto aprobado para Sprint 8:

- Solicitud de pago.
- Medios utilizados.
- Condiciones comerciales aplicadas.
- Distribución calculada.
- Asignaciones completas.
- Fracciones.
- Subtotal interno por medio.
- Ajuste de redondeo final por medio.
- Total final.
- Estado de simulación o confirmación.

No se documenta todavía como tabla implementada.

## TrazaResolucionComercial

Concepto aprobado para Sprint 8:

- Artículos.
- Unidades.
- Precios efectivos.
- Origen de precios, cuando corresponda.
- Relaciones de conversión.
- Valores internos antes de redondeo.
- Subtotal interno por medio.
- Ajuste de redondeo final.
- Criterio de selección.
- Resultado por medio.
- Explicación histórica.

La traza confirmada debe conservarse como snapshot y no reconstruirse con precios actuales.

## Venta

- Identificador global.
- Sucursal.
- Local.
- Dispositivo o terminal de origen, cuando corresponda.
- Vendedor atribuido, opcional en autoservicio.
- Cajero responsable del cobro, cuando corresponda.
- Cliente.
- Referencia simple de cliente para operación de salón.
- Número corto operativo.
- Tipo de atención: vendedor asistido o autoservicio.
- Fecha local.
- Fecha de sincronización.
- Estado.
- Caja capturadora, cuando esté en cobro.
- Sesión de caja asociada al cobro, cuando corresponda.
- Momento de captura, cuando esté en cobro.

Estados preparados:

- `ABIERTA`.
- `LISTA_PARA_COBRAR`.
- `EN_COBRO`.
- `SUSPENDIDA`.
- `EN_PAGO`.
- `CERRADA`.
- `ANULADA`.

Sprint 6 implementa el cierre transaccional local, pero no implementa todavía toda la operatoria de suspensión, anulación, caja, promociones, cambios ni devoluciones.

Sprint 9 reemplaza cualquier interpretación que equipare terminal, caja, vendedor y cajero. Una caja no es una PC/tablet y una sesión pertenece a una caja concreta y a un único cajero responsable. La sesión no pertenece al dispositivo.

El número corto no reemplaza al `global_id`. Su política definitiva de numeración y reinicio queda pendiente de validación técnica; una venta anulada no reutiliza su número corto.

## Caja

Concepto funcional aprobado para Sprint 9:

- Identificador.
- Local.
- Nombre o código operativo.
- Estado.

Una Caja representa un punto lógico/físico de cobro, no una PC o tablet.

## SesionCaja

Concepto funcional aprobado para Sprint 9:

- Identificador.
- Local.
- Caja concreta.
- Cajero responsable.
- Fecha/hora de apertura.
- Efectivo inicial declarado manualmente.
- Fecha/hora de cierre.
- Estado.

Para cobrar debe existir una sesión abierta, válida y seleccionada explícitamente. Una caja no puede tener dos sesiones activas simultáneamente. Un cajero puede tener varias sesiones abiertas en cajas distintas, con advertencia no bloqueante al abrir otra. La sesión no se traslada entre cajas ni entre dispositivos, y el efectivo inicial nunca se hereda automáticamente del turno anterior.

Una sesión puede ser consultada y utilizada desde otra computadora sin modificar su identidad. Otro cajero no puede cobrar ni confirmar utilizando una sesión ajena.

La venta `EN_COBRO` debe conservar `caja_captura_id` y `sesion_caja_id`. Al liberar de `EN_COBRO` a `LISTA_PARA_COBRAR`, esos datos y `capturada_at` se eliminan de la venta activa, pero quedan en el evento histórico de liberación.

## MovimientoCaja

Concepto funcional aprobado para Sprint 9:

- Sesión.
- Tipo.
- Importe.
- Usuario.
- Fecha/hora.
- Motivo, cuando corresponda.

Tipos definidos por Sprint 9.4:

- `INGRESO`: entra efectivo al cajón por causa distinta de una venta; aumenta el efectivo esperado, no genera `Venta`, no genera `PagoVenta` y no representa ingreso comercial por venta. Motivo opcional.
- `RETIRO`: mueve dinero fuera del cajón hacia otro lugar de resguardo; disminuye el efectivo esperado, no requiere motivo obligatorio ni autorización previa y no representa gasto, pago a proveedor ni pérdida.
- `EGRESO` o `PAGO`: utiliza efectivo de caja para pagar algo; disminuye el efectivo esperado, requiere motivo obligatorio y representa una salida económica.

Todo movimiento requiere importe mayor a `0`, sesión abierta, caja derivada de la sesión, cajero responsable y fecha/hora. No se permite registrar movimientos sobre una sesión cerrada ni asociarlos solamente al cajero.

Si el cajero tiene una sola sesión abierta, la UI futura puede usarla directamente para movimientos rápidos. Si tiene varias, debe pedir selección explícita de sesión/caja. En ambos casos el movimiento persistido debe conservar un `sesion_caja_id` concreto.

## ArqueoCaja

Concepto funcional aprobado para Sprint 9:

- Sesión.
- Tipo de arqueo.
- Conteo original.
- Efectivo esperado.
- Diferencia.
- Fecha/hora.
- Estado.

El primer conteo es ciego y nunca se borra. Después del primer conteo se muestran esperado, contado y diferencia.

El efectivo esperado en el cajón se calcula conceptualmente con efectivo inicial declarado, cobros de ventas realizados en `EFECTIVO`, movimientos `INGRESO`, menos movimientos `RETIRO` y movimientos `EGRESO`. En pagos mixtos sólo la porción `EFECTIVO` modifica el efectivo físico esperado.

El cajero cuenta únicamente el efectivo físico restante en su cajón. Los retiros registrados quedan fuera de su conteo y pueden verificarse posteriormente por supervisor o encargado para investigar diferencias. Esa verificación no reescribe el primer conteo histórico.

## SolicitudCorreccionArqueo

Concepto funcional aprobado para Sprint 9:

- Arqueo.
- Conteo original.
- Conteo corregido propuesto.
- Cajero solicitante.
- Fecha/hora.
- Estado `PENDIENTE`, aprobado o rechazado.
- Supervisor revisor, cuando corresponda.

La solicitud sólo puede iniciarse durante el cierre inmediato. Una corrección pendiente no bloquea el cierre ni la siguiente apertura.

La verificación posterior de retiros puede aportar evidencia para una investigación o corrección administrativa, pero no modifica el conteo original del cajero.

## PosibleErrorPago

Concepto funcional aprobado para Sprint 9:

- Venta.
- Sesión.
- Cajero que marca el caso.
- Fecha/hora.
- Estado pendiente.
- Resolución de supervisor, cuando corresponda.

La venta `CERRADA` permanece inmutable. La corrección posterior del medio de pago se registra como operación administrativa separada y auditable, nunca como edición silenciosa de `PagoVenta`.

## AuditoriaOperativa

Concepto funcional aprobado para Sprint 9:

- Entidad afectada.
- Operación.
- Usuario.
- Caja y sesión, cuando corresponda.
- Fecha/hora.
- Valor anterior.
- Valor nuevo.
- Contexto operativo.

Debe permitir reconstruir creación, envío, captura, liberación, modificaciones, cobro, anulación, verificación, movimientos, cierre y pendientes.

## DetalleVenta

- Variante.
- Código de artículo.
- Código de barras.
- Descripción.
- Cantidad.
- Precio unitario.
- Importe.

Cada detalle conserva snapshot comercial. Una venta histórica no depende de cambios posteriores en catálogo.

## PagoVenta

- Medio.
- Importe.
- Referencia externa.
- Estado.

Sprint 6 valida que los pagos sean suficientes para finalizar la venta. El módulo completo de caja queda fuera de este alcance.

## EventoPendiente / outbox local

- `global_id`.
- Tipo.
- Payload.
- Estado.
- Intentos.
- Fecha de creación.
- Fecha de procesamiento.
- Último error.

Evento implementado:

- `VENTA_FINALIZADA`.

Estados:

- `PENDIENTE`.
- `PROCESANDO`.
- `PROCESADO`.
- `ERROR`.

Payload mínimo de `VENTA_FINALIZADA`:

- `venta_id`.
- `venta_global_id`.
- `destino_id`.

El evento se guarda en la misma transacción que la venta cerrada y representa la obligación persistente de ejecutar efectos derivados.

## Decisión comercial

- Promoción aplicada.
- Regla utilizada.
- Explicación.
- Ahorro del cliente.
- Versión del motor comercial.

## Cola de sincronización

- Entidad.
- Identificador.
- Intentos.
- Último error.
- Estado.
- Fecha de confirmación.

Sprint 6 no implementa sincronización cloud ni worker definitivo.

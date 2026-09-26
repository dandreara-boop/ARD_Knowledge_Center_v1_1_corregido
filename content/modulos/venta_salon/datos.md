# Modelo de datos — Venta en Salón

## Estado

Sprint 7 implementó y validó funcionalmente el motor comercial de precios por Artículo.

Sprint 6 implementó y validó funcionalmente el núcleo transaccional de venta local.

Sprint 8 tiene implementada la resolución comercial y cobro del POS, con solver HiGHS integrado, migración aplicada y QA automático y manual aprobado.

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

`MedioPago` y `CondicionComercialPrecio` son conceptos separados.

La relación entre ambos debe ser configurable.

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
- Terminal.
- Vendedor.
- Cliente.
- Fecha local.
- Fecha de sincronización.
- Estado.

Estados preparados:

- `ABIERTA`.
- `SUSPENDIDA`.
- `EN_PAGO`.
- `CERRADA`.
- `ANULADA`.

Sprint 6 implementa el cierre transaccional local, pero no implementa todavía toda la operatoria de suspensión, anulación, caja, promociones, cambios ni devoluciones.

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

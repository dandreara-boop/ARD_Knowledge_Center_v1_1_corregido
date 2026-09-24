# Modelo conceptual del negocio

## Entidades centrales

- Empresa.
- Sucursal.
- Destino.
- Producto.
- CondicionComercialPrecio.
- PrecioArticulo.
- AuditoriaPrecioArticulo.
- MedioPago.
- ResolucionComercialCobro.
- TrazaResolucionComercial.
- Atributo.
- Familia de atributos.
- Valor de atributo.
- Curva.
- Variante.
- Servicio Interno de Generación de Variantes.
- Destino de Inventario.
- StockActual.
- Proveedor.
- Cliente.
- Remito de Entrada.
- Movimiento de stock.
- Venta.
- DetalleVenta.
- PagoVenta.
- EventoPendiente.
- Caja.
- Campaña.
- Promoción.

## Principio de separación

El producto representa la identidad comercial.

Los atributos representan características como talle, color, estampa o número.

La variante representa una presentación concreta del artículo determinada por una combinación de atributos.

El stock pertenece a una variante operativa, a un destino de inventario y a un estado.

El Artículo no almacena stock directo.

El stock total de un artículo se obtiene agregando variantes cuando una consulta lo requiere.

## Gestión de variantes

Las variantes no se generan obligatoriamente al crear un producto.

El flujo vigente es:

```text
Artículo
        ↓
Recepción de Mercadería
        ↓
Servicio Interno de Generación de Variantes
        ↓
Stock
```

El Servicio Interno de Generación de Variantes es un componente reutilizable utilizado por Recepción, Importaciones, Procesos Administrativos y API.

El operario trabaja con mercadería y atributos recibidos; el sistema busca o crea internamente la variante correspondiente.

## Venta local e inventario

Sprint 6 conecta Catálogo, Variante, Venta, EventoPendiente e Inventario.

La venta local se cierra en una transacción rápida que guarda `Venta CERRADA` y evento `VENTA_FINALIZADA` en el outbox local. Después del `COMMIT`, el POS puede considerar terminada la operación crítica.

Los efectos derivados, incluido inventario, se procesan posteriormente mediante eventos pendientes reintentables e idempotentes.

`DetalleVenta` conserva snapshot comercial para que la venta histórica no dependa de cambios posteriores en catálogo.

## Motor comercial de precios

Sprint 7 incorpora el motor comercial de precios a nivel de Artículo.

El precio comercial pertenece al Artículo, no a la Variante.

Las condiciones comerciales pueden ser `BASE` o derivadas de otra condición. Las reglas pertenecen a la condición comercial y se implementan como reglas Python tipadas y controladas.

Los cambios actuales de precio no recalculan ventas históricas porque `DetalleVenta` conserva `precio_unitario` como snapshot.

## Resolución comercial y cobro POS

Sprint 8 tiene diseño funcional aprobado y queda pendiente de implementación.

El diseño separa `MedioPago` de `CondicionComercialPrecio`.

Una venta abierta comienza valorizada con la condición `BASE` y puede simular otros medios o condiciones sin persistir snapshots definitivos.

La confirmación de cobro deberá congelar históricamente medios, condiciones, precios, importes, distribución, fracciones, redondeos y traza de decisión.

La resolución comercial determina cuánto corresponde cobrar; inventario conserva la responsabilidad de mover stock mediante el mecanismo existente.

Ver también:

- [Gestión de Variantes](/doc/general/gestion_variantes).
- [Motor de Inventario](/doc/general/motor_inventario).
- [Sprint 6 — Motor de Venta Local](/doc/modulos/venta_salon/sprint_6_motor_venta_local).
- [Sprint 7 — Motor Comercial de Precios](/doc/modulos/venta_salon/sprint_7_motor_comercial_precios).
- [Sprint 8 — Resolución Comercial y Cobro del POS](/doc/modulos/venta_salon/sprint_8_resolucion_comercial_cobro_pos).
- [Principios de Arquitectura](/doc/general/principios_arquitectura).

## Ejemplo

```text
Producto: Remera Algodón
Atributo Talle: 2
Atributo Color: Negro
Destino: Local Centro
Cantidad: 4
```

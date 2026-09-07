# Modelo conceptual del negocio

## Entidades centrales

- Empresa.
- Sucursal.
- Destino.
- Producto.
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
- Pago.
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

Ver también:

- [Gestión de Variantes](/doc/general/gestion_variantes).
- [Motor de Inventario](/doc/general/motor_inventario).
- [Principios de Arquitectura](/doc/general/principios_arquitectura).

## Ejemplo

```text
Producto: Remera Algodón
Atributo Talle: 2
Atributo Color: Negro
Destino: Local Centro
Cantidad: 4
```

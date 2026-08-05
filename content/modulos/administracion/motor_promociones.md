# Motor de Promociones

## Definición

El Motor de Promociones administra reglas comerciales temporales. No agrega opciones permanentes de liquidación o participación al crear un producto: la participación de los productos se decide dentro de cada promoción.

El cajero no decide si un producto participa. El motor resuelve automáticamente, aplica la regla vigente y guarda la explicación.

## Creación de promoción

Cada promoción registra:

- Nombre.
- Tipo.
- Fecha y hora de inicio.
- Fecha y hora de finalización.
- Canales.
- Sucursales.
- Condiciones de pago.
- Prioridad.
- Estado.
- Usuario creador.

## Tipos iniciales

- Descuento porcentual.
- Precio fijo.
- Dos por un valor.
- Tres por un valor.
- Segunda unidad con descuento.
- Descuento por cantidad.
- Promoción por categoría.
- Promoción por proveedor.
- Liquidación general.

## Alcance por reglas

Cada promoción define su alcance mediante inclusiones y exclusiones.

### Inclusiones

- Todos los productos.
- Proveedores seleccionados.
- Categorías.
- Códigos individuales.
- Productos.
- Sucursales.
- Canales.
- Productos de determinados remitos.
- Productos sin movimiento desde una fecha.

### Exclusiones

- Proveedores.
- Categorías.
- Códigos individuales.
- Productos.
- Sucursales.
- Canales.
- Productos ya alcanzados por otras campañas.
- Mercadería recibida después de una fecha.

Cuando una regla incluye y otra excluye el mismo artículo, prevalece la exclusión.

## Suspensión de otras promociones

Una promoción puede suspender otras promociones durante su vigencia. Por ejemplo, una liquidación general del 20 % puede suspender temporalmente promociones como 2 remeras por un valor fijo, 3 prendas por un valor fijo o segunda unidad con descuento.

Al finalizar la promoción principal, las promociones suspendidas deben reactivarse automáticamente si así fue configurado.

## Estados

- BORRADOR.
- PROGRAMADA.
- ACTIVA.
- SUSPENDIDA_MANUALMENTE.
- SUSPENDIDA_POR_OTRA_PROMOCIÓN.
- FINALIZADA.
- CANCELADA.

## Simulación previa

Antes de activar una promoción, Administración debe poder simularla y mostrar:

- Productos incluidos.
- Productos excluidos.
- Exclusiones por proveedor.
- Exclusiones por código.
- Exclusiones por categoría.
- Promociones que serán suspendidas.
- Canales y sucursales afectadas.

Cada conjunto debe permitir consultar su detalle.

Ver también:

- Venta en Salón — Promociones y precios.
- DEC-014.
- DEC-124.
- DEC-125.
- DEC-126.
- DEC-127.
- DEC-128.

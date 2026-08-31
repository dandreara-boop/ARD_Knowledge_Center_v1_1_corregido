# Modelo de datos — Carga de Productos

## Entidades

### Producto

- Código.
- Descripción.
- Precio.
- Estado.
- Canales.
- Atributos designados.
- Familia de atributos sugerida.

### Familia de atributos

- Nombre.
- Atributos incluidos.
- Estado.

### Variante

- Producto.
- Valores de atributos.
- Código de barras.
- Estado.

### Servicio Interno de Generación de Variantes

- Producto.
- Valores de atributos recibidos.
- Origen del proceso.
- Variante encontrada o creada.

### Remito de Entrada

- Número.
- Fecha.
- Estado.
- Proveedor.
- Participantes.
- Observaciones.

### Ítem del remito

- Producto.
- Código.
- Costo.
- Estado de carga.
- Observaciones.

### Conteo

- Producto.
- Valores de atributos.
- Cantidad.
- Variante resuelta internamente.

### Asignación inicial

- Producto o combinación de atributos.
- Destino.
- Cantidad.

### Movimiento de stock

- Variante.
- Origen.
- Destino.
- Cantidad.
- Motivo.
- Documento.
- Usuario.
- Fecha.

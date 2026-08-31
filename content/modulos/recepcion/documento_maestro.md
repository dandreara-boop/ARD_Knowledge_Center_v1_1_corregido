# Módulo Recepción de Mercadería

## Objetivos

{{include:modulos/carga_productos/resumen}}

## Proceso completo

{{include:modulos/carga_productos/flujo}}

## Creación de producto

La creación de producto ocurre cuando el código ingresado no existe. En ese caso se crea el producto, se asigna código y precio, y luego se agrega al Remito de Entrada.

## Productos existentes

Cuando el código ya existe, el producto se identifica y se agrega directamente al Remito de Entrada sin abrir su ficha completa.

## Remitos de entrada

El Remito de Entrada puede contener productos existentes y productos nuevos. Funciona como documento colaborativo para registrar la mercadería recibida, sus cantidades, atributos, distribución y movimientos auditables.

## Carga de atributos

Los atributos visibles en depósito dependen de lo designado desde Administración. La carga se registra únicamente con los atributos que llegaron realmente y sus cantidades.

Durante la confirmación, el sistema busca la variante correspondiente, la utiliza si ya existe o la crea automáticamente si todavía no existe. También genera el código de barras correspondiente y registra el movimiento de stock.

No debe existir un botón operativo denominado **Generar Variantes**. La generación queda resuelta internamente por el Servicio Interno de Generación de Variantes.

## Distribución por sucursal

La distribución se expresa en cantidades. No se utilizan porcentajes. Los destinos pueden ser locales, depósito, stock web u otros puntos operativos definidos.

## Stock Web

El Stock Web es un destino operativo dentro de la distribución inicial. La autoridad consolidada del Stock Web reside en la base central.

## Diagramas

Los diagramas aprobados del módulo se conservan dentro de los wireframes relacionados y en la página de pantallas.

## Wireframes relacionados

{{include:modulos/carga_productos/pantallas}}

## Modelo de datos del módulo

{{include:modulos/carga_productos/datos}}

## Reglas de negocio

- Producto y atributos se mantienen separados.
- Las variantes se crean únicamente cuando existe una necesidad real.
- Recepción utiliza internamente el Servicio de Generación de Variantes.
- El operario nunca trabaja directamente con variantes.
- El código permanece visible durante los procesos operativos.
- El remito admite productos existentes y nuevos.
- Depósito muestra solamente los atributos definidos por Administración.
- La distribución utiliza cantidades, no porcentajes.
- Finalizar el remito genera movimientos auditables.

## Casos especiales

- Código encontrado: se agrega el producto existente al remito.
- Código no encontrado: se crea el producto y luego se agrega al remito.
- Mercadería separada físicamente por producto y talle antes de distribuir.
- Etiquetado realizado en cada local después de la distribución.

## Decisiones relacionadas

{{include:modulos/carga_productos/decisiones}}

Ver también:

- [Gestión de Variantes](/doc/general/gestion_variantes).
- [Modelo Conceptual](/doc/general/modelo_conceptual).
- [Principios de Arquitectura](/doc/general/principios_arquitectura).

## Próximos desarrollos

- Consolidar la ficha estándar de cada pantalla de recepción.
- Definir configuración administrativa de atributos visibles por proceso.
- Preparar reportes de ingreso, distribución y movimientos generados.

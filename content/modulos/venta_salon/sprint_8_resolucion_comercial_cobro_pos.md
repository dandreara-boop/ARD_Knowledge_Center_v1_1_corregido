# Sprint 8 — Resolución Comercial y Cobro del POS

## Estado

DISEÑO FUNCIONAL APROBADO / PENDIENTE DE IMPLEMENTACIÓN.

Sprint 8 no se documenta como implementado ni validado por QA.

El Sprint 8 define el diseño funcional del backend que conectará:

- Motor de Venta Local del Sprint 6.
- Motor Comercial de Precios del Sprint 7.
- Medios de pago.
- Resolución de pagos simples y mixtos.

El frontend POS definitivo no pertenece al Sprint 8.

## Objetivo

El vendedor carga artículos y formas de pago.

ARD Suite realiza automáticamente los cálculos comerciales.

La venta comienza utilizando la condición comercial `BASE`, normalmente `PRECIO_1` / Contado.

Mientras la venta permanezca abierta:

- Se pueden agregar o quitar artículos.
- Se pueden modificar cantidades.
- Se pueden consultar otros precios.
- Se puede cambiar la condición de visualización.
- Se pueden preparar formas de pago.
- Se pueden agregar o quitar medios.
- Se pueden modificar importes.
- Se puede recalcular.
- Se puede abandonar una simulación y realizar otra.

Nada comercial queda definitivo hasta confirmar cobro.

## Alcance backend previsto

Sprint 8 debe diseñar para backend:

- Modelo/configuración de medios de pago.
- Asociación configurable `MedioPago -> CondicionComercialPrecio`.
- Consulta o cotización por condición o medio.
- Simulación de pago simple.
- Simulación de pago mixto.
- Múltiples medios.
- Máximo un medio marcado como `RESTO`.
- Importes fijos desde cualquier condición.
- Resolución favorable al cliente.
- Asignación por unidades físicas.
- Fraccionamiento proporcional.
- Conversión simétrica entre condiciones.
- Uso de `Decimal`.
- Redondeo hacia arriba a `0,05`, conceptualmente configurable.
- Traza estructurada de decisión.
- Persistencia del snapshot al confirmar.
- Confirmación local y atómica.
- Protección de venta cerrada.
- Integración sin romper el mecanismo de inventario existente.

## Fuera de alcance

Quedan explícitamente fuera del Sprint 8:

- Frontend POS definitivo.
- Impresión física definitiva del análisis.
- Impresora fiscal.
- Apertura, cierre y arqueo de caja.
- Promociones.
- 2x1.
- Descuentos por cantidad.
- Clientes.
- Precios por cliente.
- Cuenta corriente.
- Mayoristas por cliente.
- Bancos.
- Planes de cuotas.
- Intereses financieros específicos.
- Devoluciones.
- Implementación completa de anulaciones.
- Tiendanube.
- Nuevas funciones de sincronización nube.
- Cambios al modelo offline-first.

## Dependencias

### Sprint 6 — Motor de Venta Local

Sprint 6 ya implementó la venta local, sus detalles, pagos, outbox local, evento `VENTA_FINALIZADA` e integración posterior con inventario.

Sprint 8 no debe romper ese mecanismo.

La confirmación de cobro debe continuar integrándose con `EventoPendiente`, `InventoryService` e idempotencia ya existentes.

### Sprint 7 — Motor Comercial de Precios

Sprint 7 ya implementó precios por Artículo y condiciones comerciales de precio.

Sprint 8 usa esas condiciones y precios para resolver cuánto corresponde cobrar.

El precio sigue perteneciendo al Artículo, no a la Variante.

## Conceptos principales

### Condición BASE

Toda venta nueva comienza valorizada con la condición comercial configurada como `BASE`.

El vendedor no necesita seleccionar manualmente `PRECIO_1`.

La condición `BASE` pertenece a la configuración comercial.

### Medio de pago y condición comercial

`MedioPago` y `CondicionComercialPrecio` son conceptos distintos.

Ejemplo:

```text
EFECTIVO       -> PRECIO_1
TRANSFERENCIA  -> PRECIO_1
VISA           -> PRECIO_2
MASTERCARD     -> PRECIO_2
QR             -> PRECIO_2
```

Varios medios pueden compartir una misma condición comercial.

Conceptualmente:

```text
MedioPago
    -> condicion_comercial_id
        -> CondicionComercialPrecio
            -> PrecioArticulo
```

La relación debe ser configurable.

No se debe hardcodear que Visa siempre usa `PRECIO_2`.

## Consulta y simulación

Durante una venta `ABIERTA` debe poder consultarse cuánto costaría la operación bajo otro medio o condición comercial.

Ejemplo:

```text
Contado: 60.000
Visa:    66.000
QR:      66.000
```

Consultar:

- No modifica la venta.
- No registra un pago.
- No genera el snapshot definitivo.
- No obliga a utilizar posteriormente ese medio.

Debe existir conceptualmente una operación de cotización o simulación sin persistencia comercial definitiva.

## Requisito para futuro frontend POS

Aunque el frontend definitivo no pertenece al Sprint 8, el backend no debe impedir este comportamiento:

**REQ-POS-SIM**

Durante la carga de una venta abierta deberá ser posible seleccionar una condición comercial o medio de pago de visualización.

Todos los artículos cargados y los incorporados posteriormente deberán poder mostrarse valorizados según esa condición.

La selección será reversible, no constituirá un pago, no alterará snapshots definitivos y no condicionará la posterior resolución simple o mixta del cobro.

Ejemplo:

```text
Precio mostrado:
- Contado
- Visa
- QR
```

Si se selecciona Visa:

- Los artículos ya cargados se muestran a precio Visa.
- Los artículos escaneados posteriormente también se muestran a precio Visa.
- El total visible corresponde a Visa.

Esta selección es solamente una condición de visualización o simulación.

No constituye una selección definitiva del medio de pago.

## Pago con un único medio

Si el cliente paga todo con un medio, ARD obtiene la condición comercial asociada a ese medio y calcula la venta con los precios efectivos de esa condición.

Ejemplo:

```text
TOTAL BASE = 60.000
Medio = Visa
```

Antes de confirmar, la operación sigue siendo modificable.

## Pagos mixtos

Debe soportarse conceptualmente una cantidad arbitraria de medios.

Ejemplos:

```text
EFECTIVO       40.000
VISA           RESTO
```

```text
EFECTIVO       20.000
DEBITO         15.000
VISA           RESTO
```

```text
EFECTIVO       20.000
DEBITO         15.000
VISA           25.000
TRANSFERENCIA  RESTO
```

Debe utilizarse el mismo criterio de resolución independientemente de que existan 2, 3 o más medios.

No deben diseñarse algoritmos comerciales diferentes según la cantidad de medios.

## Un solo RESTO

Una distribución de pagos puede contener como máximo un medio marcado como `RESTO`.

Válido:

```text
EFECTIVO    20.000
VISA        30.000
MASTERCARD  RESTO
```

Inválido:

```text
EFECTIVO    20.000
VISA        RESTO
MASTERCARD  RESTO
```

Dos medios `RESTO` deben ser rechazados.

## Importes fijos desde cualquier condición

El algoritmo debe ser simétrico.

Debe resolver:

```text
40.000 EFECTIVO
RESTO VISA
```

y también:

```text
40.000 VISA
RESTO EFECTIVO
```

No debe asumirse que el importe fijo siempre está expresado a precio `BASE`.

Debe poder convertir proporcionalmente entre condiciones:

```text
PRECIO_1 <-> PRECIO_2
PRECIO_1 <-> PRECIO_3
PRECIO_2 <-> PRECIO_3
```

cuando corresponda.

## Unidad física como unidad de asignación

Antes de fraccionar monetariamente un artículo, el motor debe intentar asignar unidades físicas completas.

Ejemplo:

```text
Remera x3
Contado: 10.000 por unidad
Visa:    11.000 por unidad
```

Puede resolver:

```text
2 unidades -> contado
1 unidad   -> Visa
```

Aunque el POS muestre una única línea con cantidad 3, comercialmente son tres unidades asignables.

## Criterio principal

La regla central es:

Entre todas las distribuciones válidas que respeten los importes indicados por el cliente, ARD Suite debe seleccionar la que produzca el menor importe final para el cliente.

No usar como regla de negocio:

- Primer artículo.
- Artículo más caro.
- Primera combinación encontrada.

Puede utilizarse como heurística interna la diferencia entre precios, pero la regla funcional es minimizar el costo final real.

Ejemplo:

```text
Artículo A:
BASE 10.000
VISA 11.000

Artículo B:
BASE 20.000
VISA 23.000

Artículo C:
BASE 30.000
VISA 36.000

Cliente dispone de 30.000 efectivo y RESTO Visa.
```

Resolver C a efectivo produce:

```text
30.000 + 11.000 + 23.000 = 64.000
```

Resolver A+B a efectivo produce:

```text
10.000 + 20.000 + 36.000 = 66.000
```

ARD debe elegir 64.000.

La idea funcional del negocio es utilizar el precio base preferentemente en los artículos donde genere mayor ahorro real frente a las demás condiciones.

## Prioridades del algoritmo

Jerarquía funcional:

1. Respetar los importes solicitados por el cliente.
2. Obtener el menor costo total posible.
3. Utilizar unidades completas cuando no perjudique económicamente al cliente.
4. Fraccionar monetariamente solamente cuando sea necesario.
5. Ante soluciones económicamente equivalentes, elegir la que produzca menos fracciones.
6. Ante soluciones todavía equivalentes, utilizar un criterio determinista.

La misma entrada debe producir siempre la misma solución.

## Fraccionamiento proporcional

Cuando el importe solicitado no puede resolverse exclusivamente con unidades completas, puede dividirse monetariamente una unidad.

Ejemplo:

```text
Dos artículos.

Cada uno:
BASE = 30.000
VISA = 33.000

Cliente:
EFECTIVO = 40.000
VISA = RESTO
```

Puede asignarse:

```text
Artículo A completo a efectivo = 30.000

Del artículo B:
10.000 cubiertos con efectivo.

Quedan 20.000 equivalentes BASE.

Relación:
33.000 / 30.000 = 1,10

Parte restante Visa:
20.000 * 1,10 = 22.000

Resultado:
EFECTIVO = 40.000
VISA     = 22.000
TOTAL    = 62.000
```

## Conversión proporcional general

Conceptualmente:

```text
importe_destino =
importe_origen * (precio_destino / precio_origen)
```

Debe utilizarse `Decimal`.

Nunca `float`.

La conversión debe funcionar en ambos sentidos y entre condiciones no `BASE` cuando sea necesario.

## Redondeo monetario

Decisión aprobada:

- Precisión visible/monetaria: 2 decimales.
- Incremento de redondeo inicial: `0,05`.
- Redondeo siempre hacia arriba al siguiente múltiplo de `0,05`.
- Utilizar `Decimal`.
- No utilizar `float`.

Ejemplos:

```text
10,00  -> 10,00
10,01  -> 10,05
10,03  -> 10,05
10,05  -> 10,05
10,051 -> 10,10
```

La normalización debe aplicarse desde el momento en que una valorización proporcional genera el importe monetario correspondiente, para evitar diferencias ocultas acumuladas.

El incremento `0,05` debe quedar conceptualmente configurable y no enterrado como una constante de negocio imposible de cambiar.

Este redondeo de pagos mixtos es una política monetaria del cobro, aunque sigue el criterio de redondeo hacia arriba ya existente en el motor comercial.

## Solicitud vs distribución calculada

Debe separarse conceptualmente:

Solicitud del cliente:

```text
EFECTIVO = 20.000
DEBITO   = 15.000
VISA     = RESTO
```

Distribución comercial calculada por ARD:

- Qué unidades o artículos se asignaron a cada condición.
- Qué unidad se fraccionó.
- Qué proporción se utilizó.
- Qué redondeos se aplicaron.
- Cuál fue el total final.

El cajero normalmente necesita ver la solicitud y los importes resultantes, no toda la complejidad interna.

## Explicabilidad

El motor debe generar junto al resultado una traza estructurada de resolución.

No debe devolver solamente un total.

La explicación debe poder contener:

- Solicitud de pago.
- Medios.
- Condiciones comerciales.
- Artículos.
- Unidades.
- Precios efectivos utilizados.
- Asignaciones completas.
- Fracciones.
- Relaciones de conversión.
- Importes antes y después de redondeo cuando corresponda.
- Redondeos.
- Resultado por medio.
- Total final.
- Criterio de selección.

La explicación debe representar exactamente la decisión tomada.

No debe reconstruirse en el futuro recalculando con precios actuales.

## Futuro frontend: explicación para cajero y cliente

La pantalla de cobro futura debe ofrecer un recurso opcional:

```text
¿Cómo se calculó?
```

El cajero podrá abrir un detalle entendible.

También debe quedar prevista la posibilidad de:

```text
Imprimir detalle
```

La finalidad es que un cliente minucioso pueda recibir el análisis del cálculo sin que el cajero tenga que explicar manualmente toda la distribución.

El detalle imprimible debe utilizar la traza histórica de la resolución, no recalcular la venta.

## Simulación reversible

Mientras no se haya confirmado el cobro:

- Agregar artículo recalcula.
- Quitar artículo recalcula.
- Modificar cantidad recalcula.
- Cambiar medio recalcula.
- Cambiar importe recalcula.
- Agregar medio recalcula.
- Quitar medio recalcula.
- Cambiar cuál es `RESTO` recalcula.

Las simulaciones previas dejan de estar vigentes.

## Confirmar cobro

Estados conceptuales:

```text
ABIERTA
  ->
EN_PAGO
  ->
CONFIRMAR COBRO
  ->
CERRADA
```

Confirmar cobro es el punto de no retorno.

Una vez `CERRADA`, la venta es inmutable.

Quedan congelados históricamente:

- Artículos.
- Cantidades.
- Precios.
- Condiciones comerciales.
- Medios de pago.
- Importes.
- Distribución.
- Fracciones.
- Redondeos.
- Total.
- Explicación/traza de decisión.

Una modificación posterior de precios o reglas comerciales no altera la venta histórica.

## Error después de confirmar

No se edita una venta `CERRADA`.

Si existe un error después del cierre:

- La venta debe anularse mediante una operación explícita.
- Debe generarse una nueva venta correcta.

La venta original debe permanecer trazable.

La implementación completa de anulación o devolución no pertenece al Sprint 8 salvo infraestructura mínima indispensable.

No debe diseñarse edición de ventas cerradas como alternativa.

## Atomicidad y offline-first

Confirmar cobro debe ser una operación local y atómica.

No puede existir:

- Venta cerrada con pagos incompletos.
- Pagos confirmados con venta abierta.
- Snapshot comercial parcialmente persistido.

O se confirma todo o no se confirma nada.

La operación debe depender de la base local y no de Internet ni de la nube.

Se mantienen los principios offline-first existentes de ARD Suite.

## Inventario

No debe romperse el mecanismo existente del Sprint 6.

La confirmación de venta debe continuar integrándose con `EventoPendiente`, `InventoryService` y la idempotencia ya existente.

Responsabilidades:

- Motor comercial: cuánto corresponde cobrar.
- Inventario: qué stock debe moverse.

No deben realizarse movimientos de stock directos desde el motor comercial.

## Snapshot histórico

La resolución confirmada debe conservar suficiente información para que el resultado pueda entenderse posteriormente aunque cambien:

- `PrecioArticulo`.
- Reglas de `PRECIO_2` / `PRECIO_3`.
- Relaciones entre medios y condiciones.
- Configuración de redondeo.

La venta histórica nunca debe depender de recalcular con la configuración actual.

## QA funcional previsto

Casos obligatorios:

1. Venta completa con condición `BASE`.
2. Venta completa con medio asociado a `PRECIO_2`.
3. Consultar Visa sin modificar ni persistir la venta.
4. 40.000 contado + `RESTO` Visa.
5. 40.000 Visa + `RESTO` contado.
6. Tres medios: efectivo + débito + `RESTO` Visa.
7. Más de tres medios usando el mismo algoritmo.
8. Varias combinaciones posibles y elección de menor costo.
9. Varias unidades del mismo artículo.
10. Asignación de unidades completas.
11. Necesidad de fraccionar una unidad.
12. Conversión entre dos condiciones no `BASE`.
13. Redondeo exacto a múltiplos de `0,05` hacia arriba.
14. Recalcular después de modificar un importe.
15. Recalcular después de agregar un artículo.
16. Recalcular después de cambiar medio.
17. Rechazar dos `RESTO`.
18. Rechazar condición o precio inexistente.
19. Explicación estructurada coherente con el resultado.
20. Confirmación atómica.
21. Intentar modificar venta `CERRADA` debe rechazarse.
22. Cambio posterior de precios no modifica la venta histórica.
23. Cambio posterior de asociación medio/condición no modifica la venta histórica.
24. Confirmar que inventario continúa usando el mecanismo existente.
25. Determinismo: misma entrada produce la misma distribución.

## Decisiones asociadas

| Código | Decisión |
|---|---|
| DAT-POS-001 | `MedioPago` y `CondicionComercialPrecio` son conceptos separados. |
| DAT-POS-002 | Toda venta nueva inicia valorizada con la condición comercial `BASE`. |
| DAT-POS-003 | La consulta o simulación comercial no persiste snapshot ni pagos definitivos. |
| DAT-POS-004 | El futuro POS podrá usar una condición o medio de visualización reversible durante la carga. |
| DAT-POS-005 | Una distribución de pagos admite múltiples medios y como máximo un `RESTO`. |
| DAT-POS-006 | El mismo algoritmo debe resolver pagos simples, mixtos y N medios. |
| DAT-POS-007 | La resolución debe minimizar el costo final para el cliente respetando los importes solicitados. |
| DAT-POS-008 | La unidad física se prioriza antes del fraccionamiento monetario. |
| DAT-POS-009 | La conversión proporcional entre condiciones es simétrica y usa `Decimal`. |
| DAT-POS-010 | El redondeo monetario de cobro sube al siguiente múltiplo configurable de `0,05`. |
| DAT-POS-011 | La resolución debe generar una traza estructurada explicable. |
| DAT-POS-012 | La venta confirmada conserva snapshot histórico completo de la resolución. |
| DAT-POS-013 | Una venta `CERRADA` es inmutable. |
| DAT-POS-014 | Un error posterior al cierre se corrige mediante anulación explícita y nueva venta. |
| DAT-POS-015 | Confirmar cobro es una operación local y atómica. |
| DAT-POS-016 | El motor comercial no mueve stock y conserva el mecanismo de inventario existente. |

## Referencias relacionadas

- [Sprint 6 — Motor de Venta Local](/doc/modulos/venta_salon/sprint_6_motor_venta_local).
- [Sprint 7 — Motor Comercial de Precios](/doc/modulos/venta_salon/sprint_7_motor_comercial_precios).
- [Medios de pago y condiciones comerciales](/doc/modulos/venta_salon/medios_pago).
- [Pagos mixtos](/doc/modulos/venta_salon/pagos_mixtos).
- [Modelo de Datos](/doc/modelo_datos/documento_maestro).
- [Registro de Decisiones](/doc/referencias/decisiones_agrupadas).

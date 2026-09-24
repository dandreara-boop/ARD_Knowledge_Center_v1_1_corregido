# Sprint 8 — Resolución Comercial y Cobro del POS

## Estado

DISEÑO COMERCIAL DEFINIDO / SOLVER SELECCIONADO Y PROBADO PRELIMINARMENTE / IMPLEMENTACIÓN DEFINITIVA PENDIENTE.

Sprint 8 no se documenta como implementado ni validado por QA.

El Sprint 8 no está cerrado todavía.

Estado operativo:

- Diseño comercial definido.
- Solver seleccionado y probado preliminarmente.
- Implementación definitiva pendiente.
- QA definitivo pendiente.
- Migración `0007` todavía no aplicada.
- Sin commit/push final de Sprint 8.

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
- Cero o un medio marcado como `RESTO`.
- Importes fijos desde cualquier condición.
- Resolución favorable al cliente.
- Asignación por unidades físicas.
- Fraccionamiento proporcional.
- Conversión simétrica entre condiciones.
- Uso de `Decimal`.
- Redondeo comercial final por medio hacia arriba a `0,05`, conceptualmente configurable.
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

## RESTO

Una distribución de pagos puede contener:

- Cero medios marcados como `RESTO`.
- Un medio marcado como `RESTO`.

Nunca puede contener más de un `RESTO`.

Con `RESTO`, los medios fijos deben respetarse y `RESTO` absorbe la parte calculada.

Sin `RESTO`, puede haber múltiples medios con importes fijos. La operación es válida si existe una distribución comercial que satisface esos importes y cubre completamente las unidades.

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

## Orden de los medios

El orden de los medios recibido en el request no tiene prioridad comercial.

Reordenar:

```text
EFECTIVO
VISA
TRANSFERENCIA
```

como:

```text
TRANSFERENCIA
EFECTIVO
VISA
```

no debe cambiar el óptimo económico.

Debe existir un criterio canónico interno para desempates.

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
2. Obtener el menor total final cobrado al cliente, evaluado después del redondeo comercial final por medio.
3. Entre soluciones con el mismo total final, usar menos unidades físicas fraccionadas entre medios.
4. Ante soluciones todavía equivalentes, utilizar un criterio determinista.

La misma entrada debe producir siempre la misma solución.

No se definen objetivos separados como "maximizar unidades completas" y "minimizar unidades fraccionadas".

El contrato funcional es único: menor total final, luego menor fraccionamiento físico, luego desempate determinista.

Ejemplo:

```text
22.000,01 -> 22.000,05
22.000,04 -> 22.000,05
```

Ambas alternativas tienen el mismo costo comercial final. En ese caso se prefiere la alternativa con menos fracciones físicas; si persiste el empate, decide el criterio determinista.

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

Los cálculos internos de conversión, prorrateo, proporción y subtotales por medio deben conservar precisión suficiente.

No se redondean fragmentos internos individualmente.

## Modelo matemático

La parte monetaria de la resolución comercial se modela principalmente como programación lineal continua.

Conceptualmente:

```text
x[u,m] >= 0
sum_m x[u,m] = 1
v[u,m] = precio[u,m] * x[u,m]
V[m] = sum_u v[u,m]
```

Donde:

- `u` representa una unidad física vendible.
- `m` representa un medio de pago.
- `x[u,m]` representa la proporción de la unidad `u` asignada al medio `m`.
- `v[u,m]` representa el valor comercial de esa proporción bajo el precio efectivo del medio.
- `V[m]` representa el subtotal interno calculado para el medio.

Los medios con importe fijo deben satisfacer el importe solicitado.

Cuando existe `RESTO`, el medio `RESTO` absorbe la parte calculada después de respetar los medios fijos.

La decisión de minimizar unidades físicas fraccionadas incorpora variables discretas o binarias. La formulación completa, al considerar ese criterio, es MILP.

## Solver elegido

El solver elegido para la implementación definitiva es HiGHS mediante Python `highspy`.

Motivos:

- Resuelve LP y MILP.
- Funciona localmente y sin depender de Internet.
- Es compatible con el principio offline-first.
- Tiene disponibilidad para Windows y Linux a nivel de paquete/distribución.
- En pruebas preliminares mostró tiempos suficientes para los escenarios evaluados.
- Entrega óptimos globales, evitando depender de un algoritmo comercial a medida difícil de auditar.

HiGHS es una dependencia técnica, no un concepto del dominio.

Debe quedar encapsulado detrás de esta estructura:

```text
CommercialResolutionService
    -> CommercialOptimizer
        -> HighsCommercialOptimizer
```

`Venta`, `Pricing`, `Inventario`, routers y endpoints no deben depender directamente de `highspy`.

## Representación monetaria y double

ARD Suite usa `Decimal` y dos decimales en límites de negocio y persistencia.

HiGHS opera internamente con `double`, por lo que no se asume exactitud decimal absoluta dentro del solver.

La integración definitiva debe:

- Preparar coeficientes numéricos de forma controlada.
- Evitar `float` dispersos fuera del adaptador técnico.
- Centralizar la adaptación numérica dentro de `HighsCommercialOptimizer`.
- Reconstruir la solución del solver.
- Validar la solución reconstruida con `Decimal`.
- Rechazar la confirmación si la solución no supera la validación de negocio.

Las tolerancias definitivas todavía no están aprobadas.

## Redondeo monetario

Decisión aprobada:

- Precisión visible/monetaria: 2 decimales.
- Incremento de redondeo comercial final: `0,05`.
- Redondeo siempre hacia arriba al siguiente múltiplo de `0,05`.
- Utilizar `Decimal`.
- No utilizar `float`.

El redondeo comercial se aplica solamente sobre el importe final calculado para cada medio de pago.

Los fragmentos internos no se redondean individualmente.

Primero se obtiene el subtotal interno por medio con precisión suficiente. Después se aplica el redondeo comercial final.

Los importes fijos cargados por el cliente o por el cajero se respetan sin alterarlos por redondeo.

Ejemplos:

```text
10,00  -> 10,00
10,01  -> 10,05
10,03  -> 10,05
10,05  -> 10,05
10,051 -> 10,10
```

El incremento `0,05` debe quedar conceptualmente configurable y no enterrado como una constante de negocio imposible de cambiar.

Este redondeo de pagos mixtos es una política monetaria del cobro, aunque sigue el criterio de redondeo hacia arriba ya existente en el motor comercial.

## Centavos

ARD usa `Decimal` y dos decimales en los bordes de negocio y persistencia.

Las pequeñas diferencias de centavos no son la estrategia principal de resolución comercial.

El incremento `0,05` pertenece a la política de redondeo final de cobro.

No debe usarse `0,05` para discretizar fracciones internas de artículos.

No debe diseñarse una programación dinámica monetaria masiva por ticks de `0,05`.

## Precios efectivos

Cada medio de pago referencia una condición comercial.

La resolución usa los precios efectivos ya almacenados en `PrecioArticulo` para la condición correspondiente.

El origen del precio puede ser `REGLA`, `MANUAL` u otro origen vigente del motor comercial.

Los precios pueden ser no proporcionales entre condiciones.

El optimizador no debe inferir porcentajes ni reconstruir reglas del Sprint 7. Debe consumir precios efectivos.

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
- Origen de precios cuando corresponda.
- Importes fijos solicitados.
- Asignaciones completas.
- Fracciones.
- Fracciones internas.
- Relaciones de conversión.
- Valores internos antes de redondeo.
- Subtotal interno por medio.
- Ajuste de redondeo final.
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

Antes de confirmar, la implementación debe reconstruir y validar con `Decimal`:

- Importes fijos solicitados.
- Cobertura completa de unidades.
- Regla de cero o un `RESTO`.
- Redondeo comercial final por medio.
- Total final.
- Coherencia de la traza.

Una solución del solver que no supera estas validaciones no puede confirmar la venta.

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

El snapshot mínimo debe conservar:

- Medios.
- Condiciones comerciales.
- Precios efectivos.
- Origen de precios cuando corresponda.
- Importes fijos solicitados.
- Unidades completas asignadas.
- Unidades fraccionadas.
- Fracciones internas.
- Valores internos antes de redondeo.
- Subtotal interno por medio.
- Ajuste de redondeo final.
- Importe final por medio.
- Total final.
- Criterio de selección.

## Sin límite arbitrario de ticket

No se aprueba un límite arbitrario de cantidad de ítems o unidades por ticket para Sprint 8.

Las pruebas preliminares hasta 100 unidades son una señal técnica inicial, no un SLA.

Si aparecen problemas de performance durante implementación o QA, deben medirse y documentarse antes de introducir restricciones, heurísticas o fallbacks.

No debe haber heurísticas silenciosas.

## Oráculo de tests

La implementación productiva con HiGHS debe validarse contra un oráculo independiente para casos pequeños.

El oráculo no debe reutilizar el optimizador productivo.

Debe evaluar escenarios exhaustivos pequeños y verificar:

- Factibilidad.
- Menor total final.
- Menor fraccionamiento entre soluciones equivalentes.
- Determinismo.
- Independencia del orden de medios.
- Casos con `RESTO`.
- Casos sin `RESTO`.
- Precios `MANUAL`.
- Precios no proporcionales.

## Dependencia formal

`highspy` todavía no está formalmente incorporado al repositorio de implementación ni a `requirements`.

La prueba técnica usó un entorno virtual temporal.

La incorporación formal queda para la implementación definitiva:

- Fijar versión compatible.
- Validar Windows.
- Validar Linux.
- Validar CI.
- Registrar dependencia y motivo.

## Windows y Linux

ARD Suite debe poder correr al menos en Windows y Linux.

El motor de resolución comercial no debe depender de características exclusivas de Windows.

La prueba técnica de `highspy` se realizó en Windows.

La disponibilidad en Linux fue verificada a nivel de paquete/distribución, pero ARD Suite con esta integración todavía no fue validado en Linux.

Antes de declarar cerrado el soporte multiplataforma de Sprint 8 debe existir validación automatizada o CI.

## Prueba técnica realizada

El 24/09/2026 se realizó una prueba aislada en Windows con:

- Python `3.13.3`.
- `highspy` `1.15.1`.
- HiGHS `1.15.1`.

Resultados preliminares:

- LP básico correcto.
- MIP básico correcto.
- Caso A/B/C: solución óptima `C -> EFECTIVO`, `A+B -> VISA`, total `64.000`.
- Caso fraccional: total `62.000`.
- Caso multimedio con reordenamiento: ambos órdenes total `63.533,35`, confirmando independencia del orden del request.

Estos resultados seleccionan técnicamente HiGHS como solver, pero no cierran implementación ni QA final.

## Benchmark preliminar

Mediciones sintéticas en entorno Windows de desarrollo:

| Escenario | Variables | Restricciones | Tiempo aprox. |
|---|---:|---:|---:|
| 10 unidades / 2 medios | 40 | 31 | 0,0097 s |
| 30 unidades / 3 medios | 180 | 122 | 0,0113 s |
| 50 unidades / 4 medios | 400 | 253 | 0,0153 s |
| 100 unidades / 4 medios | 800 | 503 | 0,0199 s |

Estos datos son preliminares y no constituyen SLA.

## Historial de decisión técnica

Evolución de la decisión:

- Se evaluó inicialmente una estrategia greedy.
- Se detectó dependencia del orden de medios y ausencia de garantía de óptimo global.
- Se exploró búsqueda exacta.
- Se detectó el problema de redondear fragmentos internos.
- Se revisó la regla: no se redondean fragmentos internos.
- Se consolidó redondeo final por subtotal de medio.
- El problema monetario se formuló como LP, con MILP cuando se agrega minimización de unidades fraccionadas.
- Se evaluó HiGHS vía `highspy`.
- Las pruebas preliminares resultaron correctas.
- Se seleccionó HiGHS como solver técnico para implementación definitiva.

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
13. Redondeo final por medio a múltiplos de `0,05` hacia arriba.
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
26. Independencia del orden de medios en el request.
27. Caso sin `RESTO` con varios importes fijos.
28. Validación con precios `MANUAL`.
29. Validación con precios no proporcionales.
30. Validación Decimal de la solución reconstruida.
31. Comparación contra oráculo independiente para escenarios pequeños.

## Decisiones asociadas

| Código | Decisión |
|---|---|
| DAT-POS-001 | `MedioPago` y `CondicionComercialPrecio` son conceptos separados. |
| DAT-POS-002 | Toda venta nueva inicia valorizada con la condición comercial `BASE`. |
| DAT-POS-003 | La consulta o simulación comercial no persiste snapshot ni pagos definitivos. |
| DAT-POS-004 | El futuro POS podrá usar una condición o medio de visualización reversible durante la carga. |
| DAT-POS-005 | Una distribución de pagos admite múltiples medios y cero o un `RESTO`. |
| DAT-POS-006 | El mismo algoritmo debe resolver pagos simples, mixtos y N medios. |
| DAT-POS-007 | La resolución debe minimizar el costo final para el cliente respetando los importes solicitados. |
| DAT-POS-008 | La unidad física se prioriza antes del fraccionamiento monetario. |
| DAT-POS-009 | La conversión proporcional entre condiciones es simétrica y usa `Decimal`. |
| DAT-POS-010 | El redondeo monetario de cobro se aplica sólo al importe final calculado por medio y sube al siguiente múltiplo configurable de `0,05`. |
| DAT-POS-011 | La resolución debe generar una traza estructurada explicable. |
| DAT-POS-012 | La venta confirmada conserva snapshot histórico completo de la resolución. |
| DAT-POS-013 | Una venta `CERRADA` es inmutable. |
| DAT-POS-014 | Un error posterior al cierre se corrige mediante anulación explícita y nueva venta. |
| DAT-POS-015 | Confirmar cobro es una operación local y atómica. |
| DAT-POS-016 | El motor comercial no mueve stock y conserva el mecanismo de inventario existente. |
| DAT-POS-017 | Los fragmentos internos no se redondean individualmente; se conserva precisión suficiente hasta el subtotal por medio. |
| DAT-POS-018 | Los importes fijos ingresados por cliente o cajero se respetan sin alterarlos por redondeo. |
| DAT-POS-019 | La resolución monetaria se modela como LP y, al minimizar unidades fraccionadas, como MILP. |
| DAT-POS-020 | HiGHS mediante `highspy` es el solver técnico elegido para la implementación definitiva. |
| DAT-POS-021 | `highspy` debe quedar encapsulado detrás de `CommercialOptimizer`; dominio, routers y endpoints no dependen directamente del solver. |
| DAT-POS-022 | La solución del solver debe reconstruirse y validarse con `Decimal` antes de permitir la confirmación. |
| DAT-POS-023 | El orden de medios del request no tiene prioridad comercial; los desempates usan criterio canónico interno. |
| DAT-POS-024 | El optimizador usa precios efectivos de `PrecioArticulo` y no reconstruye reglas del Sprint 7. |
| DAT-POS-025 | No se aprueban límites arbitrarios de ticket sin medición y documentación previas. |
| DAT-POS-026 | La implementación productiva debe compararse contra un oráculo independiente en escenarios pequeños. |
| DAT-POS-027 | ARD debe soportar Windows y Linux; la integración Linux de Sprint 8 queda pendiente de validación automatizada. |
| DAT-POS-028 | `highspy` queda pendiente de incorporación formal, pin de versión y validación CI durante implementación. |

## Referencias relacionadas

- [Sprint 6 — Motor de Venta Local](/doc/modulos/venta_salon/sprint_6_motor_venta_local).
- [Sprint 7 — Motor Comercial de Precios](/doc/modulos/venta_salon/sprint_7_motor_comercial_precios).
- [Medios de pago y condiciones comerciales](/doc/modulos/venta_salon/medios_pago).
- [Pagos mixtos](/doc/modulos/venta_salon/pagos_mixtos).
- [Modelo de Datos](/doc/modelo_datos/documento_maestro).
- [Registro de Decisiones](/doc/referencias/decisiones_agrupadas).

# Sprint 7 — Motor Comercial de Precios

## Estado

Sprint 7 implementado y validado funcionalmente.

El Sprint 7 implementó el motor comercial de precios a nivel de Artículo.

El objetivo es administrar condiciones comerciales de precio, precios por artículo, recálculos controlados y auditoría de cambios efectivos sin incorporar todavía promociones, pagos mixtos, caja ni canales externos.

## Alcance implementado

Sprint 7 documenta como existentes:

- `CondicionComercialPrecio`.
- `PrecioArticulo`.
- `AuditoriaPrecioArticulo`.
- Precio perteneciente al Artículo, no a la Variante.
- Condición `BASE`.
- Condiciones `DERIVADAS`.
- Reglas Python tipadas.
- Precio con origen `REGLA` o `MANUAL`.
- Recálculo automático por cambio individual de precio base.
- Preview de cambios generales de reglas.
- Aplicación explícita de recálculo masivo.
- Políticas para precios manuales.
- Auditoría de cambios efectivos.

No se documentan como implementados en este sprint:

- Frontend.
- Promociones.
- Clientes.
- Precios específicos por cliente.
- Bancos.
- Tarjetas.
- Cuotas.
- Motor completo de medios de pago.
- Optimizador de pagos mixtos.
- Prorrateo de pagos mixtos.
- Caja.
- Arqueo.
- Sincronización cloud.
- Tiendanube/e-commerce.

## Modelo comercial de precios

### Precio por Artículo

El precio comercial pertenece al Artículo.

La Variante no define un precio independiente en este sprint.

Las ventas históricas continúan conservando `precio_unitario` como snapshot. Modificar precios actuales no altera ventas anteriores.

### Condiciones comerciales

Ejemplo conceptual:

- `PRECIO_1` — `BASE`.
- `PRECIO_2` — derivado de `PRECIO_1`.
- `PRECIO_3` — derivado de `PRECIO_1`.

Las reglas pertenecen a la condición comercial, no individualmente a cada artículo.

## Reglas tipadas

Tipos iniciales implementados:

- `INCREMENTO_PORCENTUAL`.
- `DESCUENTO_PORCENTUAL`.

No existe lenguaje libre de fórmulas.

No se usa:

- `eval`.
- Expresiones arbitrarias.
- DSL dinámico.

La lógica se implementa mediante reglas Python tipadas y controladas.

## Redondeo

Tipos de redondeo implementados:

- `SIN_REDONDEO`.
- `ENTERO`.
- `MULTIPLO`.

Para `MULTIPLO` existe `multiplo_redondeo`.

La implementación validada utiliza `ROUND_CEILING`, es decir, redondeo hacia el siguiente múltiplo comercial.

Ejemplo probado:

```text
PRECIO_1 = 9.990

Regla PRECIO_2:
+10 %

Resultado matemático:
10.989

Con múltiplo 100:
PRECIO_2 = 11.000
```

Los cálculos monetarios utilizan `Decimal`.

## Cambio individual del precio base

Cuando cambia el precio `BASE` de un artículo:

1. Se actualiza el precio `BASE`.
2. Se recalculan automáticamente sus precios derivados activos.
3. Los derivados se calculan con las reglas vigentes.
4. Si un precio derivado tenía origen `MANUAL`, el cambio individual del `BASE` elimina ese override.
5. El derivado vuelve a origen `REGLA`.
6. La operación es atómica.

Caso validado:

```text
P1 = 9.990
P2 manual = 10.500

Cambio:
P1 = 12.000

Resultado:
P1 = 12.000 REGLA
P2 = 13.200 REGLA
```

El override manual anterior no se conserva en este flujo.

## Cambio general de una regla

El cambio general de una regla es distinto del cambio individual del precio base.

Ejemplo:

```text
PRECIO_2 cambia de:
P1 + 10 %

a:
P1 + 15 %
```

Modificar la configuración de la condición no recalcula silenciosamente todos los artículos.

El proceso implementado es controlado:

1. Modificar o configurar la regla.
2. Ejecutar preview.
3. Revisar impacto.
4. Aplicar explícitamente el recálculo con confirmación.

El preview no persiste cambios en `PrecioArticulo`.

Durante el intervalo entre modificar la definición de la regla y aplicar el recálculo pueden existir precios almacenados calculados con la regla anterior. El recálculo masivo es un proceso explícito de mantenimiento.

Esta característica es parte del diseño validado.

## Preview

El preview informa:

- Artículos afectados.
- Cantidad de precios con origen `REGLA`.
- Cantidad de precios con origen `MANUAL`.
- Artículo.
- Precio actual.
- Precio propuesto.
- Origen actual.

Caso QA real:

Artículo 2:

- `P1 = 12.000`.
- `P2 actual = 13.200 REGLA`.
- `P2 propuesto con +15 % = 13.800`.

Artículo 3:

- `P1 = 10.000`.
- `P2 actual = 10.700 MANUAL`.
- `P2 propuesto con +15 % = 11.500`.

Preview:

- Artículos afectados = 2.
- Precios `REGLA` = 1.
- Precios `MANUAL` = 1.

El preview no modificó los precios almacenados.

## Políticas de precios manuales

### CONSERVAR_MANUALES

Al aplicar un recálculo general:

- Precios `REGLA` se recalculan.
- Precios `MANUAL` se conservan.

QA validado:

```text
Artículo 2:
13.200 REGLA -> 13.800 REGLA

Artículo 3:
10.700 MANUAL -> 10.700 MANUAL
```

Resultado:

- Artículos afectados = 2.
- Precios actualizados = 1.
- Manuales conservados = 1.

### APLICAR_REGLA_A_TODOS

La regla se aplica también a precios `MANUAL`.

El precio deja de ser excepción y vuelve a `REGLA`.

QA validado:

```text
Artículo 3:
10.700 MANUAL -> 11.500 REGLA
```

### REVISAR_EXCEPCIONES

`REVISAR_EXCEPCIONES` puede estar reservado conceptualmente o contractualmente.

No se documenta como funcionalidad operativa implementada en Sprint 7 cuando el backend la rechaza.

## Auditoría

`AuditoriaPrecioArticulo` conserva como mínimo:

- Artículo.
- Condición comercial.
- Precio anterior.
- Precio nuevo.
- Origen anterior.
- Origen nuevo.
- Motivo.
- Usuario opcional.
- Timestamp.

Motivos implementados:

- `CREACION`.
- `CAMBIO_BASE`.
- `MODIFICACION_MANUAL`.
- `RECALCULO_REGLA`.
- `CAMBIO_REGLA_MASIVO`.

Regla final validada:

Sólo se considera una modificación efectiva si cambia:

- `precio`, o
- `origen`.

Por lo tanto:

```text
13800 REGLA -> 13800 REGLA
```

No:

- Actualiza el registro.
- Modifica `updated_at`.
- Genera auditoría.
- Incrementa `precios_actualizados`.

Pero:

```text
11500 MANUAL -> 11500 REGLA
```

Sí:

- Actualiza el origen.
- Modifica `updated_at`.
- Genera auditoría.
- Incrementa `precios_actualizados`.

Esta regla fue incorporada después de detectar durante QA registros de auditoría sin cambios efectivos.

Los registros históricos generados antes de la corrección pueden permanecer en la base de desarrollo. No representan el comportamiento final del motor.

## Persistencia

Tablas implementadas:

- `condiciones_comerciales_precio`.
- `precios_articulo`.
- `auditoria_precios_articulo`.

`precios_articulo` mantiene unicidad conceptual por:

```text
Artículo + Condición comercial
```

Sólo puede existir una condición `BASE` activa según validación de servicio.

La decisión de validarlo en servicio, y no mediante una restricción parcial específica de base de datos, busca compatibilidad con MariaDB.

## Migración

Migración implementada:

```text
20260917_0006_pricing_engine.py
```

`down_revision`:

```text
20260908_0005
```

No se modifican migraciones anteriores.

## API implementada

```text
POST /api/precios/condiciones
GET /api/precios/condiciones
GET /api/precios/condiciones/{condicion_id}
PUT /api/precios/condiciones/{condicion_id}

GET /api/precios/articulos/{articulo_id}
PUT /api/precios/articulos/{articulo_id}/base
PUT /api/precios/articulos/{articulo_id}/manual
GET /api/precios/articulos/{articulo_id}/condiciones/{condicion_id}

POST /api/precios/condiciones/{condicion_id}/recalculo/preview
POST /api/precios/condiciones/{condicion_id}/recalculo/aplicar
```

## Errores comerciales implementados

- `PRICE_CONDITION_NOT_FOUND`.
- `PRICE_CONDITION_INACTIVE`.
- `PRICE_BASE_REQUIRED`.
- `PRICE_RULE_REQUIRED`.
- `PRICE_RULE_INVALID`.
- `PRICE_PERCENTAGE_INVALID`.
- `PRICE_ROUNDING_INVALID`.
- `PRICE_CIRCULAR_DEPENDENCY`.
- `ARTICLE_PRICE_NOT_FOUND`.
- `ARTICLE_PRICE_INVALID`.
- `PRICE_MANUAL_OVERRIDE_INVALID`.
- `PRICE_RECALCULATION_POLICY_REQUIRED`.

## Tests automáticos

Comando utilizado:

```text
python -m pytest -p no:cacheprovider
```

Resultado final:

- 66 passed.

Se utiliza `-p no:cacheprovider` por el problema conocido de permisos con `.pytest_cache` en el entorno Windows.

El QA automático y manual cubrió como mínimo:

- Creación de condición `BASE`.
- Creación de condición `DERIVADA`.
- Incremento porcentual.
- Redondeo por múltiplo.
- Cambio de precio base.
- Generación automática de derivados.
- Override manual.
- Regeneración de manual a `REGLA` al cambiar `BASE`.
- Modificación de regla sin recálculo silencioso.
- Preview sin persistencia.
- Identificación de `REGLA`/`MANUAL`.
- `CONSERVAR_MANUALES`.
- `APLICAR_REGLA_A_TODOS`.
- Auditoría.
- Ausencia de auditoría cuando precio y origen no cambian.
- Auditoría cuando sólo cambia el origen.
- `precios_actualizados` contando cambios efectivos.

## Decisiones asociadas

| Código | Decisión |
|---|---|
| DAT-PRICE-001 | El precio comercial pertenece al Artículo, no a la Variante. |
| DAT-PRICE-002 | Las reglas pertenecen a condiciones comerciales y no a cada artículo. |
| DAT-PRICE-003 | El motor usa reglas Python tipadas y controladas, sin fórmulas libres. |
| DAT-PRICE-004 | Los cálculos monetarios utilizan `Decimal`. |
| DAT-PRICE-005 | Cambiar el precio `BASE` de un artículo recalcula derivados activos en forma atómica. |
| DAT-PRICE-006 | El cambio general de una regla requiere preview y aplicación explícita. |
| DAT-PRICE-007 | El preview no persiste cambios en `PrecioArticulo`. |
| DAT-PRICE-008 | La política frente a precios manuales se define explícitamente al aplicar recálculo masivo. |
| DAT-PRICE-009 | La auditoría de precios se genera sólo ante cambios efectivos de precio u origen. |
| DAT-PRICE-010 | Las ventas históricas conservan snapshot de precio y no se recalculan por cambios actuales. |
| DAT-PRICE-011 | La condición `BASE` activa única se valida en servicio por compatibilidad con MariaDB. |

## Referencias relacionadas

- [Módulo Venta en Salón](/doc/modulos/venta_salon/documento_maestro).
- [Modelo de Datos](/doc/modelo_datos/documento_maestro).
- [Promociones y precios en la venta](/doc/modulos/venta_salon/promociones).
- [Medios de pago y condiciones comerciales](/doc/modulos/venta_salon/medios_pago).
- [Registro de Decisiones](/doc/referencias/decisiones_agrupadas).

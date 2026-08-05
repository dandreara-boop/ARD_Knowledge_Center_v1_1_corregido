# Administración Central en la nube

## Definición

La aplicación de Administración será web, estará alojada en la nube y será accesible desde cualquier lugar por usuarios autorizados.

Las sucursales seguirán operando con bases locales. Sus datos se sincronizarán hacia una base central, y los informes administrativos se consultarán desde esa base central consolidada.

## Informes alcanzados

- Ventas.
- Stock.
- Caja.
- Arqueos.
- Cierres.
- Cambios.
- Créditos comerciales.
- Anulaciones.
- Remitos.
- Transferencias.
- Excepciones.
- Estado de sincronización.

## Datos obligatorios por informe

Cada informe debe mostrar:

- Fecha y hora de generación.
- Período consultado.
- Filtros aplicados.
- Si el resultado es consolidado o por sucursal.
- Última sincronización general.
- Última sincronización de cada sucursal involucrada.
- Sucursales con información pendiente o atrasada.

## Información parcial

Un informe puede contener información parcial si una sucursal no sincronizó. En ese caso el sistema debe indicarlo claramente y no presentar esos datos como completamente actualizados.

## Consulta operativa

Los informes deben priorizar tablas filtrables, trazabilidad hacia el comprobante o movimiento original y lectura clara de vigencia de datos. Los gráficos son opcionales y secundarios.

Ver también:

- Arquitectura Distribuida — Sincronización.
- Administración — Panel principal.
- DEC-118.
- DEC-123.

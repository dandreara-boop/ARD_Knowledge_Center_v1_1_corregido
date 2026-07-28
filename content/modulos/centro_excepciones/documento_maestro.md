# Centro de Excepciones

## Objetivo

Agrupar operaciones que requieren revisión, corrección, seguimiento o decisión administrativa.

## Ventas anuladas

Muestra operaciones anuladas con motivo, usuario, fecha, medios afectados, stock revertido y auditoría.

## Correcciones

Incluye correcciones de medios de pago, fondos iniciales, valores reconocidos, ajustes y modificaciones autorizadas.

## Stock negativo

Agrupa ventas locales que generaron stock negativo y deben revisarse en Administración.

## Errores de sincronización

Agrupa operaciones en estado ERROR_REINTENTABLE o REQUIERE_REVISION dentro de la cola de sincronización.

## Créditos

Permite revisar Créditos Comerciales emitidos, parcialmente utilizados, vencidos, anulados o asociados a clientes.

## Arqueos

Agrupa arqueos con diferencia, revisiones guiadas, cierres con diferencia y correcciones originadas en caja.

## Transferencias

Agrupa transferencias demoradas, incompletas, con diferencias o pendientes de confirmación.

## Alertas

Incluye alertas operativas y administrativas configurables por la empresa.

## Reglas

- Una excepción no borra la operación original.
- Toda resolución queda auditada.
- Las excepciones deben poder filtrarse por módulo, sucursal, fecha, usuario y estado.

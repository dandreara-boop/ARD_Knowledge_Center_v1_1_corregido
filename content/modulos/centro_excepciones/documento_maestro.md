# Centro de Excepciones

## Objetivo

Agrupar operaciones que requieren revisión, corrección, seguimiento o decisión administrativa.

El Centro de Excepciones concentra situaciones que requieren revisión administrativa sin interrumpir al cajero o vendedor.

## Categorías

### Caja

- Cierres con diferencia.
- Fondos iniciales corregidos.
- Cambios de medio de pago.
- Ventas anuladas.
- Movimientos de caja atípicos.
- Arqueos pendientes de revisión.

### Stock

- Ventas con stock negativo.
- Ajustes manuales.
- Diferencias de recepción.
- Mercadería pendiente.
- Transferencias con diferencia.

### Sincronización

- Operaciones pendientes demasiado tiempo.
- Errores repetidos.
- Conflictos.
- Sucursales sin actualizar.

### Créditos comerciales

- Créditos anulados.
- Modificaciones manuales.
- Uso sospechoso.
- Créditos vencidos.

## Estados

- PENDIENTE.
- EN_REVISION.
- RESUELTA.
- OBSERVADA.
- DESCARTADA.

## Datos conservados

Cada excepción debe conservar:

- Origen.
- Fecha y hora.
- Sucursal.
- Usuario.
- Importe o cantidad.
- Gravedad.
- Historial.
- Responsable de revisión.
- Resolución.

## Reglas

- Una excepción no borra la operación original.
- Una excepción no reemplaza el registro que la originó.
- Toda resolución queda auditada.
- Las excepciones deben poder filtrarse por módulo, sucursal, fecha, usuario y estado.

Ver también:

- Administración — Panel principal.
- Usuarios y Permisos.
- DEC-119.
- DEC-120.

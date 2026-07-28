# Usuarios y Permisos

## Objetivo

Definir cómo ARD Suite controla acceso, permisos, excepciones, autorizaciones y auditoría.

## Tipos de usuario

- Administrador general.
- Administración.
- Encargado de sucursal.
- Cajero.
- Operador de depósito o recepción.
- Usuario de consulta.

## Permisos configurables

Los permisos deben poder configurarse por rol y, cuando corresponda, por usuario individual.

## Excepciones

Las excepciones son operaciones que se apartan del flujo habitual y requieren trazabilidad o autorización.

## Autorizaciones

Una autorización registra usuario solicitante, usuario autorizante, acción, fecha, hora, motivo y resultado.

## Permisos individuales

Un usuario puede recibir permisos específicos sin modificar el rol base, siempre que quede auditado.

## Validación Backend

Toda acción sensible debe validarse en backend. La interfaz puede ocultar acciones, pero la seguridad no depende solamente del frontend.

## Auditoría

La auditoría conserva usuario, operación, entidad afectada, valor anterior, valor nuevo, motivo, fecha, hora y origen de la acción.

## Relación con módulos

- Recepción: creación o modificación de productos y cierre de remitos.
- Venta: modificaciones de valor reconocido y operaciones suspendidas.
- Cambios: emisión y uso de Crédito Comercial.
- Caja: correcciones, ajustes, cierres con diferencia y movimientos manuales.
- Administración: configuración global, usuarios y políticas.

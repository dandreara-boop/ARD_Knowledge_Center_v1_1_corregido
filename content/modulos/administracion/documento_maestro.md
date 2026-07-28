# Módulo Administración

## Objetivos

Administración concentra la configuración, control y seguimiento de la operación completa de ARD Suite.

{{include:modulos/administracion/resumen}}

## Panel principal

El panel principal debe permitir lectura rápida del estado operativo: ventas, stock, caja, excepciones, remitos, transferencias y alertas.

## Operación diaria

La operación diaria administra productos, precios, proveedores, clientes, usuarios, políticas globales, campañas, auditoría y centro de control.

## Informes

Los informes deben cubrir ventas, stock, caja, movimientos, promociones, clientes, proveedores, remitos y excepciones.

## Stock

Administración consulta stock local, stock web, movimientos y diferencias operativas.

## Productos

Administra catálogo, precios, atributos designados, canales, estado y reglas comerciales asociadas.

## Remitos

Administra Remitos de Entrada y Remitos de Venta, con su estado, participantes, movimientos y auditoría.

## Transferencias

Las transferencias conectan sucursales, depósito y stock web. El detalle conceptual se integra con Logística.

## Clientes

Administra clientes identificados, historial, créditos comerciales asociados y políticas aplicables.

## Proveedores

Administra proveedores asociados a productos y Remitos de Entrada.

## Promociones

Define campañas, promociones, condiciones comerciales, vigencias y reglas del motor comercial.

## Caja

Consulta turnos, arqueos, cierres, diferencias, movimientos manuales y correcciones auditables.

## Centro de excepciones

Agrupa operaciones que requieren revisión administrativa: ventas anuladas, correcciones, stock negativo, errores de sincronización, créditos, arqueos, transferencias y alertas.

## Usuarios

Administra usuarios locales y centrales, estado, rol y permisos.

## Permisos

Los permisos son configurables y deben validarse en backend.

## Seguridad

Toda acción sensible conserva auditoría. Las autorizaciones y excepciones deben quedar vinculadas al usuario que las ejecuta o aprueba.

## Configuración

Administración define políticas globales: promociones, condición comercial por medio de pago, cambios, Crédito Comercial, tolerancias de caja, vigencias y permisos.

## Casos especiales

- Correcciones fuera de tolerancia.
- Operaciones sincronizadas con error.
- Stock negativo generado por venta local.
- Crédito Comercial vencido o parcialmente utilizado.
- Usuarios con permisos individuales.

## Próximos desarrollos

- Detallar pantallas administrativas.
- Definir reportes mínimos por rol.
- Consolidar reglas de permisos y autorizaciones.
- Preparar indicadores del centro de excepciones.

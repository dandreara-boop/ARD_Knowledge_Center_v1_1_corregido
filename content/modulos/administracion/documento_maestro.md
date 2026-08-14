# Módulo Administración

## Estado

**APROBADO PARA DESARROLLO.**

Administración concentra la configuración, control y seguimiento de la operación completa de ARD Suite. Su pantalla inicial funciona como un centro de navegación orientado por frecuencia de uso: prioriza las consultas y controles diarios, y deja la configuración en segundo plano.

{{include:modulos/administracion/resumen}}

## Panel principal

El panel principal no abre directamente en Usuarios y Permisos. Debe mostrar primero los accesos administrativos más consultados y solamente indicadores accionables.

### Accesos frecuentes

- Informes de ventas.
- Informe de stock.
- Remitos de Entrada.

### Control diario

- Arqueos y cierres.
- Correcciones de caja.
- Centro de excepciones.
- Transferencias.
- Estado de sincronización.

### Gestión comercial

- Productos.
- Precios.
- Motor de Promociones.
- Clientes.
- Proveedores.

### Configuración

- Usuarios.
- Tipos de usuario y permisos.
- Sucursales y cajas.
- Medios de pago.
- Políticas comerciales.
- Tolerancias y límites.
- Configuración general.

## Indicadores de portada

La portada administrativa debe mostrar únicamente indicadores que permitan actuar:

- Pendientes de revisión.
- Cierres con diferencia.
- Remitos incompletos.
- Errores de sincronización.
- Sucursales con datos atrasados.
- Excepciones pendientes.

No se deben usar gráficos decorativos como contenido principal. Los gráficos pueden existir en informes puntuales, pero siempre como apoyo secundario frente a tablas filtrables y datos accionables.

## Operación diaria

Administración consulta ventas, stock, caja, remitos, transferencias, promociones, clientes, proveedores, excepciones y sincronización. La operación diaria debe estar separada de la configuración para evitar que tareas poco frecuentes ocupen la portada.

## Informes administrativos

Los informes administrativos se consultan desde la aplicación web de Administración alojada en la nube, contra una base central consolidada alimentada por sincronización desde las sucursales.

Ver también:

- [Administración — Informes administrativos desde la nube](/doc/modulos/administracion/informes_nube).
- [Arquitectura Distribuida](/doc/general/arquitectura_distribuida).
- [Módulo Sincronización](/doc/modulos/sincronizacion/documento_maestro).

## Administración Local

Administración Local permite consultar información propia de una sucursal aunque no haya Internet, usando la base local compartida de esa sucursal. No reemplaza a Administración Central: funciona como consulta operativa local para usuarios autorizados.

## Informe de ventas

Debe permitir filtrar por fecha desde y hasta, sucursal, cajero, vendedor, producto, categoría, proveedor, medio de pago, condición comercial, promoción y estado de la venta.

Resultados mínimos:

- Cantidad de ventas.
- Cantidad de unidades.
- Importe bruto.
- Descuentos.
- Importe final.
- Ventas anuladas.
- Cambios.
- Créditos emitidos.
- Créditos utilizados.
- Totales por medio de pago.

La vista principal prioriza tablas filtrables y acceso al remito de venta completo. Los gráficos son opcionales y secundarios.

## Informe de stock

Debe cubrir stock por sucursal, stock web, stock consolidado, stock negativo, mercadería pendiente de recepción, mercadería en tránsito, productos sin movimiento, productos con stock bajo, último movimiento y consulta por producto con atributos operativos.

El informe debe indicar la vigencia de los datos de cada sucursal y advertir cuando exista información pendiente o atrasada.

## Stock

Administración consulta stock local, stock web, movimientos y diferencias operativas. Los ajustes manuales e inventarios no pertenecen al alcance del módulo Logística.

## Productos

Administra catálogo, precios, atributos designados, canales, estado y reglas comerciales asociadas.

La participación en liquidaciones, campañas o promociones no se guarda como opción permanente del producto. El alcance se define dentro de cada promoción.

## Remitos

Administra Remitos de Entrada y Remitos de Venta, con su estado, participantes, movimientos y auditoría.

## Transferencias

Las transferencias conectan sucursales, depósito y stock web. El detalle de confirmación en destino y reposición posterior se integra con Logística.

## Clientes

Administra clientes identificados, historial, créditos comerciales asociados y políticas aplicables.

## Proveedores

Administra proveedores asociados a productos, reglas comerciales y Remitos de Entrada.

## Motor de Promociones

Define campañas, promociones, condiciones comerciales, vigencias, reglas de inclusión y exclusión, suspensión temporal de otras promociones y simulación previa.

Ver también:

- Administración — Motor de Promociones.
- Venta en Salón — Motor Comercial.
- DEC-124 a DEC-128.

## Caja

Consulta turnos, arqueos, cierres, diferencias, movimientos manuales y correcciones auditables.

## Centro de excepciones

Agrupa operaciones que requieren revisión administrativa sin interrumpir al cajero o vendedor: ventas anuladas, correcciones, stock negativo, errores de sincronización, créditos, arqueos, transferencias y alertas.

Ver también:

- Administración — Centro de Excepciones.
- DEC-119.
- DEC-120.

## Usuarios y permisos

Administra usuarios, tipos de usuario, permisos configurables, alcances, excepciones individuales y autorizaciones puntuales. Toda acción sensible debe validarse obligatoriamente en backend.

Ver también:

- Usuarios y Permisos.
- DEC-117.

## Seguridad

Toda acción sensible conserva auditoría. Las autorizaciones y excepciones deben quedar vinculadas al usuario que las ejecuta, solicita o aprueba.

## Configuración

Administración define políticas globales: promociones, condición comercial por medio de pago, cambios, Crédito Comercial, tolerancias de caja, límites, sucursales, cajas, usuarios y permisos.

## Casos especiales

- Correcciones fuera de tolerancia.
- Operaciones sincronizadas con error.
- Stock negativo generado por venta local.
- Crédito Comercial vencido o parcialmente utilizado.
- Usuarios con permisos individuales concedidos o denegados.
- Promociones suspendidas por otra promoción.
- Sucursales con datos atrasados en informes consolidados.

## Próximo módulo

Con Administración aprobada para desarrollo, Logística funcionalmente definida y Sincronización aprobada funcionalmente para desarrollo, el siguiente análisis corresponde al Modelo de Datos.

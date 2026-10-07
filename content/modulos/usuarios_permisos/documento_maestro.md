# Usuarios y Permisos

## Objetivo

Definir cómo ARD Suite controla acceso, permisos, excepciones, autorizaciones y auditoría.

## Estructura

Los roles no serán rígidos. La estructura funcional será:

```text
Usuario
  ↓
Tipo de usuario
  ↓
Permisos configurables
```

Los tipos de usuario funcionan como plantillas de permisos y pueden ajustarse sin modificar la identidad del usuario.

## Tipos de usuario iniciales

- Vendedor.
- Cajero.
- Supervisor.
- Administrador.
- Operario de recepción.
- Auditor.

La jerarquía funcional inicial para salón y caja es:

```text
VENDEDOR
  ↓
CAJERO
  ↓
SUPERVISOR
  ↓
ADMINISTRADOR
```

Los roles son agrupaciones de permisos, no lógica hardcodeada por nombre de rol. El cajero hereda funcionalmente capacidades de vendedor; el supervisor hereda capacidades de cajero; el administrador hereda capacidades de supervisor.

## Permisos configurables

Los permisos deben poder configurarse por rol y, cuando corresponda, por usuario individual.

### Venta

- Iniciar venta.
- Suspender venta.
- Recuperar ventas abiertas.
- Preparar venta para caja.
- Enviar venta a caja.
- Anular venta propia.
- Anular venta de otro usuario.
- Modificar cantidades.
- Modificar precios.
- Consultar ventas del mismo local según alcance.
- Aplicar crédito comercial.

### Cambios

- Iniciar cambio.
- Recibir varias prendas.
- Modificar valor reconocido.
- Emitir crédito comercial.
- Usar crédito comercial.
- Anular crédito comercial.

### Caja

- Abrir turno.
- Abrir sesión de caja con efectivo inicial declarado manualmente.
- Capturar venta lista para cobrar.
- Liberar venta capturada.
- Modificar venta capturada antes del cobro.
- Cobrar con sesión de caja válida.
- Verificar mercadería.
- Registrar ingresos de caja.
- Registrar retiros.
- Registrar egresos o pagos.
- Realizar arqueo.
- Revisar diferencias.
- Solicitar corrección de conteo durante el cierre inmediato.
- Marcar posible error de medio de pago.
- Anular desde la revisión.
- Cerrar con diferencia.

Tener permiso para cobrar no significa tener una caja abierta. Para cobrar también debe existir una sesión de caja válida. Un supervisor o administrador que cobre también necesita sesión de caja.

Tener permiso para registrar ingresos, retiros o egresos tampoco alcanza por sí solo: el movimiento debe registrarse sobre una `SesionCaja` abierta y propia del cajero responsable.

### Productos y stock

- Crear producto.
- Editar producto.
- Consultar costos.
- Modificar precios.
- Cargar remitos.
- Confirmar mercadería recibida.
- Transferir mercadería.
- Ajustar stock.
- Imprimir etiquetas.

### Administración

- Crear usuarios.
- Crear tipos de usuario.
- Configurar permisos.
- Revisar correcciones.
- Revisar solicitudes de corrección de arqueo.
- Resolver posibles errores de medio de pago mediante operación administrativa separada.
- Aprobar excepciones.
- Consultar auditoría.
- Configurar promociones.
- Configurar tolerancias.
- Modificar políticas comerciales.

### Logística

- Consultar stock de otros locales.
- Solicitar mercadería.
- Preparar solicitud.
- Modificar cantidad preparada.
- Confirmar despacho.
- Confirmar recepción.
- Registrar diferencia.
- Cancelar solicitud.
- Revisar excepciones logísticas.

## Excepciones individuales

Un usuario puede recibir excepciones individuales sin modificar el tipo de usuario base:

- CONCEDER.
- DENEGAR.

Toda excepción individual debe quedar auditada y visible para Administración.

## Alcance de permisos

Los permisos pueden limitarse por alcance:

- Solo su caja.
- Su sucursal.
- Todas las sucursales.
- Su turno.
- Operaciones del día.
- Límite de tiempo.
- Límite de importe.

## Excepciones

Las excepciones son operaciones que se apartan del flujo habitual y requieren trazabilidad o autorización.

## Autorizaciones

Una autorización puntual permite que un superior habilite una operación específica sin cambiar permisos permanentes.

Toda autorización registra:

- Usuario solicitante.
- Usuario autorizante.
- Operación.
- Motivo.
- Fecha y hora.
- Valores anteriores y nuevos.
- Resultado.

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
- Logística: solicitud, preparación, despacho, recepción y diferencias.

Ver también:

- Administración — Centro de Excepciones.
- DEC-117.

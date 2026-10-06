# Módulo Caja

## Objetivos

Registrar cobros, movimientos, arqueos y cierres de turno con velocidad operativa, control y auditoría.

## Apertura de turno

{{include:modulos/venta_salon/wf008_arqueo_caja}}

## Apertura obligatoria

Para cobrar debe existir una sesión de caja abierta y válida.

El efectivo inicial se declara manualmente en cada nueva sesión. No se hereda automáticamente el efectivo del cierre anterior.

Una caja no puede tener dos sesiones activas simultáneamente. La sesión queda ligada a una caja concreta durante toda su vida y no puede trasladarse a otra caja.

Si el cajero cambia de caja, debe cerrar la sesión actual, realizar arqueo, abrir una nueva sesión en la nueva caja y declarar manualmente el nuevo efectivo inicial.

## Ventas

La caja cobra ventas presenciales registradas primero localmente.

## Movimientos de caja

Todo ingreso o egreso ajeno a una venta se registra como movimiento explícito de caja.

## Ingresos

- Fondo inicial.
- Refuerzo de efectivo para cambio.

## Retiros

- Retiro de efectivo.
- Entrega o depósito de recaudación.

Un retiro mueve dinero fuera del cajón, requiere importe, usuario, sesión y fecha/hora. El motivo no es obligatorio, no necesita autorización previa del supervisor, reduce el efectivo esperado y no representa un gasto.

## Egresos / pagos

Los egresos o pagos se registran como salidas económicas explícitas, con importe, motivo obligatorio, usuario, sesión y fecha/hora. Reducen el efectivo esperado y se mantienen separados de los retiros.

## Ajustes

Los ajustes son correcciones excepcionales autorizadas.

## Arqueo ciego

El primer conteo de efectivo es ciego: el cajero no ve el importe esperado antes de confirmar.

## Corrección guiada

La revisión guiada permite detectar diferencias sin alterar silenciosamente ventas cerradas ni pagos históricos.

## Anulación desde arqueo

Si durante el arqueo se detecta una operación que debe anularse, la anulación debe conservar vínculo con el arqueo que originó la revisión.

## Posible error de medio de pago

Durante el cierre, el cajero puede revisar las operaciones de su sesión y marcar una o varias como posible error de medio de pago.

No necesita indicar en ese momento cuál sería el medio correcto. Se genera un pendiente de supervisión.

La venta `CERRADA` permanece inmutable. El supervisor investiga y, si corresponde, registra una corrección administrativa separada y auditable; nunca se edita silenciosamente `PagoVenta` ni la venta histórica.

## Cierre

El cierre finaliza formalmente el turno y registra efectivo real, diferencia, correcciones y observaciones.

## Cierre con diferencia

La caja puede cerrarse con diferencia documentada.

## Cambio de turno

Una corrección pendiente no bloquea el cierre. La sesión se cierra igualmente y el siguiente cajero puede abrir una nueva sesión de inmediato.

Principio: la operación del local no debe detenerse por controles administrativos pendientes.

## Casos especiales

- Arqueo de control sin cierre de turno.
- Diferencia dentro de tolerancia.
- Diferencia fuera de tolerancia.
- Solicitud de corrección de arqueo.
- Posible error de medio de pago.
- Cierre con diferencia.

## Decisiones

- DEC-078 a DEC-087 registran la decisión histórica de arqueo independiente del cierre, conteo ciego, tolerancia, revisión guiada, corrección auditable, cierre con diferencia, herencia del efectivo real y movimientos explícitos de caja.
- Sprint 9 reemplaza la herencia automática de efectivo por apertura manual obligatoria y reemplaza la corrección directa de medio de pago durante arqueo por pendientes de supervisión auditables.

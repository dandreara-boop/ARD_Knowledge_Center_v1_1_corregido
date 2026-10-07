# Módulo Caja

## Objetivos

Registrar cobros, movimientos, arqueos y cierres de turno con velocidad operativa, control y auditoría.

## Apertura de turno

{{include:modulos/venta_salon/wf008_arqueo_caja}}

## Apertura obligatoria

Para cobrar debe existir una sesión de caja abierta y válida.

El efectivo inicial se declara manualmente en cada nueva sesión. No se hereda automáticamente el efectivo del cierre anterior.

Una caja no puede tener dos sesiones activas simultáneamente. La sesión queda ligada a una caja concreta durante toda su vida y no puede trasladarse a otra caja.

La sesión no pertenece al dispositivo. Si una PC/tablet falla, el mismo cajero puede continuar la misma sesión desde otro dispositivo sin transferirla.

Un cajero puede tener más de una sesión abierta en cajas distintas. Al abrir una nueva sesión mientras ya tiene otra abierta, el sistema advierte, pero no bloquea.

Cuando un cajero tenga varias sesiones abiertas, la sesión activa para cobrar debe seleccionarse explícitamente. El sistema no debe elegir "cualquier sesión abierta".

## Ventas

La caja cobra ventas presenciales registradas primero localmente.

En el flujo nuevo de salón, una venta `EN_COBRO` queda ligada a `caja_captura_id` y `sesion_caja_id`. La confirmación exige `usuario_id`, sesión abierta correspondiente y cajero responsable de esa sesión.

## Movimientos de caja

Sprint 9.4 implementó movimientos operativos de efectivo durante una `SesionCaja`, reutilizando `MovimientoCaja` sin cambios de schema, sin migración y con movimientos append-only.

Todo ingreso, retiro o egreso/pago ajeno a una venta se registra como movimiento explícito de caja. Son conceptos diferentes y se conservan separados.

Los movimientos sólo pueden registrarse sobre una sesión `ABIERTA`. La Caja se deriva de la `SesionCaja`, y el cajero que registra el movimiento debe ser el responsable de esa sesión.

## Ingresos

- Fondo inicial.
- Refuerzo de efectivo para cambio.

Un ingreso agrega efectivo al cajón por una causa distinta de una venta. Requiere importe mayor a `0`, cajero, sesión y fecha/hora. El motivo es opcional. Aumenta el efectivo esperado, no genera `Venta`, no genera `PagoVenta` y no representa ingreso comercial por venta.

## Retiros

- Retiro de efectivo.
- Entrega o depósito de recaudación.

Un retiro mueve dinero fuera del cajón hacia otro lugar de resguardo. Requiere importe mayor a `0`, cajero, sesión y fecha/hora. El motivo no es obligatorio, no necesita autorización previa del supervisor, reduce el efectivo esperado y no representa gasto, pago a proveedor ni pérdida.

## Egresos / pagos

Los egresos o pagos se registran como salidas económicas explícitas, con importe mayor a `0`, motivo obligatorio, cajero, sesión y fecha/hora. Reducen el efectivo esperado y se mantienen separados de los retiros.

Sprint 9.4 no desarrolla todavía contabilidad ni cuenta corriente de proveedores. El movimiento registra la salida operativa de efectivo.

## Selección de sesión para movimientos

Si el cajero tiene una sola sesión abierta, la interfaz futura puede usar esa sesión directamente para `INGRESO`, `RETIRO` o `EGRESO/PAGO`.

Si el cajero tiene dos o más sesiones abiertas, la interfaz debe pedir explícitamente sobre cuál sesión/caja se registra el movimiento.

Esta simplificación pertenece sólo a la experiencia de usuario. El movimiento persistido siempre queda asociado a un `sesion_caja_id` concreto y no sólo al cajero.

No modifica la regla de cobro de Sprint 9.3: una venta capturada utiliza sesión explícita y no puede saltarse esa selección.

## Efectivo esperado

Fórmula conceptual para futuro arqueo:

```text
efectivo inicial
+ cobros de ventas realizados en EFECTIVO
+ movimientos INGRESO
- movimientos RETIRO
- movimientos EGRESO
= efectivo esperado en el cajón
```

El único `MedioPago` que mueve efectivo físico dentro del cajón es `EFECTIVO`. En pagos mixtos, sólo la porción cobrada con `EFECTIVO` incrementa el efectivo esperado.

No se identifica efectivo físico comparando el nombre visible del medio. El modelo deberá poseer una identificación explícita y estable del único medio que representa efectivo físico.

Transferencias, QR, tarjetas y otros medios electrónicos pertenecen a la información de la sesión, pero no al efectivo físico del cajón.

## Ajustes

Los ajustes son correcciones excepcionales autorizadas.

## Arqueo ciego

El primer conteo de efectivo es ciego: el cajero no ve el importe esperado antes de confirmar.

En el cierre de su `SesionCaja`, el cajero cuenta únicamente el efectivo físico que permanece en su cajón. No recupera retiros, no reúne dinero retirado previamente, no cuenta dinero guardado en caja fuerte y no cuenta fondos que ya dejaron físicamente su caja.

Los retiros registrados ya no forman parte del efectivo que debe contar el cajero. Permanecen registrados y auditables; el supervisor o encargado puede verificarlos posteriormente para investigar una diferencia.

Una diferencia de arqueo no implica automáticamente error, faltante o sobrante atribuible al cajero. Es una diferencia operativa que se conserva y puede investigarse.

## Corrección guiada

La revisión guiada permite detectar diferencias sin alterar silenciosamente ventas cerradas ni pagos históricos.

La posterior verificación de retiros puede aportar evidencia para una investigación o corrección administrativa, pero no reescribe el primer conteo histórico del cajero.

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
- Sprint 9.3 refina sesiones de caja: sesión independiente del dispositivo, responsable único, una sesión abierta por caja, varias sesiones abiertas por cajero en cajas distintas, advertencia no bloqueante, selección explícita de sesión y confirmación por cajero responsable.
- Sprint 9.4 implementa movimientos operativos de caja: `INGRESO`, `RETIRO`, `EGRESO/PAGO`, impacto en efectivo esperado, sesión abierta, responsable y trazabilidad.
- Sprint 9.5 documenta decisiones previas a implementación para efectivo físico, cierre y alcance del arqueo.

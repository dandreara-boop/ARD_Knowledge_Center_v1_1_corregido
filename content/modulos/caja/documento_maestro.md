# Módulo Caja

## Objetivos

Registrar cobros, movimientos, arqueos y cierres de turno con velocidad operativa, control y auditoría.

## Apertura de turno

{{include:modulos/venta_salon/wf008_arqueo_caja}}

## Fondo heredado

El turno recibe el efectivo real confirmado por el cierre anterior.

## Corrección del fondo

El cajero puede corregir el fondo heredado al abrir el turno dejando motivo y auditoría.

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

## Gastos

Los gastos autorizados se registran como egresos explícitos, con motivo y usuario.

## Ajustes

Los ajustes son correcciones excepcionales autorizadas.

## Arqueo ciego

El primer conteo de efectivo es ciego: el cajero no ve el importe esperado antes de confirmar.

## Corrección guiada

La revisión guiada permite corregir medios de pago sin borrar el registro original.

## Anulación desde arqueo

Si durante el arqueo se detecta una operación que debe anularse, la anulación debe conservar vínculo con el arqueo que originó la revisión.

## Cambio de medio de pago

Toda corrección de medio conserva medio original, medio corregido, importe, usuario, fecha, hora, motivo y arqueo relacionado.

## Cierre

El cierre finaliza formalmente el turno y registra efectivo real, diferencia, correcciones y observaciones.

## Cierre con diferencia

La caja puede cerrarse con diferencia documentada.

## Herencia del efectivo real

El siguiente turno hereda el efectivo físico real confirmado, no el efectivo esperado.

## Casos especiales

- Arqueo de control sin cierre de turno.
- Diferencia dentro de tolerancia.
- Diferencia fuera de tolerancia.
- Corrección de medio de pago.
- Cierre con diferencia.

## Decisiones

- DEC-078 a DEC-087 definen arqueo independiente del cierre, conteo ciego, tolerancia, revisión guiada, corrección auditable, cierre con diferencia, herencia del efectivo real y movimientos explícitos de caja.

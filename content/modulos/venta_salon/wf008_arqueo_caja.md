# WF-008 — Arqueo y Cierre de Caja

## Estado

**Actualizado por Sprint 9.4: movimientos operativos documentados; cierre y arqueo pendientes.**

![WF-008 Arqueo y Cierre de Caja](/static/images/wf008_arqueo_caja_v1_2.png)

## Objetivo

Permitir que un cajero identificado realice un control de caja en cualquier momento y cierre formalmente su sesión cuando corresponda, conservando diferencias, solicitudes de corrección y pendientes de supervisión sin bloquear el cambio de turno.

## Diferencia entre arqueo y cierre

### Arqueo de control

- Puede iniciarse en cualquier momento del turno.
- Se utiliza ante una duda o posible error de cobro.
- No finaliza el turno.
- Después del control, el cajero continúa vendiendo.

### Cierre de sesión

- Finaliza formalmente la sesión de caja del cajero.
- Registra efectivo real, diferencia, correcciones y observaciones.
- No define automáticamente el fondo de la siguiente sesión.

## Apertura del turno

La apertura es obligatoria para cobrar. El cajero declara manualmente el efectivo inicial de cada nueva sesión.

```text
Caja:                    Caja 1
Efectivo inicial:        $118.000
Cajero responsable:      Usuario actual
```

No se hereda automáticamente el efectivo del cierre anterior.

Una sesión pertenece a una caja concreta y a un único cajero responsable. No se traslada entre cajas ni entre dispositivos.

Una caja no puede tener dos sesiones abiertas simultáneamente. Un cajero puede tener varias sesiones abiertas en cajas distintas; al abrir otra sesión recibe una advertencia no bloqueante.

Si existen varias sesiones abiertas para el cajero, la sesión activa de cobro se selecciona explícitamente. El sistema no elige cualquier sesión abierta.

## Movimientos de caja

Solo se consideran movimientos manuales aquellos que no provienen directamente de una venta.

### INGRESO

- Refuerzo de efectivo para cambio.

Entra efectivo al cajón por una causa distinta de una venta. Aumenta el efectivo esperado, no genera `Venta`, no genera `PagoVenta` y no representa ingreso comercial por venta. El motivo es opcional.

### RETIRO

Sale efectivo del cajón para trasladarlo a otro lugar de resguardo, como caja fuerte. Disminuye el efectivo esperado, no representa gasto, pago a proveedor ni pérdida. El motivo es opcional y no requiere autorización de supervisor para un retiro normal.

### EGRESO/PAGO

Sale efectivo del cajón para realizar un pago o afrontar un gasto, por ejemplo flete, compra de insumos o mensajería. Disminuye el efectivo esperado y representa una salida económica. El motivo es obligatorio.

El efectivo esperado se calcula así:

```text
efectivo inicial
+ ventas cobradas en efectivo
+ ingresos manuales
- retiros
- egresos/pagos
= efectivo esperado
```

Sólo los medios que representen efectivo físico suman al efectivo esperado. Transferencias, QR, tarjetas y otros medios no efectivos pertenecen a la información de la sesión, pero no al efectivo físico del cajón.

Cada movimiento conserva tipo, importe, cajero, caja, sesión, fecha y hora. El motivo es obligatorio para egresos/pagos, pero no para ingresos ni retiros.

Los movimientos sólo pueden registrarse sobre una sesión `ABIERTA` y por el cajero responsable. Si el cajero tiene una sola sesión abierta, la interfaz puede usarla directamente para estos movimientos; si tiene varias, debe pedir selección explícita de sesión/caja. En todos los casos el movimiento persistido conserva `sesion_caja_id`.

## Conteo ciego

Al iniciar el arqueo, el cajero solo ve un campo para ingresar el efectivo contado. No puede ver el efectivo esperado ni las ventas acumuladas antes de confirmar.

Esto evita que adapte el conteo al importe teórico.

## Resultado

Después del primer conteo, el sistema muestra:

- efectivo esperado;
- efectivo contado;
- diferencia;
- tolerancia configurada;
- estado del arqueo.

Los medios electrónicos son calculados automáticamente por el sistema. Solo el efectivo se cuenta manualmente.

## Tolerancia

Administración define una tolerancia global o por sucursal.

- Dentro de tolerancia: puede continuar o cerrar dejando registro.
- Fuera de tolerancia: pasa a revisión guiada por el mismo cajero.

## Revisión guiada

El sistema permite revisar las operaciones de la sesión mostrando como mínimo:

- número corto;
- hora;
- total;
- medio o medios de pago.

Si el cajero sospecha un error de medio de pago, marca la operación como posible error. Puede marcar varias operaciones y no necesita indicar inmediatamente cuál sería el medio correcto.

La venta cerrada no se modifica. Se genera un pendiente de supervisión.

El supervisor investiga posteriormente y resuelve mediante una operación administrativa separada y auditable.

Nunca se edita silenciosamente `PagoVenta` ni la venta histórica.

## Corrección de conteo

Si el cajero detecta durante el propio cierre que contó incorrectamente, puede solicitar una corrección.

La solicitud conserva:

- conteo original;
- conteo corregido propuesto;
- usuario;
- fecha/hora;
- estado `PENDIENTE`.

El supervisor puede aprobarla o rechazarla. El supervisor no debe crear una corrección que el cajero nunca solicitó.

La solicitud sólo puede iniciarse durante el cierre inmediato, no posteriormente.

## Cierre con diferencia

La caja puede cerrarse aunque no coincida.

Ejemplo:

```text
Efectivo esperado: $520.000
Efectivo real:     $517.000
Diferencia:         -$3.000
Estado: CERRADA_CON_DIFERENCIA
```

Una corrección pendiente no bloquea el cierre. La sesión se cierra igualmente y el siguiente cajero puede abrir una nueva sesión inmediatamente, declarando manualmente su efectivo inicial.

## Estados

```text
ABIERTA
ARQUEO_EN_CURSO
EN_REVISION
ARQUEADA
CERRADA
CERRADA_CON_DIFERENCIA
```

## Modelo conceptual

### Sesión de caja

- sucursal;
- caja;
- cajero;
- apertura;
- efectivo inicial declarado manualmente;
- estado;
- cierre;
- efectivo real final.

### Arqueo

- turno;
- tipo: control intermedio o cierre;
- fecha y hora;
- efectivo contado;
- efectivo esperado;
- diferencia;
- tolerancia aplicada;
- estado.

### Solicitud de corrección de arqueo

- arqueo;
- conteo original;
- conteo corregido propuesto;
- usuario;
- fecha y hora;
- estado.

### Posible error de medio de pago

- venta;
- sesión;
- cajero;
- fecha y hora;
- estado;
- resolución posterior de supervisor.

## Decisiones relacionadas

- **DEC-078:** arqueo independiente del cierre.
- **DEC-079:** primer conteo ciego.
- **DEC-080:** medios electrónicos calculados automáticamente.
- **DEC-081:** tolerancia configurable.
- **DEC-082:** primera revisión por el cajero.
- **DEC-083:** decisión histórica de corrección auditable de medios; Sprint 9 reemplaza la corrección directa por marcado de posible error y resolución posterior del supervisor mediante operación administrativa separada y auditable.
- **DEC-084:** cierre permitido con diferencia.
- **DEC-085:** decisión histórica reemplazada por Sprint 9; ya no hay herencia automática de efectivo.
- **DEC-086:** decisión histórica reemplazada por Sprint 9; ya no hay corrección de fondo heredado.
- **DEC-087:** todo ingreso o egreso no proveniente de una venta es un movimiento explícito de caja.
- **DEC-174 a DEC-191:** decisiones Sprint 9 de operación de caja, venta preparada, sesión, captura ligada a sesión, arqueo, pendientes, permisos y confirmación por responsable.
- **DEC-192 a DEC-196:** decisiones Sprint 9.4 de movimientos operativos de caja, efectivo esperado, sesión abierta, responsable, selección de sesión y auditoría.

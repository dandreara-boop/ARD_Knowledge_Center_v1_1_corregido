# WF-008 — Arqueo y Cierre de Caja

## Estado

**Propuesta funcional v1.2 para revisión.**

![WF-008 Arqueo y Cierre de Caja](/static/images/wf008_arqueo_caja_v1_2.png)

## Objetivo

Permitir que un cajero identificado realice un control de caja en cualquier momento y cierre formalmente su turno cuando corresponda, conservando todas las diferencias y correcciones.

## Diferencia entre arqueo y cierre

### Arqueo de control

- Puede iniciarse en cualquier momento del turno.
- Se utiliza ante una duda o posible error de cobro.
- No finaliza el turno.
- Después del control, el cajero continúa vendiendo.

### Cierre de turno

- Finaliza formalmente el turno del cajero.
- Registra efectivo real, diferencia, correcciones y observaciones.
- Define el fondo real que recibirá el siguiente turno.

## Apertura del turno

El cajero recibe el fondo heredado del turno anterior y puede confirmarlo o corregirlo.

```text
Fondo heredado:          $120.000
Efectivo recibido real:  $118.000
Motivo: faltante informado al recibir la caja
```

El nuevo turno comienza con el efectivo real confirmado. La corrección queda auditada.

## Movimientos de caja

Solo se consideran movimientos manuales aquellos que no provienen directamente de una venta.

### Ingresos

- Fondo inicial.
- Refuerzo de efectivo para cambio.

### Egresos

- Retiro de efectivo.
- Entrega o depósito de recaudación.
- Gastos autorizados.

### Ajustes

Correcciones excepcionales autorizadas.

El efectivo esperado se calcula así:

```text
Fondo inicial
+ Ventas en efectivo
+ Refuerzos
- Retiros
- Gastos
± Ajustes autorizados
= Efectivo esperado
```

Cada movimiento conserva tipo, importe, usuario, fecha, hora y motivo.

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

El error más frecuente es registrar un medio de pago incorrecto. El sistema ofrece:

- ventas registradas como efectivo;
- ventas pagadas con medios electrónicos;
- importes, horarios y remitos;
- posibles coincidencias con la diferencia;
- sugerencias de operaciones sospechosas.

El cajero puede corregir el medio de pago. La venta original no se borra ni se sobrescribe silenciosamente.

Cada corrección registra:

- medio original;
- medio corregido;
- importe;
- usuario;
- fecha y hora;
- motivo;
- arqueo que originó la revisión.

Después de cada corrección, la diferencia se recalcula automáticamente.

## Cierre con diferencia

La caja puede cerrarse aunque no coincida.

Ejemplo:

```text
Efectivo esperado: $520.000
Efectivo real:     $517.000
Diferencia:         -$3.000
Estado: CERRADA_CON_DIFERENCIA
```

El siguiente turno hereda **$517.000**, porque ese es el efectivo físico confirmado.

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

### Turno de caja

- sucursal;
- caja;
- cajero;
- apertura;
- fondo heredado;
- fondo confirmado;
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

### Corrección de cobro

- venta;
- arqueo;
- medio original;
- medio corregido;
- importe;
- usuario;
- motivo;
- fecha y hora.

## Decisiones relacionadas

- **DEC-078:** arqueo independiente del cierre.
- **DEC-079:** primer conteo ciego.
- **DEC-080:** medios electrónicos calculados automáticamente.
- **DEC-081:** tolerancia configurable.
- **DEC-082:** primera revisión por el cajero.
- **DEC-083:** corrección de medios totalmente auditable.
- **DEC-084:** cierre permitido con diferencia.
- **DEC-085:** herencia del efectivo real.
- **DEC-086:** fondo inicial corregible y documentado.
- **DEC-087:** todo ingreso o egreso no proveniente de una venta es un movimiento explícito de caja.

# Cambios y Créditos Comerciales

## Estado

**Definición funcional aprobada.**

## Principio operativo

El ticket o remito original es la mejor referencia para determinar el valor de una prenda, pero el sistema debe resolver el cambio de forma rápida aunque el cliente no lo presente.

## Orden para determinar el valor reconocido

```text
1. Buscar la venta original.
2. Si existe, utilizar el valor histórico reconocido en esa venta.
3. Si no existe, sugerir el valor unitario de la oferta definida para cambios.
4. Permitir una modificación justificada según permisos y límites configurables.
```

### Venta encontrada

Cada renglón vendido debe conservar:

- precio normal;
- precio promocional aplicado;
- valor reconocido para cambio;
- promoción original;
- número de remito;
- fecha y sucursal.

Las promociones actuales no modifican el valor histórico.

### Venta no encontrada

El sistema propone como primera opción el valor unitario derivado de la oferta de referencia.

Ejemplo:

```text
Promoción: 2 remeras por $50.000
Valor sugerido por unidad: $25.000
```

El cajero puede modificar el valor únicamente si sus permisos lo permiten. Toda modificación registra valor anterior, valor nuevo, usuario, fecha, motivo y autorización cuando corresponda.

## Cambio de varias prendas

Una operación puede recibir múltiples artículos:

| Prenda recibida para cambio | Valor reconocido |
|---|---:|
| Remera | $25.000 |
| Pantalón | $35.000 |
| Buzo | $40.000 |
| **Crédito total** | **$100.000** |

El crédito total se aplica a los productos nuevos. Si la nueva compra supera el crédito, se cobra la diferencia.

## No se entrega dinero

El valor reconocido por cambios nunca genera entrega de efectivo. Se transforma en **Crédito Comercial**.

El Crédito Comercial:

- no representa dinero en caja;
- puede utilizarse en la misma venta o en una compra futura;
- puede aplicarse total o parcialmente;
- conserva saldo e historial;
- puede asociarse a un cliente o emitirse al portador según política global.

## Comprobante de Crédito Comercial

Cuando el cliente no utiliza todo el crédito en el momento, el sistema puede imprimir o enviar un comprobante con:

- número único;
- importe original;
- saldo disponible;
- fecha de emisión;
- vigencia;
- sucursal;
- código de barras o QR;
- leyenda **No canjeable por dinero**.

## Aplicación en una venta

```text
Productos nuevos:       $95.000
Crédito comercial:      $70.000
Diferencia a cobrar:     $25.000
```

Si el crédito es mayor que la compra, el remanente continúa disponible según la política global.

## Varias ventas abiertas

La caja puede mantener varios remitos de venta abiertos o suspendidos simultáneamente. Esto permite guardar una venta mientras el cliente vuelve al salón y atender a otra persona sin perder lo cargado.

Estados previstos:

```text
ABIERTO
SUSPENDIDO
EN_COBRO
FINALIZADO
ANULADO
```

Una venta suspendida conserva artículos, cliente, promociones preliminares y última actividad.

## Modelo conceptual

### Operación de cambio

- identificador;
- sucursal;
- cliente opcional;
- venta original opcional;
- fecha;
- estado;
- crédito total;
- usuario.

### Renglón de cambio

- producto;
- cantidad;
- valor reconocido unitario y total;
- renglón original opcional;
- motivo del valor.

### Crédito Comercial

- identificador único;
- cliente opcional;
- operación de origen;
- importe original;
- saldo disponible;
- vigencia;
- estado.

Estados:

```text
DISPONIBLE
PARCIALMENTE_UTILIZADO
UTILIZADO
VENCIDO
ANULADO
```

## Decisiones relacionadas

- **DEC-061:** prioridad al valor histórico cuando se encuentra la venta.
- **DEC-062:** valor sugerido por oferta cuando no se encuentra la venta.
- **DEC-063:** modificación justificada y auditable.
- **DEC-064:** no se recalcula una venta encontrada con promociones actuales.
- **DEC-065:** se prioriza el procedimiento operativo más frecuente.
- **DEC-066:** política global de reconocimiento de valor.
- **DEC-067:** una operación admite múltiples prendas.
- **DEC-068:** los cambios nunca devuelven dinero.
- **DEC-069:** el saldo a favor se rige por política global.
- **DEC-070:** el crédito comercial no es efectivo ni egreso de caja.
- **DEC-071:** una caja mantiene varios remitos abiertos.
- **DEC-072:** una venta suspendida conserva toda su información.
- **DEC-073:** el crédito se aplica total o parcialmente a una nueva venta.
- **DEC-074:** puede emitirse un Crédito Comercial para uso futuro.
- **DEC-075:** el comprobante posee identificador, QR o código de barras.
- **DEC-076:** el crédito admite utilización parcial.
- **DEC-077:** vigencia, identificación y transferibilidad son configurables.

# Módulo Cambios y Crédito Comercial

## Concepto funcional

Un cambio no es una entrega de dinero. El flujo aprobado es:

```text
Cambio
  ↓
Crédito Comercial
```

## Documento base integrado

{{include:modulos/venta_salon/cambios_creditos}}

## Varias prendas

Una operación de cambio admite múltiples prendas. El sistema suma el valor reconocido de cada una y genera un crédito total aplicable a la nueva venta.

## Valor reconocido

El valor reconocido se toma de la venta original cuando existe. Si no existe, el sistema sugiere el valor unitario de la oferta definida para cambios.

## Con ticket

Con ticket o remito original, se utiliza la venta encontrada y el valor histórico reconocido.

## Sin ticket

Sin ticket, el sistema propone un valor de referencia configurable. Cualquier modificación requiere permisos, motivo y auditoría.

## Crédito Comercial

El Crédito Comercial no es efectivo ni un egreso de caja. Puede aplicarse total o parcialmente en la misma venta o conservarse para una compra futura.

## Uso parcial

El crédito puede utilizarse parcialmente hasta agotarse. El remanente conserva saldo e historial.

## QR

El comprobante de Crédito Comercial puede emitirse con QR para identificación rápida.

## Código de barras

El comprobante también puede incluir código de barras como alternativa operativa al QR.

## Cliente identificado

El crédito puede asociarse a un cliente identificado según política global.

## Cliente ocasional

El crédito puede emitirse al portador si la política global lo permite.

## Vigencia

La vigencia es configurable y forma parte del comprobante emitido.

## Configuración

Son configurables la vigencia, la asociación al cliente, la transferibilidad y los límites de modificación del valor reconocido.

## Wireframes

Las fichas visuales específicas de cambios quedan preparadas en el capítulo Wireframes.

## Decisiones

- DEC-061 a DEC-077 definen valor reconocido, operación con múltiples prendas, Crédito Comercial, comprobante, uso parcial, vigencia, identificación y transferibilidad.

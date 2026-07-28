# WF-004 — Caja de Venta

**Estado:** Aprobado  
**Versión:** 1.1  
**Módulo:** Venta en Salón

## Objetivo

Registrar y cobrar una venta con la menor fricción posible. El cajero ingresa productos e importes; ARD Suite calcula precios, promociones, condición comercial, total y saldo.

## Wireframe aprobado

![WF-004 Caja de Venta](/static/images/wf004_caja_venta_v1_1.png)

## Estructura aprobada

- Número de remito de venta visible y de solo lectura.
- Campo principal para código de barras, con retorno automático del foco después de cada carga.
- Botón **Buscar artículo** para artículos sin etiqueta, con código ilegible o desconocido.
- Botón **Buscar venta** para recuperar operaciones anteriores.
- Grilla tipo planilla con: número, código, producto, cantidad, precio aplicado y subtotal.
- Los atributos no se muestran en la grilla principal.
- Resumen por condición comercial.
- Promociones aplicadas y ahorro del cliente.
- Formulario de medios de pago.
- Botón de flecha en cada medio para asignar el saldo pendiente completo.
- Total a pagar, importe ingresado y saldo.
- Acción principal **Cobrar / Finalizar**.

## Reglas de interacción

1. El cálculo es automático al modificar cualquier importe.
2. La flecha de un medio de pago carga el saldo pendiente, no el total original.
3. El botón Cobrar / Finalizar se habilita cuando el saldo es cero y la venta es válida.
4. El cajero no selecciona promociones ni decide la condición comercial.
5. Toda explicación comercial queda guardada en el historial.

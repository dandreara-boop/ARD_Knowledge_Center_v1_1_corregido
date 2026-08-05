# Módulo Logística

## Estado

**DEFINIDO FUNCIONALMENTE.**

## Objetivo

Administrar confirmación en destino, reposición posterior entre locales, mercadería pendiente o en tránsito, diferencias de recepción, permisos, historial y auditoría.

{{include:modulos/logistica/resumen}}

## Alcance incluido

El módulo Logística manejará únicamente:

1. Confirmación en destino de la mercadería distribuida durante la recepción.
2. Reposición posterior entre locales.
3. Mercadería pendiente o en tránsito asociada a esos procesos.
4. Diferencias de recepción.
5. Permisos relacionados.
6. Historial y auditoría.

## Fuera de alcance

No incorporar dentro de Logística:

- Inventarios.
- Ajustes de stock.
- Compras.
- Recepción de proveedores.
- Configuración del stock web.
- Inteligencia comercial.
- Sugerencias de IA.
- Análisis de rotación.

Esos procesos pertenecen a otros módulos.

## Distribución inicial

La distribución inicial permanece integrada al Módulo Carga de Productos. El operario recibe mercadería, cuenta por atributos, ve la propuesta de distribución, la modifica si corresponde y confirma cantidades para cada local y stock web.

No debe crear transferencias manuales adicionales. Al confirmar, el sistema genera internamente los movimientos necesarios.

Cada local debe ver en una misma pantalla:

- Mercadería pendiente de recibir.
- Remito de Entrada relacionado.
- Código.
- Producto.
- Cantidad asignada.
- Cantidad recibida.
- Acción para confirmar.
- Acción para imprimir etiquetas.
- Estado de etiquetado.
- Acción para habilitar para venta.

La secuencia interna puede ser:

```text
ASIGNADA
  ↓
PENDIENTE DE RECEPCION
  ↓
RECIBIDA
  ↓
ETIQUETADA
  ↓
DISPONIBLE PARA VENTA
```

La interfaz del operario debe ocultar complejidad innecesaria.

Ver también:

- Carga de Productos — Distribución inicial.
- DEC-136.
- DEC-137.
- DEC-138.

## Diferencias en distribución inicial

Si la cantidad recibida no coincide con la asignada, se debe permitir confirmar la cantidad real, incorporar al stock únicamente lo recibido, mantener la diferencia registrada, generar una excepción administrativa y guardar origen, destino, usuarios, fecha y observaciones.

No se bloquea toda la recepción por una diferencia.

## Reposición entre locales

Flujo funcional:

1. Buscar producto.
2. Consultar stock disponible en otros locales.
3. Seleccionar local proveedor.
4. Ingresar cantidad.
5. Enviar solicitud.
6. Local proveedor confirma y prepara.
7. Mercadería pasa a reservada o en tránsito.
8. Local receptor confirma lo recibido.
9. Stock se actualiza.

### Pantalla de solicitud

- Código.
- Producto.
- Stock del local solicitante.
- Stock visible en otros locales.
- Cantidad solicitada.
- Motivo.
- Acción Enviar solicitud.

### Pantalla del local proveedor

- Solicitud.
- Local solicitante.
- Producto.
- Cantidad.
- Preparar.
- No disponible.
- Modificar cantidad con motivo.

### Pantalla del receptor

- Origen.
- Producto.
- Cantidad enviada.
- Cantidad recibida.
- Confirmar recepción.
- Registrar diferencia.

Las prendas ya transferidas entre locales normalmente estarán etiquetadas, por lo cual no se exige reimpresión salvo necesidad.

## Permisos de Logística

- Consultar stock de otros locales.
- Solicitar mercadería.
- Preparar solicitud.
- Modificar cantidad preparada.
- Confirmar despacho.
- Confirmar recepción.
- Registrar diferencia.
- Cancelar solicitud.
- Revisar excepciones logísticas.

## Transferencias y trazabilidad

Las transferencias deben conservar origen, destino, estado, usuario, fecha y movimientos asociados.

## Stock Web

El Stock Web puede recibir mercadería desde recepción o transferencias posteriores, pero su configuración pertenece a Administración u otro módulo específico.

## Casos especiales

- Transferencia pendiente de recepción.
- Diferencia entre preparado y recibido.
- Mercadería en tránsito.
- Solicitud cancelada.
- Recepción parcial.

## Decisiones relacionadas

- LOG-001: transferencias auditables.
- DEC-037: la asignación vincula cantidad recibida y destino.
- DEC-038: finalizar el remito genera movimientos auditables.
- DEC-136: distribución integrada con la recepción.
- DEC-137: confirmación y etiquetado en destino.
- DEC-138: complejidad interna oculta.
- DEC-139: reposición accesible al personal de ventas.
- DEC-140: solicitud previa al traslado.
- DEC-141: diferencias recibidas sin bloqueo.
- DEC-142: alcance limitado del módulo Logística.

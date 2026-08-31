# Flujo operativo — Carga de Productos

## 1. Creación o identificación

Administración carga códigos de productos existentes.

Cuando el código existe:

```text
Código
  ↓
Producto encontrado
  ↓
Agregar al remito
```

Cuando no existe:

```text
Código no encontrado
  ↓
Crear producto
  ↓
Asignar código y precio
```

## 2. Remito de Entrada

Puede contener productos existentes y nuevos.

## 3. Recepción física

La mercadería se separa primero por producto y luego por talle.

Administración trabaja en paralelo asignando código y valor de venta.

## 4. Atributos

La pantalla de depósito muestra solamente los atributos definidos en Administración.

El operario indica únicamente los atributos que llegaron realmente y sus cantidades. No genera variantes manualmente.

```text
Seleccionar producto
  ↓
Indicar atributos recibidos
  ↓
Ingresar cantidades
  ↓
Confirmar
```

Al confirmar, el sistema busca la variante correspondiente, la reutiliza si existe o la crea automáticamente si todavía no existe. También genera el código de barras y registra el movimiento de stock.

## 5. Distribución

Se trabaja con cantidades, nunca con porcentajes.

Ejemplo:

| Talle | Recibido | Web | Local Centro | Local Norte |
|---|---:|---:|---:|---:|
| 2 | 10 | 2 | 4 | 4 |
| 3 | 10 | 2 | 4 | 4 |

## 6. Etiquetado

Se realiza en cada local después de la distribución.

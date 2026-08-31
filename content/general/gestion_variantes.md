# Gestión de Variantes

## Filosofía

En ARD Suite la entidad comercial principal es el Artículo.

Una Variante representa una presentación concreta de un artículo determinada por una combinación de atributos.

Ejemplo:

```text
Artículo
  Remera Lisa

Variantes
  Remera Lisa Talle 2 Blanco
  Remera Lisa Talle 2 Negro
  Remera Lisa Talle 3 Blanco
```

Las variantes son utilizadas posteriormente para:

- Stock.
- Ventas.
- Logística.
- Cambios.
- Estadísticas.
- Tienda Online.

## Principio de simplicidad

El usuario nunca debe pensar en variantes, producto cartesiano o generación de combinaciones.

El usuario únicamente trabaja con mercadería.

Toda la complejidad técnica debe ser resuelta por el sistema.

## Familias de atributos

Una Familia de Atributos es una plantilla reutilizable que simplifica la configuración de nuevos artículos.

Ejemplos:

| Familia | Atributos |
|---|---|
| TEXTIL | Talle, Color |
| CALZADO | Número, Color |
| PINTURAS | Color, Capacidad |
| FERRETERÍA | Rosca, Largo, Material |

Las familias funcionan únicamente como plantillas reutilizables.

No generan variantes automáticamente.

No crean stock.

No crean códigos.

Únicamente simplifican la configuración de nuevos artículos.

## Creación de variantes

Las variantes se crean únicamente cuando existe una necesidad real.

Principalmente durante:

- Recepción de Mercadería.
- Importaciones.
- Procesos administrativos específicos.

No existe generación obligatoria de variantes al crear un artículo.

## Recepción de Mercadería

Durante la recepción, el operario no utiliza un botón denominado **Generar Variantes**.

El flujo correcto es:

```text
Seleccionar artículo
        ↓
Indicar únicamente los atributos que llegaron realmente
        ↓
Ingresar cantidades
        ↓
Confirmar
```

Durante ese proceso el sistema deberá:

- Buscar la variante correspondiente.
- Utilizarla si ya existe.
- Crearla automáticamente si todavía no existe.
- Generar automáticamente el código de barras correspondiente.
- Registrar el movimiento de stock.

Todo este proceso ocurre internamente.

El operario nunca trabaja directamente con variantes.

## Beneficios de este enfoque

- Menor complejidad operativa.
- No se generan variantes innecesarias.
- Menor cantidad de registros.
- Catálogo más limpio.
- Mayor velocidad de carga.
- Refleja exactamente la mercadería recibida.
- Simplifica el aprendizaje del operario.

## Modelo conceptual actualizado

Flujo anterior reemplazado:

```text
Artículo
        ↓
Generar Variantes
        ↓
Recepción
```

Nuevo flujo:

```text
Artículo
        ↓
Recepción de Mercadería
        ↓
Servicio Interno de Generación de Variantes
        ↓
Stock
```

El Servicio de Generación de Variantes pasa a ser un componente interno reutilizable.

Será utilizado por:

- Recepción.
- Importaciones.
- Procesos Administrativos.
- API.

No será normalmente una pantalla utilizada por el operario.

## Referencias relacionadas

- [Modelo Conceptual](/doc/general/modelo_conceptual).
- [Recepción de Mercadería](/doc/modulos/recepcion/documento_maestro).
- [Administración — Productos](/doc/modulos/administracion/documento_maestro).
- [Principios de Arquitectura](/doc/general/principios_arquitectura).

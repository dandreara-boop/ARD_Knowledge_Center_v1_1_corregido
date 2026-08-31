# Principios de Arquitectura

## Principio de Abstracción Operativa

### Objetivo

El usuario siempre debe trabajar utilizando conceptos propios del negocio.

Nunca debe interactuar con estructuras técnicas internas del sistema.

Las estructuras internas pertenecen exclusivamente a la implementación del software.

## Responsabilidad del Frontend

El Frontend tiene como objetivo ofrecer la experiencia de uso más simple posible.

Debe:

- Mostrar información comprensible.
- Permitir seleccionar opciones.
- Validar datos básicos de ingreso.
- Traducir la interacción del usuario al formato requerido por la API.

Ejemplo:

```text
Artículo
  Remera Lisa

Talle
  [x] 1
  [x] 2

Color
  [x] Blanco
  [x] Negro

Cantidad
  5
```

El operario nunca visualizará:

```text
valor_atributo_id = 6
valor_atributo_id = 8
```

Los identificadores internos pertenecen exclusivamente al backend.

## Responsabilidad del Backend

El Backend es responsable de toda la lógica del negocio.

Debe:

- Validar reglas.
- Validar permisos.
- Validar atributos.
- Detectar duplicados.
- Crear variantes.
- Registrar auditoría.
- Actualizar stock.
- Mantener consistencia de datos.

El Frontend nunca debe implementar reglas de negocio.

## Principio de Reutilización

Toda regla importante debe existir una única vez.

Las aplicaciones:

- Escritorio.
- Web.
- Mobile.
- API Pública.
- Integraciones futuras.

deben reutilizar exactamente el mismo Backend.

La lógica nunca debe duplicarse entre interfaces.

## API Interna

La API trabaja con identificadores internos.

Ejemplo:

```text
valor_atributo_ids
codigo_barra
articulo_id
```

El usuario nunca interactúa directamente con esos identificadores.

La interfaz los transforma automáticamente.

## Motor de Reglas

El Motor de Reglas constituye el único lugar donde se implementan las decisiones importantes del negocio.

No deben existir reglas comerciales distribuidas entre:

- Routers.
- Frontend.
- Repositories.

Los Services coordinan procesos.

Las Policies toman decisiones.

Las Rules realizan validaciones específicas.

## Flujo Arquitectónico

```text
Usuario
   ↓
Frontend
   ↓
API
   ↓
Service
   ↓
Business Rules
   ↓
Repository
   ↓
MariaDB
```

Las decisiones del negocio se producen exclusivamente dentro del Motor de Reglas.

## Ejemplo práctico

Creación automática de variantes.

El usuario selecciona:

```text
Talle 1
Color Blanco
Cantidad 5
```

El Frontend convierte esa selección en los identificadores internos.

La API recibe:

```text
valor_atributo_ids
```

El Motor de Reglas valida:

- Atributos permitidos.
- Combinación existente.
- Código de barras.
- Consistencia.

Si todo es correcto, `VariantService` crea la variante.

El usuario nunca necesita conocer cómo funciona internamente ese proceso.

## Beneficios

- Menor complejidad para el usuario.
- Interfaces más limpias.
- Backend reutilizable.
- Menor mantenimiento.
- Menor riesgo de inconsistencias.
- Posibilidad de múltiples interfaces utilizando la misma lógica.

## Estado del Proyecto

| Sprint | Alcance | Estado |
|---|---|---|
| Sprint 1 | Infraestructura Base | ✓ Finalizado |
| Sprint 2 | Catálogo Comercial | ✓ Finalizado |
| Sprint 3 | Servicio de Generación de Variantes | ✓ Finalizado |
| Sprint 4 | Motor de Reglas de Negocio | ✓ Finalizado |

## Conclusión

ARD Suite adopta como principio de arquitectura que toda complejidad técnica debe permanecer dentro del sistema.

El operador interactúa únicamente con procesos comerciales.

Esta decisión busca reducir tiempos de capacitación, minimizar errores operativos y facilitar la evolución futura del sistema.

## Referencias relacionadas

- [Visión y filosofía](/doc/general/vision).
- [Modelo Conceptual](/doc/general/modelo_conceptual).
- [Gestión de Variantes](/doc/general/gestion_variantes).
- [Registro de Decisiones](/doc/referencias/decisiones_agrupadas).

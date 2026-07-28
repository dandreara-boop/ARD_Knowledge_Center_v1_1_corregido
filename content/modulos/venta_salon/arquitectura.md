# Arquitectura local y nube — Venta en Salón

## Flujo de persistencia

```text
Escaneo
  ↓
Venta local
  ↓
Stock local actualizado
  ↓
Comprobante
  ↓
Cola de sincronización
  ↓
Base central
  ↓
Historial consolidado
```

## Identificador global

Toda venta tendrá un identificador único para evitar duplicaciones en los reintentos.

## Cola de sincronización

Estados:

- PENDIENTE.
- ENVIANDO.
- CONFIRMADO.
- ERROR_REINTENTABLE.
- REQUIERE_REVISION.

## Venta con stock negativo

Se registra localmente y se sincroniza.

La nube genera una excepción administrativa.

El vendedor continúa trabajando sin advertencias.

# Arquitectura distribuida

## Objetivo

Cada sucursal debe poder vender aunque Internet sea lento o esté interrumpido.

## Estructura

```text
                    BASE CENTRAL EN LA NUBE
                              │
               ┌──────────────┴──────────────┐
               │                             │
       BASE LOCAL SUCURSAL 1         BASE LOCAL SUCURSAL 2
               │                             │
             CAJA                          CAJA
```

## Regla principal

> Toda venta presencial se registra primero en la base local y luego se sincroniza con la nube.

## Base central

Administra:

- Catálogo.
- Precios.
- Promociones.
- Políticas.
- Usuarios.
- Proveedores.
- Clientes.
- Historial consolidado.
- Transferencias.
- Tiendanube.
- Futuro canal web propio.

## Base local

Contiene lo necesario para operar:

- Productos.
- Códigos.
- Precios.
- Promociones.
- Stock local.
- Usuarios autorizados.
- Ventas.
- Caja.
- Pagos.
- Cambios.
- Cola de sincronización.

## Funcionamiento sin conexión

La sucursal continúa vendiendo. Las operaciones quedan pendientes y se envían cuando regresa la conexión.

## Autoridad de los datos

| Información | Autoridad principal |
|---|---|
| Productos y precios | Central |
| Promociones y políticas | Central |
| Venta presencial | Sucursal local |
| Caja | Sucursal local |
| Stock operativo del local | Sucursal local |
| Historial consolidado | Central |
| Stock web | Central |

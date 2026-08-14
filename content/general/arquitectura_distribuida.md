# Arquitectura distribuida

## Objetivo

Cada sucursal debe poder vender aunque Internet sea lento o esté interrumpido.

## Estructura

```text
                    SERVIDOR CENTRAL ARD SUITE
                              │
               ┌──────────────┴──────────────┐
               │                             │
       SERVIDOR LOCAL SUCURSAL 1    SERVIDOR LOCAL SUCURSAL 2
       Base + API + sincronizacion  Base + API + sincronizacion
               │                             │
            LAN local                     LAN local
```

## Regla principal

> Toda operación presencial se registra primero en la base local de la sucursal y luego se sincroniza con la Central.

No existe una base independiente por cada puesto de trabajo. Cada sucursal utiliza una única base local compartida por LAN.

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

La caída de Internet no impide la operación local mientras la red interna, el servidor local y la base local funcionen. El detalle funcional completo se encuentra en [Módulo Sincronización](/doc/modulos/sincronizacion/documento_maestro).

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

## Independencia de infraestructura

La Central ARD Suite no queda acoplada a un proveedor específico. Puede alojarse inicialmente en DigitalOcean, migrarse luego a un servidor propio y complementarse en producción madura con respaldo externo o cloud sin rediseñar funcionalmente las sucursales.

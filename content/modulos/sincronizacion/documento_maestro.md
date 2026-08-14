# Módulo Sincronización

## Estado

**APROBADO FUNCIONALMENTE PARA DESARROLLO.**

## Objetivo

Documentar la arquitectura distribuida de ARD Suite y el comportamiento esperado de la operación local, la sincronización automática, la contingencia manual y la visibilidad administrativa de datos entre sucursales y Central.

Este módulo no implementa tablas, servicios, colas, backups, importadores ni conectividad cloud. Define el criterio funcional aprobado para orientar el futuro Modelo de Datos y el desarrollo posterior.

## Arquitectura general

ARD Suite tendrá una arquitectura distribuida. Cada sucursal contará con:

- Una única base de datos local.
- Una API local.
- Un servicio local de sincronización.
- Varios equipos conectados mediante la red interna LAN.

```text
SUCURSAL

        Servidor local
   +---------------------+
   | Base de datos local |
   | API local           |
   | Sincronizacion      |
   +----------+----------+
              |
          RED INTERNA
              |
      +-------+--------+
      |       |        |
   Caja 1   Caja 2   Otros equipos
```

No existe una base independiente por cada puesto de trabajo. Existe una base local por sucursal, compartida por todos los equipos de esa sucursal.

## Red interna e Internet

La red interna y la conexión a Internet son dependencias diferentes.

La red interna permite:

- Utilizar ARD Suite dentro de la sucursal.
- Compartir ventas, stock, ventas abiertas y cambios entre puestos.
- Hacer arqueos, consultar caja y operar varios equipos contra el mismo servidor local.

Internet solamente es necesario para:

- Sincronizar con la Central.
- Recibir actualizaciones administrativas.
- Enviar operaciones consolidadas.
- Acceder a Administración Central desde fuera de la sucursal.

La caída de Internet no debe impedir la operación local mientras la red interna, el servidor local y la base local funcionen.

## Base Central

La Central almacenará el historial consolidado de toda la empresa.

```text
Sucursal Centro --+
                  |
Sucursal Norte ---+--> Central ARD Suite
                  |
Stock Web --------+
```

Debe recibir ventas, anulaciones, cambios, créditos comerciales, movimientos de caja, arqueos, cierres, correcciones, movimientos de stock, logística, excepciones y auditoría.

## Administración Central

Administración Central será una aplicación web accesible desde cualquier ubicación por usuarios autorizados. Consulta la base consolidada y permite revisar ventas, stock por sucursal, stock total, caja, cierres, arqueos, diferencias, cambios, créditos, anulaciones, remitos, logística, excepciones y estado de sincronización.

Cada informe debe indicar la vigencia de los datos:

- Última conexión.
- Última sincronización.
- Sucursales pendientes.
- Antigüedad de los datos.

Nunca debe presentar información desactualizada como actual.

## Administración Local

Administración Local permite consultar la información propia de una sucursal aun sin Internet. Consulta directamente la base local de la sucursal y no reemplaza a Administración Central.

Según permisos, podrá mostrar:

- Ventas del día.
- Remitos.
- Stock local.
- Caja.
- Arqueos y cierres.
- Diferencias, anulaciones y correcciones.
- Cambios y créditos comerciales.
- Movimientos de efectivo y transferencias.
- Excepciones locales.

## Operación local primero

Toda operación presencial se confirma primero en la base local.

```text
Operacion del usuario
        |
Guardar en base local
        |
Actualizar estado local
        |
Agregar evento a cola
        |
Intentar sincronizar
```

Una venta nunca debe esperar respuesta de Internet para finalizar.

## Sincronización automática

La sincronización normal será continua y en segundo plano.

```text
Evento local
    |
Intentar enviar inmediatamente
```

Si se envía correctamente, queda **CONFIRMADO**. Si falla, queda **PENDIENTE** o en un estado de error reintentable y se reintenta automáticamente. La falta de Internet no cambia el procedimiento del operario.

## Cola persistente

La cola local persistente conserva los eventos sincronizables y sobrevive reinicios, cierre del servicio, cortes eléctricos e interrupciones de Internet.

Estados conceptuales:

```text
PENDIENTE
ENVIANDO
CONFIRMADO
ERROR_REINTENTABLE
REQUIERE_REVISION
```

Cada evento debe conservar al menos identificador global, sucursal, terminal de origen, tipo de operación, entidad afectada, fecha y hora, estado, cantidad de intentos, último error, fecha de confirmación y dependencias cuando correspondan.

## Identificador global e idempotencia

Cada operación sincronizable debe tener un identificador global único. El mismo evento puede enviarse varias veces sin duplicar efectos.

```text
Evento enviado
        |
Respuesta perdida
        |
Sucursal lo reenvia
        |
Central detecta mismo ID
        |
No duplica operacion
```

Este principio es obligatorio para la sincronización online y para la importación manual de paquetes.

## Orden y dependencias

Algunos eventos dependen de otros. Por ejemplo, una venta anulada no debe procesarse antes que la venta creada.

El sistema debe respetar:

- Orden por entidad.
- Dependencias explícitas.
- Secuencia de operaciones relacionadas.

Un evento con error no debe bloquear eventos independientes.

## Dirección de sincronización

### Sucursal hacia Central

Se sincronizan ventas, anulaciones, cambios, créditos, caja, arqueos, cierres, correcciones, logística, stock, excepciones y auditoría.

### Central hacia Sucursal

Se sincronizan productos, códigos, precios, promociones, proveedores, medios de pago, políticas comerciales, usuarios, permisos, configuración de caja, sucursales, parámetros, solicitudes de reposición y cambios administrativos aplicables.

## Autoridad de los datos

No todas las bases pueden modificar todas las entidades. Cada grupo de información tiene una autoridad principal para reducir conflictos.

| Información | Autoridad principal |
|---|---|
| Productos | Central |
| Precios | Central |
| Promociones | Central |
| Políticas comerciales | Central |
| Usuarios y permisos | Central |
| Configuraciones | Central |
| Venta presencial | Sucursal de origen |
| Caja | Sucursal |
| Arqueos | Sucursal |
| Stock operativo local | Sucursal |
| Stock consolidado | Central |
| Stock web | Central |
| Logística | Compartida según el estado del proceso |

## Versionado de datos centrales

Los datos enviados desde Central a sucursales deberán manejar versiones.

```text
Catalogo v163
Precios v91
Promociones v27
Permisos v42
Configuracion v18
```

Cada sucursal conservará la última versión aplicada. Administración Central podrá ver qué versión tiene cada local.

## Ventas históricas

Una actualización posterior de precio o promoción no debe modificar una venta finalizada. Cada venta debe conservar precio utilizado, promoción aplicada, condición comercial, versión comercial, explicación del cálculo, medio de pago y valores reconocidos para cambio.

El historial comercial es inalterable.

## Usuarios offline

Los usuarios previamente autorizados para una sucursal podrán continuar trabajando sin Internet mediante usuarios almacenados localmente, credenciales locales seguras y últimos permisos sincronizados.

Cuando vuelva la conexión se aplicarán nuevas altas, bajas, bloqueos y cambios de permisos. La falta de conexión no debe impedir a un usuario previamente habilitado iniciar su turno.

## Transparencia para ventas

El operario de ventas no debe enterarse de la pérdida de conexión a Internet. Mientras la red local, el servidor local y la base local estén disponibles, el sistema debe comportarse normalmente.

No se deben mostrar al cajero mensajes invasivos, errores de nube, ventanas de sincronización ni colas pendientes.

El estado de conectividad será visible únicamente para Administración, encargados autorizados y soporte técnico.

## Desconexiones prolongadas

Una desconexión de horas o días no modifica el procedimiento. La sucursal sigue vendiendo, haciendo caja, registrando cambios, haciendo arqueos y acumulando eventos.

La cola simplemente crece. Cuando vuelve Internet, se reanudan los envíos, se procesan los eventos pendientes y se reconstruye el consolidado Central.

## Panel de sincronización

Administración debe mostrar por sucursal estado, última conexión, última sincronización, cantidad de eventos pendientes, antigüedad del evento más antiguo, último error, cantidad de errores, versión de catálogo, precios, promociones, permisos y configuraciones.

| Sucursal | Estado | Última conexión | Pendientes | Más antiguo | Catálogo | Promos |
|---|---|---:|---:|---|---|---|
| Centro | Actualizada | 16:34 | 0 | - | v163 | v27 |
| Norte | Sin conexión | 13:18 | 184 | 13:19 | v161 | v26 |

El panel debe destacar solo situaciones que requieren intervención.

## Paquetes manuales de contingencia

El intercambio mediante archivos es excepcional. No se genera un archivo por cada operación.

La operación normal es:

```text
Guardar localmente
        |
Cola persistente
        |
Esperar conectividad
        |
Sincronizacion automatica
```

Solo un usuario autorizado desde Administración podrá solicitar **Generar paquete de contingencia**.

### Central hacia Sucursal

En una situación extrema, Administración Central podrá generar un archivo de actualización para una sucursal con productos, precios, promociones, proveedores, usuarios, permisos y configuraciones.

Debe incluir sucursal destino, identificador único, fecha y hora, versiones origen y destino, checksum, firma y contenido incluido.

Se aplica una sola vez al servidor local. Todos los puestos de esa sucursal quedan actualizados inmediatamente porque utilizan la misma base.

### Sucursal hacia Central

Una sucursal desconectada podrá generar manualmente un paquete con eventos aún pendientes: ventas, anulaciones, cambios, créditos, caja, arqueos, cierres, correcciones, movimientos de stock y excepciones.

Luego podrá llevarse a otro equipo con Internet e importarse en Administración Central.

### Mismo protocolo

El paquete manual no constituye un sistema paralelo. Debe usar los mismos eventos, identificadores, idempotencia y validaciones que la sincronización online.

Si el archivo fue importado y luego vuelve Internet, los eventos reenviados automáticamente no deben duplicarse.

## Independencia del proveedor de infraestructura

ARD Suite no debe quedar acoplado a DigitalOcean. Conceptualmente existirá un **Servidor Central ARD Suite**, alojado inicialmente en DigitalOcean, posteriormente en infraestructura propia o eventualmente en otro proveedor.

Las sucursales no deben necesitar modificaciones importantes al cambiar el proveedor de infraestructura.

## Etapas de infraestructura

### Etapa inicial / Piloto

DigitalOcean funciona como Central para poner el sistema en marcha rápidamente, probarlo en los dos locales y validar la interacción con operarios.

### Etapa posterior

Un servidor propio dedicado pasa a operar como Central principal.

### Producción madura

Servidor propio principal más respaldo externo o cloud. El sistema deberá permitir esta evolución sin rediseñar las sucursales.

## Copias de seguridad

El principio aprobado es no depender de una sola copia de la información.

```text
Base local de sucursal
        +
Servidor central propio
        +
Respaldo externo
```

No se desarrolla todavía el sistema de backups. Solo queda documentado el principio de redundancia.

## Referencias cruzadas

- [Administración Central](/doc/modulos/administracion/documento_maestro)
- [Administración Local](#administracion-local)
- [Caja](/doc/modulos/caja/documento_maestro)
- [Venta en Salón](/doc/modulos/venta_salon/documento_maestro)
- [Logística](/doc/modulos/logistica/documento_maestro)
- [Usuarios y Permisos](/doc/modulos/usuarios_permisos/documento_maestro)
- [Centro de Excepciones](/doc/modulos/centro_excepciones/documento_maestro)
- [Futuro Modelo de Datos](/doc/modelo_datos/documento_maestro)

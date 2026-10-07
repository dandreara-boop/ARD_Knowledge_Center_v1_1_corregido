# Sprint 9 — Operación de Caja y Flujo de Venta en Salón

## Estado

SPRINT 9.3 IMPLEMENTADO.

Estado técnico:

- Sprint 9.3 terminado.
- 122 tests passed.
- No requirió nueva migración.
- Alembic continúa en `20261006_0009` (head).

Sprint 9 define la operación cotidiana del salón y de las cajas sobre las capacidades construidas en Sprint 6, Sprint 7 y Sprint 8.

El objetivo es separar correctamente vendedor, cajero, dispositivo, caja y sesión de caja, permitiendo tanto la venta directa en caja como la preparación de ventas por vendedores durante períodos de alta demanda.

## Principio operativo

La operación del local no debe detenerse por controles administrativos pendientes.

Las verificaciones, diferencias de arqueo y posibles errores detectados durante el cierre deben conservar trazabilidad y control sin impedir innecesariamente el cambio de turno.

La posibilidad de que un cajero tenga más de una sesión abierta en cajas distintas y la independencia de la sesión respecto del dispositivo responden a este principio: advertir no significa impedir.

## Conceptos separados

ARD Suite distingue explícitamente:

- Local.
- Dispositivo o terminal.
- Usuario.
- Vendedor.
- Cajero.
- Supervisor.
- Caja.
- Sesión de caja.
- Venta.
- Cobro.

Un dispositivo no es una caja.
Un vendedor no es necesariamente el cajero.
Una caja no es una PC.
Una sesión de caja no pertenece a una PC.

Una sesión de caja representa la responsabilidad de un cajero sobre una caja concreta durante un período determinado.

La separación conceptual definitiva es:

```text
DISPOSITIVO != CAJERO != CAJA != SESION DE CAJA
```

## Modos operativos

### Modo normal — Caja crea y cobra

El cajero puede:

1. Crear la venta.
2. Identificar al vendedor real cuando corresponda.
3. Cargar o escanear artículos.
4. Modificar la venta mientras siga abierta.
5. Resolver el pago utilizando Sprint 8.
6. Confirmar el cobro.

El cajero que registra la operación no debe quedar automáticamente registrado como vendedor.

### Autoservicio

Cuando no existió atención atribuible a un vendedor:

```text
tipo_atencion = AUTOSERVICIO
vendedor_id = null
```

No se inventa un vendedor para completar el registro.

### Modo alta demanda — Vendedor prepara y caja cobra

El vendedor puede preparar la venta desde una PC o tablet sin necesidad de tener una sesión de caja abierta.

```text
ABIERTA
   ↓
LISTA_PARA_COBRAR
   ↓
EN_COBRO
   ↓
CERRADA
```

Una venta capturada puede liberarse de `EN_COBRO` a `LISTA_PARA_COBRAR`.

La captura evita que dos cajas trabajen simultáneamente sobre la misma venta.

## Identificación de la venta preparada

La venta mantiene su identificador global permanente y además tendrá un número corto visible para la operación del salón.

El vendedor registra también una referencia simple del cliente, normalmente nombre u otra identificación breve.

```text
Venta
- global_id
- numero_corto
- referencia_cliente
- vendedor_id
- local_id
- estado
```

El vendedor entrega al cliente un pequeño papel con el número corto.

No se requiere QR para este flujo porque imprimirlo introduciría una demora innecesaria.

La caja debe poder localizar rápidamente la operación escribiendo el número corto y confirmando con Enter.

El número corto nunca reemplaza al `global_id`.

La estrategia definitiva de numeración y reinicio del número corto deberá quedar configurable o validarse técnicamente durante la implementación. No se reutiliza el número de una operación anulada.

## Disponibilidad, captura y liberación

Una venta `LISTA_PARA_COBRAR` queda disponible para las cajas habilitadas del mismo local.

La pantalla principal del vendedor prioriza sus propias ventas, aunque puede permitirse consultar otras ventas del mismo local por número o referencia sin otorgar por ello permiso de modificación.

Cuando una caja captura una venta, pasa a `EN_COBRO` y otra caja no puede capturarla simultáneamente.

El cajero que la capturó puede modificarla antes de confirmar.

Si el vendedor necesita volver a modificarla, la caja debe liberarla previamente.

La liberación devuelve `EN_COBRO` a `LISTA_PARA_COBRAR` y queda auditada. No equivale a anular.

## Anulación de operación incompleta

Una operación abandonada o que no continuará puede anularse.

La venta anulada permanece en el historial y no se elimina físicamente.

Si posteriormente el cliente decide realizar la compra, se crea una nueva venta con una nueva identificación operativa. Nunca se reutiliza el número corto de la operación anulada.

## Auditoría del flujo

Debe poder reconstruirse al menos:

- Quién creó la venta.
- Vendedor atribuido.
- Quién la envió a caja.
- Cuándo quedó lista para cobrar.
- Quién la capturó.
- En qué caja.
- Liberaciones.
- Modificaciones posteriores.
- Quién confirmó el cobro.
- Anulación, si existió.

Las correcciones operativas deben conservar valores anteriores y nuevos cuando corresponda.

## Verificación de mercadería en caja

La verificación es configurable.

```text
SIN_VERIFICACION
VERIFICACION_VISUAL
VERIFICACION_POR_ESCANEO
```

En verificación por escaneo, el sistema compara las unidades esperadas con las verificadas.

Si aparece una unidad adicional, el cajero puede incorporarla a la venta.

Si falta una unidad esperada, el sistema no debe eliminarla automáticamente. El cajero puede volver a escanear o modificar explícitamente la venta.

Una segunda lectura de un artículo cuya cantidad esperada ya fue completada se considera una unidad adicional potencial.

Debe conservarse método, cantidades esperadas y verificadas, existencia de diferencias, correcciones y resultado final.

Una verificación puede finalizar correctamente después de una corrección conservando históricamente que existió una diferencia.

Una diferencia no se interpreta automáticamente como error del vendedor.

No se solicita motivo al cajero por cada corrección operativa durante la verificación. El sistema registra usuario, fecha/hora, valor anterior, valor nuevo y venta afectada.

## Caja y sesión de caja

Una Caja representa un punto lógico/físico de cobro, no una PC o tablet.

Para cobrar y confirmar una venta debe existir una sesión de caja abierta y válida. Preparar una venta no requiere sesión de caja.

La sesión pertenece a un local, una caja concreta y un único cajero responsable durante toda su vida.

La sesión no se traslada entre cajas.

La sesión tampoco se traslada entre dispositivos. Puede ser consultada y utilizada desde otra computadora sin transferirla ni modificar su identidad.

Una caja no puede tener dos sesiones abiertas simultáneamente.

Un cajero puede tener más de una sesión abierta simultáneamente, siempre que correspondan a cajas diferentes.

Ejemplo válido:

```text
Maria
├── CAJA-2 -> Sesion #458 -> ABIERTA
└── CAJA-3 -> Sesion #461 -> ABIERTA
```

Si Maria abrió `Sesion #458` en `CAJA-2` desde `PC-2` y `PC-2` falla, puede ingresar desde `PC-3` y continuar utilizando la misma `Sesion #458`. No existe transferencia de sesión entre PCs porque la sesión nunca perteneció al dispositivo.

Otro cajero no puede cobrar utilizando la sesión de Maria. Una intervención administrativa futura de supervisor no cambia quién fue el responsable original de la sesión.

Si el cajero abre una nueva sesión y ya posee otra sesión abierta, el sistema debe mostrar una advertencia clara, pero no bloquear la apertura.

Ejemplo conceptual:

```text
ATENCION

Ya tenes una sesion abierta:

CAJA-2
Sesion #458

¿Queres abrir tambien una sesion en CAJA-3?
```

Cuando existan varias sesiones abiertas para un cajero, el sistema no debe elegir automáticamente cuál utilizar. La sesión activa para cobrar debe seleccionarse explícitamente y mostrarse de manera visible, por ejemplo:

```text
Maria | CAJA-3 | Sesion #461
```

No se permite una regla del tipo "buscar cualquier sesión abierta del cajero".

## Apertura

La apertura es obligatoria para cobrar.

El efectivo inicial se declara manualmente en cada nueva sesión. Puede ser `0` o mayor.

No se hereda automáticamente el efectivo del cierre anterior.

Cada sesión constituye un período independiente de responsabilidad.

Dos solicitudes simultáneas no pueden abrir dos sesiones abiertas sobre la misma Caja. Sprint 9.3 protege la apertura mediante bloqueo transaccional de la Caja.

## Captura, sesión y confirmación

Una venta capturada para cobro queda asociada de manera inequívoca a:

- `caja_captura_id`.
- `sesion_caja_id`.

Flujo:

```text
LISTA_PARA_COBRAR
        |
        v
captura con sesión explícita
        |
        v
EN_COBRO
        |
        v
CERRADA
```

Al capturar:

- La sesión debe existir.
- Debe estar `ABIERTA`.
- Debe pertenecer al cajero que opera.
- Su Caja debe estar activa.
- Caja y Venta deben pertenecer al mismo local/destino.

La caja se obtiene de la sesión. No se permite capturar utilizando solamente `caja_id`.

También se mantiene la protección para que dos cajas o sesiones no puedan capturar simultáneamente la misma Venta.

Si una venta pasa de `EN_COBRO` a `LISTA_PARA_COBRAR`, se eliminan de la venta activa:

- `caja_captura_id`.
- `sesion_caja_id`.
- `capturada_at`.

El evento histórico de liberación conserva la caja y sesión anteriores. El `numero_corto` de la venta no se modifica ni se reutiliza.

Para el flujo nuevo de salón, confirmar `EN_COBRO -> CERRADA` exige:

- Que exista `sesion_caja_id`.
- Que la sesión continúe `ABIERTA`.
- Que corresponda a `caja_captura_id`.
- Que el cajero que confirma sea el responsable de esa sesión.

`usuario_id` no puede omitirse para confirmar una venta `EN_COBRO`. Otro cajero no puede confirmar utilizando una sesión ajena.

La venta `CERRADA` conserva `caja_captura_id` y `sesion_caja_id` como trazabilidad histórica.

El backend mantiene temporalmente compatibilidad con el flujo anterior `ABIERTA -> CERRADA` sin exigir `usuario_id` ni sesión, porque corresponde a mecanismos anteriores a Sprint 9. Esto no constituye un bypass permitido para el nuevo flujo POS de salón `LISTA_PARA_COBRAR -> EN_COBRO -> CERRADA`.

## Movimientos de efectivo

### RETIRO

Representa mover dinero fuera del cajón hacia una caja fuerte u otro lugar de resguardo.

Requiere importe, usuario, sesión y fecha/hora.

No requiere motivo obligatorio ni autorización previa del supervisor.

Reduce el efectivo físico esperado y no representa un gasto de la empresa.

### EGRESO / PAGO

Representa utilizar efectivo de caja para pagar algo.

Requiere importe, motivo, usuario, sesión y fecha/hora.

Reduce el efectivo esperado y representa una salida económica diferenciada de un retiro.

### Efectivo esperado

```text
efectivo inicial declarado
+ cobros en efectivo
+ ingresos de efectivo
- retiros
- egresos/pagos
± otros movimientos explícitos
= efectivo esperado
```

Los medios no efectivos pertenecen a los totales comerciales de la sesión pero no forman parte del efectivo físico del cajón.

## Cierre y arqueo

El cierre requiere conteo físico del efectivo.

El primer conteo es ciego: antes de confirmarlo el cajero no ve el efectivo esperado.

Después del primer conteo se muestran efectivo esperado, efectivo contado y diferencia.

El primer conteo nunca se elimina ni sobrescribe.

### Corrección de conteo

Si el cajero detecta inmediatamente que contó incorrectamente, puede solicitar una corrección durante el propio flujo de cierre.

La solicitud debe realizarse antes de abandonar o confirmar definitivamente ese flujo.

Después no puede iniciar retrospectivamente una nueva corrección de arqueo.

Se conservan conteo original, conteo corregido propuesto, cajero, fecha/hora y estado.

La solicitud queda `PENDIENTE` y requiere revisión de supervisor, quien puede aprobarla o rechazarla.

El supervisor no inventa una corrección que el cajero nunca solicitó.

### Cierre con revisión pendiente

Una corrección pendiente no bloquea el cambio de turno.

La sesión puede cerrarse y el siguiente cajero puede abrir una nueva sesión.

La resolución administrativa posterior permanece vinculada al cierre original.

## Revisión de operaciones al cierre

Durante el cierre el cajero debe poder consultar las operaciones realizadas en su sesión mostrando como mínimo número corto de venta, hora, total y medio o medios de pago.

Esto permite contrastar el sistema con tickets de terminales y otros comprobantes.

## Posible error de medio de pago

Si el cajero considera que una operación pudo registrarse con un medio incorrecto, no modifica la venta cerrada.

Puede marcar una o varias operaciones como `POSIBLE_ERROR_PAGO`.

No está obligado a diagnosticar en ese momento cuál era el medio correcto.

Se registra venta, sesión, cajero, fecha/hora y estado pendiente.

El caso queda para revisión del supervisor.

## Resolución por supervisor

El supervisor investiga el caso pendiente.

Puede confirmar que no existió error o realizar la corrección administrativa autorizada correspondiente.

La venta original permanece inmutable.

Nunca se reemplaza silenciosamente el medio de pago histórico original.

La corrección es un registro separado y auditable que conserva venta original, medio original, medio corregido cuando corresponda, importe, supervisor, fecha/hora, relación con sesión/cierre y resultado.

## Pendientes de supervisión

El sistema debe ofrecer un circuito unificado de pendientes, incluyendo solicitudes de corrección de arqueo y posibles errores de medio de pago.

Estos pendientes no bloquean por defecto la operación del local ni la apertura de la siguiente sesión.

## Venta cerrada

Se mantiene la regla de Sprint 8:

```text
Venta CERRADA = inmutable
```

No se corrigen errores editando directamente una venta cerrada.

Cuando corresponda una corrección administrativa, se registra una operación separada y auditable.

Cuando corresponda rehacer la operación comercial, se utiliza anulación explícita y nueva venta.

## Roles y permisos

La seguridad interna se basa en permisos y los roles son agrupaciones o plantillas de permisos.

Jerarquía funcional inicial:

```text
VENDEDOR
   ↓
CAJERO
   ↓
SUPERVISOR
   ↓
ADMINISTRADOR
```

### VENDEDOR

Puede incluir:

- `venta.crear`
- `venta.modificar_propia`
- `venta.enviar_caja`
- `venta.consultar`

### CAJERO

Incluye capacidades de vendedor y puede agregar:

- `caja.abrir`
- `caja.capturar_venta`
- `caja.modificar_venta_capturada`
- `caja.cobrar`
- `caja.verificar_mercaderia`
- `caja.retirar`
- `caja.egreso`
- `caja.cerrar`
- `caja.marcar_posible_error_pago`

### SUPERVISOR

Incluye capacidades de cajero y puede agregar:

- `supervision.ver_cajas`
- `supervision.revisar_cierres`
- `supervision.arqueo`
- `supervision.corregir_pago`
- `supervision.intervenir_venta`

### ADMINISTRADOR

Incluye capacidades de supervisor y agrega configuración general de usuarios, roles, permisos, cajas, medios de pago, condiciones comerciales y políticas operativas.

Los nombres técnicos definitivos de permisos podrán ajustarse durante implementación sin alterar estas capacidades funcionales.

## Permiso y contexto operativo

Tener permiso `caja.cobrar` no significa tener una caja abierta.

Para cobrar deben coexistir usuario autorizado, sesión de caja abierta y válida, y una venta capturada o creada para cobro.

Un supervisor o administrador que quiera cobrar también necesita una sesión de caja válida.

## Vendedor y cajero

La atribución comercial del vendedor es independiente del usuario que realiza el cobro.

Una venta puede conservar históricamente vendedor, cajero y supervisor posterior sin confundir responsabilidades.

## Visibilidad

El vendedor trabaja principalmente con sus propias ventas.

Puede consultar operaciones de otros vendedores del mismo local cuando sea necesario, pero esa visibilidad no implica permiso de modificación.

El cajero puede modificar la venta capturada para cobrar.

El supervisor puede intervenir según sus permisos.

## Integración con Sprints 6, 7 y 8

Sprint 9 no reemplaza el Motor de Venta Local.

La confirmación continúa utilizando el cierre local transaccional y el outbox existente. Inventario continúa fuera del camino crítico del POS.

Los precios siguen perteneciendo al Artículo y continúan resolviéndose mediante el Motor Comercial de Precios.

El cobro utiliza la resolución comercial implementada en Sprint 8.

Sprint 9 agrega el contexto operativo: quién vende, quién cobra, en qué caja y sesión, cómo llega la venta a caja, cómo se verifica, cómo se cierra y arquea la sesión y cómo se detectan y supervisan errores posteriores.

No modifica el algoritmo comercial de pagos simples o mixtos.

## Offline-first

Todas las operaciones esenciales del salón y caja deben funcionar contra la base local.

La falta de Internet no puede impedir crear ventas, prepararlas, capturarlas, cobrar, registrar movimientos, cerrar caja ni registrar pendientes de supervisión localmente.

La sincronización posterior no pertenece al camino crítico de venta.

## Fuera de alcance del Sprint 9

No se documentan como implementados en Sprint 9.3:

- Motor completo de promociones.
- Devoluciones.
- Implementación completa de cambios.
- Comisiones de vendedores.
- Estadísticas avanzadas.
- Sincronización cloud definitiva.
- Frontend definitivo completo.
- Cierre de caja.
- Arqueo.
- Retiros.
- Egresos/pagos.
- Correcciones de arqueo.
- Posibles errores de medios de pago.
- Supervisión.
- Modelo de dispositivos.
- Contabilidad general.
- Conciliación bancaria automática.
- Integraciones fiscales no definidas.

## Estado de implementación

```text
Diseño funcional: CERRADO
Implementación backend Sprint 9.3: TERMINADA
Migración nueva Sprint 9.3: NO REQUERIDA
Alembic head: 20261006_0009
QA automático: 122 tests passed
Frontend: PENDIENTE
```


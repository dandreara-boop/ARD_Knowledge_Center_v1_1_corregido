# Decisiones — Venta en Salón y Caja

| Código | Decisión |
|---|---|
| DEC-014 | Las promociones no generan productos nuevos. |
| DEC-015 | Se aplica la promoción más conveniente para el cliente. |
| DEC-017 | Toda decisión automática debe ser explicable y auditable. |
| DEC-018 | Cada unidad conserva el precio aplicado y el valor reconocido para cambios. |
| DEC-020 | La política de cambios es global y no la decide el cajero. |
| DEC-041 | Cada sucursal tiene una base local independiente. |
| DEC-042 | La venta presencial se registra primero localmente. |
| DEC-043 | La sincronización utiliza identificadores globales para evitar duplicados. |
| DEC-044 | La nube conserva el historial consolidado. |
| DEC-045 | Cada tipo de información tiene una autoridad definida. |
| DEC-046 | La falta de Internet no impide vender. |
| DEC-047 | La forma de pago participa en el cálculo comercial. |
| DEC-048 | Medio de pago y condición comercial son conceptos separados. |
| DEC-049 | Las cobranzas se administran separadamente por medio de pago. |
| DEC-050 | La venta se recalcula al modificar los importes antes de confirmarse. |
| DEC-051 | El tratamiento del pago mixto se define mediante políticas globales. |
| DEC-052 | El motor optimiza el pago mixto para obtener el mejor resultado permitido. |
| DEC-053 | Los pagos mixtos admiten límites disponibles o carga progresiva de importes. |
| DEC-054 | La empresa configura qué medios se consideran contado. |
| DEC-055 | Se priorizan unidades completas y grupos promocionales completos. |
| DEC-056 | El cálculo comercial se actualiza continuamente. |
| DEC-057 | Una unidad o grupo que combine contado y financiado pierde el beneficio de contado. |
| DEC-058 | Existirá un catálogo visual configurable para artículos sin etiqueta individual. |
| DEC-059 | Un producto puede venderse por código, catálogo visual o ambos. |
| DEC-060 | La pantalla de caja muestra solo la información imprescindible para trabajar con rapidez. |
| DAT-SALE-001 | La venta local se materializa antes de ejecutar trabajos derivados. |
| DAT-SALE-002 | Venta cerrada y evento pendiente se guardan atómicamente. |
| DAT-SALE-003 | Inventario queda fuera del camino crítico del POS. |
| DAT-SALE-004 | Los detalles conservan snapshot comercial histórico. |
| DAT-SALE-005 | El outbox local persistente representa obligaciones derivadas. |
| DAT-SALE-006 | El procesamiento de eventos es reintentable. |
| DAT-SALE-007 | Los efectos derivados de venta son idempotentes. |
| DAT-SALE-008 | Los movimientos derivados de venta usan UUID5 determinístico compatible con `String(36)`. |
| DAT-SALE-009 | Los eventos con error no se pierden. |
| DAT-SALE-010 | Los eventos procesados no vuelven a aplicar inventario. |
| DAT-SALE-011 | El stock negativo no bloquea la venta local. |
| DAT-PRICE-001 | El precio comercial pertenece al Artículo, no a la Variante. |
| DAT-PRICE-002 | Las reglas pertenecen a condiciones comerciales y no a cada artículo. |
| DAT-PRICE-003 | El motor usa reglas Python tipadas y controladas, sin fórmulas libres. |
| DAT-PRICE-004 | Los cálculos monetarios utilizan Decimal. |
| DAT-PRICE-005 | Cambiar el precio BASE de un artículo recalcula derivados activos en forma atómica. |
| DAT-PRICE-006 | El cambio general de una regla requiere preview y aplicación explícita. |
| DAT-PRICE-007 | El preview no persiste cambios en PrecioArticulo. |
| DAT-PRICE-008 | La política frente a precios manuales se define explícitamente al aplicar recálculo masivo. |
| DAT-PRICE-009 | La auditoría de precios se genera sólo ante cambios efectivos de precio u origen. |
| DAT-PRICE-010 | Las ventas históricas conservan snapshot de precio y no se recalculan por cambios actuales. |
| DAT-PRICE-011 | La condición BASE activa única se valida en servicio por compatibilidad con MariaDB. |
| DAT-POS-001 | MedioPago y CondicionComercialPrecio son conceptos separados. |
| DAT-POS-002 | Toda venta nueva inicia valorizada con la condición comercial BASE. |
| DAT-POS-003 | La consulta o simulación comercial no persiste snapshot ni pagos definitivos. |
| DAT-POS-004 | El futuro POS podrá usar una condición o medio de visualización reversible durante la carga. |
| DAT-POS-005 | Una distribución de pagos admite múltiples medios y cero o un RESTO. |
| DAT-POS-006 | El mismo algoritmo debe resolver pagos simples, mixtos y N medios. |
| DAT-POS-007 | La resolución debe minimizar el costo final para el cliente respetando los importes solicitados. |
| DAT-POS-008 | La unidad física se prioriza antes del fraccionamiento monetario. |
| DAT-POS-009 | La conversión proporcional entre condiciones es simétrica y usa Decimal. |
| DAT-POS-010 | El redondeo monetario de cobro se aplica sólo al importe final calculado por medio y sube al siguiente múltiplo configurable de 0,05. |
| DAT-POS-011 | La resolución debe generar una traza estructurada explicable. |
| DAT-POS-012 | La venta confirmada conserva snapshot histórico completo de la resolución. |
| DAT-POS-013 | Una venta CERRADA es inmutable. |
| DAT-POS-014 | Un error posterior al cierre se corrige mediante anulación explícita y nueva venta. |
| DAT-POS-015 | Confirmar cobro es una operación local y atómica. |
| DAT-POS-016 | El motor comercial no mueve stock y conserva el mecanismo de inventario existente. |
| DAT-POS-017 | Los fragmentos internos no se redondean individualmente; se conserva precisión suficiente hasta el subtotal por medio. |
| DAT-POS-018 | Los importes fijos ingresados por cliente o cajero se respetan sin alterarlos por redondeo. |
| DAT-POS-019 | La resolución monetaria se modela como LP y, al minimizar unidades fraccionadas, como MILP. |
| DAT-POS-020 | HiGHS mediante highspy es el solver técnico elegido para la implementación definitiva. |
| DAT-POS-021 | highspy debe quedar encapsulado detrás de CommercialOptimizer; dominio, routers y endpoints no dependen directamente del solver. |
| DAT-POS-022 | La solución del solver debe reconstruirse y validarse con Decimal antes de permitir la confirmación. |
| DAT-POS-023 | El orden de medios del request no tiene prioridad comercial; los desempates usan criterio canónico interno. |
| DAT-POS-024 | El optimizador usa precios efectivos de PrecioArticulo y no reconstruye reglas del Sprint 7. |
| DAT-POS-025 | No se aprueban límites arbitrarios de ticket sin medición y documentación previas. |
| DAT-POS-026 | La implementación productiva debe compararse contra un oráculo independiente en escenarios pequeños. |
| DAT-POS-027 | ARD debe soportar Windows y Linux; la integración Linux de Sprint 8 queda pendiente de validación automatizada. |
| DAT-POS-028 | highspy queda pendiente de incorporación formal, pin de versión y validación CI durante implementación. |
| DEC-174 | Sprint 9 separa dispositivo, vendedor, cajero, caja y sesión de caja como responsabilidades distintas; la sesión no pertenece a una PC/tablet. |
| DEC-175 | La venta puede operar en modo normal o en modo alta demanda con preparación por vendedor y cobro por caja. |
| DEC-176 | La venta preparada conserva `global_id` permanente y número corto operativo; el número corto no reemplaza al identificador global ni se reutiliza tras anulación. |
| DEC-177 | Una venta `LISTA_PARA_COBRAR` sólo puede estar capturada por una caja a la vez y puede liberarse de `EN_COBRO` a `LISTA_PARA_COBRAR`. |
| DEC-178 | La verificación de mercadería es configurable y sus correcciones se auditan sin pedir motivo por cada diferencia operativa. |
| DEC-179 | Para cobrar se requiere permiso y una sesión de caja abierta, válida y seleccionada explícitamente. |
| DEC-180 | Una sesión de caja pertenece a una caja concreta y a un único cajero responsable; no se traslada entre cajas ni entre dispositivos. |
| DEC-181 | El efectivo inicial de cada sesión se declara manualmente y no se hereda automáticamente del cierre anterior. |
| DEC-182 | RETIRO y EGRESO/PAGO son movimientos distintos: retiro no es gasto, egreso/pago sí representa salida económica. |
| DEC-183 | El primer conteo de arqueo es ciego y nunca se borra. |
| DEC-184 | La corrección de conteo de arqueo sólo puede solicitarla el cajero durante el cierre inmediato y queda pendiente de supervisor. |
| DEC-185 | Un posible error de medio de pago se marca para supervisión; no se corrige directamente la venta cerrada ni `PagoVenta`. |
| DEC-186 | Los pendientes de supervisión no bloquean el cierre ni la apertura de la siguiente sesión. |
| DEC-187 | Los roles son agrupaciones configurables de permisos; la jerarquía funcional inicial es `VENDEDOR → CAJERO → SUPERVISOR → ADMINISTRADOR`. |
| DEC-188 | Una caja puede tener una sola sesión abierta; un cajero puede tener varias sesiones abiertas en cajas distintas, con advertencia no bloqueante al abrir otra. |
| DEC-189 | Si el cajero tiene varias sesiones abiertas, el sistema no elige automáticamente: la sesión activa de cobro debe seleccionarse y mostrarse explícitamente. |
| DEC-190 | Una venta `EN_COBRO` queda ligada a `caja_captura_id` y `sesion_caja_id`; la caja se obtiene de la sesión y no se captura sólo con `caja_id`. |
| DEC-191 | Confirmar `EN_COBRO -> CERRADA` exige `usuario_id`, sesión abierta correspondiente y cajero responsable de esa sesión; el legacy `ABIERTA -> CERRADA` conserva compatibilidad temporal sin habilitar bypass del POS nuevo. |
| DEC-192 | Sprint 9.4 distingue `INGRESO`, `RETIRO` y `EGRESO/PAGO` como movimientos manuales de efectivo separados, con impacto propio sobre el efectivo esperado. |
| DEC-193 | `INGRESO` y `RETIRO` tienen motivo opcional para no frenar la operación; `EGRESO/PAGO` exige motivo obligatorio por representar una salida económica. |
| DEC-194 | Los movimientos operativos de caja sólo pueden registrarse sobre una `SesionCaja` abierta y por el cajero responsable de esa sesión. |
| DEC-195 | Para movimientos rápidos de caja, la UI puede usar la única sesión abierta del cajero; si existen varias, debe pedir selección explícita. La persistencia siempre conserva `sesion_caja_id`. |
| DEC-196 | Los movimientos de caja conservan trazabilidad de tipo, importe, motivo, cajero, caja, sesión y fecha/hora; cualquier futura anulación o corrección deberá ser auditable. |
| DEC-197 | `EFECTIVO` es el único `MedioPago` que mueve efectivo físico dentro del cajón y debe reconocerse mediante una identificación explícita y estable, no por texto visible. |
| DEC-198 | En pagos mixtos sólo la porción cobrada mediante `EFECTIVO` incrementa el efectivo físico esperado. |
| DEC-199 | En el cierre de su `SesionCaja`, el cajero cuenta exclusivamente el efectivo físico que permanece en su cajón. |
| DEC-200 | Los `RETIRO` registrados quedan fuera del conteo del cajero y pueden verificarse posteriormente por supervisor o encargado para investigar diferencias. |
| DEC-201 | La verificación posterior de retiros no reescribe el primer conteo histórico; una diferencia de arqueo no culpabiliza automáticamente al cajero. |

## Cambios y créditos comerciales

- DEC-061 a DEC-077: valor reconocido, cambios múltiples, ventas abiertas y Crédito Comercial.

## Arqueo y cierre de caja

- DEC-078 a DEC-087: arqueo ciego, revisión guiada, tolerancia, cierre con diferencia y movimientos explícitos de efectivo.
- DEC-085 y DEC-086 quedan como registro histórico reemplazado por Sprint 9: ya no hay herencia automática ni corrección de fondo heredado.

## Sprint 9 — Operación de Caja y Flujo de Venta en Salón

- DEC-174 a DEC-201: separación conceptual de roles y caja, sesión independiente del dispositivo, modos de venta, venta preparada, captura/liberación ligada a sesión, verificación, sesión de caja personal, apertura manual, varias sesiones por cajero con advertencia no bloqueante, sesión activa explícita, confirmación por responsable, movimientos operativos de caja, efectivo físico, arqueo ciego, alcance del conteo, retiros verificables posteriormente, correcciones pendientes, posible error de pago, pendientes de supervisión y permisos.

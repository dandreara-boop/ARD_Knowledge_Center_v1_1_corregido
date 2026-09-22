# Registro de Decisiones

Cada decisión indica código, título, descripción, fecha y versión documental.

## General

| Código | Título | Descripción | Fecha | Versión |
|---|---|---|---|---|
| DEC-017 | Decisión automática explicable | Toda decisión automática es explicable y auditable. | 2026-07-27 | 1.2 |
| DEC-028 | Objetivo principal de pantalla | Una pantalla debe tener un objetivo principal. | 2026-07-27 | 1.0 |
| DEC-035 | Modelo conceptual previo | El modelo conceptual se define antes de las tablas físicas. | 2026-07-27 | 1.0 |
| DEC-039 | Prototipos aprobados | Los prototipos aprobados forman parte del Knowledge Center. | 2026-07-27 | 1.0 |
| DEC-041 | Base local por sucursal | Cada sucursal tendrá una base local independiente. | 2026-07-27 | 1.1 |
| DEC-042 | Venta primero local | Toda venta presencial se registra primero localmente. | 2026-07-27 | 1.1 |
| DEC-043 | Identificadores globales | La sincronización usa identificadores globales. | 2026-07-27 | 1.1 |
| DEC-044 | Historial consolidado | La nube conserva el historial consolidado. | 2026-07-27 | 1.1 |
| DEC-045 | Autoridad de datos | Cada tipo de dato tiene una autoridad definida. | 2026-07-27 | 1.1 |
| DEC-046 | Venta sin Internet | La falta de Internet no impide vender. | 2026-07-27 | 1.1 |
| DEC-168 | Abstracción operativa | El usuario trabaja con conceptos del negocio y no con identificadores internos. | 2026-08-31 | 1.7 |
| DEC-169 | Frontend sin reglas de negocio | El Frontend traduce la interacción del usuario al formato requerido por la API sin implementar reglas de negocio. | 2026-08-31 | 1.7 |
| DEC-170 | Backend como autoridad de negocio | El Backend concentra lógica, validaciones, permisos, auditoría, stock y consistencia. | 2026-08-31 | 1.7 |
| DEC-171 | Reutilización de reglas | Toda regla importante existe una única vez y es reutilizada por todas las interfaces. | 2026-08-31 | 1.7 |
| DEC-172 | Motor de Reglas único | El Motor de Reglas es el único lugar donde se implementan las decisiones importantes del negocio. | 2026-08-31 | 1.7 |
| DEC-173 | Responsabilidad por capa | Services coordinan procesos, Policies toman decisiones y Rules realizan validaciones específicas. | 2026-08-31 | 1.7 |

## Inventario

| Código | Título | Descripción | Fecha | Versión |
|---|---|---|---|---|
| DAT-STK-001 | Stock por variante y destino | El stock se registra por variante, destino de inventario y estado, no directamente por artículo. | 2026-09-01 | 1.8 |
| DAT-STK-002 | Cambio con movimiento | Todo cambio de stock genera un MovimientoStock auditable. | 2026-09-01 | 1.8 |
| DAT-STK-003 | Historial y saldo | El modelo mantiene MovimientoStock como historial y StockActual como saldo materializado. | 2026-09-01 | 1.8 |
| DAT-STK-004 | Movimientos tipificados | Los movimientos de stock se registran con tipos preparados para recepción, venta, cambios, transferencias, ajustes y merma. | 2026-09-01 | 1.8 |
| DAT-STK-005 | Origen trazable | Todo movimiento conserva documento u origen trazable mediante tipo de origen, id de origen y referencia. | 2026-09-01 | 1.8 |
| DAT-STK-006 | Stock negativo en salón | La venta presencial no se bloquea por stock teórico insuficiente. | 2026-09-01 | 1.8 |
| DAT-STK-007 | Ajustes compensatorios | Los ajustes se registran como movimientos positivos o negativos contra el stock contado. | 2026-09-01 | 1.8 |
| DAT-STK-008 | Idempotencia global | Cada MovimientoStock posee global_id único para evitar duplicar efectos ante reintentos. | 2026-09-01 | 1.8 |
| DAT-STK-009 | Prioridad de venta | La materialización de una venta presencial tiene prioridad sobre procesos secundarios. | 2026-09-01 | 1.8 |
| DAT-STK-010 | Venta y evento atómicos | Venta y evento pendiente deben persistirse en la misma transacción. | 2026-09-01 | 1.8 |
| DAT-STK-011 | Inventario diferible | Inventario podrá procesarse fuera del camino crítico del POS cuando la integridad lo permita. | 2026-09-01 | 1.8 |
| DAT-STK-012 | Facturación rápida | Los procesos pesados no deben ralentizar la facturación. | 2026-09-01 | 1.8 |
| DAT-STK-013 | Saldo incremental | StockActual se actualiza incrementalmente y no recalculando todo el historial por operación. | 2026-09-01 | 1.8 |

## Recepción

| Código | Título | Descripción | Fecha | Versión |
|---|---|---|---|---|
| DEC-022 | Producto y atributos separados | Producto y atributos se mantienen separados. | 2026-07-27 | 1.0 |
| DEC-029 | Código visible | El código permanece visible en los procesos operativos. | 2026-07-27 | 1.0 |
| DEC-030 | Prioridad por código | La carga de remitos prioriza productos existentes por código. | 2026-07-27 | 1.0 |
| DEC-031 | Agregado rápido | Un producto existente se agrega sin abrir su ficha completa. | 2026-07-27 | 1.0 |
| DEC-032 | Remito mixto | El remito admite productos existentes y nuevos. | 2026-07-27 | 1.0 |
| DEC-033 | Atributos designados | Depósito muestra solo los atributos designados. | 2026-07-27 | 1.0 |
| DEC-034 | Cantidades, no porcentajes | La distribución se expresa en cantidades, no porcentajes. | 2026-07-27 | 1.0 |
| DEC-036 | Conteo por atributos | El conteo se registra por combinación de atributos. | 2026-07-27 | 1.0 |
| DEC-037 | Asignación por destino | La asignación vincula cantidad recibida y destino. | 2026-07-27 | 1.0 |
| DEC-038 | Movimientos auditables | Finalizar el remito genera movimientos auditables. | 2026-07-27 | 1.0 |
| DEC-165 | Variantes bajo demanda | Las variantes se crean únicamente cuando existe una necesidad real. | 2026-08-26 | 1.6 |
| DEC-166 | Servicio interno de variantes | Recepción, Importaciones, Procesos Administrativos y API usan un servicio interno que busca o crea variantes automáticamente. | 2026-08-26 | 1.6 |
| DEC-167 | Familias como plantillas | Las Familias de Atributos son plantillas reutilizables y no generan variantes, stock ni códigos. | 2026-08-26 | 1.6 |

## Venta

| Código | Título | Descripción | Fecha | Versión |
|---|---|---|---|---|
| DEC-014 | Promociones sin productos ficticios | Las promociones no generan productos nuevos. | 2026-07-27 | 1.1 |
| DEC-015 | Mejor promoción para cliente | Se aplica la promoción más conveniente para el cliente. | 2026-07-27 | 1.1 |
| DEC-018 | Valor por unidad | Cada unidad conserva su precio aplicado. | 2026-07-27 | 1.1 |
| DEC-020 | Política global de cambios | La política de cambios es global. | 2026-07-27 | 1.2 |
| DEC-047 | Pago en cálculo comercial | La forma de pago participa en el cálculo comercial. | 2026-07-27 | 1.1 |
| DEC-048 | Medio y condición separados | Medio de pago y condición comercial se modelan por separado. | 2026-07-27 | 1.1 |
| DEC-050 | Recálculo de venta | La venta se recalcula antes de confirmarse. | 2026-07-27 | 1.1 |
| DEC-051 | Pago mixto por política | El pago mixto responde a políticas globales. | 2026-07-27 | 1.1 |
| DEC-052 | Optimización de pagos | El sistema optimiza la combinación de pagos. | 2026-07-27 | 1.1 |
| DEC-053 | Límites o carga progresiva | Se permiten límites disponibles o carga progresiva. | 2026-07-27 | 1.1 |
| DEC-054 | Contado configurable | La condición contado es configurable por medio. | 2026-07-27 | 1.1 |
| DEC-055 | Prioridad por unidad o grupo | Se priorizan unidades o grupos completos. | 2026-07-27 | 1.1 |
| DEC-056 | Recálculo continuo | El recálculo es continuo. | 2026-07-27 | 1.1 |
| DEC-057 | Mezcla financiada | Una unidad parcialmente financiada pierde el beneficio de contado. | 2026-07-27 | 1.1 |
| DEC-058 | Catálogo visual | Catálogo visual para artículos sin código individual. | 2026-07-27 | 1.1 |
| DEC-059 | Venta por código o catálogo | Venta por código, catálogo visual o ambos. | 2026-07-27 | 1.1 |
| DAT-SALE-001 | Venta local materializada | La venta local se materializa antes de ejecutar trabajos derivados. | 2026-09-08 | 1.9 |
| DAT-SALE-002 | Cierre y evento atómicos | Venta cerrada y evento pendiente se guardan en la misma transacción. | 2026-09-08 | 1.9 |
| DAT-SALE-003 | Inventario diferido | Inventario queda fuera del camino crítico del POS. | 2026-09-08 | 1.9 |
| DAT-SALE-004 | Snapshot comercial | Los detalles de venta conservan variante, códigos, descripción, cantidad, precio unitario e importe históricos. | 2026-09-08 | 1.9 |
| DAT-SALE-005 | Outbox local persistente | El outbox local representa la obligación persistente de ejecutar efectos derivados. | 2026-09-08 | 1.9 |
| DAT-SALE-006 | Procesamiento reintentable | Los eventos pendientes pueden reintentarse después de errores sin perder la venta. | 2026-09-08 | 1.9 |
| DAT-SALE-007 | Efectos idempotentes | Los efectos derivados de venta deben poder reintentarse sin duplicar inventario. | 2026-09-08 | 1.9 |
| DAT-SALE-008 | UUID5 para movimientos de venta | Los movimientos derivados de venta usan UUID5 determinístico compatible con `String(36)`. | 2026-09-08 | 1.9 |
| DAT-SALE-009 | Errores persistentes | Los eventos con error conservan estado, intentos y último error para revisión o reintento. | 2026-09-08 | 1.9 |
| DAT-SALE-010 | Procesados no reaplicados | Los eventos procesados no vuelven a aplicar inventario. | 2026-09-08 | 1.9 |
| DAT-SALE-011 | Stock negativo no bloqueante | El stock negativo no bloquea la venta local. | 2026-09-08 | 1.9 |
| DAT-PRICE-001 | Precio por Artículo | El precio comercial pertenece al Artículo, no a la Variante. | 2026-09-17 | 2.0 |
| DAT-PRICE-002 | Reglas por condición | Las reglas pertenecen a condiciones comerciales y no a cada artículo. | 2026-09-17 | 2.0 |
| DAT-PRICE-003 | Reglas tipadas | El motor usa reglas Python tipadas y controladas, sin fórmulas libres. | 2026-09-17 | 2.0 |
| DAT-PRICE-004 | Decimal monetario | Los cálculos monetarios utilizan Decimal. | 2026-09-17 | 2.0 |
| DAT-PRICE-005 | Base recalcula derivados | Cambiar el precio BASE de un artículo recalcula derivados activos en forma atómica. | 2026-09-17 | 2.0 |
| DAT-PRICE-006 | Regla general controlada | El cambio general de una regla requiere preview y aplicación explícita. | 2026-09-17 | 2.0 |
| DAT-PRICE-007 | Preview sin persistencia | El preview no persiste cambios en PrecioArticulo. | 2026-09-17 | 2.0 |
| DAT-PRICE-008 | Política de manuales | La política frente a precios manuales se define explícitamente al aplicar recálculo masivo. | 2026-09-17 | 2.0 |
| DAT-PRICE-009 | Auditoría efectiva | La auditoría de precios se genera sólo ante cambios efectivos de precio u origen. | 2026-09-17 | 2.0 |
| DAT-PRICE-010 | Snapshot histórico | Las ventas históricas conservan snapshot de precio y no se recalculan por cambios actuales. | 2026-09-17 | 2.0 |
| DAT-PRICE-011 | BASE única en servicio | La condición BASE activa única se valida en servicio por compatibilidad con MariaDB. | 2026-09-17 | 2.0 |

## Caja

| Código | Título | Descripción | Fecha | Versión |
|---|---|---|---|---|
| DEC-049 | Cobros por medio | Los cobros se administran separadamente por medio. | 2026-07-27 | 1.1 |
| DEC-060 | Caja rápida | La caja prioriza velocidad, simplicidad e información indispensable. | 2026-07-27 | 1.1 |
| DEC-071 | Ventas abiertas | La caja puede mantener varios remitos abiertos o suspendidos. | 2026-07-27 | 1.2 |
| DEC-072 | Venta suspendida | Una venta suspendida conserva toda la información cargada. | 2026-07-27 | 1.2 |
| DEC-078 | Arqueo sin cierre | Un arqueo puede realizarse sin cerrar el turno. | 2026-07-27 | 1.2 |
| DEC-079 | Conteo ciego | El primer conteo es ciego. | 2026-07-27 | 1.2 |
| DEC-080 | Solo efectivo manual | Solo se cuenta efectivo; los medios electrónicos los calcula el sistema. | 2026-07-27 | 1.2 |
| DEC-081 | Tolerancia configurable | Administración define la tolerancia de diferencias. | 2026-07-27 | 1.2 |
| DEC-082 | Revisión guiada | La primera revisión la realiza el cajero mediante un flujo guiado. | 2026-07-27 | 1.2 |
| DEC-083 | Corrección auditable | Toda corrección del medio de pago conserva el valor original y su auditoría. | 2026-07-27 | 1.2 |
| DEC-084 | Cierre con diferencia | El turno puede cerrarse aunque exista una diferencia documentada. | 2026-07-27 | 1.2 |
| DEC-085 | Herencia de efectivo real | El próximo turno hereda el efectivo físico real confirmado. | 2026-07-27 | 1.2 |
| DEC-086 | Fondo inicial corregible | El fondo heredado puede corregirse al abrir el turno dejando motivo. | 2026-07-27 | 1.2 |
| DEC-087 | Movimiento explícito | Todo ingreso o egreso ajeno a una venta es un movimiento explícito de caja. | 2026-07-27 | 1.2 |

## Administración

| Código | Título | Descripción | Fecha | Versión |
|---|---|---|---|---|
| ADM-001 | Configuración global | Administración define políticas globales del sistema. | 2026-07-27 | 1.3 |
| ADM-002 | Centro de excepciones | Las operaciones que requieren revisión se agrupan en un centro específico. | 2026-07-27 | 1.3 |
| ADM-003 | Seguridad backend | Toda acción sensible se valida en backend. | 2026-07-27 | 1.3 |
| DEC-112 | Centro de navegación administrativo | Administración funciona como centro de navegación, no como acceso directo a configuración. | 2026-08-05 | 1.4 |
| DEC-113 | Configuración separada | La configuración administrativa queda separada de la operación diaria. | 2026-08-05 | 1.4 |
| DEC-114 | Prioridad por frecuencia | La portada prioriza visualmente las operaciones consultadas con mayor frecuencia. | 2026-08-05 | 1.4 |
| DEC-115 | Accesos principales | Informes de ventas, informe de stock y Remitos de Entrada son accesos administrativos principales. | 2026-08-05 | 1.4 |
| DEC-116 | Configuraciones en segundo plano | Usuarios, permisos, sucursales, cajas, medios de pago y políticas quedan en configuración. | 2026-08-05 | 1.4 |
| DEC-117 | Panel por permisos efectivos | El panel administrativo se muestra según permisos efectivos del usuario. | 2026-08-05 | 1.4 |
| DEC-118 | Informes operativos | Los informes se orientan a consulta operativa, con tablas filtrables y trazabilidad. | 2026-08-05 | 1.4 |
| DEC-119 | Centro único de excepciones | Las situaciones revisables se concentran en un Centro de Excepciones administrativo. | 2026-08-05 | 1.4 |
| DEC-120 | Excepción sin reemplazo | La excepción no borra ni reemplaza el registro que la originó. | 2026-08-05 | 1.4 |
| DEC-121 | Configuración separada de operación | La configuración no debe mezclarse con las acciones operativas diarias. | 2026-08-05 | 1.4 |
| DEC-122 | Indicadores accionables | La portada administrativa muestra indicadores accionables, no gráficos decorativos. | 2026-08-05 | 1.4 |
| DEC-123 | Administración central en la nube | Administración será web, accesible desde la nube para usuarios autorizados. | 2026-08-05 | 1.4 |
| DEC-124 | Alcance por promoción | Las promociones definen su alcance dentro de cada promoción, no en la ficha del producto. | 2026-08-05 | 1.4 |
| DEC-125 | Exclusiones por conjuntos o códigos | El motor permite exclusiones por proveedores, categorías, códigos, productos, sucursales y canales. | 2026-08-05 | 1.4 |
| DEC-126 | Suspensión temporal | Una promoción puede suspender temporalmente otras promociones existentes. | 2026-08-05 | 1.4 |
| DEC-127 | Prevalece la exclusión | Si un artículo queda incluido y excluido, prevalece la exclusión. | 2026-08-05 | 1.4 |
| DEC-128 | Simulación previa | Administración puede simular una promoción antes de activarla. | 2026-08-05 | 1.4 |

## Web

| Código | Título | Descripción | Fecha | Versión |
|---|---|---|---|---|
| DEC-040 | Web propia posterior | La web propia se construirá después de validar la operación física. | 2026-07-27 | 1.1 |

## IA

| Código | Título | Descripción | Fecha | Versión |
|---|---|---|---|---|
| IA-001 | Recomendaciones explicables | Las recomendaciones de IA deben ser explicables dentro de reglas claras. | 2026-07-27 | 1.3 |

## Logística

| Código | Título | Descripción | Fecha | Versión |
|---|---|---|---|---|
| LOG-001 | Transferencias auditables | Las transferencias entre destinos deben conservar estado y trazabilidad. | 2026-07-27 | 1.3 |
| DEC-136 | Distribución integrada | La distribución inicial permanece integrada con la recepción. | 2026-08-05 | 1.4 |
| DEC-137 | Confirmación en destino | Cada local confirma recepción, etiquetado y habilitación para venta. | 2026-08-05 | 1.4 |
| DEC-138 | Complejidad oculta | La interfaz del operario oculta la complejidad interna de movimientos. | 2026-08-05 | 1.4 |
| DEC-139 | Reposición accesible | La reposición entre locales es accesible al personal de ventas autorizado. | 2026-08-05 | 1.4 |
| DEC-140 | Solicitud previa | Todo traslado entre locales se inicia con una solicitud previa. | 2026-08-05 | 1.4 |
| DEC-141 | Diferencias sin bloqueo | Una diferencia recibida se registra sin bloquear toda la recepción. | 2026-08-05 | 1.4 |
| DEC-142 | Alcance limitado | Logística se limita a confirmación en destino, reposición, tránsito, diferencias, permisos y auditoría. | 2026-08-05 | 1.4 |

## Sincronización

| Código | Título | Descripción | Fecha | Versión |
|---|---|---|---|---|
| DEC-143 | Operación local prioritaria | Toda operación presencial se confirma primero en la base local y no depende de Internet. | 2026-08-13 | 1.5 |
| DEC-144 | Eventos persistentes | Los cambios se transmitirán mediante una cola local persistente. | 2026-08-13 | 1.5 |
| DEC-145 | Idempotencia global | Los eventos podrán reenviarse sin duplicar efectos. | 2026-08-13 | 1.5 |
| DEC-146 | Autoridad por dato | Cada grupo de información tendrá una fuente principal. | 2026-08-13 | 1.5 |
| DEC-147 | Versionado central | Productos, precios, promociones, permisos y configuraciones tendrán versiones controladas. | 2026-08-13 | 1.5 |
| DEC-148 | Historial comercial inalterable | Las ventas finalizadas conservarán las reglas y precios utilizados originalmente. | 2026-08-13 | 1.5 |
| DEC-149 | Errores aislados | Un evento problemático no impedirá sincronizar otros eventos independientes. | 2026-08-13 | 1.5 |
| DEC-150 | Vigencia visible | Administración conocerá la fecha y hora de última sincronización de cada sucursal. | 2026-08-13 | 1.5 |
| DEC-151 | Base local compartida | Todos los equipos de cada local utilizan una única base local compartida mediante LAN. | 2026-08-13 | 1.5 |
| DEC-152 | Servidor local de sucursal | Cada local dispone de servicios locales para base, API y sincronización. | 2026-08-13 | 1.5 |
| DEC-153 | Administración Local | Los usuarios autorizados podrán consultar información local aun sin Internet. | 2026-08-13 | 1.5 |
| DEC-154 | Paquetes de actualización offline | La Central podrá producir archivos firmados y versionados para actualizar una sucursal desconectada. | 2026-08-13 | 1.5 |
| DEC-155 | Exportación manual de eventos | Una sucursal podrá exportar los eventos pendientes para incorporarlos manualmente a Central. | 2026-08-13 | 1.5 |
| DEC-156 | Protocolo único | Online y archivos utilizan los mismos eventos e identificadores. | 2026-08-13 | 1.5 |
| DEC-157 | Actualización única por sucursal | Un paquete se aplica una sola vez en el servidor local y beneficia a todos los puestos. | 2026-08-13 | 1.5 |
| DEC-158 | Archivo bajo demanda | Los archivos manuales serán exclusivamente un mecanismo de contingencia solicitado por un usuario autorizado. | 2026-08-13 | 1.5 |
| DEC-159 | Independencia de proveedor | ARD Suite deberá poder migrar su Central entre cloud y servidor propio sin alterar funcionalmente las sucursales. | 2026-08-13 | 1.5 |
| DEC-160 | Usuarios offline | Los usuarios previamente autorizados pueden seguir operando con los últimos permisos locales. | 2026-08-13 | 1.5 |
| DEC-161 | Transparencia para ventas | El operario de ventas no recibe alertas de Internet mientras la operación local esté disponible. | 2026-08-13 | 1.5 |
| DEC-162 | Desconexiones largas | Horas o días sin conexión no modifican la operación normal del local. | 2026-08-13 | 1.5 |
| DEC-163 | Sincronización continua | Los eventos se intentan enviar apenas se crean y se reintentan automáticamente. | 2026-08-13 | 1.5 |
| DEC-164 | Panel administrativo | Administración puede consultar estado, pendientes, errores y versiones de cada sucursal. | 2026-08-13 | 1.5 |

## Cambios y Créditos Comerciales

| Código | Título | Descripción | Fecha | Versión |
|---|---|---|---|---|
| DEC-061 | Valor histórico | Si se encuentra la venta, se utiliza el valor histórico reconocido. | 2026-07-27 | 1.2 |
| DEC-062 | Valor sugerido | Sin venta localizada, se sugiere el valor unitario de la oferta definida para cambios. | 2026-07-27 | 1.2 |
| DEC-063 | Modificación auditada | Toda modificación del valor requiere motivo, usuario y auditoría. | 2026-07-27 | 1.2 |
| DEC-064 | Sin recálculo histórico | El valor histórico no se recalcula con promociones actuales. | 2026-07-27 | 1.2 |
| DEC-065 | Procedimiento habitual | El sistema prioriza el procedimiento habitual. | 2026-07-27 | 1.2 |
| DEC-066 | Política global de valor | La política de reconocimiento de valor es global y configurable. | 2026-07-27 | 1.2 |
| DEC-067 | Varias prendas | Una operación de cambio admite varias prendas. | 2026-07-27 | 1.2 |
| DEC-068 | Sin entrega de dinero | Los cambios nunca generan entrega de dinero. | 2026-07-27 | 1.2 |
| DEC-069 | Saldo según política | El saldo a favor se administra según política global. | 2026-07-27 | 1.2 |
| DEC-070 | Crédito no efectivo | El Crédito Comercial no es efectivo ni un egreso de caja. | 2026-07-27 | 1.2 |
| DEC-073 | Aplicación parcial o total | El crédito se aplica total o parcialmente a una nueva venta. | 2026-07-27 | 1.2 |
| DEC-074 | Crédito futuro | Puede emitirse un Crédito Comercial para una compra futura. | 2026-07-27 | 1.2 |
| DEC-075 | Comprobante identificable | El comprobante de crédito tiene identificador único y QR o código de barras. | 2026-07-27 | 1.2 |
| DEC-076 | Uso parcial | El crédito puede utilizarse parcialmente hasta agotarse. | 2026-07-27 | 1.2 |
| DEC-077 | Vigencia configurable | Vigencia, asociación al cliente y transferibilidad son configurables. | 2026-07-27 | 1.2 |

# Registro de decisiones de arquitectura

Este registro reúne las decisiones aprobadas y vigentes. Los detalles de aplicación se encuentran en cada módulo.

## Producto, recepción y stock

| Código | Decisión |
|---|---|
| DEC-014 | Las promociones no generan productos nuevos. |
| DEC-015 | Se aplica la promoción más conveniente para el cliente. |
| DEC-017 | Toda decisión automática es explicable y auditable. |
| DEC-018 | Cada unidad conserva su precio aplicado. |
| DEC-020 | La política de cambios es global. |
| DEC-022 | Producto y atributos se mantienen separados. |
| DEC-028 | Una pantalla debe tener un objetivo principal. |
| DEC-029 | El código permanece visible en los procesos operativos. |
| DEC-030 | La carga de remitos prioriza productos existentes por código. |
| DEC-031 | Un producto existente se agrega sin abrir su ficha completa. |
| DEC-032 | El remito admite productos existentes y nuevos. |
| DEC-033 | Depósito muestra solo los atributos designados. |
| DEC-034 | La distribución se expresa en cantidades, no porcentajes. |
| DEC-035 | El modelo conceptual se define antes de las tablas físicas. |
| DEC-036 | El conteo se registra por combinación de atributos. |
| DEC-037 | La asignación vincula cantidad recibida y destino. |
| DEC-038 | Finalizar el remito genera movimientos auditables. |
| DEC-039 | Los prototipos aprobados forman parte del Knowledge Center. |
| DEC-165 | Las variantes se crean únicamente cuando existe una necesidad real. |
| DEC-166 | El Servicio Interno de Generación de Variantes resuelve variantes para Recepción, Importaciones, Procesos Administrativos y API. |
| DEC-167 | Las Familias de Atributos son plantillas reutilizables y no generan variantes, stock ni códigos. |

## Arquitectura operativa y reglas

| Código | Decisión |
|---|---|
| DEC-168 | El usuario trabaja con conceptos del negocio y no con identificadores internos. |
| DEC-169 | El Frontend traduce la interacción del usuario al formato requerido por la API sin implementar reglas de negocio. |
| DEC-170 | El Backend concentra la lógica del negocio, validaciones, auditoría, stock y consistencia. |
| DEC-171 | Toda regla importante debe existir una única vez y ser reutilizada por todas las interfaces. |
| DEC-172 | El Motor de Reglas es el único lugar donde se implementan las decisiones importantes del negocio. |
| DEC-173 | Services coordinan procesos, Policies toman decisiones y Rules realizan validaciones específicas. |

## Inventario

| Código | Decisión |
|---|---|
| DAT-STK-001 | Stock por variante y destino. |
| DAT-STK-002 | Todo cambio genera movimiento. |
| DAT-STK-003 | Historial auditable y saldo materializado. |
| DAT-STK-004 | Movimientos tipificados. |
| DAT-STK-005 | Documento u origen trazable. |
| DAT-STK-006 | Stock negativo permitido en salón. |
| DAT-STK-007 | Ajustes mediante movimientos compensatorios. |
| DAT-STK-008 | Identificador global e idempotencia. |
| DAT-STK-009 | La materialización de venta tiene prioridad. |
| DAT-STK-010 | Venta y evento pendiente deben persistirse atómicamente. |
| DAT-STK-011 | Inventario podrá procesarse fuera del camino crítico del POS. |
| DAT-STK-012 | Procesos pesados no deben ralentizar facturación. |
| DAT-STK-013 | StockActual se actualiza incrementalmente. |

## Venta local

| Código | Decisión |
|---|---|
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

## Precios

| Código | Decisión |
|---|---|
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

## Resolución comercial y cobro POS

| Código | Decisión |
|---|---|
| DAT-POS-001 | MedioPago y CondicionComercialPrecio son conceptos separados. |
| DAT-POS-002 | Toda venta nueva inicia valorizada con la condición comercial BASE. |
| DAT-POS-003 | La consulta o simulación comercial no persiste snapshot ni pagos definitivos. |
| DAT-POS-004 | El futuro POS podrá usar una condición o medio de visualización reversible durante la carga. |
| DAT-POS-005 | Una distribución de pagos admite múltiples medios y como máximo un RESTO. |
| DAT-POS-006 | El mismo algoritmo debe resolver pagos simples, mixtos y N medios. |
| DAT-POS-007 | La resolución debe minimizar el costo final para el cliente respetando los importes solicitados. |
| DAT-POS-008 | La unidad física se prioriza antes del fraccionamiento monetario. |
| DAT-POS-009 | La conversión proporcional entre condiciones es simétrica y usa Decimal. |
| DAT-POS-010 | El redondeo monetario de cobro sube al siguiente múltiplo configurable de 0,05. |
| DAT-POS-011 | La resolución debe generar una traza estructurada explicable. |
| DAT-POS-012 | La venta confirmada conserva snapshot histórico completo de la resolución. |
| DAT-POS-013 | Una venta CERRADA es inmutable. |
| DAT-POS-014 | Un error posterior al cierre se corrige mediante anulación explícita y nueva venta. |
| DAT-POS-015 | Confirmar cobro es una operación local y atómica. |
| DAT-POS-016 | El motor comercial no mueve stock y conserva el mecanismo de inventario existente. |

## Canales y arquitectura distribuida

| Código | Decisión |
|---|---|
| DEC-040 | La web propia se construirá después de validar la operación física. |
| DEC-041 | Cada sucursal tendrá una base local independiente. |
| DEC-042 | Toda venta presencial se registra primero localmente. |
| DEC-043 | La sincronización usa identificadores globales. |
| DEC-044 | La nube conserva el historial consolidado. |
| DEC-045 | Cada tipo de dato tiene una autoridad definida. |
| DEC-046 | La falta de Internet no impide vender. |

## Caja, pagos y venta en salón

| Código | Decisión |
|---|---|
| DEC-047 | La forma de pago participa en el cálculo comercial. |
| DEC-048 | Medio de pago y condición comercial se modelan por separado. |
| DEC-049 | Los cobros se administran separadamente por medio. |
| DEC-050 | La venta se recalcula antes de confirmarse. |
| DEC-051 | El pago mixto responde a políticas globales. |
| DEC-052 | El sistema optimiza la combinación de pagos. |
| DEC-053 | Se permiten límites disponibles o carga progresiva. |
| DEC-054 | La condición contado es configurable por medio. |
| DEC-055 | Se priorizan unidades o grupos completos. |
| DEC-056 | El recálculo es continuo. |
| DEC-057 | Una unidad parcialmente financiada pierde el beneficio de contado. |
| DEC-058 | Catálogo visual para artículos sin código individual. |
| DEC-059 | Venta por código, catálogo visual o ambos. |
| DEC-060 | La caja prioriza velocidad, simplicidad e información indispensable. |

## Cambios y créditos comerciales

| Código | Decisión |
|---|---|
| DEC-061 | Si se encuentra la venta, se utiliza el valor histórico reconocido. |
| DEC-062 | Sin venta localizada, se sugiere el valor unitario de la oferta definida para cambios. |
| DEC-063 | Toda modificación del valor requiere motivo, usuario y auditoría. |
| DEC-064 | El valor histórico no se recalcula con promociones actuales. |
| DEC-065 | El sistema prioriza el procedimiento habitual, aunque no sea el escenario ideal. |
| DEC-066 | La política de reconocimiento de valor es global y configurable. |
| DEC-067 | Una operación de cambio admite varias prendas. |
| DEC-068 | Los cambios nunca generan entrega de dinero. |
| DEC-069 | El saldo a favor se administra según política global. |
| DEC-070 | El Crédito Comercial no es efectivo ni un egreso de caja. |
| DEC-071 | La caja puede mantener varios remitos abiertos o suspendidos. |
| DEC-072 | Una venta suspendida conserva toda la información cargada. |
| DEC-073 | El crédito se aplica total o parcialmente a una nueva venta. |
| DEC-074 | Puede emitirse un Crédito Comercial para una compra futura. |
| DEC-075 | El comprobante de crédito tiene identificador único y QR o código de barras. |
| DEC-076 | El crédito puede utilizarse parcialmente hasta agotarse. |
| DEC-077 | Vigencia, asociación al cliente y transferibilidad son configurables. |

## Arqueo, turnos y movimientos de caja

| Código | Decisión |
|---|---|
| DEC-078 | Un arqueo puede realizarse sin cerrar el turno. |
| DEC-079 | El primer conteo es ciego: el cajero no ve el importe esperado. |
| DEC-080 | Solo se cuenta efectivo; los medios electrónicos los calcula el sistema. |
| DEC-081 | Administración define la tolerancia de diferencias. |
| DEC-082 | La primera revisión la realiza el mismo cajero mediante un flujo guiado. |
| DEC-083 | Toda corrección del medio de pago conserva el valor original y su auditoría. |
| DEC-084 | El turno puede cerrarse aunque exista una diferencia documentada. |
| DEC-085 | El próximo turno hereda el efectivo físico real confirmado. |
| DEC-086 | El fondo heredado puede corregirse al abrir el turno dejando motivo. |
| DEC-087 | Todo ingreso o egreso ajeno a una venta se registra como movimiento explícito de caja. |

## Administración, informes, permisos y promociones

| Código | Decisión |
|---|---|
| DEC-112 | Administración funciona como centro de navegación. |
| DEC-113 | La configuración se separa de la operación diaria. |
| DEC-114 | La portada prioriza accesos por frecuencia de uso. |
| DEC-115 | Informes de ventas, informe de stock y Remitos de Entrada son accesos administrativos principales. |
| DEC-116 | Las configuraciones permanecen en segundo plano. |
| DEC-117 | El panel administrativo se ajusta a permisos efectivos. |
| DEC-118 | Los informes se orientan a consulta operativa. |
| DEC-119 | Las excepciones se concentran en un centro único. |
| DEC-120 | La excepción no altera ni reemplaza el registro de origen. |
| DEC-121 | La configuración queda separada de la operación. |
| DEC-122 | La portada usa indicadores administrativos accionables. |
| DEC-123 | Administración central será accesible desde la nube. |
| DEC-124 | Las promociones definen su alcance dentro de cada promoción. |
| DEC-125 | Las exclusiones pueden definirse por conjuntos o códigos. |
| DEC-126 | Una promoción puede suspender temporalmente promociones existentes. |
| DEC-127 | Ante inclusión y exclusión simultánea, prevalece la exclusión. |
| DEC-128 | Las promociones pueden simularse antes de activarse. |

## Logística

| Código | Decisión |
|---|---|
| DEC-136 | La distribución inicial permanece integrada con la recepción. |
| DEC-137 | La confirmación y etiquetado se realizan en destino. |
| DEC-138 | La interfaz oculta la complejidad interna de movimientos. |
| DEC-139 | La reposición queda accesible al personal de ventas autorizado. |
| DEC-140 | Todo traslado entre locales requiere solicitud previa. |
| DEC-141 | Las diferencias recibidas se registran sin bloquear toda la recepción. |
| DEC-142 | El alcance de Logística queda limitado funcionalmente. |

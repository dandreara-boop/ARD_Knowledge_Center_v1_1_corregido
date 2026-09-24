# Historial de versiones

## Versión 2.1 — Resolución Comercial y Cobro del POS

- Se creó la página específica Sprint 8 — Resolución Comercial y Cobro del POS.
- Se documentó Sprint 8 como diseño comercial definido, solver seleccionado y probado preliminarmente, con implementación definitiva y QA pendientes.
- Se conectó conceptualmente el Motor de Venta Local del Sprint 6 con el Motor Comercial de Precios del Sprint 7.
- Se documentó la separación entre `MedioPago` y `CondicionComercialPrecio`.
- Se definió que toda venta nueva comienza valorizada con la condición comercial `BASE`.
- Se documentó la simulación reversible sin persistencia comercial definitiva.
- Se registró el requisito `REQ-POS-SIM` para futuro frontend POS.
- Se aprobó el diseño de pagos simples y mixtos con N medios, cero o un `RESTO`, conversión simétrica y menor total final para el cliente.
- Se documentó unidad física antes de fraccionamiento, fraccionamiento proporcional y redondeo monetario final por medio hacia arriba a `0,05` configurable.
- Se corrigió la decisión de redondeo: los fragmentos internos no se redondean individualmente y los importes fijos se respetan sin alterarlos.
- Se documentó la evolución técnica desde una estrategia greedy inicial, el problema de dependencia de orden y la búsqueda exacta, hasta el modelo LP/MILP.
- Se seleccionó HiGHS mediante `highspy` como solver técnico preliminar, encapsulado detrás de `CommercialOptimizer`.
- Se registró la prueba aislada del 24/09/2026 en Windows con Python `3.13.3`, `highspy` `1.15.1` y HiGHS `1.15.1`.
- Se documentaron benchmarks sintéticos preliminares hasta 100 unidades sin establecer SLA ni límites arbitrarios de ticket.
- Se asentó que ARD debe soportar Windows y Linux, pero la integración Linux y CI de Sprint 8 quedan pendientes.
- Se dejó explícito que `highspy` todavía no está incorporado formalmente a `requirements` ni al repositorio de implementación.
- Se definió la traza estructurada de resolución y el snapshot histórico de la venta confirmada.
- Se documentó que confirmar cobro es local, atómico y offline-first.
- Se preservó el mecanismo de inventario existente de Sprint 6.
- Se dejó fuera del alcance frontend POS definitivo, caja completa, promociones, bancos, cuotas, Tiendanube y nuevas funciones de sincronización cloud.
- Se incorporaron las decisiones `DAT-POS-001` a `DAT-POS-028`.

## Versión 2.0 — Motor Comercial de Precios

- Se creó la página específica Sprint 7 — Motor Comercial de Precios.
- Se documentó Sprint 7 como implementado y validado funcionalmente.
- Se documentaron `CondicionComercialPrecio`, `PrecioArticulo` y `AuditoriaPrecioArticulo`.
- Se definió que el precio comercial pertenece al Artículo y no a la Variante.
- Se documentaron condiciones `BASE` y derivadas, reglas Python tipadas y ausencia de fórmulas libres, `eval` o DSL dinámico.
- Se registraron redondeos `SIN_REDONDEO`, `ENTERO` y `MULTIPLO`, con `ROUND_CEILING` para múltiplos comerciales.
- Se documentó el cambio individual de precio `BASE` con recálculo atómico de derivados y eliminación de override manual.
- Se documentó que el cambio general de una regla requiere preview y aplicación explícita, sin recálculo silencioso.
- Se documentaron políticas `CONSERVAR_MANUALES` y `APLICAR_REGLA_A_TODOS`.
- Se dejó `REVISAR_EXCEPCIONES` como reservado conceptualmente, no como funcionalidad operativa implementada.
- Se documentó la auditoría sólo ante cambios efectivos de precio u origen.
- Se registró la migración `20260917_0006_pricing_engine.py` con `down_revision` `20260908_0005`.
- Se documentaron endpoints y errores comerciales implementados de precios.
- Se registró la validación automática y manual con resultado final `66 passed` usando `python -m pytest -p no:cacheprovider`.
- Se incorporaron las decisiones `DAT-PRICE-001` a `DAT-PRICE-011`.

## Versión 1.9 — Motor de Venta Local

- Se creó la página específica Sprint 6 — Motor de Venta Local.
- Se documentó Sprint 6 como implementado y validado funcionalmente.
- Se documentaron `Venta`, `DetalleVenta`, `PagoVenta` y `EventoPendiente` como outbox local.
- Se registró el cierre transaccional de venta mediante `POST /api/ventas/{venta_id}/finalizar`.
- Se documentó que `Venta CERRADA` y `VENTA_FINALIZADA` se guardan en la misma transacción.
- Se dejó explícito que inventario, sincronización, estadísticas y servicios externos no están en el camino crítico del POS.
- Se documentó el procesamiento posterior de `VENTA_FINALIZADA` reutilizando `InventoryService`.
- Se confirmó que el stock negativo sigue permitido y no bloquea la venta local.
- Se registró el incidente real de `global_id` de 48 caracteres y el error MariaDB `DataError 1406`.
- Se documentó la solución final con UUID5 determinístico y namespace fijo `8a248879-2d85-4e15-98f1-c769b5ed77cb`.
- Se documentó la prueba real de recuperación de evento `ERROR`, ausencia de doble descuento y evento `PROCESADO` no reaplicado.
- Se registró la migración `20260908_0005_sales_engine.py` posterior a `20260901_0004`.
- Se documentaron los endpoints y reglas implementadas del Sprint 6.
- Se registró la validación automática: 48 tests antes de la corrección y 50 tests después de la regresión UUID5/reintentos con `python -m pytest -p no:cacheprovider`.
- Se incorporaron las decisiones `DAT-SALE-001` a `DAT-SALE-011`.

## Versión 1.8 — Motor de Inventario

- Se incorporó el capítulo Motor de Inventario.
- Se documentó que el stock se registra por Variante, Destino de Inventario y Estado.
- Se definió el doble nivel MovimientoStock como historial auditable y StockActual como saldo materializado.
- Se estableció que StockActual se actualiza incrementalmente.
- Se documentaron tipos iniciales de destino, estados de stock y tipos de movimiento preparados.
- Se dejó asentada la idempotencia mediante global_id.
- Se documentó que el stock negativo está permitido en salón y no debe bloquear la venta presencial.
- Se incorporó el principio de prioridad operativa para POS.
- Se documentó que venta y evento pendiente deben persistirse atómicamente.
- Se dejó preparado el punto de integración con eventos de dominio sin documentar un bus completo.
- Se registró la validación de Sprint 5 con pruebas manuales, 39 tests automáticos aprobados y Alembic 20260901_0004 como HEAD.
- Se incorporaron las decisiones DAT-STK-001 a DAT-STK-013.

## Versión 1.7 — Motor de Reglas de Negocio

- Se incorporó el capítulo Principios de Arquitectura.
- Se aprobó el Principio de Abstracción Operativa.
- Se documentó que el usuario trabaja con conceptos del negocio y no con estructuras técnicas internas.
- Se definió la separación de responsabilidades entre Frontend, API, Services, Policies, Rules, Repositories y MariaDB.
- Se estableció que el Motor de Reglas es el único lugar donde se implementan las decisiones importantes del negocio.
- Se actualizó el estado del proyecto marcando Sprint 4 como finalizado.
- Se agregaron referencias cruzadas desde Visión, Modelo Conceptual, Gestión de Variantes y Recepción.

## Versión 1.6 — Variantes bajo demanda

- Se incorporó el capítulo Gestión de Variantes.
- Se documentó que las variantes se crean únicamente cuando existe una necesidad real.
- Se definió el Servicio Interno de Generación de Variantes como componente reutilizable para Recepción, Importaciones, Procesos Administrativos y API.
- Se incorporaron Familias de Atributos como plantillas reutilizables sin generación automática de variantes, stock ni códigos.
- Se actualizó Recepción de Mercadería para eliminar la generación manual de variantes del flujo operativo.
- Se agregaron referencias cruzadas desde Modelo Conceptual, Recepción y Administración.

## Versión 1.5 — Sincronización aprobada funcionalmente

- Se creó el módulo Sincronización como capítulo documental independiente.
- Se documentó la arquitectura local por sucursal con base compartida, API local, servicio de sincronización y red interna LAN.
- Se separó funcionalmente red interna e Internet para garantizar operación local offline.
- Se definieron Base Central, Administración Central, Administración Local, cola persistente, idempotencia, orden, dependencias y dirección de sincronización.
- Se documentaron usuarios offline, transparencia para ventas, desconexiones prolongadas y panel administrativo de sincronización.
- Se incorporaron paquetes manuales de contingencia sin crear un sistema paralelo.
- Se dejó asentada la independencia respecto de DigitalOcean y las etapas de infraestructura.
- Se incorporó el bloque de decisiones de Sincronización en el registro agrupado.
- Se actualizó el mapa de avance: Administración aprobada para desarrollo, Logística definida funcionalmente, Sincronización aprobada funcionalmente para desarrollo y Modelo de Datos como próximo módulo.

## Versión 1.4 — Administración y Logística definidas

- Se marcó Administración como **APROBADO PARA DESARROLLO**.
- Se documentó Administración Central en la nube e informes consolidados con vigencia de sincronización.
- Se completó Usuarios y Permisos con tipos configurables, alcances, excepciones individuales y autorizaciones puntuales.
- Se actualizó el Centro de Excepciones con categorías, estados, datos conservados y regla de no reemplazo del origen.
- Se creó el submódulo Motor de Promociones con reglas de alcance, exclusiones, suspensión y simulación previa.
- Se marcó Logística como **DEFINIDO FUNCIONALMENTE** y se limitó su alcance.
- Se documentó distribución inicial integrada con recepción, confirmación en destino, diferencias sin bloqueo y reposición entre locales.
- Se incorporaron DEC-112 a DEC-128 y DEC-136 a DEC-142 sin completar numeración faltante.
- Se dejó Sincronización como próximo módulo a definir.

## Versión 1.3 — Documento Maestro de Arquitectura Funcional

- Se convirtió el Knowledge Center en Documento Maestro de Arquitectura Funcional.
- Se crearon capítulos maestros para Recepción de Mercadería, Venta en Salón, Cambios y Crédito Comercial, Anulación, Caja, Administración, Logística y Venta Web.
- Se integró la información existente dentro de capítulos leíbles de principio a fin.
- Se creó el capítulo específico de Usuarios y Permisos.
- Se creó el Centro de Excepciones.
- Se creó el Modelo de Datos funcional por entidades y módulos.
- Se creó el catálogo estándar de Wireframes WF-001 a WF-009.
- Se reorganizó el Registro de Decisiones por grupos: General, Recepción, Venta, Caja, Administración, Web, IA y Logística.
- Se eliminó el concepto funcional de entrega de dinero dentro del flujo de cambios, dejando documentado Cambio → Crédito Comercial.
- Se mantuvo FastAPI, Jinja2, login, rutas existentes, imágenes y tecnología actual.

## Versión 1.2 — Cambios, Créditos Comerciales y Arqueo de Caja

- Se documentó el proceso completo de cambios con y sin venta original.
- Se incorporó la recepción de múltiples prendas dentro de una misma operación.
- Se definió el Crédito Comercial, su uso parcial y su comprobante con QR o código de barras.
- Se documentó la posibilidad de mantener varias ventas abiertas o suspendidas.
- Se agregó **WF-008 Arqueo y Cierre de Caja** con su imagen de revisión.
- Se distinguió el arqueo de control del cierre formal del turno.
- Se incorporó la apertura con fondo heredado y posibilidad de corrección.
- Se definió el conteo ciego de efectivo.
- Se incorporó la revisión guiada de medios de pago y sus correcciones auditables.
- Se definió el cierre permitido con diferencia y la herencia del efectivo real.
- Se documentaron fondo inicial, refuerzos, retiros, gastos y ajustes como movimientos de caja.
- Se consolidaron las decisiones DEC-061 a DEC-087.

## Versión 1.1 — Venta en Salón y Caja

- Se incorporó la especificación funcional completa de la pantalla **WF-004 Caja de Venta**.
- Se incorporó **WF-005 Catálogo Visual de Artículos sin Código**.
- Se añadieron las imágenes aprobadas de ambas pantallas.
- Se documentaron medios de pago, condición comercial, pagos mixtos y promociones.
- Se documentó la regla de unidad o grupo promocional completo para obtener el beneficio de contado.
- Se agregó la flecha para completar automáticamente el saldo pendiente por medio de pago.
- Se confirmó el recálculo automático permanente.
- Se consolidaron las decisiones DEC-047 a DEC-060.
- Se amplió el menú lateral del Módulo 2.
- Se corrigió la iteración del menú lateral para evitar el error de Jinja con `section.items`.

## Versión 1.0 — Nueva generación del sitio

- Sitio reconstruido desde cero.
- Organización por lineamientos generales y módulos funcionales.
- Dashboard del proyecto.
- Navegación lateral permanente.
- Fichas de módulos.
- Buscador.
- Diseño responsive.
- Migración de los conceptos principales.
- Incorporación de mockups aprobados de Carga de Productos.

# Historial de versiones

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

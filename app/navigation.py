from __future__ import annotations

PROJECT_INFO = {
    "name": "ARD Suite",
    "subtitle": "Documento Maestro de Arquitectura Funcional",
    "version": "v2.1",
    "status": "Sprint 1 a Sprint 7 finalizados; Sprint 8 aprobado funcionalmente",
    "description": (
        "Centro documental para lineamientos, modulos funcionales, modelo de datos, "
        "wireframes, decisiones e historial del proyecto."
    ),
}

PROJECT_PROGRESS = [
    {"name": "Sprint 1 — Infraestructura Base", "progress": 100, "visual": "✓ Finalizado"},
    {"name": "Sprint 2 — Catálogo Comercial", "progress": 100, "visual": "✓ Finalizado"},
    {"name": "Sprint 3 — Servicio Interno de Generación de Variantes", "progress": 100, "visual": "✓ Finalizado"},
    {"name": "Sprint 4 — Motor de Reglas de Negocio", "progress": 100, "visual": "✓ Finalizado"},
    {"name": "Sprint 5 — Motor de Inventario", "progress": 100, "visual": "✓ Finalizado"},
    {"name": "Sprint 6 — Motor de Venta Local", "progress": 100, "visual": "✓ Finalizado y validado"},
    {"name": "Sprint 7 — Motor Comercial de Precios", "progress": 100, "visual": "✓ Finalizado y validado"},
    {"name": "Sprint 8 — Resolución Comercial y Cobro del POS", "progress": 100, "visual": "DISEÑO FUNCIONAL APROBADO"},
    {"name": "Recepción de Mercadería", "progress": 100, "visual": "██████████ 100%"},
    {"name": "Venta en Salón", "progress": 90, "visual": "█████████░ 90%"},
    {"name": "Caja", "progress": 80, "visual": "████████░░ 80%"},
    {"name": "Administración", "progress": 100, "visual": "APROBADO PARA DESARROLLO"},
    {"name": "Logística", "progress": 100, "visual": "DEFINIDO FUNCIONALMENTE"},
    {"name": "Sincronización", "progress": 100, "visual": "APROBADO FUNCIONALMENTE PARA DESARROLLO"},
    {"name": "Venta Web", "progress": 20, "visual": "██░░░░░░░░ 20%"},
    {"name": "IA", "progress": 10, "visual": "█░░░░░░░░░ 10%"},
]

MODULE_INDEXES = {
    "recepcion": {
        "title": "Recepción",
        "module": "Módulo 1",
        "description": "Índice documental del módulo de recepción de mercadería.",
        "doc_slug": "modulos/recepcion/documento_maestro",
    },
    "venta": {
        "title": "Venta",
        "module": "Módulo 2",
        "description": "Índice documental del módulo de venta en salón.",
        "doc_slug": "modulos/venta_salon/documento_maestro",
    },
    "caja": {
        "title": "Caja",
        "module": "Módulo 2",
        "description": "Índice documental del flujo de caja.",
        "doc_slug": "modulos/caja/documento_maestro",
    },
    "creditos": {
        "title": "Créditos",
        "module": "Módulo 2",
        "description": "Índice documental para créditos y saldos a favor.",
        "doc_slug": "modulos/cambios/documento_maestro",
    },
    "cambios": {
        "title": "Cambios",
        "module": "Módulo 2",
        "description": "Índice documental del módulo de cambios y Crédito Comercial.",
        "doc_slug": "modulos/cambios/documento_maestro",
    },
    "anulacion": {
        "title": "Anulación",
        "module": "Módulo 2",
        "description": "Índice documental del módulo de anulación.",
        "doc_slug": "modulos/anulacion/documento_maestro",
    },
    "administracion": {
        "title": "Administración",
        "module": "Módulo 3",
        "description": "Índice documental del módulo administrativo.",
        "doc_slug": "modulos/administracion/documento_maestro",
    },
    "logistica": {
        "title": "Logística",
        "module": "Módulo 4",
        "description": "Índice documental del módulo logístico.",
        "doc_slug": "modulos/logistica/documento_maestro",
    },
    "sincronizacion": {
        "title": "Sincronización",
        "module": "Módulo 5",
        "description": "Índice documental del módulo de sincronización distribuida.",
        "doc_slug": "modulos/sincronizacion/documento_maestro",
    },
    "venta-web": {
        "title": "Venta Web",
        "module": "Módulo 6",
        "description": "Índice documental del canal de venta web.",
        "doc_slug": "modulos/venta_web/documento_maestro",
    },
}

INDEX_PAGES = {
    "modelo-datos": {
        "title": "Modelo de Datos",
        "description": "Índice consolidado para los documentos de datos del proyecto.",
        "doc_slug": "modelo_datos/documento_maestro",
    },
    "wireframes": {
        "title": "Wireframes",
        "description": "Índice visual preparado para centralizar pantallas y prototipos.",
        "doc_slug": "wireframes/documento_maestro",
    },
}

NAVIGATION = [
    {"title": "Inicio", "icon": "⌂", "route": "/", "order": 10},
    {
        "title": "Lineamientos Generales",
        "icon": "◇",
        "route": "/doc/general/vision",
        "order": 20,
        "children": [
            {"title": "Visión y filosofía", "icon": "•", "route": "/doc/general/vision", "doc_slug": "general/vision", "order": 10},
            {
                "title": "Arquitectura distribuida",
                "icon": "•",
                "route": "/doc/general/arquitectura_distribuida",
                "doc_slug": "general/arquitectura_distribuida",
                "order": 20,
            },
        ],
    },
    {
        "title": "Modelo Conceptual",
        "icon": "◎",
        "route": "/doc/general/modelo_conceptual",
        "doc_slug": "general/modelo_conceptual",
        "order": 30,
        "children": [
            {"title": "Gestión de Variantes", "icon": "•", "route": "/doc/general/gestion_variantes", "doc_slug": "general/gestion_variantes", "order": 10},
            {"title": "Principios de Arquitectura", "icon": "•", "route": "/doc/general/principios_arquitectura", "doc_slug": "general/principios_arquitectura", "order": 20},
            {"title": "Motor de Inventario", "icon": "•", "route": "/doc/general/motor_inventario", "doc_slug": "general/motor_inventario", "order": 30},
        ],
    },
    {
        "title": "Módulo 1",
        "icon": "□",
        "route": None,
        "order": 40,
        "children": [
            {
                "title": "Recepción",
                "icon": "↧",
                "route": "/doc/modulos/recepcion/documento_maestro",
                "doc_slug": "modulos/recepcion/documento_maestro",
                "order": 10,
                "children": [
                    {"title": "Ficha del módulo", "icon": "•", "route": "/doc/modulos/carga_productos/resumen", "doc_slug": "modulos/carga_productos/resumen", "order": 10},
                    {"title": "Flujo operativo", "icon": "•", "route": "/doc/modulos/carga_productos/flujo", "doc_slug": "modulos/carga_productos/flujo", "order": 20},
                    {"title": "Modelo de datos", "icon": "•", "route": "/doc/modulos/carga_productos/datos", "doc_slug": "modulos/carga_productos/datos", "order": 30},
                    {"title": "Pantallas", "icon": "•", "route": "/doc/modulos/carga_productos/pantallas", "doc_slug": "modulos/carga_productos/pantallas", "order": 40},
                    {"title": "Decisiones", "icon": "•", "route": "/doc/modulos/carga_productos/decisiones", "doc_slug": "modulos/carga_productos/decisiones", "order": 50},
                ],
            },
        ],
    },
    {
        "title": "Módulo 2",
        "icon": "▣",
        "route": None,
        "order": 50,
        "children": [
            {
                "title": "Venta",
                "icon": "◴",
                "route": "/doc/modulos/venta_salon/documento_maestro",
                "doc_slug": "modulos/venta_salon/documento_maestro",
                "order": 10,
                "children": [
                    {"title": "Ficha del módulo", "icon": "•", "route": "/doc/modulos/venta_salon/resumen", "doc_slug": "modulos/venta_salon/resumen", "order": 10},
                    {"title": "Arquitectura local/nube", "icon": "•", "route": "/doc/modulos/venta_salon/arquitectura", "doc_slug": "modulos/venta_salon/arquitectura", "order": 20},
                    {"title": "Sprint 6 — Motor de Venta Local", "icon": "•", "route": "/doc/modulos/venta_salon/sprint_6_motor_venta_local", "doc_slug": "modulos/venta_salon/sprint_6_motor_venta_local", "order": 30},
                    {"title": "Sprint 7 — Motor Comercial de Precios", "icon": "•", "route": "/doc/modulos/venta_salon/sprint_7_motor_comercial_precios", "doc_slug": "modulos/venta_salon/sprint_7_motor_comercial_precios", "order": 40},
                    {"title": "Sprint 8 — Resolución Comercial y Cobro", "icon": "•", "route": "/doc/modulos/venta_salon/sprint_8_resolucion_comercial_cobro_pos", "doc_slug": "modulos/venta_salon/sprint_8_resolucion_comercial_cobro_pos", "order": 50},
                    {"title": "Flujo operativo", "icon": "•", "route": "/doc/modulos/venta_salon/flujo", "doc_slug": "modulos/venta_salon/flujo", "order": 60},
                    {"title": "Promociones y precios", "icon": "•", "route": "/doc/modulos/venta_salon/promociones", "doc_slug": "modulos/venta_salon/promociones", "order": 70},
                ],
            },
            {
                "title": "Caja",
                "icon": "$",
                "route": "/doc/modulos/caja/documento_maestro",
                "doc_slug": "modulos/caja/documento_maestro",
                "order": 20,
                "children": [
                    {"title": "WF-004 Caja de Venta", "icon": "•", "route": "/doc/modulos/venta_salon/wf004_caja", "doc_slug": "modulos/venta_salon/wf004_caja", "order": 10},
                    {"title": "WF-008 Arqueo de Caja", "icon": "•", "route": "/doc/modulos/venta_salon/wf008_arqueo_caja", "doc_slug": "modulos/venta_salon/wf008_arqueo_caja", "order": 20},
                    {"title": "Medios de pago", "icon": "•", "route": "/doc/modulos/venta_salon/medios_pago", "doc_slug": "modulos/venta_salon/medios_pago", "order": 30},
                    {"title": "Pagos mixtos", "icon": "•", "route": "/doc/modulos/venta_salon/pagos_mixtos", "doc_slug": "modulos/venta_salon/pagos_mixtos", "order": 40},
                ],
            },
            {"title": "Cambios", "icon": "↻", "route": "/doc/modulos/cambios/documento_maestro", "doc_slug": "modulos/cambios/documento_maestro", "order": 30},
            {"title": "Anulación", "icon": "!", "route": "/doc/modulos/anulacion/documento_maestro", "doc_slug": "modulos/anulacion/documento_maestro", "order": 40},
            {"title": "Créditos", "icon": "◧", "route": "/doc/modulos/cambios/documento_maestro", "doc_slug": "modulos/cambios/documento_maestro", "order": 50},
        ],
    },
    {
        "title": "Módulo 3",
        "icon": "⚙",
        "route": None,
        "order": 60,
        "children": [
            {"title": "Administración", "icon": "▤", "route": "/doc/modulos/administracion/documento_maestro", "doc_slug": "modulos/administracion/documento_maestro", "order": 10},
            {"title": "Ficha del módulo", "icon": "•", "route": "/doc/modulos/administracion/resumen", "doc_slug": "modulos/administracion/resumen", "order": 20},
            {"title": "Informes desde la nube", "icon": "•", "route": "/doc/modulos/administracion/informes_nube", "doc_slug": "modulos/administracion/informes_nube", "order": 30},
            {"title": "Usuarios y Permisos", "icon": "•", "route": "/doc/modulos/usuarios_permisos/documento_maestro", "doc_slug": "modulos/usuarios_permisos/documento_maestro", "order": 40},
            {"title": "Centro de Excepciones", "icon": "•", "route": "/doc/modulos/centro_excepciones/documento_maestro", "doc_slug": "modulos/centro_excepciones/documento_maestro", "order": 50},
            {"title": "Motor de Promociones", "icon": "•", "route": "/doc/modulos/administracion/motor_promociones", "doc_slug": "modulos/administracion/motor_promociones", "order": 60},
        ],
    },
    {
        "title": "Módulo 4",
        "icon": "⇄",
        "route": None,
        "order": 70,
        "children": [
            {"title": "Logística", "icon": "↔", "route": "/doc/modulos/logistica/documento_maestro", "doc_slug": "modulos/logistica/documento_maestro", "order": 10},
            {"title": "Ficha del módulo", "icon": "•", "route": "/doc/modulos/logistica/resumen", "doc_slug": "modulos/logistica/resumen", "order": 20},
        ],
    },
    {
        "title": "Módulo 5",
        "icon": "~",
        "route": None,
        "order": 80,
        "children": [
            {"title": "Sincronización", "icon": "⇆", "route": "/doc/modulos/sincronizacion/documento_maestro", "doc_slug": "modulos/sincronizacion/documento_maestro", "order": 10},
        ],
    },
    {
        "title": "Módulo 6",
        "icon": "○",
        "route": None,
        "order": 85,
        "children": [
            {"title": "Venta Web", "icon": "▥", "route": "/doc/modulos/venta_web/documento_maestro", "doc_slug": "modulos/venta_web/documento_maestro", "order": 10},
            {"title": "Ficha del módulo", "icon": "•", "route": "/doc/modulos/inteligencia_comercial/resumen", "doc_slug": "modulos/inteligencia_comercial/resumen", "order": 20},
            {"title": "Tiendanube y web propia", "icon": "•", "route": "/doc/modulos/inteligencia_comercial/tiendanube", "doc_slug": "modulos/inteligencia_comercial/tiendanube", "order": 30},
        ],
    },
    {"title": "Modelo de Datos", "icon": "▦", "route": "/doc/modelo_datos/documento_maestro", "doc_slug": "modelo_datos/documento_maestro", "order": 90},
    {"title": "Wireframes", "icon": "▧", "route": "/doc/wireframes/documento_maestro", "doc_slug": "wireframes/documento_maestro", "order": 100},
    {
        "title": "Registro de Decisiones",
        "icon": "✓",
        "route": "/doc/referencias/decisiones_agrupadas",
        "doc_slug": "referencias/decisiones_agrupadas",
        "order": 110,
        "children": [
            {"title": "Decisiones agrupadas", "icon": "•", "route": "/doc/referencias/decisiones_agrupadas", "doc_slug": "referencias/decisiones_agrupadas", "order": 10},
            {"title": "Registro base v1.2", "icon": "•", "route": "/doc/referencias/decisiones", "doc_slug": "referencias/decisiones", "order": 20},
        ],
    },
    {"title": "Diccionario", "icon": "≡", "route": "/doc/referencias/diccionario", "doc_slug": "referencias/diccionario", "order": 120},
    {"title": "Historial", "icon": "◷", "route": "/doc/referencias/historial", "doc_slug": "referencias/historial", "order": 130},
]


def iter_navigation_items(items=None):
    if items is None:
        items = NAVIGATION
    for item in items:
        yield item
        yield from iter_navigation_items(item.get("children", []))


def sorted_navigation(items=None):
    if items is None:
        items = NAVIGATION
    normalized = []
    for item in items:
        copied = {**item}
        children = copied.get("children", [])
        if children:
            copied["children"] = sorted_navigation(children)
        normalized.append(copied)
    return sorted(normalized, key=lambda item: item.get("order", 0))

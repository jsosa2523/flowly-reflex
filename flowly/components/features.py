"""Sección de características de Flowly."""
import reflex as rx


FEATURES = [
    {
        "icon": "layout-dashboard",
        "title": "Tableros Kanban",
        "desc": "Visualiza el flujo de trabajo con drag-and-drop intuitivo y vistas personalizables por equipo.",
        "color": "violet",
    },
    {
        "icon": "chart-bar",
        "title": "Analíticas en tiempo real",
        "desc": "Métricas de productividad, velocidad de sprint y reportes automatizados con un clic.",
        "color": "blue",
    },
    {
        "icon": "brain",
        "title": "IA integrada",
        "desc": "Sugerencias inteligentes, asignación automática de prioridades y resúmenes diarios generados por IA.",
        "color": "violet",
    },
    {
        "icon": "messages",
        "title": "Chat contextual",
        "desc": "Comunícate directamente en cada tarea sin salir de la plataforma. Todo en contexto.",
        "color": "teal",
    },
    {
        "icon": "clock",
        "title": "Time tracking",
        "desc": "Registra tiempo por tarea automáticamente y genera reportes de horas para facturación.",
        "color": "amber",
    },
    {
        "icon": "shield-lock",
        "title": "Permisos granulares",
        "desc": "Control total de acceso por rol, proyecto o miembro del equipo. Cumplimiento SOC 2.",
        "color": "green",
    },
]

COLOR_MAP = {
    "violet": ("violet", 3, 9, 11),
    "blue": ("blue", 3, 9, 11),
    "teal": ("teal", 3, 8, 11),
    "amber": ("amber", 3, 9, 11),
    "green": ("green", 3, 9, 11),
}


def feature_card(icon: str, title: str, desc: str, color: str) -> rx.Component:
    c, bg_shade, icon_shade, _ = COLOR_MAP.get(color, ("violet", 3, 9, 11))
    return rx.box(
        rx.vstack(
            # Ícono
            rx.box(
                rx.icon(icon, size=20, color=rx.color(c, icon_shade)),
                width="40px",
                height="40px",
                border_radius="10px",
                background_color=rx.color(c, bg_shade),
                display="flex",
                align_items="center",
                justify_content="center",
            ),
            rx.text(title, font_size="15px", font_weight="500"),
            rx.text(desc, font_size="13px", color=rx.color("gray", 10), line_height="1.6"),
            spacing="3",
            align="start",
        ),
        background_color=rx.color("gray", 2),
        border=f"1px solid {rx.color('gray', 4)}",
        border_radius="14px",
        padding="1.25rem",
        transition="transform 0.2s, box-shadow 0.2s",
        _hover={
            "transform": "translateY(-2px)",
            "box_shadow": "0 8px 24px rgba(0,0,0,0.07)",
        },
    )


def features_section() -> rx.Component:
    return rx.box(
        rx.container(
            # Header
            rx.vstack(
                rx.text(
                    "FUNCIONALIDADES",
                    font_size="11px",
                    font_weight="500",
                    letter_spacing="1.5px",
                    color=rx.color("gray", 10),
                ),
                rx.heading(
                    "Todo lo que tu equipo necesita",
                    font_family="'Syne', sans-serif",
                    font_size=["24px", "30px", "34px"],
                    font_weight="800",
                    letter_spacing="-0.5px",
                    as_="h2",
                    text_align="center",
                ),
                rx.text(
                    "Sin integraciones complicadas. Todo incluido desde el día uno.",
                    font_size="15px",
                    color=rx.color("gray", 10),
                    text_align="center",
                ),
                spacing="2",
                align="center",
                margin_bottom="2.5rem",
            ),
            # Grid de features
            rx.grid(
                *[
                    feature_card(
                        feat["icon"],
                        feat["title"],
                        feat["desc"],
                        feat["color"],
                    )
                    for feat in FEATURES
                ],
                columns=["1", "2", "3"],
                spacing="4",
                width="100%",
            ),
            max_width="1100px",
        ),
        padding=["3rem 1.5rem", "4rem 2rem"],
        width="100%",
        background_color=rx.color("gray", 1),
    )

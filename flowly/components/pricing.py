"""Sección de precios de Flowly."""
import reflex as rx


PLANS = [
    {
        "name": "Starter",
        "price": "$0",
        "period": "gratis para siempre",
        "description": "Ideal para freelancers y equipos pequeños que están comenzando.",
        "features": [
            "Hasta 3 proyectos activos",
            "5 miembros por equipo",
            "2 GB de almacenamiento",
            "Tableros Kanban básicos",
            "Soporte por email",
        ],
        "cta": "Comenzar gratis",
        "featured": False,
        "badge": None,
    },
    {
        "name": "Pro",
        "price": "$19",
        "period": "por usuario / mes",
        "description": "Para equipos en crecimiento que necesitan más potencia y automatización.",
        "features": [
            "Proyectos ilimitados",
            "Hasta 20 miembros",
            "50 GB de almacenamiento",
            "IA integrada y automatizaciones",
            "Analíticas avanzadas",
            "Time tracking",
            "Soporte prioritario",
        ],
        "cta": "Empezar prueba gratuita",
        "featured": True,
        "badge": "Más popular",
    },
    {
        "name": "Enterprise",
        "price": "Custom",
        "period": "contacta ventas",
        "description": "Para organizaciones grandes con necesidades de seguridad y compliance.",
        "features": [
            "Todo lo de Pro incluido",
            "Miembros ilimitados",
            "Almacenamiento ilimitado",
            "SSO / SAML",
            "SLA garantizado 99.99%",
            "Onboarding dedicado",
            "Auditoría SOC 2 Type II",
        ],
        "cta": "Contactar ventas",
        "featured": False,
        "badge": None,
    },
]


def check_item(text: str) -> rx.Component:
    return rx.hstack(
        rx.icon("check", size=14, color=rx.color("green", 9)),
        rx.text(text, font_size="13px", color=rx.color("gray", 11)),
        spacing="2",
        align="center",
    )


def pricing_card(plan: dict) -> rx.Component:
    is_featured = plan["featured"]
    return rx.box(
        rx.vstack(
            # Badge opcional
            rx.cond(
                plan["badge"] is not None,
                rx.box(
                    rx.text(
                        plan["badge"] or "",
                        font_size="11px",
                        font_weight="500",
                        color=rx.color("violet", 11),
                    ),
                    background_color=rx.color("violet", 3),
                    padding="3px 10px",
                    border_radius="20px",
                    display="inline-block",
                    align_self="start",
                ),
                rx.box(height="22px"),
            ),
            # Nombre del plan
            rx.text(
                plan["name"],
                font_family="'Syne', sans-serif",
                font_size="18px",
                font_weight="800",
            ),
            # Precio
            rx.hstack(
                rx.text(
                    plan["price"],
                    font_family="'Syne', sans-serif",
                    font_size="36px",
                    font_weight="800",
                    color=rx.color("violet", 9) if is_featured else rx.color("gray", 12),
                ),
                rx.text(
                    plan["period"],
                    font_size="12px",
                    color=rx.color("gray", 10),
                    align_self="end",
                    padding_bottom="6px",
                ),
                align="end",
                spacing="1",
            ),
            # Descripción
            rx.text(
                plan["description"],
                font_size="13px",
                color=rx.color("gray", 10),
                line_height="1.5",
            ),
            rx.separator(width="100%", color=rx.color("gray", 4)),
            # Lista de features
            rx.vstack(
                *[check_item(feat) for feat in plan["features"]],
                spacing="2",
                align="start",
                width="100%",
            ),
            # Botón CTA
            rx.button(
                plan["cta"],
                width="100%",
                border_radius="8px",
                height="40px",
                font_size="14px",
                font_weight="500",
                cursor="pointer",
                background_color=rx.color("violet", 9) if is_featured else "transparent",
                color="white" if is_featured else rx.color("gray", 12),
                border=f"1px solid {rx.color('gray', 6)}" if not is_featured else "none",
                _hover={
                    "background_color": rx.color("violet", 10) if is_featured else rx.color("gray", 3),
                },
                transition="background-color 0.2s",
            ),
            spacing="4",
            align="start",
            width="100%",
        ),
        background_color=rx.color("gray", 1),
        border=(
            f"2px solid {rx.color('violet', 8)}"
            if is_featured
            else f"1px solid {rx.color('gray', 4)}"
        ),
        border_radius="16px",
        padding="1.5rem",
        box_shadow="0 8px 32px rgba(83,74,183,0.12)" if is_featured else "none",
        position="relative",
    )


def pricing_section() -> rx.Component:
    return rx.box(
        rx.container(
            # Header
            rx.vstack(
                rx.text(
                    "PLANES",
                    font_size="11px",
                    font_weight="500",
                    letter_spacing="1.5px",
                    color=rx.color("gray", 10),
                ),
                rx.heading(
                    "Elige tu plan",
                    font_family="'Syne', sans-serif",
                    font_size=["24px", "30px", "34px"],
                    font_weight="800",
                    letter_spacing="-0.5px",
                    as_="h2",
                    text_align="center",
                ),
                rx.text(
                    "Sin tarjeta de crédito para empezar. Cancela cuando quieras.",
                    font_size="15px",
                    color=rx.color("gray", 10),
                    text_align="center",
                ),
                spacing="2",
                align="center",
                margin_bottom="2.5rem",
            ),
            # Grid de precios
            rx.grid(
                *[pricing_card(plan) for plan in PLANS],
                columns=["1", "1", "3"],
                spacing="4",
                align="start",
                width="100%",
            ),
            max_width="1100px",
        ),
        padding=["3rem 1.5rem", "4rem 2rem"],
        width="100%",
        background_color=rx.color("gray", 2),
    )

"""Barra de navegación de Flowly."""
import reflex as rx


def nav_link(text: str) -> rx.Component:
    return rx.link(
        text,
        href="#",
        color=rx.color("gray", 11),
        font_size="14px",
        text_decoration="none",
        _hover={"color": rx.color("gray", 12)},
        transition="color 0.2s",
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.flex(
            # Logo
            rx.text(
                "Flowly",
                font_family="'Syne', sans-serif",
                font_weight="800",
                font_size="22px",
                letter_spacing="-0.5px",
                color=rx.color("gray", 12),
            ),
            # Links de navegación (ocultos en mobile)
            rx.desktop_only(
                rx.hstack(
                    nav_link("Producto"),
                    nav_link("Precios"),
                    nav_link("Blog"),
                    nav_link("Empresa"),
                    spacing="6",
                )
            ),
            # Botones de acción
            rx.hstack(
                rx.link(
                    rx.button(
                        "Iniciar sesión",
                        variant="ghost",
                        color=rx.color("gray", 11),
                        font_size="14px",
                        cursor="pointer",
                    ),
                    href="#",
                ),
                rx.button(
                    "Comenzar gratis",
                    background_color=rx.color("violet", 9),
                    color="white",
                    border_radius="8px",
                    font_size="14px",
                    font_weight="500",
                    padding="0 18px",
                    height="36px",
                    cursor="pointer",
                    _hover={"background_color": rx.color("violet", 10)},
                    transition="background-color 0.2s",
                ),
                spacing="3",
                align="center",
            ),
            justify="between",
            align="center",
            width="100%",
        ),
        padding="0 2rem",
        height="64px",
        border_bottom=f"1px solid {rx.color('gray', 4)}",
        background_color=rx.color("gray", 1),
        position="sticky",
        top="0",
        z_index="100",
        backdrop_filter="blur(8px)",
        width="100%",
    )

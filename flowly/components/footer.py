"""Footer de Flowly."""
import reflex as rx


FOOTER_LINKS = {
    "Producto": ["Características", "Precios", "Roadmap", "Changelog"],
    "Empresa": ["Sobre nosotros", "Blog", "Carreras", "Prensa"],
    "Soporte": ["Documentación", "Centro de ayuda", "Comunidad", "Estado"],
    "Legal": ["Privacidad", "Términos", "Seguridad", "Cookies"],
}


def footer_column(title: str, links: list) -> rx.Component:
    return rx.vstack(
        rx.text(
            title,
            font_size="13px",
            font_weight="600",
            color=rx.color("gray", 12),
            margin_bottom="0.5rem",
        ),
        *[
            rx.link(
                link,
                href="#",
                font_size="13px",
                color=rx.color("gray", 10),
                text_decoration="none",
                _hover={"color": rx.color("gray", 12)},
                transition="color 0.2s",
            )
            for link in links
        ],
        spacing="2",
        align="start",
    )


def footer() -> rx.Component:
    return rx.box(
        rx.container(
            # Parte superior: logo + columnas de links
            rx.flex(
                # Logo y descripción
                rx.vstack(
                    rx.text(
                        "Flowly",
                        font_family="'Syne', sans-serif",
                        font_weight="800",
                        font_size="22px",
                        letter_spacing="-0.5px",
                        color=rx.color("gray", 12),
                    ),
                    rx.text(
                        "Gestión de equipos moderna,\nrápida y sin fricciones.",
                        font_size="13px",
                        color=rx.color("gray", 10),
                        line_height="1.6",
                        white_space="pre-line",
                    ),
                    # Redes sociales
                    rx.hstack(
                        rx.link(
                            rx.icon("brand-twitter", size=16, color=rx.color("gray", 10)),
                            href="https://twitter.com",
                            _hover={"opacity": "0.7"},
                        ),
                        rx.link(
                            rx.icon("brand-github", size=16, color=rx.color("gray", 10)),
                            href="https://github.com",
                            _hover={"opacity": "0.7"},
                        ),
                        rx.link(
                            rx.icon("brand-linkedin", size=16, color=rx.color("gray", 10)),
                            href="https://linkedin.com",
                            _hover={"opacity": "0.7"},
                        ),
                        spacing="3",
                        margin_top="0.5rem",
                    ),
                    spacing="3",
                    align="start",
                    min_width="180px",
                ),
                # Columnas de links
                rx.desktop_only(
                    rx.grid(
                        *[
                            footer_column(title, links)
                            for title, links in FOOTER_LINKS.items()
                        ],
                        columns="4",
                        spacing="8",
                    )
                ),
                justify="between",
                gap="3rem",
                wrap="wrap",
            ),
            rx.separator(
                width="100%",
                color=rx.color("gray", 4),
                margin="2rem 0 1.5rem",
            ),
            # Parte inferior: copyright
            rx.flex(
                rx.text(
                    "© 2026 Flowly Inc. Todos los derechos reservados.",
                    font_size="12px",
                    color=rx.color("gray", 9),
                ),
                rx.hstack(
                    rx.link("Privacidad", href="#", font_size="12px", color=rx.color("gray", 9), text_decoration="none"),
                    rx.link("Términos", href="#", font_size="12px", color=rx.color("gray", 9), text_decoration="none"),
                    rx.link("Cookies", href="#", font_size="12px", color=rx.color("gray", 9), text_decoration="none"),
                    spacing="4",
                ),
                justify="between",
                align="center",
                wrap="wrap",
                gap="1rem",
            ),
            max_width="1100px",
        ),
        padding=["3rem 1.5rem 2rem", "4rem 2rem 2rem"],
        width="100%",
        background_color=rx.color("gray", 1),
        border_top=f"1px solid {rx.color('gray', 4)}",
    )

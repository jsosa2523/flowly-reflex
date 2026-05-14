"""Sección Hero de la landing page."""
import reflex as rx


def mock_dashboard() -> rx.Component:
    """Mockup visual del dashboard para el hero."""
    return rx.box(
        # Sprint card
        rx.box(
            rx.hstack(
                rx.box(
                    rx.text("AB", font_size="12px", font_weight="600", color=rx.color("violet", 11)),
                    width="36px",
                    height="36px",
                    border_radius="50%",
                    background_color=rx.color("violet", 3),
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    flex_shrink="0",
                ),
                rx.vstack(
                    rx.text("Sprint Q2 2026", font_size="13px", font_weight="500"),
                    rx.box(
                        rx.box(
                            width="72%",
                            height="100%",
                            background_color=rx.color("violet", 9),
                            border_radius="4px",
                        ),
                        width="100%",
                        height="8px",
                        background_color=rx.color("violet", 3),
                        border_radius="4px",
                        overflow="hidden",
                    ),
                    rx.text("72% completado", font_size="11px", color=rx.color("gray", 10)),
                    spacing="1",
                    width="100%",
                    align="start",
                ),
                spacing="3",
                align="center",
                width="100%",
            ),
            background_color=rx.color("gray", 1),
            border=f"1px solid {rx.color('gray', 4)}",
            border_radius="10px",
            padding="14px",
        ),
        # Stat mini-grid
        rx.grid(
            *[
                rx.box(
                    rx.text(stat, font_family="'Syne', sans-serif", font_size="20px", font_weight="800", color=rx.color("violet", 11)),
                    rx.text(label, font_size="11px", color=rx.color("gray", 10)),
                    background_color=rx.color("violet", 2),
                    border_radius="8px",
                    padding="10px 12px",
                )
                for stat, label in [("24", "Tareas activas"), ("↑8%", "Velocidad"), ("6", "Miembros"), ("3d", "Al deadline")]
            ],
            columns="2",
            spacing="2",
        ),
        # Notification card
        rx.hstack(
            rx.icon("check", color=rx.color("green", 9), size=16),
            rx.text(
                rx.text.span("Diseño UI aprobado por ", font_size="12px", color=rx.color("gray", 11)),
                rx.text.span("Carlos R.", font_size="12px", font_weight="600"),
            ),
            background_color=rx.color("gray", 1),
            border=f"1px solid {rx.color('gray', 4)}",
            border_radius="10px",
            padding="12px 14px",
            align="center",
            spacing="2",
        ),
        display="flex",
        flex_direction="column",
        gap="10px",
        background="linear-gradient(135deg, #EEEDFE 0%, #E1F5EE 100%)",
        border_radius="16px",
        padding="1.25rem",
        border=f"1px solid {rx.color('gray', 4)}",
    )


def hero_section() -> rx.Component:
    return rx.box(
        rx.container(
            rx.flex(
                # Columna de texto
                rx.vstack(
                    # Badge
                    rx.hstack(
                        rx.box(
                            width="8px",
                            height="8px",
                            border_radius="50%",
                            background_color=rx.color("green", 9),
                        ),
                        rx.text(
                            "Nuevo — Automatización con IA",
                            font_size="12px",
                            font_weight="500",
                            color=rx.color("green", 11),
                        ),
                        background_color=rx.color("green", 2),
                        padding="4px 12px",
                        border_radius="20px",
                        align="center",
                        spacing="2",
                    ),
                    # Título principal
                    rx.heading(
                        "Gestiona tu equipo ",
                        rx.text.span("sin fricciones", color=rx.color("violet", 9)),
                        font_family="'Syne', sans-serif",
                        font_size=["32px", "40px", "48px"],
                        font_weight="800",
                        line_height="1.1",
                        letter_spacing="-1.5px",
                        as_="h1",
                    ),
                    # Subtítulo
                    rx.text(
                        "Flowly centraliza tareas, métricas y comunicación en un solo lugar. "
                        "Menos reuniones, más resultados.",
                        font_size="16px",
                        line_height="1.7",
                        color=rx.color("gray", 11),
                        max_width="480px",
                    ),
                    # Botones CTA
                    rx.hstack(
                        rx.button(
                            "Empieza gratis →",
                            background_color=rx.color("violet", 9),
                            color="white",
                            border_radius="10px",
                            font_size="15px",
                            font_weight="500",
                            height="44px",
                            padding="0 24px",
                            cursor="pointer",
                            _hover={"background_color": rx.color("violet", 10)},
                            transition="background-color 0.2s",
                        ),
                        rx.button(
                            "Ver demo",
                            variant="outline",
                            border_radius="10px",
                            font_size="15px",
                            font_weight="500",
                            height="44px",
                            padding="0 24px",
                            cursor="pointer",
                            color=rx.color("gray", 12),
                            border=f"1px solid {rx.color('gray', 6)}",
                            background_color="transparent",
                            _hover={"background_color": rx.color("gray", 3)},
                            transition="background-color 0.2s",
                        ),
                        spacing="3",
                        flex_wrap="wrap",
                    ),
                    # Social proof
                    rx.hstack(
                        rx.hstack(
                            *[
                                rx.box(
                                    rx.text(initials, font_size="10px", font_weight="600", color=rx.color("violet", 11)),
                                    width="28px",
                                    height="28px",
                                    border_radius="50%",
                                    background_color=rx.color("violet", 3),
                                    border=f"2px solid {rx.color('gray', 1)}",
                                    display="flex",
                                    align_items="center",
                                    justify_content="center",
                                    margin_left="-8px" if i > 0 else "0",
                                )
                                for i, initials in enumerate(["MR", "AL", "JK", "CP"])
                            ],
                            spacing="0",
                        ),
                        rx.text(
                            "+2,000 equipos ya usan Flowly",
                            font_size="13px",
                            color=rx.color("gray", 10),
                        ),
                        align="center",
                        spacing="2",
                    ),
                    spacing="5",
                    align="start",
                    width="100%",
                ),
                # Columna visual (dashboard mockup)
                rx.box(
                    mock_dashboard(),
                    width="100%",
                    min_width="280px",
                ),
                direction=["column", "column", "row"],
                gap=["2rem", "2rem", "4rem"],
                align="center",
                width="100%",
            ),
            max_width="1100px",
        ),
        padding=["3rem 1.5rem", "4rem 2rem", "5rem 2rem"],
        width="100%",
    )

"""Flowly — Landing Page principal en Reflex."""
import reflex as rx
from flowly.components.navbar import navbar
from flowly.components.hero import hero_section
from flowly.components.features import features_section
from flowly.components.pricing import pricing_section
from flowly.components.footer import footer


def index() -> rx.Component:
    """Página principal: landing page completa."""
    return rx.box(
        navbar(),
        hero_section(),
        features_section(),
        pricing_section(),
        footer(),
        font_family="'DM Sans', sans-serif",
        background_color=rx.color("gray", 1),
        min_height="100vh",
    )


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@300;400;500&display=swap",
    ],
    style={
        "margin": "0",
        "padding": "0",
        "box_sizing": "border-box",
    },
)

app.add_page(index, route="/", title="Flowly — Gestiona tu equipo sin fricciones")

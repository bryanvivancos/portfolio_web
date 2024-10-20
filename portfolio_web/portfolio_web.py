"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from portfolio_web.components.navbar import navbar
from portfolio_web.views.header.header import header
from portfolio_web.views.links.links import links
from portfolio_web.components.footer import footer
import portfolio_web.styles.styles as styles
from portfolio_web.styles.styles import Size

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
            header(),
            links(),                
            max_width= styles.MAX_WIDTH,
            width= "100%",
            margin_y= Size.BIG.value
            ),
            margin_x=Size.SMALL.value,
        ),
        footer(),        
    )

app = rx.App(
    stylesheets= styles.STYLESHEETS,
    style= styles.BASE_STYLE,
)
app.add_page(
    index,
    title= "Bryan's Web",
    description= "Mi portafolio web",
    image="images/image.jpg"
)

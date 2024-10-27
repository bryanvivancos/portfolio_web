"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from portfolio_web.components.navbar import navbar
from portfolio_web.views.header import header
from portfolio_web.views.links import links
from portfolio_web.views.main_icons import main_icons
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
            main_icons(),
            links(),                
            max_width= styles.MAX_WIDTH,
            width= "100%",
            margin_y= Size.BIG.value
            ),
            margin_x=Size.MEDIUM.value,
        ),
        footer(),        
    )

app = rx.App(
    stylesheets= styles.STYLESHEETS,
    style= styles.BASE_STYLE,
    #GOOGLE ANALYTICS
#     head_components=[
#         rx.script(
#             src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}"),
#         rx.script(
#             f"""
# window.dataLayer = window.dataLayer || [];
# function gtag(){{dataLayer.push(arguments);}}
# gtag('js', new Date());
# gtag('config', '{const.G_TAG}');
# """
#         ),
#     ],
)

title= "Bryan's Web"
description= "Mi portafolio web donde podrás encontrar practicamente todo sobre mí."
preview= "images/avatar.jpg"

app.add_page(
    index,
    title= title,
    description= description,
    image= preview,
    meta=[
        {"name": "og:type", "content":"website"},
        {"name": "og:title", "content":title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary:large:image"},
        {"name": "twitter:site", "content": "@bryanvivancos"}
    ]
)

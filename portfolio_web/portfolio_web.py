"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import portfolio_web.styles.styles as styles
from portfolio_web.pages.index import index

class State(rx.State):
    pass

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
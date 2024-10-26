import reflex as rx
from portfolio_web.styles.colors import Color
import portfolio_web.styles.styles as styles

def link_navbar(text:str,url:str) -> rx.Component:
    return rx.link(
        rx.text(
            text
        ),
        href= url ,
        color= Color.BACKGROUND.value,
        style=styles.navbar_title_style,
    )
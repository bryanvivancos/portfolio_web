import reflex as rx
import datetime
from portfolio_web.styles.styles import Size

def footer() -> rx.Component:
    return rx.hstack(
        rx.text(
        f"2020-{datetime.date.today().year} BY BRYAN JOSUE VIVANCO SILVA" 
        ),
        rx.text(
            "PIURA - PERÚ"
        ),
        width= "100%",
        justify_content="space-evenly",
        padding_x= Size.BIG.value,
        margin_bottom= Size.BIG.value,
        font_size= Size.MEDIUM.value,
    )
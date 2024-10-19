import reflex as rx
from portfolio_web.styles.styles import Size

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Hi there",
        ),
        position= "sticky",
        bg= "#1a1e29",
        padding_x= Size.DEFAULT.value,
        padding_y= Size.SMALL.value,
        z_index = "999",
        width="100%",
        top= "0",
    )
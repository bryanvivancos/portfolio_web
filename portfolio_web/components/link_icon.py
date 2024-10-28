import reflex as rx
from portfolio_web.styles.styles import Size as Size

def link_icon(image:str,url:str, alt:str,external:bool) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width= Size.BIG.value,
            alt=alt,
        ),
        href=url,
        is_external= external,
    )
import reflex as rx
import datetime
import portfolio_web.constants as const
from portfolio_web.styles.styles import Size
from portfolio_web.styles.colors import TextColor
from portfolio_web.styles.colors import Color
import portfolio_web.styles.styles as styles

def footer() -> rx.Component:
    return rx.vstack(
        rx.link(
            rx.text(
            f"© 2020-{datetime.date.today().year} BY BRYAN JOSUE VIVANCO SILVA",
            text_align="center",
            color= TextColor.FOOTER.value,
            _hover= {"color": Color.SECONDARY.value},
            ),
            href= const.PORTWEB_URL,
            is_external= True,
        ),
        rx.text(
            "PIURA PERÚ",
            text_align="center"
        ),
        width= "100%",
        align= "center",
        padding_x= Size.BIG.value,
        padding_bottom=Size.BIG.value,
        font_size= Size.SM.value,
        spacing=Size.ZERO.value,
        color= TextColor.FOOTER.value
    )
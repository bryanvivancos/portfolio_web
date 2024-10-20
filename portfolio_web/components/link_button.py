import reflex as rx
import portfolio_web.styles.styles as styles
from portfolio_web.styles.styles import Size

def link_button(title:str,body:str,image:str="",url:str="#") -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src= image,
                    width= Size.LARGE.value,
                    margin= Size.MEDIUM.value,
                    align="center",
                ),
                rx.vstack(
                    rx.text(
                    title, 
                    style= styles.button_title_style,
                    ),  
                    rx.text(
                        body, 
                        style= styles.button_body_style,
                    ),
                    spacing= Size.ZERO.value,
                    padding= Size.SMALL.value,
                    gap=Size.ZERO.value,
                ),
            gap=Size.ZERO.value,
            width="100%",
            align_items= "start",
            ),
        ),
        href= url,    
        is_external= True,
        width= "100%"
    ),
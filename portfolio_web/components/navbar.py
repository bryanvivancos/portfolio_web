import reflex as rx
from portfolio_web.styles.styles import Size
from portfolio_web.components.link_button_navbar import link_navbar
from portfolio_web.routes import Route
from portfolio_web.styles.colors import Color
import portfolio_web.styles.styles as styles

def navbar() -> rx.Component:
    return rx.center(
        rx.hstack(
            link_navbar(
                "¿Quien soy?",
                "#me",    
            ),
            link_navbar(
                "Proyectos",
                "#proyectos"
            ),
            link_navbar(
                "Cursos y Certificaciones",
                "#cursos"
            ),
            link_navbar(
                "Skills",
                "#skills"
            ),
            max_width= styles.MAX_WIDTH,
            width= "100%",
            justify_content= "space-evenly",
            align_items= "center",
        ),
        position= "sticky",
        bg= Color.SECONDARY.value,
        padding_x= Size.DEFAULT.value,
        padding_y= Size.SMALL.value,
        z_index = "999",
        width="100%",
        top= "0",
        gap="1em",
    )
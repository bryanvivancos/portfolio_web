import reflex as rx
from portfolio_web.components.link_icon import link_icon
from portfolio_web.styles.styles import Size

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                fallback="BJ", 
                radius="full",
                size="8"
            ),
            rx.vstack(
                rx.heading(
                "Bryan Josue Vivanco Silva"
                ),
                rx.text(
                    """Ingeniero Electrónico y Telecomunicaciones. 
                    +1 año realizando proyectos personales, aprendiendo tecnologías y +3 años trabajando en el campo de TI. Autodidacta con orientación al servicio, rápida capacidad de aprendizaje, buenas relaciones interpersonales a todo nivel social, alta capacidad analítica comunicativa, pensamiento estratégico y dinamismo. Buenas habilidades para el trabajo en equipo y bajo presión, alta capacidad organizativa y buen criterio. 
                    """
                ),
            ),
            spacing= Size.MEDIUM.value,
        ),
        rx.hstack(
            link_icon(
                "https://www.linkedin.com/in/bryan-josue-vivanco-silva-8739521bb/"),
            link_icon(
                "https://github.com/bryanvivancos"),
            width="100%",
            justify_content= "space-evenly",
        ),
        spacing= Size.BIG.value,
    )
    
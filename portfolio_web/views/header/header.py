import reflex as rx
from portfolio_web.components.link_icon import link_icon
from portfolio_web.styles.styles import Size
import portfolio_web.styles.styles as styles
from portfolio_web.styles.colors import TextColor
import portfolio_web.constants as const
from portfolio_web.styles.colors import Color

def header() -> rx.Component:
    return rx.vstack(
        rx.grid(
            rx.center(
                rx.image(
                src="https://media.licdn.com/dms/image/v2/D4E03AQE-ofROHczE0w/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1710025305289?e=1735171200&v=beta&t=ogGBnGyZee56lDxgoB_2KQ1kOZYybxUPJs6FEsqIGvo",
                color=Color.BACKGROUND.value,
                border_radius="50%", 
                padding="2px",
                border= "4px solid #01C38E",   
                width= rx.breakpoints(initial="150px",sm="200px"),        
                height= rx.breakpoints(initial="150px",sm="200px"),
                ),
            ),
            rx.vstack(
                rx.heading(
                "Bryan Josue Vivanco Silva",
                size="8",
                ),
                rx.text(
                    """Ingeniero Electrónico y Telecomunicaciones. 
                    +1 año realizando proyectos personales, aprendiendo tecnologías y +3 años trabajando en el campo de TI. Autodidacta con orientación al servicio, rápida capacidad de aprendizaje, buenas relaciones interpersonales a todo nivel social, alta capacidad analítica comunicativa, pensamiento estratégico y dinamismo. Buenas habilidades para el trabajo en equipo y bajo presión, alta capacidad organizativa y buen criterio. 
                    """,
                    color= TextColor.BODY.value,
                    font_size=Size.MEDIUM.value
                ),
            ),
            grid_template_columns= rx.breakpoints(initial="1fr",sm="1fr 2fr"),
            columns= rx.breakpoints(initial="1",sm="2"),
            spacing= Size.MEDIUM.value,
            justify="center"
        ),
        rx.hstack(
            link_icon(
                "icons/linkedin.svg",
                const.LINKEDIN_URL,
                True,
            ),
            link_icon(
                "icons/github.svg",
                const.GITHUB_URL,
                True,
            ),
            link_icon(
                "icons/mail.svg",
                f"mailto:{const.EMAIL}",
                True,
            ),
            style= styles.link_icon_style
        ),
        spacing= Size.BIG.value,
    )
    
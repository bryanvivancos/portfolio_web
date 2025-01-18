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
                src="/images/avatar.jpg",
                alt="Imagen de perfil de Bryan Vivanco",
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
                    """Ingeniero Electrónico y Telecomunicaciones Colegiado de la Universidad Nacional de Piura con N° reg CIP 328477. 
                        Desarrollador autodidacta con +1 año realizando proyectos personales, aprendiendo tecnologías y +3 años trabajando en el campo de TI. Con buenas habilidades para el trabajo en equipo y bajo presión, proactivo, con pensamiento analítico, rápida capacidad de aprendizaje, capacidad de autogestión y atención al detalle, adaptable al cambio y con buena comunicación verbal. Capaz de dar y recibir feedback, así mismo, gran talento de liderazgo.
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
        id= "me",
        spacing= Size.BIG.value,
        padding_top=Size.BIG.value,
    )
    
import reflex as rx
from portfolio_web.components.link_button import link_button
from portfolio_web.components.titles import title
from portfolio_web.styles.styles import Size
from portfolio_web.components.link_icon import link_icon
import portfolio_web.styles.styles as styles
import portfolio_web.constants as const

def links() -> rx.Component:
    return rx.vstack(
        
        link_button(
            "icons/google_drive.svg",
            "CV desde Google Drive",
            "CV desde Google Drive",
            const.CV_URL,
        ),
        title("Proyectos","proyectos"),
        link_button(
            "icons/github.svg",
            "DE FORMULARIO WEB A WORD - PYTHON",
            "Proyecto que automatiza el llenado de un Formato Word con las respuestas de un Formulario WEB",
            const.FORMULARIOWEB_URL,
        ),
        link_button(
            "icons/github.svg",
            "GENERATING DATA - PYTHON",
            "Proyecto que se encarga de generar data para visualizarla y analizarla",
            const.GENERATINGDATA_URL,
        ),
        link_button(
            "icons/github.svg",
            "GETTING STARTED WITH DJANGO - PYTHON",
            "Primeros pasos para crear una aplicación web con Django ",
            const.GETTINDJANGO_URL,
        ),
        link_button(
            "icons/github.svg",
            "X FOLLOW CARD - REACT",
            "Plantilla que simula la tarjeta de seguido/dejar de seguir de la plataforma X(antes Twitter)",
            const.XFOLLOWCARD_URL,
        ),
        
        title("Cursos y Certificaciones","cursos"),
        link_button(
            "icons/certificate.svg",
            "Data Science For Business",
            "Tu primera semana como Data Scientist",
            const.DSFB_URL,
        ),
        link_button(
            "icons/certificate.svg",
            "CIETSI - COLEGIO DE INGENIEROS, CD - PIURA",
            "Implementación de una base de datos con SQL SERVER 2022",
            const.CERTCIETSI_URL,
        ),
        link_button(
            "icons/certificate.svg",
            "UDEMY",
            "Desarrollo Web - HTML, CSS, JAVASCRIPT",
            const.CV_URL,
        ),
        link_button(
            "icons/certificate.svg",
            "CISCO NETACAD",
            "NDG Linux Essentials",
            const.NETNDGLINUX_URL,
        ),
        
        title("Skills Adicionales","skills"),
        rx.hstack(
            rx.image(
            src="icons/html.svg",
            width= Size.BIG.value,
            alt="skill adicional html",
            ),
            rx.image(
            src="icons/css.svg",
            width= Size.BIG.value,
            alt="skill adicional css",
            ),
            rx.image(
            src="icons/javascript.svg",
            width= Size.BIG.value,
            alt="skill adicional javascript",
            ),
            style= styles.link_icon_style,
        ),
        
        spacing= Size.MEDIUM.value,
        width="100%",
    )
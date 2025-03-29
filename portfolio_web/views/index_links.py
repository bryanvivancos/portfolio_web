import reflex as rx
from portfolio_web.components.link_button import link_button
from portfolio_web.components.titles import title
from portfolio_web.styles.styles import Size
from portfolio_web.components.link_icon import link_icon
import portfolio_web.styles.styles as styles
import portfolio_web.constants as const

def index_links() -> rx.Component:
    return rx.vstack(
        
        link_button(
            "icons/google_drive.svg",
            "CV desde Google Drive",
            "Curriculum desde Google Drive",
            const.CV_URL,
        ),
        link_button(
            "icons/google_drive.svg",
            "CV from Google Drive",
            "EN-US Resume from Google Drive",
            const.CV_EN_US_URL,
        ),
        
        rx.vstack(
            title("Proyectos"),
            link_button(
                "icons/github.svg",
                "ASSIST CONTROL PROJECT",
                "Proyecto para llevar un control de asistencia de colaboradores de una empresa con PYTHON, DJANGO y SQL SERVER",
                const.CONTROL_ASSIST,
            ),
            link_button(
                "icons/github.svg",
                "ALBUM/CATALOG PROJECT",
                "Plataforma CRUD con Python que interactúa con una base de datos en SUPABASE",
                const.CATALOG_URL,
            ),
            link_button(
                "icons/github.svg",
                "PYTHON BACKEND CON FASTAPI Y MONGODB",
                "Ejercicio de un Backend en Python usando las tecnologías de FastAPI y MongoDB",
                const.BACKENDEX_URL,
            ),
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
            id="proyectos",
            width="100%",
        ),
        rx.vstack(
            title("Cursos y Certificaciones"),
            link_button(
                "icons/certificate.svg",
                "WEB COMPONENTS CON JAVASCRIPT ",
                "Platzi",
                const.WEB_COMPONENTS_URL,
            ),
            link_button(
                "icons/certificate.svg",
                "CONSUMO DE API REST CON JAVASCRIPT",
                "Platzi",
                const.API_PRACTICO_URL,
            ),
            link_button(
                "icons/certificate.svg",
                "INTRODUCCION AL DESARROLLO BACKEND",
                "Platzi",
                const.INTRO_BACKEND_URL,
            ),
            link_button(
                "icons/certificate.svg",
                "JAVASCRIPT: MANIPULACIÓN DEL DOM",
                "Platzi",
                const.DOM_URL,
            ),
            link_button(
                "icons/certificate.svg",
                "APPLIED DATA WITH PYTHON",
                "IBM Course Level 2",
                const.APPLIED_DS_IBM_URL,
            ),
            link_button(
                "icons/certificate.svg",
                "IMPLEMENTACIÓN DE UNA BASE DE DATOS CON SQL SERVER 2022",
                "CIETSI - Colegio de Ingenieros, CD - PIURA",
                const.CERTCIETSI_URL,
            ),
            link_button(
                "icons/certificate.svg",
                "DESARROLLO WEB - HTML, CSS, JAVASCRIPT",
                "Udemy",
                const.CV_URL,
            ),
            id="cursos",
            width="100%",
        ),
        rx.vstack(
            title("Skills Adicionales"),
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
                rx.image(
                src="icons/django.svg",
                width= Size.XL.value,
                alt="skill django",
                ),
                
                style= styles.link_icon_style,
                justify= rx.breakpoints(initial="center", sm="start"),
            ),
            id="skills",
            width="100%",
        ),    
        spacing= Size.MEDIUM.value,
        width="100%",
    )
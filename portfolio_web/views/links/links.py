import reflex as rx
from portfolio_web.components.link_button import link_button
from portfolio_web.components.titles import title
from portfolio_web.styles.styles import Size

def links() -> rx.Component:
    return rx.vstack(
        title("PROYECTOS"),
        link_button(
            "CV desde Google Drive",
            "CV desde Google Drive",
            "https://docs.google.com/document/d/1COvjcCJE4GXUlkkSa9U6CrofLQPBkKWM/edit?usp=sharing&ouid=117976139180001148882&rtpof=true&sd=true",
        ),
        link_button(
            "DE FORMULARIO WEB A WORD - PYTHON",
            "Proyecto que automatiza el llenado de un Formato Word con las respuestas de un Formulario WEB",
            "https://github.com/bryanvivancos",
        ),
        link_button(
            "GENERATING DATA - PYTHON",
            "Proyecto que se encarga de generar data para visualizarla y analizarla",
            "https://github.com/bryanvivancos",
        ),
        link_button(
            "GETTING STARTED WITH DJANGO - PYTHON",
            "Proyecto que crea una página de inicio y una base de datos con Django ",
            "https://github.com/bryanvivancos",
        ),
        link_button(
            "X FOLLOW CARD - REACT",
            "Plantilla que simula la tarjeta de seguido/dejar de seguir de la plataforma X(antes Twitter)",
            "https://github.com/bryanvivancos",
        ),
        
        title("CURSOS Y CERTIFICACIONES"),
        link_button(
            "Data Science For Business",
            "Tu primera semana como Data Scientist",
            "https://docs.google.com/document/d/1COvjcCJE4GXUlkkSa9U6CrofLQPBkKWM/edit?usp=sharing&ouid=117976139180001148882&rtpof=true&sd=true",
        ),
        link_button(
            "CIETSI - COLEGIO DE INGENIEROS, CD - PIURA",
            "Implementación de una base de datos con SQL SERVER 2022",
            "https://docs.google.com/document/d/1COvjcCJE4GXUlkkSa9U6CrofLQPBkKWM/edit?usp=sharing&ouid=117976139180001148882&rtpof=true&sd=true",
        ),
        link_button(
            "HARVARD",
            "Desarrollo Web - HTML, CSS, JAVASCRIPT",
            "https://docs.google.com/document/d/1COvjcCJE4GXUlkkSa9U6CrofLQPBkKWM/edit?usp=sharing&ouid=117976139180001148882&rtpof=true&sd=true",
        ),
        link_button(
            "CISCO NETACAD",
            "NDG Linux Essentials",
            "https://docs.google.com/document/d/1COvjcCJE4GXUlkkSa9U6CrofLQPBkKWM/edit?usp=sharing&ouid=117976139180001148882&rtpof=true&sd=true",
        ),
        title("SKILLS ADICIONALES"),
        
        spacing= Size.MEDIUM.value,
        width="100%"
    )
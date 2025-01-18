import reflex as rx
import portfolio_web.constants as const
import portfolio_web.styles.styles as styles
from portfolio_web.styles.styles import Size
from portfolio_web.components.titles import title
from portfolio_web.components.link_icon import link_icon

def main_icons() -> rx.Component:
    return rx.grid(
        rx.vstack(
            title("Contáctame"),
            rx.hstack(
                link_icon(
                    "icons/linkedin.svg",
                    const.LINKEDIN_URL,
                    "linkedin",
                    True,
                ),
                link_icon(
                    "icons/github.svg",
                    const.GITHUB_URL,
                    "github",
                    True,
                ),
                link_icon(
                    "icons/mail.svg",
                    f"mailto:{const.EMAIL}",
                    "mail to",
                    True,
                ),
                style= styles.link_icon_style,
                justify= rx.breakpoints(initial="center", sm="start"),
            ),
        ),
        rx.vstack(
            title("Tecnologías"),
            rx.hstack(
                rx.image(
                src="icons/python.svg",
                width= Size.BIG.value,
                alt="skill python",
                ),
                rx.image(
                src="icons/react.svg",
                width= Size.BIG.value,
                alt="skill react",
                ),
                rx.image(
                src="icons/linux.svg",
                width= Size.XL.value,
                alt="skill linux",
                ),
                
                style= styles.link_icon_style,
                justify= rx.breakpoints(initial="center", sm="start"),
            ),
        ),
        width= "100%",
        columns= rx.breakpoints(initial="1", sm="2"),
    )
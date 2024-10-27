import reflex as rx
import portfolio_web.styles.styles as styles

def title(text:str, id:str = ""):
    return rx.heading(
            text,
            id= id,
            style= styles.titles_style,
            size="6",
        )
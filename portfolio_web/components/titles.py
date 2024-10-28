import reflex as rx
import portfolio_web.styles.styles as styles

def title(text:str):
    return rx.heading(
            text,
            style= styles.titles_style,
            size="6",
        )
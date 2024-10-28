import reflex as rx
import portfolio_web.utils as utils
import portfolio_web.styles.styles as styles
from portfolio_web.components.navbar import navbar
from portfolio_web.views.header import header
from portfolio_web.views.index_links import index_links
from portfolio_web.views.main_icons import main_icons
from portfolio_web.components.footer import footer
from portfolio_web.styles.styles import Size

@rx.page(
    title= utils.index_title,
    description= utils.index_description,
    image= utils.preview,
    meta= utils.index_meta,
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
            header(),
            main_icons(),
            index_links(),                
            max_width= styles.MAX_WIDTH,
            width= "100%",
            margin_y= Size.BIG.value
            ),
            margin_x=Size.MEDIUM.value,
        ),
        footer(),        
    )
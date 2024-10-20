import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font
from .fonts import FontWeight

#constantes
MAX_WIDTH = "720px"

#Fonts

STYLESHEETS= [
    "https://fonts.googleapis.com/css?family=Quicksand:wght@400;700&display=swap"
]

#sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL= "0.5em"
    MEDIUM= "0.9em"
    DEFAULT= "1em"
    DL = "1.1"
    LARGE= "1.5em"
    BIG= "2em"
    
    
#styles

BASE_STYLE = {
    "font_family":Font.DEFAULT.value,
    "font_weight":FontWeight.LIGHT.value,
    "scroll_behavior":"smooth",
    "background_color": Color.BACKGROUND.value,
    rx.heading:{
        "color":TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight":FontWeight.BOLD.value,
    },
    rx.button: {
        "width":"100%",
        "height":"100%",
        "padding":Size.SMALL.value,
        "border_radius":Size.DEFAULT.value,
        "color": TextColor.BODY.value,
        "background_color": Color.PRIMARY.value,
        "text_align": "start",
        "_hover": {
            "background_color": Color.SECONDARY.value,
        },
    },
    rx.link : {
        "text_decoration": "none",
        "_hover": {},
    },
}

navbar_title_style= dict(
    font_family= Font.TITLE.value,
    font_weight= FontWeight.BOLD.value,
    font_size= Size.DL.value,
    text_align= "center",
)

titles_style= dict(
    width= "100%",
    font_family= Font.TITLE.value,
    margin= Size.MEDIUM.value,
    margin_left= Size.ZERO.value,
    margin_bottom= Size.ZERO.value
)
    

button_title_style= dict(
    font_family= Font.TITLE.value,
    font_size=Size.DEFAULT.value,
    color= TextColor.HEADER.value
)

button_body_style= dict(
    font_size=Size.MEDIUM.value,
    color= TextColor.BODY.value
)

link_icon_style = dict(
    width="100%",
    justify_content= "space-evenly",
)


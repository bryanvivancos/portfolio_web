import reflex as rx
from enum import Enum

#constantes
MAX_WIDTH = "720px"

#sizes
class Size(Enum):
    SMALL= "0.5em"
    MEDIUM= "0.9em"
    DEFAULT= "1em"
    BIG= "2em"
    
    
#styles
BASE_STYLE = {
    rx.button: {
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding":Size.SMALL.value,
        "border_radius":Size.DEFAULT.value,
    },
    rx.link : {
        "text_decoration": "none",
        "_hover": {},
    }
}

titles_style= dict(
    width= "100%",
    padding= Size.MEDIUM.value,
)
    

button_title_style= dict(
    font_size=Size.DEFAULT.value
)

button_body_style= dict(
    font_size=Size.MEDIUM.value,
)


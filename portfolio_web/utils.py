import reflex as rx

#comun

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

preview= "images/avatar.jpg"

_meta=[
        {"name": "og:type", "content":"website"},
        
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary:large:image"},
        {"name": "twitter:site", "content": "@bryanvivancos"}
    ]

#index

index_title= "Bryan's Web"
index_description= "Mi portafolio web donde podrás encontrar practicamente todo sobre mí."

index_meta= [
    {"name": "og:title", "content":index_title},
    {"name": "og:description", "content": index_description},
] 
index_meta.extend(_meta)


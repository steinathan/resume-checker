from typing import List
from pydantic import BaseModel, Field


class Css(BaseModel):
    value: str = ".section {\n\toutline: 1px solid #000;\n\toutline-offset: 4px;\n}"
    visible: bool = False


class Options(BaseModel):
    breakLine: bool = True
    pageNumbers: bool = True


class Page(BaseModel):
    margin: int = 18
    format: str = "a4"
    options: Options = Options()


class Theme(BaseModel):
    background: str = "#ffffff"
    text: str = "#000000"
    primary: str = "#dc2626"


class Font(BaseModel):
    family: str = "IBM Plex Serif"
    subset: str = "latin"
    variants: List[str] = ["regular"]
    size: int = 14


class Typography(BaseModel):
    font: Font = Font()
    lineHeight: float = 1.5
    hideIcons: bool = False
    underlineLinks: bool = True


default_layout = [
    [
        ["profiles", "summary", "experience", "education", "projects", "volunteer", "references"],
        ["skills", "interests", "certifications", "awards", "publications", "languages"],
    ]
]


class MetadataSchema(BaseModel):
    template: str = "rhyhorn"
    layout: List[List[List[str]]] = Field(
        default_factory=lambda: default_layout)  # Assuming defaultLayout is defined elsewhere
    css: Css = Css()
    page: Page = Page()
    theme: Theme = Theme()
    typography: Typography = Typography()
    notes: str = ""


default_metadata = {
    "template": "rhyhorn",
    "layout": default_layout,  # Assuming default_layout is defined elsewhere
    "css": {
        "value": ".section {\n\toutline: 1px solid #000;\n\toutline-offset: 4px;\n}",
        "visible": False,
    },
    "page": {
        "margin": 18,
        "format": "a4",
        "options": {
            "breakLine": True,
            "pageNumbers": True,
        },
    },
    "theme": {
        "background": "#ffffff",
        "text": "#000000",
        "primary": "#dc2626",
    },
    "typography": {
        "font": {
            "family": "IBM Plex Serif",
            "subset": "latin",
            "variants": ["regular", "italic", "600"],
            "size": 14,
        },
        "lineHeight": 1.5,
        "hideIcons": False,
        "underlineLinks": True,
    },
    "notes": "",
}

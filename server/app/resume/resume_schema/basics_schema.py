from typing import List, Optional
from pydantic import BaseModel, Field

from app.resume.resume_schema.sections.sections import UrlSchema


class PictureEffects(BaseModel):
    hidden: bool = False
    border: bool = False
    grayscale: bool = False


class Picture(BaseModel):
    url: str = Field("")
    size: int = Field(64)
    aspectRatio: float = Field(1)
    borderRadius: int = Field(0)
    effects: PictureEffects = PictureEffects()


class CustomField(BaseModel):
    id: str = Field("")
    icon: str = Field("")
    name: str = Field("")
    value: str = Field("")


class BasicsSchema(BaseModel):
    name: str = Field(default="")
    headline: str = Field(default="")
    email: Optional[str] = Field(default="")
    phone: str = Field(default="")
    location: str = Field(default="")
    url: UrlSchema = Field(default_factory=UrlSchema)
    customFields: List[CustomField] = Field(default_factory=list)
    picture: Picture = Field(default_factory=Picture)

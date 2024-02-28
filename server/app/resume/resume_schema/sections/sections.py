from __future__ import annotations

import uuid
from typing import List

from pydantic import Field, BaseModel


class ItemSchema(BaseModel):
    id: str = Field(default=str(uuid.uuid4()))
    visible: bool = True


class UrlSchema(BaseModel):
    label: str = Field(default="")
    href: str = Field(default="")


class AwardSchema(ItemSchema):
    pass
    # title: str = Field(..., min_length=1)
    # awarder: str = Field(default="")
    # date: str = Field(default="")
    # summary: str = Field(default="")
    # url: UrlSchema = UrlSchema()


class SummarySchema(ItemSchema):
    content: str = Field(default="")


class CertificationSchema(ItemSchema):
    name: str = Field("certifications", min_length=1)
    issuer: str = Field(default="")
    date: str = Field(default="")
    summary: str = Field(default="")
    url: UrlSchema = Field(default_factory=UrlSchema)


class EducationSchema(ItemSchema):
    institution: str = Field(..., min_length=1)
    studyType: str = Field(default="")
    area: str = Field(default="")
    score: str = Field(default="")
    date: str = Field(default="")
    summary: str = Field(default="")
    url: UrlSchema = UrlSchema


class ExperienceSchema(ItemSchema):
    company: str = Field(..., min_length=1)
    position: str = Field(default="")
    location: str = Field(default="")
    date: str = Field(default="")
    summary: str = Field(default="")
    url: UrlSchema = UrlSchema


class VolunteerSchema(ItemSchema):
    organization: str = Field(..., min_length=1)
    position: str
    location: str
    date: str
    summary: str
    url: str = UrlSchema


class InterestSchema(ItemSchema):
    name: str = Field(..., min_length=1)
    keywords: List[str] = []


class LanguageSchema(ItemSchema):
    name: str = Field(..., min_length=1)
    description: str
    level: int = Field(default=1, ge=0, le=5)


class ProfileSchema(ItemSchema):
    network: str = Field(..., min_length=1)
    username: str = Field(..., min_length=1)
    icon: str = Field(...,
                      description='Slug for the icon from https://simpleicons.org. For example, "github", "linkedin", '
                                  'etc.')
    url: UrlSchema


class ProjectSchema(ItemSchema):
    name: str = Field(..., min_length=1)
    description: str
    date: str
    summary: str
    keywords: List[str] = []
    url: UrlSchema


class PublicationSchema(ItemSchema):
    name: str = Field(..., min_length=1)
    publisher: str
    date: str
    summary: str
    url: UrlSchema


class ReferenceSchema(ItemSchema):
    name: str = Field(..., min_length=1)
    description: str
    summary: str
    url: UrlSchema


class SkillSchema(ItemSchema):
    name: str
    description: str
    level: int = Field(default=1, ge=0, le=5)
    keywords: List[str] = []

from typing import Union, Any, Dict

from pydantic import computed_field

from app.resume.resume_schema.sections.sections import *


class SectionItem(BaseModel):
    id: str
    visible: bool = Field(default=True)
    columns: int = Field(default=1, ge=1, le=5)
    items: List[Any] = Field(default=[])

    @computed_field
    @property
    def name(self) -> str:
        return self.id.upper()


class SectionSchema(BaseModel):
    name: str = Field("")
    columns: int = Field(default=1, ge=1, le=5)
    visible: bool = Field(default=True)


class SectionsSchema(BaseModel):
    summary: SectionItem = SectionItem(id="summary", visible=True, items=[])
    awards: SectionItem = SectionItem(id="awards", visible=True, items=[])
    certifications: SectionItem = SectionItem(id="certifications", visible=True, items=[])
    education: SectionItem = SectionItem(id="education", visible=True, items=[])
    experience: SectionItem = SectionItem(id="experience", visible=True, items=[])
    volunteer: SectionItem = SectionItem(id="volunteer", visible=True, items=[])
    interests: SectionItem = SectionItem(id="interests", visible=True, items=[])
    languages: SectionItem = SectionItem(id="languages", visible=True, items=[])
    profiles: SectionItem = SectionItem(id="profiles", visible=True, items=[])
    projects: SectionItem = SectionItem(id="projects", visible=True, items=[])
    publications: SectionItem = SectionItem(id="publications", visible=True, items=[])
    references: SectionItem = SectionItem(id="references", visible=True, items=[])
    skills: SectionItem = SectionItem(id="skills", visible=True, items=[])
    custom: Dict[str, Any] = Field(default_factory=dict)


# x = SectionsSchema(
#     # certifications=SectionSchema(name="xxudu"columns=2,
#     #                              items=[CertificationSchema(title="xxudu"summary="hello world")]),
#     awards=SectionSchema(name="xxudu"columns=2, items=[AwardSchema(title="xxudu"summary="hello world")]),
#     summary=SummarySchema(name="xxudu"content="hello world"visible=False))
# print(x.model_dump_json())

# print(x.awards.items[0])



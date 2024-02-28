from pydantic import BaseModel, Field

from app.resume.resume_schema.basics_schema import BasicsSchema
from app.resume.resume_schema.metadata_schema import MetadataSchema
from app.resume.resume_schema.sections_schema import SectionsSchema


class ResumeSchema(BaseModel):
    basics: BasicsSchema = Field(default_factory=BasicsSchema)
    sections: SectionsSchema = Field(default_factory=SectionsSchema)
    metadata: MetadataSchema = Field(default_factory=MetadataSchema)


resume_data_schema = ResumeSchema()
default_resume = resume_data_schema.model_dump_json()

# default_resume = {
#     "basics": {
#         "name": "Navicstein Chinemerem ",
#         "headline": "Professional person for the Resume",
#         "email": "pricop@gmail.com",
#         "phone": "+234709100957",
#         "location": "Lagos",
#         "url": {
#             "label": "",
#             "href": "https://google.com"
#         },
#         "customFields": [],
#         "picture": {
#             "url": "",
#             "size": 64,
#             "aspectRatio": 1,
#             "borderRadius": 0,
#             "effects": {
#                 "hidden": False,
#                 "border": False,
#                 "grayscale": False
#             }
#         }
#     },
#     "sections": {
#         "summary": {
#             "name": "Summary",
#             "columns": 1,
#             "visible": True,
#             "id": "summary",
#             "content": "<p>Results-oriented AI Engineer with 5 years of experience in full-stack development, AI implementation, and real-time video processing. Proven track record in optimizing processes and enhancing customer experiences</p>"
#         },
#         "awards": {
#             "name": "Awards",
#             "columns": 1,
#             "visible": True,
#             "id": "awards",
#             "items": []
#         },
#         "certifications": {
#             "name": "Certifications",
#             "columns": 1,
#             "visible": True,
#             "id": "certifications",
#             "items": []
#         },
#         "education": {
#             "name": "Education",
#             "columns": 1,
#             "visible": True,
#             "id": "education",
#             "items": []
#         },
#         "experience": {
#             "name": "Experience",
#             "columns": 1,
#             "visible": True,
#             "id": "experience",
#             "items": [
#                 {
#                     "id": "prkxlnxevjzhg1p4i8gyr9qv",
#                     "visible": True,
#                     "company": "Vidlogs",
#                     "position": "Fullstack Developer",
#                     "location": "NY",
#                     "date": "March 2024 - Present",
#                     "summary": "<ul><li><p>CX is a customer experience platform that helps businesses improve their customer experience by analyzing customer calls and providing insights to the business. </p></li><li><p> Led the development of the frontend for CX using React, contributing to the user interface of the customer experience platform.</p></li><li><p> Engaged in task decomposition and estimations, ensuring efficient project planning and execution. o Conducted peer code reviews to ensure best practices were followed using GitHub. o Developed the Authentication service using JWT, OAuth, etc. </p></li><li><p>Served as the Scrum Master, guiding and facilitating agile methodologies within the team to ensure effective project delivery.</p></li></ul>",
#                     "url": {
#                         "label": "",
#                         "href": ""
#                     }
#                 }
#             ]
#         },
#         "volunteer": {
#             "name": "Volunteering",
#             "columns": 1,
#             "visible": True,
#             "id": "volunteer",
#             "items": []
#         },
#         "interests": {
#             "name": "Interests",
#             "columns": 1,
#             "visible": True,
#             "id": "interests",
#             "items": [
#                 {
#                     "id": "vc8i472rhy1ijtyhfy3szsr5",
#                     "visible": True,
#                     "name": "Infrastructure  Automation:",
#                     "keywords": []
#                 }
#             ]
#         },
#         "languages": {
#             "name": "Languages",
#             "columns": 1,
#             "visible": True,
#             "id": "languages",
#             "items": []
#         },
#         "profiles": {
#             "name": "Profiles",
#             "columns": 1,
#             "visible": True,
#             "id": "profiles",
#             "items": []
#         },
#         "projects": {
#             "name": "Projects",
#             "columns": 1,
#             "visible": True,
#             "id": "projects",
#             "items": []
#         },
#         "publications": {
#             "name": "Publications",
#             "columns": 1,
#             "visible": True,
#             "id": "publications",
#             "items": []
#         },
#         "references": {
#             "name": "References",
#             "columns": 1,
#             "visible": True,
#             "id": "references",
#             "items": []
#         },
#         "skills": {
#             "name": "Skills",
#             "columns": 1,
#             "visible": True,
#             "id": "skills",
#             "items": []
#         },
#         "custom": {
#             "le4q445bq6cei559tb3nyj7i": {
#                 "name": "Custom Section",
#                 "columns": 1,
#                 "visible": True,
#                 "id": "le4q445bq6cei559tb3nyj7i",
#                 "items": []
#             }
#         }
#     },
#     "metadata": {
#         "template": "azurill",
#         "layout": [
#             [
#                 [
#                     "profiles",
#                     "summary",
#                     "experience",
#                     "education",
#                     "projects",
#                     "volunteer",
#                     "references",
#                     "custom.le4q445bq6cei559tb3nyj7i"
#                 ],
#                 [
#                     "skills",
#                     "interests",
#                     "certifications",
#                     "awards",
#                     "publications",
#                     "languages"
#                 ]
#             ]
#         ],
#         "css": {
#             "value": ".section {\n\toutline: 1px solid #000;\n\toutline-offset: 4px;\n}",
#             "visible": False
#         },
#         "page": {
#             "margin": 18,
#             "format": "a4",
#             "options": {
#                 "breakLine": True,
#                 "pageNumbers": True
#             }
#         },
#         "theme": {
#             "background": "#ffffff",
#             "text": "#000000",
#             "primary": "#16a34a"
#         },
#         "typography": {
#             "font": {
#                 "family": "IBM Plex Sans",
#                 "subset": "latin",
#                 "variants": [
#                     "regular"
#                 ],
#                 "size": 14
#             },
#             "lineHeight": 1.5,
#             "hideIcons": False,
#             "underlineLinks": True
#         },
#         "notes": ""
#     }
# }

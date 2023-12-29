from __future__ import annotations

from typing import List

from langchain.output_parsers import ResponseSchema, StructuredOutputParser, PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field, validator, field_validator

cover_letter_tmpl = """# Instruction: Below is a job description and a cover letter. Your responsibility is to 
generate a cover letter than can be used as it is with a title and body

# RESUME:
{resume}

# JOB DESCRIPTION:
{job_description}

# COVER LETTER:
\n
"""

analyse_resume_tmpl = """As a Resume Specialist, meticulously evaluate the given resume, offering insightful 
observations, precise enhancements, and assign a comprehensive score to each section. give detailed tips where 
necessary to the improvements fields

{format_instructions}

# RESUME:
{resume}
"""

resume_cover_letter_prompt = PromptTemplate(
    template=cover_letter_tmpl,
    input_variables=["resume", "job_description"],
)


class ResumeSection(BaseModel):
    issues: List[str] = Field(
        description="issues you found in the section, eg. missing end-date, inconsistent date formatting")
    improvements: List[str] = Field(description="ways in which the section can be improved based on the issue with examples")
    done: List[str] = Field(
        description="things user did for sections, examples: provided your phone number. provided your email."
                    "added a work experience")
    score: float = Field(description="score to the section on how well it is, from [0-10]", default=0.0)


class ResumeCheckerModel(BaseModel):
    """ Resume checker is the model of an analysis from a resume without a job description """
    contact_info: ResumeSection = Field(description="contact info, email, phone, etc")
    education: ResumeSection = Field(description="education")
    experience: ResumeSection = Field(description="experience")
    skills: ResumeSection = Field(description="skills")
    summary: ResumeSection = Field(description="summary")
    personal_projects: ResumeSection = Field(description="personal projects")
    date_formatting: ResumeSection = Field(description="how well and consistent was the date formatted")
    section_headings: ResumeSection = Field(
        description="how best & professional the section heading was spelled, eg. prefer `Work History` to `work "
                    "experience`")
    resume_skills: List[str] | None = Field(description="Identify and list the skills mentioned in the resume",
                                            default=[])


analyse_resume_parser = PydanticOutputParser(pydantic_object=ResumeCheckerModel)

analyse_resume_prompt = PromptTemplate(
    template=analyse_resume_tmpl,
    input_variables=["resume"],
    partial_variables={
        "format_instructions": analyse_resume_parser.get_format_instructions()
    }
)

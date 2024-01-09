from __future__ import annotations
from typing import List, Dict

from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

revamp_tmpl = """
Revise my resume by incorporating the following skills and addressing specific issues. Ensure that the skills are integrated smoothly into the resume below. Additionally, address the mentioned issues and implement the provided suggestions.

{format_instructions}

You must not include any explanation whatsoever, only pure JSON!

# Skills to add:
{missing_skills}

# Issues to address:
{issues}

# What to fix:
{suggestions}

# RESUME:
{resume}

\n
"""


class Degree(BaseModel):
    GPA: str | None = Field(None, description="Grade Point Average")
    college: str | None = Field(None, description="Name of the college")
    degreeName: str | None = Field(None, description="Name of the degree")
    endYear: str | None = Field(None, description="End year of the degree")
    location: str | None = Field(None, description="Location of the college")
    startYear: str | None = Field(None, description="Start year of the degree")


class Intro(BaseModel):
    citizenship: str | None = Field(
        None, description="Citizenship information")
    email: str | None = Field(None, description="Email address")
    linkedin: str | None = Field(None, description="LinkedIn profile")
    location: str | None = Field(None, description="Location information")
    personName: str | None = Field(None, description="Name of the person")
    phone: str | None = Field(None, description="Phone number")
    summary: str | None = Field(None, description="Summary or bio")
    website: str | None = Field(None, description="Personal website")


class Job(BaseModel):
    company: str | None = Field(None, description="Name of the company")
    endDate: str | None = Field(None, description="End date of the job")
    location: str | None = Field(None, description="Location of the job")
    responsibilities: List[str] | None = Field(
        [], description="List of job responsibilities, each responsibility should be in a separate array item")
    startDate: str | None = Field(None, description="Start date of the job")
    title: str | None = Field(None, description="Job title")


class Project(BaseModel):
    code: str = Field("", description="Code or repository link")
    description: str | None = Field(
        None, description="Description of the project")
    link: str = Field("", description="Link to the project")


class SkillDict(BaseModel):
    Skills: List[str] | None = Field(
        [], description="List of technical skills")
    Interests: List[str] | None = Field(
        [], description="List of personal interests")


class StructuredResume(BaseModel):
    degrees: List[Degree] | None = Field(
        [], description="List of educational degrees")
    intro: Intro | None = Field({}, description="Introduction section")
    jobs: List[Job] | None = Field([], description="List of work experiences")
    projectList: List[Project] | None = Field([], description="List of projects")
    skillDict: Dict[str, List[str]] | None = Field({},
                                                   description="Dictionary of skills and interests, for example: Programming, Infrastructure & Automation, Other Skills")


resume_fixer_parser = PydanticOutputParser(
    pydantic_object=StructuredResume)  # type: ignore

revamp_resume_prompt = PromptTemplate(
    template=revamp_tmpl,
    input_variables=["resume", "suggestions", "issues", "missing_skills"],
    partial_variables={
        "format_instructions": resume_fixer_parser.get_format_instructions()
    }
)

# print(resume_fixer_parser.get_format_instructions())

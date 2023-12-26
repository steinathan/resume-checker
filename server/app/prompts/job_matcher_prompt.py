from typing import List

from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

job_analysis_tmpl = """
# Instruction:
You are an expert
You're tasked with checking and validating resume by comparing it to the job 
description below. Your responsibility is to strictly determine whether the resume is suitable for the job or not.

{format_instructions}

no other explanations must be produced

# RESUME:
{resume}

# JOB DESCRIPTION:
{job_description}

# YOUR OUTPUT:
\n
"""


class JobSection(BaseModel):
    value: List[str] = Field(description="the value of the section")
    explanations: List[str] = Field(description="list of possible explanations")
    improvements: List[str] = Field(
        description="If applicable, suggest improvements to the section based on its value.")
    # met: bool = Field(description="whether or not")


class ResumeJobPromptModel(BaseModel):
    """ analyzes a job against a resume """
    education: JobSection = Field(
        description="Specify the educational qualifications necessary for the job description")
    # experience: JobSection = Field(description="Outline the required work experience for the job.")
    met_skills: JobSection = Field(
        description="Identify the essential skills outlined in the job description that the resume meets")
    unmet_skills: JobSection = Field(
        description="Identify the essential skills outlined in the job description that the resume did not meet")
    resume_skills: JobSection = Field(description="Identify and list the skills mentioned in the resume")
    avoidable_keywords: JobSection = Field(
        description="Identify and list keywords in the resume that may not be suitable or relevant for the job and "
                    "could be omitted.")
    score: float = Field(
        description="Evaluate the alignment of the resume with the job description. float from [0.0-10.0].")
    explanation: str = Field(default="Explain whether the resume is suitable or unsuitable for the job description "
                                     "and the reasons behind it.")


analyse_resume_parser = PydanticOutputParser(pydantic_object=ResumeJobPromptModel)

print(analyse_resume_parser.get_format_instructions())

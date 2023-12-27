from typing import List

from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

job_ats_tmpl = """# Instruction: You are an expert ATS personnel evaluating the resume of a user for a job. You're 
tasked with checking and validating resume by comparing it to the job description below. Your responsibility is to  

strictly determine whether the resume is suitable for the job or not. your response must be in a second person point of view, eg. use "Your" instead "The user"

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
    values: List[str] = Field(description="list of the values of the section")
    explanations: List[str] = Field(description="list of possible explanations")
    improvements: List[str] = Field(
        description="If applicable, suggest improvements to the section based on its value.")


class AtsJobPromptModel(BaseModel):
    """ analyzes a job against a resume """
    education: JobSection = Field(
        description="Extract the educational qualifications necessary for the job from the job description")
    # experience: JobSection = Field(description="Outline the required work experience for the job.")
    met_skills: JobSection = Field(
        description="Identify the essential skills outlined in the job description that the resume meets")
    unmet_skills: JobSection = Field(
        description="Identify the essential skills outlined in the job description that the resume did not meet")
    resume_skills: JobSection = Field(description="Identify and list the skills mentioned in the resume")
    avoidable_keywords: JobSection = Field(
        description="Identify and list keywords in the work experience and skills section that may not be suitable or "
                    "relevant for the job and could be omitted.")
    score: float = Field(
        description="Evaluate the alignment of the resume with the job description. float from [0.0-10.0].")
    explanation: str = Field(default="Explain whether the resume is suitable or unsuitable for the job description "
                                     "and the reasons behind it.")


job_ats_parser = PydanticOutputParser(pydantic_object=AtsJobPromptModel)


job_ats_prompt = PromptTemplate(
    template=job_ats_tmpl,
    input_variables=["resume", "job_description"],
    partial_variables={
        "format_instructions": job_ats_parser.get_format_instructions()
    }
)


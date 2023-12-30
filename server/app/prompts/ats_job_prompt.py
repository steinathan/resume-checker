from enum import Enum
from typing import List

from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

job_ats_tmpl = """You are an expert ATS analyzer personnel evaluating my resume for a potential job i'm applying for.
 You're tasked with checking and validating my resume by comparing it to the job description below.

{format_instructions}

no other explanations must be produced

# JOB DESCRIPTION:
{job_description}
# END JOB DESCRIPTION

# MY RESUME:
{resume}
# END RESUME

# MY RESUME ANALYSIS:
\n
"""


class JobSection(BaseModel):
    issues: List[str] = Field(
        description="If applicable to the section, identify and list any potential issue that might present challenges in securing the job.")
    # values: List[str] = Field(
    #     description="If applicable to the section. Enumerate the values within the section that align with the given instructions.")
    explanation: str = Field(
        description="Provide potential explanations or justifications for the identified issues in the section.")
    suggestion: str = Field(description="If applicable, suggest improvements to the section based on its value.")
    score: float = Field(
        description="Assign a score to the section indicating how well the resume aligns with the job description, on a scale from 0 to 10.")


class RejectionRateEnum(str, Enum):
    unknown = "unknown"
    very_low = 'very_low'
    low = 'low'
    medium = 'medium'
    high = 'high'
    very_high = 'very_high'


class SkillType(str, Enum):
    hard = 'hard'
    soft = 'soft'


class AtsSkill(BaseModel):
    value: str = Field(description="the value of the skill found from the job description.")
    match: bool = Field(description="Determine whether or not i have the skill in my resume or not from the job")
    type: SkillType = Field(description="The skill type.")


class TitleMatch(BaseModel):
    explanation: str = Field(description="possible explanation for the match")
    match: bool = Field(default=False, description="indicate if the job title is matched within the resume")


class AtsJobPromptModel(BaseModel):
    """ analyzes a job against a resume """
    job_title: str = Field(description="Extract the job title from the provided job description")
    company_name: str = Field(description="Extract the company's name from the job description or make an inference "
                                          "if it's not explicitly mentioned")
    education: JobSection = Field(
        description="Extract the educational qualifications necessary for the job from the job description only")
    avoidable_keywords: JobSection = Field(
        description="Identify and list keywords in the work experience and skills section that may not be suitable or "
                    "relevant for the job and could be omitted.")
    score: float = Field(
        description="Evaluate the alignment of the resume with the job description. float from [0.0-10.0].")
    summary: str = Field(description="Explain whether the resume is suitable or unsuitable for the job description "
                                     "and the reasons behind it.")
    title_match: TitleMatch = Field(description="indicate if the job title from the job description is matched within "
                                                "the resume or not")


job_ats_parser = PydanticOutputParser(pydantic_object=AtsJobPromptModel)

job_ats_prompt = PromptTemplate(
    template=job_ats_tmpl,
    input_variables=["resume", "job_description"],
    partial_variables={
        "format_instructions": job_ats_parser.get_format_instructions()
    }
)

print(job_ats_parser.get_format_instructions())

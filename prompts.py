from typing import List

from langchain.output_parsers import ResponseSchema, StructuredOutputParser, PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field, validator, field_validator

checker_tmpl = """
# Instruction:
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

cover_letter_tmpl = """# Instruction: Below is a job description and a cover letter. Your responsibility is to 
generate a cover letter than can be used as it is with a tile and body

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

checker_response_schemas = [
    ResponseSchema(name="score", description="the score to the resume against the job description, from [0-10]",
                   type="float"),
    ResponseSchema(name="fit", description="if the resume is qualified for the job or not", type="boolean"),
    ResponseSchema(name="explanation", description="why the resume is fit or not for the job description"),
    ResponseSchema(name="fixes",
                   description="if not fit, explain in a markdown step by step the different ways the resume can be "
                               "improved for"
                               "the job in a first person singular. eg. you should highlight any experience or skill.."),
]

check_output_parser = StructuredOutputParser.from_response_schemas(checker_response_schemas)

resume_checker_prompt = PromptTemplate(
    template=checker_tmpl,
    input_variables=["resume", "job_description"],
    partial_variables={
        "format_instructions": check_output_parser.get_format_instructions()
    }
)

resume_cover_letter_prompt = PromptTemplate(
    template=cover_letter_tmpl,
    input_variables=["resume", "job_description"],
)


class ResumeSection(BaseModel):
    issues: List[str] = Field(
        description="issues you found in the section, eg. missing end-date, inconsistent date formatting")
    improvements: List[str] = Field(description="ways in which the section can be improved based on the issue")
    done: List[str] = Field(
        description="things user did for sections, examples: provided your phone number. provided your email."
                    "added a work experience")
    score: float = Field(description="score to the section on how well it is, from [0-10]", default=0.0)


class ResumeCheckerModel(BaseModel):
    # ats_tips: Section = Field(description="tips for the ATS")
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

    # computed at runtime
    # total_score: float = 0.0

    # @field_validator("total_score")
    # def compute_total_score(cls, total_score: float, values):
    #     section_scores = [values[section].score for section in values if isinstance(values[section], ResumeSection)]
    #     return sum(section_scores) / max(len(section_scores), 1)


analyse_resume_parser = PydanticOutputParser(pydantic_object=ResumeCheckerModel)

analyse_resume_prompt = PromptTemplate(
    template=analyse_resume_tmpl,
    input_variables=["resume"],
    partial_variables={
        "format_instructions": analyse_resume_parser.get_format_instructions()
    }
)

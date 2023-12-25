from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.prompts import PromptTemplate

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

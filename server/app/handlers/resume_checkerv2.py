from __future__ import annotations

import logging
import os
import tempfile
from dataclasses import dataclass
from datetime import datetime

import requests
import validators
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain_community.chat_models import ChatOpenAI
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.llms.ollama import Ollama
from langchain_community.llms.together import Together
from langchain_core.callbacks import StreamingStdOutCallbackHandler, CallbackManager

from app.prompts.ats_job_prompt import job_ats_parser, job_ats_prompt, AtsJobPromptModel
from app.prompts.resume_analysis_prompt import resume_cover_letter_prompt, analyse_resume_prompt, \
    ResumeCheckerModel, analyse_resume_parser

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[
        logging.FileHandler("resume_logger.log"),
        logging.StreamHandler()
    ]
)


def is_valid_url(url: str) -> bool:
    return validators.url(url)


def download_pdf(url):
    response = requests.get(url)

    if response.status_code == 200:
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_file:
            temp_file.write(response.content)
            temp_file_path = temp_file.name
            print(f"PDF downloaded successfully. File path: {temp_file_path}")
            return temp_file_path
    else:
        print(f"Failed to download PDF. Status code: {response.status_code}")
        return None


def trim_space(text: str) -> str:
    return text.replace("\n", " ").replace("\r", " ").replace("\t", " ")


@dataclass
class AtsAnalyserResult:
    resume_content: str | None
    job_url: str | None
    job_description: str
    generated_cover_letter: str | None = None
    ats_analysis: AtsJobPromptModel | None = None


class ResumeAnalyser:
    """ ResumeAnalyser takes in a path to your resume and a job posting URL and lets you know if you're fit for the
    job or not"""
    llm = any
    resume_content: str | None = ""
    job_content: str | None = ""

    def __init__(self, job_posting_url: str | None = None, resume_file_path: str | None = None,
                 resume_content: str | None = None, job_content: str | None = None):
        self.job_posting_url = job_posting_url
        self.resume_content = resume_content
        self.resume_path = resume_file_path
        self.job_content = job_content

        # either resume_content or path should be provided
        if not resume_content and not resume_file_path:
            raise ValueError("Either resume_content or resume_file_path must be provided")

        model_name = os.getenv("LLM_MODEL")
        if model_name == "openai":
            self.llm = ChatOpenAI(model_name="gpt-3.5-turbo-1106")
        elif model_name == "ollama":
            self.llm = Ollama(
                model="mistral",
                callback_manager=CallbackManager(
                    [StreamingStdOutCallbackHandler()])
            )
        elif model_name == "together":
            self.llm = Together(
                model="mistralai/Mistral-7B-Instruct-v0.2",
                temperature=0.7,
                top_k=1,
            )
        else:
            raise ValueError("Invalid LLM model name")

        logging.info(f"Using {model_name} model")

        self.load_resume(self.resume_path or "")

        if self.job_posting_url:
            self.load_job_site(self.job_posting_url)

    def load_resume(self, path: str):
        """ loads the resume text from the resume path """
        if not self.resume_content:
            logging.info(f"Resume content not provided, loading resume from URL or PATH: {path}")
            if is_valid_url(path):
                logging.info(f"Loading resume from HTTP: {path}")
                path = download_pdf(path)
            loader = PyPDFLoader(path)
            logging.info(f"Loading resume from local file: {path}")

            docs = loader.load()
            for doc in docs:
                if not self.resume_content:
                    self.resume_content = ""
                self.resume_content += trim_space(doc.page_content)

    def load_job_site(self, url):
        """ loads the job text from the job site url """
        loader = WebBaseLoader(url)
        docs = loader.load()
        for doc in docs:
            if not self.job_content:
                self.job_content = ""
            self.job_content += trim_space(doc.page_content)

    def run_ats(self) -> AtsAnalyserResult:
        """ Runs the program for an ATS """
        check_prompt_str = job_ats_prompt.format(
            resume=self.resume_content, job_description=self.job_content)
        logging.debug(check_prompt_str)
        output = self.llm.predict(check_prompt_str)
        ats_result: AtsJobPromptModel = job_ats_parser.parse(output)
        fit = ats_result.score > 6.5

        cover_letter: str | None = None

        if fit:
            cover_letter = self.generate_cover_letter()
        else:
            logging.info("resume is not fit, refusing to generate cover letter")

        return AtsAnalyserResult(
            resume_content=self.resume_content,
            generated_cover_letter=cover_letter,
            ats_analysis=ats_result,
            job_description=self.job_content,
            job_url=self.job_posting_url,
        )

    def analyse_resume(self) -> ResumeCheckerModel:
        """ analyses the resume extracting, ats tips, contact info, education match, date formatting and file type,
        this only analysis the resume without the job description"""
        analyse_resume_prompt_str = analyse_resume_prompt.format(resume=self.resume_content)
        output = self.llm.predict(analyse_resume_prompt_str)
        resume_analysis_result = analyse_resume_parser.parse(output)
        return resume_analysis_result

    def generate_cover_letter(self) -> str:
        """ generate cover letter for the job"""
        cover_letter_prompt_str = resume_cover_letter_prompt.format(resume=self.resume_content,
                                                                    job_description=self.job_content)
        cover_letter = self.llm.predict(cover_letter_prompt_str)
        logging.debug(cover_letter_prompt_str)

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"cover_letter_{timestamp}.txt"
        filename = os.path.join("cover_letters", filename)

        with open(filename, "w") as f:
            f.write(cover_letter)

        logging.info(f"Cover letter generated at {filename}")
        print(f"""
Here's an example cover letter you can use
{cover_letter}
        """)
        return cover_letter

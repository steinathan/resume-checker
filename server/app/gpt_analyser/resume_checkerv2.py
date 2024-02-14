from __future__ import annotations

import logging
import os
import re
import tempfile
from dataclasses import dataclass
from typing import Any, List
import fitz

import requests
import validators
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.llms.ollama import Ollama
from langchain_community.llms.together import Together
from langchain_core.callbacks import StreamingStdOutCallbackHandler, CallbackManager

from app.prompts.ats_job_prompt import job_ats_parser, job_ats_prompt, AtsJobPromptModel
from app.prompts.resume_analysis_prompt import resume_cover_letter_prompt, analyse_resume_prompt, \
    ResumeCheckerModel, analyse_resume_parser, ResumeAnalysisResult
from app.prompts.resume_fixer import revamp_resume_prompt, resume_fixer_parser, StructuredResume

load_dotenv()


def is_valid_url(url: str) -> bool:
    return validators.url(url)


def detect_email(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    matches = re.findall(email_pattern, text)
    return len(matches) > 0 if matches else None


def detect_linkedin(text):
    """ detect a linkedin url or string """
    linkedin_pattern = r'(linkedin\.com\/\w+)|(linkedin\.com\/in\/\w+)|(\bLinkedIn\b)'
    matches = re.search(linkedin_pattern, text, flags=re.IGNORECASE)
    return matches.group() if matches else None


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


def has_interest(text):
    pattern = re.compile(r'\b:\s*interests?\s*:\b|\binterests?\b|\b:\s*interests?\b|\binterests?\s*:\b', re.IGNORECASE)
    return bool(pattern.search(text))


def extract_text_with_formatting(pdf_path) -> tuple[str, int]:
    """ langchain pdf doesn't preserve formatting"""
    # noinspection PyUnresolvedReferences
    doc = fitz.open(pdf_path)
    text = ""

    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()

    return text, doc.page_count


@dataclass
class AtsAnalyserResult:
    resume_content: str | None
    job_url: str | None
    job_description: str
    generated_cover_letter: str | None = None
    ats_analysis: AtsJobPromptModel | None = None


def calculate_word_count(text: str) -> int:
    """ calculate word count of text """
    words = text.split()
    word_count = len(words)
    return word_count


def to_prompt_bullet(items: List[str]) -> str:
    """ """
    return ", ".join([f"{item}" for item in items])


class ResumeAnalyser:
    """ ResumeAnalyser takes in a path to your resume and a job posting URL and lets you know if you're fit for the
    job or not"""
    llm: Any = None
    resume_content: str | None = ""
    job_content: str | None = ""
    resume_page_count: int | None = None

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
            self.llm = ChatOpenAI(model_name="gpt-3.5-turbo-1106")  # type: ignore
        elif model_name == "ollama":
            self.llm = Ollama(
                model="mistral",
                callback_manager=CallbackManager(
                    [StreamingStdOutCallbackHandler()])
            )
        elif model_name == "together":
            self.llm = Together(  # type: ignore
                model="openchat/openchat-3.5-1210",
                temperature=0,
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
            logging.info(f"Loading resume from local file: {path}")
            self.resume_content, self.resume_page_count = extract_text_with_formatting(path)

    def load_job_site(self, url):
        """ loads the job text from the job site url """
        loader = WebBaseLoader(url)
        docs = loader.load()
        for doc in docs:
            if not self.job_content:
                self.job_content = ""
            self.job_content += (doc.page_content)

    def run_ats(self) -> AtsAnalyserResult:
        """ Runs the program for an ATS """
        check_prompt_str = job_ats_prompt.format(
            resume=self.resume_content, job_description=self.job_content)
        logging.debug(check_prompt_str)
        output = self.llm.predict(check_prompt_str)
        ats_result: AtsJobPromptModel = job_ats_parser.parse(output)

        cover_letter: str = self.generate_cover_letter()
        return AtsAnalyserResult(
            resume_content=self.resume_content,
            generated_cover_letter=cover_letter,
            ats_analysis=ats_result,
            job_description=str(self.job_content),
            job_url=self.job_posting_url,
        )

    def analyse_resume(self) -> ResumeAnalysisResult:
        """ analyses the resume extracting, ats tips, contact info, education match, date formatting and file type,
        this only analysis the resume without the job description"""
        analyse_resume_prompt_str = analyse_resume_prompt.format(resume=self.resume_content)
        output = self.llm.predict(analyse_resume_prompt_str)

        llm_output: ResumeCheckerModel = analyse_resume_parser.parse(output)
        analysis_result = ResumeAnalysisResult(**llm_output.model_dump())

        # local word count calculations & ema+il/LinkedIn parsing
        word_count = calculate_word_count(str(self.resume_content))
        if word_count < 475:
            analysis_result.word_count.issues.append(
                f"There are {word_count} words in your resume, which is below the recommended word for your resume")
            analysis_result.word_count.improvements.append("Consider adding more targeted keywords and strong nouns")
            analysis_result.word_count.score = 7.5
        elif word_count > 600:
            analysis_result.word_count.issues.append(
                f"There are {word_count} words in your resume, which is above the recommended word for your resume")
            analysis_result.word_count.improvements.append("Consider removing some keywords and nouns")
            analysis_result.word_count.score = 5.5

        # check for contact email & urls
        if not detect_linkedin(self.resume_content):
            analysis_result.contact_info.issues.append("No linkedin url provided")
            analysis_result.contact_info.improvements.append(
                "Including your LinkedIn on your resume lets recruiters quickly explore your professional journey and achievements.")

        if not detect_email(self.resume_content):
            # score auto added by gpt
            analysis_result.contact_info.issues.append("No email address provided")
            analysis_result.contact_info.improvements.append(
                "Consider adding an email address, Use a professional-looking gmail, outlook, or personal domain email address. Delete your hotmail if any with extreme prejudice.")

        if self.resume_page_count is not None and self.resume_page_count > 1:
            analysis_result.file_info.issues.append("Resume pages are much")
            analysis_result.file_info.improvements.append("Unless you have 20+ years' experience, make it 1 page.")
            analysis_result.file_info.score = 6.5
        else:
            analysis_result.file_info.score = 9

        if not has_interest(self.resume_content):
            analysis_result.interests.issues.append("No interests provided")
            analysis_result.interests.improvements.append(
                "Interests are important because it gives the interviewer something to connect with you on, and it makes you more than just a faceless resume")
            analysis_result.interests.score = 1.5
        else:
            analysis_result.interests.score = 9

        return analysis_result

    def generate_cover_letter(self) -> str:
        """ generate cover letter for the job"""
        cover_letter_prompt_str = resume_cover_letter_prompt.format(resume=self.resume_content,
                                                                    job_description=self.job_content)
        cover_letter = self.llm.predict(cover_letter_prompt_str)
        logging.debug(cover_letter_prompt_str)

        return cover_letter

    def revamp_resume(self, skills: List[str], suggestions: List[str], issues: List[str]) -> StructuredResume:
        """ revamp the resume fixing the issues """
        revamp_prompt_str = revamp_resume_prompt.format(
            resume=self.resume_content,
            suggestions=to_prompt_bullet(suggestions),
            issues=to_prompt_bullet(issues),
            missing_skills=to_prompt_bullet(skills),
        )
        logging.debug(revamp_prompt_str)

        llm_out = self.llm.predict(revamp_prompt_str)
        revamped_resume: StructuredResume = resume_fixer_parser.parse(llm_out)

        return revamped_resume

from __future__ import annotations

import logging

from pydantic import BaseModel

from app.handlers.resume_checkerv2 import ResumeAnalyser, AtsAnalyserResult
from app.models.common_models import Resume, User, CoverLetter, AtsJobScan
from app.skill_extractor.skill_extractor import SkillExtractor
from app.supabase_client.client import supabase
from uuid import uuid4

from app.skill_extractor.skill_extractor import MatchingResult as SkillExtractorResult
from app.prompts.resume_analysis_prompt import ResumeCheckerModel, ResumeAnalysisResult

TABLE_NAME = "resumes"
COVER_LETTER_TABLE = "cover_letters"
JOB_SCAN_TABLE = "job_scans"


class AnalyseJobForResumeParams(BaseModel):
    job_url: str | None = None
    job_description: str | None = None
    resume_id: str | None = None


class CreateResumeParams(BaseModel):
    """ create resume parameters after uploading one"""
    src: str
    name: str
    text: str | None = None


def create_new_resume(user: User, params: CreateResumeParams) -> Resume:
    resume_id = str(uuid4())
    if params.src:
        if not params.src.endswith("pdf"):
            raise ValueError("src must be a valid PDF")

    resume = Resume(**params.model_dump(), user_id=user.id, id=resume_id)
    response = supabase.table(TABLE_NAME).insert(resume.model_dump()).execute()
    return Resume(**response.data[0])


def find_all_resumes(user: User) -> list[Resume]:
    response = supabase.table(TABLE_NAME).select(
        "*").order("created_at", desc=True).eq("user_id", user.id).execute()
    return [Resume(**data) for data in response.data]


def update_resume(user: User, resume_id: str, resume: Resume) -> Resume | None:
    (supabase.table(TABLE_NAME).update(resume.model_dump())
     .eq("user_id", user.id)
     .eq("id", resume_id)
     .execute())
    return find_resume_by_id(user, resume_id)


async def delete_resume(user: User, resume_id: str) -> bool:
    await (supabase.table(TABLE_NAME).delete()
           .eq("user_id", user.id)
           .eq("id", resume_id)
           .execute())
    return True


def find_resume_by_id(user: User, resume_id: str) -> Resume | None:
    response = supabase.table(TABLE_NAME).select(
        "*").eq("user_id", user.id).eq("id", resume_id).execute()
    if response.data:
        return Resume(**response.data[0])
    return None


class JobScanResult(BaseModel):
    cover_letter: CoverLetter | None = None
    job_scan: AtsJobScan | None = None


def find_job_scan_by_id(user: User, scan_id: str) -> JobScanResult | None:
    response = supabase.table(JOB_SCAN_TABLE).select(
        "*").eq("user_id", user.id).eq("id", scan_id).execute()

    cover_letter = None

    if response.data:
        job_scan = AtsJobScan(**response.data[0])
        response = (supabase.table(COVER_LETTER_TABLE).select("*")
                    .eq("scan_id", job_scan.id)
                    .maybe_single()
                    .execute())

        if response:
            cover_letter = CoverLetter(**response.data)

        return JobScanResult(cover_letter=cover_letter, job_scan=job_scan)
    return None


def create_cover_letter(user_id: str, resume_id: str, scan_id: str, cover_letter_text=str) -> CoverLetter:
    letter = CoverLetter(
        id=str(uuid4()),
        user_id=user_id,
        scan_id=scan_id,
        resume_id=resume_id,
        text=cover_letter_text
    )

    logging.info("creating job scan result", letter.model_dump())
    response = supabase.table(COVER_LETTER_TABLE).insert(
        letter.model_dump()).execute()
    return CoverLetter(**response.data[0])


def create_scan_result(skills_result: SkillExtractorResult, scan_result: AtsAnalyserResult, user: User,
                       resume: Resume) -> AtsJobScan:
    job = AtsJobScan(
        id=str(uuid4()),
        user_id=str(user.id),
        resume_id=str(resume.id),
        job_description=scan_result.job_description,
        ats_analysis=scan_result.ats_analysis,
        skills_analysis=skills_result
    )

    if scan_result is not None:
        job.job_url = scan_result.job_url

    logging.info("creating job scan result", job.model_dump())
    response = supabase.table(JOB_SCAN_TABLE).insert(
        job.model_dump()).execute()
    return AtsJobScan(**response.data[0])


def process_ats_scan(user: User, params: AnalyseJobForResumeParams):
    resume = find_resume_by_id(user, str(params.resume_id))
    if not resume:
        raise Exception("Resume not found for user")

    analyzer = ResumeAnalyser(job_posting_url=params.job_url, job_content=params.job_description,
                              resume_content=resume.text)
    ats_result: AtsAnalyserResult = analyzer.run_ats()

    skill_extractor = SkillExtractor()
    skill_extractor_result = skill_extractor.process_ats_skills(
        str(analyzer.resume_content), str(analyzer.job_content))

    # create resume ats job scan in db
    job_scan = create_scan_result(skills_result=skill_extractor_result, scan_result=ats_result, user=user,
                                  resume=resume)

    # create cover letter
    if ats_result.generated_cover_letter is not None:
        cover_letter = create_cover_letter(
            user.id, resume.id, job_scan.id, ats_result.generated_cover_letter)

    return job_scan


async def analyze_resume(user: User, resume_id: str) -> ResumeCheckerModel:
    resume = find_resume_by_id(user, resume_id)
    if not resume:
        raise Exception("Resume not found for user")

    # process via LLM
    analyzer = ResumeAnalyser(
        resume_content=resume.text, resume_file_path=resume.src)
    analysis: ResumeAnalysisResult = analyzer.analyse_resume()

    # extract skills
    skill_extractor = SkillExtractor()
    skills = skill_extractor.get_skills(str(analyzer.resume_content))

    # update the resume with analysis results
    update_resume(user, str(resume.id), resume.model_copy(update={
        "analysis": analysis,
        "text": analyzer.resume_content,
        "skills": skills
    }
    ))

    return analysis


def list_job_scans_for_user(user: User) -> list[AtsJobScan]:
    response = supabase.table(JOB_SCAN_TABLE).select("*").order("created_at", desc=True).eq("user_id",
                                                                                            user.id).execute()
    return [AtsJobScan(**data) for data in response.data]

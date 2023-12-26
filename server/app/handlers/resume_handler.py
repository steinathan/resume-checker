from __future__ import annotations

from pydantic import BaseModel

from app.handlers.resume_checkerv2 import ResumeAnalyser, ResumeAnalyserResult
from app.models.common_models import Resume, User
from app.supabase_client.client import supabase
from uuid import uuid4

from prompts import ResumeCheckerModel

TABLE_NAME = "resumes"


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
    resume = Resume(**params.model_dump(), user_id=user.id, id=resume_id)
    response = supabase.table(TABLE_NAME).insert(resume.model_dump()).execute()
    return Resume(**response.data[0])


def find_all_resumes(user: User) -> list[Resume]:
    response = supabase.table(TABLE_NAME).select("*").eq("user_id", user.id).execute()
    return [Resume(**data) for data in response.data]


def update_resume(user: User, resume_id: str, resume: Resume) -> Resume:
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
    response = supabase.table(TABLE_NAME).select("*").eq("user_id", user.id).eq("id", resume_id).execute()
    if response.data:
        return Resume(**response.data[0])
    return None


def process_job_for_resume(user: User, params: AnalyseJobForResumeParams):
    resume = find_resume_by_id(user, params.resume_id)
    if not resume:
        raise Exception("Resume not found for user")
    analyzer = ResumeAnalyser(job_posting_url=params.job_url, resume_content=resume.text)
    result: ResumeAnalyserResult = analyzer.run()
    return result


async def analyze_resume(user: User, resume_id: str) -> object:
    resume = find_resume_by_id(user, resume_id)
    if not resume:
        raise Exception("Resume not found for user")

    analyzer = ResumeAnalyser(resume_content=resume.text, resume_file_path=resume.src)
    analysis: ResumeCheckerModel = analyzer.analyse_resume()

    # update the resume with analysis results
    update_resume(user, resume.id, resume.model_copy(update={"analysis": analysis, "text": analyzer.resume_content}))

    return analysis

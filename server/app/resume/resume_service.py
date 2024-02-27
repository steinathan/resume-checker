from __future__ import annotations

import logging
import os
from datetime import datetime
from typing import List

from prisma.models import Resume
from prisma.types import ResumeCreateInput, ResumeUpdateInput
from pydantic import BaseModel

from app.gpt_analyser.resume_checkerv2 import ResumeAnalyser, AtsAnalyserResult
from app.helpers.resume_generator import build_resume
from app.models.common_models import User, CoverLetter, AtsJobScan
from app.prompts.ats_job_prompt import JobSection
from app.prompts.resume_fixer import StructuredResume
from app.skill_extractor.skill_extractor import SkillExtractor, AtsSkill, MatchingResult
from app.supabase_client.client import supabase
from uuid import uuid4

from app.skill_extractor.skill_extractor import MatchingResult as SkillExtractorResult
from app.prompts.resume_analysis_prompt import ResumeCheckerModel, ResumeAnalysisResult, ResumeSection

RESUME_TABLE = "resumes"
COVER_LETTER_TABLE = "cover_letters"
JOB_SCAN_TABLE = "job_scans"


class AnalyseJobForResumeParams(BaseModel):
    job_url: str | None = None
    job_description: str | None = None
    resume_id: str | None = None


async def create_new_resume(user: User, params: ResumeCreateInput) -> Resume:
    data: ResumeCreateInput = {
        "user_id": user.id,
        "title": params.get("title"),
        "slug": params.get("slug")
    }
    resume = await Resume.prisma().create(data=data)
    return resume


async def find_all_resumes(user: User) -> list[Resume]:
    user_resumes = await Resume.prisma().find_many(
        where={
            "user_id": user.id
        },
        order={
            "updated_at": "desc"
        }
    )
    return user_resumes


async def update_resume(resume_id: str, params: ResumeUpdateInput) -> Resume | None:
    resume = await Resume.prisma().update(
        where={
            "id": resume_id,
        },
        data=params)
    return resume


async def delete_resume(user: User, resume_id: str) -> bool:
    # TODO: delete the file, then the cover letter, then the resume
    await Resume.prisma().delete(where={
        "id": resume_id,
        # "user_id": user.id
    })
    return True


def find_resume_by_id(user: User, resume_id: str) -> Resume | None:
    response = (supabase.table(RESUME_TABLE)
                .select("*")
                .eq("user_id", user.id)
                .eq("id", resume_id).execute()
                )
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

    skill_extractor = SkillExtractor(resume.skills)
    skill_extractor_result: MatchingResult = skill_extractor.process_ats_skills(
        str(analyzer.resume_content), str(analyzer.job_content))

    #  get the percentage of skills matched vs not match / 10
    matched_skills = skill_extractor_result.matched_skills
    unmatched_skills = skill_extractor_result.unmatched_skills

    skill_score = len(matched_skills) / len(unmatched_skills) * 10

    # if ats_result.ats_analysis.title_match.match:  # type: ignore
    #     skill_score += 3

    ats_result.ats_analysis.score = round(skill_score)  # type: ignore
    # create resume ats job scan in db
    job_scan = create_scan_result(skills_result=skill_extractor_result, scan_result=ats_result, user=user,
                                  resume=resume)

    # create cover letter
    if ats_result.generated_cover_letter is not None:
        cover_letter = create_cover_letter(
            user.id, resume.id, job_scan.id, ats_result.generated_cover_letter)

    return job_scan


def fix_resume(user: User, resume_id: str, scan_id: str | None = None):
    """ gets issues, suggestions and skills, and trys to `fix` the resume using a default resume template """
    # TODO: get list of templates from DB
    template_name = "master_tmpl.docx"
    master_tmpl_path = os.path.join(os.getcwd(), 'resume_templates', template_name)

    resume = find_resume_by_id(user, resume_id)
    if not resume:
        raise Exception("Resume not found for user")

    analyzer = ResumeAnalyser(
        resume_content=resume.text, resume_file_path=resume.src)

    issues: List[str] = []
    suggestions: List[str] = []
    missing_skills: List[str] = []

    # find all issues & suggestions from resume and job description
    if resume.analysis:
        vals = resume.analysis.__dict__.items()
        for key, value in vals:
            if isinstance(value, ResumeSection):
                issues.extend(value.issues)
                suggestions.extend(value.improvements)

    if scan_id:
        scan_result = find_job_scan_by_id(user, scan_id)
        if scan_result and scan_result.job_scan:
            job_scan = scan_result.job_scan

            # find missing skills from job description
            ats_skills: list[AtsSkill] = job_scan.skills_analysis.ats_skills if job_scan.skills_analysis else []
            missing_skills.extend([skill.name for skill in ats_skills])

            # add improvements && issues from scan result
            if job_scan.ats_analysis:
                vals = job_scan.ats_analysis.__dict__.items()
                for key, value in vals:
                    if isinstance(value, JobSection):
                        issues.extend(value.issues)
                        suggestions.append(value.suggestion)

    analysis: StructuredResume = analyzer.revamp_resume(issues=issues, suggestions=suggestions, skills=missing_skills)
    new_resume = build_resume(master_tmpl_path, analysis)

    return new_resume


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
    response = (supabase.table(JOB_SCAN_TABLE)
                .select("*")
                .order("created_at", desc=True)
                .eq("user_id", user.id)
                .execute())
    return [AtsJobScan(**data) for data in response.data]

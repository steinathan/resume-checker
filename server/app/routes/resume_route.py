from __future__ import annotations

import logging
from pathlib import Path
from typing import Annotated, Optional, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from starlette.responses import FileResponse

from app.dependencies import get_current_user
from app.handlers import resume_handler, user_handler
from app.handlers.resume_handler import CreateResumeParams
from app.models.common_models import Resume, User

router = APIRouter(
    tags=["resume"],
    dependencies=[Depends(get_current_user)],
)


@router.post("/resume", response_model=Resume)
async def create_resume(params: CreateResumeParams, current_user: Annotated[User, Depends(get_current_user)]):
    """ creates a new resume called after uploading to bucket"""
    if current_user.resume_analysis_remaining <= 0:
        raise Exception("You have no resume analysis remaining")

    resume = resume_handler.create_new_resume(current_user, params)
    try:
        await resume_handler.analyze_resume(current_user, resume.id)
        resume = resume_handler.find_resume_by_id(current_user, resume.id)

        # update plan details for user
        if resume and current_user.plan == "free":
            current_user.resume_analysis_remaining -= 1
            await user_handler.update_user_by_dict(current_user.id, {
                "resume_analysis_remaining": current_user.resume_analysis_remaining,
            })

        return resume
    except Exception as e:
        logging.error(e)
        await resume_handler.delete_resume(current_user, resume.id)
        raise HTTPException(status_code=500, detail="Error processing resume, kindly re-upload this resume")


@router.get("/resumes", response_model=Optional[List[Resume]])
async def list_resume(current_user: Annotated[User, Depends(get_current_user)]):
    """ list all resumes for user """
    return resume_handler.find_all_resumes(current_user)


@router.get("/resumes/{resume_id}", response_model=Optional[Resume])
async def find_resume(resume_id: str, current_user: Annotated[User, Depends(get_current_user)]):
    """ finds the resume by id """
    return resume_handler.find_resume_by_id(current_user, resume_id)


@router.delete("/resume/{resume_id}", response_model=Resume)
async def delete_resume_by_id(resume_id: str, current_user: Annotated[User, Depends(get_current_user)]):
    await resume_handler.delete_resume(current_user, resume_id)


@router.post("/resume/{resume_id}/analyze")
async def analyze_user_resume(resume_id: str, current_user: Annotated[User, Depends(get_current_user)]):
    """ analyzes a resume extracting fixes and suggestions, save the results to the resume"""
    return await resume_handler.analyze_resume(current_user, resume_id)


@cache(expire=60 * 5)
@router.get("/resume/{resume_id}/fix")
def fix_user_resume(current_user: Annotated[User, Depends(get_current_user)], resume_id: str,
                    scan_id: str | None = None):
    """ attempts to fix the issues in the resume using the feeback from the job scan"""
    # template_name = "jobby_mcjobface.docx"
    # file_path = os.path.join(os.getcwd(),  template_name)
    file_path = resume_handler.fix_resume(current_user, resume_id, scan_id)
    file_name = Path(file_path).name
    return FileResponse(path=file_path, filename=file_name, media_type='application/octet-stream')

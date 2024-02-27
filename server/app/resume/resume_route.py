from __future__ import annotations

import logging
from pathlib import Path
from typing import Annotated, Optional, List

from fastapi import APIRouter, Depends, HTTPException
from prisma.types import ResumeCreateInput
from starlette.responses import FileResponse

from app.dependencies import get_current_user
from app.resume import resume_service
from app.user import user_service
from app.models.common_models import Resume, User

router = APIRouter(
    tags=["resume"],
    dependencies=[Depends(get_current_user)],
)


@router.post("/resume", response_model=Resume)
async def create_resume(params: ResumeCreateInput, current_user: Annotated[User, Depends(get_current_user)]):
    """ creates a new resume called after uploading to bucket"""
    if current_user.resume_analysis_remaining <= 0:
        raise Exception("You have no resume analysis remaining")
    resume = await resume_service.create_new_resume(current_user, params)
    return resume


@router.get("/resumes", response_model=Optional[List[Resume]])
async def list_resume(current_user: Annotated[User, Depends(get_current_user)]):
    """ list all resumes for user """
    return resume_service.find_all_resumes(current_user)


@router.get("/resumes/{resume_id}", response_model=Optional[Resume])
async def find_resume(resume_id: str, current_user: Annotated[User, Depends(get_current_user)]):
    """ finds the resume by id """
    return resume_service.find_resume_by_id(current_user, resume_id)


@router.delete("/resume/{resume_id}", response_model=Resume)
async def delete_resume_by_id(resume_id: str, current_user: Annotated[User, Depends(get_current_user)]):
    await resume_service.delete_resume(current_user, resume_id)


@router.post("/resume/{resume_id}/analyze")
async def analyze_user_resume(resume_id: str, current_user: Annotated[User, Depends(get_current_user)]):
    """ analyzes a resume extracting fixes and suggestions, save the results to the resume"""
    return await resume_service.analyze_resume(current_user, resume_id)


@router.get("/resume/{resume_id}/fix")
def fix_user_resume(current_user: Annotated[User, Depends(get_current_user)], resume_id: str,
                    scan_id: str | None = None):
    """ attempts to fix the issues in the resume using the feeback from the job scan"""
    # template_name = "jobby_mcjobface.docx"
    # file_path = os.path.join(os.getcwd(),  template_name)
    file_path = resume_service.fix_resume(current_user, resume_id, scan_id)
    file_name = Path(file_path).name
    return FileResponse(path=file_path, filename=file_name, media_type='application/octet-stream')

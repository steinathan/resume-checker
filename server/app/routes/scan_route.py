from typing import Optional, List, Annotated

from fastapi import APIRouter, Depends

from app.resume import resume_service
from app.user import user_service

from app.dependencies import get_current_user
from app.resume.resume_service import JobScanResult, AnalyseJobForResumeParams
from app.models.common_models import AtsJobScan, User

router = APIRouter(
    tags=["scan"],
    dependencies=[Depends(get_current_user)],
)


@router.post("/job/scan", response_model=AtsJobScan)
async def at_scan_job(params: AnalyseJobForResumeParams, current_user: Annotated[User, Depends(get_current_user)]):
    """ scans a job against a resume """

    if current_user.scans_remaining <= 0:
        raise Exception("You have no scans remaining")

    scan = resume_service.process_ats_scan(current_user, params)

    # check the users plan and minus count
    if scan and current_user.plan == "free":
        current_user.scans_remaining -= 1
        await user_service.update_user_by_dict(current_user.id, {
            "scans_remaining": current_user.scans_remaining,
        })

    return scan


@router.get("/job/scans", response_model=Optional[List[AtsJobScan]])
async def get_job_scans(current_user: Annotated[User, Depends(get_current_user)]):
    """ lists all job scans for the user """
    return resume_service.list_job_scans_for_user(current_user)


@router.get("/job/scans/{scan_id}", response_model=Optional[JobScanResult])
async def find_job_scan(scan_id: str, current_user: Annotated[User, Depends(get_current_user)]):
    """ finds the resume by id """
    return resume_service.find_job_scan_by_id(current_user, scan_id)

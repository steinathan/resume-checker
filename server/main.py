import logging
from typing import Annotated, List, Optional

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse

from app.dependencies import get_current_user
from app.models.common_models import User, Resume, AtsJobScan
from app.supabase_client.client import supabase
from pathlib import Path

from app.handlers.resume_handler import CreateResumeParams, create_new_resume, find_all_resumes, process_ats_scan, \
    AnalyseJobForResumeParams, analyze_resume, find_resume_by_id, list_job_scans_for_user, find_job_scan_by_id, \
    JobScanResult

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[
        logging.FileHandler("resume_logger.log"),
        logging.StreamHandler()
    ]
)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/users/me", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@app.post("/resume", response_model=Resume)
async def create_resume(params: CreateResumeParams, current_user: Annotated[User, Depends(get_current_user)]):
    """ creates a new resume called after uploading to bucket"""
    resume = create_new_resume(current_user, params)
    await analyze_resume(current_user, resume.id)
    return find_resume_by_id(current_user, resume.id)


@app.post("/job/scan", response_model=AtsJobScan)
async def at_scan_job(params: AnalyseJobForResumeParams, current_user: Annotated[User, Depends(get_current_user)]):
    """ scans a job against a resume """
    return process_ats_scan(current_user, params)


@app.get("/job/scans", response_model=Optional[List[AtsJobScan]])
async def get_job_scans(current_user: Annotated[User, Depends(get_current_user)]):
    """ lists all job scans for the user """
    return list_job_scans_for_user(current_user)


@app.get("/resumes", response_model=Optional[List[Resume]])
async def list_resume(current_user: Annotated[User, Depends(get_current_user)]):
    """ list all resumes for user """
    return find_all_resumes(current_user)


@app.get("/resumes/{resume_id}", response_model=Optional[Resume])
async def find_resume(resume_id: str, current_user: Annotated[User, Depends(get_current_user)]):
    """ finds the resume by id """
    return find_resume_by_id(current_user, resume_id)


@app.get("/job/scans/{scan_id}", response_model=Optional[JobScanResult])
async def find_job_scan(scan_id: str, current_user: Annotated[User, Depends(get_current_user)]):
    """ finds the resume by id """
    return find_job_scan_by_id(current_user, scan_id)


@app.post("/get-token")
async def get_login_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    data = supabase.auth.sign_in_with_password({"email": form_data.username, "password": form_data.password})
    token, token_type = data.session.access_token, data.session.token_type
    return {"access_token": token, "token_type": token_type}


@app.post("/resume/{resume_id}/analyze")
async def analyze_user_resume(resume_id: str, current_user: Annotated[User, Depends(get_current_user)]):
    """ analyzes a resume extracting fixes and suggestions, save the results to the resume"""
    return await analyze_resume(current_user, resume_id)


app.mount("/", StaticFiles(directory="static", html=True), name="static")


@app.exception_handler(404)
async def redirect_all_requests_to_frontend(request: Request, exc: HTTPException):
    return HTMLResponse(open(Path(__file__).parent / "static/index.html").read())


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)

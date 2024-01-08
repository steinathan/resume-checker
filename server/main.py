from __future__ import annotations

import logging
import os

import sentry_sdk

from typing import Annotated, List, Optional

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse, FileResponse

from app.dependencies import get_current_user
from app.models.common_models import User, Resume, AtsJobScan
from app.supabase_client.client import supabase
from pathlib import Path
from api_analytics.fastapi import Analytics  # type: ignore

from app.handlers.resume_handler import CreateResumeParams, create_new_resume, find_all_resumes, process_ats_scan, \
    AnalyseJobForResumeParams, analyze_resume, find_resume_by_id, list_job_scans_for_user, find_job_scan_by_id, \
    JobScanResult, delete_resume, fix_resume

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[
        logging.FileHandler("resume_logger.log"),
        logging.StreamHandler()
    ]
)

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),
    traces_sample_rate=1.0,
    send_default_pii=True,
    profiles_sample_rate=1.0,
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
app.add_middleware(Analytics, api_key=os.environ.get("API_ANALYTICS_KEY") or "")


@app.get("/users/me", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@app.post("/resume", response_model=Resume)
async def create_resume(params: CreateResumeParams, current_user: Annotated[User, Depends(get_current_user)]):
    """ creates a new resume called after uploading to bucket"""
    resume = create_new_resume(current_user, params)
    try:
        await analyze_resume(current_user, resume.id)
        return find_resume_by_id(current_user, resume.id)
    except Exception as e:
        logging.error(e)
        await delete_resume(current_user, resume.id)
        raise HTTPException(status_code=500, detail="Error processing resume, kindly re-upload this resume")


@app.delete("/resume/{resume_id}", response_model=Resume)
async def delete_resume_by_id(resume_id: str, current_user: Annotated[User, Depends(get_current_user)]):
    await delete_resume(current_user, resume_id)


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


@app.get("/resume/{resume_id}/fix")
def fix_user_resume(current_user: Annotated[User, Depends(get_current_user)], resume_id: str,
                    scan_id: str | None = None):
    """ attempts to fix the issues in the resume using the feeback from the job scan"""
    # template_name = "jobby_mcjobface.docx"
    # file_path = os.path.join(os.getcwd(),  template_name)
    file_path = fix_resume(current_user, resume_id, scan_id)
    file_name = Path(file_path).name
    return FileResponse(path=file_path, filename=file_name, media_type='application/octet-stream')


@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0


@app.exception_handler(404)
async def redirect_all_requests_to_frontend(request: Request, exc: HTTPException):
    """ redirect all non-server routes to be served by the client """
    return HTMLResponse(open(Path(__file__).parent / "static/index.html").read())


app.mount("/", StaticFiles(directory="static", html=True), name="static")

log_config = uvicorn.config.LOGGING_CONFIG
log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
log_config["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)

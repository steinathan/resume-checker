import uuid

from app.handlers.resume_checkerv2 import ResumeAnalyser, AtsAnalyserResult
from app.handlers.resume_handler import create_cover_letter, create_scan_result
from app.models.common_models import User, Resume, CoverLetter

resume_path = "https://rbscckjjbznellmpzemf.supabase.co/storage/v1/object/public/ai-resume/d8cce208-7143-4eaa-9f51-7ee3c55630f4/The%20Sheets%20&%20Giggles.pdf"
job_url = "https://boards.greenhouse.io/remotecom/jobs/5789193003"


# analyzer = ResumeAnalyser(job_posting_url=job_url, resume_file_path=resume_path)
# result = analyzer.run_ats()


def gen_uuid():
    return str(uuid.uuid4())


user = User(username="pricop", id=gen_uuid())
resume = Resume(id=gen_uuid(), user_id=user.id, src="https:///test.com", name="dummy-resume")
analysis = AtsAnalyserResult(resume_content="xxxxxxx", job_url="https:///bool.com",
                             job_description="dummy descriptipn",
                             generated_cover_letter="i wish to apply here")

letter = CoverLetter(
    id=gen_uuid(),
    user_id=user.id,
    resume_id=resume.id,
    text="resume text that works",
    job_url="dummy url",
    job_description="dummy description"
)


def test_create_cover_letter():
    letter = create_cover_letter(user, resume, analysis)
    print(letter)


def test_create_scan_result():
    create_scan_result(analysis, user, resume, letter)


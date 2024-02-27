import uuid

from app.gpt_analyser.resume_checkerv2 import ResumeAnalyser, AtsAnalyserResult
from app.resume.resume_service import create_cover_letter, create_scan_result
from app.models.common_models import User, Resume, CoverLetter

resume_path = "https://rbscckjjbznellmpzemf.supabase.co/storage/v1/object/public/ai-resume/d8cce208-7143-4eaa-9f51-7ee3c55630f4/Resume%20-%20Navi.pdf"
job_url = "https://boards.greenhouse.io/remotecom/jobs/5789193003"


def test_resume_ats_analyser():
    analyzer = ResumeAnalyser(job_posting_url=job_url, resume_file_path=resume_path)
    result = analyzer.run_ats()
    print(result)


def test_analyse_resume():
    analyzer = ResumeAnalyser(job_posting_url=job_url, resume_file_path=resume_path)
    result = analyzer.analyse_resume()
    print(result)


def test_resume_revamper():
    analyzer = ResumeAnalyser(job_posting_url=job_url, resume_file_path=resume_path)
    issues = ["Lack of summary", "Incomplete address", "Incomplete education details", "Inconsistent date formatting"]
    suggestions = ["Include a brief summary highlighting key skills and experiences",
                   "Include full address including street, city, and zip code",
                   "Include the full name of the university, the location, and the degree obtained",
                   "Use consistent date formatting (Month Year - Month Year)",
                   "Add bullet points to list specific job responsibilities and achievements"]
    missing_skills = ['Online Writing', 'Coaching', 'Telecommuting', 'Microsoft Access', 'Planning', 'Problem Solving',
                      'Online Marketing', 'Performance Management', 'Data Science', 'Scheduling', 'Product Management',
                      'Creative Problem Solving', 'Project Management', 'Customer Support', 'Strategic Planning',
                      'Marketing', 'Medical Coding', 'Service Level', 'Workforce Management', 'Newsletters',
                      'Online Teaching', 'Process Improvement', 'Remote Infrastructure Management', 'Forecasting',
                      'Management', 'Sales', 'Writing', 'Business Process Outsourcing', 'Leadership',
                      'Employee Assistance Programs', 'Operations', 'Customer Service', 'Disabilities', 'Editing',
                      'Teaching', 'Data Entry', 'Mental Health', 'Nursing', 'Social Media', 'Web Conferencing',
                      'Capacity Planning', 'Accounting', 'Dashboard']
    result = analyzer.revamp_resume(issues=issues, suggestions=suggestions, skills=missing_skills)
    print(result)


test_resume_revamper()


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

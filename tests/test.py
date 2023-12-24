from resume_checker import ResumeAnalyser

resume_path = "../resumes/main.pdf"
job_url = "https://boards.greenhouse.io/remotecom/jobs/5789193003"
analyzer = ResumeAnalyser(job_posting_url=job_url, resume_path=resume_path)
analyzer.run()

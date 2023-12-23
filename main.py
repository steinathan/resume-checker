#!/usr/bin/python3

import click
from resume_checker import ResumeAnalyser


@click.command()
@click.option('--resume', help='Path to the resume file', default="./resumes/main.pdf")
@click.option('--job-url', help='URL of the job posting', required=True)
def cli_entry_point(resume, job_url):
    """
    CLI entry point for the Resume Analyser tool.
    """
    analyzer = ResumeAnalyser(job_posting_url=job_url, resume_path=resume)
    analyzer.run()


if __name__ == "__main__":
    cli_entry_point()
    # resume_path = "./resumes/main.pdf"
    # job_url = "https://boards.greenhouse.io/remotecom/jobs/5789193003"
    # analyzer = ResumeAnalyser(job_posting_url=job_url, resume_path=resume_path)
    # analyzer.run()

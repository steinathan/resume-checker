from app.models.common_models import ResumeLLMAnalysis

analysis_dump = {
    "contact_info": {
        "issues": [
            "missing email address"
        ],
        "improvements": [
            "add email address to contact info section"
        ],
        "done": [
            "provided phone number"
        ],
        "score": 6.5
    },
    "education": {
        "issues": [
            "inconsistent date formatting"
        ],
        "improvements": [
            "standardize date format"
        ],
        "done": [
            "added education section"
        ],
        "score": 7
    },
    "experience": {
        "issues": [
            "inconsistent date formatting",
            "incomplete job descriptions"
        ],
        "improvements": [
            "standardize date format",
            "expand on job responsibilities"
        ],
        "done": [
            "added work experience section"
        ],
        "score": 6
    },
    "skills": {
        "issues": [],
        "improvements": [],
        "done": [
            "added skills section"
        ],
        "score": 8
    },
    "summary": {
        "issues": [
            "missing summary"
        ],
        "improvements": [
            "add a summary to highlight key achievements and skills"
        ],
        "done": [],
        "score": 5
    },
    "personal_projects": {
        "issues": [
            "inconsistent date formatting"
        ],
        "improvements": [
            "standardize date format"
        ],
        "done": [],
        "score": 7
    },
    "date_formatting": {
        "issues": [
            "inconsistent date formatting"
        ],
        "improvements": [
            "standardize date format"
        ],
        "done": [],
        "score": 6
    },
    "section_headings": {
        "issues": [
            "section headings are not clearly defined"
        ],
        "improvements": [
            "use standard section headings, e.g. 'Work Experience', 'Education', 'Skills', etc."
        ],
        "done": [],
        "score": 5.5
    }
}
text = ResumeLLMAnalysis(**analysis_dump)
print("total_score", text.total_score)
print("section_count", text.sections_count)

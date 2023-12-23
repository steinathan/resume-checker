## Resume Analyser

A Python tool for analyzing the fit between a resume and a job posting, assigns a score then generates a cover letter automatically, runs with local models (ollama) or openai

## Overview

Resume Analyser is a command-line tool designed for evaluating how well a given resume aligns with a specific job
posting. The tool utilizes advanced language models for understanding and comparing textual content, providing a score
and detailed feedback.

## Features

- **Language Models:** Integrates with OpenAI's GPT-3.5 Turbo and Ollama for natural language processing.
- **Resume Parsing:** Extracts text content from PDF resumes for analysis.
- **Job Site Scraping:** Fetches job description content from specified URLs.
- **Scoring System:** Generates a score indicating the fit between the resume and job description.
- **Cover Letter Generation:** Automatically generates a cover letter if the fit is positive.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- [Poetry](https://python-poetry.org/) (To install, follow
  the [official instructions](https://python-poetry.org/docs/#installation))
- Required Python packages (install using `poetry install`)

## Usage

First, install ollama here https://github.com/jmorganca/ollama

```shell
$ curl https://ollama.ai/install.sh | sh
$ ollama pull mistral
```

1. Clone the repository:

```bash
git clone https://github.com/navicstein/resume-checker.git
cd resume-checker
```

2. Install dependencies using Poetry:

```bash
poetry install
```

3. Set up environment variables:
Create a .env file with the following content:
```dotenv
OPENAI_API_KEY=xxxxxxxx
LLM_MODEL=openai  # or ollama
```

4. Place your resume(s) in the `resumes` directory.

Run the tool:
```shell
python main.py --job-url="https://xxxxxxx" --resume="./path/to/resume.pdf"
```


## TODOS
- Scrape and find jobs automatically 
- Auto apply for jobs if applicable after confirmation
FROM python:3.11

WORKDIR /app

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -

COPY pyproject.toml poetry.lock* /app/

RUN #poetry install --no-root
RUN pipx install poetry
ENV PATH="$PATH:$POETRY_HOME/bin"

COPY . /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

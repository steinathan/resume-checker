# Stage 1: Build frontend
FROM node:14 AS frontend-builder

WORKDIR /app

COPY frontend/package.json frontend/yarn.lock /app/
RUN yarn
ENV NODE_ENV=production
COPY frontend /app

RUN yarn build

# Stage 2: Build server
FROM python:3.11 as backend-builder

WORKDIR /app

COPY server/pyproject.toml poetry.lock* /app/
RUN ls
COPY server/.env /app/

RUN pip install poetry
RUN poetry config virtualenvs.create false
ENV PATH="$PATH:$POETRY_HOME/bin"
RUN poetry install --no-root

COPY server /app

COPY --from=frontend-builder /app/dist /app/server/static

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

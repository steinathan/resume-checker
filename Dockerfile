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

WORKDIR /project

COPY server /project

RUN pip install poetry
RUN poetry config virtualenvs.create false
ENV PATH="$PATH:$POETRY_HOME/bin"
RUN poetry install --no-root

COPY server /project

COPY --from=frontend-builder /app/dist /project/static
RUN ls -la /project/static
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

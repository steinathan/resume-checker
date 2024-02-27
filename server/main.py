from __future__ import annotations

import logging
import os
from pathlib import Path

import sentry_sdk
import uvicorn
from api_analytics.fastapi import Analytics  # type: ignore
from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from prisma.enums import Provider
from starlette.responses import HTMLResponse
from prisma import Prisma
from app.routes import scan_route, stripe_route  # type: ignore
from app.resume import resume_route
from app.user import user_route

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[
        logging.FileHandler("resume_logger.log"),
        logging.StreamHandler()
    ]
)

if os.environ.get("ENV") == "production":
    print("initialized sentry")
    sentry_sdk.init(
        dsn=os.environ.get("SENTRY_DSN"),
        traces_sample_rate=1.0,
        send_default_pii=True,
        profiles_sample_rate=1.0,
    )

app = FastAPI()

prefix = "/api"
app.include_router(user_route.router, prefix=prefix)
app.include_router(resume_route.router, prefix=prefix)
app.include_router(scan_route.router, prefix=prefix)
app.include_router(stripe_route.router, prefix=prefix)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(Analytics, api_key=os.environ.get("API_ANALYTICS_KEY") or "")


@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0


@app.exception_handler(404)
async def redirect_all_requests_to_frontend(request: Request, exc: HTTPException):
    """ redirect all non-server routes to be served by the client """
    try:
        return HTMLResponse(open(Path(__file__).parent / "static/index.html").read())
    except FileNotFoundError:
        pass


app.mount("/", StaticFiles(directory="static", html=True), name="static")

log_config = uvicorn.config.LOGGING_CONFIG
log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
log_config["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"


@app.on_event("startup")
async def startup():
    db = Prisma(auto_register=True, log_queries=True)
    await db.connect()

    # await db.user.create(data={
    #     "email": "admin@gmail.com",
    #     "password": "123456",
    #     "name": "admin",
    #     "username": "admin123",
    #     "provider": Provider.email
    # })
    print("[startup] app started successfully")
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)

from __future__ import annotations
from datetime import datetime
from uuid import uuid4, UUID

from pydantic import BaseModel


class AllBaseModel(BaseModel):
    id: str | None = None
    # adding iso format for supabase purposes
    created_at: str = datetime.now().isoformat()
    updated_at: str = datetime.now().isoformat()


class User(AllBaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = False


class Resume(AllBaseModel):
    user_id: str
    src: str
    name: str
    text: str | None = None


class CoverLetter(AllBaseModel):
    user_id: str
    resume_id: str
    job_url: str | None = None
    job_description: str | None = None

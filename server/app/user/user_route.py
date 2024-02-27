from __future__ import annotations

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from prisma.models import User
from pydantic import BaseModel

from app.dependencies import get_current_user
from app.user import user_service
# from app.models.common_models import User
from app.supabase_client.client import supabase
from typing import Annotated

router = APIRouter(
    tags=["auth"],
    prefix="/auth"
)


class UserRegisterInput(BaseModel):
    id: str | None = None
    email: str
    name: str
    password: str
    username: str


class UserLoginInput(BaseModel):
    identifier: str
    password: str


@router.get("/me")
async def get_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@router.get("/providers")
async def get_providers():
    return ["email"]


@router.post("/register")
async def register(params: UserRegisterInput):
    # create user is auth
    data = supabase.auth.sign_up({
        "email": params.email,
        "password": params.password,
    })
    # add to table
    params.id = data.user.id
    user = await user_service.create_user(params)
    return user


@router.post("/login")
async def login(params: UserLoginInput):
    # create user is auth
    data = supabase.auth.sign_in_with_password({"email": params.identifier, "password": params.password})
    token, token_type = data.session.access_token, data.session.token_type
    user = await user_service.find_user_by_id(data.user.id)
    return {"access_token": token, "token_type": token_type, "user": user}


@router.post("/get-token")
async def get_login_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    data = supabase.auth.sign_in_with_password({"email": form_data.username, "password": form_data.password})
    token, token_type = data.session.access_token, data.session.token_type
    return {"access_token": token, "token_type": token_type}


@router.get("/verify-jwt", response_model=User)
async def verify_user(jwt: str):
    return user_service.upsert_user_by_jwt(jwt)

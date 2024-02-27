from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from prisma.models import User

from app.dependencies import get_current_user
from app.user import user_service
# from app.models.common_models import User
from app.supabase_client.client import supabase
from typing import Annotated

router = APIRouter(
    tags=["users"]
)


@router.get("/users/me", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@router.post("/get-token")
async def get_login_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    data = supabase.auth.sign_in_with_password({"email": form_data.username, "password": form_data.password})
    token, token_type = data.session.access_token, data.session.token_type
    return {"access_token": token, "token_type": token_type}


@router.get("/user/verify", response_model=User)
async def verify_user(jwt: str):
    return user_service.upsert_user_by_jwt(jwt)

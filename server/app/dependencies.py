from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi_cache.decorator import cache

from app.handlers import user_handler
from app.handlers.user_handler import upsert_user_by_jwt
from app.models.common_models import User
from app.supabase_client.client import supabase

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="get-token")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    user = upsert_user_by_jwt(token)
    if user:
        return user
    else:
        data = supabase.auth.get_user(token)
        user = data.user
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user_handler.find_user_by_id(user.id)

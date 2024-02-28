from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.user import user_service
from app.models.common_models import User
from app.supabase_client.client import supabase

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="get-token")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    data = supabase.auth.get_user(token)
    if data.user:
        return await user_service.find_user_by_id(data.user.id)
    else:
        data = supabase.auth.get_user(token)
        user = data.user
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return await user_service.find_user_by_id(user.id)

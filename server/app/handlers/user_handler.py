from __future__ import annotations

from app.models.common_models import User
from app.supabase_client.client import supabase

USERS_TABLE = "users"


def find_user_by_id(user_id: str) -> User | None:
    response = (supabase.table(USERS_TABLE)
                .select("*")
                .eq("id", user_id).execute()
                )
    if response.data:
        return User(**response.data[0])
    return None


def upsert_user_by_jwt(jwt: str) -> User | None:
    """ this function is called everytime a user `mounts` a page in the client"""
    data = supabase.auth.get_user(jwt)
    if data.user:
        jwt_user = data.user
        supabase.table(USERS_TABLE).upsert({
            "id": jwt_user.id,
            "email_address": jwt_user.email,
            "full_name": jwt_user.user_metadata.get("full_name") or jwt_user.user_metadata.get("name")
        }).execute()
        return find_user_by_id(jwt_user.id)
    return None


def upsert_user(user: User) -> User:
    (supabase.table(USERS_TABLE).upsert(user.model_dump()).execute())
    return user


def update_user(user: User) -> User | None:
    upsert_user(user)
    return user

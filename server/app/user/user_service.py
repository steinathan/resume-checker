from __future__ import annotations

from gotrue import AuthResponse
from prisma.enums import Provider
from prisma.models import User
from random_username.generate import generate_username

# from app.models.common_models import User
from app.supabase_client.client import supabase
from app.user.user_route import UserRegisterInput

USERS_TABLE = "users"


async def find_user_by_id(user_id: str) -> User | None:
    return await User.prisma().find_first(where={"id": user_id})


async def upsert_user_by_jwt(jwt: str) -> User | None:
    """ this function is called everytime a user `mounts` a page in the client"""
    data = supabase.auth.get_user(jwt)
    if data.user:
        auth_user = data.user
        name = auth_user.user_metadata.get("full_name") or auth_user.user_metadata.get("name")
        user = await User.prisma().upsert(
            where={
                'id': auth_user.id,
            },
            data={
                'create': {
                    "username": generate_username(5),
                    "email": auth_user.email,
                    "provider": Provider.email,
                    "name": name
                },
                'update': {
                    'email': auth_user.email,
                    "name": name
                },
            }
        )
        return user
    return None


def upsert_user(user: User) -> User:
    (supabase.table(USERS_TABLE).upsert(user.model_dump()).execute())
    return user


def update_user(user: User) -> User | None:
    upsert_user(user)
    return user


async def update_user_by_dict(id: str, user_dict: dict) -> None:
    """ updates the user by dict, performs partial update """
    (supabase.table(USERS_TABLE).update(user_dict)
     .eq('id', id).execute())


async def create_user(inputs):
    """ creates a user """
    return await User.prisma().create(data={
        "id": inputs.id,
        "username": inputs.username,
        "email": inputs.email,
        "provider": Provider.email,
        "name": inputs.name
    })

from __future__ import annotations

from app.models.common_models import User
from app.supabase_client.client import supabase

USERS_TABLE = "users"


def find_user_by_id(user_id: str) -> User | None:
    user = supabase.auth.get_user()
    print(user)
    # response = (supabase.table(USERS_TABLE)
    #             .select("*")
    #             .eq("id", user_id).execute()
    #             )
    # if response.data:
    #     return User(**response.data[0])
    return None


print(find_user_by_id("d8cce208-7143-4eaa-9f51-7ee3c55630f4"))
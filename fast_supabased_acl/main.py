import os
from typing import Annotated, List
from supabase import create_client, Client
from gotrue.errors import AuthApiError
from fastapi import Depends, HTTPException, Header

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

async def token_auth(token: str):
    if not token:
        raise HTTPException(status_code=400, detail="Token header required")

    try:
        user = supabase.auth.get_user(token)
    except AuthApiError as e:
        raise HTTPException(status_code=401, detail="Invalid token")

    return user


class FastSupabasedACL:
    def __init__(self, role: List[str] = ["authenticated"]):
        self.role = role

    def __call__(self, user = Depends(token_auth)):
        if self.role != user.user.role:
            raise HTTPException(status_code=403, detail="Unauthorized")

        return user
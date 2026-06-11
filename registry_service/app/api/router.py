from typing import Annotated

from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from app.dependencies import get_user_repo

router = APIRouter()

UserRepo = Annotated[UserRepository, Depends(get_user_repo)]

@router.get("/users")
async def get_users(user_repo: UserRepo) -> list[str]:
    users = user_repo.list()

    return users
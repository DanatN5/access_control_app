from typing import Annotated

from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from app.dependencies import get_user_repo
from app.schemas import UserBase

router = APIRouter()

UserRepo = Annotated[UserRepository, Depends(get_user_repo)]

@router.get("/users")
async def get_users(user_repo: UserRepo) -> list[str]:
    users = user_repo.list()

    return users

@router.get("/users/{user_id}")
async def get_user_by_id(
    user_repo: UserRepo,
    user_id: int
) -> UserBase:
    return user_repo.get(user_id)

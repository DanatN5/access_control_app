from app.database import AsyncSessionLocal
from collections.abc import AsyncGenerator
from typing import Annotated
from fastapi import Query, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.UnitOfWork import UnitOfWork
from app.services.user_service import UserService


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

async def get_uow(
        session: Annotated[AsyncSession, Depends(get_session)]
) -> AsyncGenerator[UnitOfWork, None]:
    async with UnitOfWork(session) as uow:
        yield uow

async def get_user_service(
        uow: Annotated[UnitOfWork, Depends(get_uow)]
) -> UserService:
    return UserService(uow)
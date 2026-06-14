from app.database import AsyncSessionLocal
from collections.abc import AsyncGenerator, Callable
from typing import Annotated, Type, TypeVar
from fastapi import Query, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.uow import SQLAlchemyUnitOfWork, UnitOfWork
from app.repositories.repository_protocol import SQLAlchemyRepo
# from app.repositories.user_repository import UserSQLAlchemyRepo
# from app.repositories.group_repository import GroupSQLAlchemyRepo
# from app.repositories.access_repository import AccessSQLAlchemyRepo
# from app.services.user_service import UserService
# from app.services.group_service import GroupService


S = TypeVar("S")
R = TypeVar("R")

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

async def get_uow(
        session: Annotated[AsyncSession, Depends(get_session)]
) -> AsyncGenerator[UnitOfWork, None]:
    async with SQLAlchemyUnitOfWork(session) as uow:
        yield uow


def get_service(service: Type[S]) -> Callable:

    async def dependency(
            uow: Annotated[UnitOfWork, Depends(get_uow)]
            )-> S:
        return service(uow)
    
    return dependency

def get_repo(repository: Type[R]) -> Callable:
    
    async def dependency(
            session: Annotated[AsyncSession, Depends(get_session)]
    ) -> R:
        return repository(session)
    
    return dependency


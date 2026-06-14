from typing import Annotated

from fastapi import Depends, APIRouter
from app.repositories.user_repository import UserRepository
from app.repositories.user_repository import UserSQLAlchemyRepo
from app.services.user_service import UserService
from app.dependencies import get_repo, get_service
from app.schemas.user_schemas import UserCreate, UserRead
from app.schemas.group_schemas import GroupRead
from app.schemas.access_schemas import AccessRead

users = APIRouter()

UserRepoDependency = Annotated[UserRepository, Depends(get_repo(UserSQLAlchemyRepo))]
UserServiceDependency = Annotated[UserService, Depends(get_service(UserService))]

@users.get("/users")
async def get_users(user_repo: UserRepoDependency) -> list[UserRead]:
    users = await user_repo.list(eager=True)

    return users

@users.get("/users/{user_id}")
async def get_user_by_id(
    user_repo: UserRepoDependency,
    user_id: int
) -> UserRead:
    return await user_repo.get(user_id, eager=True)

@users.get("/users/{user_id}/group")
async def get_user_group(
    user_id: int,
    user_service: UserServiceDependency
) -> GroupRead:
    return await user_service.get_group(user_id)

@users.get("/users/{user_id}/accesses")
async def get_user_accesses(
    user_id: int,
    user_service: UserServiceDependency
) -> list[AccessRead]:
    return await user_service.get_accesses(user_id) 

@users.post("/users")
async def create_user(
    user: UserCreate,
    user_service: UserServiceDependency
) -> UserRead:
    return await user_service.create(user)

from typing import Annotated

from fastapi import Depends, APIRouter
from app.repositories.group_repository import GroupRepository
from app.repositories.group_repository import GroupSQLAlchemyRepo
from app.services.group_service import GroupService
from app.dependencies import get_repo, get_service
from app.schemas.user_schemas import UserCreate, UserRead
from app.schemas.group_schemas import GroupRead, GroupCreate
from app.schemas.access_schemas import AccessRead

groups = APIRouter()

GroupRepoDependency = Annotated[GroupRepository, Depends(get_repo(GroupSQLAlchemyRepo))]
GroupServiceDependency = Annotated[GroupService, Depends(get_service(GroupService))]

@groups.post("/groups")
async def create_group(
    group_service: GroupServiceDependency,
    group: GroupCreate
) -> GroupRead:
    return await group_service.create_group(group)

@groups.get("/groups")
async def get_groups_list(
    group_repo: GroupRepoDependency
) -> list[GroupRead]:
    return await group_repo.list(eager=True)
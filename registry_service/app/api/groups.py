from typing import Annotated

from fastapi import Depends, APIRouter
from app.repositories.group_repository import GroupRepository
from app.repositories.group_repository import GroupSQLAlchemyRepo
from app.services.group_service import GroupService
from app.dependencies import get_repo, get_service
from app.schemas.group_schemas import GroupRead, GroupCreate

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

@groups.get("/groups/{group_id}")
async def get_user_by_id(
    group_repo: GroupRepoDependency,
    group_id: int
) -> GroupRead:
    return await group_repo.get(group_id, eager=True)
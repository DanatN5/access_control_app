from typing import Annotated

from fastapi import Depends, APIRouter
from app.repositories.access_repository import AccessRepository, AccessSQLAlchemyRepo
from app.services.access_service import AccessService
from app.dependencies import get_repo, get_service
from app.schemas.user_schemas import UserCreate, UserRead
from app.schemas.group_schemas import GroupRead, GroupCreate
from app.schemas.access_schemas import AccessRead, AccessCreate

accesses = APIRouter()

AccessRepoDependency = Annotated[AccessRepository, Depends(get_repo(AccessSQLAlchemyRepo))]
AccessServiceDependency = Annotated[AccessService, Depends(get_service(AccessService))]

@accesses.post("/accesses")
async def create_access(
    access_service: AccessServiceDependency,
    access: AccessCreate
) -> AccessRead:
    return await access_service.create_access(access)


@accesses.get("/accesses")
async def get_accesses_list(
    accesses_repo: AccessRepoDependency
) -> list[AccessRead]:
    return await accesses_repo.list()
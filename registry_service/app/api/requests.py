from fastapi import APIRouter, Depends
from typing import Annotated
from app.dependencies import get_repo, get_service
from app.schemas.request_schemas import ValidatedRequest, RequestRead, RequestReadShort, RequestCreate
from app.repositories.request_repository import RequestRepository, RequestSQLAlchemyRepo
from app.services.request_service import RequestService


RequestRepoDependency = Annotated[RequestRepository, Depends(get_repo(RequestSQLAlchemyRepo))]
RequestServiceDependency = Annotated[RequestService, Depends(get_service(RequestService))]

requests = APIRouter()

@requests.post("/requests")
async def create_request(
    request: RequestCreate,
    request_service: RequestServiceDependency
) -> RequestRead:
    return await request_service._create(request)


@requests.get("/requests")
async def get_requests(request_repo: RequestRepoDependency) -> list[RequestReadShort]:
    return await request_repo.list()


@requests.get("/requests/{request_id}")
async def get_request_by_id(
    request_id: int,
    request_repo: RequestRepoDependency
) -> RequestRead:
    return await request_repo.get(request_id)


@requests.patch("/requests/{request_id}")
async def process_request(
    request_id: int,
    request: ValidatedRequest,
    request_service: RequestServiceDependency,
) -> None:
    await request_service.process_request(request)

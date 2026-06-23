from fastapi import APIRouter, Depends
from typing import Annotated
from app.schemas.request_schemas import RequestCreate
from app.dependencies import get_broker, get_client, get_publish_service
from app.client import HttpClient
from app.messaging.broker import Broker
from app.services.publish_service import PublishService


publish = APIRouter()

ClientDependency = Annotated[HttpClient, Depends(get_client)]
BrokerDependency = Annotated[Broker, Depends(get_broker)]
ServiceDependency = Annotated[PublishService, Depends(get_publish_service)]

@publish.post("/publish")
async def publish_request(
    request: RequestCreate,
    service: ServiceDependency,
) -> None:
    await service.publish(request)
    

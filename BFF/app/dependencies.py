from app.messaging.broker import Broker, FaststreamBroker
from app.services.publish_service import PublishService
from app.messaging.fs_broker import broker
from app.client import HttpClient, HttpxClient
from typing import AsyncGenerator, Annotated
from fastapi import Depends

import httpx

ClientDependency = Annotated[HttpClient, Depends(get_client)]
BrokerDependency = Annotated[Broker, Depends(get_broker)]

async def get_client() -> AsyncGenerator[HttpClient, None]:
    async with httpx.AsyncClient() as client:
        yield HttpxClient(client)
    


async def get_broker() -> Broker:
    return FaststreamBroker(broker)


async def get_publish_service(
        client: ClientDependency,
        broker: BrokerDependency
) -> PublishService:
    return PublishService(client, broker)

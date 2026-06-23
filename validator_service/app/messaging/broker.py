import httpx
from faststream.rabbit import RabbitBroker
from app.messaging.schemas import Request
from app.application.service import ValidationService
from app.application.request_handler import RequestHandler
from app.infrastructure.client import HttpxClient
from app.config import settings


broker = RabbitBroker(str(settings.broker.url),reconnect_interval=5.0)

local = "amqp://guest:guest@rabbitmq:5672/"

client_url = ""

@broker.subscriber(str(settings.broker.queue))
async def proccess_request(
    request: Request
) -> None:
    async with httpx.AsyncClient() as client:
        httpx_client = HttpxClient(client)
        validator = ValidationService(httpx_client)
        handler = RequestHandler(httpx_client, validator)
        
        await handler.handle(request)




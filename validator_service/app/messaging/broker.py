import httpx
from faststream.rabbit import RabbitBroker
from app.messaging.schemas import Request
from app.application.service import ValidationService
from validator_service.app.infrastructure.managers import RegistryCLient
from app.application.request_handler import RequestHandler


broker = RabbitBroker("amqp://guest:guest@localhost:5672/")

client_url = ""

@broker.subscriber("requests")
async def proccess_request(
    request: Request
) -> None:
    async with httpx.AsyncClient() as client:
        validator = ValidationService(client)
        handler = RequestHandler(client, validator)
        
        await handler.handle(request)




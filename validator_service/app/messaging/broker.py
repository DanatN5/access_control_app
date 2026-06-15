from faststream.rabbit import RabbitBroker
from app.messaging.schemas import Request
from app.application.service import ValidationService
from app.infrastructure.clients import RegistryCLient


broker = RabbitBroker("amqp://guest:guest@localhost:5672/")

client_url = ""

@broker.subscriber("requests")
async def proccess_request(
    request: Request
) -> None:
    service = ValidationService(RegistryCLient(client_url))

    user_id = request.user_id
    target_ids = request.target_ids

    if request.action == "grant_access":
        service.grant_access(user_id, target_ids)
    elif request.action == "revoke_access":
        service.revoke_access(user_id, target_ids)
    elif request.action == "reset_group":
        service.reset_group(user_id, target_ids[0])
    else:
        service.unset_group(user_id, target_ids[0])



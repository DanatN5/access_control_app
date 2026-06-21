from app.client import HttpxClient
from app.messaging.broker import FaststreamBroker
from app.schemas import RequestCreate
from app.config import settings

class PublishService:
    def __init__(self, client: HttpxClient, broker: FaststreamBroker):
        self.client = client
        self.broker = broker

    async def publish(self, request: RequestCreate) -> None:
        await self.client.send(settings.request_url, request)
        await self.broker.publish(request, settings.broker.queue)
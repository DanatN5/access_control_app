from app.client import HttpxClient
from app.messaging.broker import FaststreamBroker
from app.schemas import RequestCreate
from app.config import settings

class PublishService:
    def __init__(self, broker: FaststreamBroker):

        self.broker = broker

    async def publish(self, request: RequestCreate) -> None:
        await self.broker.publish(request, str(settings.broker.queue))
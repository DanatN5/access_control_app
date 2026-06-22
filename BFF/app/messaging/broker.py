from faststream.rabbit import RabbitBroker
from typing import Protocol


class Broker(Protocol):
    async def publish(self, msg: str, queue: str) -> None: pass


class FaststreamBroker:
    def __init__(self, broker: RabbitBroker):
        self.broker = broker

    async def publish(self, msg: str, queue: str) -> None:
        await self.broker.publish(msg.model_dump(mode="json"), queue)






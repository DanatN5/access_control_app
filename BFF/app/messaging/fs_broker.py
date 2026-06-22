from faststream.rabbit import RabbitBroker
from app.config import settings

broker = RabbitBroker(str(settings.broker.url))

local = "amqp://guest:guest@localhost:5672/"
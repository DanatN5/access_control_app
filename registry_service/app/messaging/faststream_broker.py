from faststream.rabbit import RabbitBroker
from faststream import FastStream
from app.config import settings
from app.messaging.consumer import router

broker = RabbitBroker(str(settings.broker.url))

broker.include_router(router)

app = FastStream(broker)


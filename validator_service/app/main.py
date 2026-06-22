from faststream import FastStream
from app.messaging.broker import broker

app = FastStream(broker)
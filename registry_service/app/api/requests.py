from fastapi import APIRouter
from app.schemas.request_schemas import RequestValidatedEvent

request = APIRouter()

@request.post("/requests")
async def create_request(request: RequestValidatedEvent):
    pass
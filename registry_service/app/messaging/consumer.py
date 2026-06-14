from faststream.rabbit import RabbitRouter
from app.config import settings
from app.messaging.schemas import RequestMessage
from app.database import AsyncSessionLocal
from app.repositories.uow import SQLAlchemyUnitOfWork
from app.services.user_service import UserService
from app.repositories.request_repository import RequestSQLAlchemyRepo

router = RabbitRouter()
validated_request_queue = settings.broker.queue

@router.subscriber(validated_request_queue)
async def process_request(
    request: RequestMessage
) -> None:
    async with AsyncSessionLocal() as session:
        async with SQLAlchemyUnitOfWork(session) as uow:
            service = UserService(uow)
            repo = RequestSQLAlchemyRepo(session)
            if not request.validated:
                repo.update
                return
            elif request.action == "grant":
                service.grant(request.values)
            else:
                service.revoke(request.values)
            repo.update

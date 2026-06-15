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
            
            user_id = request.user_id
            target_ids = request.target_ids

            if request.action == "grant_access":
                service.grant_access(user_id, target_ids)
            elif request.action == "revoke_access":
                service.revoke_access(user_id, target_ids)
            elif request.action == "reset_group":
                service.reset_group(user_id, target_ids)
            else:
                service.unset_group(user_id, target_ids)

            repo.update

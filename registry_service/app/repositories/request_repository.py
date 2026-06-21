from typing import Protocol
from app.repositories.repository_protocol import Repository, SQLAlchemyRepo
from app.models import Request


class RequestRepository(Repository["Request", int], Protocol):
    pass
    

class RequestSQLAlchemyRepo(SQLAlchemyRepo):
    model = Request
    name = "Request"

    async def update_request(
            self, id: int,
            status: str,
            errors: list[str] | None = None
        ):
        
        request = self.session.get(self.model, id)
        if request:
            request.status = status
            if errors:
                request.errors = errors




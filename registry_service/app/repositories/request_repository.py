from typing import Protocol
from app.repositories.repository_protocol import Repository, SQLAlchemyRepo
from app.models import Request


class RequestRepository(Repository["Request", int], Protocol):
    pass
    

class RequestSQLAlchemyRepo(SQLAlchemyRepo):
    model = Request
    name = "Request"

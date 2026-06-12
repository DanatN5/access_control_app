from sqlalchemy import Table, Column, ForeignKey
from app.database import Base


user_accesses = Table(
    "user_accesses",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("access_id", ForeignKey("accesses.id"), primary_key=True)
)

    
group_access = Table(
    "group_access",
    Base.metadata,
    Column("group_id", ForeignKey("groups.id"), primary_key=True),
    Column("access_id", ForeignKey("accesses.id"), primary_key=True)
)
group_forbidden_access = Table(
    "group_forbidden_access",
    Base.metadata,
    Column("group_id", ForeignKey("groups.id"), primary_key=True),
    Column("access_id", ForeignKey("accesses.id"), primary_key=True)
)
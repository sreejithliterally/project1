from database import Base
from sqlalchemy.sql.expression import null, text
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from pydantic import BaseModel


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable = False)
    email = Column(String, nullable = False, unique=True)
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class UserInput(BaseModel):
    weight: float
    height: float
    goal: str
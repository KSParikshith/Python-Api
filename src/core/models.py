from sqlalchemy import Column, String, DateTime, func
import uuid
from .db import Base


class User(Base):
    __tablename__ = "users"

    # use a string column and default to a uuid4 string
    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(128), nullable=False)
    email = Column(String(256), unique=True, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

from uuid import UUID
from pydantic import BaseModel, EmailStr
from typing import Optional, Union
from datetime import datetime


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserRead(BaseModel):
    id: Union[UUID, str]  # accept uuid.UUID or plain string
    name: str
    email: EmailStr
    created_at: Optional[datetime]

    class Config:
        orm_mode = True

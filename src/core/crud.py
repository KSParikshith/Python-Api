import uuid
from typing import Union
from uuid import UUID
from sqlalchemy.orm import Session
from . import models, schemas


def _id_to_str(value: Union[str, UUID]) -> str:
    return str(value) if value is not None else None


def get_user(db: Session, user_id: Union[str, UUID]):
    user_id_str = _id_to_str(user_id)
    return db.query(models.User).filter(models.User.id == user_id_str).first()


def getAll_users(db: Session):   
    return db.query(models.User).all()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    # allow the model's default to generate the UUID string; keep explicit
    # id generation here if you prefer to control the value:
    # db_user = models.User(id=str(uuid.uuid4()), name=user.name, email=user.email)
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

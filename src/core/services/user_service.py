from typing import Union
from uuid import UUID
from sqlalchemy.orm import Session

from .. import crud, schemas


def create_user(db: Session, user: schemas.UserCreate):
    existing = crud.get_user_by_email(db, user.email)
    if existing:
        raise ValueError("Email already registered")
    return crud.create_user(db, user)


def get_user(db: Session, user_id: Union[str, UUID]):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise LookupError("User not found")
    return db_user


def get_all_users(db: Session):
    return crud.getAll_users(db)

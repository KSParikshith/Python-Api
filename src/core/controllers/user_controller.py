from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import schemas
from ..db import get_db
from ..services import user_service

router = APIRouter(prefix="", tags=["users"])


@router.post("/users/", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        return user_service.create_user(db, user)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.get("/users/{user_id}", response_model=schemas.UserRead)
def read_user(user_id: UUID, db: Session = Depends(get_db)):
    try:
        return user_service.get_user(db, user_id)
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


@router.get("/getAll-users/", response_model=list[schemas.UserRead])
def read_all_users(db: Session = Depends(get_db)):
    users = user_service.get_all_users(db)
    if not users:
        raise HTTPException(status_code=404, detail="Users not found")
    return users

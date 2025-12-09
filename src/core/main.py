from uuid import UUID
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import String, Uuid
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .db import engine, get_db

#models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Core Service")


@app.post("/users/", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)


@app.get("/users/{user_id}", response_model=schemas.UserRead)
def read_user(user_id: UUID, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/getAll-users/", response_model=list[schemas.UserRead])
def read_user(db: Session = Depends(get_db)):
    db_user = crud.getAll_users(db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Users not found")
    return db_user

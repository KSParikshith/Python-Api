import os
import tempfile
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import pytest

from src.core import models, crud, schemas


def setup_in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    models.Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal


def test_create_and_get_user():
    SessionLocal = setup_in_memory_db()
    db = SessionLocal()
    user_in = schemas.UserCreate(name="Alice", email="alice@example.com")
    user = crud.create_user(db, user_in)
    assert user.id is not None
    fetched = crud.get_user(db, user.id)
    assert fetched.email == "alice@example.com"

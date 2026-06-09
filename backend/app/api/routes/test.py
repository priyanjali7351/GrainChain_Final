from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.test import TestUserCreate
from app.services.test_service import create_test_user

router = APIRouter(prefix="/test", tags=["Test"])

@router.post("/")
def create_user(data: TestUserCreate, db: Session = Depends(get_db)):
    return create_test_user(db, data.name)
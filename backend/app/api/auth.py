from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.auth import UserSignup, UserLogin, Token
from app.services.auth_service import signup, login

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/signup")
def register_user(
    user: UserSignup,
    db: Session = Depends(get_db)
):
    try:
        new_user = signup(db, user)
        return {
            "message": "User created successfully",
            "user_id": new_user.id
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=Token)
def login_user(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    try:
        return login(db, user)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
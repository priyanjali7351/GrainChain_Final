#signup page and login logic

from sqlalchemy.orm import Session

from app.database.models import User
from app.schemas.auth import UserSignup, UserLogin
from app.core.security import hash_password, verify_password, create_access_token


def signup(db: Session, user_data: UserSignup):
    existing_user = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )

    if existing_user:
        raise ValueError("Email already registered")

    new_user = User(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hash_password(user_data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login(db: Session, user_data: UserLogin) -> dict:
    user = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )

    if not user or not verify_password(user_data.password, user.hashed_password):
        raise ValueError("Invalid email or password")

    token = create_access_token( data={"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}
from sqlalchemy.orm import Session

from app.models.user import User
from app.auth.password import hash_password, verify_password
from app.auth.jwt_handler import create_access_token


def register_user(db: Session, name: str, email: str, password: str):

    existing = db.query(User).filter(User.email == email).first()

    if existing:
        return None

    user = User(
        name=name,
        email=email,
        password_hash=hash_password(password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def login_user(db: Session, email: str, password: str):

    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.password_hash):
        return None

    token = create_access_token(
        {
            "sub": str(user.id)
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": user
    }
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.models.base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    name = Column(String(100), nullable=False)

    email = Column(String(150), unique=True, nullable=False)

    password_hash = Column(String(255), nullable=False)

    google_id = Column(String(255), nullable=True)

    auth_provider = Column(String(30), default="local")

    profile_picture = Column(String(500), nullable=True)

    is_verified = Column(Boolean, default=False)

    is_active = Column(Boolean, default=True)

    last_login = Column(DateTime(timezone=True), nullable=True)

    conversations = relationship(
        "Conversation",
        back_populates="user",
        cascade="all, delete"
    )
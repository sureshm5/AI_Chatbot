from sqlalchemy import Column, String, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Conversation(BaseModel):

    __tablename__ = "conversations"

    user_id = Column(
        ForeignKey("users.id")
    )

    title = Column(
        String(255),
        default="New Chat"
    )

    model_used = Column(
        String(100),
        default="gpt-oss-20b"
    )

    provider = Column(
        String(50),
        default="openrouter"
    )

    summary = Column(
        Text,
        nullable=True
    )

    is_pinned = Column(
        Boolean,
        default=False
    )

    is_archived = Column(
        Boolean,
        default=False
    )

    user = relationship(
        "User",
        back_populates="conversations"
    )

    messages = relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete"
    )
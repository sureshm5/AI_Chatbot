from sqlalchemy import Column, String, Text, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Message(BaseModel):

    __tablename__ = "messages"

    conversation_id = Column(
        ForeignKey("conversations.id")
    )

    role = Column(
        String(20)
    )

    content = Column(
        Text
    )

    tokens_used = Column(
        Integer,
        default=0
    )

    cached = Column(
        Boolean,
        default=False
    )

    latency_ms = Column(
        Integer,
        default=0
    )

    conversation = relationship(
        "Conversation",
        back_populates="messages"
    )
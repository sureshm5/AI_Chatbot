from sqlalchemy import Column, String, ForeignKey

from app.models.base import BaseModel


class Document(BaseModel):

    __tablename__ = "documents"

    conversation_id = Column(
        ForeignKey("conversations.id")
    )

    filename = Column(String(255))

    filepath = Column(String(500))

    file_type = Column(String(50))

    status = Column(String(50))
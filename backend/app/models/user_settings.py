from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Float

from app.models.base import BaseModel


class UserSettings(BaseModel):

    __tablename__ = "user_settings"

    user_id = Column(
        ForeignKey("users.id")
    )

    theme = Column(
        String(20),
        default="dark"
    )

    preferred_model = Column(
        String(100),
        default="gpt-oss-20b"
    )

    temperature = Column(
        Float,
        default=0.7
    )

    max_tokens = Column(
        Integer,
        default=8192
    )

    voice_enabled = Column(
        Boolean,
        default=False
    )
from sqlalchemy.orm import Session

from app.models.message import Message


def get_messages(db: Session, conversation_id: int):

    return (
        db.query(Message)
        .filter(Message.conversation_id == conversation_id)
        .order_by(Message.created_at.asc())
        .all()
    )
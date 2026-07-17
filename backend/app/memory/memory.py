from sqlalchemy.orm import Session

from app.models.message import Message


def get_memory(

    db: Session,

    conversation_id: int,

    limit: int = 10

):

    messages = (

        db.query(Message)

        .filter(

            Message.conversation_id == conversation_id

        )

        .order_by(Message.id.desc())

        .limit(limit)

        .all()

    )

    messages.reverse()

    return messages
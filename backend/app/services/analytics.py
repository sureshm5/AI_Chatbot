from sqlalchemy.orm import Session

from app.models.message import Message


def get_stats(db: Session):

    messages = db.query(Message).all()

    total_tokens = sum(
        m.tokens_used
        for m in messages
    )

    avg_latency = 0

    if messages:

        avg_latency = sum(
            m.latency_ms
            for m in messages
        ) / len(messages)

    return {

        "messages": len(messages),

        "tokens": total_tokens,

        "avg_latency_ms": round(avg_latency, 2)

    }
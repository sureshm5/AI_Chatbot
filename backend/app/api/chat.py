from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import time

from app.database.database import get_db
from app.schemas.chat import ChatRequest
from app.llm.model_manager import chat
from app.models.conversation import Conversation
from app.models.message import Message
from app.orchestrator.orchestrator import process
from app.memory.memory import get_memory
from app.auth.dependencies import get_current_user


router = APIRouter()


@router.post("/chat")
async def chatbot(
    data: ChatRequest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    conversation = (
        db.query(Conversation)
        .filter(Conversation.id == data.conversation_id)
        .first()
    )

    if not conversation:
        return {"error": "Conversation not found"}

    # Save User Message
    user_message = Message(
        conversation_id=data.conversation_id,
        role="user",
        content=data.message
    )

    db.add(user_message)
    db.commit()

    # Auto title
    if conversation.title == "New Chat":
        conversation.title = " ".join(data.message.split()[:5])
        db.commit()

    # -------------------------
    # Measure AI latency
    # -------------------------

    start = time.perf_counter()

    memory = get_memory(

        db,

        data.conversation_id

    )

    history = ""

    for msg in memory:

        history += f"{msg.role}: {msg.content}\n"

    prompt = history + "\nuser: " + data.message

    answer = process(

        data.message,

        prompt

    )

    end = time.perf_counter()

    latency = int((end - start) * 1000)

    # Approx token estimation
    tokens = len(answer.split()) * 2

    ai_message = Message(
        conversation_id=data.conversation_id,
        role="assistant",
        content=answer,
        latency_ms=latency,
        tokens_used=tokens,
        cached=False
    )

    db.add(ai_message)
    db.commit()

    return {
        "response": answer,
        "latency_ms": latency,
        "tokens_used": tokens
    }
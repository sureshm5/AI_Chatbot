from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import Body
from app.services.conversation_service import rename_conversation
from app.database.database import get_db
from app.auth.dependencies import get_current_user
from app.services.conversation_service import delete_conversation

from app.services.conversation_service import (
    create_conversation,
    get_conversations,
)

from app.services.message_service import get_messages


router = APIRouter(
    prefix="/conversation",
    tags=["Conversation"]
)


@router.post("/")
def new_chat(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return create_conversation(
        db=db,
        user_id=int(current_user["sub"])
    )


@router.get("/")
def history(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return get_conversations(
        db=db,
        user_id=int(current_user["sub"])
    )


@router.get("/{conversation_id}")
def conversation_messages(
    conversation_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return get_messages(
        db,
        conversation_id
    )

@router.delete("/{conversation_id}")
def delete_chat(

    conversation_id: int,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)

):

    success = delete_conversation(

        db,

        conversation_id,

        int(current_user["sub"])

    )

    if not success:

        return {

            "error": "Conversation not found"

        }

    return {

        "message": "Conversation deleted"

    }

@router.put("/{conversation_id}")
def rename_chat(

    conversation_id: int,

    title: str = Body(embed=True),

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)

):

    convo = rename_conversation(

        db,

        conversation_id,

        int(current_user["sub"]),

        title

    )

    if not convo:

        return {

            "error":"Conversation not found"

        }

    return convo
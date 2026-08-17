from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.conversation import Conversation
from app.models.message import Message
from app.schemas.conversations import (
    ConversationDetail,
    ConversationSummary,
)


router = APIRouter(
    prefix="/api/v1/conversations",
    tags=["Conversations"],
)


# ---------------------------------------------------------
# GET /api/v1/conversations
# Get all conversations for the current development user
# ---------------------------------------------------------
@router.get(
    "",
    response_model=list[ConversationSummary],
)
def get_conversations(
    db: Session = Depends(get_db),
):
    statement = (
        select(Conversation)
        .where(Conversation.user_id == 1)
        .order_by(Conversation.created_at.desc())
    )

    conversations = db.scalars(statement).all()

    return conversations


# ---------------------------------------------------------
# GET /api/v1/conversations/{conversation_id}
# Get one conversation with all its messages
# ---------------------------------------------------------
@router.get(
    "/{conversation_id}",
    response_model=ConversationDetail,
)
def get_conversation(
    conversation_id: int,
    db: Session = Depends(get_db),
):
    # Find the conversation and make sure it belongs
    # to the current development user.
    conversation = db.scalar(
        select(Conversation).where(
            Conversation.id == conversation_id,
            Conversation.user_id == 1,
        )
    )

    # If the conversation doesn't exist, return 404.
    if conversation is None:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found",
        )

    # Get all messages belonging to this conversation.
    messages = db.scalars(
        select(Message)
        .where(Message.conversation_id == conversation_id)
        .order_by(Message.created_at.asc())
    ).all()

    # Return conversation information + messages.
    return {
        "id": conversation.id,
        "title": conversation.title,
        "created_at": conversation.created_at,
        "messages": messages,
    }
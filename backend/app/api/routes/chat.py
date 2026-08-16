from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.conversation_service import ConversationService
from app.services.ollama_service import OllamaService


router = APIRouter()

conversation_service = ConversationService()
llm_service = OllamaService()


SYSTEM_PROMPT = """
You are an AI Business Operations Copilot.

Your job is to help employees with business operations,
company information, planning, and productivity.

Be clear, professional, concise, and honest.

Do not claim to have performed an external action unless
the system actually executed the corresponding tool.
"""


@router.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
):
    user_id = 1

    if request.conversation_id is None:
        conversation = (
            conversation_service.create_conversation(
                db=db,
                user_id=user_id,
            )
        )

        conversation_id = conversation.id

    else:
        conversation_id = request.conversation_id

    conversation_service.add_message(
        db=db,
        conversation_id=conversation_id,
        role="user",
        content=request.message,
    )

    stored_messages = conversation_service.get_messages(
        db=db,
        conversation_id=conversation_id,
    )

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]

    messages.extend(
        {
            "role": message.role,
            "content": message.content,
        }
        for message in stored_messages
    )

    response = llm_service.chat(messages)

    conversation_service.add_message(
        db=db,
        conversation_id=conversation_id,
        role="assistant",
        content=response,
    )

    return ChatResponse(
        conversation_id=conversation_id,
        response=response,
    )
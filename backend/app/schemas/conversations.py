from datetime import datetime

from pydantic import BaseModel


class MessageResponse(BaseModel):
    id: int
    role: str
    content: str
    created_at: datetime


class ConversationSummary(BaseModel):
    id: int
    title: str | None
    created_at: datetime


class ConversationDetail(BaseModel):
    id: int
    title: str | None
    created_at: datetime
    messages: list[MessageResponse]
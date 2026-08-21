from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from app.config import settings
from app.models import (
    User,
    Conversation,
    Message,
)


engine = create_engine(settings.database_url)


with Session(engine) as db:

    # -------------------------------------------------
    # 1. Get an existing user
    # -------------------------------------------------

    user = db.scalar(
        select(User)
        .where(User.id == 1)
    )

    if user is None:
        print("User with ID 1 was not found.")
        raise SystemExit

    print("\nUSER")
    print("ID:", user.id)
    print("Email:", user.email)
    print("Name:", user.name)

    # -------------------------------------------------
    # 2. Test User -> Conversations
    # -------------------------------------------------

    print("\nCONVERSATIONS")

    for conversation in user.conversations:
        print(
            conversation.id,
            conversation.title,
        )

    # -------------------------------------------------
    # 3. Test Conversation -> Messages
    # -------------------------------------------------

    print("\nMESSAGES")

    for conversation in user.conversations:

        print(
            f"\nConversation {conversation.id}:"
        )

        for message in conversation.messages:

            print(
                f"  [{message.role}] {message.content}"
            )

    print("\nRelationship test completed successfully.")
    
    print("\nREVERSE RELATIONSHIP")

conversation = db.scalar(
    select(Conversation)
    .where(Conversation.id == 1)
)

if conversation:
    print(
        "Conversation belongs to:",
        conversation.user.name
    )
    
    print("\nMESSAGE → CONVERSATION")

message = db.scalar(
    select(Message)
    .where(Message.id == 1)
)

if message:
    print(
        "Message:",
        message.content
    )

    print(
        "Conversation:",
        message.conversation.title
    )
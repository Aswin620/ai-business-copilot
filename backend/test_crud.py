from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from app.config import settings
from app.models import User, Conversation, Message


engine = create_engine(settings.database_url)


with Session(engine) as db:

    print("\n========== CLEANUP OLD TEST DATA ==========")

    old_user = db.scalar(
        select(User).where(
            User.email == "crud-test@ai-business-copilot.local"
        )
    )

    if old_user:
        print(f"Found old test user: {old_user.id}")

        db.delete(old_user)
        db.commit()

        print("Old test user deleted.")

    else:
        print("No old test user found.")


    print("\n========== CREATE ==========")

    # -----------------------------------------
    # CREATE USER
    # -----------------------------------------

    user = User(
        email="crud-test@ai-business-copilot.local",
        name="CRUD Test User",
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    print(f"Created User: {user.id}")


    # -----------------------------------------
    # CREATE CONVERSATION
    # -----------------------------------------

    conversation = Conversation(
        user_id=user.id,
        title="CRUD Test Conversation",
    )

    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    print(f"Created Conversation: {conversation.id}")


    # -----------------------------------------
    # CREATE MESSAGE
    # -----------------------------------------

    message = Message(
        conversation_id=conversation.id,
        role="user",
        content="This is a CRUD test message.",
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    print(f"Created Message: {message.id}")


    print("\n========== READ ==========")

    # -----------------------------------------
    # READ USER
    # -----------------------------------------

    saved_user = db.scalar(
        select(User).where(
            User.id == user.id
        )
    )

    print(
        "User:",
        saved_user.name
    )


    # -----------------------------------------
    # READ CONVERSATION
    # -----------------------------------------

    saved_conversation = db.scalar(
        select(Conversation).where(
            Conversation.id == conversation.id
        )
    )

    print(
        "Conversation:",
        saved_conversation.title
    )


    # -----------------------------------------
    # READ MESSAGE
    # -----------------------------------------

    saved_message = db.scalar(
        select(Message).where(
            Message.id == message.id
        )
    )

    print(
        "Message:",
        saved_message.content
    )


    print("\n========== ORM RELATIONSHIPS ==========")

    # User → Conversations

    print(
        "User conversations:",
        len(saved_user.conversations)
    )


    # Conversation → User

    print(
        "Conversation user:",
        saved_conversation.user.name
    )


    # Conversation → Messages

    print(
        "Conversation messages:",
        len(saved_conversation.messages)
    )


    # Message → Conversation

    print(
        "Message conversation:",
        saved_message.conversation.title
    )


    print("\n========== UPDATE ==========")

    # -----------------------------------------
    # UPDATE USER
    # -----------------------------------------

    saved_user.name = "Updated CRUD Test User"

    db.commit()
    db.refresh(saved_user)

    print(
        "Updated user name:",
        saved_user.name
    )


    print("\n========== DELETE ==========")

    # -----------------------------------------
    # DELETE MESSAGE
    # -----------------------------------------

    db.delete(saved_message)
    db.commit()

    print(
        "Deleted message:",
        message.id
    )


    print("\n========== FINAL VERIFICATION ==========")

    deleted_message = db.scalar(
        select(Message).where(
            Message.id == message.id
        )
    )

    if deleted_message is None:
        print("Message successfully deleted.")

    else:
        print("ERROR: Message still exists.")


    print("\nCRUD TEST COMPLETED SUCCESSFULLY.")
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from app.config import settings
from app.models import User


engine = create_engine(settings.database_url)


with Session(engine) as db:

    print("Starting transaction...")

    user = User(
        email="rollback-test@ai-business-copilot.local",
        name="Rollback Test User",
    )

    db.add(user)

    print("User added to session.")
    print("User has NOT been committed yet.")

    db.rollback()

    print("Transaction rolled back.")

    result = db.scalar(
        select(User).where(
            User.email == "rollback-test@ai-business-copilot.local"
        )
    )

    if result is None:
        print("SUCCESS: User does not exist.")
        print("Rollback worked.")
    else:
        print("ERROR: User still exists.")
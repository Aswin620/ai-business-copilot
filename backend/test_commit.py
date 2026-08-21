from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from app.config import settings
from app.models import User


engine = create_engine(settings.database_url)


with Session(engine) as db:

    user = User(
        email="commit-test@ai-business-copilot.local",
        name="Commit Test User",
    )

    db.add(user)

    db.commit()
    db.refresh(user)

    print("User committed.")
    print("User ID:", user.id)

    result = db.scalar(
        select(User).where(
            User.email == "commit-test@ai-business-copilot.local"
        )
    )

    if result:
        print("SUCCESS: User exists in database.")
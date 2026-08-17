from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.config import settings
from app.models.user import User


engine = create_engine(settings.database_url)


with Session(engine) as db:
    user = User(
        email="dev@ai-business-copilot.local",
        name="Development User",
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    print(f"Created user with ID: {user.id}")
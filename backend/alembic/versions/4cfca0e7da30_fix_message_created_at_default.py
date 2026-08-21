"""fix message created_at default

Revision ID: 4cfca0e7da30
Revises: 069f592b1ad7
Create Date: 2026-08-21 14:00:00

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4cfca0e7da30"
down_revision: Union[str, Sequence[str], None] = "069f592b1ad7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Add PostgreSQL default to messages.created_at."""

    op.alter_column(
        "messages",
        "created_at",
        existing_type=sa.DateTime(),
        server_default=sa.text("now()"),
        existing_nullable=False,
    )


def downgrade() -> None:
    """Remove PostgreSQL default from messages.created_at."""

    op.alter_column(
        "messages",
        "created_at",
        existing_type=sa.DateTime(),
        server_default=None,
        existing_nullable=False,
    )
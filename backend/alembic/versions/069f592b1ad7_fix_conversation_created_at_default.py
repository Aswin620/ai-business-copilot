"""fix conversation created_at default

Revision ID: YOUR_REVISION_ID
Revises: 8ab8a8a441f9
Create Date: 2026-08-21

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "069f592b1ad7"
down_revision: Union[str, Sequence[str], None] = "8ab8a8a441f9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Add the missing PostgreSQL default."""

    op.alter_column(
        "conversations",
        "created_at",
        existing_type=sa.DateTime(),
        server_default=sa.text("now()"),
        existing_nullable=False,
    )


def downgrade() -> None:
    """Remove the PostgreSQL default."""

    op.alter_column(
        "conversations",
        "created_at",
        existing_type=sa.DateTime(),
        server_default=None,
        existing_nullable=False,
    )
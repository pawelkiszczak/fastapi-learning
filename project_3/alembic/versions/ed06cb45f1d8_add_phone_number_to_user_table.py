"""add phone number to user table

Revision ID: ed06cb45f1d8
Revises: b364ade8be4a
Create Date: 2025-12-19 20:50:59.167912

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ed06cb45f1d8'
down_revision: Union[str, Sequence[str], None] = 'b364ade8be4a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'users',
        sa.Column('phone_number', sa.String(), nullable=True)
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass

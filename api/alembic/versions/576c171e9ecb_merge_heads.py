"""Merge heads

Revision ID: 576c171e9ecb
Revises: 92143a972557, ac44af84f8a2
Create Date: 2025-06-16 20:04:29.315566

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '576c171e9ecb'
down_revision: Union[str, None] = ('92143a972557', 'ac44af84f8a2')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

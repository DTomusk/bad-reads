"""Merge multiple heads

Revision ID: 951617c2b17d
Revises: 92143a972557, ac44af84f8a2
Create Date: 2025-07-12 15:13:23.610873

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '951617c2b17d'
down_revision: Union[str, None] = ('92143a972557', 'ac44af84f8a2')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

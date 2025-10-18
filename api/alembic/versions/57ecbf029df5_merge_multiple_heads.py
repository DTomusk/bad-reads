"""Merge multiple heads

Revision ID: 57ecbf029df5
Revises: abf965563987, 576c171e9ecb
Create Date: 2025-10-18 21:00:46.020752

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '57ecbf029df5'
down_revision: Union[str, None] = ('abf965563987', '576c171e9ecb')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

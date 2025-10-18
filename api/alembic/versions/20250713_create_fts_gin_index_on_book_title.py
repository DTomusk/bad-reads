"""create fts gin index on book title

Revision ID: 7a0e2fa127ab
Revises: dbc0439ca2e9
Create Date: 2025-07-13 15:51:13.709388

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a0e2fa127ab'
down_revision: Union[str, None] = 'dbc0439ca2e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute(
        """
        CREATE INDEX book_title_fts_idx
        ON books
        USING gin(to_tsvector('english', title));
        """
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute(
        """
        DROP INDEX IF EXISTS book_title_fts_idx;
        """
    )

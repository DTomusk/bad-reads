"""enable pg_trgm and add gin index

Revision ID: 8938b1bc82db
Revises: 457b9205d425
Create Date: 2025-05-28 21:04:10.670624

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8938b1bc82db'
down_revision: Union[str, None] = '457b9205d425'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Enable the pg_trgm extension
    op.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm;")

    # Create a GIN index on books.title using pg_trgm
    op.execute("""
        CREATE INDEX IF NOT EXISTS ix_books_title_trgm
        ON books
        USING gin (title gin_trgm_ops);
    """)


def downgrade() -> None:
    # Drop the index on downgrade
    op.execute("DROP INDEX IF EXISTS ix_books_title_trgm;")
    
    # (Optional) Drop the extension if you want to fully revert
    op.execute("DROP EXTENSION IF EXISTS pg_trgm;")

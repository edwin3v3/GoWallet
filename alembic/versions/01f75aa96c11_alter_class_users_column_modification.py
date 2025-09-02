"""Alter Class Users: Column modification

Revision ID: 01f75aa96c11
Revises: 4419d026d918
Create Date: 2025-09-02 11:29:45.361126

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '01f75aa96c11'
down_revision: Union[str, None] = '4419d026d918'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

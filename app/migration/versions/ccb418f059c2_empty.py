# empty migration
"""empty

Revision ID: ccb418f059c2
Revises: b237f8818d68
Create Date: 2025-08-11 06:59:03.257883

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'ccb418f059c2'
down_revision: Union[str, Sequence[str], None] = 'b237f8818d68'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    pass


def downgrade():
    pass
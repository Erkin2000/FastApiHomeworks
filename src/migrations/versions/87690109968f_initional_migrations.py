"""initional_migrations

Revision ID: 87690109968f
Revises: 
Create Date: 2024-09-21 18:46:07.535055

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '87690109968f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('hotels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:

    op.drop_table('hotels')


"""create user table

Revision ID: 6790e0dce987
Revises: 
Create Date: 2024-12-05 14:47:50.718129

"""
from typing import Sequence, Union
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6790e0dce987'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(150), nullable=False),
        sa.Column('created_t', sa.DateTime(), default=datetime.now(), nullable=False),
    )

def downgrade() -> None:
    op.drop_table('user')

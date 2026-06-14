"""Initial tables

Revision ID: cba9974dc9b5
Revises: 
Create Date: 2026-06-14 06:01:43.998503

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cba9974dc9b5'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('accesses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('access_name', sa.String(length=20), nullable=False),
    sa.Column('resource_name', sa.String(length=20), nullable=False),
    sa.Column('credentials', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('resource_name')
    )
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group_name', sa.String(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('group_access',
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('access_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['access_id'], ['accesses.id'], ),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.PrimaryKeyConstraint('group_id', 'access_id')
    )
    op.create_table('group_forbidden_access',
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('access_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['access_id'], ['accesses.id'], ),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.PrimaryKeyConstraint('group_id', 'access_id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=15), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_accesses',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('access_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['access_id'], ['accesses.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'access_id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('user_accesses')
    op.drop_table('users')
    op.drop_table('group_forbidden_access')
    op.drop_table('group_access')
    op.drop_table('groups')
    op.drop_table('accesses')

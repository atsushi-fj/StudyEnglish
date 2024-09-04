"""Recreate initial migration

Revision ID: 86b1243b8daf
Revises: 
Create Date: 2024-08-22 12:20:25.387731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86b1243b8daf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('word',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('english', sa.String(length=140), nullable=True),
    sa.Column('japanese', sa.String(length=140), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['wordbook.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('word')
    # ### end Alembic commands ###

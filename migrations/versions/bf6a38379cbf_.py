"""empty message

Revision ID: bf6a38379cbf
Revises: 
Create Date: 2023-07-26 14:02:31.304378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf6a38379cbf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lessons',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.Column('lesson_date', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('members',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bookings',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('member', sa.UUID(), nullable=True),
    sa.Column('lesson', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['lesson'], ['lessons.id'], ),
    sa.ForeignKeyConstraint(['member'], ['members.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookings')
    op.drop_table('members')
    op.drop_table('lessons')
    # ### end Alembic commands ###
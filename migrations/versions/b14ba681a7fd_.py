"""empty message

Revision ID: b14ba681a7fd
Revises: 30a833e98c31
Create Date: 2021-06-24 14:07:17.748667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b14ba681a7fd'
down_revision = '30a833e98c31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('year', sa.String(length=150), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('designer', sa.String(length=150), nullable=True),
    sa.Column('genre', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game')
    # ### end Alembic commands ###
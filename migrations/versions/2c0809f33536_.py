"""empty message

Revision ID: 2c0809f33536
Revises: 3583e792f74d
Create Date: 2021-06-21 14:18:32.158271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c0809f33536'
down_revision = '3583e792f74d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('year_published', sa.String(length=150), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('designer_name', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game')
    # ### end Alembic commands ###
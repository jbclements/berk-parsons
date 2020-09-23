"""add treatment col

Revision ID: c795ee8630cd
Revises: 68347a5650d2
Create Date: 2019-02-03 18:31:31.538302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c795ee8630cd'
down_revision = '68347a5650d2'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('treatment', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'treatment')
    # ### end Alembic commands ###


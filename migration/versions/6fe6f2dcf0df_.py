"""empty message

Revision ID: 6fe6f2dcf0df
Revises: 
Create Date: 2022-03-23 03:02:40.908172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fe6f2dcf0df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('new_table',
    sa.Column('id_operator', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('operator', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('number1', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('number2', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('id_result', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('result', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='new_table_pkey'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('new_table')
    # ### end Alembic commands ###

"""Initial Migration

Revision ID: 1aee3cc2ff97
Revises: 
Create Date: 2023-03-28 17:05:33.627856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1aee3cc2ff97'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trip_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('start_date', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('start_time', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trip_table', schema=None) as batch_op:
        batch_op.drop_column('start_time')
        batch_op.drop_column('start_date')

    # ### end Alembic commands ###

"""Initial Migration

Revision ID: b28ece0c2a45
Revises: 
Create Date: 2024-09-01 18:02:54.457151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b28ece0c2a45'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.String(length=150), nullable=True))
        batch_op.drop_column('firstName')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('firstName', sa.VARCHAR(length=150), nullable=True))
        batch_op.drop_column('first_name')

    # ### end Alembic commands ###

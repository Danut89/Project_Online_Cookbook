"""Add is_admin field to User

Revision ID: 94ed09f7a133
Revises: caf1a7a5780b
Create Date: 2025-03-24 20:12:23.195126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94ed09f7a133'
down_revision = 'caf1a7a5780b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_admin')

    # ### end Alembic commands ###

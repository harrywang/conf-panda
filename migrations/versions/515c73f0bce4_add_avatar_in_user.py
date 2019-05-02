"""add avatar in user

Revision ID: 515c73f0bce4
Revises: 4b6909ef6e08
Create Date: 2017-10-13 19:29:35.145905

"""

# revision identifiers, used by Alembic.
revision = '515c73f0bce4'
down_revision = '4b6909ef6e08'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('avatar', sa.Text(), nullable=True))

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('avatar')

    ### end Alembic commands ###
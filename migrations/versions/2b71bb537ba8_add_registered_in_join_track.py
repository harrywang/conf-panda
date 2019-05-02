"""add registered in join_track

Revision ID: 2b71bb537ba8
Revises: 4ed839b92a24
Create Date: 2016-07-27 13:17:40.619350

"""

# revision identifiers, used by Alembic.
revision = '2b71bb537ba8'
down_revision = '4ed839b92a24'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('track_user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('registered', sa.Boolean(), nullable=True))

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('track_user', schema=None) as batch_op:
        batch_op.drop_column('registered')

    ### end Alembic commands ###
